---
title: kCGPDFContextOutputIntents
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.4+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextoutputintents
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextoutputintents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextoutputintents.json'
content_hash: 'sha256:d53ce2b1f36cc140'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextOutputIntents

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextOutputIntents: CFString
```

## Discussion

Output intent dictionaries. This key is optional. If present, the value must be an array of one or more [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md) dictionaries. The array is added to the PDF document in the `/OutputIntents` entry in the PDF file’s document catalog. Each dictionary in the array must be of form specified for the [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md) key, except that only the first dictionary in the array is required to contain the “S” key with a value of `GTS_PDFX`. If both the [kCGPDFContextOutputIntent](kcgpdfcontextoutputintent.md) and [kCGPDFContextOutputIntents](kcgpdfcontextoutputintents.md) keys are specified, the former is ignored.

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
- [kCGPDFContextSubject](kcgpdfcontextsubject.md)
- [kCGPDFContextKeywords](kcgpdfcontextkeywords.md)
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
