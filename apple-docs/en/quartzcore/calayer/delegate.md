---
title: delegate
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/delegate
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/delegate.json'
content_hash: 'sha256:8596d6e2964b7a66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# delegate

<sub>Instance Property</sub>

The layer’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any CALayerDelegate)? { get set }
```

## Discussion

You can use a delegate object to provide the layer’s contents, handle the layout of any sublayers, and provide custom actions in response to layer-related changes. The object you assign to this property should implement one or more of the methods of the [CALayerDelegate](../calayerdelegate.md) informal protocol. For more information about that protocol, see `CALayerDelegate`

In iOS, if the layer is associated with a [UIView](../../uikit/uiview.md) object, this property _must_ be set to the view that owns the layer.
