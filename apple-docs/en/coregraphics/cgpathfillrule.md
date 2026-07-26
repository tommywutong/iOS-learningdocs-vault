---
title: CGPathFillRule
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathfillrule
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathfillrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathfillrule.json'
content_hash: 'sha256:012d325ae7252b00'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathFillRule

<sub>Enumeration</sub>

Rules for determining which regions are interior to a path, used by the [fillPath(using:)](<cgcontext/fillpath(using_).md>) and [clip(using:)](<cgcontext/clip(using_).md>) methods.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGPathFillRule
```

## Overview

When filling a path, regions that a fill rule defines as interior to the path are painted. When clipping with a path, regions interior to the path remain visible after clipping.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md)

## Topics

### Enumeration Cases

- [CGPathFillRule.evenOdd](cgpathfillrule/evenodd.md) — A rule that considers a region to be interior to a path based on the number of times it is enclosed by path elements.
- [CGPathFillRule.winding](cgpathfillrule/winding.md) — A rule that considers a region to be interior to a path if the winding number for that region is nonzero.

## See Also

### Constants

- [CGTextEncoding](cgtextencoding.md) — Text encodings for fonts.
