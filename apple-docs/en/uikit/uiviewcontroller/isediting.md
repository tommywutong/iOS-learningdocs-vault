---
title: isEditing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/isediting
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/isediting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/isediting.json'
content_hash: 'sha256:68fb721a519e44b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# isEditing

<sub>Instance Property</sub>

A Boolean value indicating whether the view controller currently allows the user to edit the view contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEditing: Bool { get set }
```

## Discussion

If [true](../../swift/true.md), the view controller currently allows editing; otherwise, [false](../../swift/false.md).

If the view is editable and the associated navigation controller contains an edit-done button, then a Done button is displayed; otherwise, an Edit button is displayed. Clicking either button toggles the state of this property. Add an edit-done button by setting the custom left or right view of the navigation item to the value returned by the [editButtonItem](editbuttonitem.md) method. Set the [editing](isediting.md) property to the initial state of your view. Use the [- setEditing:animated:](<setediting(__animated_).md>) method as an action method to animate the transition of this state if the view is already displayed.

## See Also

### Adding editing behaviors to your view controller

- [- setEditing:animated:](<setediting(__animated_).md>) — Sets whether the view controller shows an editable view.
- [editButtonItem](editbuttonitem.md) — Returns a bar button item that toggles its title and associated state between Edit and Done.
