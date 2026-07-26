---
title: 'progressive(_:initialAmount:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 26.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersionstyle/progressive(_:initialamount:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/progressive(_:initialamount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/progressive%28_%3Ainitialamount%3A%29.json'
content_hash: 'sha256:862f2cd6b3212fcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# progressive(_:initialAmount:)

<sub>Type Method</sub>

An immersion style that displays unbounded content that partially replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
static func progressive(_ immersionRange: ClosedRange<Double>, initialAmount: Double? = nil) -> ProgressiveImmersionStyle
```

## Parameters

- `immersionRange` — The range of immersion used for this instance of the style. The lower bound and upper bound value of the range represent the minimum and maximum amount of the spherical field of view of the user that can be covered by the portal effect of the style. The lower bound value must be equal to or greater than `0.0` and smaller than the upper bound. The upper bound value must be greater than the lower bound and smaller than or equal to `1.0`.

- `initialAmount` — The initial amount of immersion used for this instance of the style. If `nil`, a system default will be used. The value must be within the range defined by this style.

## Discussion

The immersion style affects how windows interact with virtual objects in the environment. In `progressive` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people avoid losing track of windows behind virtual content when passthrough is off.

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<../view/onimmersionchange(initial___).md>) is within the range of the immersion that this style is defined with.

Use the [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier to specify this style for an [ImmersiveSpace](../immersivespace.md):

```swift
@main
struct ImmersiveApp: App {
    @State private var immersionStyle: ImmersionStyle = .progressive(0.2...0.6, initial: 0.6)
    var body: some Scene {
        ImmersiveSpace { ... }
        .immersionStyle(selection: $immersionStyle, in: .progressive))
    }
}
```

The system initially uses a radial portal effect that replaces passthrough in a portion of the field of view. People can interactively adjust the size of the portal by turning the Digital Crown, including down to a minimum amount of immersion defined by the app and up to the defined maximum amount of immersion.
