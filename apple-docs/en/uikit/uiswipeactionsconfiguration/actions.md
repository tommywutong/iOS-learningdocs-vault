---
title: actions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswipeactionsconfiguration/actions
source_url: 'https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipeactionsconfiguration/actions.json'
content_hash: 'sha256:65673b74f94d4029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwipeActionsConfiguration](../uiswipeactionsconfiguration.md)

# actions

<sub>Instance Property</sub>

The swipe actions.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var actions: [UIContextualAction] { get }
```

## Discussion

The first object in this array corresponds to the default action, which is the action that’s performed in response to a full swipe.

## See Also

### Getting the swipe action information

- [performsFirstActionWithFullSwipe](performsfirstactionwithfullswipe.md) — A Boolean value indicating whether a full swipe automatically performs the first action.
