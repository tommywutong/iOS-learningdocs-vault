---
title: 'gRPC - Best Practices | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/grpc-best-practices/'
original_language: en
published: 2021-12-15
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e58a1af204f49a93'
translated: false
---

> 原文：[gRPC - Best Practices | Kreya](https://kreya.app/blog/grpc-best-practices/)　·　Kreya Blog

Creating and using gRPC services is pretty easy. However, there are a few gotchas and best practices that should be known to all. For example, do you know the default message size limit? Or do you know that protobuf supports optional fields since v3.15? Or that enum names should be unique inside a protobuf package?

If you don't know the answers to these questions, then this blog post is exactly for you.

## Designing gRPC services

Designing gRPC services is different from designing REST services, where the API contract (ex. OpenAPI) is often generated from the server implementation. With gRPC, it's the other way around. The API contract is first defined in protobuf, then the client and server stubs are generated from that API definition. In this section, we explain some of the best practices when designing gRPC APIs.

### Style guide

If you follow the [protobuf style guide](https://developers.google.com/protocol-buffers/docs/style), you already are doing great! Following the style guide ensures that code generators can transform your definitions correctly into the language specific naming convention. For example, the following protobuf message

```protobuf
message Book {  string name = 1;}
```

will be converted to this Java code

```java
public String getName() { ... }public Builder setName(String v) { ... }
```

while it would look something like this in C#

```csharp
public String Name { get; set; }
```

Enforcing the style guide is best done via a linter, ex. with [protolint](https://github.com/yoheimuta/protolint).

### Separate request and response messages

Another topic that often comes up is separate request and response messages. We recommend that you create a separate message for each request and response. Name them `{MethodName}Request` and `{MethodName}Reponse`. This allows you to modify request and response messages for a single service method without introducing accidental changes to other methods. It is tempting to re-use messages and simply ignoring fields that aren't needed. With time, this will result in a mess, since it isn't obvious what the API expects. Exceptions to this rule are usually made when returning a single, well-defined entity or when returning an empty message.

```protobuf
service BookService {  rpc CreateBook(Book) returns (Book); // don't do this  rpc ListBooks(ListBooksRequest) returns (ListBooksResponse); // this is OK  rpc GetBook(GetBookRequest) returns (Book); // this is also OK  rpc DeleteBook(DeleteBookRequest) returns (google.protobuf.Empty); // this is also OK}
```

The empty message is already defined as `google.protobuf.Empty`, so it doesn't make sense to define yet another empty message. An argument could be made that using an empty `DeleteBookResponse` message would be better in this case, since then one can add fields to that message in the future. While this is true, chances are that you are never going to add a field to that message. Nevertheless, it can be a valid strategy. Just be consistent, do not mix these two approaches.

A similar argument can be made for returning single entities. Defining a `GetBookResponse` message would be perfectly valid, it is just not recommended to do so. Again, consistency is key.

### Enums

Enums can be annoying to use in gRPC. Consider the following example

```protobuf
enum Genre {  HORROR = 0;  FANTASY = 1;  ROMANCE = 2;}
```

This is a valid protobuf enum, but it has several drawbacks. For once, it is recommended to define the first entry of the enum as `ENUM_NAME_UNSPECIFIED` and assign it the 0 value. This defines it as the default enum entry and will always be set if no other value was set. If we do not specify this default entry, we cannot differentiate between the default value and no value ([prior to protobuf v3.15](#optional-fields)). An exception to this rule is made when there is already a useful default entry in the enum, then that is used instead.

Another gotcha is that names of enum entries must be unique in the whole package. Defining a completely unrelated enum with the entry `ROMANCE` will result in an error message because of how enums in C and C++ are implemented. To avoid this, it can be useful to prefix the enum entries with the enum name. Some code generators (ex. for C#) will remove these prefixes automatically, so that the resulting code looks "clean" again. If you do not have any duplicated enum names, you can omit the prefix, but it should be done consistently.

As a result, a better enum definition would look like this:

```protobuf
enum Genre {  GENRE_UNSPECIFIED = 0;  GENRE_HORROR = 1;  GENRE_FANTASY = 2;  GENRE_ROMANCE = 3;}
```

### Well known types

A mistake a lot of new gRPC users make is to overlook the [well known types](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf). These message types are available by default in addition to the scalar value types (string, float, ...). For example, instead of defining your of timestamp message type, use the well known Timestamp type:

```protobuf
import "google/protobuf/timestamp.proto";message Book {  google.protobuf.Timestamp creation_time = 1;}
```

### Versioning and breaking changes

The gRPC protocol is designed to support many changes without breaking existing consumers. For example, these changes are non-breaking:

- Adding a field to a message

    - The default value will be set when the field isn't sent
- Renaming a field or message *

    - Field names aren't serialized, only the field numbers
- Deleting a field *

    - Older clients still "receive" the default value
    - Remember to mark removed fields as reserved, ex. `reserved 2;` so that they won't be reused in the future
- Adding a value to an enum
- Adding a new message
- Adding a method to an existing service
- Adding a new service

* _These changes do not result in a breaking change of the gRPC protocol, but when updating to the new version, clients may need to adjust their code._

Other changes, such as changing a field number or removing a service method, are breaking. Note that changing the data type of a field can be non-breaking, depending on the data types used. [For more information, visit the proto3 documentation](https://developers.google.com/protocol-buffers/docs/proto3#updating).

To allow breaking changes in the future, the gRPC naming convention suggests to use the version number as the last part of the package name, for example:

```protobuf
package app.kreya.v1;
```

When introducing a breaking change, a new package with a new version number should be created. The old package should be kept around as long as needed.

### Optional fields

Consider the following proto3 message which defines the field `bar`:

```protobuf
message Foo {  int32 bar = 1;}
```

With this definition, it is impossible to check whether `bar` has been set to 0 or if no value has been set, since the default value of `int32` fields is 0. Prior to protobuf v3.15, this would be solved by using a wrapper type:

```protobuf
import "google/protobuf/wrappers.proto";message Foo {  google.protobuf.Int32Value bar = 1;}
```

Since the data type of the `bar` field is now a message type, it can be nullable and we are able to check whether "nothing" or 0 was set.

Starting with protobuf v3.15 (or v3.12 via the `--experimental_allow_proto3_optional` flag), [field presence tracking](https://github.com/protocolbuffers/protobuf/blob/master/docs/field_presence.md) via the `optional` keyword is supported:

```protobuf
message Foo {  optional int32 bar = 1;}
```

This exposes `hasBar()` and `clearBar()` (depending on the language) methods in the generated code.

### Oneof

Oneof is a wonderful example where a protobuf language feature helps to make gRPC APIs more intuitive. As an example, imagine we have a service method where users are able to change their profile picture, either from an URL or by uploading their own (small) image. Instead of doing this

```protobuf
// Either set image_url or image_data. Setting both will result in an error.message ChangeProfilePictureRequest {  string image_url = 1;  bytes image_data = 2;}
```

we can define the desired behaviour directly into the message with oneof

```protobuf
message ChangeProfilePictureRequest {  oneof image {    string url = 1;    bytes data = 2;  }}
```

Not only is that much clearer for API consumers, it is also easier to check which field has been set in the generated code. Keep in mind that oneof also allows that none of the fields has been set, meaning there is no need to introduce a separate `none` field if the oneof should be optional.

### Abritary data

It may be tempting to serialize abritary data as JSON and send it as a string. However, that isn't very efficient. Protobuf provides two different messages types for arbritary data, depending on your use case. For example, if the JSON representation of your data looks something like this and you do not know the field names and types beforehand:

```json
{  "data": {    "some-value": 3    "some-other-value": "custom-string"    "some-array": [1, 2, 3],    "nested": {      "nested-string": "test"    }  ]}
```

it would be best to use a [Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct):

```protobuf
message StructTest {  google.protobuf.Struct data = 1;}
```

Should you need to send abritary protobuf messages and do not know their type, [Any](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#any) is the solution.

```protobuf
message LogEntry {  google.protobuf.Timestamp log_time = 1;  google.protobuf.Any log_message = 2; // Can be any protobuf message}
```

## Using gRPC

You finally designed your gRPC API, implemented a client and a server and deployed it to production. Now you are wondering if there are any gotchas when hosting or calling gRPC services. It turns out that there are a few, which we've listed below.

### Large messages

Since gRPC messages are loaded fully into memory, large messages should be avoided, especially in languages with a garbage collector. When implementing or consuming a gRPC service, the default message size limit of 4 MB should also be kept in mind. Even though this limit can be increased, in most cases it probably isn't a good idea as gRPC simply isn't designed for large messages.

If you have use cases where you need to send or receive large messages, consider using a separate HTTP endpoint. Another option would be to use gRPC streaming and split the large payload into several manageable chunks.

### Load balancing

Load balancing gRPC traffic isn't as easy as load balancing HTTP/1.1 traffic. With HTTP/1.1 traffic, load balancers can operate at the transport layer (L4) and simply distribute TCP connections across the endpoints. This isn't possible with gRPC, since it uses HTTP/2, which in turn uses a single TCP connection for all calls. To achieve transparent load balancing with gRPC, load balancers need to operate at the application layer (L7), which may impact performance negatively.

Another approach would be to use client-side load balancing, where clients store (or retrieve) a list of all available gRPC endoints. For each call, the client then selects a different endpoint to use. This results in a better performance, since no load balancer proxy is involved, but may be more difficult to implement, since all clients need to know the list of available endpoints (and create a channel for each endpoint).

### Reuse channels

Creating a gRPC channel is costly process, as it creates a new HTTP/2 connection. A channel should be reused whenever possible. Consult the documentation of the gRPC implementation of your language whether the channel is safe to use across multiple threads and whether it can be used to make multiple concurrent calls.

Should you have periods of inactivity, HTTP/2 connections need to be kept alive. Otherwise the connection closes and a new connection needs to be created from scratch. This can be solved with keepalive pings. In a lot of gRPC implementations, there is explicit support for this feature.

### Max concurrent HTTP/2 streams

HTTP/2 limits the maximum amount of concurrent streams (concurrent requests) on a single connection. Since a gRPC channel operates on a single HTTP/2 connection, many concurrent gRPC calls to the same server may exceed that limit. As a result, gRPC calls that would exceed that limit are getting queued until a previous call completes.

Some gRPC implementations already provide a solution for this, where additional HTTP/2 connections are created automatically. In others, this needs to be implemented manually. However, since most servers set the limit to 100 concurrent streams, this may not affect you at all.

## Closing

Please note that best practices may change with time. Also, not everyone may agree with the above list, which is totally fine. We tried to highlight and explain cases where exceptions and deviations from the usual best practices make complete sense.

For further reading, Google has a great and extensive list of gRPC API design best practices at [https://google.aip.dev/general](https://google.aip.dev/general).

If you have any questions or feedback, don't hesistate to contact us at [[email protected]](https://kreya.app/cdn-cgi/l/email-protection#e78f828b8b88a78c95829e86c9869797).
