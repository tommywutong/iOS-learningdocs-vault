---
title: 'init(actions:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiswipeactionsconfiguration/init(actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/init(actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipeactionsconfiguration/init%28actions%3A%29.json'
content_hash: 'sha256:892c4a941ac78439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwipeActionsConfiguration](../uiswipeactionsconfiguration.md)

# init(actions:)

<sub>Initializer</sub>

Creates a swipe action configuration object with the specified set of actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(actions: [UIContextualAction])
```

## Parameters

- `actions` — The swipe actions to display. The first item in the array represents the outermost action. For example, when the user swipes from right-to-left, the first action is rightmost. The first action is also the default action.

## Return Value

A newly initialized swipe action configuration object.
