---
title: token
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetpushinfo/token
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetpushinfo/token'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetpushinfo/token.json'
content_hash: 'sha256:c2809f3b875597ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetPushInfo](../widgetpushinfo.md)

# token

<sub>Instance Property</sub>

A unique push token that may be used to deliver updates for widgets and widget relevances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
let token: Data
```

## Discussion

This token is valid until told otherwise through the [pushTokenDidChange(_:widgets:)](<../widgetpushhandler/pushtokendidchange(__widgets_).md>) method on your push handler.
