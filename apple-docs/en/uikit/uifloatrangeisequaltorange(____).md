---
title: 'UIFloatRangeIsEqualToRange(_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+（12.0 起废弃）, iPadOS 7.0+（12.0 起废弃）, Mac Catalyst 7.0+（12.0 起废弃）, tvOS, visionOS, Swift 1.0+（4.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uifloatrangeisequaltorange(_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrangeisequaltorange(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrangeisequaltorange%28_%3A_%3A%29.json'
content_hash: 'sha256:c123f4e345e10958'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFloatRangeIsEqualToRange(_:_:)

<sub>Function</sub>

Returns a Boolean indicating whether two float ranges are equivalent.

> [!warning] Deprecated
> Use `==` instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func UIFloatRangeIsEqualToRange(_ range: UIFloatRange, _ otherRange: UIFloatRange) -> Bool
```

## Parameters

- `range` — The first range to compare.

- `otherRange` — The second range to compare.

## Discussion

Two ranges are considered equal when their minimum values are the same and their maximum values are the same. In practice, the minimum and maximum values do not have to be exactly equal, but the difference between each pair of values must be less than `FLT_EPSILON`.

## See Also

### Testing the range values

- [UIFloatRangeIsInfinite](uifloatrange/isinfinite.md) — Returns a Boolean indicating whether the specified float range is infinitely large.
