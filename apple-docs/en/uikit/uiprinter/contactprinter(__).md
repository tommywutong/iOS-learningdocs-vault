---
title: 'contactPrinter(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinter/contactprinter(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/contactprinter(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/contactprinter%28_%3A%29.json'
content_hash: 'sha256:bcc65d149d18a2b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# contactPrinter(_:)

<sub>Instance Method</sub>

Connects to the printer and gathers information about its capabilities.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func contactPrinter(_ completionHandler: ((Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func contactPrinter() async -> Bool
```

## Parameters

- `completionHandler` — The block to execute with the results. This block has no return value and takes the following parameter: - **available** — [true](../../swift/true.md) if the printer was available and its information was retrieved or [false](../../swift/false.md) if the printer could not be found or was unavailable.

## Discussion

For printers you create yourself using the [+ printerWithURL:](<init(url_)-1mibn.md>) method, you must call this method prior to accessing properties containing printer-related information. This method runs asynchronously, returning immediately while the system continues to try and gather information about the printer’s name, location, capabilities, and so on. When the printer’s availability is determined, the results are delivered to the `completionHandler` block you provided.

Calling this method can take a significantly long time (up to 30 seconds), so after calling this method you should continue with other tasks. Use your completion handler block to update your app as appropriate.
