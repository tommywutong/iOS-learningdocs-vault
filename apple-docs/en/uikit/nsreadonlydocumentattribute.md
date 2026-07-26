---
title: NSReadOnlyDocumentAttribute
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsreadonlydocumentattribute
source_url: 'https://developer.apple.com/documentation/uikit/nsreadonlydocumentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsreadonlydocumentattribute.json'
content_hash: 'sha256:06daa27697ec50c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSReadOnlyDocumentAttribute

<sub>Global Variable</sub>

An indication of whether the document is read-only.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSAttributedStringDocumentAttributeKey const NSReadOnlyDocumentAttribute;
```

## Discussion

The value of this attribute is an [NSNumber](../foundation/nsnumber.md) object that contains an integer. A value of `1` indicates read-only. If the value is `0`, missing, or negative, the document doesn’t display as read-only.

This attribute is not related to the file system protection on the file. Instead, this attribute can affect how the file displays to the user.

The string constant in macOS 10.3 and earlier is `@"ReadOnly"`.

## See Also

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
- [NSSubjectDocumentAttribute](../appkit/nssubjectdocumentattribute.md) — The subject of the document.
- [NSTitleDocumentAttribute](../appkit/nstitledocumentattribute.md) — The document title.
