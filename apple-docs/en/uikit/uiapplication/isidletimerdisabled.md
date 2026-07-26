---
title: isIdleTimerDisabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/isidletimerdisabled
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isidletimerdisabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isidletimerdisabled.json'
content_hash: 'sha256:f813df4c402cba16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isIdleTimerDisabled

<sub>Instance Property</sub>

A Boolean value that controls whether the idle timer is disabled for the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isIdleTimerDisabled: Bool { get set }
```

## Discussion

The default value of this property is [false](../../swift/false.md). When most apps have no touches as user input for a short period, the system puts the device into a “sleep” state where the screen dims. This is done for the purposes of conserving power. However, apps that don’t have user input except for the accelerometer — games, for instance — can, by setting this property to [true](../../swift/true.md), disable the “idle timer” to avert system sleep.

> [!important] Important
> You should set this property only if necessary and should be sure to reset it to [false](../../swift/false.md) when the need no longer exists. Most apps should let the system turn off the screen when the idle timer elapses. This includes audio apps. With appropriate use of Audio Session Services, playback and recording proceed uninterrupted when the screen turns off. The only apps that should disable the idle timer are mapping apps, games, or programs where the app needs to continue displaying content when user interaction is minimal.
