---
title: printPageRenderer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprintformatter/printpagerenderer
source_url: 'https://developer.apple.com/documentation/uikit/uiprintformatter/printpagerenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintformatter/printpagerenderer.json'
content_hash: 'sha256:7bc17d43db9552c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintFormatter](../uiprintformatter.md)

# printPageRenderer

<sub>Instance Property</sub>

Returns the page renderer for the print formatter.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var printPageRenderer: UIPrintPageRenderer? { get }
```

## Discussion

If the receiving print formatter was not added to a page renderer—that is, it was assigned to the [printFormatter](../uiprintinteractioncontroller/printformatter.md) property of the [UIPrintInteractionController](../uiprintinteractioncontroller.md) class—the value returned is `nil`.

## See Also

### Communicating with the page renderer

- [- removeFromPrintPageRenderer](<removefromprintpagerenderer().md>) — Removes the print formatter from the page renderer.
