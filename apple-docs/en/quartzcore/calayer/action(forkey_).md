---
title: 'action(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/action(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/action(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/action%28forkey%3A%29.json'
content_hash: 'sha256:493704ca51d43336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# action(forKey:)

<sub>Instance Method</sub>

Returns the action object assigned to the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func action(forKey event: String) -> (any CAAction)?
```

## Parameters

- `event` — The identifier of the action.

## Return Value

Returns the object that provides the action for `key`. The object must implement the [CAAction](../caaction.md) protocol.

## Discussion

This method searches for the given action object of the layer. Actions define dynamic behaviors for a layer. For example, the animatable properties of a layer typically have corresponding action objects to initiate the actual animations. When that property changes, the layer looks for the action object associated with the property name and executes it. You can also associate custom action objects with your layer to implement app-specific actions.

This method searches for the layer’s associated actions in the following order:

1. If the layer has a delegate that implements the [- actionForLayer:forKey:](<../calayerdelegate/action(for_forkey_).md>) method, the layer calls that method. The delegate must do one of the following:

- Return the action object for the given key.
- Return the [NSNull](../../foundation/nsnull.md) object if it does not handle the action.

1. The layer looks in the layer’s [actions](actions.md) dictionary for a matching key/action pair.
2. The layer looks in the [style](style.md) dictionary for an [actions](actions.md) dictionary  for a matching key/action pair.
3. The layer calls the [+ defaultActionForKey:](<defaultaction(forkey_).md>) class method to look for any class-defined actions.

If any of the above steps returns an instance of [NSNull](../../foundation/nsnull.md), it is converted to `nil` before continuing.

When an action object is invoked it receives three parameters: the name of the event, the object on which the event happened (the layer), and a dictionary of named arguments specific to each event kind.

## See Also

### Related Documentation

- [Layer filters](../calayer.md#Layer-filters)
- [style](style.md) — An optional dictionary used to store property values that aren’t explicitly defined by the layer.

### Getting the layer’s actions

- [actions](actions.md) — A dictionary containing layer actions.
- [+ defaultActionForKey:](<defaultaction(forkey_).md>) — Returns the default action for the current class.
