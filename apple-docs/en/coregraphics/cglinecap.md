---
title: CGLineCap
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinecap
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinecap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinecap.json'
content_hash: 'sha256:4349d57af2018f19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGLineCap

<sub>Enumeration</sub>

Styles for rendering the endpoint of a stroked line.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGLineCap
```

## Overview

A line cap specifies the method used by [CGContextStrokePath](<cgcontext/strokepath().md>) to draw the endpoint of the line. To change the line cap style in a graphics context, you use the function [CGContextSetLineCap](<cgcontext/setlinecap(__).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGLineCapButt](cglinecap/butt.md) — A line with a squared-off end. Core Graphics draws the line to extend only to the exact endpoint of the path. This is the default.
- [kCGLineCapRound](cglinecap/round.md) — A line with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [kCGLineCapSquare](cglinecap/square.md) — A line with a squared-off end. Core Graphics extends the line beyond the endpoint of the path for a distance equal to half the line width.

### Initializers

- [init(rawValue:)](<cglinecap/init(rawvalue_).md>)
