---
title: 'textLineFragment(for:isUpstreamAffinity:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragment(for:isupstreamaffinity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/textlinefragment%28for%3Aisupstreamaffinity%3A%29.json'
content_hash: 'sha256:d9f61036b27e3fc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# textLineFragment(for:isUpstreamAffinity:)

<sub>Instance Method</sub>

Returns a text line fragment from a specific text location in the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textLineFragment(for textLocation: any NSTextLocation, isUpstreamAffinity: Bool) -> NSTextLineFragment?
```

## Parameters

- `textLocation` — A text location that a text line fragment contains.

- `isUpstreamAffinity` — A Boolean value that indicates whether the text line fragment ends at the text location you provide.

## Return Value

The text line fragment that contains or ends at the text location you provide, or `nil` if there isn’t a match.

## Discussion

Set `isUpstreamAffinity` to [true](../../swift/true.md) to find a text fragment by its element range end location, such as when you enumerate over line fragments in reverse order. Set `isUpstreamAffinity` to [false](../../swift/false.md) to find a text fragment that contains `textLocation`.

## See Also

### Getting line fragments

- [textLineFragments](textlinefragments.md) — An array of text line fragments.
- [EnumerationOptions](enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- textLineFragmentForVerticalOffset:requiresExactMatch:](<textlinefragment(forverticaloffset_requiresexactmatch_).md>) — Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.
