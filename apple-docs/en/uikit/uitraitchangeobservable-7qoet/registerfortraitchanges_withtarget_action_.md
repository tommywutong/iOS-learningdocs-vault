---
title: 'registerForTraitChanges:withTarget:action:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withtarget:action:'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withtarget:action:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges%3Awithtarget%3Aaction%3A.json'
content_hash: 'sha256:d765b0072e2f0925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-7qoet.md)

# registerForTraitChanges:withTarget:action:

<sub>Instance Method</sub>

Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id<UITraitChangeRegistration>) registerForTraitChanges:(NSArray<Class<UITraitDefinition>> *) traits withTarget:(id) target action:(SEL) action;
```

## Parameters

- `traits` — An array of traits to observe for changes.

- `target` — The object that receives the method call passed in the action parameter.

- `action` — A selector identifying the method the system calls when one of the registered trait changes.

## Return Value

An opaque token you can use to stop observing trait changes by passing to [unregisterForTraitChanges(_:)](<../uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>). You don’t have to unregister your observations, and you can safely ignore this value.

## Discussion

The method specified by the selector can take zero, one, or two arguments. If the method takes one argument, the system passes the object whose trait collection is changing. If the method takes two arguments, the system passes the trait collection prior to the observed changes as the second argument.

The following example registers size class traits so that the system executes the closure when a size class trait changes in the view’s trait collection:

```swift
@objc func sizeClassChanged(view: UIView, previousTraitCollection: UITraitCollection) {
    // Perform invalidation in response to the size class changing.
}

let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

view.registerForTraitChanges(sizeTraits, target: self, action: #selector(sizeClassChanged(view:
previousTraitCollection:)))

```

## See Also

### Observing trait changes

- [registerForTraitChanges:withAction:](registerfortraitchanges_withaction_.md) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges:withHandler:](registerfortraitchanges_withhandler_.md) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [unregisterForTraitChanges:](unregisterfortraitchanges_.md) — Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
