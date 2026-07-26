---
title: CIRenderDestinationAlphaMode
framework: Core Image
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirenderdestinationalphamode
source_url: 'https://developer.apple.com/documentation/coreimage/cirenderdestinationalphamode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirenderdestinationalphamode.json'
content_hash: 'sha256:8517e05e0473b2d0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIRenderDestinationAlphaMode

<sub>Enumeration</sub>

Different ways of representing alpha.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum CIRenderDestinationAlphaMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [CIRenderDestinationAlphaNone](cirenderdestinationalphamode/none.md) — Designates a destination with no alpha compositing.
- [CIRenderDestinationAlphaPremultiplied](cirenderdestinationalphamode/premultiplied.md) — Designates a destination that expects premultiplied alpha values.
- [CIRenderDestinationAlphaUnpremultiplied](cirenderdestinationalphamode/unpremultiplied.md) — Designates a destination that expects non-premultiplied alpha values.

### Initializers

- [init(rawValue:)](<cirenderdestinationalphamode/init(rawvalue_).md>)

## See Also

### Custom Render Destination

- [Generating an animation with a Core Image Render Destination](generating-an-animation-with-a-core-image-render-destination.md) — Animate a filtered image to a Metal view in a SwiftUI app using a Core Image Render Destination.
- [CIRenderDestination](cirenderdestination.md) — A specification for configuring all attributes of a render task’s destination and issuing asynchronous render tasks.
- [CIRenderInfo](cirenderinfo.md) — An encapsulation of a render task’s timing, passes, and pixels processed.
- [CIRenderTask](cirendertask.md) — A single render task.
