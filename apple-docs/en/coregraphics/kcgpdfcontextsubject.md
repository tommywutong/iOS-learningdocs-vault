---
title: kCGPDFContextSubject
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextsubject
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextsubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextsubject.json'
content_hash: 'sha256:de225b4546aafd0f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextSubject

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextSubject: CFString
```

## Discussion

The subject of a document. Optional; if present, the value of this key must be a [CFString](../corefoundation/cfstring.md) object.

## See Also

### Metadata Keys

- [kCGPDFContextAuthor](kcgpdfcontextauthor.md) — The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [kCGPDFContextCreator](kcgpdfcontextcreator.md) — The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [kCGPDFContextTitle](kcgpdfcontexttitle.md) — The corresponding value is a string that represents the title of the document. This key is optional.
- [kCGPDFContextOwnerPassword](kcgpdfcontextownerpassword.md)
- [kCGPDFContextUserPassword](kcgpdfcontextuserpassword.md)
- [kCGPDFContextAllowsPrinting](kcgpdfcontextallowsprinting.md) — Whether the document allows printing when unlocked with the user password.
- [kCGPDFContextAllowsCopying](kcgpdfcontextallowscopying.md) — Whether the document allows copying when unlocked with the user password.
- [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md)
- [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
