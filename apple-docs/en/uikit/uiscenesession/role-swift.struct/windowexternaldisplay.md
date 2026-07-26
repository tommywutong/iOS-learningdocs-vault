---
title: windowExternalDisplay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS 13.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplay
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession/role-swift.struct/windowexternaldisplay.json'
content_hash: 'sha256:5cf716d4d6fb5ec7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISceneSession](../../uiscenesession.md) · [Role](../role-swift.struct.md)

# windowExternalDisplay

<sub>Type Property</sub>

A scene that displays noninteractive windows on an externally connected display.

> [!warning] Deprecated
> Use [UIWindowSceneSessionRoleExternalDisplayNonInteractive](windowexternaldisplaynoninteractive.md) for a scene that displays noninteractive windows on an externally connected screen. A scene that displays interactive windows uses [UIWindowSceneSessionRoleApplication](windowapplication.md), even if the windows display on an externally connected screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let windowExternalDisplay: UISceneSession.Role
```

## See Also

### Determining scene roles

- [UIWindowSceneSessionRoleApplication](windowapplication.md) — A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [UIWindowSceneSessionRoleExternalDisplayNonInteractive](windowexternaldisplaynoninteractive.md) — A scene that displays noninteractive windows on an externally connected display.
- [carTemplateApplication](cartemplateapplication.md) — A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](cptemplateapplicationdashboardscenesessionroleapplication.md) — A scene that displays navigation content on the CarPlay Dashboard.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](cptemplateapplicationinstrumentclusterscenesessionroleapplication.md) — A scene that displays navigation content on the CarPlay Instruments Cluster.
