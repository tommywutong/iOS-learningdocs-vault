---
title: 'value(fromBaseUnitValue:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/unitconverter/value(frombaseunitvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/unitconverter/value(frombaseunitvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitconverter/value%28frombaseunitvalue%3A%29.json'
content_hash: 'sha256:dbcfb1ec9e029645'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UnitConverter](../unitconverter.md)

# value(fromBaseUnitValue:)

<sub>Instance Method</sub>

For a given unit, returns the specified value of the base unit in terms of that unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(fromBaseUnitValue baseUnitValue: Double) -> Double
```

## Parameters

- `baseUnitValue` — The value in terms of the base unit.

## Return Value

The value in terms of a given unit.

## Discussion

This method takes a value in the base unit of a unit’s dimension and returns the result of converting it into that unit. For example, a converter for the pounds unit calling this method, passing `2.20462` to the `baseUnitValue` parameter, results in `1.0` (_2.20462 lbs = 1 kg_).

## See Also

### Converting Between Units

- [- baseUnitValueFromValue:](<baseunitvalue(fromvalue_).md>) — For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.
