---
title: 'drawHeaderForPage(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/drawheaderforpage(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawheaderforpage(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/drawheaderforpage%28at%3Ain%3A%29.json'
content_hash: 'sha256:ae4ad824dd8a42c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# drawHeaderForPage(at:in:)

<sub>Instance Method</sub>

Draws the header of a page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drawHeaderForPage(at pageIndex: Int, in headerRect: CGRect)
```

## Parameters

- `pageIndex` — The index of the page on which to draw the header.

- `headerRect` — The rectangle in which to draw the header content. This rectangle uses the coordinate system of the paper rectangle ([paperRect](paperrect.md)), with the origin of the coordinates at the top-left corner of the sheet.

## Discussion

The default implementation of this method does nothing. The system doesn’t call this method if [headerHeight](headerheight.md) isn’t a positive value. Override this method to draw the header of the specified page.

The system configures this method for drawing to the current graphics context according to [UIGraphicsGetCurrentContext](<../uigraphicsgetcurrentcontext().md>).

## See Also

### Drawing a page

- [- drawPageAtIndex:inRect:](<drawpage(at_in_).md>) — Draws a page of content for the printer.
- [- drawContentForPageAtIndex:inRect:](<drawcontentforpage(at_in_).md>) — Draws the content of a page.
- [- drawPrintFormatter:forPageAtIndex:](<drawprintformatter(__forpageat_).md>) — Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [- drawFooterForPageAtIndex:inRect:](<drawfooterforpage(at_in_).md>) — Draws the footer of a page.
