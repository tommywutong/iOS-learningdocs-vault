---
title: ZStackContent3D
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/zstackcontent3d
source_url: 'https://developer.apple.com/documentation/swiftui/zstackcontent3d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/zstackcontent3d.json'
content_hash: 'sha256:0751449a7a043a71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ZStackContent3D

<sub>Structure</sub>

A type that adds spacing to a [ZStack](zstack.md).

<sub>visionOS</sub>

```swift
@frozen nonisolated struct ZStackContent3D<Content> where Content : View
```

## Overview

You don’t create this type directly. SwiftUI creates it for you when you use the `ZStack(alignment:spacing:content)` initializer.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [View](view.md)

## Topics

### Initializers

- [init(spacing:content:)](<zstackcontent3d/init(spacing_content_).md>)

### Instance Properties

- [content](zstackcontent3d/content.md)
- [spacing](zstackcontent3d/spacing.md)
