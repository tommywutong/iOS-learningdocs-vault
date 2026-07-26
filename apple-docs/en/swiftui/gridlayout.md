---
title: GridLayout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gridlayout
source_url: 'https://developer.apple.com/documentation/swiftui/gridlayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gridlayout.json'
content_hash: 'sha256:738be830866aca7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GridLayout

<sub>Structure</sub>

A grid that you can use in conditional layouts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen nonisolated struct GridLayout
```

## Overview

This layout container behaves like a [Grid](grid.md), but conforms to the [Layout](layout.md) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](anylayout.md). If you don’t need a conditional layout, use [Grid](grid.md) instead.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a grid

- [init(alignment:horizontalSpacing:verticalSpacing:)](<gridlayout/init(alignment_horizontalspacing_verticalspacing_).md>) — Creates a grid with the specified spacing and alignment.

### Getting the grid’s properties

- [alignment](gridlayout/alignment.md) — The alignment of subviews.
- [horizontalSpacing](gridlayout/horizontalspacing.md) — The horizontal distance between adjacent subviews.
- [verticalSpacing](gridlayout/verticalspacing.md) — The vertical distance between adjacent subviews.

### Type Aliases

- [Body](gridlayout/body.md)

### Default Implementations

- [Layout Implementations](gridlayout/layout-implementations.md)

## See Also

### Transitioning between layout types

- [AnyLayout](anylayout.md) — A type-erased instance of the layout protocol.
- [HStackLayout](hstacklayout.md) — A horizontal container that you can use in conditional layouts.
- [VStackLayout](vstacklayout.md) — A vertical container that you can use in conditional layouts.
- [ZStackLayout](zstacklayout.md) — An overlaying container that you can use in conditional layouts.
