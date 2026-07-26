---
title: 'viewWithTag(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/viewwithtag(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/viewwithtag(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/viewwithtag%28_%3A%29.json'
content_hash: 'sha256:ba303be98e78fb15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# viewWithTag(_:)

<sub>Instance Method</sub>

Returns the view whose tag matches the specified value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewWithTag(_ tag: Int) -> UIView?
```

## Parameters

- `tag` — The tag value to search for.

## Return Value

The view in the receiver’s hierarchy whose tag property matches the value in the `tag` parameter.

## Discussion

This method searches the current view and all of its subviews for the specified view.

## See Also

### Identifying the view at runtime

- [tag](tag.md) — An integer that you can use to identify view objects in your application.
