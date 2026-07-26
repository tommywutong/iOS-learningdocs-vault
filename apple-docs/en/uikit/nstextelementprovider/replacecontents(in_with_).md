---
title: 'replaceContents(in:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextelementprovider/replacecontents(in:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider/replacecontents(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider/replacecontents%28in%3Awith%3A%29.json'
content_hash: 'sha256:47133de2192182e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextElementProvider](../nstextelementprovider.md)

# replaceContents(in:with:)

<sub>Instance Method</sub>

Replaces the characters specified by range with the text elements you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replaceContents(in range: NSTextRange, with textElements: [NSTextElement]?)
```

## Parameters

- `range` — An [NSTextRange](../nstextrange.md).

- `textElements` — The elements to replace that characters at `range`.

## Discussion

If the edges of `range` aren’t at existing element range boundaries, the method either splits the element if it allows the operation (for example, [NSTextParagraph](../nstextparagraph.md)), or the adjusts the replacement range.

> [!note] Note
> This method is for use by [NSTextLayoutManager](../nstextlayoutmanager.md).

## See Also

### Accessing and updating the text

- [- enumerateTextElementsFromLocation:options:usingBlock:](<enumeratetextelements(from_options_using_).md>) — Enumerates text elements starting at the text location you provide.
- [EnumerationOptions](../nstextlayoutfragment/enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- locationFromLocation:withOffset:](<location(__offsetby_).md>) — Returns a new location from location with offset you provide.
