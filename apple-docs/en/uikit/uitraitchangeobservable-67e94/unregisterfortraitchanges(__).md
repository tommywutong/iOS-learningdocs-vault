---
title: 'unregisterForTraitChanges(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-67e94/unregisterfortraitchanges(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/unregisterfortraitchanges(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-67e94/unregisterfortraitchanges%28_%3A%29.json'
content_hash: 'sha256:2cd7d98ed8c2d8b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-67e94.md)

# unregisterForTraitChanges(_:)

<sub>Instance Method</sub>

Tells the system to stop observing previously registered traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func unregisterForTraitChanges(_ registration: any UITraitChangeRegistration)
```

## Parameters

- `registration` — A token that identifies the registration, obtained from one of the trait registration method calls.

## Discussion

Use this method if you want the system to stop observing trait changes for a previous registration. UIKit doesn’t require you to unregister for trait changes at the end of the view lifecycle. Unregister only if you need to dynamically change which traits you observe.

## See Also

### Observing trait changes

- [registerForTraitChanges(_:action:)](<registerfortraitchanges(__action_).md>) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges(_:handler:)](<registerfortraitchanges(__handler_).md>) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [TraitChangeHandler](traitchangehandler.md) — A closure the system executes when observed traits change.
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
