---
title: CIRenderInfo
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderinfo
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderinfo.json'
content_hash: 'sha256:0ff41ac294bfe41c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRenderInfo

<sub>Class</sub>

An encapsulation of a render task’s timing, passes, and pixels processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIRenderInfo
```

## Overview

A `CIRenderInfo` object allows Xcode Quick Look to visualize the render graph with detailed timing information.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Properties

- [kernelExecutionTime](cirenderinfo/kernelexecutiontime.md) — The amount of time a render spent executing kernels.
- [passCount](cirenderinfo/passcount.md) — The number of passes the render took.
- [pixelsProcessed](cirenderinfo/pixelsprocessed.md) — The number of pixels the render produced executing kernels.
- [kernelCompileTime](cirenderinfo/kernelcompiletime.md)

## See Also

### Custom Render Destination

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md) — Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [CIRenderDestination](cirenderdestination.md) — A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [CIRenderTask](cirendertask.md) — A single render task.
- [CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md) — Different ways of representing alpha.
