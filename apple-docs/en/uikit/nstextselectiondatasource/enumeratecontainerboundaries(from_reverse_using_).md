---
title: 'enumerateContainerBoundaries(from:reverse:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratecontainerboundaries(from:reverse:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/enumeratecontainerboundaries%28from%3Areverse%3Ausing%3A%29.json'
content_hash: 'sha256:ed7e63b5092c882e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# enumerateContainerBoundaries(from:reverse:using:)

<sub>Instance Method</sub>

Enumerates all the container boundaries starting from the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func enumerateContainerBoundaries(from location: any NSTextLocation, reverse: Bool, using block: (any NSTextLocation, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `location` — The location where the enumeration starts.

- `reverse` — A Boolean value that indicates the enumeration starts at the end of the container.

- `block` — AA closure to invoke to evaluate the container boundaries; end the enumeration early by returning `false`.

## Discussion

This is an optional method you implement to enumerate the text up to the container or page boundary when the text selection data provider supports this layout functionality.

## See Also

### Enumerating components of the selection

- [- enumerateCaretOffsetsInLineFragmentAtLocation:usingBlock:](<enumeratecaretoffsetsinlinefragment(at_using_).md>) — Enumerates all the insertion point caret offsets from left to right in visual order.
- [- enumerateSubstringsFromLocation:options:usingBlock:](<enumeratesubstrings(from_options_using_).md>) — Enumerates the textual segment boundaries starting at the location you specify.
