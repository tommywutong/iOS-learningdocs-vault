---
title: brightness
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/brightness
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/brightness'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/brightness.json'
content_hash: 'sha256:46f267e29025a602'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# brightness

<sub>Instance Property</sub>

The brightness level of the screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var brightness: CGFloat { get set }
```

## Discussion

This property is only supported on the main screen. The value of this property is a number between `0.0` and `1.0`, inclusive, where `0.0` is the minimum brightness and `1.0` is the maximum brightness.

Brightness changes remain in effect until the person locks their device, even if the person closes your app before then. The next time the person unlocks the device, the system restores the brightness setting to the original value in Settings or Control Center.

In visionOS, setting this property has no effect.

## See Also

### Managing brightness

- [wantsSoftwareDimming](wantssoftwaredimming.md) — A Boolean value that indicates whether the screen may be dimmed lower than the hardware is normally capable of by emulating it in software.
