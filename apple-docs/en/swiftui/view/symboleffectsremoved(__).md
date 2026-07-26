---
title: 'symbolEffectsRemoved(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/symboleffectsremoved(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/symboleffectsremoved(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/symboleffectsremoved%28_%3A%29.json'
content_hash: 'sha256:caab8ada45049778'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# symbolEffectsRemoved(_:)

<sub>Instance Method</sub>

Returns a new view with its inherited symbol image effects either removed or left unchanged.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func symbolEffectsRemoved(_ isEnabled: Bool = true) -> some View

```

## Parameters

- `isEnabled` — Whether to remove inherited symbol effects or not.

## Return Value

A copy of the view with its symbol effects either removed or left unchanged.

## Discussion

The following example adds a repeating pulse effect to two symbol images, but then disables the effect on one of them:

```swift
VStack {
    Image(systemName: "bolt.slash.fill") // does not pulse
        .symbolEffectsRemoved()
    Image(systemName: "folder.fill.badge.person.crop") // pulses
}
.symbolEffect(.pulse)
```

## See Also

### Managing symbol effects

- [symbolEffect(_:options:isActive:)](<symboleffect(__options_isactive_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffect(_:options:value:)](<symboleffect(__options_value_).md>) — Returns a new view with a symbol effect added to it.
- [SymbolEffectTransition](../symboleffecttransition.md) — Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.
