---
title: kCGPDFContextOwnerPassword
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextownerpassword
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextownerpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextownerpassword.json'
content_hash: 'sha256:1ea4dd79bce4f373'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextOwnerPassword

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextOwnerPassword: CFString
```

## Discussion

The owner password of the PDF document. If this key is specified, the document is encrypted using the value as the owner password; otherwise, the document will not be encrypted. The value of this key must be a CFString object that can be represented in ASCII encoding. Only the first 32 bytes are used for the password. There is no default value for this key. If the value of this key cannot be represented in ASCII, the document is not created and the creation function returns `NULL`.

## See Also

### Metadata Keys

- [kCGPDFContextAuthor](kcgpdfcontextauthor.md) — The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [kCGPDFContextCreator](kcgpdfcontextcreator.md) — The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [kCGPDFContextTitle](kcgpdfcontexttitle.md) — The corresponding value is a string that represents the title of the document. This key is optional.
- [kCGPDFContextUserPassword](kcgpdfcontextuserpassword.md)
- [kCGPDFContextAllowsPrinting](kcgpdfcontextallowsprinting.md) — Whether the document allows printing when unlocked with the user password.
- [kCGPDFContextAllowsCopying](kcgpdfcontextallowscopying.md) — Whether the document allows copying when unlocked with the user password.
- [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md)
- [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md)
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
