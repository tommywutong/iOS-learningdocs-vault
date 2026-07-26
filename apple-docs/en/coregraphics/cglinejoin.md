---
title: CGLineJoin
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cglinejoin
source_url: 'https://developer.apple.com/documentation/coregraphics/cglinejoin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cglinejoin.json'
content_hash: 'sha256:af69fa059b972bba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGLineJoin

<sub>Enumeration</sub>

Junction types for stroked lines.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGLineJoin
```

## Overview

A line join specifies how [CGContextStrokePath](<cgcontext/strokepath().md>) draws the junction between connected line segments. To set the line join style in a graphics context, you use the function [CGContextSetLineJoin](<cgcontext/setlinejoin(__).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGLineJoinMiter](cglinejoin/miter.md)
- [kCGLineJoinRound](cglinejoin/round.md) — A join with a rounded end. Core Graphics draws the line to extend beyond the endpoint of the path. The line ends with a semicircular arc with a radius of 1/2 the line’s width, centered on the endpoint.
- [kCGLineJoinBevel](cglinejoin/bevel.md) — A join with a squared-off end. Core Graphics draws the line to extend beyond the endpoint of the path, for a distance of 1/2 the line’s width.

### Initializers

- [init(rawValue:)](<cglinejoin/init(rawvalue_).md>)
