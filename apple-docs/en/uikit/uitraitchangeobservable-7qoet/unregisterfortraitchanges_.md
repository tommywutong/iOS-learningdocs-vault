---
title: 'unregisterForTraitChanges:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-7qoet/unregisterfortraitchanges:'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/unregisterfortraitchanges:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-7qoet/unregisterfortraitchanges%3A.json'
content_hash: 'sha256:43f75585cc1f801e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-7qoet.md)

# unregisterForTraitChanges:

<sub>Instance Method</sub>

Tells the system to stop observing previously registered traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) unregisterForTraitChanges:(id<UITraitChangeRegistration>) registration;
```

## Parameters

- `registration` — A token that identifies the registration, obtained from one of the trait registration method calls.

## Discussion

Use this method if you want the system to stop observing trait changes for a previous registration. UIKit doesn’t require you to unregister for trait changes at the end of the view lifecycle. Unregister only if you need to dynamically change which traits you observe.

## See Also

### Observing trait changes

- [registerForTraitChanges:withAction:](registerfortraitchanges_withaction_.md) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges:withHandler:](registerfortraitchanges_withhandler_.md) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges:withTarget:action:](registerfortraitchanges_withtarget_action_.md) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
