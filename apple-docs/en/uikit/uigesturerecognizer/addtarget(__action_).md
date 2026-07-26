---
title: 'addTarget(_:action:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/addtarget(_:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/addtarget(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/addtarget%28_%3Aaction%3A%29.json'
content_hash: 'sha256:467b2af0b4b824bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# addTarget(_:action:)

<sub>Instance Method</sub>

Adds a target and an action to a gesture-recognizer object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addTarget(_ target: Any, action: Selector)
```

## Parameters

- `target` — An object that is a recipient of action messages sent by the receiver when the represented gesture occurs. `nil` is not a valid value.

- `action` — A selector identifying a method of a target to be invoked by the action message. `NULL` is not a valid value.

## Discussion

You may call this method multiple times to specify multiple target-action pairs. However, if you request to add a target-action pair that has already been added, then the request is ignored.

## See Also

### Related Documentation

- [- initWithTarget:action:](<init(target_action_).md>) — Creates a gesture recognizer with a target and an action selector.

### Adding and removing targets and actions

- [- removeTarget:action:](<removetarget(__action_).md>) — Removes a target and an action from a gesture-recognizer object.
