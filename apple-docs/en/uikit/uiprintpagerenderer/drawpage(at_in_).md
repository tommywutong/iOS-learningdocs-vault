---
title: 'drawPage(at:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/drawpage(at:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawpage(at:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/drawpage%28at%3Ain%3A%29.json'
content_hash: 'sha256:3efc9ac598c9fc80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# drawPage(at:in:)

<sub>Instance Method</sub>

Draws a page of content for the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drawPage(at pageIndex: Int, in printableRect: CGRect)
```

## Parameters

- `pageIndex` — The index of the page to draw.

- `printableRect` — The rectangle in which to draw printable content.

## Discussion

The default implementation of this method calls, in sequence, [- drawHeaderForPageAtIndex:inRect:](<drawheaderforpage(at_in_).md>), [- drawContentForPageAtIndex:inRect:](<drawcontentforpage(at_in_).md>), [- drawPrintFormatter:forPageAtIndex:](<drawprintformatter(__forpageat_).md>), and [- drawFooterForPageAtIndex:inRect:](<drawfooterforpage(at_in_).md>). Override this method to draw the specified page of content for the printer.

The system configures this method for drawing to the current graphics context according to [UIGraphicsGetCurrentContext](<../uigraphicsgetcurrentcontext().md>).

## See Also

### Drawing a page

- [- drawHeaderForPageAtIndex:inRect:](<drawheaderforpage(at_in_).md>) — Draws the header of a page.
- [- drawContentForPageAtIndex:inRect:](<drawcontentforpage(at_in_).md>) — Draws the content of a page.
- [- drawPrintFormatter:forPageAtIndex:](<drawprintformatter(__forpageat_).md>) — Performs custom drawing in addition to the specified print formatter’s drawing for a page.
- [- drawFooterForPageAtIndex:inRect:](<drawfooterforpage(at_in_).md>) — Draws the footer of a page.
