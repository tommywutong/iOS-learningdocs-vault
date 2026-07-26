---
title: CARemoteLayerServer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.1+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caremotelayerserver
source_url: 'https://developer.apple.com/documentation/quartzcore/caremotelayerserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caremotelayerserver.json'
content_hash: 'sha256:3221a455f9fdbebd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CARemoteLayerServer

<sub>Class</sub>

A legacy class for cross-process rendering.

<sub>Mac Catalyst, macOS</sub>

```swift
class CARemoteLayerServer
```

## Overview

`CARemoteLaterServer` is a legacy class for cross-process rendering. [IOSurfaceCreateMachPort(_:)](<../iosurface/iosurfacecreatemachport(__).md>) and [IOSurfaceCreateXPCObject(_:)](<../iosurface/iosurfacecreatexpcobject(__).md>), available with [IOSurface](../iosurface/iosurface.md), offer an improved way to perform cross-process rendering.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Server

- [serverPort](caremotelayerserver/serverport.md) — The port number of the server.

### Getting a Server Instance

- [+ sharedServer](<caremotelayerserver/shared().md>) — Returns the (singleton) instance of the shared remote layer server.

## See Also

### Remote Display of Layer Content

- [CARemoteLayerClient](caremotelayerclient.md) — A legacy class for cross-process rendering.
