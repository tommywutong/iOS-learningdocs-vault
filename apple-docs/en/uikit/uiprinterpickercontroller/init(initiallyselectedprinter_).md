---
title: 'init(initiallySelectedPrinter:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinterpickercontroller/init(initiallyselectedprinter:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/init(initiallyselectedprinter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/init%28initiallyselectedprinter%3A%29.json'
content_hash: 'sha256:b39c9d04422dcda4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# init(initiallySelectedPrinter:)

<sub>Initializer</sub>

Creates and returns a printer picker with an initially selected printer object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(initiallySelectedPrinter printer: UIPrinter?)
```

## Parameters

- `printer` — A printer object to select initially. Specify `nil` if you do not want to display a selected printer initially.

## Return Value

An initialized printer picker controller object.

## Discussion

After creating a printer picker controller, assign your delegate as needed and present the controller.
