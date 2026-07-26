---
title: CGPathDrawingMode
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathdrawingmode
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathdrawingmode.json'
content_hash: 'sha256:d60b0aa2e4212531'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathDrawingMode

<sub>Enumeration</sub>

Options for rendering a path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGPathDrawingMode
```

## Overview

You can pass a path drawing mode constant to the function [CGContextDrawPath](<cgcontext/drawpath(using_).md>) to specify how Core Graphics should paint a graphics context’s current path.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGPathFill](cgpathdrawingmode/fill.md) — Render the area contained within the path using the non-zero winding number rule.
- [kCGPathEOFill](cgpathdrawingmode/eofill.md) — Render the area within the path using the even-odd rule.
- [kCGPathStroke](cgpathdrawingmode/stroke.md) — Render a line along the path.
- [kCGPathFillStroke](cgpathdrawingmode/fillstroke.md) — First fill and then stroke the path, using the nonzero winding number rule.
- [kCGPathEOFillStroke](cgpathdrawingmode/eofillstroke.md) — First fill and then stroke the path, using the even-odd rule.

### Initializers

- [init(rawValue:)](<cgpathdrawingmode/init(rawvalue_).md>)

## See Also

### Drawing the Current Graphics Path

- [CGContextDrawPath](<cgcontext/drawpath(using_).md>) — Draws the current path using the provided drawing mode.
- [fillPath(using:)](<cgcontext/fillpath(using_).md>) — Paints the area within the current path, as determined by the specified fill rule.
- [CGContextStrokePath](<cgcontext/strokepath().md>) — Paints a line along the current path.
