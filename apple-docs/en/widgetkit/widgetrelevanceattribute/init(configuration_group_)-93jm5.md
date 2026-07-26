---
title: 'init(configuration:group:)'
framework: WidgetKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 26.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetrelevanceattribute/init(configuration:group:)-93jm5'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetrelevanceattribute/init(configuration:group:)-93jm5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetrelevanceattribute/init%28configuration%3Agroup%3A%29-93jm5.json'
content_hash: 'sha256:6d22af54f959e539'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetRelevanceAttribute](../widgetrelevanceattribute.md)

# init(configuration:group:)

<sub>Initializer</sub>

Associates the widget kind with a group. When multiple widgets are in the same group, the system will only suggest one member of the group simultaneously. Widgets in the same group are interpreted to contain redundant information, and therefore should not be presented together.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
init(configuration: Configuration, group: WidgetRelevanceGroup)
```

## Parameters

- `configuration` — The specific configuration

- `group` — The group to associate the widget with

## Discussion

Multiple groups can be associated with the same widget by providing multiple `WidgetRelevanceAttribute` instances with different groups.
