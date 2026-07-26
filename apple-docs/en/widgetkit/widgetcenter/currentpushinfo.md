---
title: currentPushInfo
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetcenter/currentpushinfo
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/currentpushinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/currentpushinfo.json'
content_hash: 'sha256:fb205846b4015ee3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# currentPushInfo

<sub>Instance Property</sub>

Provides the current push information for widget reloads and relevance refreshes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
var currentPushInfo: WidgetPushInfo? { get async }
```

## Discussion

May be nil if the token has not completed generation, or if no widgets have been configured for push.
