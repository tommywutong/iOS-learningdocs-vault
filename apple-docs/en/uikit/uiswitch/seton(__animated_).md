---
title: 'setOn(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiswitch/seton(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/seton(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/seton%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:4349a80bbe1dacb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# setOn(_:animated:)

<sub>Instance Method</sub>

Sets the state of the switch to the on or off position, optionally animating the transition.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setOn(_ on: Bool, animated: Bool)
```

## Parameters

- `on` — [true](../../swift/true.md) if the switch should be turned to the on position; [false](../../swift/false.md) if it should be turned to the off position. If the switch is already in the designated position, nothing happens.

- `animated` — [true](../../swift/true.md) to animate the “flipping” of the switch; otherwise [false](../../swift/false.md).

## Discussion

Setting the switch to either position doesn’t result in an action message being sent.

## See Also

### Setting the on/off state

- [on](ison.md) — A Boolean value that determines whether the switch is in the on or off position.
