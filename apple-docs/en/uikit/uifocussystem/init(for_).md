---
title: 'init(for:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+（15.0 起废弃）, iPadOS 12.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS 12.0+（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uifocussystem/init(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/init%28for%3A%29.json'
content_hash: 'sha256:1e72702511546e67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# init(for:)

<sub>Initializer</sub>

Retrieves a focus system object that contains the state information for the specified object.

> [!warning] Deprecated
> Use `UIFocusSystem/focusSystem(for:)` instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(for environment: any UIFocusEnvironment)
```

## Parameters

- `environment` — The object whose state you want to return. Specify the view, view controller, or window whose state you want. You can also specify any other object that adopts the [UIFocusEnvironment](../uifocusenvironment.md) protocol.

## Return Value

The [UIFocusSystem](../uifocussystem.md) object that manages the state for the specified object or `nil` if focus interactions are not available for the object.
