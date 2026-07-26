---
title: editButtonItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/editbuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/editbuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/editbuttonitem.json'
content_hash: 'sha256:dfa5d89a0256126d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# editButtonItem

<sub>Instance Property</sub>

Returns a bar button item that toggles its title and associated state between Edit and Done.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editButtonItem: UIBarButtonItem { get }
```

## Discussion

If one of the custom views of the [navigationItem](navigationitem.md) property is set to the returned object, the associated navigation bar displays an Edit button if [editing](isediting.md) is [false](../../swift/false.md) and a Done button if [editing](isediting.md) is [true](../../swift/true.md). The default button action invokes the [- setEditing:animated:](<setediting(__animated_).md>) method.

## See Also

### Adding editing behaviors to your view controller

- [editing](isediting.md) — A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [- setEditing:animated:](<setediting(__animated_).md>) — Sets whether the view controller shows an editable view.
