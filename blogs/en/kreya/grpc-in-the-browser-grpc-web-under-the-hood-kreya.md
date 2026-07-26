---
title: 'gRPC in the browser: gRPC-Web under the hood | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/grpc-web-deep-dive/'
original_language: en
published: 2026-03-23
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6690cbbadc60ee9b'
translated: false
---

> 原文：[gRPC in the browser: gRPC-Web under the hood | Kreya](https://kreya.app/blog/grpc-web-deep-dive/)　·　Kreya Blog

In my [previous post](https://kreya.app/blog/grpc-deep-dive/) we explored the full gRPC protocol stack, from the `.proto` contract down to the HTTP/2 frame on the wire. We ended with a cliffhanger: browsers cannot speak native gRPC. I promised to cover that gap. This is that post.

We will look at why browsers are fundamentally incompatible with the gRPC HTTP/2 protocol and how gRPC-Web works around those limitations at the byte level. Along the way, we will dig into the Fetch API's streaming internals and close with what is (hopefully) coming in the near future.

## Why browsers can't speak native gRPC

To understand the problem, we need to revisit what gRPC actually requires from its transport layer. Two HTTP/2 features are critical, and both are inaccessible to browser JavaScript.

### The trailer problem

As we covered in the previous post, gRPC sends its final status not in the HTTP status code but in HTTP/2 trailers, a `HEADERS` frame sent after all `DATA` frames. This is what allows a server to stream 1000 records and only then report success or failure.

The Fetch API exposes `response.headers`, but not trailers. The `response.trailers` property has been in the WhatWG Fetch specification as a `Promise<Headers>` for years, and it is still not implemented in any major browser. The reason is not laziness, it is a genuinely hard platform problem. HTTP/1.1 doesn't have trailers at all (at least not in practice), and exposing HTTP/2 trailer semantics through a clean cross-version API turns out to be non-trivial.

### The framing problem

Even if trailers were available, JavaScript has no mechanism to control raw HTTP/2 framing. The browser's networking layer decides when to open and close HTTP/2 streams, handles flow control, and manages connection multiplexing. Your JavaScript code never touches a single HTTP/2 `DATA` frame directly.

These two constraints together mean that native gRPC, in its current form, cannot run in a browser without modification.

## gRPC-Web: trailers in disguise

The official solution from the gRPC team is gRPC-Web, a protocol adaptation that works around both constraints by moving trailers into the HTTP body. Instead of relying on `HEADERS` frames that JavaScript can't read, trailers are encoded as a special final message inside the `DATA` frames that the browser can read perfectly well.

### The flag byte upgrade

gRPC-Web reuses the same 5-byte length-prefixed framing as gRPC, but gives a new meaning to the first byte. Where gRPC only uses bit 0 (the compression flag), gRPC-Web reserves bit 7 as a trailer flag:

| Byte | Bits | Purpose |
|---|---|---|
| 0 | 0 | **Compression flag**: `1` = the payload is compressed |
| 0 | 7 | **Trailer flag**: `1` = this frame contains trailers, not application data |
| 1-4 | all | **Message length**: 4-byte big-endian unsigned integer |

So a gRPC-Web response stream consists of:

- Zero or more data frames (flag byte `0x00` or `0x01` if compressed)
- Exactly one trailer frame at the end (flag byte `0x80`)

### The trailer frame on the wire

The trailer frame's payload is a plain block of HTTP header-style key-value pairs, separated by `\r\n` (CRLF), just like HTTP/1.1 headers.

For a successful completion, the trailer payload looks like this:

```text
grpc-status: 0\r\ngrpc-message: OK\r\n
```

That is 34 bytes. The complete 5-byte header then becomes `80 00 00 00 22`.

Let's visualize a complete successful server-streaming response in gRPC-Web. First a data frame carrying our "Apple" fruit message, then a trailer frame:

```
--- data frame ---00 00 00 00 0a 08 96 01 12 05 41 70 70 6c 65│  │           └─ Protobuf payload (10 bytes)│  └───────────── Message length (0xA = 10)└──────────────── Flag byte: 0x00 (data, uncompressed)--- trailer frame ---80 00 00 00 22 67 72 70 63 2d 73 74 61 74 75 73 3a 20 30 0d 0a│  │           67 72 70 63 2d 6d 65 73 73 61 67 65 3a 20 4f 4b 0d 0a│  │           └─ "grpc-status: 0\r\ngrpc-message: OK\r\n" (34 bytes)│  └───────────── Trailer block length (0x22 = 34)└──────────────── Flag byte: 0x80 (trailer frame)
```

The JavaScript code reads the response body as a stream of bytes, parses the 5-byte header to determine the frame type and length, then either parses the protobuf payload or parses the trailer key-value pairs.

### Content types

gRPC-Web defines four content types:

| Content-Type | Encoding | Suitable for |
|---|---|---|
| `application/grpc-web` | Binary | Fetch API |
| `application/grpc-web+proto` | Binary + protobuf hint | Fetch API |
| `application/grpc-web-text` | Base64 | XHR (legacy) |
| `application/grpc-web-text+proto` | Base64 + protobuf hint | XHR (legacy) |

The `-text` variants exist for compatibility with the older `XMLHttpRequest` API, which is text-oriented and cannot handle arbitrary binary chunks from a streaming response. With `-text`, the entire response body is base64-encoded, so XHR can accumulate it as a string and the client decodes it before envelope parsing.

With the modern Fetch API you always want the binary variants.

### Streaming limitations

gRPC-Web inherits a hard constraint from HTTP/1.x semantics: the request body must be complete before the server can start responding. This rules out two of the four gRPC streaming models:

| Streaming model | Works in gRPC-Web? | Reason |
|---|---|---|
| Unary | ✅ | Single request, single response |
| Server streaming | ✅ | Single request, streaming response body |
| Client streaming | ❌ | Requires streaming request body |
| Bidirectional streaming | ❌ | Requires simultaneous request/response streams |

Client and bidirectional streaming from a browser are simply not possible with gRPC-Web.

### The translation layer

Because a standard gRPC server speaks HTTP/2 with native trailers, something must translate the gRPC-Web envelope into native gRPC and back. There are two ways to provide this:

**A proxy**: The classic approach is Envoy with the `grpc_web` filter sitting in front of your gRPC server. The proxy unwraps the gRPC-Web envelope, forwards the call upstream as native gRPC, and re-wraps the response. This works language-agnostically but adds an operational hop.

**In-process middleware**: Most modern server frameworks handle the translation themselves, with no separate proxy needed:

- **.NET**: `Grpc.AspNetCore.Web` adds a single `app.UseGrpcWeb()` middleware call. ASP.NET Core detects the `application/grpc-web` content type and translates on the fly.
- **Go**: `improbable-eng/grpc-web` provides an `http.Handler` wrapper around any gRPC server. One line of setup, no infrastructure changes.
- **Node.js / Deno**: The `@grpc/grpc-js` package combined with a small `grpc-web` wrapper handles the translation in-process with no separate infrastructure.

The in-process approach is generally preferred for new services: it keeps the stack simple, eliminates an extra network hop, and co-locates the protocol logic with the service code. The proxy approach remains useful when you don't control the server implementation or need to front many heterogeneous backends.

### Troubleshooting gRPC-Web in the browser

gRPC-Web is notoriously difficult to debug with standard browser tooling. The Chrome DevTools Network tab will show you that a gRPC-Web request was made and how many bytes were transferred, but it has no idea what those bytes mean. The response body is raw binary, and there is no built-in way to inspect the envelope framing or decode the protobuf payload.

Several things compound the problem:

- **The trailer is hidden.** The trailer frame is just another chunk of response body bytes. DevTools has no hook to surface it as headers, so it appears nowhere in the familiar "Headers" or "Trailers" panel. You might spend a long time wondering why `grpc-status` is nowhere to be found.
- **The 5-byte envelope is opaque.** Even if you export the raw bytes, you must manually strip the 5-byte length header before you can feed the payload into a protobuf decoder. For the `-text` variants, there is an extra base64 decode step before you even get to the envelope.
- **Error messages are buried.** A failed gRPC-Web call typically returns HTTP 200 (the actual status is in the trailer frame). DevTools will show a green 200 response with no obvious sign that anything went wrong. The real error is encoded in the trailer frame payload, which is just more opaque bytes at the tail of the response body.
- **The grpc-Web proxy adds a hop.** If Envoy or in-process middleware is misbehaving, stripping headers, changing content types, or corrupting the envelope, the only way to see this is to capture traffic at both the browser and the backend simultaneously or debugging the middleware itself.

The most practical debugging workflow is to export a HAR file from the browser's Network tab and open it in a tool that understands gRPC-Web. [Kreya's HAR import](https://kreya.app/blog/har-import/) does exactly this: if you have already imported your `.proto` definitions, Kreya will automatically decode the envelope framing and render the protobuf payloads as human-readable fields, no manual byte stripping required.

## The Fetch API and streaming internals

Before closing the gRPC-Web chapter, it is worth understanding what the browser's Fetch API can and cannot do with streaming today, because any gRPC-compatible browser client has to work within these constraints.

### Reading a streaming response

The Fetch API exposes the response body as a [`ReadableStream<Uint8Array>`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream). Reading it incrementally looks like this:

```javascript
const response = await fetch('/fruit.v1.FruitService/ListFruits', {  method: 'POST',  headers: { 'Content-Type': 'application/grpc-web+proto' },  body: requestBytes,});const reader = response.body.getReader();let buffer = new Uint8Array(0);while (true) {  const { done, value } = await reader.read();  if (done) break;  // Append new chunk to buffer  buffer = concat(buffer, value);  // Parse complete envelopes out of the buffer  while (buffer.length >= 5) {    const flags = buffer[0];    const length = new DataView(buffer.buffer).getUint32(1, false); // big-endian    if (buffer.length < 5 + length) break; // wait for more data    const payload = buffer.slice(5, 5 + length);    buffer = buffer.slice(5 + length);    if (flags & 0x80) {      parseTrailers(payload); // trailer frame    } else {      dispatchMessage(payload); // data frame    }  }}
```

The key insight is that chunks from `reader.read()` do not align with gRPC-Web frames. A single `DATA` frame from the server may arrive split across multiple `read()` calls, or several frames may arrive in one chunk. Your buffer management must handle both cases.

### Streaming request bodies

Reading the response is straightforward, but what about writing? Can we stream a request body from browser JavaScript?

The answer is: **yes, but with caveats**.

Since Chrome 105, you can pass a `ReadableStream` as the `body` of a `fetch()` request:

```javascript
const stream = new ReadableStream({  start(controller) {    controller.enqueue(encodeMessage(request1));    controller.enqueue(encodeMessage(request2));    controller.close();  },});await fetch('/service/Method', {  method: 'POST',  headers: { 'Content-Type': 'application/grpc-web+proto' },  body: stream,  duplex: 'half', // required!});
```

The `duplex: 'half'` option is the critical detail. It tells the browser that this is a one-way upload: the client is free to stream the body, but the server's response body will not arrive until the client's request body is closed. This maps to HTTP/1.1 semantics, where you finish sending before you start receiving.

**What about `duplex: 'full'`?** True bidirectional streaming would require `duplex: 'full'`, where the server can start sending responses while the client is still uploading. This requires the browser to open an HTTP/2 stream and read from it while simultaneously writing to it, exactly what gRPC does natively. The option exists as a [proposal tracked in the WHATWG Fetch repository](https://github.com/whatwg/fetch/issues/1254) and is experimentally available behind a flag in some Chromium builds, but as of early 2026 it is not shipped in any stable browser. Safari and Firefox do not support it at all yet.

## Connect-RPC: designed for the web from the start

gRPC-Web retrofits gRPC onto browsers while preserving full gRPC server compatibility. **[Connect-RPC](https://connectrpc.com)** (developed by [Buf](https://buf.build)) takes a different philosophy: design a protocol that is idiomatic HTTP from the ground up, works natively in browsers without any proxy, and also interoperates with gRPC.

A Connect-RPC server speaks three protocols simultaneously: the Connect protocol, native gRPC, and gRPC-Web. The client declares which one it wants through the `Content-Type` header.

### Unary calls: just HTTP

The most striking difference in Connect-RPC is how unary calls work. There is no length-prefixed framing for unary requests or responses. The serialized protobuf message is simply the entire HTTP body, nothing more.

A `GetFruit` request looks like this on the wire:

```http
POST /fruit.v1.FruitService/GetFruit HTTP/1.1Content-Type: application/connect+protoContent-Length: 7<7 bytes of raw protobuf>
```

And a successful response:

```http
HTTP/1.1 200 OKContent-Type: application/connect+protoContent-Length: 10<10 bytes of raw protobuf>
```

This is indistinguishable from a well-behaved JSON REST API, just with a different content type. Any HTTP proxy, CDN, or debugging tool understands it immediately. No special handling, no envelope parsing, no proxy required.

### Connect unary error handling

Because Connect uses real HTTP status codes for unary errors, the error response is equally transparent:

```http
HTTP/1.1 404 Not FoundContent-Type: application/json{  "code": "not_found",  "message": "fruit Apple not found"}
```

Notice the `Content-Type: application/json`, this is deliberate and unconditional. Even when the client negotiated binary protobuf for the happy path (`Content-Type: application/connect+proto`), errors are always returned as JSON. This means you can read any Connect error with nothing more than `curl` or a browser's network inspector, without having to decode binary protobuf just to find out what went wrong. The full set of Connect error codes and their HTTP status mappings is well-defined in the [Connect protocol specification](https://connectrpc.com/docs/protocol#error-codes). For richer errors, Connect also supports the same `details` array as gRPC's `google.rpc.Status`:

```json
{  "code": "invalid_argument",  "message": "request validation failed",  "details": [    {      "type": "google.rpc.BadRequest",      "value": "CiQKBG5hbWUSHG11c3QgYmUgYXQgbGVhc3QgMSBjaGFyYWN0ZXI="    }  ]}
```

### Streaming calls: the end-of-stream message

For streaming calls, Connect uses the same 5-byte envelope framing as gRPC. The compression flag (bit 0) works identically. But instead of a trailer flag (bit 7 like gRPC-Web), Connect uses bit 1 (value `0x02`) as an end-of-stream flag:

| Byte | Bits | Purpose |
|---|---|---|
| 0 | 1 | **End-of-stream flag**: `1` = this is the final message with trailers |
| 0 | 0 | **Compression flag**: `1` = the payload is compressed |
| 1-4 | all | **Message length**: 4-byte big-endian unsigned integer |

The end-of-stream message has its payload encoded as **JSON**, regardless of whether the rest of the stream uses protobuf or JSON encoding. This is intentional: it makes the terminal status easy to inspect with any tool.

For a successful stream, it looks like this:

```
--- data frame (same as gRPC) ---00 00 00 00 0a 08 96 01 12 05 41 70 70 6c 65│  │           └─ Protobuf payload (10 bytes)│  └───────────── Message length (0xA = 10)└──────────────── Flag byte: 0x00 (data, uncompressed)--- end-of-stream message ---02 00 00 00 0f 7b 22 6d 65 74 61 64 61 74 61 22 3a 7b 7d 7d│  │           └─ JSON payload: {"metadata":{}} (15 bytes)│  └───────────── End-of-stream message length (0xF = 15)└──────────────── Flag byte: 0x02 (end-of-stream)
```

When the stream errors mid-flight, the end-of-stream message carries the error instead of metadata:

```json
{  "error": {    "code": "internal",    "message": "upstream database unavailable"  }}
```

This design has a subtle but important benefit over gRPC-Web's CRLF-delimited trailer block: the end-of-stream message is regular JSON, parseable by any standard JSON library, with a well-typed schema you can evolve over time.

## Protocol comparison

| Feature | Native gRPC | gRPC-Web | Connect (unary) | Connect (streaming) |
|---|---|---|---|---|
| Transport | HTTP/2 | HTTP/1.1+ | HTTP/1.1+ | HTTP/1.1+ |
| HTTP/3 (QUIC) support | ✅ (Draft spec) | ✅ | ✅ | ✅ |
| Request framing | 5-byte envelope | 5-byte envelope | No framing | 5-byte envelope |
| Response framing | 5-byte envelope | 5-byte envelope | No framing | 5-byte envelope |
| Trailers | HTTP/2 HEADERS | Body (flag `0x80`) | HTTP headers | Body (flag `0x02`) |
| Error encoding | `grpc-status` trailer | Trailer frame | HTTP status + JSON | End-of-stream JSON |
| Browser compatible | ❌ | ✅ | ✅ | ✅ |
| Proxy component required | N/A | ✅ | ❌ | ❌ |
| Client streaming in browser | ❌ | ❌ | ❌ (unary) | ✅ (with `duplex: 'half'`) |
| Bidirectional in browser | ❌ | ❌ | N/A | ❌ (pending `duplex: 'full'`) |
| Human-readable errors | ❌ | ❌ | ✅ | ✅ |
| Works with curl | ❌ | Partially | ✅ | ✅ |

Connect's `application/connect+json` content type brings another benefit: it uses Protobuf's canonical JSON mapping, so every call is both human-readable and testable with `curl`, without any special client library.

## What is coming

The browser networking stack is actively evolving. Several changes in flight will reshape how gRPC-style protocols work in browsers.

### WebTransport

[WebTransport](https://developer.chrome.com/docs/capabilities/web-apis/webtransport) is a browser API built on QUIC (HTTP/3). It provides multiplexed bidirectional streams and unreliable datagrams, without the head-of-line blocking that plagues TCP.

From the browser's perspective, WebTransport is a lower-level primitive than Fetch. You open streams explicitly, you control when each stream starts and ends, and you can send multiple streams over a single QUIC connection. This maps much more naturally to gRPC's stream model than Fetch does.

The gRPC team has done exploratory work on running gRPC over WebTransport, and experimental implementations exist in some gRPC libraries. No formal specification has been published yet (the closest published doc is [G2, gRPC over HTTP/3](https://github.com/grpc/proposal/blob/master/G2-http3-protocol.md), which covers straight QUIC transport rather than the WebTransport browser API). The envisioned protocol uses standard gRPC length-prefixed framing inside QUIC streams, with the call path (`/package.Service/Method`) as the stream header.

Browser availability: Chrome has supported WebTransport since version 97 (late 2021). Firefox support is under active development. Safari support is not yet announced.

Actual production deployment of gRPC-over-WebTransport is still rare as of early 2026, but the foundation is solid and adoption will follow browser support.

### Fetch API `duplex: 'full'`

As mentioned earlier, [`duplex: 'half'`](https://developer.chrome.com/docs/capabilities/web-apis/fetch-streaming-requests) enables streaming request bodies but does not allow the server to respond while the client is still uploading. `duplex: 'full'` would remove that restriction, enabling true bidirectional streaming over a standard HTTP/2 Fetch request.

The Chrome team has been working on this. There is an [explainer in the WHATWG Fetch repository](https://github.com/whatwg/fetch/issues/1254) and an active Origin Trial. Once stable, it would allow native bidirectional Connect-RPC streaming over Fetch, without any need for WebTransport.

### HTTP/3 and QUIC adoption

HTTP/3 is already widely supported in browsers and increasingly deployed on the server side. While native gRPC was originally defined strictly over HTTP/2, support for gRPC over HTTP/3 has started landing in implementations. For example, the .NET gRPC implementation supports HTTP/3 out of the box in modern versions, allowing native gRPC over QUIC with all the associated benefits.

Because gRPC-Web and Connect-RPC do not have strong ties to HTTP/2-specific framing, they can automatically work with HTTP/3. Their envelope formats are unchanged, they are just bytes in a POST body, traveling equally well over TCP or QUIC. For gRPC-Web apps currently running behind a proxy or CDN, you can enable HTTP/3 for the proxy-to-browser leg immediately without changing a line of client or server code.

### The Fetch trailers proposal

The WHATWG Fetch specification has an [open proposal](https://github.com/whatwg/fetch/issues/981) for `response.trailers` returning a `Promise<Headers>` that resolves when all trailers have been received. If this lands, browsers could eventually consume native gRPC responses without adapting the wire format at all.

This has been blocked mainly because the semantics interact subtly with HTTP/1.1 chunked-encoded trailers (technically defined but almost never used in practice), and because it requires coordinating with the HTTP/2 and HTTP/3 specifications. It remains an open issue and is unlikely to ship in the next one to two years.

## Closing

Getting gRPC to work in a browser turns out to require far more engineering than it first appears. Native gRPC is off the table: browsers cannot read HTTP/2 trailers or control raw frames. gRPC-Web solves the trailer problem elegantly by encoding trailers as a special flagged message in the body, but it requires a proxy and locks you out of client and bidirectional streaming. Connect-RPC solves the proxy problem by treating unary calls as plain HTTP and embedding end-of-stream metadata as a JSON message, while remaining fully compatible with gRPC and gRPC-Web on the server side.

WebTransport is the long-term answer for true bidirectional streaming in browsers, and `duplex: 'full'` for Fetch may bridge the gap before WebTransport reaches universal support.

Tools like [Kreya](https://kreya.app) support native gRPC and gRPC-Web out of the box, so you can inspect gRPC-Web trailer frames without writing a single line of parsing code. But now you know exactly what is happening under the hood.

## Further Reading

- [gRPC deep dive](https://kreya.app/blog/grpc-deep-dive/): The previous post in this series covering native gRPC and HTTP/2 framing in depth.
- [Debugging gRPC-Web with HAR files](https://kreya.app/blog/har-import/): How to export a HAR file from your browser and use Kreya to decode gRPC-Web payloads without touching a single raw byte.
- [gRPC-Web protocol specification](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-WEB.md): Official specification for the gRPC-Web wire format.
- [Connect-RPC protocol specification](https://connectrpc.com/docs/protocol): Full specification of the Connect protocol, including unary and streaming framing.
- [WebTransport explainer](https://developer.chrome.com/docs/capabilities/web-apis/webtransport): Chrome's developer documentation on the WebTransport API.
- [WHATWG Fetch: readable stream bodies](https://fetch.spec.whatwg.org/#concept-body): The WHATWG Fetch specification sections covering `ReadableStream` bodies and the duplex mode.
- Protobuf ([part 1](https://kreya.app/blog/protocolbuffers-wire-format/) and [part 2](https://kreya.app/blog/protocolbuffers-wire-format-part-2/)): How protobuf messages are encoded into compact binary.
