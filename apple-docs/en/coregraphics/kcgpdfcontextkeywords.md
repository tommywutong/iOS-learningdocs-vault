---
title: kCGPDFContextKeywords
framework: Core Graphics
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/kcgpdfcontextkeywords
source_url: 'https://developer.apple.com/documentation/coregraphics/kcgpdfcontextkeywords'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/kcgpdfcontextkeywords.json'
content_hash: 'sha256:2721c73d888f7121'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# kCGPDFContextKeywords

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCGPDFContextKeywords: CFString
```

## Discussion

The keywords for this document. This key is optional. If the value of  this key is a [CFString](../corefoundation/cfstring.md) object, the `/Keywords` entry will be the specified  string. If the value of this key is a [CFArray](../corefoundation/cfarray.md) object, then it must be an array  of [CFString](../corefoundation/cfstring.md) objects. The `/Keywords` entry will, in this case, be the concatenation  of the specified strings separated by commas (`","`). In addition, an  entry with the key `"/AAPL:Keywords"` is stored in the document  information dictionary; its value is an array consisting of each of the  specified strings. The value of this key must be in one of the above  forms; otherwise, this key is ignored.

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
- [kCGPDFContextEncryptionKeyLength](kcgpdfcontextencryptionkeylength.md)
