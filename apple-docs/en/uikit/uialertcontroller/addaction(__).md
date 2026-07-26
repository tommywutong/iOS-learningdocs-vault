---
title: 'addAction(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uialertcontroller/addaction(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/addaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/addaction%28_%3A%29.json'
content_hash: 'sha256:39ad6b8516d75345'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# addAction(_:)

<sub>Instance Method</sub>

Attaches an action object to the alert or action sheet.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(_ action: UIAlertAction)
```

## Parameters

- `action` — The action object to display as part of the alert. Actions are displayed as buttons in the alert. The action object provides the button text and the action to be performed when that button is tapped.

## Discussion

If your alert has multiple actions, the order in which you add those actions determines their order in the resulting alert or action sheet.

## See Also

### Configuring the user actions

- [actions](actions.md) — The actions that the user can take in response to the alert or action sheet.
- [preferredAction](preferredaction.md) — The preferred action for the user to take from an alert.
