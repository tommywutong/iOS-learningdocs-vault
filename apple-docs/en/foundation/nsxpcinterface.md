---
title: NSXPCInterface
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsxpcinterface
source_url: 'https://developer.apple.com/documentation/foundation/nsxpcinterface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsxpcinterface.json'
content_hash: 'sha256:357abc44c2282363'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSXPCInterface

<sub>Class</sub>

An interface that may be sent to an exported object or remote object proxy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSXPCInterface
```

## Overview

This object holds all information about the interface of an exported object or remote object proxy. It describes what messages are allowed, what kinds of objects are allowed as arguments, what the signature of any reply blocks are, and information about additional proxy objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializers

- [+ interfaceWithProtocol:](<nsxpcinterface/init(with_).md>) — Returns an NSXPCInterface instance for a given protocol.
- [init(withProtocol:)](<nsxpcinterface/init(withprotocol_).md>)

### Instance Properties

- [protocol](nsxpcinterface/protocol.md) — The Objective-C protocol that this interface is based on.

### Instance Methods

- [- classesForSelector:argumentIndex:ofReply:](<nsxpcinterface/classes(for_argumentindex_ofreply_).md>) — Returns the current list of allowed classes that can appear within the specified collection object argument to the specified method.
- [- interfaceForSelector:argumentIndex:ofReply:](<nsxpcinterface/forselector(__argumentindex_ofreply_).md>) — Returns the interface previously set for the specified selector and parameter.
- [- setClasses:forSelector:argumentIndex:ofReply:](<nsxpcinterface/setclasses(__for_argumentindex_ofreply_).md>) — Sets the classes that can appear within the (numerically) specified collection object argument to the specified method.
- [- setInterface:forSelector:argumentIndex:ofReply:](<nsxpcinterface/setinterface(__for_argumentindex_ofreply_).md>) — Configures a specific parameter of a method to be sent as a proxy object instead of copied.
- [- setXPCType:forSelector:argumentIndex:ofReply:](<nsxpcinterface/setxpctype(__for_argumentindex_ofreply_).md>)
- [- XPCTypeForSelector:argumentIndex:ofReply:](<nsxpcinterface/xpctype(for_argumentindex_ofreply_).md>)

## See Also

### XPC Client

- [NSXPCProxyCreating](nsxpcproxycreating.md) — Methods for creating new proxy objects.
- [NSXPCConnection](nsxpcconnection.md) — A bidirectional communication channel between two processes.
- [NSXPCCoder](nsxpccoder.md) — A coder that encodes and decodes objects that your app sends over an XPC connection.
