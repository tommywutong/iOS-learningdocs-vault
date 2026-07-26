---
title: symbol
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unit/symbol
source_url: 'https://developer.apple.com/documentation/foundation/unit/symbol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unit/symbol.json'
content_hash: 'sha256:3607b7765fb0eb28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Unit](../unit.md)

# symbol

<sub>Instance Property</sub>

The symbolic representation of the unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var symbol: String { get }
```

## Discussion

The symbol of a unit is a string that can be used to designate a number as a quantity of a particular unit in user-readable representations. Units typically have symbols that are abbreviated and standardized, so as to be easily and unambiguously conveyed. For example, the `milePerHour` unit has the symbol `mph`. If a unit does not have a standardized or well-understood symbol, the lowercase name of the unit can be used. For example, the `metricCup` unit has the symbol `metric cup`.

Unit symbols may incorporate a metric prefix to indicate a multiple or fraction of existing unit symbols. For example, the `kilogram` unit has the symbol `kg`, which uses the SI prefix k for kilo- to indicate a magnitude of 103 for the `gram` unit, and the `microgram` unit has the symbol `µg`, which uses the SI prefix µ for micro- to indicate a magnitude of 10-6 for the `gram` unit.
