---
title: 'setRootElement(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/setrootelement(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/setrootelement(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/setrootelement%28_%3A%29.json'
content_hash: 'sha256:b25eb6493d5e4063'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# setRootElement(_:)

<sub>Instance Method</sub>

Set the root element of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func setRootElement(_ root: XMLElement)
```

## Parameters

- `root` — An [XMLNode](../xmlnode.md) object that is to be the root element.

## Discussion

As a side effect, this method removes all other children, including `NSXMLNode` objects representing comments and processing-instructions.

## See Also

### Managing the Root Element

- [- rootElement](<rootelement().md>) — Returns the root element of the receiver.
