---
title: 'location(_:offsetBy:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/location(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/location(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/location%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:406d4064bc553a1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# location(_:offsetBy:)

<sub>Instance Method</sub>

Returns a new location using the location and offset you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(_ location: any NSTextLocation, offsetBy offset: Int) -> (any NSTextLocation)?
```

## Parameters

- `location` — The starting location in the selection.

- `offset` — An offset that describes the extent of the new location.

## Return Value

A new `NSTextLocation, or nil` when the inputs don’t produce any legal location, such as when the input is an out of bounds index.

## Discussion

The offset value can be positive or negative indicating the logical direction.

## See Also

### Finding specific content in the selection

- [- lineFragmentRangeForPoint:inContainerAtLocation:](<linefragmentrange(for_incontainerat_).md>) — Returns the range of the line fragment that contains the point you specify.
- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the offset between the two locations you specify.
- [- textRangeForSelectionGranularity:enclosingLocation:](<textrange(for_enclosing_).md>) — Returns a text range that corresponds to selection granularity of the enclosing location.
