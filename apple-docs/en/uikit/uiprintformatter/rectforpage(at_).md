---
title: 'rectForPage(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintformatter/rectforpage(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/rectforpage(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/rectforpage%28at%3A%29.json'
content_hash: 'sha256:bdb783228195ed44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# rectForPage(at:)

<sub>Instance Method</sub>

Returns the area that encloses a specified page of content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func rectForPage(at pageIndex: Int) -> CGRect
```

## Parameters

- `pageIndex` — The index number of a page.

## Return Value

A rectangle enclosing the content area for page `pageIndex`.

## Discussion

Returns [CGRectZero](../../coregraphics/cgrectzero.md) if the print formatter draws no content on the specified page.

## See Also

### Drawing the content

- [- drawInRect:forPageAtIndex:](<draw(in_forpageat_).md>) — Draws the portion of a print formatter’s content for the specified area of the specified page.
