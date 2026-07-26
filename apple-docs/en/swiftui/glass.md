---
title: Glass
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/glass
source_url: 'https://developer.apple.com/documentation/swiftui/glass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/glass.json'
content_hash: 'sha256:d5cfa68edefc5951'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Glass

<sub>Structure</sub>

A structure that defines the configuration of the Liquid Glass material.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
struct Glass
```

## Overview

You provide instances of a variant of Liquid Glass to the [glassEffect(_:in:)](<view/glasseffect(__in_).md>) view modifier:

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

You can combine Liquid Glass effects using a [GlassEffectContainer](glasseffectcontainer.md), which supports morphing views with this effect into each other based on the geometry of their associated views.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Methods

- [interactive(_:)](<glass/interactive(__).md>) — Returns a copy of the structure configured to be interactive.
- [tint(_:)](<glass/tint(__).md>) — Returns a copy of the structure with a configured tint color.

### Type Properties

- [clear](glass/clear.md) — The clear variant of glass.
- [identity](glass/identity.md) — The identity variant of glass. When applied, your content remains unaffected as if no glass effect was applied.
- [regular](glass/regular.md) — The regular variant of the Liquid Glass material.

## See Also

### Styling content

- [border(_:width:)](<view/border(__width_).md>) — Adds a border to this view with the specified style and width.
- [foregroundStyle(_:)](<view/foregroundstyle(__).md>) — Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](<view/foregroundstyle(____).md>) — Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](<view/foregroundstyle(______).md>) — Sets the primary, secondary, and tertiary levels of the foreground style.
- [backgroundStyle(_:)](<view/backgroundstyle(__).md>) — Sets the specified style to render backgrounds within the view.
- [backgroundStyle](environmentvalues/backgroundstyle.md) — An optional style that overrides the default system background style when set.
- [ShapeStyle](shapestyle.md) — A color or pattern to use when rendering a shape.
- [AnyShapeStyle](anyshapestyle.md) — A type-erased ShapeStyle value.
- [Gradient](gradient.md) — A color gradient represented as an array of color stops, each having a parametric location value.
- [MeshGradient](meshgradient.md) — A two-dimensional gradient defined by a 2D grid of positioned colors.
- [AnyGradient](anygradient.md) — A color gradient.
- [ShadowStyle](shadowstyle.md) — A style to use when rendering shadows.
