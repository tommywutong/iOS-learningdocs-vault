---
title: 'init(placeholderItem:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemprovider/init(placeholderitem:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemprovider/init(placeholderitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemprovider/init%28placeholderitem%3A%29.json'
content_hash: 'sha256:9bfb52e39f532ff7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemProvider](../uiactivityitemprovider.md)

# init(placeholderItem:)

<sub>Initializer</sub>

Initializes and returns a provider object with the specified placeholder data.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(placeholderItem: Any)
```

## Parameters

- `placeholderItem` — An object that can stand in for the actual object you plan to create. The contents of the object may be empty but the class of the object must match the class of the object you plan to provide later.

## Return Value

An initialized provider object.
