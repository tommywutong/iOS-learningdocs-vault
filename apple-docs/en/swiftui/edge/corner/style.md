---
title: Edge.Corner.Style
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/edge/corner/style
source_url: 'https://developer.apple.com/documentation/swiftui/edge/corner/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/edge/corner/style.json'
content_hash: 'sha256:5a68a0d5e858b75b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [Edge](../../edge.md) · [Corner](../corner.md)

# Edge.Corner.Style

<sub>Structure</sub>

A style that describes the corner of a rectangular shape.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Style
```

## Overview

A corner can be square, rounded with a fixed-radius curve, or rounded with a curve that’s concentric to the container shape. For more information on how to create a shape with configurable corner styles, see [ConcentricRectangle](../../concentricrectangle.md).

> [!info] See Also
> [ConcentricRectangle](../../concentricrectangle.md), [RoundedRectangularShape](../../roundedrectangularshape.md)

## Relationships

- **Conforms To**: [Animatable](../../animatable.md), [Copyable](../../../swift/copyable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [ExpressibleByFloatLiteral](../../../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../../../swift/expressiblebyintegerliteral.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [concentric](style/concentric.md) — A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius.

### Type Methods

- [concentric(minimum:)](<style/concentric(minimum_).md>) — A rounded corner style where the corner’s radius shares a center point with the container shape’s corner radius, with an optional minimum radius.
- [fixed(_:)](<style/fixed(__).md>) — A rounded corner style where the corner’s radius is the value you provide.

### Default Implementations

- [ExpressibleByFloatLiteral Implementations](style/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](style/expressiblebyintegerliteral-implementations.md)
