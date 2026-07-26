---
title: URLSessionWebSocketTask.CloseCode.goingAway
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessionwebsockettask/closecode-swift.enum/goingaway
source_url: 'https://developer.apple.com/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum/goingaway'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessionwebsockettask/closecode-swift.enum/goingaway.json'
content_hash: 'sha256:a34b4c44b96d4dc4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLSessionWebSocketTask](../../urlsessionwebsockettask.md) · [CloseCode](../closecode-swift.enum.md)

# URLSessionWebSocketTask.CloseCode.goingAway

<sub>Case</sub>

A code that indicates an endpoint is going away.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case goingAway
```

## Discussion

This code indicates situations like a server going down or a browser having navigated away from a page.

## See Also

### Close codes

- [NSURLSessionWebSocketCloseCodeAbnormalClosure](abnormalclosure.md) — A reserved code that indicates the connection closed without a close control frame.
- [NSURLSessionWebSocketCloseCodeInternalServerError](internalservererror.md) — A code that indicates the server terminated the connection because it encountered an unexpected condition.
- [NSURLSessionWebSocketCloseCodeInvalid](invalid.md) — A code that indicates the connection is still open.
- [NSURLSessionWebSocketCloseCodeInvalidFramePayloadData](invalidframepayloaddata.md) — A code that indicates the server terminated the connection because it received data inconsistent with the message’s type.
- [NSURLSessionWebSocketCloseCodeMandatoryExtensionMissing](mandatoryextensionmissing.md) — A code that indicates the client terminated the connection because the server didn’t negotiate a required extension.
- [NSURLSessionWebSocketCloseCodeMessageTooBig](messagetoobig.md) — A code that indicates an endpoint is terminating the connection because it received a message too big for it to process.
- [NSURLSessionWebSocketCloseCodeNoStatusReceived](nostatusreceived.md) — A reserved code that indicates an endpoint expected a status code and didn’t receive one.
- [NSURLSessionWebSocketCloseCodeNormalClosure](normalclosure.md) — A code that indicates normal connection closure.
- [NSURLSessionWebSocketCloseCodePolicyViolation](policyviolation.md) — A code that indicates an endpoint terminated the connection because it received a message that violates its policy.
- [NSURLSessionWebSocketCloseCodeProtocolError](protocolerror.md) — A code that indicates an endpoint terminated the connection due to a protocol error.
- [NSURLSessionWebSocketCloseCodeTLSHandshakeFailure](tlshandshakefailure.md) — A reserved code that indicates the connection closed due to the failure to perform a TLS handshake.
- [NSURLSessionWebSocketCloseCodeUnsupportedData](unsupporteddata.md) — A code that indicates an endpoint terminated the connection after receiving a type of data it can’t accept.
