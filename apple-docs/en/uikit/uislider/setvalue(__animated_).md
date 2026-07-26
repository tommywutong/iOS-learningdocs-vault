---
title: 'setValue(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/setvalue(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/setvalue(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/setvalue%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:6eeb98a4c6179424'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# setValue(_:animated:)

<sub>Instance Method</sub>

Sets the slider’s current value, allowing you to animate the change visually.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setValue(_ value: Float, animated: Bool)
```

## Parameters

- `value` — The new value to assign to the [value](value.md) property

- `animated` — Specify [true](../../swift/true.md) to animate the change in value; otherwise, specify [false](../../swift/false.md) to update the slider’s appearance immediately. Animations are performed asynchronously and do not block the calling thread.

## Discussion

If you specify a value that is beyond the minimum or maximum values, the slider limits the value to the minimum or maximum. For example, if the minimum value is 0.0 and you specify -1.0, the slider sets the [value](value.md) property to 0.0.

## See Also

### Accessing the slider’s value

- [value](value.md) — The slider’s current value.
