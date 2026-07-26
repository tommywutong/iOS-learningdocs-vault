---
title: 'resolvedColor(with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/resolvedcolor(with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/resolvedcolor(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/resolvedcolor%28with%3A%29.json'
content_hash: 'sha256:6057161e9c062dec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# resolvedColor(with:)

<sub>Instance Method</sub>

Returns the version of the current color that results from the specified traits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resolvedColor(with traitCollection: UITraitCollection) -> UIColor
```

## Parameters

- `traitCollection` — The traits to use when resolving the color information.

## Return Value

The version of the color to display for the specified traits.

## Discussion

Use this method when you need to resolve a dynamic color to a specific color value for the specified trait collection. For example, reading the [CGColor](cgcolor.md) property or calling [- getRed:green:blue:alpha:](<getred(__green_blue_alpha_).md>) resolves a dynamic color to a specific color value that’s no longer dynamic. If your calling context isn’t inside one of the methods documented in the [currentTraitCollection](../uitraitcollection/current.md) property, you need to provide a trait collection from an appropriate trait environment, such as your view or view controller.

The example below uses this method set a border color on a [CALayer](../../quartzcore/calayer.md):

```swift
// This method sets the border color when UITraitCollection.current is undefined.
func updateBorderColor(layer: CALayer) {
    
    // Read the trait collection from the view.
    let traitCollection = view.traitCollection
    // Use the trait collection to resolve a dynamic color.
    let borderColor = UIColor.label.resolvedColor(with: traitCollection)
    // Use the CGColor value of the resolved color.
    layer.borderColor = borderColor.cgColor
}
```

## See Also

### Related Documentation

- [- performAsCurrentTraitCollection:](<../uitraitcollection/performascurrent(__).md>) — Executes custom code using the traits of the receiving trait collection.
