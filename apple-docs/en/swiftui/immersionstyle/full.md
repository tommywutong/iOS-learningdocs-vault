---
title: full
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 26.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersionstyle/full
source_url: 'https://developer.apple.com/documentation/swiftui/immersionstyle/full'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersionstyle/full.json'
content_hash: 'sha256:5d87bac2f057d749'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersionStyle](../immersionstyle.md)

# full

<sub>Type Property</sub>

An immersion style that displays unbounded content that completely replaces passthrough video.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) static var full: FullImmersionStyle { get }
```

## Discussion

When this immersion style is selected, the immersion amount reported by the closure of [onImmersionChange(initial:_:)](<../view/onimmersionchange(initial___).md>) is `1.0`.

Use the [immersionStyle(selection:in:)](<../scene/immersionstyle(selection_in_).md>) scene modifier to specify this style for an [ImmersiveSpace](../immersivespace.md).

When using this style, the space’s content fully obscures passthrough except for the user’s upper limbs. You can manage limb visibility separately by applying the [upperLimbVisibility(_:)](<../scene/upperlimbvisibility(__).md>) scene modifier to the space, or the view modifier equivalent to a view inside the scene.

The immersion style affects how windows interact with virtual objects in the environment. In `full` immersion, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is off.

## See Also

### Getting built-in styles

- [automatic](automatic.md) — The default immersion style.
- [mixed](mixed.md) — An immersion style that displays unbounded content intermixed with other app content, along with passthrough video.
- [progressive](progressive.md) — An immersion style that displays unbounded content that partially replaces passthrough video.
