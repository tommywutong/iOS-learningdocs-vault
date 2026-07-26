---
title: AttributedString.LineHeight
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/lineheight
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/lineheight'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/lineheight.json'
content_hash: 'sha256:a576d73bd3aa308a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.LineHeight

<sub>Structure</sub>

The line height definition of a paragraph.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LineHeight
```

## Overview

The line height defines the distance between the baselines of two subsequent lines of text.

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [loose](lineheight/loose.md) — Constant line height based on a multiple of the point size that is perceived as loose.
- [normal](lineheight/normal.md) — Constant line height based on a multiple of the point size that is perceived as normal.
- [tight](lineheight/tight.md) — Constant line height based on a multiple of the point size that is perceived as tight.
- [variable](lineheight/variable.md) — Variable line height based on font metrics.

### Type Methods

- [exact(points:)](<lineheight/exact(points_).md>) — Constant line height based on a fixed total.
- [leading(increase:)](<lineheight/leading(increase_).md>) — Constant line height based on point size and a fixed increase.
- [multiple(factor:)](<lineheight/multiple(factor_).md>) — Constant line height based on a multiple of the point size.
