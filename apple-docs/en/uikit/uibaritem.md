---
title: UIBarItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibaritem
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem.json'
content_hash: 'sha256:a4151315f011551f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIBarItem

<sub>Class</sub>

An abstract superclass for items that you can add to a bar that appears at the bottom of the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIBarItem
```

## Overview

Items on a bar behave in a way similar to buttons (instances of [UIButton](uibutton.md)). They have a title, image, action, and target. You can also enable and disable an item on a bar.

### Customize appearance

You can customize the image to represent the item, and the position of the image, using [image](uibaritem/image.md) and [imageInsets](uibaritem/imageinsets.md) respectively.

You can also specify a custom image and position to use in landscape orientation when using the iPhone appearance idiom using [landscapeImagePhone](uibaritem/landscapeimagephone.md) and [landscapeImagePhoneInsets](uibaritem/landscapeimagephoneinsets.md) respectively. In addition, you can customize the title’s text attributes using [- setTitleTextAttributes:forState:](<uibaritem/settitletextattributes(__for_).md>), either for a single item, or for all items by using the appearance proxy (for example, `[UIBarItem appearance]`).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIBarButtonItem](uibarbuttonitem.md), [UITabBarItem](uitabbaritem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIAppearance](uiappearance.md)

## Topics

### Creating a bar item

- [- init](<uibaritem/init().md>) — Initializes the bar item to its default state.
- [- initWithCoder:](<uibaritem/init(coder_).md>) — Creates a bar item from data in an unarchiver.

### Getting and setting properties

- [title](uibaritem/title.md) — The title displayed on the item.
- [image](uibaritem/image.md) — The image used to represent the item.
- [landscapeImagePhone](uibaritem/landscapeimagephone.md) — The image to use to represent the item in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImage](uibaritem/largecontentsizeimage.md) — The image to display for users who are blind or have low vision.
- [imageInsets](uibaritem/imageinsets.md) — The image inset or outset for each edge.
- [landscapeImagePhoneInsets](uibaritem/landscapeimagephoneinsets.md) — The image inset or outset for each edge of the image in landscape orientation when using the iPhone appearance idiom.
- [largeContentSizeImageInsets](uibaritem/largecontentsizeimageinsets.md) — The insets to apply to the bar item’s large image when displaying the image in an assistive UI.
- [enabled](uibaritem/isenabled.md) — A Boolean value indicating whether the item is enabled.
- [tag](uibaritem/tag.md) — The bar item’s tag, an app-supplied integer that you can use to identify bar item objects in your app.

### Customizing appearance

- [- setTitleTextAttributes:forState:](<uibaritem/settitletextattributes(__for_).md>) — Sets the title’s text attributes for a given control state.
- [- titleTextAttributesForState:](<uibaritem/titletextattributes(for_).md>) — Returns the title’s text attributes for a given control state.

## See Also

### Bars

- [UIBarButtonItem](uibarbuttonitem.md) — A specialized button for placement on a toolbar, navigation bar, or shortcuts bar.
- [UIBarButtonItemGroup](uibarbuttonitemgroup.md) — A group of one or more bar button items for placement on a navigation bar or shortcuts bar.
- [UIBarButtonItemVisibilityPriority](uibarbuttonitemvisibilitypriority.md) _(beta)_
- [UINavigationBar](uinavigationbar.md) — Navigational controls that display in a bar along the top of the screen, usually in conjunction with a navigation controller.
- [UISearchBar](uisearchbar.md) — A specialized view for receiving search-related information from the user.
- [UIToolbar](uitoolbar.md) — A control that displays one or more buttons along an edge of your interface.
- [UITabBar](uitabbar.md) — A control that displays one or more buttons in a tab bar for selecting between different subtasks, views, or modes in an app.
- [UITabBarItem](uitabbaritem.md) — An object that describes an item in a tab bar.
- [UIBarPositioning](uibarpositioning.md) — A set of methods for defining the positioning of bars in iOS apps.
- [UIBarPositioningDelegate](uibarpositioningdelegate.md) — A set of methods that support the positioning of a bar that conforms to the [UIBarPositioning](uibarpositioning.md) protocol.
- [UIBarMinimization](uibarminimization-swift.struct.md)
