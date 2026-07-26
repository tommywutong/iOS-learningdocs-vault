---
title: targetContentIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationshortcutitem/targetcontentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcutitem/targetcontentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcutitem/targetcontentidentifier.json'
content_hash: 'sha256:8a4871551f3b656a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutItem](../uiapplicationshortcutitem.md)

# targetContentIdentifier

<sub>Instance Property</sub>

The object that determines which scene handles the quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var targetContentIdentifier: Any? { get }
```

## Discussion

UIKit applies the value in this property to the activation conditions defined by the [UISceneActivationConditions](../uisceneactivationconditions.md) objects of the available scenes. Based on the predicates you specify, UIKit selects the most appropriate scene for handling the action.
