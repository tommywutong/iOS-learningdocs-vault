---
title: 'printInteractionController(_:choosePaper:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:choosepaper:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller%28_%3Achoosepaper%3A%29.json'
content_hash: 'sha256:f24fbc1c63a68207'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionController(_:choosePaper:)

<sub>Instance Method</sub>

Asks the delegate for an object that encapsulates the paper size and printing area for the print job.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, choosePaper paperList: [UIPrintPaper]) -> UIPrintPaper
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

- `paperList` — An array of [UIPrintPaper](../uiprintpaper.md) objects that represent combinations of paper sizes and imageable areas supported by the selected printer.

## Return Value

A [UIPrintPaper](../uiprintpaper.md) object representing both the paper size and imageable area (or printable rectangle) to use for the print job.

## Discussion

This method is intended for apps (typically document-based apps) that have a notion of distinct paper sizes. The delegate can examine the objects in `paperList` to locate the paper size and printable rectangle combination that is best suited for its needs and return the encapsulating `UIPrintPaper` object. Or it can call the [+ bestPaperForPageSize:withPapersFromArray:](<../uiprintpaper/bestpaper(forpagesize_withpapersfrom_).md>) class method of the [UIPrintPaper](../uiprintpaper.md) class, passing in a specific page size (typically the document size), and return the object returned by that method.

## See Also

### Related Documentation

- [printPaper](../uiprintinteractioncontroller/printpaper.md) — An object that represents the paper size and printing area for the print job.

### Choosing a Paper Size for the Print Job

- [- printInteractionController:cutLengthForPaper:](<printinteractioncontroller(__cutlengthfor_).md>) — Asks the delegate for a length to use when cutting the page.
- [- printInteractionController:chooseCutterBehavior:](<printinteractioncontroller(__choosecutterbehavior_).md>) — Asks the delegate for the cutter behavior for the print job.
