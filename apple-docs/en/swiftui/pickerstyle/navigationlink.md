---
title: navigationLink
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pickerstyle/navigationlink
source_url: 'https://developer.apple.com/documentation/swiftui/pickerstyle/navigationlink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle/navigationlink.json'
content_hash: 'sha256:fa97a97c5d0610aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PickerStyle](../pickerstyle.md)

# navigationLink

<sub>Type Property</sub>

A picker style represented by a navigation link that presents the options by pushing a List-style picker view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var navigationLink: NavigationLinkPickerStyle { get }
```

## Discussion

In navigation stacks, prefer the default [menu](menu.md) style. Consider the navigation link style when you have a large number of options or your design is better expressed by pushing onto a stack.

To apply this style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<../view/pickerstyle(__).md>) modifier.

## See Also

### Getting built-in picker styles

- [automatic](automatic.md) — The default picker style, based on the picker’s context.
- [inline](inline.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](menu.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [palette](palette.md) — A picker style that presents the options as a row of compact elements.
- [radioGroup](radiogroup.md) — A picker style that presents the options as a group of radio buttons.
- [segmented](segmented.md) — A picker style that presents the options in a segmented control.
- [tabs](tabs.md) — A picker style that presents options as segmented tabs. _(beta)_
- [wheel](wheel.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
