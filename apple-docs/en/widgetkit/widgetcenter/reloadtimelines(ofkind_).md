---
title: 'reloadTimelines(ofKind:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetcenter/reloadtimelines(ofkind:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/reloadtimelines(ofkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/reloadtimelines%28ofkind%3A%29.json'
content_hash: 'sha256:ada173753eab7dba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# reloadTimelines(ofKind:)

<sub>Instance Method</sub>

Reloads the timelines for all widgets of a particular kind.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func reloadTimelines(ofKind kind: String)
```

## Parameters

- `kind` — A string that identifies the widget and matches the value you used when you created the widget’s configuration.

## See Also

### Reloading Widget Timelines

- [reloadAllTimelines()](<reloadalltimelines().md>) — Reloads the timelines for all configured widgets belonging to the containing app.
