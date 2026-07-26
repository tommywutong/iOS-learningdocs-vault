---
title: 'init(url:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/init(url:)-8wb4p'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/init(url:)-8wb4p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/init%28url%3A%29-8wb4p.json'
content_hash: 'sha256:94783d326001428d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# init(url:)

<sub>Initializer</sub>

Creates a document interaction controller with the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(url: URL)
```

## Parameters

- `url` — A URL that specifies the location of the desired document. This parameter is retained. It can be changed later by modifying the [URL](url.md) property.

## Return Value

A new document interaction controller object.
