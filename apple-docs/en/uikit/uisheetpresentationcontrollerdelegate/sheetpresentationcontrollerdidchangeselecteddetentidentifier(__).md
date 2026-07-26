---
title: 'sheetPresentationControllerDidChangeSelectedDetentIdentifier(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontrollerdelegate/sheetpresentationcontrollerdidchangeselecteddetentidentifier%28_%3A%29.json'
content_hash: 'sha256:52a25038398af654'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationControllerDelegate](../uisheetpresentationcontrollerdelegate.md)

# sheetPresentationControllerDidChangeSelectedDetentIdentifier(_:)

<sub>Instance Method</sub>

Provides an opportunity to respond after the sheet presentation controller’s selected detent changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func sheetPresentationControllerDidChangeSelectedDetentIdentifier(_ sheetPresentationController: UISheetPresentationController)
```

## Parameters

- `sheetPresentationController` — The sheet presentation controller whose detent changes.

## Discussion

Implement this method if you want to perform changes in response to the user resizing a sheet to a new detent.

The system calls this method after a sheet’s [selectedDetentIdentifier](../uisheetpresentationcontroller/selecteddetentidentifier.md) changes in response to user interaction. The system doesn’t call this after you change [selectedDetentIdentifier](../uisheetpresentationcontroller/selecteddetentidentifier.md) programmatically.
