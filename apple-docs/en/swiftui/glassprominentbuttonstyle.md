---
title: GlassProminentButtonStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glassprominentbuttonstyle
source_url: 'https://developer.apple.com/documentation/swiftui/glassprominentbuttonstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glassprominentbuttonstyle.json'
content_hash: 'sha256:ae5081a78ef21898'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GlassProminentButtonStyle

<sub>Structure</sub>

A button style that applies prominent glass border artwork based on the button’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
nonisolated struct GlassProminentButtonStyle
```

## Overview

You can also use [glassProminent](primitivebuttonstyle/glassprominent.md) to construct this style.

## Relationships

- **Conforms To**: [PrimitiveButtonStyle](primitivebuttonstyle.md)

## Topics

### Initializers

- [init()](<glassprominentbuttonstyle/init().md>) — Creates a prominent glass button style.

### Instance Methods

- [makeBody(configuration:)](<glassprominentbuttonstyle/makebody(configuration_).md>) — Creates a view that represents the body of a button.

## See Also

### Styling views with Liquid Glass

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md) — Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md) — Enhance your app experience with system-provided and custom Liquid Glass.
- [glassEffect(_:in:)](<view/glasseffect(__in_).md>) — Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](<view/glasseffectid(__in_).md>) — Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectTransition(_:)](<view/glasseffecttransition(__).md>) — Associates a glass effect transition with any glass effects defined within this view.
- [glassEffectUnion(id:namespace:)](<view/glasseffectunion(id_namespace_).md>) — Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [interactive(_:)](<glass/interactive(__).md>) — Returns a copy of the structure configured to be interactive.
- [GlassEffectContainer](glasseffectcontainer.md) — A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [GlassEffectTransition](glasseffecttransition.md) — A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [GlassButtonStyle](glassbuttonstyle.md) — A button style that applies glass border artwork based on the button’s context.
- [DefaultGlassEffectShape](defaultglasseffectshape.md) — The default shape applied by glass effects, a capsule.
