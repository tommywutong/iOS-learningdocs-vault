---
title: 'draw(in:forPageAt:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintformatter/draw(in:forpageat:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/draw(in:forpageat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/draw%28in%3Aforpageat%3A%29.json'
content_hash: 'sha256:c5eecc00e13ea996'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# draw(in:forPageAt:)

<sub>Instance Method</sub>

Draws the portion of a print formatter’s content for the specified area of the specified page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func draw(in rect: CGRect, forPageAt pageIndex: Int)
```

## Parameters

- `rect` — The area in which to draw the content.

- `pageIndex` — The number of the page of content to draw.

## Discussion

This method is called by the default implementation of `drawPrintFormatter:forPageAtIndex:` of the [UIPrintPageRenderer](../uiprintpagerenderer.md) class for each print formatter associated with a page.

## See Also

### Drawing the content

- [- rectForPageAtIndex:](<rectforpage(at_).md>) — Returns the area that encloses a specified page of content.
