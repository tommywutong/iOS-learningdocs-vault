---
title: appSettings
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/appsettings
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/appsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/appsettings.json'
content_hash: 'sha256:fad98a1926fe7434'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# appSettings

<sub>Type Property</sub>

Placement for commands that expose app settings and preferences.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let appSettings: CommandGroupPlacement
```

## Discussion

By default, this group includes the following command in macOS:

- Preferences

## See Also

### App interactions

- [appInfo](appinfo.md) — Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [appTermination](apptermination.md) — Placement for commands that result in app termination.
- [appVisibility](appvisibility.md) — Placement for commands that control the visibility of running apps.
- [systemServices](systemservices.md) — Placement for commands that expose services other apps provide.
