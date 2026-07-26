---
title: 'location(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringloadedinteractioncontext/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractioncontext/location%28in%3A%29.json'
content_hash: 'sha256:ce15de057403920c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringLoadedInteractionContext](../uispringloadedinteractioncontext.md)

# location(in:)

<sub>Instance Method</sub>

Returns the location of the drag activity within the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func location(in view: UIView?) -> CGPoint
```

## Parameters

- `view` — The view that is used to determine the location of the drag activity.

## Return Value

A point in the local coordinate system of `view`.

## Discussion

To get the location of the drag activity within the window, use `nil` for the view.
