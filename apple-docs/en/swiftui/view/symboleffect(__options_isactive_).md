---
title: 'symbolEffect(_:options:isActive:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/symboleffect(_:options:isactive:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/symboleffect(_:options:isactive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/symboleffect%28_%3Aoptions%3Aisactive%3A%29.json'
content_hash: 'sha256:0264b794f2603d32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# symbolEffect(_:options:isActive:)

<sub>Instance Method</sub>

Returns a new view with a symbol effect added to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func symbolEffect<T>(_ effect: T, options: SymbolEffectOptions = .default, isActive: Bool = true) -> some View where T : IndefiniteSymbolEffect, T : SymbolEffect

```

## Parameters

- `effect` — A symbol effect to add to the view. Existing effects added by ancestors of the view are preserved, but may be overridden by the new effect. Added effects will be applied to the [Image](../image.md) views contained by the child view.

- `isActive` — Whether the effect is active or inactive.

## Return Value

A copy of the view with a symbol effect added.

## Discussion

The following example adds a repeating pulse effect to two symbol images:

```swift
VStack {
    Image(systemName: "bolt.slash.fill")
    Image(systemName: "folder.fill.badge.person.crop")
}
.symbolEffect(.pulse)
```

## See Also

### Managing symbol effects

- [symbolEffect(_:options:value:)](<symboleffect(__options_value_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](<symboleffectsremoved(__).md>) — Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [SymbolEffectTransition](../symboleffecttransition.md) — Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.
