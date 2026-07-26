---
title: VStackLayout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/vstacklayout
source_url: 'https://developer.apple.com/documentation/swiftui/vstacklayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/vstacklayout.json'
content_hash: 'sha256:b478951e153fa39b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VStackLayout

<sub>Structure</sub>

A vertical container that you can use in conditional layouts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct VStackLayout
```

## Overview

This layout container behaves like a [VStack](vstack.md), but conforms to the [Layout](layout.md) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](anylayout.md). If you don’t need a conditional layout, use [VStack](vstack.md) instead.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a vertical stack

- [init(alignment:spacing:)](<vstacklayout/init(alignment_spacing_).md>) — Creates a vertical stack with the specified spacing and horizontal alignment.

### Getting the stack’s properties

- [alignment](vstacklayout/alignment.md) — The horizontal alignment of subviews.
- [spacing](vstacklayout/spacing.md) — The distance between adjacent subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](anylayout.md) — A type-erased instance of the layout protocol.
- [HStackLayout](hstacklayout.md) — A horizontal container that you can use in conditional layouts.
- [ZStackLayout](zstacklayout.md) — An overlaying container that you can use in conditional layouts.
- [GridLayout](gridlayout.md) — A grid that you can use in conditional layouts.
