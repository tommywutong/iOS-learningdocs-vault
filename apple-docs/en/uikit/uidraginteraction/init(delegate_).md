---
title: 'init(delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidraginteraction/init(delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidraginteraction/init(delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidraginteraction/init%28delegate%3A%29.json'
content_hash: 'sha256:b9e432369650a0cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragInteraction](../uidraginteraction.md)

# init(delegate:)

<sub>Initializer</sub>

Initializes a drag interaction object with a custom delegate object.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(delegate: any UIDragInteractionDelegate)
```

## Parameters

- `delegate` — The object that configures and controls a drag interaction.

## Return Value

A drag interaction that has a delegate.
