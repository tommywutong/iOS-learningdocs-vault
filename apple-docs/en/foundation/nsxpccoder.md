---
title: NSXPCCoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpccoder
source_url: 'https://developer.apple.com/documentation/foundation/nsxpccoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpccoder.json'
content_hash: 'sha256:f3e5057cbb8107da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCCoder

<sub>Class</sub>

A coder that encodes and decodes objects that your app sends over an XPC connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSXPCCoder
```

## Overview

If you want to perform custom encoding or decoding of [Codable](../swift/codable.md) objects that your app sends over an [NSXPCConnection](nsxpcconnection.md), use [isKind(of:)](<../objectivec/nsobjectprotocol/iskind(of_).md>) to determine if the coder provided to your object is a kind of [NSXPCCoder](nsxpccoder.md).

## Relationships

- **Inherits From**: [NSCoder](nscoder.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the Coder

- [connection](nsxpccoder/connection.md) — The connection currently performing encoding or decoding.
- [userInfo](nsxpccoder/userinfo.md) — An optional user information object associated with the coder.

### Encoding and Decoding

- [- encodeXPCObject:forKey:](<nsxpccoder/encodexpcobject(__forkey_).md>) — Encodes an object to send over an XPC connection.
- [- decodeXPCObjectOfType:forKey:](<nsxpccoder/decodexpcobject(oftype_forkey_).md>) — Decodes an object and validates that its type matches the type a service provides over XPC.

## See Also

### XPC Client

- [NSXPCProxyCreating](nsxpcproxycreating.md) — Methods for creating new proxy objects.
- [NSXPCConnection](nsxpcconnection.md) — A bidirectional communication channel between two processes.
- [NSXPCInterface](nsxpcinterface.md) — An interface that may be sent to an exported object or remote object proxy.
