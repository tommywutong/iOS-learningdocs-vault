---
title: activityFamily
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/activityfamily
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/activityfamily'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/activityfamily.json'
content_hash: 'sha256:ca4144119833e970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# activityFamily

<sub>Instance Property</sub>

The size family of the current Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var activityFamily: ActivityFamily { get set }
```

## Discussion

A Live Activity you initiate on one device can also appear on a remote device that renders the Live Activity in a different family size. As a result, it renders for a specific family, depending on both the device and the location in which it appears. For example, when rendering on the iOS or iPadOS Lock Screen, the current family is doc://com.apple.comdumentation/documentation/WidgetKit/ActivityFamily/medium.

Use [supplementalActivityFamilies(_:)](<../widgetconfiguration/supplementalactivityfamilies(__).md>) to opt in and allow your Live Activity to render with additional families.

## See Also

### Configuring a Live Activity

- [activitySystemActionForegroundColor(_:)](<../view/activitysystemactionforegroundcolor(__).md>) — The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [activityBackgroundTint(_:)](<../view/activitybackgroundtint(__).md>) — Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [isActivityFullscreen](isactivityfullscreen.md) — A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
