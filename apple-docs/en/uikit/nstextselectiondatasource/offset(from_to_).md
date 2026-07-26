---
title: 'offset(from:to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/offset(from:to:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/offset(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/offset%28from%3Ato%3A%29.json'
content_hash: 'sha256:78b674726e853da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# offset(from:to:)

<sub>Instance Method</sub>

Returns the offset between the two locations you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func offset(from: any NSTextLocation, to: any NSTextLocation) -> Int
```

## Parameters

- `from` — The starting location.

- `to` — The ending location.

## See Also

### Finding specific content in the selection

- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new location using the location and offset you specify.
- [- lineFragmentRangeForPoint:inContainerAtLocation:](<linefragmentrange(for_incontainerat_).md>) — Returns the range of the line fragment that contains the point you specify.
- [- textRangeForSelectionGranularity:enclosingLocation:](<textrange(for_enclosing_).md>) — Returns a text range that corresponds to selection granularity of the enclosing location.
