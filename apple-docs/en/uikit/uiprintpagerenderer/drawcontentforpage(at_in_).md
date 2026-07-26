---
title: 'drawContentForPage(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/drawcontentforpage(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawcontentforpage(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/drawcontentforpage%28at%3Ain%3A%29.json'
content_hash: 'sha256:3f99419d2f50b3b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# drawContentForPage(at:in:)

<sub>Instance Method</sub>

Draws the content of a page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drawContentForPage(at pageIndex: Int, in contentRect: CGRect)
```

## Parameters

- `pageIndex` — The index of the page on which to draw content.

- `contentRect` — The area in which to draw content, in the coordinate system of the printable rectangle. This area is equal to [printableRect](printablerect.md) minus [headerHeight](headerheight.md) and [footerHeight](footerheight.md).

## Discussion

The default implementation of this method does nothing. Override this method to draw the content of the specified page.

The system configures this method for drawing to the current graphics context according to [UIGraphicsGetCurrentContext](<../uigraphicsgetcurrentcontext().md>).

## See Also

### Drawing a page

- [- drawPageAtIndex:inRect:](<drawpage(at_in_).md>) — Draws a page of content for the printer.
- [- drawHeaderForPageAtIndex:inRect:](<drawheaderforpage(at_in_).md>) — Draws the header of a page.
- [- drawPrintFormatter:forPageAtIndex:](<drawprintformatter(__forpageat_).md>) — Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [- drawFooterForPageAtIndex:inRect:](<drawfooterforpage(at_in_).md>) — Draws the footer of a page.
