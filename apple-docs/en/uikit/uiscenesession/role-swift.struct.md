---
title: UISceneSession.Role
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesession/role-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession/role-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession/role-swift.struct.json'
content_hash: 'sha256:cf81728ff97dc15e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSession](../uiscenesession.md)

# UISceneSession.Role

<sub>Structure</sub>

Constants that indicate the possible roles for a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Role
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Determining scene roles

- [UIWindowSceneSessionRoleApplication](role-swift.struct/windowapplication.md) — A scene that displays interactive windows on the device’s built-in display or an externally connected display.
- [UIWindowSceneSessionRoleExternalDisplay](role-swift.struct/windowexternaldisplay.md) — A scene that displays noninteractive windows on an externally connected display. _(deprecated)_
- [UIWindowSceneSessionRoleExternalDisplayNonInteractive](role-swift.struct/windowexternaldisplaynoninteractive.md) — A scene that displays noninteractive windows on an externally connected display.
- [carTemplateApplication](role-swift.struct/cartemplateapplication.md) — A scene that displays interactive content on a CarPlay-enabled vehicle screen.
- [CPTemplateApplicationDashboardSceneSessionRoleApplication](role-swift.struct/cptemplateapplicationdashboardscenesessionroleapplication.md) — A scene that displays navigation content on the CarPlay Dashboard.
- [CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication](role-swift.struct/cptemplateapplicationinstrumentclusterscenesessionroleapplication.md) — A scene that displays navigation content on the CarPlay Instruments Cluster.

### Creating scene roles

- [init(rawValue:)](<role-swift.struct/init(rawvalue_).md>) — Creates a scene role with the specified raw value.

### Type Properties

- [UISceneSessionRoleImmersiveSpaceApplication](role-swift.struct/immersivespaceapplication.md)
- [UIWindowSceneSessionRoleVolumetricApplication](role-swift.struct/windowapplicationvolumetric.md)

## See Also

### Getting the configuration attributes

- [name](../uisceneconfiguration/name.md) — The app-specific name assigned to the scene configuration.
- [role](../uisceneconfiguration/role.md) — The role assigned to the scene configuration.
