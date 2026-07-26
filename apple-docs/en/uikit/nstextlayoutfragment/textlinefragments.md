---
title: textLineFragments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutfragment/textlinefragments
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutfragment/textlinefragments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutfragment/textlinefragments.json'
content_hash: 'sha256:b4f6a87187f124f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutFragment](../nstextlayoutfragment.md)

# textLineFragments

<sub>Instance Property</sub>

An array of text line fragments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textLineFragments: [NSTextLineFragment] { get }
```

## Discussion

Valid when [NSTextLayoutFragmentStateLayoutAvailable](state-swift.enum/layoutavailable.md). This property is KVO-compliant.

## See Also

### Getting line fragments

- [EnumerationOptions](enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- textLineFragmentForTextLocation:isUpstreamAffinity:](<textlinefragment(for_isupstreamaffinity_).md>) — Returns a text line fragment from a specific text location in the document.
- [- textLineFragmentForVerticalOffset:requiresExactMatch:](<textlinefragment(forverticaloffset_requiresexactmatch_).md>) — Returns the text line fragment for the vertical offset you provide, or the closest text line fragment beyond the vertical offset.
