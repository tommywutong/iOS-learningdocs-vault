---
title: NSXPCListenerEndpoint
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpclistenerendpoint
source_url: 'https://developer.apple.com/documentation/foundation/nsxpclistenerendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpclistenerendpoint.json'
content_hash: 'sha256:9e45265c58cb9e5b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCListenerEndpoint

<sub>Class</sub>

An object that names a specific XPC listener.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSXPCListenerEndpoint
```

## Overview

An instance of [NSXPCListenerEndpoint](nsxpclistenerendpoint.md) may be retrieved from an [NSXPCListener](nsxpclistener.md) instance and sent over existing [NSXPCConnection](nsxpcconnection.md)s. A process may then use the endpoint to create a new [NSXPCConnection](nsxpcconnection.md) to the original [NSXPCListener](nsxpclistener.md).

This pattern is useful if you have a service which multiplexes work to other services. The service can act as an intermediate helper. The requesting application does not need to know specifically which service it is connecting to, just that it implements a known [NSXPCInterface](nsxpcinterface.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(coder:)](<nsxpclistenerendpoint/init(coder_).md>)

## See Also

### XPC Services

- [NSXPCListener](nsxpclistener.md) — A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [NSXPCListenerDelegate](nsxpclistenerdelegate.md) — The protocol that delegates to the XPC listener use to accept or reject new connections.
