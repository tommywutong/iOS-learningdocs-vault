---
title: kCGPDFContextUserPassword
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextuserpassword
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextuserpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextuserpassword.json'
content_hash: 'sha256:22680ad2b2aa6e3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextUserPassword

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextUserPassword: CFString
```

## Discussion

The user password of the PDF document. If the document is encrypted, then the value of this key will be the user password for the document. If not specified, the user password is the empty string. The value of this key must be a CFString object that can be represented in ASCII encoding; only the first 32 bytes will be used for the password. If the value of this key cannot be represented in ASCII, the document is not created and the creation function returns `NULL`.

## See Also

### Metadata Keys

- [kCGPDFContextAuthor](kcgpdfcontextauthor.md) — The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [kCGPDFContextCreator](kcgpdfcontextcreator.md) — The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [kCGPDFContextTitle](kcgpdfcontexttitle.md) — The corresponding value is a string that represents the title of the document. This key is optional.
- [kCGPDFContextOwnerPassword](kcgpdfcontextownerpassword.md)
- [kCGPDFContextAllowsPrinting](kcgpdfcontextallowsprinting.md) — Whether the document allows printing when unlocked with the user password.
- [kCGPDFContextAllowsCopying](kcgpdfcontextallowscopying.md) — Whether the document allows copying when unlocked with the user password.
- [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md)
- [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md)
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
