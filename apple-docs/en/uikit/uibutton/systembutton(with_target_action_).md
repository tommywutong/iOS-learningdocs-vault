---
title: 'systemButton(with:target:action:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/systembutton(with:target:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/systembutton(with:target:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/systembutton%28with%3Atarget%3Aaction%3A%29.json'
content_hash: 'sha256:99db5db5decc1505'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# systemButton(with:target:action:)

<sub>Type Method</sub>

Creates and returns a system type button with specified image, target, and action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func systemButton(with image: UIImage, target: Any?, action: Selector?) -> Self
```

## Parameters

- `image` — The image for a system button.

- `target` — The object that receives the `action` message.

- `action` — The action to send to `target` when this item is selected.

## Discussion

This method is a convenience constructor for creating a `UIButtonTypeSystem` type button objects with a specific target and action.
