---
title: Subview.ContainerSizingOptions
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/subview/containersizingoptions
source_url: 'https://developer.apple.com/documentation/swiftui/subview/containersizingoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/subview/containersizingoptions.json'
content_hash: 'sha256:29dfd25d48e66919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Subview](../subview.md)

# Subview.ContainerSizingOptions

<sub>Enumeration</sub>

Options on how all subviews should be sized when in a container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ContainerSizingOptions
```

## Overview

> [!note] Note
> This option is not about the sizing considerations of a view being measured individually. Instead, this option describes the sizing characteristics of a group of subviews altogether, which also would only have actual effects when used in a container.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [Subview.ContainerSizingOptions.uniform(axis:)](<containersizingoptions/uniform(axis_).md>) — Subviews will share the same size.
- [Subview.ContainerSizingOptions.variable](containersizingoptions/variable.md) — Subviews will be sized individually.
