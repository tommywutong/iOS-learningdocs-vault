---
title: UIFloatRangeIsEqualToRange
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifloatrangeisequaltorange
source_url: 'https://developer.apple.com/documentation/uikit/uifloatrangeisequaltorange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifloatrangeisequaltorange.json'
content_hash: 'sha256:8ed79f416e696dbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFloatRangeIsEqualToRange

<sub>Function</sub>

Returns a Boolean indicating whether two float ranges are equivalent.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
static BOOL UIFloatRangeIsEqualToRange(UIFloatRange range, UIFloatRange otherRange);
```

## Parameters

- `range` — The first range to compare.

- `otherRange` — The second range to compare.

## Discussion

Two ranges are considered equal when their minimum values are the same and their maximum values are the same. In practice, the minimum and maximum values do not have to be exactly equal, but the difference between each pair of values must be less than `FLT_EPSILON`.

## See Also

### Testing the range values

- [UIFloatRangeIsInfinite](uifloatrange/isinfinite.md) — Returns a Boolean indicating whether the specified float range is infinitely large.
