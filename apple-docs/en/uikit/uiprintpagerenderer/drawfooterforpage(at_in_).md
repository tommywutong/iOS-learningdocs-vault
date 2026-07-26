---
title: 'drawFooterForPage(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/drawfooterforpage(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawfooterforpage(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/drawfooterforpage%28at%3Ain%3A%29.json'
content_hash: 'sha256:e8abdcceb26bc185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# drawFooterForPage(at:in:)

<sub>Instance Method</sub>

Draws the footer of a page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drawFooterForPage(at pageIndex: Int, in footerRect: CGRect)
```

## Parameters

- `pageIndex` — The index of the page on which to draw the footer content.

- `footerRect` — The rectangle in which to draw the footer content. This rectangle uses the coordinate system of the paper rectangle ([paperRect](paperrect.md)), with the origin of the coordinates at the top-left corner of the sheet.

## Discussion

The default implementation of this method does nothing. The system doesn’t call this method if [footerHeight](footerheight.md) isn’t a positive value. Override this method to draw the footer of the specified page.

The system configures this method for drawing to the current graphics context according to [UIGraphicsGetCurrentContext](<../uigraphicsgetcurrentcontext().md>).

## See Also

### Drawing a page

- [- drawPageAtIndex:inRect:](<drawpage(at_in_).md>) — Draws a page of content for the printer.
- [- drawHeaderForPageAtIndex:inRect:](<drawheaderforpage(at_in_).md>) — Draws the header of a page.
- [- drawContentForPageAtIndex:inRect:](<drawcontentforpage(at_in_).md>) — Draws the content of a page.
- [- drawPrintFormatter:forPageAtIndex:](<drawprintformatter(__forpageat_).md>) — Performs custom drawing in addition to the specified print formatter’s drawing for a page.
