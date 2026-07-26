---
title: 'fill(using:)'
framework: Core Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cgrect/fill(using:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cgrect/fill(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgrect/fill%28using%3A%29.json'
content_hash: 'sha256:3e1ff66f3a85e78b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGRect](../cgrect.md)

# fill(using:)

<sub>Instance Method</sub>

Fills this rect in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.

<sub>macOS</sub>

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.
