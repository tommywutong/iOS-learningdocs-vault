---
title: UITraitChangeHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitchangehandler
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangehandler.json'
content_hash: 'sha256:a947a3126a00380a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitChangeHandler

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof id<UITraitEnvironment>, UITraitCollection *) UITraitChangeHandler;
```

## See Also

### Observing trait changes

- [registerForTraitChanges:withAction:](uitraitchangeobservable-7qoet/registerfortraitchanges_withaction_.md) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges:withHandler:](uitraitchangeobservable-7qoet/registerfortraitchanges_withhandler_.md) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges:withTarget:action:](uitraitchangeobservable-7qoet/registerfortraitchanges_withtarget_action_.md) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges:](uitraitchangeobservable-7qoet/unregisterfortraitchanges_.md) — Tells the system to stop observing previously registered traits.
- [UITraitChangeRegistration](uitraitchangeregistration.md)
