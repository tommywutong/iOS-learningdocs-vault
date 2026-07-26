---
title: 'enumerateCaretOffsetsInLineFragment(at:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextselectiondatasource/enumeratecaretoffsetsinlinefragment(at:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextselectiondatasource/enumeratecaretoffsetsinlinefragment%28at%3Ausing%3A%29.json'
content_hash: 'sha256:8e6e1831178df35d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextSelectionDataSource](../nstextselectiondatasource.md)

# enumerateCaretOffsetsInLineFragment(at:using:)

<sub>Instance Method</sub>

Enumerates all the insertion point caret offsets from left to right in visual order.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateCaretOffsetsInLineFragment(at location: any NSTextLocation, using block: (CGFloat, any NSTextLocation, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `location` — The `NSTextLocation` to start from.

- `block` — The closure to invoke once for each logical caret edge in the line fragment, in left-to-right visual order. End the enumeration early by returning `false`.

## Discussion

The `caretOffset` is in the coordinate system for the text container. When `leadingEdge` is `true`, it indicates that `caretOffset` is at the logical edge preceding the character. For left-to-right characters, the caret is on the left, and on the right for right-to-left characters.

## See Also

### Enumerating components of the selection

- [- enumerateContainerBoundariesFromLocation:reverse:usingBlock:](<enumeratecontainerboundaries(from_reverse_using_).md>) — Enumerates all the container boundaries starting from the location you specify.
- [- enumerateSubstringsFromLocation:options:usingBlock:](<enumeratesubstrings(from_options_using_).md>) — Enumerates the textual segment boundaries starting at the location you specify.
