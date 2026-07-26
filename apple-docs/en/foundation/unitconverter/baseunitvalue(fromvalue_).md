---
title: 'baseUnitValue(fromValue:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/unitconverter/baseunitvalue(fromvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/unitconverter/baseunitvalue(fromvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitconverter/baseunitvalue%28fromvalue%3A%29.json'
content_hash: 'sha256:74671de7ceabf088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UnitConverter](../unitconverter.md)

# baseUnitValue(fromValue:)

<sub>Instance Method</sub>

For a given unit, returns the specified value of that unit in terms of the base unit of its dimension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func baseUnitValue(fromValue value: Double) -> Double
```

## Parameters

- `value` — The value in terms of a given unit.

## Return Value

The value in terms of the base unit.

## Discussion

This method takes a value in a particular unit and returns the result of converting it into the base unit of that unit’s dimension. For example, a converter for the miles unit calling this method, passing `1.0` to the `value` parameter, results in `1609.34` (_1 mi = 1609.34 m_).

## See Also

### Converting Between Units

- [- valueFromBaseUnitValue:](<value(frombaseunitvalue_).md>) — For a given unit, returns the specified value of the base unit in terms of that unit.
