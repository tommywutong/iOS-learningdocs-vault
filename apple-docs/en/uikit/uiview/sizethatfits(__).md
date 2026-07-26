---
title: 'sizeThatFits(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/sizethatfits(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/sizethatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/sizethatfits%28_%3A%29.json'
content_hash: 'sha256:67543d95237dc3c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# sizeThatFits(_:)

<sub>Instance Method</sub>

Asks the view to calculate and return the size that best fits the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sizeThatFits(_ size: CGSize) -> CGSize
```

## Parameters

- `size` — The size for which the view should calculate its best-fitting size.

## Return Value

A new size that fits the receiver’s subviews.

## Discussion

The default implementation of this method returns the existing size of the view. Subclasses can override this method to return a custom value based on the desired layout of any subviews. For example, a [UISwitch](../uiswitch.md) object returns a fixed size value that represents the standard size of a switch view, and a [UIImageView](../uiimageview.md) object returns the size of the image it is currently displaying.

This method does not resize the receiver.

## See Also

### Related Documentation

- [frame](frame.md) — The frame rectangle, which describes the view’s location and size in its superview’s coordinate system.
- [bounds](bounds.md) — The bounds rectangle, which describes the view’s location and size in its own coordinate system.

### Configuring the resizing behavior

- [contentMode](contentmode-swift.property.md) — A flag used to determine how a view lays out its content when its bounds change.
- [ContentMode](contentmode-swift.enum.md) — Options to specify how a view adjusts its content when its size changes.
- [- sizeToFit](<sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [autoresizesSubviews](autoresizessubviews.md) — A Boolean value that determines whether the receiver automatically resizes its subviews when its bounds change.
- [autoresizingMask](autoresizingmask-swift.property.md) — An integer bit mask that determines how the receiver resizes itself when its superview’s bounds change.
