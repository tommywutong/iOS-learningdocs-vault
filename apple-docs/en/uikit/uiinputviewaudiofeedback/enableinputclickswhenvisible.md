---
title: enableInputClicksWhenVisible
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewaudiofeedback/enableinputclickswhenvisible
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewaudiofeedback/enableinputclickswhenvisible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewaudiofeedback/enableinputclickswhenvisible.json'
content_hash: 'sha256:9684340963386521'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewAudioFeedback](../uiinputviewaudiofeedback.md)

# enableInputClicksWhenVisible

<sub>Instance Property</sub>

Specifies whether or not an input view enables input clicks.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional var enableInputClicksWhenVisible: Bool { get }
```

## Parameters

- `enableInputClicksWhenVisible` — Return [true](../../swift/true.md) to enable input clicks by way of the [- playInputClick](<../uidevice/playinputclick().md>) method, or [false](../../swift/false.md) to disable input clicks. The value is [false](../../swift/false.md) by default.

## Discussion

In your custom subclass of [UIView](../uiview.md), implement this property as a getter method. Return [true](../../swift/true.md) to enable input clicks in your custom input or keyboard accessory view, as follows:

**Swift**

```swift
var enableInputClicksWhenVisible: Bool {
    return true
}
```

**Objective-C**

```objc
- (BOOL) enableInputClicksWhenVisible {
    return YES;
}
```

Input clicks will be produced only if the user has also enabled keyboard clicks in Settings \> Sounds.
