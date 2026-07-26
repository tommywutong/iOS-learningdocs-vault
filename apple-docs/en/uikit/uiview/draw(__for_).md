---
title: 'draw(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/draw(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/draw(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/draw%28_%3Afor%3A%29.json'
content_hash: 'sha256:f9c6c36cdc38cfe0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# draw(_:for:)

<sub>Instance Method</sub>

Implemented to draw the view’s content for printing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func draw(_ rect: CGRect, for formatter: UIViewPrintFormatter)
```

## Parameters

- `rect` — A rectangle that defines the area for drawing printable content.

- `formatter` — An instance of [UIViewPrintFormatter](../uiviewprintformatter.md) obtained by calling the [- viewPrintFormatter](<viewprintformatter().md>) method.

## Discussion

You implement this method if you want a view’s printed content to appear differently than its displayed content. If you add a view print formatter to a print job but do not implement this method, the view’s [- drawRect:](<draw(__).md>) method is called to provide the content for printing.

For more information about how to implement a custom drawing routine for printed content, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

## See Also

### Formatting printed view content

- [- viewPrintFormatter](<viewprintformatter().md>) — Returns a print formatter for the receiving view.
