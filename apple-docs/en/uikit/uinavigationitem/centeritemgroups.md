---
title: centerItemGroups
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/centeritemgroups
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/centeritemgroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/centeritemgroups.json'
content_hash: 'sha256:adfa8be72715972c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# centerItemGroups

<sub>Instance Property</sub>

Customizable item groups to display in the center section of the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var centerItemGroups: [UIBarButtonItemGroup] { get set }
```

## Discussion

Use this property to specify _center item groups_, groups of controls that appear in the navigation bar to provide quick access to your app’s capabilities. Center items appear in the center of the navigation bar for the [UINavigationItemStyleBrowser](itemstyle/browser.md) and [UINavigationItemStyleEditor](itemstyle/editor.md) styles, and in the overflow menu for the [UINavigationItemStyleNavigator](itemstyle/navigator.md) style.

Optionally, you can allow people to customize the layout of center item groups and preserve that customization across app launches. When you create center item groups, you can choose from three types of behaviors:

- Create a fixed group to disallow moving or removing that group from the navigation bar.
- Create a movable group to allow moving a group in the navigation bar, but not removing it.
- Create an optional group to allow moving, removing, or adding back that group.

The following code enables center item layout customization by assigning a [customizationIdentifier](customizationidentifier.md). Then, it shows two approaches to creating center item groups: creating a group from an array of items and creating a group from a single item.

```swift
// Specify a unique customization identifier to enable navigation bar layout customization.
navigationItem.customizationIdentifier = "MyCustomNavigationItem"

// Create a fixed group with multiple items.
let editingGroup = UIBarButtonItemGroup.fixedGroup(items: [
    UIBarButtonItem(title: "Undo", image: UIImage(systemName: "arrow.uturn.backward"), primaryAction: UIAction { _ in
        // Implement undo action.
    }),
    UIBarButtonItem(title: "Redo", image: UIImage(systemName: "arrow.uturn.forward"), primaryAction: UIAction { _ in
        // Implement redo action.
    })
])

// Create a movable group from a single item.
let croppingItem = UIBarButtonItem(title: "Crop", image: UIImage(systemName: "crop"), primaryAction: UIAction { _ in
    // Implement crop action.
})
let croppingGroup = croppingItem.creatingMovableGroup(customizationIdentifier: "Cropping")

navigationItem.centerItemGroups = [editingGroup, croppingGroup]
```

## See Also

### Specifying custom views

- [leadingItemGroups](leadingitemgroups.md) — Item groups to display in the leading section of the navigation bar.
- [trailingItemGroups](trailingitemgroups.md) — Item groups to display in the trailing section of the navigation bar.
- [pinnedTrailingGroup](pinnedtrailinggroup.md) — The item group to display on the trailing edge of the navigation bar, on the trailing side of the overflow and search items.
- [titleView](titleview.md) — A custom view that displays in the center of the navigation bar when the receiver is the top item.
- [subtitleView](subtitleview.md) — A custom view to display below the title in the navigation bar.
- [largeSubtitleView](largesubtitleview.md) — A custom view to display below the large title.
- [leftBarButtonItems](leftbarbuttonitems.md) — An array of custom bar button items to display on the left (or leading) side of the navigation bar when the navigation item is the top item.
- [leftBarButtonItem](leftbarbuttonitem.md) — A custom bar button item that displays on the left (or leading) edge of the navigation bar when the navigation item is the top item.
- [rightBarButtonItems](rightbarbuttonitems.md) — An array of custom bar button items to display on the right (or trailing) side of the navigation bar when the navigation item is the top item.
- [rightBarButtonItem](rightbarbuttonitem.md) — A custom bar button item that displays on the right (or trailing) edge of the navigation bar when the navigation item is the top item.
- [- setLeftBarButtonItems:animated:](<setleftbarbuttonitems(__animated_).md>) — Sets the left bar button items, optionally animating the transition to the new items.
- [- setLeftBarButtonItem:animated:](<setleftbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the new item.
- [- setRightBarButtonItems:animated:](<setrightbarbuttonitems(__animated_).md>) — Sets the right bar button items, optionally animating the transition to the new items.
- [- setRightBarButtonItem:animated:](<setrightbarbutton(__animated_).md>) — Sets the custom bar button item, optionally animating the transition to the view.
