---
title: 'progressive(_:initialAmount:aspectRatio:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersionstyle/progressive(_:initialamount:aspectratio:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/progressive(_:initialamount:aspectratio:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/progressive%28_%3Ainitialamount%3Aaspectratio%3A%29.json'
content_hash: 'sha256:d9320e15fa7390ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# progressive(_:initialAmount:aspectRatio:)

<sub>Type Method</sub>

An immersion style that displays unbounded content that partially replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
static func progressive(_ immersionRange: ClosedRange<Double>, initialAmount: Double? = nil, aspectRatio: ProgressiveImmersionAspectRatio?) -> ProgressiveImmersionStyle
```

## Parameters

- `initialAmount` — The initial amount of immersion used for this instance of the style. If `nil`, a system default will be used. The value must be within the range defined by this style.

- `aspectRatio` — The aspect ratio of the portal. If `nil`, a system default of landscape will be used.

## Discussion

Use the [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier to specify this style for an [ImmersiveSpace](../immersivespace.md).

The immersion style affects how windows interact with virtual objects in the environment. In `progressive` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is off.

The system initially uses a portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by rotating the Digital Crown, including down to a minimum amount of immersion defined by the app and up to the defined maximum amount of immersion.
