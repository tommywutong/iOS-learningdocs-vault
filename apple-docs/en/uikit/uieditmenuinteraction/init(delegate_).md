---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uieditmenuinteraction/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction/init%28delegate%3A%29.json'
content_hash: 'sha256:909f2feb209b65a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuInteraction](../uieditmenuinteraction.md)

# init(delegate:)

<sub>Initializer</sub>

Initializes an edit menu interaction object with the delegate object you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: (any UIEditMenuInteractionDelegate)?)
```

## Discussion

Create an object that conforms to the [UIEditMenuInteractionDelegate](../uieditmenuinteractiondelegate.md) protocol and assign it to this property. The interaction uses the system delegate if no delegate is provided (if you pass in `nil`).
