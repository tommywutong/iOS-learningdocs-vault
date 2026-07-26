---
title: WidgetPushInfo
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetpushinfo
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetpushinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetpushinfo.json'
content_hash: 'sha256:6399ec35f1c90b7a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetPushInfo

<sub>Structure</sub>

A structure that contains information about the push token for updating widgets and widget relevances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetPushInfo
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [token](widgetpushinfo/token.md) — A unique push token that may be used to deliver updates for widgets and widget relevances.

## See Also

### Push notification updates

- [Updating widgets with WidgetKit push notifications](updating-widgets-with-widgetkit-push-notifications.md) — Use WidgetKit to receive push tokens and reload your widgets with remote push notifications.
- [WidgetPushHandler](widgetpushhandler.md) — A type that can receive push information about widget refreshes and relevance refreshes.
