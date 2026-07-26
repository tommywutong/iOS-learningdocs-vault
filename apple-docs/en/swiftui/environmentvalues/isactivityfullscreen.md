---
title: isActivityFullscreen
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/isactivityfullscreen
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/isactivityfullscreen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/isactivityfullscreen.json'
content_hash: 'sha256:b58a3fd6b174b708'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isActivityFullscreen

<sub>Instance Property</sub>

A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@backDeployed(before: iOS 17.0)
var isActivityFullscreen: Bool { get }
```

## Discussion

When a Live Activity fills the entire screen, the system extends the background tint color you set with the [activityBackgroundTint(_:)](<../view/activitybackgroundtint(__).md>) modifier to fill the screen.

Note that this environment variable is always `false` in iOS 16.

## See Also

### Configuring a Live Activity

- [activitySystemActionForegroundColor(_:)](<../view/activitysystemactionforegroundcolor(__).md>) — The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [activityBackgroundTint(_:)](<../view/activitybackgroundtint(__).md>) — Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [activityFamily](activityfamily.md) — The size family of the current Live Activity.
