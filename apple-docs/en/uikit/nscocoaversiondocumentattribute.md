---
title: NSCocoaVersionDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscocoaversiondocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nscocoaversiondocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscocoaversiondocumentattribute.json'
content_hash: 'sha256:e1ffbc50967443b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCocoaVersionDocumentAttribute

<sub>Global Variable</sub>

The version of Cocoa that created the file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSCocoaVersionDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing a float. For RTF files only, stores the version of Cocoa with which the file was created. Absence of this value indicates an RTF file was not created by Cocoa or its predecessors.

Values less than `100` are pre–macOS; `100` is macOS 10.0 or 10.1; `102` is macOS 10.2 and 10.3; values greater than `102` correspond to values of `NSAppKitVersionNumber` in macOS 10.4 and later.

The string constant in macOS 10.3 and earlier is `@"CocoaRTFVersion"`.

## See Also

### Getting document metadata keys

- [NSAuthorDocumentAttribute](../appkit/nsauthordocumentattribute.md) — The author of the document.
- [NSCategoryDocumentAttribute](../appkit/nscategorydocumentattribute.md) — The document’s category.
- [NSCharacterEncodingDocumentAttribute](nscharacterencodingdocumentattribute.md) — The string encoding for the document.
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
