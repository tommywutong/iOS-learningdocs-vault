---
title: ScrollInputKind
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollinputkind
source_url: 'https://developer.apple.com/documentation/swiftui/scrollinputkind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollinputkind.json'
content_hash: 'sha256:51bb3fd1e62080e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollInputKind

<sub>Structure</sub>

Inputs used to scroll views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollInputKind
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [handGestureShortcut](scrollinputkind/handgestureshortcut.md) — A finger or wrist movement that the user can perform in order to scroll a view.
- [look](scrollinputkind/look.md) — On visionOS, by looking at the edge of a scroll view the content can automatically scroll. The axes will be determined automatically.

### Type Methods

- [look(axes:)](<scrollinputkind/look(axes_).md>) — On visionOS, by looking at the edge of a scroll view the content can automatically scroll. This contructor method takes a set of the scrollable axes.

## See Also

### Managing scrolling for different inputs

- [scrollInputBehavior(_:for:)](<view/scrollinputbehavior(__for_).md>) — Enables or disables scrolling in scrollable views when using particular inputs.
- [ScrollInputBehavior](scrollinputbehavior.md) — A type that defines whether input should scroll a view.
