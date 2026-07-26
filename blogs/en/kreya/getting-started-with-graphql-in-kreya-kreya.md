---
title: 'Getting Started with GraphQL in Kreya | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/getting-started-with-graphql/'
original_language: en
published: 2026-03-30
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c2b99108bedc5ffd'
translated: false
---

> 原文：[Getting Started with GraphQL in Kreya | Kreya](https://kreya.app/blog/getting-started-with-graphql/)　·　Kreya Blog

With the release of Kreya [v1.19.0](https://kreya.app/docs/release-notes/#119020260225) support for GraphQL was added. This guide will walk you through setting up your first GraphQL operation, from schema import to automated testing.

## What is GraphQL?

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. GraphQL provides a complete and understandable description of the data in your API, gives clients the power to ask for exactly what they need and nothing more, and makes it easier to evolve APIs over time.

More information and detailed examples about GraphQL can be found on the [official website](https://graphql.org/).

## Importing a GraphQL schema

To call GraphQL APIs, using importers is optional. However, using a schema importer has a lot of advantages. For example, it provides autocompletion for your requests and scripting types and validates your queries.

You have three possibilities to import a GraphQL schema in Kreya:

- **Local File**: Import existing `.graphql` or `.gql` files directly.
- **Schema URL**: Link to a hosted static schema definition.
- **Introspection**: Query a running server to dynamically fetch its current schema, this is perfect for rapidly evolving APIs.

Select your preferred option in the **Importers** tab.

If you don't currently have a schema, you can use the schema introspection from our Kreya example GraphQL server. `https://example-api.kreya.app/graphql`

## Creating and sending a GraphQL operation

To create a new GraphQL operation, click the  icon in the operations list and select `GraphQL`. Next, choose a descriptive name for your operation and hit enter.

If you defined a schema importer in the previous step, you can select it from the header. If you only have one importer, it will be selected automatically.

After that, you need to define the endpoint in the **Settings** tab.

The Kreya example GraphQL endpoint is also available for use here. `https://example-api.kreya.app/graphql`

Finally, define your query in the **Request** tab.

```graphql
query {  books {    id    name  }}
```

This is a classic GraphQL query. It requests a specific list of resources `books` and only the pieces of data (`id` and `name`) needed for the UI. This is one of the major advantages of GraphQL: with a REST API, you might hit an endpoint such as `/api/books` and receive 50 fields (author, publication date, ISBN, etc.), even if you only require the names.

## Define variables

Using variables allows you to separate your query logic from your test data. You can specify a variable in the **Variables** tab at the bottom of the request editor.

```json
{  "bookId": 3}
```

This variable can then be reused in the query itself using the prefix `$`, e.g. `$bookId`.

```graphql
query getBook($bookId: Int = 1) {  book(id: $bookId) {    id    name  }}
```

## Testing your GraphQL API [Pro / Enterprise](https://kreya.app/pricing/)

Similar to gRPC, REST, and WebSocket operations, the **Script** tab allows you to perform functional testing on your GraphQL API. An example of some basic tests, include verifying status codes, response shapes, and specific data values.

```javascript
import { expect } from 'chai';kreya.graphql.onQueryCompleted(call => {  kreya.trace('The GraphQL query completed.');  kreya.test('Status code', () => expect(call.status.code).to.equal(200));  kreya.test('status is success', () => expect(call.status.isSuccess).to.be.true);  kreya.test('Book name', () => expect(call.response.content.data.book.name).to.eq("Harry Potter and the Philosopher's Stone"));});
```

More scripting hooks such as `kreya.graphql.onMutationCompleted` and `kreya.graphql.onSubscriptionCompleted` can be found in the [documentation](https://kreya.app/docs/scripting-and-tests/operation-scripts/graphql-script-api-reference/).

Another way to test your API is to use snapshot tests. You can enable snapshot testing via the **Settings** tab.

A detailed description of how to use Snapshot Testing can also be found in the [documentation](https://kreya.app/docs/scripting-and-tests/tests/snapshot-testing/).

## Conclusion

That's it! You just sent your first GraphQL operation with Kreya!

Have fun exploring the world of GraphQL! If you have any questions or suggestions on how we can improve its use in Kreya, please [contact us](https://kreya.app/cdn-cgi/l/email-protection#6a020f0606052a01180f130b440b1a1a) or [report an issue](https://github.com/riok/Kreya/issues/new/choose).
