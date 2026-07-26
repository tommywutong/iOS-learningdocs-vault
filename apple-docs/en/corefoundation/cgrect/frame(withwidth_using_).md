---
title: 'frame(withWidth:using:)'
framework: Core Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cgrect/frame(withwidth:using:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cgrect/frame(withwidth:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cgrect/frame%28withwidth%3Ausing%3A%29.json'
content_hash: 'sha256:ebd6e4a8d4091748'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CGRect](../cgrect.md)

# frame(withWidth:using:)

<sub>Instance Method</sub>

Draws a frame around the inside of this rect in the current NSGraphicsContext in the context’s fill color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSFrameRect()`.

<sub>macOS</sub>

```swift
func frame(withWidth width: CGFloat = 1.0, using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.
