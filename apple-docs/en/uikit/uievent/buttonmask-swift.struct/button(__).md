---
title: 'button(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uievent/buttonmask-swift.struct/button(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uievent/buttonmask-swift.struct/button(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/buttonmask-swift.struct/button%28_%3A%29.json'
content_hash: 'sha256:3d6b116cce874d5e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIEvent](../../uievent.md) · [ButtonMask](../buttonmask-swift.struct.md)

# button(_:)

<sub>Type Method</sub>

Creates a button mask from the specified button index.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static func button(_ buttonNumber: Int) -> UIEvent.ButtonMask
```

## Parameters

- `buttonNumber` — The index of the button on the input device. Pass `1` to represent [UIEventButtonMaskPrimary](primary.md), and `2` to represent [UIEventButtonMaskSecondary](secondary.md).

## See Also

### Creating button masks

- [init(rawValue:)](<init(rawvalue_).md>) — Creates a button mask with the specified raw value.
