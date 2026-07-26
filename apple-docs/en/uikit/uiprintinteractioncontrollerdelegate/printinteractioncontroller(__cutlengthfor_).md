---
title: 'printInteractionController(_:cutLengthFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller(_:cutlengthfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontroller%28_%3Acutlengthfor%3A%29.json'
content_hash: 'sha256:e2697ce77083da5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionController(_:cutLengthFor:)

<sub>Instance Method</sub>

Asks the delegate for a length to use when cutting the page.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionController(_ printInteractionController: UIPrintInteractionController, cutLengthFor paper: UIPrintPaper) -> CGFloat
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

- `paper` — A [UIPrintPaper](../uiprintpaper.md) that specifies the maximum physical and printable areas of the page.

## Return Value

The physical length of the page in points.

## Discussion

Some printers can cut a roll of print paper at a particular length. If you implement this method in your delegate, then it may be called during a print job. Your delegate should determine the length in which the content fits and return this value. When printed, the paper will be cut to this length.

## See Also

### Choosing a Paper Size for the Print Job

- [- printInteractionController:choosePaper:](<printinteractioncontroller(__choosepaper_).md>) — Asks the delegate for an object that encapsulates the paper size and printing area for the print job.
- [- printInteractionController:chooseCutterBehavior:](<printinteractioncontroller(__choosecutterbehavior_).md>) — Asks the delegate for the cutter behavior for the print job.
