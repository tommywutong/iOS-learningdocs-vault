---
title: url
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiprinter/url
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/url.json'
content_hash: 'sha256:ce678642ddad827d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# url

<sub>Instance Property</sub>

The full address of the printer.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var url: URL { get }
```

## Discussion

Use this property to retrieve the address of a printer on the network. You can also save the value in this property to disk and use it later to initialize a new printer object that points to the same printer.
