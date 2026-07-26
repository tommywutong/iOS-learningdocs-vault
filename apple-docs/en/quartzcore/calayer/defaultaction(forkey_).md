---
title: 'defaultAction(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/defaultaction(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/defaultaction(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/defaultaction%28forkey%3A%29.json'
content_hash: 'sha256:3c85986e7984e785'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# defaultAction(forKey:)

<sub>Type Method</sub>

Returns the default action for the current class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func defaultAction(forKey event: String) -> (any CAAction)?
```

## Parameters

- `event` — The identifier of the action.

## Return Value

Returns a suitable action object for the given key or `nil` of no action object was associated with that key.

## Discussion

Classes that want to provide default actions can override this method and use it to return those actions.

## See Also

### Getting the layer’s actions

- [- actionForKey:](<action(forkey_).md>) — Returns the action object assigned to the specified key.
- [actions](actions.md) — A dictionary containing layer actions.
