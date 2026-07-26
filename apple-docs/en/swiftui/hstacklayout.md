---
title: HStackLayout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/hstacklayout
source_url: 'https://developer.apple.com/documentation/swiftui/hstacklayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/hstacklayout.json'
content_hash: 'sha256:bc5cde332099b6b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# HStackLayout

<sub>Structure</sub>

A horizontal container that you can use in conditional layouts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct HStackLayout
```

## Overview

This layout container behaves like an [HStack](hstack.md), but conforms to the [Layout](layout.md) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](anylayout.md). If you don’t need a conditional layout, use [HStack](hstack.md) instead.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a horizontal stack

- [init(alignment:spacing:)](<hstacklayout/init(alignment_spacing_).md>) — Creates a horizontal stack with the specified spacing and vertical alignment.

### Getting the stack’s properties

- [alignment](hstacklayout/alignment.md) — The vertical alignment of subviews.
- [spacing](hstacklayout/spacing.md) — The distance between adjacent subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](anylayout.md) — A type-erased instance of the layout protocol.
- [VStackLayout](vstacklayout.md) — A vertical container that you can use in conditional layouts.
- [ZStackLayout](zstacklayout.md) — An overlaying container that you can use in conditional layouts.
- [GridLayout](gridlayout.md) — A grid that you can use in conditional layouts.
