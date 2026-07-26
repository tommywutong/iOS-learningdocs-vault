---
title: Text.Layout.DrawingOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/layout/drawingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout/drawingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout/drawingoptions.json'
content_hash: 'sha256:27f6b7fa2d384e4c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Text](../../text.md) · [Layout](../layout.md)

# Text.Layout.DrawingOptions

<sub>Structure</sub>

Option flags used when drawing `Text.Layout` lines or runs into a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct DrawingOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Copyable](../../../swift/copyable.md), [Equatable](../../../swift/equatable.md), [ExpressibleByArrayLiteral](../../../swift/expressiblebyarrayliteral.md), [OptionSet](../../../swift/optionset.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md), [SetAlgebra](../../../swift/setalgebra.md)

## Topics

### Type Properties

- [disablesSubpixelQuantization](drawingoptions/disablessubpixelquantization.md) — If set, subpixel quantization requested by the text engine is disabled. This can be useful for text that will be animated to prevent it jittering.
