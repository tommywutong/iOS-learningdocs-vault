---
title: Date.FormatStyle.Symbol.Hour.AMPMStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/hour/ampmstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/hour/ampmstyle.json'
content_hash: 'sha256:b48d77a91c60cc9c'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Hour](../hour.md)

# Date.FormatStyle.Symbol.Hour.AMPMStyle

<sub>Structure</sub>

The format style of the string representation of the day period, before or after noon, in a date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AMPMStyle
```

## Overview

Possible values for this style are: [omitted](ampmstyle/omitted.md), [narrow](ampmstyle/narrow.md), [abbreviated](ampmstyle/abbreviated.md), and [wide](ampmstyle/wide.md).

## Relationships

- **Conforms To**: [Decodable](../../../../../swift/decodable.md), [Encodable](../../../../../swift/encodable.md), [Equatable](../../../../../swift/equatable.md), [Hashable](../../../../../swift/hashable.md), [Sendable](../../../../../swift/sendable.md), [SendableMetatype](../../../../../swift/sendablemetatype.md)

## Topics

### Creating AMPM Styles

- [abbreviated](ampmstyle/abbreviated.md) — A type that specifies the abbreviated day period for when the locale prefers using day period with hour.
- [narrow](ampmstyle/narrow.md) — A type that specifies the narrow day period if the locale prefers using day period with hour.
- [omitted](ampmstyle/omitted.md) — A type that hides the day period marker.
- [wide](ampmstyle/wide.md) — A type that represents the wide day period if the locale prefers using day period with hour.

### Comparing AMPM Styles

- [==(_:_:)](<../../../==(____).md>) — Returns true if the two `Date` values represent the same point in time.
