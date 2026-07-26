---
title: 'init(operation:intent:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewdropproposal/init(operation:intent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropproposal/init(operation:intent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropproposal/init%28operation%3Aintent%3A%29.json'
content_hash: 'sha256:77de1acee8a8a2d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropProposal](../uitableviewdropproposal.md)

# init(operation:intent:)

<sub>Initializer</sub>

Creates a drop proposal object that specifies how to incorporate the dropped content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(operation: UIDropOperation, intent: UITableViewDropProposal.Intent)
```

## Parameters

- `operation` — The type of operation that you want to perform. Use this parameter to specify whether you want to move the original item to this new location, move a copy of the content, or prevent the content from being inserted at this location. For a list of possible values, see [UIDropOperation](../uidropoperation.md).

- `intent` — The option for how to incorporate the content into the table view. You can insert the content between items or add it to an existing item.

## Return Value

An initialized drop proposal.
