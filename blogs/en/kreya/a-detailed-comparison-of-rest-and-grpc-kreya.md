---
title: 'A detailed comparison of REST and gRPC | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/rest-vs-grpc/'
original_language: en
published: 2023-04-26
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7ec236b51d97d453'
translated: false
---

> 原文：[A detailed comparison of REST and gRPC | Kreya](https://kreya.app/blog/rest-vs-grpc/)　·　Kreya Blog

For a long time, REST was the one and only "standard" for building APIs. It kind of replaced SOAP, which was an ugly mess of "too much XML". But in recent years, new alternatives have emerged. In 2015, Facebook released GraphQL to the public, and in 2016 Google followed suit with the release of [gRPC](https://grpc.io/). In this article, we are going to focus on the latter and compare it with REST, which is still widely used.

![REST vs gRPC thumbnail](https://kreya.app/thumbnails/rest-vs-grpc.png)

## Overview

The following table will give you an overview of the discussed points and shows where REST and gRPC really shine.

| Topic | REST | gRPC |
|---|---|---|
| [Standardization](#standardization) | No standard | Well defined |
| [Paradigm](#fundamental-differences) | Resource based | RPC |
| [Service modes](#service-modes) | Only unary | Unary, client streaming, server streaming and bidirectional streaming |
| [Requirements](#requirements) | Any HTTP version, JSON parser | HTTP/2, gRPC implementation for language |
| [API design](#api-design) | Code first | Design first |
| [Default data format](#data-format) | JSON | Protobuf |
| [Web browser support](#browser-compatibility) | Native | gRPC web, via workarounds |
| [Tools](#tooling) | More established tools | Language support varies, some with excellent implementations |

## Standardization

One of the disadvantages of REST is the lack of standardization. REST is more of a paradigm than an API standard and many folks mean different things when talking about it. For most, the term "REST API" is used for HTTP-based JSON APIs. For others, REST is used interchangeably with certain specifications such as [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) or [JSON:API](https://jsonapi.org/). But using XML instead of JSON would still make an API RESTful, even though that is not widely understood. The term REST is not even tied to HTTP. This can result in a lot of confusion when working with REST APIs. For example, consumers may automatically expect idempotency or cacheability of certain REST API endpoints, even though that is not defined explicitly.

In comparison, gRPC is well defined. For example, the [gRPC implementation over HTTP/2](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md) is pretty detailed.

## Fundamental differences

The paradigms of REST and gRPC are not the same.

With REST, everything centers around resources, which can be retrieved and manipulated. If we take a book as an example resource, a REST API will typically provide the following endpoints:

- `GET /books` (fetch all books, most likely with parameters to filter and page the results)
- `GET /books/{id}` (fetch a specific book)
- `POST /books` (create a book)
- `DELETE /books/{id}` (delete a book)

and so on. Most HTTP-based REST APIs follow this pattern. While this works well, certain cases are difficult to represent as a REST API. For example, what if I want to create multiple books and do not want to call `POST /books` repeatedly for each book (for performance, idempotency or whatever reason)? Do I create a `POST /books/batch` endpoint? Is that still "RESTful"? While easy to solve technically, it often creates long discussions among developers.

gRPC on the other hand is an RPC framework. It centers around service methods. If we take the book API example, with gRPC we would create a `BookService` with the following methods:

- `GetBooks()`
- `GetBook()`
- `CreateBook()`
- `DeleteBook()`

We can name these methods however we like and require whatever parameters we need. If we now want to add a method to create multiple books, nothing stops us from adding a `CreateBooks()` method. gRPC offers more "freedom" when designing APIs, as there are less (self-imposed) restrictions.

### Service modes

gRPC supports four kind of service methods:

- **Unary:** Send a single request, receive a single response
- **Server streaming:** Send a single request, receive multiple responses
- **Client streaming:** Send multiple requests, receive a single response
- **Bidirectional streaming:** Send multiple requests, receive multiple reponses

This is a very nice advantage of gRPC in comparison to REST, which only supports unary requests. Supporting other service modes in REST APIs would require the usage of a different protocol such as server-sent events or websockets, which isn't quite "RESTful".

### Requirements

REST APIs often "just work" with any kind of HTTP version. As long as a programming language has an HTTP client and a library for JSON parsing, consuming REST APIs is a breeze.

gRPC explicitely needs HTTP/2 support, otherwise it will not work. In recent years, this has become less of a problem, as most proxies and frameworks have added support for HTTP/2.

As gRPC requires code generation (for creating clients or server stubs), only [a set of programming languages](https://grpc.io/docs/languages/) are supported.

## API design

A REST API is often the result of its implementation, dubbed "code-first." While it is possible to design the API with OpenAPI first and then generate a server stub, it is not an approach that many developers take. The OpenAPI definition is more likely generated from the API implementation, if there is an OpenAPI definition at all. As a result, the API definition is tightly coupled to the implementation. Changes in the wrong model/class can result in unintentional breaking changes of the API.

gRPC uses a different approach, where the API has to be defined before one can implement it (dubbed "design-first"). Clients and server stubs are then generated from this API definition. This requires some thinking ahead, as one cannot jump directly into implementing the API.

Both approaches have their pros and cons. The usual REST API approach allows quicker iteration, as the server is always the source of truth. With gRPC, it can be annoying to first change the API definition before being able to adjust the implementation. However, it brings some safety benefits by having the API explicitly defined.

## Data format

Both REST and gRPC can use different formats to transfer data. Most REST APIs use JSON, while gRPC uses [Protocol Buffers](https://protobuf.dev/) (Protobuf) by default, so we will compare these two.

JSON has limited support for data types and also has some quirks (ex. big numbers need to be represented as strings). It is a text format and human readable. Field names are serialized, which takes up some space. In some programming languages, this also requires the use of reflection to deserialize JSON messages, which is quite slow.

As written above, gRPC APIs and the respective message types are first defined as Protocol Buffers. Each message is strongly typed, may contain useful comments and has lots of other interesting features. For the supported list of programming languages, code to (de-)serialize messages can be automatically generated. As it is a binary format and does not serialize the field names, it uses less space than an equivalent JSON message. This does have the drawback that it is no longer human readable and requires the Protobuf definition to deserialize messages, which can hamper the developer experience.

The following JSON example would take up roughly 66 bytes (with whitespace removed).

```json
{  "persons": [    {      "name": "Max",      "age": 23    },    {      "name": "Mike",      "age": 52    }  ]}
```

An equivalent serialized protobuf message would only use 19 bytes.

```text
0x0A070A034D617810170A080A0448616E731034
```

### Large messages

Protobuf is designed to serialize and deserialize messages in-memory. As a result, transferring huge messages with Protobuf/gRPC is not recommended. Most gRPC implementation place a default limit of 4 MB on individual messages.

Handling large data sizes with REST APIs, such as file uploads, is rather straight forward. The received file can be treated as a stream, using very little memory. This is not impossible with gRPC, but needs more manual effort. The file would have to be chunked into several parts on the sender side. Each chunk would then be sent as an individual message via a client-streaming method to the server. The server receives each chunk and can construct a data stream from it, resulting in a similar behaviour to the REST API, although with more effort.

## Browser compatibility

This is where REST really shines. It is supported natively by web browsers, making it effortless to consume REST APIs from web applications.

gRPC is not directly supported by browsers, as it requires explicit HTTP/2 support and access to certain HTTP/2 features, which web browsers do not provide. As a workaround, [gRPC Web](https://github.com/grpc/grpc-web) can be used. It is a slight variation of the gRPC protocol to make it consumable by web browsers. For some programming languages, gRPC Web support is already included in the framework. For others, a proxy is needed to translate gRPC traffic into gRPC Web traffic and vice versa. In comparison to REST APIs, which require no dependencies, gRPC APIs are more cumbersome to consume from the web.

A workaround could be to use [JSON transcoding](https://cloud.google.com/endpoints/docs/grpc/transcoding), which allows developers to expose a gRPC API as a REST API.

## Tooling

gRPC and REST tooling varies heavily between programming languages and frameworks. In some, gRPC feels more "native" while in others, the REST tooling is much more advanced.

Proper language support for gRPC matters a lot more, since it requires tooling to generate clients and server stubs. For non-supported programming, you are out of luck. Clients for REST APIs can always be created manually, but this may take some effort. While tools to create REST clients from OpenAPI definitions exist, their developer experience is often lackluster in comparison to the gRPC equivalent.

Since REST APIs have been around for much longer, more tools that help build, test and deploy REST APIs exist. Their functionality is often more advanced than that of gRPC tools. This is also one of the main reasons why we built [Kreya](https://kreya.app), which tries to be the best gRPC GUI client (while also supporting REST).

## Conclusion

REST and gRPC both have their advantages and disadvantages.

Consuming REST APIs from web apps is generally easier. REST is also more widely used, making it simpler to use for some developers, as they may not know about gRPC.

In my opinion, gRPC definitely has advantages in server-to-server communications (ex. between microservices). The ability to share the exact API definition and to create API clients in multiple programming languages is a huge win.

There is no definitive answer to "Should we use REST or gRPC?". Some APIs could have unique use cases for which gRPC or REST may prove a better fit. Or developers could simply be more comfortable or experienced with either REST or gRPC. All these reasons are fine. In the end, everyone has to decide for themselves which technology to use.
