---
title: kCGPDFContextEncryptionKeyLength
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextencryptionkeylength
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextencryptionkeylength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextencryptionkeylength.json'
content_hash: 'sha256:4a2cddc51280eb32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextEncryptionKeyLength

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextEncryptionKeyLength: CFString
```

## Discussion

The encryption key length in bits; see Table 3.18 “Entries  common to all encryption dictionaries”, PDF Reference: Adobe PDF version 1.5 (4th ed.) for more information. Optional; if present, the value of this key  must be a [CFNumber](../corefoundation/cfnumber.md) object with value which is a multiple of 8 between 40 and  128, inclusive. If this key is absent or invalid, the encryption key  length defaults to 40 bits.

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
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
