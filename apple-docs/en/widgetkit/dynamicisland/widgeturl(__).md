---
title: 'widgetURL(_:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/dynamicisland/widgeturl(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/dynamicisland/widgeturl(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/dynamicisland/widgeturl%28_%3A%29.json'
content_hash: 'sha256:4fa03b4925ef80e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [DynamicIsland](../dynamicisland.md)

# widgetURL(_:)

<sub>Instance Method</sub>

Sets the URL that opens the corresponding app of a Live Activity when a user taps on the Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func widgetURL(_ url: URL?) -> DynamicIsland
```

## Parameters

- `url` — The URL that opens the app.

## Return Value

The configuration object for the Dynamic Island with the specified URL.

## Discussion

By setting the URL with this function, it becomes the default URL for deep linking into the app for each view of the Live Activity. However, if you include a [Link](../../swiftui/link.md) in the Live Activity, the link takes priority over the default URL. When a person taps on the `Link`, it takes them to the place in the app that corresponds to the URL of the `Link`.
