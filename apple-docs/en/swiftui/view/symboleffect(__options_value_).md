---
title: 'symbolEffect(_:options:value:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/symboleffect(_:options:value:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/symboleffect(_:options:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/symboleffect%28_%3Aoptions%3Avalue%3A%29.json'
content_hash: 'sha256:9b1d205ccab5a4de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# symbolEffect(_:options:value:)

<sub>Instance Method</sub>

Returns a new view with a symbol effect added to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func symbolEffect<T, U>(_ effect: T, options: SymbolEffectOptions = .default, value: U) -> some View where T : DiscreteSymbolEffect, T : SymbolEffect, U : Equatable

```

## Parameters

- `effect` — A symbol effect to add to the view. Existing effects added by ancestors of the view are preserved, but may be overridden by the new effect. Added effects will be applied to the [Image](../image.md) views contained by the child view.

- `value` — The value to monitor for changes, the animation is triggered each time the value changes.

## Return Value

A copy of the view with a symbol effect added.

## Discussion

The following example adds a bounce effect to two symbol images, the animation will play each time `counter` changes:

```swift
VStack {
    Image(systemName: "bolt.slash.fill")
    Image(systemName: "folder.fill.badge.person.crop")
}
.symbolEffect(.bounce, value: counter)
```

## See Also

### Managing symbol effects

- [symbolEffect(_:options:isActive:)](<symboleffect(__options_isactive_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](<symboleffectsremoved(__).md>) — Returns a new view with its inherited symbol image effects either removed or left unchanged.
- [SymbolEffectTransition](../symboleffecttransition.md) — Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.
