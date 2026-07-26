---
title: 'enumerateSubstrings(from:options:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/enumeratesubstrings(from:options:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratesubstrings(from:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/enumeratesubstrings%28from%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:967376859ad55ae1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# enumerateSubstrings(from:options:using:)

<sub>Instance Method</sub>

Enumerates the textual segment boundaries starting at the location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateSubstrings(from location: any NSTextLocation, options: NSString.EnumerationOptions = [], using block: (String?, NSTextRange, NSTextRange?, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `location` — The location where the enumeration starts.

- `options` — One or more of the available [NSString.EnumerationOptions](../../foundation/nsstring/enumerationoptions.md).

- `block` — A closure to invoke to evaluate the substrings; end the enumeration early by returning `false`.

## Discussion

## See Also

### Enumerating components of the selection

- [- enumerateCaretOffsetsInLineFragmentAtLocation:usingBlock:](<enumeratecaretoffsetsinlinefragment(at_using_).md>) — Enumerates all the insertion point caret offsets from left to right in visual order.
- [- enumerateContainerBoundariesFromLocation:reverse:usingBlock:](<enumeratecontainerboundaries(from_reverse_using_).md>) — Enumerates all the container boundaries starting from the location you specify.
