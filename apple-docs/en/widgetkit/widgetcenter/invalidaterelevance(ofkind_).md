---
title: 'invalidateRelevance(ofKind:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetcenter/invalidaterelevance(ofkind:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/invalidaterelevance(ofkind:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/invalidaterelevance%28ofkind%3A%29.json'
content_hash: 'sha256:d4f02f6ffa2a5419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# invalidateRelevance(ofKind:)

<sub>Instance Method</sub>

Mark the relevance for a kind as invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func invalidateRelevance(ofKind kind: String)
```

## Parameters

- `kind` — A string that identifies the widget and matches the value you used when you created the widget’s configuration.

## Discussion

Call this function when the relevance returned for a widget has changed and needs to be reloaded.

Marking relevance as invalid causes the system to call, at a later time, the `relevance` function on the timeline provider that matches the specified kind.
