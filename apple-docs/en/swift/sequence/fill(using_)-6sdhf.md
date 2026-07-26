---
title: 'fill(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/fill(using:)-6sdhf'
source_url: 'https://developer.apple.com/documentation/swift/sequence/fill(using:)-6sdhf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/fill%28using%3A%29-6sdhf.json'
content_hash: 'sha256:167cb97822a2ca28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# fill(using:)

<sub>Instance Method</sub>

Fills this list of rects in the current NSGraphicsContext with that rect’s associated gray component value in the DeviceGray color space. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFillListWithGrays()`.

<sub>macOS</sub>

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.
