---
title: 'Testing APIs with Kreya | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/testing-apis-with-kreya/'
original_language: en
published: 2023-08-16
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bce5917ce8e40444'
translated: false
---

> 原文：[Testing APIs with Kreya | Kreya](https://kreya.app/blog/testing-apis-with-kreya/)　·　Kreya Blog

Do you have a legacy API without any tests? Multiple APIs written in different languages? Or a Q&A team that wants to test all APIs with the same powerful tool? Then Kreya is the perfect solution for you!

Testing APIs with Kreya has its advantages. You can test your API both manually (e.g. during development) and in an automated way. Learn more about testing with Kreya in this article.

## About Kreya

Kreya at its core is a simple tool for calling APIs, but it also includes powerful features that make calling and testing APIs easier.

For example, you can import APIs via OpenAPI/Swagger, gRPC server reflection or protobuf files. This will create a Kreya operation for each API method. Note that this is not a one-time action: When a new API method is added, users can simply refresh the API importer and the new method will be added to the existing ones.

Other notable features include centralized authentication management, environments & templating, file-based storage, and more!

## Manual testing and verification

Most users start by manually invoking Kreya operations and checking the response. As seen in the screenshot below, this works pretty well, especially if one is unfamiliar with the API or during development.

But what if we want to continuously test that the API behaves a certain way? Invoking the operation and manually verifying the response becomes a chore.

## Automated testing

The solution to this problem is to automate the API tests. For this use case, Kreya provides the [Scripting feature](https://kreya.app/docs/scripting-and-tests/). Scripting allows you to define tests in JavaScript, which are run automatically each time the operation is invoked. It is also possible to store data as [user variables](https://kreya.app/docs/scripting-and-tests/#user-variables), which can then be reused in other operations.

info

Scripting is only available in the Pro plan. [Start the 10-day trial](https://kreya.app/pricing/) to explore this feature!

### Testing a REST API

Let's see what testing a simple REST API in Kreya would look like. We will use the [Kreya example project](https://github.com/riok/Kreya/tree/master/example-project) as an example.

First, we test the `POST /v1/books` endpoint to create a book by sending the following JSON content:

```json
{  "name": "The Great Gatsby"}
```

And as Script, we define the following:

```javascript
// chai comes bundled with Kreya, no need to install it yourselfimport { expect } from 'chai';// Code here runs before the request is sentconst expectedBookName = 'The Great Gatsby';// Add a callback function for when the REST call completeskreya.rest.onCallCompleted(call => {  // kreya.trace is similar to console.log, the output is visible in the Trace tab  kreya.trace('The REST call completed.');  // This is how you define test cases in Kreya  kreya.test('Status code should be 200', () => expect(call.status.code).to.equal(200));  kreya.test('Content type should be JSON', () => expect(call.response.contentType).to.eq('application/json'));  const book = call.response.content;  kreya.test('Book should have correct name', () => expect(book.name).to.eq(expectedBookName));  // Store the created book ID to reuse it later  kreya.variables.set('book_id', book.id);});
```

When the operation is sent, the test results are displayed:

Notice how we stored the `book_id` user variable. We can use that to delete the book again. It is available through [Templating](https://kreya.app/docs/templating/) as `{{ vars.book_id }}`:

### Testing a gRPC API

Testing gRPC APIs is very similar to testing REST APIs. We'll use the "Advanced scripting example" operation from the example project. It calls a gRPC duplex streaming (multiple requests and responses) operation and contains three requests like this:

```json
{  "message": "{{ vars.messages ? vars.messages[0] : 'no messages set' }}"}
```

If the `messages` user variable is set, it sends each message in a separate request. This means we have to define the `messages` user variable before the operation is sent, which we do in the Script:

```javascript
import { expect } from 'chai';// Code here runs before the request is sentconst messages = ['first message', 'second message', 'third message'];kreya.variables.set('messages', messages);// May be invoked multiple times, as gRPC calls may have multiple responseskreya.grpc.onResponse(response => {  kreya.test('Should equal the sent message', () => expect(response.content.message).to.eql(messages[response.index]));});// Invoked only once, when the gRPC call finally completeskreya.grpc.onCallCompleted(call => {  kreya.test('Status should be ok', () => expect(call.status.code).to.equal(0));  kreya.trace(`Got ${call.responseCount} responses`);  kreya.test('Response count should match sent messages', () =>    // Intentionally wrong to show how failed tests are displayed    expect(call.responseCount).to.eql(messages.length - 1),  );});
```

Note that the Script is slightly changed from the one in the example project to show how test failures are being displayed:

### Integrate into CI/CD pipeline

Adding scripts and tests is all fine and good, but we would still have to manually invoke the operations to see the test results. It would be much better to integrate this into a CI/CD pipeline to be able to run tests continuously.

For this, the ["kreyac CLI"](https://kreya.app/docs/cli/) can be used. And because Kreya stores the project data as simple text files, this can be easily stored in a git repository. This is exactly what we do with the Kreya example project, which contains a [GitHub action](https://github.com/riok/Kreya/blob/master/.github/workflows/test.yml). It simply invokes some kreyac commands:

```shell
kreyac info # just for debugging purposes: show basic information about kreyac and the projectkreyac environment list # just for debugging purposes: show the environments of the Kreya projectkreyac environment set-active Production # always set the active environment before invoking operations to make sure that the correct one is activekreyac operation invoke "REST/Get books.krop" # Invoke a single REST operation.kreyac operation invoke "gRPC/Say hello (unary call).krop" # Invoke a single gRPC operation.kreyac operation invoke "Kreya features/Scripting/**" # Invoke all scripting operations. Also runs the tests defined via Scripting. The command would exit with a non-successful code if a test fails.
```

Which generates the following output:

## Closing

That's all you need to know to start testing APIs with Kreya! For further information, you can find the complete [Scripting documentation in our docs](https://kreya.app/docs/scripting-and-tests/).

Do you feel something is missing or could be improved? Do not hesitate to contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#b3dbd6dfdfdcf3d8c1d6cad29dd2c3c3).
