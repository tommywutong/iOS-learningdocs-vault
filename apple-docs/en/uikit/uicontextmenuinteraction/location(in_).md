---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuinteraction/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteraction/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteraction/location%28in%3A%29.json'
content_hash: 'sha256:229b0d0aae9dcadf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteraction](../uicontextmenuinteraction.md)

# location(in:)

<sub>Instance Method</sub>

Returns the location of the user interaction in the specified view’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func location(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view containing the target coordinate system. To return a point in the window’s coordinate system, specify `nil`.

## Return Value

The location of the interaction specified in the coordinate system of `view`.
