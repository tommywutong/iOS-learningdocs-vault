---
title: performsFirstActionWithFullSwipe
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswipeactionsconfiguration/performsfirstactionwithfullswipe
source_url: 'https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/performsfirstactionwithfullswipe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswipeactionsconfiguration/performsfirstactionwithfullswipe.json'
content_hash: 'sha256:da67c935508eaa97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwipeActionsConfiguration](../uiswipeactionsconfiguration.md)

# performsFirstActionWithFullSwipe

<sub>Instance Property</sub>

A Boolean value indicating whether a full swipe automatically performs the first action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var performsFirstActionWithFullSwipe: Bool { get set }
```

## Discussion

When this property is set to [true](../../swift/true.md), a full swipe in the row performs the first action listed in the [actions](actions.md) property. The default value of this property is [true](../../swift/true.md).

## See Also

### Getting the swipe action information

- [actions](actions.md) — The swipe actions.
