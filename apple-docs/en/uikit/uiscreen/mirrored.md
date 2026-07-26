---
title: mirrored
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/mirrored
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/mirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/mirrored.json'
content_hash: 'sha256:d2161f83c189df9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# mirrored

<sub>Instance Property</sub>

The screen an external display mirrors from.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var mirrored: UIScreen? { get }
```

## Discussion

When a screen supports mirroring and mirroring is active, this property contains the screen object associated with the device’s main screen. This represents the screen the attached display mirrors from. The value of this property is `nil` when mirroring is disabled, not supported, or no screen is connected to the device.

To disable mirroring and present unique content on the external display, register a scene accessory with [- registerSceneAccessory:](<../uiviewcontroller/registersceneaccessory(__).md>). For more information, see [Presenting content on a connected display](../presenting-content-on-a-connected-display.md).

## See Also

### Related Documentation

- [mainScreen](main.md) — Returns the screen object representing the device’s screen. _(deprecated)_

### Detecting screen capture

- [captured](iscaptured.md) — A Boolean value that indicates whether the system is actively cloning the screen to another destination. _(deprecated)_
