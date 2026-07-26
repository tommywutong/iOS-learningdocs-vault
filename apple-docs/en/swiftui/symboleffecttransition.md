---
title: SymbolEffectTransition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symboleffecttransition
source_url: 'https://developer.apple.com/documentation/swiftui/symboleffecttransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symboleffecttransition.json'
content_hash: 'sha256:7d9d0abdb64eef83'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SymbolEffectTransition

<sub>Structure</sub>

Creates a transition that applies the Appear, Disappear, DrawOn or DrawOff symbol animation to symbol images within the inserted or removed view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @frozen @preconcurrency struct SymbolEffectTransition
```

## Overview

Other views are unaffected by this transition.

## Relationships

- **Conforms To**: [Transition](transition.md)

## Topics

### Creating a transition

- [init(effect:options:)](<symboleffecttransition/init(effect_options_).md>)

## See Also

### Managing symbol effects

- [symbolEffect(_:options:isActive:)](<view/symboleffect(__options_isactive_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffect(_:options:value:)](<view/symboleffect(__options_value_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](<view/symboleffectsremoved(__).md>) — Returns a new view with its inherited symbol image effects either removed or left unchanged.
