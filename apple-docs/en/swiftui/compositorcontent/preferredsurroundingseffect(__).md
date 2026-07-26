---
title: 'preferredSurroundingsEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/compositorcontent/preferredsurroundingseffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/compositorcontent/preferredsurroundingseffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/compositorcontent/preferredsurroundingseffect%28_%3A%29.json'
content_hash: 'sha256:3ad8081942262d0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CompositorContent](../compositorcontent.md)

# preferredSurroundingsEffect(_:)

<sub>Instance Method</sub>

Applies an effect to passthrough video.

<sub>macOS, visionOS</sub>

```swift
nonisolated func preferredSurroundingsEffect(_ effect: SurroundingsEffect?) -> some CompositorContent

```

## Parameters

- `effect` — The effect that you want to apply.

## Return Value

A CompositorContent that exhibits the specified preference.

## Discussion

Use this modifier to indicate a preference for the appearance of passthrough video when displaying the modified compositor content. For example, you can enhance the immersiveness of a scene that uses the default [mixed](../immersionstyle/mixed.md) immersion style by applying the [systemDark](../surroundingseffect/systemdark.md) preference to a compositor content inside the scene.

This also dims passthrough video, which helps to draw attention to the scene’s virtual content while still enabling people to remain aware of their surroundings.

> [!note] Note
> This modifier expresses a preference, but the system might not be able to honor it.

Use a value of `nil` to indicate that you have no preference. You typically do this to counteract a preference expressed by something lower in the view hierarchy.
