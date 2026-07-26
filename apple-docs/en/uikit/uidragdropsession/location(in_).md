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
doc_path: '/documentation/uikit/uidragdropsession/location(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/location(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/location%28in%3A%29.json'
content_hash: 'sha256:9a7708655edf6328'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# location(in:)

<sub>Instance Method</sub>

Returns the geometrical location of the user’s drag activity within the specified view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func location(in view: UIView) -> CGPoint
```

## Parameters

- `view` — The view whose coordinate system is used to get the location.

## Return Value

The location point of the drag activity, in the coordinate system of the specified view.
