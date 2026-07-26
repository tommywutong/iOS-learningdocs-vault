---
title: 'activityBackgroundTint(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/activitybackgroundtint(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/activitybackgroundtint(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/activitybackgroundtint%28_%3A%29.json'
content_hash: 'sha256:0bbde00919d78dbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# activityBackgroundTint(_:)

<sub>Instance Method</sub>

Sets the tint color for the background of a Live Activity that appears on the Lock Screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func activityBackgroundTint(_ color: Color?) -> some View

```

## Parameters

- `color` — The background tint color to apply. To use the system’s default background material, pass `nil`.

## Discussion

When you set a custom background tint color, consider setting a custom text color for the auxiliary button people use to end a Live Activity on the Lock Screen. To set a custom text color, use the [activitySystemActionForegroundColor(_:)](<activitysystemactionforegroundcolor(__).md>) view modifier.

## See Also

### Configuring a Live Activity

- [activitySystemActionForegroundColor(_:)](<activitysystemactionforegroundcolor(__).md>) — The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [isActivityFullscreen](../environmentvalues/isactivityfullscreen.md) — A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [activityFamily](../environmentvalues/activityfamily.md) — The size family of the current Live Activity.
