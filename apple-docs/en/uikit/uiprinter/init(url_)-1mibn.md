---
title: 'init(url:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprinter/init(url:)-1mibn'
source_url: 'https://developer.apple.com/documentation/uikit/uiprinter/init(url:)-1mibn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprinter/init%28url%3A%29-1mibn.json'
content_hash: 'sha256:749e172a2c7109ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrinter](../uiprinter.md)

# init(url:)

<sub>Initializer</sub>

Creates and returns a printer with the specified location.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(url: URL)
```

## Parameters

- `url` — A URL that identifies the location of the printer on your network.

## Return Value

A printer object representing the specified printer or `nil` if there was a problem initializing the object.

## Discussion

Use this method to create printer objects for printers whose address you already know. The printer does not need to be online or available when you call this method. The URL you specify is stored in the returned object so that you can contact the printer later using the [- contactPrinter:](<contactprinter(__).md>) method.
