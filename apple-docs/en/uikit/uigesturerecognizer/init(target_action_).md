---
title: 'init(target:action:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/init(target:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/init(target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/init%28target%3Aaction%3A%29.json'
content_hash: 'sha256:b219ee2db30dd0fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# init(target:action:)

<sub>Initializer</sub>

Creates a gesture recognizer with a target and an action selector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(target: Any?, action: Selector?)
```

## Parameters

- `target` — An object that is the recipient of action messages sent by the receiver when it recognizes a gesture. `nil` isn’t a valid value.

- `action` — A selector that identifies the method implemented by the target to handle the gesture recognized by the receiver. The action selector must conform to the signature described in the class overview. `nil` isn’t a valid value.

## Return Value

An initialized instance of a concrete [UIGestureRecognizer](../uigesturerecognizer.md) subclass.

## Discussion

This method is the designated initializer. After creating the gesture recognizer, you may associate other target-action pairs with it by calling [- addTarget:action:](<addtarget(__action_).md>).

## See Also

### Related Documentation

- [- removeTarget:action:](<removetarget(__action_).md>) — Removes a target and an action from a gesture-recognizer object.
- [- addTarget:action:](<addtarget(__action_).md>) — Adds a target and an action to a gesture-recognizer object.

### Initializing a gesture recognizer

- [- initWithCoder:](<init(coder_).md>) — Creates a gesture recognizer from data in an unarchiver.
- [- init](<init().md>) — Creates a gesture recognizer.
