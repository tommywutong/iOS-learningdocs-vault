---
title: CIRenderTask
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirendertask
source_url: 'https://developer.apple.com/documentation/coreimage/cirendertask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirendertask.json'
content_hash: 'sha256:5466b548f6e855ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRenderTask

<sub>Class</sub>

A single render task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIRenderTask
```

## Overview

A single render task issued in conjunction with [CIRenderDestination](cirenderdestination.md).

A `CIRenderTask` object appears in Xcode Quick Look as a graph.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance Methods

- [- waitUntilCompletedAndReturnError:](<cirendertask/waituntilcompleted().md>) — Waits until the [CIRenderTask](cirendertask.md) finishes and returns.

### Instance Properties

- [plannedPassCount](cirendertask/plannedpasscount.md) _(beta)_
- [plannedPeakMemory](cirendertask/plannedpeakmemory.md) _(beta)_
- [plannedPixelsOverdrawn](cirendertask/plannedpixelsoverdrawn.md) _(beta)_
- [plannedPixelsProcessed](cirendertask/plannedpixelsprocessed.md) _(beta)_

## See Also

### Custom Render Destination

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md) — Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [CIRenderDestination](cirenderdestination.md) — A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [CIRenderInfo](cirenderinfo.md) — An encapsulation of a render task’s timing, passes, and pixels processed.
- [CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md) — Different ways of representing alpha.
