---
title: UITraitChangeObservable.TraitChangeHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitchangeobservable-67e94/traitchangehandler
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/traitchangehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-67e94/traitchangehandler.json'
content_hash: 'sha256:88cd8046fee7c8cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-67e94.md)

# UITraitChangeObservable.TraitChangeHandler

<sub>Type Alias</sub>

A closure the system executes when observed traits change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias TraitChangeHandler<TraitEnvironment> = (TraitEnvironment, UITraitCollection) -> Void where TraitEnvironment : UITraitEnvironment
```

## Parameters

- `traitEnvironment` — The observed object containing the updated trait collection.

- `previousTraitCollection` — The trait collection prior to the changes that triggered the execution of the handler.

## Discussion

Use [registerForTraitChanges(_:handler:)](<registerfortraitchanges(__handler_).md>) to register a list of traits to observe and a handler to execute.

If the closure captures a strong reference to the object receiving the registration, it creates a strong reference cycle. Use the `traitEnvironment` parameter to refer to the observed object inside the closure.

## See Also

### Observing trait changes

- [registerForTraitChanges(_:action:)](<registerfortraitchanges(__action_).md>) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges(_:handler:)](<registerfortraitchanges(__handler_).md>) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges(_:)](<unregisterfortraitchanges(__).md>) — Tells the system to stop observing previously registered traits.
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
