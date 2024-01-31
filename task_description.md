# Future Audiences Takehome Assignment

## Problem description

Design and implement a python-based API to produce a Google-like short description of a person. As a bonus, implement a simple javascript-based UI to demonstrate the API.

Example: When you google “yoshua bengio”, you get “Canadian computer scientist” in the short description as shown in [this result](https://www.google.com/search?q=yoshua+bengio):

![Yoshua Bengio Short Description](yoshua_bengio.png)

Your API will return a short text description similar to "Candian computer scientist" for input "yoshua bengio" but based on Wikipedia content.

For the bonus task: your UI will have a text box where the user can enter the name of the person and a button to submit the request. On clicking the button, the UI will call your API and display the result.

## Instructions

### Data source

Your source is the English wikipedia page content of the person being asked. For this, you will use the [mediawiki API](https://www.mediawiki.org/wiki/API:Get_the_contents_of_a_page).

Example : Try the following query for Yoshua Bengio:

```sh
curl https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Yoshua_Bengio&rvlimit=1&formatversion=2&format=json&rvprop=content
```

You will get a json output which is seen [here](api_result.json). You will notice `{{Short description|Canadian computer scientist}}` in the content value. You can use this query as a template and replace titles with the appropriate input that your API gets.

### Deliverables

#### Code

You will have 48 hours to submit the assignment, but please spend no more than **90 minutes** on your solution. This may sound like not much time, but we expect this team to be prototyping many possible tools, so quick but functional apps will be a common ask.

Please provide your functioning code in a zipped github repo. One should be able to run your API server locally and try out with some inputs via `curl`.

#### Questions

Please answer the following questions in a file called `questions.md` in the root of your repo:

1. Design and provide the input and output schema for your API. Some things to consider:
   1. How will the schema take into consideration if the person being provided is not on English wikipedia?
   2. How will you account for missing “short description” in content?
2. Consider this hypothetical scenario: Your API is going to be deployed and made available to the public for use. What things could you do to keep this API service highly available and reliable? (Think of as many issues as come to your mind and propose your potential solutions. No code is required for this)
3. What tradeoffs did you pursue in order to stay within the 90 minute limit?
4. What additional changes would you have made had you had more time?
5. How and where did you use AI coding assistants? What did you like about them? What did you dislike about them?
6. What enhancements would you make to the UI if you had more time?

### Additional parameters

- Please make use of Python, and if appropriate javascript in your solution.
- Minimally use external libraries and frameworks
- AI coding assistants are permitted, but please note in your solution where you have done so and be prepared to discuss any code in a follow-up interview.
