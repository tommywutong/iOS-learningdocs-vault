---
title: NSCharacterEncodingDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscharacterencodingdocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nscharacterencodingdocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscharacterencodingdocumentattribute.json'
content_hash: 'sha256:3cf219052b6273c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCharacterEncodingDocumentAttribute

<sub>Global Variable</sub>

The string encoding for the document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSCharacterEncodingDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object containing an integer specifying [NSStringEncoding](../foundation/nsstringencoding.md) for the file; default for plain text is the default encoding. This key in options can specify the string encoding for reading the data. Upon return, the document attributes can contain the actual encoding used. For writing methods, this value is used for generating the plain text data.

The string constant in macOS 10.3 and earlier is `@"CharacterEncoding"`.

## See Also

### Getting document metadata keys

- [NSAuthorDocumentAttribute](../appkit/nsauthordocumentattribute.md) — The author of the document.
- [NSCategoryDocumentAttribute](../appkit/nscategorydocumentattribute.md) — The document’s category.
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
