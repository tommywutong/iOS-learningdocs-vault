---
title: 'bestPaper(forPageSize:withPapersFrom:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintpaper/bestpaper(forpagesize:withpapersfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintpaper/bestpaper(forpagesize:withpapersfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintpaper/bestpaper%28forpagesize%3Awithpapersfrom%3A%29.json'
content_hash: 'sha256:5aeb99e439e13957'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintPaper](../uiprintpaper.md)

# bestPaper(forPageSize:withPapersFrom:)

<sub>Type Method</sub>

The print-paper object that UIKit determines to be the best for a print job based on the specified page size and the paper size–imageable area combinations specific to the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class func bestPaper(forPageSize contentSize: CGSize, withPapersFrom paperList: [UIPrintPaper]) -> UIPrintPaper
```

## Parameters

- `contentSize` — The size of the printed page that your application requests, in points. You should think of this as the size of the physical sheet of paper to use in printing without consideration of the margin.

- `paperList` — An array of `UIPrintPaper` objects that represent combinations of supported paper size and printable areas. The array of objects usually comes directly from the second argument of the [- printInteractionController:choosePaper:](<../uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) method of the [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md) protocol.

## Return Value

An instance of `UIPrintPaper` that represents the optimal printable area and paper size for the current print job. Returns `nil` if the instance could not be created.

## Discussion

The delegate of [UIPrintInteractionController](../uiprintinteractioncontroller.md) may call this method in its implementation of the [- printInteractionController:choosePaper:](<../uiprintinteractioncontrollerdelegate/printinteractioncontroller(__choosepaper_).md>) method declared in the [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md) protocol.
