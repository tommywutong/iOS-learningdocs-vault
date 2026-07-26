---
title: isOn
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/ison
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/ison'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/ison.json'
content_hash: 'sha256:dd4bf1ecec5c59e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# isOn

<sub>Instance Property</sub>

A Boolean value that determines whether the switch is in the on or off position.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isOn: Bool { get set }
```

## Discussion

This property allows you to retrieve and set (without animation) a value determining whether the [UISwitch](../uiswitch.md) object is on or off.

## See Also

### Setting the on/off state

- [- setOn:animated:](<seton(__animated_).md>) — Sets the state of the switch to the on or off position, optionally animating the transition.
