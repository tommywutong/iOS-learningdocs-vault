---
title: selectedItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitabbar/selecteditem
source_url: 'https://developer.apple.com/documentation/uikit/uitabbar/selecteditem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitabbar/selecteditem.json'
content_hash: 'sha256:fd01e5e5b9583e1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITabBar](../uitabbar.md)

# selectedItem

<sub>Instance Property</sub>

The currently selected item on the tab bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var selectedItem: UITabBarItem? { get set }
```

## Discussion

Use this property to get the currently selected item. If you change the value of this property, the tab bar selects the corresponding item and updates the tab bar’s appearance accordingly. Set the property to `nil` to clear the selection.

When an item is selected, the tab bar displays the image in the tab bar item’s [selectedImage](../uitabbaritem/selectedimage.md) property. If the [selectedImageTintColor](selectedimagetintcolor.md) property is set, the tab bar also applies the color in that property to the selected image. To prevent system coloring of an item, provide images using the [UIImageRenderingModeAlwaysOriginal](../uiimage/renderingmode-swift.enum/alwaysoriginal.md) rendering mode.

The default value for this property is `nil`.

## See Also

### Configuring tab bar items

- [items](items.md) — The items displayed by the tab bar.
- [- setItems:animated:](<setitems(__animated_).md>) — Sets the items on the tab bar, optionally animating any changes into position.
