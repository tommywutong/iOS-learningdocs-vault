---
title: actions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/actions
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/actions.json'
content_hash: 'sha256:b1f59ba8aaa6b3c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# actions

<sub>Instance Property</sub>

The actions that the user can take in response to the alert or action sheet.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var actions: [UIAlertAction] { get }
```

## Discussion

The actions are in the order in which you added them to the alert controller. This order also corresponds to the order in which they’re displayed in the alert or action sheet. The second action in the array is displayed below the first, the third is displayed below the second, and so on.

## See Also

### Configuring the user actions

- [- addAction:](<addaction(__).md>) — Attaches an action object to the alert or action sheet.
- [preferredAction](preferredaction.md) — The preferred action for the user to take from an alert.
