---
title: CGPathElementType
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathelementtype
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathelementtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathelementtype.json'
content_hash: 'sha256:9175634d2b91d2a1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathElementType

<sub>Enumeration</sub>

The type of element found in a path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGPathElementType
```

## Overview

For more information about paths, see [CGPath](cgpath.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGPathElementMoveToPoint](cgpathelementtype/movetopoint.md) — The path element that starts a new subpath.
- [kCGPathElementAddLineToPoint](cgpathelementtype/addlinetopoint.md) — The path element that adds a line from the current point to a new point.
- [kCGPathElementAddQuadCurveToPoint](cgpathelementtype/addquadcurvetopoint.md) — The path element that adds a quadratic curve from the current point to the specified point.
- [kCGPathElementAddCurveToPoint](cgpathelementtype/addcurvetopoint.md) — The path element that adds a cubic curve from the current point to the specified point.
- [kCGPathElementCloseSubpath](cgpathelementtype/closesubpath.md) — The path element that closes and completes a subpath. The element does not contain any points. See the function [CGPathCloseSubpath](<cgmutablepath/closesubpath().md>).

### Initializers

- [init(rawValue:)](<cgpathelementtype/init(rawvalue_).md>)

## See Also

### Applying a Function to the Elements of a Path

- [CGPathApply](<cgpath/apply(info_function_).md>) — For each element in a graphics path, calls a custom applier function.
- [CGPathApplierFunction](cgpathapplierfunction.md) — Defines a callback function that can view an element in a graphics path.
- [CGPathElement](cgpathelement.md) — A data structure that provides information about a path element.
