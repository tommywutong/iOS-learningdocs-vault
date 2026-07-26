---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/parsestrategy/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/parsestrategy/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/parsestrategy/parse%28_%3A%29.json'
content_hash: 'sha256:ac51f6c6ae022f2b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [ParseStrategy](../parsestrategy.md)

# parse(_:)

<sub>Instance Method</sub>

Returns a `Date` of a given string interpreted using the current settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: String) throws -> Date
```

## Parameters

- `value` — A string representation of a date.

## Return Value

A `Date` represented by `value`.

## Discussion

> [!danger] Throws
> Throws `NSFormattingError` if the string cannot be parsed.
