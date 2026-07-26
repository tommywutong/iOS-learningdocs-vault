---
title: 'drawPrintFormatter(_:forPageAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpagerenderer/drawprintformatter(_:forpageat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpagerenderer/drawprintformatter(_:forpageat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpagerenderer/drawprintformatter%28_%3Aforpageat%3A%29.json'
content_hash: 'sha256:eceba00d3d8103aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPageRenderer](../uiprintpagerenderer.md)

# drawPrintFormatter(_:forPageAt:)

<sub>Instance Method</sub>

Performs custom drawing in addition to the specified print formatter’s drawing for a page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func drawPrintFormatter(_ printFormatter: UIPrintFormatter, forPageAt pageIndex: Int)
```

## Parameters

- `printFormatter` — A [UIPrintFormatter](../uiprintformatter.md) object associated with the page at `pageIndex`.

- `pageIndex` — The index of the page for `printFormatter` to draw on.

## Discussion

The system invokes this method for each print formatter associated with the specified page. The default implementation invokes the [- drawInRect:forPageAtIndex:](<../uiprintformatter/draw(in_forpageat_).md>) method of each [UIPrintFormatter](../uiprintformatter.md) object.

Override this method to intermix custom drawing with the formatter drawing — for example, by adding an overlay or underlay graphic. Call [- drawInRect:forPageAtIndex:](<../uiprintformatter/draw(in_forpageat_).md>) to have the print formatter draw its portion of the page.

The system configures this method for drawing to the current graphics context according to [UIGraphicsGetCurrentContext](<../uigraphicsgetcurrentcontext().md>).

## See Also

### Drawing a page

- [- drawPageAtIndex:inRect:](<drawpage(at_in_).md>) — Draws a page of content for the printer.
- [- drawHeaderForPageAtIndex:inRect:](<drawheaderforpage(at_in_).md>) — Draws the header of a page.
- [- drawContentForPageAtIndex:inRect:](<drawcontentforpage(at_in_).md>) — Draws the content of a page.
- [- drawFooterForPageAtIndex:inRect:](<drawfooterforpage(at_in_).md>) — Draws the footer of a page.
