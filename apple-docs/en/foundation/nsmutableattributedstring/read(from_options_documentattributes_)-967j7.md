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
doc_path: '/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-967j7'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableattributedstring/read(from:options:documentattributes:)-967j7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableattributedstring/read%28from%3Aoptions%3Adocumentattributes%3A%29-967j7.json'
content_hash: 'sha256:05c65a11e75744c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableAttributedString](../nsmutableattributedstring.md)

# read(from:options:documentAttributes:)

<sub>Instance Method</sub>

Sets the contents of the receiver from the specified data object`.`

> [!warning] Deprecated
> Use [- readFromData:options:documentAttributes:error:](<read(from_options_documentattributes_)-5mbcx.md>) instead.

<sub>macOS</sub>

```swift
func read(from data: Data, options: [AnyHashable : Any] = [:], documentAttributes dict: AutoreleasingUnsafeMutablePointer<NSDictionary?>?) -> Bool
```

## Parameters

- `data` — The data to read.

- `options` — The option keys for importing the document. For a list of possible values, see “Option keys for importing documents” in [NSAttributedString](../nsattributedstring.md).

- `dict` — On return, contains the document attributes. For a list of possible values, see “Document Attributes” in [NSAttributedString](../nsattributedstring.md).

## Return Value

[true](../../swift/true.md) if the attributed string is created successfully or [false](../../swift/false.md) if it was not.

## See Also

### Deprecated

- [- readFromURL:options:documentAttributes:](<read(from_options_documentattributes_)-85y1d.md>) — Sets the contents of receiver from the file at the specified URL. _(deprecated)_
- [- readFromFileURL:options:documentAttributes:error:](<read(fromfileurl_options_documentattributes_).md>) — Sets the contents of the receiver from the file at the given URL. _(deprecated)_
