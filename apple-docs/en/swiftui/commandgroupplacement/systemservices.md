---
title: systemServices
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/commandgroupplacement/systemservices
source_url: 'https://developer.apple.com/documentation/swiftui/commandgroupplacement/systemservices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/commandgroupplacement/systemservices.json'
content_hash: 'sha256:92228a3058069b56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [CommandGroupPlacement](../commandgroupplacement.md)

# systemServices

<sub>Type Property</sub>

Placement for commands that expose services other apps provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let systemServices: CommandGroupPlacement
```

## Discussion

By default, this group includes the following command in macOS:

- Services submenu (managed automatically)

## See Also

### App interactions

- [appInfo](appinfo.md) — Placement for commands that provide information about the app, the terms of the user’s license agreement, and so on.
- [appSettings](appsettings.md) — Placement for commands that expose app settings and preferences.
- [appTermination](apptermination.md) — Placement for commands that result in app termination.
- [appVisibility](appvisibility.md) — Placement for commands that control the visibility of running apps.
