---
title: ZStackLayout
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/zstacklayout
source_url: 'https://developer.apple.com/documentation/swiftui/zstacklayout'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/zstacklayout.json'
content_hash: 'sha256:4ad78996b650a7a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ZStackLayout

<sub>Structure</sub>

An overlaying container that you can use in conditional layouts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ZStackLayout
```

## Overview

This layout container behaves like a [ZStack](zstack.md), but conforms to the [Layout](layout.md) protocol so you can use it in the conditional layouts that you construct with [AnyLayout](anylayout.md). If you don’t need a conditional layout, use [ZStack](zstack.md) instead.

## Relationships

- **Conforms To**: [Animatable](animatable.md), [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Layout](layout.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a stack

- [init(alignment:)](<zstacklayout/init(alignment_).md>) — Creates a stack with the specified alignment.

### Getting the stack’s properties

- [alignment](zstacklayout/alignment.md) — The alignment of subviews.

## See Also

### Transitioning between layout types

- [AnyLayout](anylayout.md) — A type-erased instance of the layout protocol.
- [HStackLayout](hstacklayout.md) — A horizontal container that you can use in conditional layouts.
- [VStackLayout](vstacklayout.md) — A vertical container that you can use in conditional layouts.
- [GridLayout](gridlayout.md) — A grid that you can use in conditional layouts.
