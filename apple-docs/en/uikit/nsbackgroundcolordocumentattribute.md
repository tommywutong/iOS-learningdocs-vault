---
title: NSBackgroundColorDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsbackgroundcolordocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nsbackgroundcolordocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsbackgroundcolordocumentattribute.json'
content_hash: 'sha256:146fe89bcd02f739'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSBackgroundColorDocumentAttribute

<sub>Global Variable</sub>

The background color of the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSBackgroundColorDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSColor](../appkit/nscolor.md) object representing the document-wide page background color.

The string constant in macOS 10.3 and earlier is `@"BackgroundColor"`.

For applications linked on versions prior to macOS 10.5, HTML import sets the `NSBackgroundColorDocumentAttribute` to `[NSColor whiteColor]` in cases in which the HTML does not specify a background color. For applications linked on macOS 10.5 and later, no `NSBackgroundColorDocumentAttribute` is set in these cases.

## See Also

### Getting document appearance keys

- [NSAppearanceDocumentAttribute](../appkit/nsappearancedocumentattribute.md) — The appearance of the document.
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
- [NSTextLayoutSectionsAttribute](nstextlayoutsectionsattribute.md) — The layout orientations for each section.
- [NSTopMarginDocumentAttribute](../appkit/nstopmargindocumentattribute.md) — The top margin of the document.
- [NSViewModeDocumentAttribute](nsviewmodedocumentattribute.md) — The view mode.
- [NSViewSizeDocumentAttribute](nsviewsizedocumentattribute.md) — The view size.
