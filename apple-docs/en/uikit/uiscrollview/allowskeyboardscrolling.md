---
title: allowsKeyboardScrolling
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/allowskeyboardscrolling
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/allowskeyboardscrolling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/allowskeyboardscrolling.json'
content_hash: 'sha256:6d92fe14629a2c81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# allowsKeyboardScrolling

<sub>Instance Property</sub>

A Boolean value that determines whether the scroll view allows scrolling its content with hardware keyboard input.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsKeyboardScrolling: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the scroll view animates its content offset in response to input from hardware keyboard keys like Page Up, Page Down, Home, End, and the arrow keys. The scroll view needs to have focus or be first responder to receive these key events.

The default value is [true](../../swift/true.md) for apps that link against iOS 17 and later. Set this value to [false](../../swift/false.md) to disable the ability to scroll content with hardware keyboard keys.
