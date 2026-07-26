---
title: UITraitChangeRegistration
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitchangeregistration
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeregistration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeregistration.json'
content_hash: 'sha256:328a0467209c9461'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitChangeRegistration

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UITraitChangeRegistration : NSCopying, NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Observing trait changes

- [registerForTraitChanges(_:action:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__action_).md>) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges(_:handler:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__handler_).md>) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges(_:)](<uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>) — Tells the system to stop observing previously registered traits.
- [TraitChangeHandler](uitraitchangeobservable-67e94/traitchangehandler.md) — A closure the system executes when observed traits change.
