---
title: 'init(view:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewinteraction/init(view:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewinteraction/init(view:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewinteraction/init%28view%3A%29.json'
content_hash: 'sha256:a7b77e5c5a8574af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewInteraction](../uipreviewinteraction.md)

# init(view:)

<sub>Initializer</sub>

Returns a newly initialized preview interaction for the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(view: UIView)
```

## Parameters

- `view` — The view for which the preview interaction should respond.

## Return Value

An initialized preview interaction.

## Discussion

Preview interactions operate on touches within a specified view. Unlike gesture recognizers, the view doesn’t maintain a strong reference to preview interactions. You must therefore retain a reference to the preview interaction to ensure that it continues to receive touches from the view.
