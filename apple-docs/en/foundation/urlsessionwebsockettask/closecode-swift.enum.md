---
title: URLSessionWebSocketTask.CloseCode
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/closecode-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum.json'
content_hash: 'sha256:e517025cb21fbe1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionWebSocketTask](../urlsessionwebsockettask.md)

# URLSessionWebSocketTask.CloseCode

<sub>Enumeration</sub>

A code that indicates why a WebSocket connection closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CloseCode
```

## Overview

The WebSocket close codes follow the close codes defined in [RFC 6455](https://tools.ietf.org/html/rfc6455#section-7.4.1).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Close codes

- [NSURLSessionWebSocketCloseCodeAbnormalClosure](closecode-swift.enum/abnormalclosure.md) — A reserved code that indicates the connection closed without a close control frame.
- [NSURLSessionWebSocketCloseCodeGoingAway](closecode-swift.enum/goingaway.md) — A code that indicates an endpoint is going away.
- [NSURLSessionWebSocketCloseCodeInternalServerError](closecode-swift.enum/internalservererror.md) — A code that indicates the server terminated the connection because it encountered an unexpected condition.
- [NSURLSessionWebSocketCloseCodeInvalid](closecode-swift.enum/invalid.md) — A code that indicates the connection is still open.
- [NSURLSessionWebSocketCloseCodeInvalidFramePayloadData](closecode-swift.enum/invalidframepayloaddata.md) — A code that indicates the server terminated the connection because it received data inconsistent with the message’s type.
- [NSURLSessionWebSocketCloseCodeMandatoryExtensionMissing](closecode-swift.enum/mandatoryextensionmissing.md) — A code that indicates the client terminated the connection because the server didn’t negotiate a required extension.
- [NSURLSessionWebSocketCloseCodeMessageTooBig](closecode-swift.enum/messagetoobig.md) — A code that indicates an endpoint is terminating the connection because it received a message too big for it to process.
- [NSURLSessionWebSocketCloseCodeNoStatusReceived](closecode-swift.enum/nostatusreceived.md) — A reserved code that indicates an endpoint expected a status code and didn’t receive one.
- [NSURLSessionWebSocketCloseCodeNormalClosure](closecode-swift.enum/normalclosure.md) — A code that indicates normal connection closure.
- [NSURLSessionWebSocketCloseCodePolicyViolation](closecode-swift.enum/policyviolation.md) — A code that indicates an endpoint terminated the connection because it received a message that violates its policy.
- [NSURLSessionWebSocketCloseCodeProtocolError](closecode-swift.enum/protocolerror.md) — A code that indicates an endpoint terminated the connection due to a protocol error.
- [NSURLSessionWebSocketCloseCodeTLSHandshakeFailure](closecode-swift.enum/tlshandshakefailure.md) — A reserved code that indicates the connection closed due to the failure to perform a TLS handshake.
- [NSURLSessionWebSocketCloseCodeUnsupportedData](closecode-swift.enum/unsupporteddata.md) — A code that indicates an endpoint terminated the connection after receiving a type of data it can’t accept.

### Initializers

- [init(rawValue:)](<closecode-swift.enum/init(rawvalue_).md>)

## See Also

### Closing the connection

- [- cancelWithCloseCode:reason:](<cancel(with_reason_).md>) — Sends a close frame with the given close code and optional close reason.
- [closeCode](closecode-swift.property.md) — A code that indicates the reason a connection closed.
- [closeReason](closereason.md) — A block of data that provides further information about why a connection closed.
