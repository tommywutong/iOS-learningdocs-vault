---
title: UIRectCorner
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uirectcorner
source_url: 'https://developer.apple.com/documentation/uikit/uirectcorner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uirectcorner.json'
content_hash: 'sha256:f50bf13678586730'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRectCorner

<sub>Structure</sub>

The corners of a rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct UIRectCorner
```

## Overview

The specified constants reflect the corners of a rectangle that has not been modified by an affine transform and is drawn in the default coordinate system (where the origin is in the upper-left corner and positive values extend down and to the right).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIRectCornerTopLeft](uirectcorner/topleft.md) — The top-left corner of the rectangle.
- [UIRectCornerTopRight](uirectcorner/topright.md) — The top-right corner of the rectangle.
- [UIRectCornerBottomLeft](uirectcorner/bottomleft.md) — The bottom-left corner of the rectangle.
- [UIRectCornerBottomRight](uirectcorner/bottomright.md) — The bottom-right corner of the rectangle.
- [UIRectCornerAllCorners](uirectcorner/allcorners.md) — All corners of the rectangle.

### Initializer

- [init(rawValue:)](<uirectcorner/init(rawvalue_).md>) — Creates a structure that represents the corners of a rectangle.
