---
title: 'lineFragmentRange(for:inContainerAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/linefragmentrange(for:incontainerat:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/linefragmentrange(for:incontainerat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/linefragmentrange%28for%3Aincontainerat%3A%29.json'
content_hash: 'sha256:98108ddd19700f25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# lineFragmentRange(for:inContainerAt:)

<sub>Instance Method</sub>

Returns the range of the line fragment that contains the point you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func lineFragmentRange(for point: CGPoint, inContainerAt location: any NSTextLocation) -> NSTextRange?
```

## Parameters

- `point` — The starting point that contains the line fragment, in the coordinate system of `location`.

- `location` — The location of the line fragment.

## Return Value

An `NSTextRange` that describes the location of the line fragment, or nil if the range isn’t found.

## See Also

### Finding specific content in the selection

- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new location using the location and offset you specify.
- [- offsetFromLocation:toLocation:](<offset(from_to_).md>) — Returns the offset between the two locations you specify.
- [- textRangeForSelectionGranularity:enclosingLocation:](<textrange(for_enclosing_).md>) — Returns a text range that corresponds to selection granularity of the enclosing location.
