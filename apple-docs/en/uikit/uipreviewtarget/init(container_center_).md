---
title: 'init(container:center:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipreviewtarget/init(container:center:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewtarget/init(container:center:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewtarget/init%28container%3Acenter%3A%29.json'
content_hash: 'sha256:0a3bf9b24d3486c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewTarget](../uipreviewtarget.md)

# init(container:center:)

<sub>Initializer</sub>

Creates a preview target object using the specified container view and center point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(container: UIView, center: CGPoint)
```

## Parameters

- `container` — The container for the view being animated. This view must be in a window.

- `center` — The point in `container` at which to place the center of the view being animated. Specify this point in the coordinate system of `container`.

## Return Value

A new preview target object with the specified container and configuration data.

## See Also

### Creating a preview target object

- [- initWithContainer:center:transform:](<init(container_center_transform_).md>) — Creates a preview target object using the specified container view and configuration details.
