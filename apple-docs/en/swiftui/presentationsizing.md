---
title: PresentationSizing
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationsizing
source_url: 'https://developer.apple.com/documentation/swiftui/presentationsizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationsizing.json'
content_hash: 'sha256:90071e4088d6dff9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PresentationSizing

<sub>Protocol</sub>

A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PresentationSizing
```

## Overview

You don’t need to define your own version of this protocol. The system implementations of [form](presentationsizing/form.md), [page](presentationsizing/page.md), and [fitted](presentationsizing/fitted.md) are conveniences that automatically adapt to different device and screen sizes. If you do want to define your own sizing, first consider using the modifiers `PresenationSizing/sticky(horizontal:vertical:)` and [fitted(horizontal:vertical:)](<presentationsizing/fitted(horizontal_vertical_).md>). For example, to define your own sizing that proposes a 400x400 square size:

```swift
protocol SquareSizing: PresentationSizing {
    func proposedSize(
        for subview: PresentationSizingRoot,
        context: PresentationSizingContext
    ) {
        .init(width: 400, height: 400)
    }
}

extension PresentationSizing where Self == SquareSizing {
    public static var square: Self { SquareSizing() }
}
```

Then, at the callsite, you can modify `.square` just like system sizings, for example, to fit its content vertically:

```swift
.presentationSizing(.square.fitted(horizontal: false, vertical: true))
```

> [!info] See Also
> [presentationSizing(_:)](<view/presentationsizing(__).md>)

## Relationships

- **Conforming Types**: [AutomaticPresentationSizing](automaticpresentationsizing.md), [FittedPresentationSizing](fittedpresentationsizing.md), [FormPresentationSizing](formpresentationsizing.md), [PagePresentationSizing](pagepresentationsizing.md)

## Topics

### Getting built-in presentation size

- [automatic](presentationsizing/automatic.md) — The default presentation sizing, appropriate for the platform.
- [fitted](presentationsizing/fitted.md) — The presentation sizing is dictated by the ideal size of the content
- [form](presentationsizing/form.md) — The size is appropriate for forms and slightly less wide than`.page`
- [page](presentationsizing/page.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.

### Creating custom presentation size

- [fitted(horizontal:vertical:)](<presentationsizing/fitted(horizontal_vertical_).md>)
- [proposedSize(for:context:)](<presentationsizing/proposedsize(for_context_).md>)
- [sticky(horizontal:vertical:)](<presentationsizing/sticky(horizontal_vertical_).md>) — Modifies self to be sticky in the specified dimensions — growing, but not shrinking.

### Supporting types

- [AutomaticPresentationSizing](automaticpresentationsizing.md) — The default presentation sizing, appropriate for the platform.
- [FittedPresentationSizing](fittedpresentationsizing.md) — The size of the presentation is dictated by the ideal size of the content.
- [FormPresentationSizing](formpresentationsizing.md) — The size is appropriate for forms and slightly less wide than`.page`
- [PagePresentationSizing](pagepresentationsizing.md) — The size is roughly the size of a page of paper, appropriate for informational or compositional content.

## See Also

### Adapting a presentation size

- [presentationCompactAdaptation(horizontal:vertical:)](<view/presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<view/presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [PresentationAdaptation](presentationadaptation.md) — Strategies for adapting a presentation to a different size class.
- [presentationSizing(_:)](<view/presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [PresentationSizingRoot](presentationsizingroot.md) — A proxy to a view provided to the presentation with a defined presentation size.
- [PresentationSizingContext](presentationsizingcontext.md) — Contextual information about a presentation.
