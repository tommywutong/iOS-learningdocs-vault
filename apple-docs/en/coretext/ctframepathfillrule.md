---
title: CTFramePathFillRule
framework: Core Text
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframepathfillrule
source_url: 'https://developer.apple.com/documentation/coretext/ctframepathfillrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframepathfillrule.json'
content_hash: 'sha256:72a1adb196327c67'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTFramePathFillRule

<sub>Enumeration</sub>

These constants specify the fill rule used by a frame

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CTFramePathFillRule
```

## Overview

When a path intersects with itself, the client should specify which rule to use for deciding the area of the path.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kCTFramePathFillEvenOdd](ctframepathfillrule/evenodd.md) — Paints the area using the even-odd fill rule.
- [kCTFramePathFillWindingNumber](ctframepathfillrule/windingnumber.md) — Paints the area using the nonzero winding number rule.

### Initializers

- [init(rawValue:)](<ctframepathfillrule/init(rawvalue_).md>)
