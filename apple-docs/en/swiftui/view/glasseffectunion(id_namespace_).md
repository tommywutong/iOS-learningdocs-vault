---
title: 'glassEffectUnion(id:namespace:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/glasseffectunion(id:namespace:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/glasseffectunion(id:namespace:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/glasseffectunion%28id%3Anamespace%3A%29.json'
content_hash: 'sha256:0bb9c22e8ee749c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# glassEffectUnion(id:namespace:)

<sub>Instance Method</sub>

Associates any Liquid Glass effects defined within this view to a union with the provided identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@MainActor @preconcurrency func glassEffectUnion(id: (some Hashable & Sendable)?, namespace: Namespace.ID) -> some View

```

## Discussion

You may want the geometries of multiple views to contribute to a single Liquid Glass effect shape. In these cases, you can use a [glassEffectUnion(id:namespace:)](<glasseffectunion(id_namespace_).md>) to specify that a view should contribute to a union of Liquid Glass effects with a particular identifier. All Liquid Glass effects with the same shape and Liquid Glass variant will be combined into a single shape.

## See Also

### Styling views with Liquid Glass

- [Applying Liquid Glass to custom views](../applying-liquid-glass-to-custom-views.md) — Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](../landmarks-building-an-app-with-liquid-glass.md) — Enhance your app experience with system-provided and custom Liquid Glass.
- [glassEffect(_:in:)](<glasseffect(__in_).md>) — Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](<glasseffectid(__in_).md>) — Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectTransition(_:)](<glasseffecttransition(__).md>) — Associates a glass effect transition with any glass effects defined within this view.
- [interactive(_:)](<../glass/interactive(__).md>) — Returns a copy of the structure configured to be interactive.
- [GlassEffectContainer](../glasseffectcontainer.md) — A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [GlassEffectTransition](../glasseffecttransition.md) — A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [GlassButtonStyle](../glassbuttonstyle.md) — A button style that applies glass border artwork based on the button’s context.
- [GlassProminentButtonStyle](../glassprominentbuttonstyle.md) — A button style that applies prominent glass border artwork based on the button’s context.
- [DefaultGlassEffectShape](../defaultglasseffectshape.md) — The default shape applied by glass effects, a capsule.
