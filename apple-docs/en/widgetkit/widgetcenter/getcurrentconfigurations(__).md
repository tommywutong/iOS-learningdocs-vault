---
title: 'getCurrentConfigurations(_:)'
framework: WidgetKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/widgetkit/widgetcenter/getcurrentconfigurations(_:)'
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetcenter/getcurrentconfigurations(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetcenter/getcurrentconfigurations%28_%3A%29.json'
content_hash: 'sha256:5e18d1255da54258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [WidgetKit](../../widgetkit.md) · [WidgetCenter](../widgetcenter.md)

# getCurrentConfigurations(_:)

<sub>Instance Method</sub>

Retrieves information about user-configured widgets.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@preconcurrency func getCurrentConfigurations(_ completion: @escaping @Sendable (Result<[WidgetInfo], any Error>) -> Void)
```

## Parameters

- `completion` — A completion handler called when the widget information is available.

## See Also

### Getting Widget Information

- [shared](shared.md) — The shared widget center.
- [UserInfoKey](userinfokey.md) — An object that defines keys for accessing information in a user info dictionary.
