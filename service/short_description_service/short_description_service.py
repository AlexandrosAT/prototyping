from flask import Flask, request, jsonify
import requests
import re
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EXTERNAL_API_URL = "https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvlimit=1&formatversion=2&format=json&rvprop=content"
SHORT_DESCRIPTION_PATTERN = r"\{\{Short description\|([^}]*)\}\}"
REDIRECT_PATTERN = r"#REDIRECT"
REDIRECT_CONTENT_PATTERN = r"\[\[([^}]*)\]\]"


def get_short_description_from_wiki_api(query):
    try:
        response = requests.get(EXTERNAL_API_URL, params={"titles": query})
        response.raise_for_status()  # Raise an HTTPError for bad responses

        data = response.json()
        pages = data.get("query", {}).get("pages", [{}])[0]

        # Check if query is not found in Wikipedia
        missing = pages.get("missing") 
        if missing == True:
            raise ValueError("Queried content not found in Wikipedia")

        content = pages.get("revisions", [{}])[0].get("content", "")

        # Check if we receive redirection from Wikipedia
        redirect = re.findall(REDIRECT_PATTERN, content)
        if len(redirect) != 0:
            redirect_to = re.findall(REDIRECT_CONTENT_PATTERN, content)
            raise ValueError(f"Query redirected to: {redirect_to}")

        short_description = re.findall(SHORT_DESCRIPTION_PATTERN, content)
        if len(short_description) == 0:
            raise ValueError(f"No short description found for '{query}'")
        return short_description[0]

    except requests.exceptions.RequestException as req_err:
        raise Exception(f"External API request failed: {req_err}")

    except ValueError as value_err:
        raise Exception(f"{value_err}")


@app.route("/v1/get-content", methods=["GET"])
def get_content():
    query = request.args.get("query")
    if query is None:
        return jsonify({"error": "Missing query parameter"}), 400

    try:
        content = get_short_description_from_wiki_api(query)
        return jsonify({"short_description": content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
