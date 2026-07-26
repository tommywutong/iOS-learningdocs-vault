---
title: NSTextLayoutSectionsAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutsectionsattribute
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutsectionsattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutsectionsattribute.json'
content_hash: 'sha256:0f75aa7dc08a7bc3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLayoutSectionsAttribute

<sub>Global Variable</sub>

The layout orientations for each section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSTextLayoutSectionsAttribute;
```

## Discussion

An [NSArray](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47205) containing [NSDictionary](../foundation/nsdictionary.md) objects, each dictionary describing a layout orientation section. The dictionary can have two attributes: [NSTextLayoutSectionOrientation](nstextlayoutsectionorientation.md) and [NSTextLayoutSectionRange](nstextlayoutsectionrange.md). When there is a gap between sections, it’s assumed to have [NSTextLayoutOrientationHorizontal](nslayoutmanager/textlayoutorientation/horizontal.md).

## See Also

### Getting document appearance keys

- [NSAppearanceDocumentAttribute](../appkit/nsappearancedocumentattribute.md) — The appearance of the document.
- [NSBackgroundColorDocumentAttribute](nsbackgroundcolordocumentattribute.md) — The background color of the document.
- [NSBottomMarginDocumentAttribute](../appkit/nsbottommargindocumentattribute.md) — The bottom margin of the document.
- [NSDefaultFontExcludedDocumentAttribute](nsdefaultfontexcludeddocumentattribute.md)
- [NSDefaultTabIntervalDocumentAttribute](nsdefaulttabintervaldocumentattribute.md) — The default tab stop interval for the document.
- [NSExcludedElementsDocumentAttribute](../appkit/nsexcludedelementsdocumentattribute.md) — The HTML elements to exclude in generated HTML.
- [NSHyphenationFactorDocumentAttribute](nshyphenationfactordocumentattribute.md) — The hyphenation factor of the document.
- [NSLeftMarginDocumentAttribute](../appkit/nsleftmargindocumentattribute.md) — The left margin of the document.
- [NSPaperMarginDocumentAttribute](nspapermargindocumentattribute.md) — The paper margin of the document.
- [NSPaperSizeDocumentAttribute](nspapersizedocumentattribute.md) — The paper size for the document.
- [NSPrefixSpacesDocumentAttribute](../appkit/nsprefixspacesdocumentattribute.md) — The number of spaces for indenting nested HTML elements.
- [NSRightMarginDocumentAttribute](../appkit/nsrightmargindocumentattribute.md) — The right margin of the document.
- [NSTopMarginDocumentAttribute](../appkit/nstopmargindocumentattribute.md) — The top margin of the document.
- [NSViewModeDocumentAttribute](nsviewmodedocumentattribute.md) — The view mode.
- [NSViewSizeDocumentAttribute](nsviewsizedocumentattribute.md) — The view size.
