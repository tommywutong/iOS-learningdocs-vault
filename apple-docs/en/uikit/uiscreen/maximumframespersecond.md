---
title: maximumFramesPerSecond
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, tvOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/maximumframespersecond
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/maximumframespersecond'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/maximumframespersecond.json'
content_hash: 'sha256:7c8f79c1b3604c63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# maximumFramesPerSecond

<sub>Instance Property</sub>

The maximum number of frames per second a screen can render.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maximumFramesPerSecond: Int { get }
```

## Discussion

In iOS, the value of this property can be up to `120` for devices with ProMotion displays.

In tvOS, the value of this property depends on the hardware capabilities of the attached screen and the user’s selected resolution on Apple TV.

## See Also

### Getting a display link

- [- displayLinkWithTarget:selector:](<displaylink(withtarget_selector_).md>) — Returns a display link object for the current screen. _(deprecated)_
