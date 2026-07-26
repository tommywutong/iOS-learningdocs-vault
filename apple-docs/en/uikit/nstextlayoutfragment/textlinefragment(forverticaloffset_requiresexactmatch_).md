---
title: 'textLineFragment(forVerticalOffset:requiresExactMatch:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragment(forverticaloffset:requiresexactmatch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/textlinefragment%28forverticaloffset%3Arequiresexactmatch%3A%29.json'
content_hash: 'sha256:a9f5ebef311a03af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# textLineFragment(forVerticalOffset:requiresExactMatch:)

<sub>Instance Method</sub>

Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textLineFragment(forVerticalOffset verticalOffset: CGFloat, requiresExactMatch: Bool) -> NSTextLineFragment?
```

## Parameters

- `verticalOffset` — A float value that indicates a vertical distance, expressed in points, from the layout fragment frame’s origin.

- `requiresExactMatch` — A Boolean value that indicates whether the method returns an exact match, or returns the closest match if there isn’t an exact match. The default value is [true](../../swift/true.md).

## Return Value

A text line fragment, or `nil` if there isn’t a match.

## Discussion

Set `requiresExactMatch` to [true](../../swift/true.md) to find the text line fragment that contains the vertical offset, or set `requiresExactMatch` to [false](../../swift/false.md) to find the closest text line fragment matching or beyond the vertical offset. Returns `nil` if there isn’t a match.

## See Also

### Getting line fragments

- [textLineFragments](textlinefragments.md) — An array of text line fragments.
- [EnumerationOptions](enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- textLineFragmentForTextLocation:isUpstreamAffinity:](<textlinefragment(for_isupstreamaffinity_).md>) — Returns a text line fragment from a specific text location in the document.
