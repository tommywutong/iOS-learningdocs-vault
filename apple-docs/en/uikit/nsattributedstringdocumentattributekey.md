---
title: NSAttributedStringDocumentAttributeKey
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsattributedstringdocumentattributekey
source_url: 'https://developer.apple.com/documentation/uikit/nsattributedstringdocumentattributekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsattributedstringdocumentattributekey.json'
content_hash: 'sha256:9b5b12ccf62e15a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSAttributedStringDocumentAttributeKey

<sub>Type Alias</sub>

The attributes you apply to an entire document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef NSString * NSAttributedStringDocumentAttributeKey;
```

## Discussion

The [NSAttributedStringDocumentAttributeKey](nsattributedstringdocumentattributekey.md) type defines attributes that apply to an entire attributed string, and not to specific ranges of characters. You specify these attributes when writing an attributed string to disk, or reading text from a file on disk. Use these attributes to specify metadata about the overall document, including its author or title, page margin details, font-scaling options for cross-platform interchange, and more.

## Topics

### Getting document type keys

- [NSDocumentTypeDocumentAttribute](nsdocumenttypedocumentattribute.md) — The document type.
- [NSFileTypeDocumentAttribute](../appkit/nsfiletypedocumentattribute.md) — The document type for interpreting the document.
- [NSTextEncodingNameDocumentAttribute](../appkit/nstextencodingnamedocumentattribute.md) — The name of the text encoding to use.

### Getting document metadata keys

- [NSAuthorDocumentAttribute](../appkit/nsauthordocumentattribute.md) — The author of the document.
- [NSCategoryDocumentAttribute](../appkit/nscategorydocumentattribute.md) — The document’s category.
- [NSCharacterEncodingDocumentAttribute](nscharacterencodingdocumentattribute.md) — The string encoding for the document.
- [NSCocoaVersionDocumentAttribute](nscocoaversiondocumentattribute.md) — The version of Cocoa that created the file.
- [NSCommentDocumentAttribute](../appkit/nscommentdocumentattribute.md) — The document comments.
- [NSCompanyDocumentAttribute](../appkit/nscompanydocumentattribute.md) — The company or organization name associated with the document.
- [NSConvertedDocumentAttribute](../appkit/nsconverteddocumentattribute.md) — A value that indicates whether a filter service converted the file.
- [NSCopyrightDocumentAttribute](../appkit/nscopyrightdocumentattribute.md) — The document’s copyright information.
- [NSCreationTimeDocumentAttribute](../appkit/nscreationtimedocumentattribute.md) — The creation date of the document.
- [NSEditorDocumentAttribute](../appkit/nseditordocumentattribute.md) — The name of person who last edited the document.
- [NSKeywordsDocumentAttribute](../appkit/nskeywordsdocumentattribute.md) — The document keywords.
- [NSManagerDocumentAttribute](../appkit/nsmanagerdocumentattribute.md) — The name of the author’s manager.
- [NSModificationTimeDocumentAttribute](../appkit/nsmodificationtimedocumentattribute.md) — The modification date of the document.
- [NSReadOnlyDocumentAttribute](nsreadonlydocumentattribute.md) — An indication of whether the document is read-only.
- [NSSubjectDocumentAttribute](../appkit/nssubjectdocumentattribute.md) — The subject of the document.
- [NSTitleDocumentAttribute](../appkit/nstitledocumentattribute.md) — The document title.

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
- [NSTextLayoutSectionsAttribute](nstextlayoutsectionsattribute.md) — The layout orientations for each section.
- [NSTopMarginDocumentAttribute](../appkit/nstopmargindocumentattribute.md) — The top margin of the document.
- [NSViewModeDocumentAttribute](nsviewmodedocumentattribute.md) — The view mode.
- [NSViewSizeDocumentAttribute](nsviewsizedocumentattribute.md) — The view size.
- [NSViewZoomDocumentAttribute](nsviewzoomdocumentattribute.md) — The view zoom.

### Getting the font-scaling options

- [NSSourceTextScalingDocumentAttribute](nssourcetextscalingdocumentattribute.md) — The text-scaling mode you used when creating the text.
- [NSTextScalingDocumentAttribute](nstextscalingdocumentattribute.md) — The text-scaling mode to use when displaying the text.

### Getting the default attributes

- [NSDefaultAttributesDocumentAttribute](nsdefaultattributesdocumentattribute.md) — The default document attributes.

## See Also

### Getting document-wide attributes

- [Document reading option keys](document-reading-option-keys.md) — Keys for constructing an attributed string from data on disk.
- [NSAttributedStringDocumentType](nsattributedstringdocumenttype.md) — Constants for the document type document attribute key.
- [NSTextLayoutSectionKey](nstextlayoutsectionkey.md) — Constants for the text layout sections document attribute key.
- [NSTextScalingType](nstextscalingtype.md) — Constants that specify the text scaling.
