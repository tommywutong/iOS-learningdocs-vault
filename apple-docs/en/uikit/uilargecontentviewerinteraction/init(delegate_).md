---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilargecontentviewerinteraction/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilargecontentviewerinteraction/init%28delegate%3A%29.json'
content_hash: 'sha256:c0eee58d5fa2571c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILargeContentViewerInteraction](../uilargecontentviewerinteraction.md)

# init(delegate:)

<sub>Initializer</sub>

Creates an interaction object with the specified delegate.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: (any UILargeContentViewerInteractionDelegate)?)
```

## Parameters

- `delegate` — An object that implements the [UILargeContentViewerInteractionDelegate](../uilargecontentviewerinteractiondelegate.md) protocol.

## Discussion

To add the interaction to a view, use [- addInteraction:](<../uiview/addinteraction(__).md>).
