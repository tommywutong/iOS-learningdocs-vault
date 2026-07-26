---
title: 'init(for:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsimagerendererformat/init(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsimagerendererformat/init%28for%3A%29.json'
content_hash: 'sha256:7e3faa601034b06f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsImageRendererFormat](../uigraphicsimagerendererformat.md)

# init(for:)

<sub>Initializer</sub>

Creates the most suitable format for rendering on a device with the specified traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(for traitCollection: UITraitCollection)
```

## Parameters

- `traitCollection` — The traits of the drawing environment.

## Return Value

An initialized format object.
