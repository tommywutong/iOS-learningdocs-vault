---
title: narrow
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/formatstyle/symbol/era/narrow
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/era/narrow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/symbol/era/narrow.json'
content_hash: 'sha256:6c976a688659a753'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [Foundation](../../../../../foundation.md) · [Date](../../../../date.md) · [FormatStyle](../../../formatstyle.md) · [Symbol](../../symbol.md) · [Era](../era.md)

# narrow

<sub>Type Property</sub>

A narrow representation of an era.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var narrow: Date.FormatStyle.Symbol.Era { get }
```

## Discussion

A custom format style conveying the shortest representation of an era. For example, `B` (_before Christ_) and `A` (_anno Domini_).

## See Also

### Modifying an Era

- [abbreviated](abbreviated.md) — An abbreviated representation of an era.
- [wide](wide.md) — A full representation of an era.
