---
title: 'gRPC deep dive: from service definition to wire format | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/grpc-deep-dive/'
original_language: en
published: 2026-02-09
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b76cc56fb4a4c57c'
translated: false
---

> 原文：[gRPC deep dive: from service definition to wire format | Kreya](https://kreya.app/blog/grpc-deep-dive/)　·　Kreya Blog

In our previous posts ([part 1](https://kreya.app/blog/protocolbuffers-wire-format/) and [part 2](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)), we demystified Protocol Buffers and learned how data is encoded into compact binary.

But Protobuf is just the payload. To send this data between microservices, we need a transport protocol. Enter **gRPC**.

While many developers use gRPC daily, few look under the hood to see how it actually works. In this post, we’ll go beyond the basics and explore the full gRPC protocol stack: from the high-level service architecture and streaming models down to the low-level HTTP/2 framing and byte-level wire format.

## The contract-first philosophy

At the heart of gRPC lies the contract-first approach. Unlike REST, where API documentation (like OpenAPI) is often an afterthought, gRPC enforces the structure upfront using Protocol Buffers (`.proto` files).

This contract defines not just the data structures (Messages), but the service capabilities (RPCs):

```protobuf
package fruit.v1;service FruitService {    // Unary: simple request -> response    rpc GetFruit(GetFruitRequest) returns (Fruit);    // Server streaming: one request -> many responses    rpc ListFruits(ListFruitsRequest) returns (stream Fruit);    // Client streaming: many requests -> one response    rpc Upload(stream Fruit) returns (UploadSummary);    // Bidirectional streaming: many requests <-> many responses    rpc Chat(stream ChatMessage) returns (stream ChatMessage);}
```

This definition is the source of truth. From this single file, the protobuf compiler (`protoc`) generates client stubs and server boilerplate in almost any language (Go, Java, C#, Python, etc.), ensuring that the client and server always agree on the API shape.

## Streaming models

One of the biggest differentiators of gRPC is its native support for streaming. This isn't just "chunked transfer encoding", it's first-class API semantics.

- **Unary**: Looks like a standard function call or REST request. The client sends one message, the server sends one back.
- **Server streaming**: Perfect for subscriptions or large datasets. The client sends a query, and the server returns multiple results over time.
- **Client streaming**: Useful for sending a stream of data (like telemetry from an IoT device) where the server processes messages as they arrive.
- **Bidirectional streaming**: True real-time communication. Both sides can send messages independently. This is often used for chat apps or multiplayer games.

## Metadata

In addition to the actual data, gRPC allows sending metadata. Metadata is a list of key-value pairs (like HTTP headers) that provide information about the call. Keys are strings, and values are typically strings, but can also be binary data. The key names are case-insensitive and must not start with `grpc-` (reserved for gRPC internals). The keys of binary values must end with `-bin`.

Metadata is essential for cross-cutting concerns that shouldn't be part of the business logic payload:

- **Authentication**: Usage of Bearer tokens (e.g., `Authorization: Bearer <token>`).
- **Tracing**: Passing trace IDs (e.g., `transport-id: 12345`) to track requests across microservices.
- **Infrastructure**: Hints for load balancers or proxies.

Metadata can be sent by both the client (at the start of the call) and the server (at the start as headers, or at the end as trailers).

## Under the hood: the transport layer

So how does this contract map to the network? gRPC is built on top of HTTP/2, leveraging its advanced features to make these streaming models possible.

The most important concept is streams. Every gRPC call, whether it's a simple unary request or a long-lived bidirectional stream, is mapped to a single HTTP/2 stream. This allows multiplexing: you can have thousands of active gRPC calls on a single TCP connection, with their frames interleaved. This prevents opening thousands of connections that would be needed with HTTP/1.1. While it solves the HTTP/1.1 "head-of-line blocking" issue, TCP-level blocking remains a concern if packets are lost.

### Constructing the URL

Before we send any bytes, we need to address the resource. In gRPC, the URL is generated automatically from the `.proto` definition: `/{Package}.{Service}/{Method}`.

For `GetFruit`, the path becomes: `/fruit.v1.FruitService/GetFruit`

This standardization means clients and servers never argue about URL paths.

### The HTTP/2 frames

A gRPC call typically consists of three stages, each mapping to HTTP/2 frames:

1. **Request headers and metadata** (`HEADERS` frame): contains metadata like `:path`, `:method` (`POST`), and `content-type` (`application/grpc`).
2. **Data messages** (`DATA` frames): the actual application data.
3. **Response trailers** (`HEADERS` frame): the final status of the call.

### Metadata on the wire

Since gRPC is built on HTTP/2, metadata is simply mapped to HTTP/2 headers. String values are sent as-is (e.g. `user-agent: grpc-kreya/1.18.0`).

Binary values are base64-encoded and the key must end with `-bin`. Libraries usually handle this encoding/decoding transparently.

### The length-prefixed message

Inside the HTTP/2 `DATA` frame, gRPC wraps your protobuf message with a mechanism called length-prefixed framing. Even in a streaming call, every single message is independent and prefixed with a 5-byte header:

| Byte | Purpose | Description |
|---|---|---|
| 0 | Compression Flag | 0 = Uncompressed 1 = Compressed |
| 1-4 | Message Length | 4-byte big-endian integer indicating the size of the payload |

#### Visualizing the bytes

Let's reuse the fruit message from our [previous post](https://kreya.app/blog/protocolbuffers-wire-format/)

```yaml
weight: 150name: 'Apple'
```

which encodes to 10 bytes of protobuf data: `08 96 01 12 05 41 70 70 6c 65`.

When sending this over gRPC, we prepend the header:

- **Compression**: `0` (no compression)
- **Length**: `10` (`0x0A`)

The final 15-byte gRPC message looks like this:

```
00 00 00 00 0a 08 96 01 12 05 41 70 70 6c 65│  │           └─ The protobuf payload (10 bytes)│  └───────────── Payload message length (0xA = 10 bytes)└──────────────── Compression flag (0 = false)
```

This simple framing allows the receiver to read exactly the right number of bytes for the next message, decode it, and repeat, enabling fluid streaming.

### Status and trailers

In REST, you check the HTTP status code (200, 404, 500). In gRPC, the HTTP status is almost always `200 OK`, even if the logic failed!

The actual application status is sent in the trailers (the very last HTTP/2 header frame). This separation is crucial: it allows a server to successfully stream 100 items and then report an error on the 101st processing step.

A typical trailer block looks like this:

```http
grpc-status: 0grpc-message: OK
```

(Status `0` is OK. Non-zero values represent errors like `NOT_FOUND`, `UNAVAILABLE`, etc.)

### Rich errors

Sometimes, a simple status code and a string message aren't enough. You might want to return validation errors for specific fields or other error details. The rich error model (specifically `google.rpc.Status`) solves this.

Instead of just `grpc-status` and `grpc-message`, the server returns a detailed protobuf message serialized as base64 into the `grpc-status-details-bin` trailer. This standard message contains:

1. **Code**: The gRPC status code.
2. **Message**: The developer-facing error message.
3. **Details**: A list of `google.protobuf.Any` messages containing arbitrary error details (e.g., `BadRequest`, `PreconditionFailure`, `DebugInfo`).

```protobuf
message Status {  // The gRPC status code (3=INVALID_ARGUMENT, 5=NOT_FOUND, etc.)  int32 code = 1;  // The error message  string message = 2;  // A list of extra error details (any custom protobuf message, e.g. validation error details)  repeated google.protobuf.Any details = 3;}
```

Clients can decode this trailer to get structured, actionable error information.

### Compression

Depending on the environment, bandwidth can be precious, especially on mobile networks. gRPC has built-in support for compression to reduce the payload size.

#### How it works

1. **Negotiation**: The client sends a `grpc-accept-encoding` header (e.g., `br, gzip, identity`) to tell the server which algorithms it supports.
2. **Encoding**: If the server decides to compress the response, it sets the `grpc-encoding` header (e.g., `br`).
3. **Flagging**: For each message, the **compression flag** (byte 0 of the 5-byte header) is set to `1`.
4. **Payload**: The message payload is compressed using the selected algorithm.

Let's look at how the wire format changes when compression is enabled. Note that compressing our tiny "Apple" message with brotli results in a larger size due to overhead, but the structure remains the same:

```
01 00 00 00 0e 8f 04 80 08 96 01 12 05 41 70 70 6c 65 03│  │           └─ The compressed payload│  └───────────── Length of compressed message (0xE = 14 bytes)└──────────────── Compression flag (1 = true)
```

This happens per-message. It is even possible to have different compression settings for the request and the response (asymmetric compression).

## Alternative transports

While gRPC usually runs over TCP/IP with HTTP/2, the protocol is agnostic enough to run elsewhere.

- **Unix Domain Sockets**: Perfect for local IPC. It bypasses the TCP network stack for maximum efficiency.
- **Named Pipes**: The equivalent on Windows.

This flexibility allows gRPC to be the universal glue between components, whether they are on different continents or on the same chip.

## The browser gap (gRPC-Web)

There is one place gRPC struggles: **the Browser**. Web browsers do not expose the low-level HTTP/2 framing controls required for gRPC (specifically, reading trailers and granular stream control).

This challenge is addressed by gRPC-Web, a protocol adaptation that:

1. Encodes trailers inside the data stream body (so the browser doesn't need to read HTTP trailers).
2. Supports text-based application-layer encoding (base64) to bypass binary constraints.

We will cover more on how exactly gRPC-Web works in a future post.

## Closing

gRPC is more than just a serialization format, it's a complete ecosystem that standardizes how we define, generate, and consume APIs. By understanding the layers, from the `.proto` contract to the 5-byte header on the wire, you can debug issues more effectively and design better systems.

Tools like [Kreya](https://kreya.app) abstract this complexity away for daily testing, but knowing what happens under the hood puts you in control when things get tricky.

## Further Reading

- [gRPC Best Practices](https://kreya.app/blog/grpc-best-practices/): Learn about API design, versioning, and performance tips.
- [gRPC Core concepts, architecture and lifecycle](https://grpc.io/docs/what-is-grpc/core-concepts/): Official gRPC documentation on core concepts.
- [gRPC HTTP/2 specification](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md): Official gRPC HTTP/2 transport specification.
- Protobuf ([part 1](https://kreya.app/blog/protocolbuffers-wire-format/) and [part 2](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)): Deep dives into the protocol buffers format.
