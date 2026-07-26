---
title: actions
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/actions
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/actions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/actions.json'
content_hash: 'sha256:27eb6449caeeeb50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# actions

<sub>Instance Property</sub>

A dictionary containing layer actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var actions: [String : any CAAction]? { get set }
```

## Discussion

The default value of this property is `nil`. You can use this dictionary to store custom actions for your layer. The contents of this dictionary searched as part of the standard implementation of the [- actionForKey:](<action(forkey_).md>) method.

## See Also

### Getting the layer’s actions

- [- actionForKey:](<action(forkey_).md>) — Returns the action object assigned to the specified key.
- [+ defaultActionForKey:](<defaultaction(forkey_).md>) — Returns the default action for the current class.
