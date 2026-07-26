---
title: 'init(symbol:converter:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/dimension/init(symbol:converter:)'
source_url: 'https://developer.apple.com/documentation/foundation/dimension/init(symbol:converter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dimension/init%28symbol%3Aconverter%3A%29.json'
content_hash: 'sha256:1f19e5a3ae67b011'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Dimension](../dimension.md)

# init(symbol:converter:)

<sub>Initializer</sub>

Initializes a dimensional unit with the symbol and unit converter you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(symbol: String, converter: UnitConverter)
```

## Parameters

- `symbol` — The symbol used to represent the unit.

- `converter` — The unit converter used to represent the unit in terms of the dimension’s base unit.

## Return Value

A new dimensional unit with the specified symbol and unit converter.

## Discussion

This is the designated initializer.
