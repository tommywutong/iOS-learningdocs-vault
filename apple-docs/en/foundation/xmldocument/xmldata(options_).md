---
title: 'xmlData(options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/xmldata(options:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/xmldata(options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/xmldata%28options%3A%29.json'
content_hash: 'sha256:dcf33309b5f22d45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# xmlData(options:)

<sub>Instance Method</sub>

Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

<sub>Mac Catalyst, macOS</sub>

```swift
func xmlData(options: XMLNode.Options = []) -> Data
```

## Parameters

- `options` — One or more options (bit-OR’d if multiple) to affect the output of the document; see Constants for the valid output options.

## Discussion

The encoding used is based on the value returned from [characterEncoding](characterencoding.md).

## See Also

### Writing a Document as XML Data

- [XMLData](xmldata.md) — Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.
