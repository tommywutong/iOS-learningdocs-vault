---
title: WidgetMountingStyle
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetmountingstyle
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetmountingstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetmountingstyle.json'
content_hash: 'sha256:573b1217e8448816'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetMountingStyle

<sub>Structure</sub>

Values that define the widget’s supported mounting style.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct WidgetMountingStyle
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [elevated](widgetmountingstyle/elevated.md) — Mounting style surrounding the widget with a composite material
- [recessed](widgetmountingstyle/recessed.md) — Mounting style where a widget is displayed within a recessed portal

## See Also

### visionOS widgets

- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md) — Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [widgetTexture(_:)](<../swiftui/widgetconfiguration/widgettexture(__).md>) — Specifies the widget texture for this widget.
- [WidgetTexture](widgettexture.md) — Values that define the texture of the widget’s coating layer.
- [supportedMountingStyles(_:)](<../swiftui/widgetconfiguration/supportedmountingstyles(__).md>) — Specifies the mounting style for this widget.
- [LevelOfDetail](levelofdetail.md) — The level of detail the view is recommended to have.
