---
title: canActivateForTargetContentIdentifierPredicate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisceneactivationconditions/canactivatefortargetcontentidentifierpredicate
source_url: 'https://developer.apple.com/documentation/uikit/uisceneactivationconditions/canactivatefortargetcontentidentifierpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneactivationconditions/canactivatefortargetcontentidentifierpredicate.json'
content_hash: 'sha256:7ec05ca53f718ffd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneActivationConditions](../uisceneactivationconditions.md)

# canActivateForTargetContentIdentifierPredicate

<sub>Instance Property</sub>

Conditions for which UIKit can activate the scene if a better alternative doesn’t exist.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var canActivateForTargetContentIdentifierPredicate: NSPredicate { get set }
```

## Discussion

Use this property to specify the tasks your scene can handle, if needed. UIKit evaluates your predicate against the [targetContentIdentifier](../uiapplicationshortcutitem/targetcontentidentifier.md) property of the object causing the activation of the scene. Many different objects contain target content identifiers, including [NSUserActivity](../../foundation/nsuseractivity.md), [UNNotificationContent](../../usernotifications/unnotificationcontent.md), and [UIApplicationShortcutItem](../uiapplicationshortcutitem.md).

UIKit must be able to evaluate your predicate’s conditions outside the scope of your app, so don’t include conditions that require dynamic evaluation. For example, don’t include key paths in your predicate and don’t create predicates that evaluate conditions using selectors or blocks. The default value of this property is a predicate that always evaluates to the value [true](../../swift/true.md).

## See Also

### Specifying the conditions

- [prefersToActivateForTargetContentIdentifierPredicate](preferstoactivatefortargetcontentidentifierpredicate.md) — The set of conditions for which UIKit chooses to activate this scene over others.
