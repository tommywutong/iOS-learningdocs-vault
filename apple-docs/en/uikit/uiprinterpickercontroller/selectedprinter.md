---
title: selectedPrinter
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinterpickercontroller/selectedprinter
source_url: 'https://developer.apple.com/documentation/uikit/uiprinterpickercontroller/selectedprinter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinterpickercontroller/selectedprinter.json'
content_hash: 'sha256:1eb799da95aa2dbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinterPickerController](../uiprinterpickercontroller.md)

# selectedPrinter

<sub>Instance Property</sub>

The selected printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var selectedPrinter: UIPrinter? { get }
```

## Discussion

The value of this property is set to the picker you specified at creation time initially. When the picker is dismissed, the value is updated to reflect the printer that the user selected, if any. If the user cancels the picker without selecting a printer, the value of this property does not change.
