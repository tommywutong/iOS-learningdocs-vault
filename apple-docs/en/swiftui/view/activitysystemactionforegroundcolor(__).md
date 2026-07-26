---
title: 'activitySystemActionForegroundColor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/activitysystemactionforegroundcolor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/activitysystemactionforegroundcolor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/activitysystemactionforegroundcolor%28_%3A%29.json'
content_hash: 'sha256:6f120c7566fac544'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# activitySystemActionForegroundColor(_:)

<sub>Instance Method</sub>

The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func activitySystemActionForegroundColor(_ color: Color?) -> some View

```

## Parameters

- `color` — The text color to use. Pass `nil` to use the system’s default color.

## See Also

### Configuring a Live Activity

- [activityBackgroundTint(_:)](<activitybackgroundtint(__).md>) — Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [isActivityFullscreen](../environmentvalues/isactivityfullscreen.md) — A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [activityFamily](../environmentvalues/activityfamily.md) — The size family of the current Live Activity.
