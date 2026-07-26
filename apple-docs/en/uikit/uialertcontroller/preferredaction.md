---
title: preferredAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertcontroller/preferredaction
source_url: 'https://developer.apple.com/documentation/uikit/uialertcontroller/preferredaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertcontroller/preferredaction.json'
content_hash: 'sha256:97390fdef28ce203'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAlertController](../uialertcontroller.md)

# preferredAction

<sub>Instance Property</sub>

The preferred action for the user to take from an alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredAction: UIAlertAction? { get set }
```

## Discussion

The preferred action is relevant for the [UIAlertControllerStyleAlert](style/alert.md) style only; it isn’t used by action sheets. When you specify a preferred action, the alert controller highlights the text of that action to give it emphasis. (If the alert also contains a cancel button, the preferred action receives the highlighting instead of the cancel button.) If the iOS device is connected to a physical keyboard, pressing the Return key triggers the preferred action.

The action object you assign to this property must have already been added to the alert controller’s list of actions. Assigning an object to this property before adding it with the [- addAction:](<addaction(__).md>) method is a programmer error.

The default value of this property is `nil`.

## See Also

### Configuring the user actions

- [- addAction:](<addaction(__).md>) — Attaches an action object to the alert or action sheet.
- [actions](actions.md) — The actions that the user can take in response to the alert or action sheet.
