---
title: CARemoteLayerClient
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caremotelayerclient
source_url: 'https://developer.apple.com/documentation/quartzcore/caremotelayerclient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caremotelayerclient.json'
content_hash: 'sha256:62371b82f9d8f112'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CARemoteLayerClient

<sub>Class</sub>

A legacy class for cross-process rendering.

<sub>Mac Catalyst, macOS</sub>

```swift
class CARemoteLayerClient
```

## Overview

`CARemoteLaterClient` is a legacy class for cross-process rendering. [IOSurfaceCreateMachPort(_:)](<../iosurface/iosurfacecreatemachport(__).md>) and [IOSurfaceCreateXPCObject(_:)](<../iosurface/iosurfacecreatexpcobject(__).md>), available with [IOSurface](../iosurface/iosurface.md), offer an improved way to perform cross-process rendering.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Client

- [- initWithServerPort:](<caremotelayerclient/init(serverport_).md>) — Creates a layer client from a server port.

### Retrieving Client Properties

- [clientId](caremotelayerclient/clientid.md) — The ID of the remote layer client.
- [layer](caremotelayerclient/layer.md) — The layer associated with the remote client.

### Invalidating a Client

- [- invalidate](<caremotelayerclient/invalidate().md>) — Invalidates a remote layer client.

## See Also

### Remote Display of Layer Content

- [CARemoteLayerServer](caremotelayerserver.md) — A legacy class for cross-process rendering.
