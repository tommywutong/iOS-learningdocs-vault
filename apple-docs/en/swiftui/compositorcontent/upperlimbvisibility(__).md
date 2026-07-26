---
title: 'upperLimbVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/upperlimbvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/upperlimbvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/upperlimbvisibility%28_%3A%29.json'
content_hash: 'sha256:2fc0c1e57f8bc234'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# upperLimbVisibility(_:)

<sub>Instance Method</sub>

Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](../immersivespace.md) scene is presented.

<sub>macOS, visionOS</sub>

```swift
nonisolated func upperLimbVisibility(_ preferredVisibility: Visibility) -> some CompositorContent

```

## Parameters

- `preferredVisibility` — A value indicating if the upper limbs should be visible. Use `.automatic` for a system-defined standard behavior, `.visible` to keep the upper limbs visible, and `.hidden` to hide the upper limbs.

## Discussion

The system can show the user’s upper limbs during fully immersive experiences, but you can also hide them, for example, in order to display virtual hands instead.

Note that this modifier only sets a preference and ultimately the system will decide if it will honor it or not. The system may be unable to honor the preference if the immersive space is currently not visible.
