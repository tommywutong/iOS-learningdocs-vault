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
doc_path: /documentation/uikit/uimutableapplicationshortcutitem/targetcontentidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem/targetcontentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableapplicationshortcutitem/targetcontentidentifier.json'
content_hash: 'sha256:e5961893201a480f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableApplicationShortcutItem](../uimutableapplicationshortcutitem.md)

# targetContentIdentifier

<sub>Instance Property</sub>

The object that determines which scene handles the quick action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var targetContentIdentifier: Any? { get set }
```

## Discussion

Assign an object to this property when you want a specific scene of your app to handle quick actions. UIKit applies the value in this property to the activation conditions defined by the [UISceneActivationConditions](../uisceneactivationconditions.md) objects of the available scenes. Based on the predicates you specify, UIKit selects the most appropriate scene for handling the action.
