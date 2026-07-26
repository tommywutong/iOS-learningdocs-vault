---
title: lookToScrollAxes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/looktoscrollaxes
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/looktoscrollaxes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/looktoscrollaxes.json'
content_hash: 'sha256:b095f8bd9194517f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# lookToScrollAxes

<sub>Instance Property</sub>

Setting lookToScrollAxes turns on Look to Scroll for the scroll view in directions of the defined axis

<sub>visionOS</sub>

```swift
var lookToScrollAxes: UIAxis { get set }
```

## Discussion

When enabling Look to Scroll, you should consider the type of content that is in the scroll view. For best experience, this API should be on scrolling area of an app that’s considered “content”. Examples: - The message body area in Mail, but not the list of messages that’s considered navigation. - The note body in Notes - In TV app, the tile design including both horizontal and vertical scrolling views.

Note: Look to Scroll is designed for large and meaningful content. For privacy reasons, exceedingly small scroll views or having an unusually high number of scroll views in a scene could cause Look to Scroll to auto disable.

Additional requirements for enabling Look to Scroll - There can only be a max of 6 gaze scrolling scroll view per scene - isPagingEnabled must not be enabled
