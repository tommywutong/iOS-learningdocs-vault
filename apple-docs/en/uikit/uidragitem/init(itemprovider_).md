---
title: 'init(itemProvider:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragitem/init(itemprovider:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragitem/init(itemprovider:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragitem/init%28itemprovider%3A%29.json'
content_hash: 'sha256:f6361139fb409875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragItem](../uidragitem.md)

# init(itemProvider:)

<sub>Initializer</sub>

Initializes a new drag item with a specified item provider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(itemProvider: NSItemProvider)
```

## Parameters

- `itemProvider` — An instance of [NSItemProvider](../../foundation/nsitemprovider.md) that conveys the data or file to share during the drag-and-drop activity.

## Return Value

A drag item that the system initializes with the specified item provider.

## Discussion

Provide an [NSItemProvider](../../foundation/nsitemprovider.md) object to create a new drag item. The item provider communicates the data that the drag-and-drop activity shares between processes.
