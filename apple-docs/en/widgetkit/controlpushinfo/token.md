---
title: token
framework: WidgetKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/controlpushinfo/token
source_url: 'https://developer.apple.com/documentation/widgetkit/controlpushinfo/token'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlpushinfo/token.json'
content_hash: 'sha256:8007b5888d6bbdc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlPushInfo](../controlpushinfo.md)

# token

<sub>Instance Property</sub>

A unique push token that may be used to deliver updates for this control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
let token: Data
```

## Discussion

This token is valid until told otherwise through the [pushTokensDidChange(controls:)](<../controlpushhandler/pushtokensdidchange(controls_).md>) method on your push handler.
