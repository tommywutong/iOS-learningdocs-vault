---
title: 'pushTokensDidChange(controls:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/controlpushhandler/pushtokensdidchange(controls:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/controlpushhandler/pushtokensdidchange(controls:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/controlpushhandler/pushtokensdidchange%28controls%3A%29.json'
content_hash: 'sha256:eac242784b8e85f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [ControlPushHandler](../controlpushhandler.md)

# pushTokensDidChange(controls:)

<sub>Instance Method</sub>

Handle push tokens changing for configured controls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
func pushTokensDidChange(controls: [ControlInfo])
```

## Parameters

- `controls` — Information about controls that support push updates.

## Discussion

This function always provides information for all controls that support push updates even if only some of the tokens have changed.
