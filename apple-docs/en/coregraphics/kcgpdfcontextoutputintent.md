---
title: kCGPDFContextOutputIntent
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextoutputintent
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextoutputintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextoutputintent.json'
content_hash: 'sha256:143a259a0e565b92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextOutputIntent

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextOutputIntent: CFString
```

## Discussion

The output intent `PDF/X`. This key is optional. If present, the value of this key must be a CFDictionary object. The dictionary is added to the `/OutputIntents` entry in the PDF file document catalog. The keys and values contained in the dictionary must match those specified in section 9.10.4 of the PDF 1.4 specification, ISO/DIS 15930-3 document published by ISO/TC 130, and Adobe Technical Note #5413.

## See Also

### Metadata Keys

- [kCGPDFContextAuthor](kcgpdfcontextauthor.md) — The corresponding value is a string that represents the name of the person who created the document. This key is optional.
- [kCGPDFContextCreator](kcgpdfcontextcreator.md) — The corresponding value is a string that represents the name of the application used to produce the document. This key is optional.
- [kCGPDFContextTitle](kcgpdfcontexttitle.md) — The corresponding value is a string that represents the title of the document. This key is optional.
- [kCGPDFContextOwnerPassword](kcgpdfcontextownerpassword.md)
- [kCGPDFContextUserPassword](kcgpdfcontextuserpassword.md)
- [kCGPDFContextAllowsPrinting](kcgpdfcontextallowsprinting.md) — Whether the document allows printing when unlocked with the user password.
- [kCGPDFContextAllowsCopying](kcgpdfcontextallowscopying.md) — Whether the document allows copying when unlocked with the user password.
- [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md)
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
