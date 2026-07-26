---
title: relevance()
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/timelineprovider/relevance()-7036j
source_url: 'https://developer.apple.com/documentation/widgetkit/timelineprovider/relevance()-7036j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/timelineprovider/relevance%28%29-7036j.json'
content_hash: 'sha256:a772125f9f4e105f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [TimelineProvider](../timelineprovider.md)

# relevance()

<sub>Instance Method</sub>

Provides an object containing attributes that describe when a specific widget is relevant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func relevance() async -> WidgetRelevance<Void>
```

## Return Value

The object that contains attributes that describe when a specific widget is relevant.

## Discussion

The system can use the relevance to show this widget in the Smart Stack when the provided relevance matches a person’s context. For example, if you indicate relevance at a specific location, the system could show the widget when a person is at or close to the location.

By default, this method returns no relevances. Implement this requirement to tell the system that your widget is relevant.

> [!note] Note
> Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [Increasing the visibility of widgets in Smart Stacks](../widget-suggestions-in-smart-stacks.md).
