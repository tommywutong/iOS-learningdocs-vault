---
title: Date.RelativeFormatStyle.Presentation
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/presentation-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/presentation-swift.struct.json'
content_hash: 'sha256:ae59178b7cfa7390'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# Date.RelativeFormatStyle.Presentation

<sub>Structure</sub>

A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Presentation
```

## Overview

Cases include `named` and `numeric`.

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Modifying Relative Date Style Presentations

- [named](presentation-swift.struct/named.md) — A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.
- [numeric](presentation-swift.struct/numeric.md) — A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.

### Comparing Relative Date Style Presentations

- [==(_:_:)](<../==(____).md>) — Returns true if the two `Date` values represent the same point in time.

## See Also

### Supporting Types

- [UnitsStyle](unitsstyle-swift.struct.md) — A type that represents the style to use when formatting the units of relative dates.
