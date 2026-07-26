---
title: 'read(from:options:documentAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-85y1d'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-85y1d'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/read%28from%3Aoptions%3Adocumentattributes%3A%29-85y1d.json'
content_hash: 'sha256:306ee99990e3ac41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# read(from:options:documentAttributes:)

<sub>Instance Method</sub>

Sets the contents of receiver from the file at the specified URL.

> [!warning] Deprecated
> Use [- readFromURL:options:documentAttributes:error:](<read(from_options_documentattributes_)-54wth.md>) instead.

<sub>macOS</sub>

```swift
func read(from url: URL, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

## Parameters

- `url` — The URL of the document to open.

- `options` — The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [NSAttributedString](../nsattributedstring.md).

- `dict` — On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [NSAttributedString](../nsattributedstring.md).

## Return Value

[true](../../swift/true.md) if the attributed string is created successfully or [false](../../swift/false.md) if it was not.

## Discussion

Filter services can be used to convert the contents of the URL into a format recognized by Cocoa.

## See Also

### Deprecated

- [- readFromData:options:documentAttributes:](<read(from_options_documentattributes_)-967j7.md>) — Sets the contents of the receiver from the specified data object`.` _(deprecated)_
- [- readFromFileURL:options:documentAttributes:error:](<read(fromfileurl_options_documentattributes_).md>) — Sets the contents of the receiver from the file at the given URL. _(deprecated)_
