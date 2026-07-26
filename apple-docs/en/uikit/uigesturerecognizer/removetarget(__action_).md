---
title: 'removeTarget(_:action:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/removetarget(_:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/removetarget(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/removetarget%28_%3Aaction%3A%29.json'
content_hash: 'sha256:4f20201ccc6d7542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# removeTarget(_:action:)

<sub>Instance Method</sub>

Removes a target and an action from a gesture-recognizer object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeTarget(_ target: Any?, action: Selector?)
```

## Parameters

- `target` — An object that currently is a recipient of action messages sent by the receiver when the represented gesture occurs. Specify `nil` if you want to remove all targets from the receiver.

- `action` — A selector identifying a method of a target to be invoked by the action message. Specify `NULL` if you want to remove all actions from the receiver.

## Discussion

Calling this method removes the specified target-action pair. Passing `nil` for `target` matches all targets and passing `NULL` for `action` matches all actions.

## See Also

### Related Documentation

- [- initWithTarget:action:](<init(target_action_).md>) — Creates a gesture recognizer with a target and an action selector.

### Adding and removing targets and actions

- [- addTarget:action:](<addtarget(__action_).md>) — Adds a target and an action to a gesture-recognizer object.
