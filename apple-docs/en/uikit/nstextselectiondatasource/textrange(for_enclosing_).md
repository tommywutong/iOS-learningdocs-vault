---
title: 'textRange(for:enclosing:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/textrange(for:enclosing:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/textrange(for:enclosing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/textrange%28for%3Aenclosing%3A%29.json'
content_hash: 'sha256:8def24035af182e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# textRange(for:enclosing:)

<sub>Instance Method</sub>

Returns a text range that corresponds to selection granularity of the enclosing location.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textRange(for selectionGranularity: NSTextSelection.Granularity, enclosing location: any NSTextLocation) -> NSTextRange?
```

## Parameters

- `selectionGranularity` — One of the possible [Granularity](../nstextselection/granularity-swift.enum.md) options.

- `location` — A location that encloses the text range of interest.

## Return Value

Returns the text range of the section, or `nil` when `documentRange.isEmpty` `true`.

## See Also

### Finding specific content in the selection

- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new location using the location and offset you specify.
- [- lineFragmentRangeForPoint:inContainerAtLocation:](<linefragmentrange(for_incontainerat_).md>) — Returns the range of the line fragment that contains the point you specify.
- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the offset between the two locations you specify.
