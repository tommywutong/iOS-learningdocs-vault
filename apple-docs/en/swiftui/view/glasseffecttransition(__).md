---
title: 'glassEffectTransition(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/glasseffecttransition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/glasseffecttransition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/glasseffecttransition%28_%3A%29.json'
content_hash: 'sha256:8c41ffbb8a47d7dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# glassEffectTransition(_:)

<sub>Instance Method</sub>

Associates a glass effect transition with any glass effects defined within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
@MainActor @preconcurrency func glassEffectTransition(_ transition: GlassEffectTransition) -> some View

```

## Discussion

You use this modifier with the [glassEffect(_:in:)](<glasseffect(__in_).md>) view modifier and [GlassEffectContainer](../glasseffectcontainer.md) view. When used together, SwiftUI will use the provided transition to apply changes to the glass effect when you add or remove views with these effects from the view hierarchy.

In the example below, the notepad image will transition into and out of the pencil image when the isExpanded variable changes.

```swift
var isExpanded: Bool
@Namespace private var namespace

var body: some View {
    GlassEffectContainer(spacing: 10.0) {
        HStack(spacing: 10.0) {
            Image(systemName: "pencil")
                .frame(width: 20.0, height: 20.0)
                .glassEffect()
                .glassEffectID("pencil", in: namespace)

                if isExpanded {
                    Image(systemName: "note")
                        .frame(width: 20.0, height: 20.0)
                        .glassEffect()
                        .glassEffectID("note", in: namespace)
                        .glassEffectTransition(.matchedGeometry)
                }
            }
        }
    }
}
```

## See Also

### Styling views with Liquid Glass

- [Applying Liquid Glass to custom views](../applying-liquid-glass-to-custom-views.md) — Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](../landmarks-building-an-app-with-liquid-glass.md) — Enhance your app experience with system-provided and custom Liquid Glass.
- [glassEffect(_:in:)](<glasseffect(__in_).md>) — Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](<glasseffectid(__in_).md>) — Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectUnion(id:namespace:)](<glasseffectunion(id_namespace_).md>) — Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [interactive(_:)](<../glass/interactive(__).md>) — Returns a copy of the structure configured to be interactive.
- [GlassEffectContainer](../glasseffectcontainer.md) — A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [GlassEffectTransition](../glasseffecttransition.md) — A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [GlassButtonStyle](../glassbuttonstyle.md) — A button style that applies glass border artwork based on the button’s context.
- [GlassProminentButtonStyle](../glassprominentbuttonstyle.md) — A button style that applies prominent glass border artwork based on the button’s context.
- [DefaultGlassEffectShape](../defaultglasseffectshape.md) — The default shape applied by glass effects, a capsule.
