---
title: LevelOfDetail
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/levelofdetail
source_url: 'https://developer.apple.com/documentation/widgetkit/levelofdetail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/levelofdetail.json'
content_hash: 'sha256:cd82bd58ac1e8f5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# LevelOfDetail

<sub>Structure</sub>

The level of detail the view is recommended to have.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct LevelOfDetail
```

## Overview

The system can update the levelOfDetail value based on user proximity or other system specific factors and allow content customization adapting to show different levels of details.

> [!note] Note
> The `levelOfDetail` can be determined by different factors depending on the platforms. On visionOS, it would be user proximity. On all non-visionOS platforms this will always be `default` LevelOfDetail

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Type Properties

- [default](levelofdetail/default.md) — The default level of details.
- [simplified](levelofdetail/simplified.md) — The level of detail should be simplified.

## See Also

### visionOS widgets

- [Updating your widgets for visionOS](updating-your-widgets-for-visionos.md) — Choose widget styles specific to visionOS, support recessed and elevated appearances, and add proximity awareness to your widget.
- [widgetTexture(_:)](<../swiftui/widgetconfiguration/widgettexture(__).md>) — Specifies the widget texture for this widget.
- [WidgetTexture](widgettexture.md) — Values that define the texture of the widget’s coating layer.
- [supportedMountingStyles(_:)](<../swiftui/widgetconfiguration/supportedmountingstyles(__).md>) — Specifies the mounting style for this widget.
- [WidgetMountingStyle](widgetmountingstyle.md) — Values that define the widget’s supported mounting style.
