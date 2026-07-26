---
title: viewPrintFormatter()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/viewprintformatter()
source_url: 'https://developer.apple.com/documentation/uikit/uiview/viewprintformatter()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/viewprintformatter%28%29.json'
content_hash: 'sha256:c4d9cd718eb37a69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# viewPrintFormatter()

<sub>Instance Method</sub>

Returns a print formatter for the receiving view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func viewPrintFormatter() -> UIViewPrintFormatter
```

## Return Value

A [UIViewPrintFormatter](../uiviewprintformatter.md) object or `nil` if the object could not be created. If it is successfully created, the returned object is automatically associated with this view.

## Discussion

When initiating a print job, you can call this method to obtain an appropriate view print formatter object for your view. You can use the formatter object to configure the page layout options for your view during printing. Each time you call this method, you get a unique view print formatter object.

For more information about how to use print formatters to configure the printing behavior of your view, see [Drawing and Printing Guide for iOS](https://developer.apple.com/library/archive/documentation/2DDrawing/Conceptual/DrawingPrintingiOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010156).

## See Also

### Formatting printed view content

- [- drawRect:forViewPrintFormatter:](<draw(__for_).md>) — Implemented to draw the view’s content for printing.
