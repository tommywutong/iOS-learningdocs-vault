---
title: 'invalidate(view:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS, Swift 5.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewinvalidating/invalidate(view:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewinvalidating/invalidate(view:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewinvalidating/invalidate%28view%3A%29.json'
content_hash: 'sha256:05108eead84f0892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewInvalidating](../uiviewinvalidating.md)

# invalidate(view:)

<sub>Instance Method</sub>

Indicates to the system that an aspect of a view is invalid and triggers the necessary update.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidate(view: UIView)
```

## Parameters

- `view` — The view that requires invalidating.

## Discussion

A type that conforms to [UIViewInvalidating](../uiviewinvalidating.md) implements this method to perform any actions necessary to notify the system that an aspect of your view is invalid. For more info, see [Invalidating](../uiview/invalidating.md).

## See Also

### Invalidating the view

- [Invalidations](../uiview/invalidations.md) — Changes that cause an aspect of a view to be invalid and require an update.
