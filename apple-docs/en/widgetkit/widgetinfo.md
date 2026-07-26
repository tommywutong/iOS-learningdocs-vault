---
title: WidgetInfo
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetinfo
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetinfo.json'
content_hash: 'sha256:528c7f34decbab20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetInfo

<sub>Structure</sub>

A structure that contains information about user-configured widgets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@preconcurrency struct WidgetInfo
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Configured Widget Information

- [kind](widgetinfo/kind.md) — The string specified during creation of the widget’s configuration.
- [family](widgetinfo/family.md) — The size of the widget: small, medium, or large.
- [configuration](widgetinfo/configuration.md) — A SiriKit intent that contains user-edited values.

### Identifying Widget Information

- [id](widgetinfo/id.md) — The stable identity of the widget.

### Instance Methods

- [widgetConfigurationIntent(of:)](<widgetinfo/widgetconfigurationintent(of_).md>) — Gets the associated App Intent.

### Default Implementations

- [Identifiable Implementations](widgetinfo/identifiable-implementations.md)

## See Also

### Configurable widgets

- [Making a configurable widget](making-a-configurable-widget.md) — Give people the option to customize their widgets by adding a custom app intent to your project.
- [Migrating widgets from SiriKit Intents to App Intents](migrating-from-sirikit-intents-to-app-intents.md) — Configure your widgets for backward compatibility.
- [AppIntentConfiguration](appintentconfiguration.md) — An object describing the content of a widget that uses a custom intent to provide user-configurable options.
