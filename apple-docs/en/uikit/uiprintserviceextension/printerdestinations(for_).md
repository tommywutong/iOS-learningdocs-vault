---
title: 'printerDestinations(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintserviceextension/printerdestinations(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintserviceextension/printerdestinations(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintserviceextension/printerdestinations%28for%3A%29.json'
content_hash: 'sha256:1d04125770a3fdb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintServiceExtension](../uiprintserviceextension.md)

# printerDestinations(for:)

<sub>Instance Method</sub>

Searches for a printer destination that matches the print-job attributes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func printerDestinations(for printInfo: UIPrintInfo) -> [UIPrinterDestination]
```

## Parameters

- `printInfo` — The characteristics of a print job.

## Return Value

A printer or printers that fulfill the printing options in `printInfo`.

## Discussion

This method inspects the [UIPrintInfo](../uiprintinfo.md) record to determine which printers to display to the user.
