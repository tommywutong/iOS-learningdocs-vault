---
title: 'setEditing(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/setediting(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/setediting(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/setediting%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:68b2824f08b3b6eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# setEditing(_:animated:)

<sub>Instance Method</sub>

Sets whether the view controller shows an editable view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setEditing(_ editing: Bool, animated: Bool)
```

## Parameters

- `editing` — If [true](../../swift/true.md), the view controller should display an editable view; otherwise, [false](../../swift/false.md). If [true](../../swift/true.md) and one of the custom views of the [navigationItem](navigationitem.md) property is set to the value returned by the [editButtonItem](editbuttonitem.md) method, the associated navigation controller displays a Done button; otherwise, an Edit button.

- `animated` — If [true](../../swift/true.md), animates the transition; otherwise, does not.

## Discussion

Subclasses that use an edit-done button must override this method to change their view to an editable state if [editing](isediting.md) is [true](../../swift/true.md) and a non-editable state if it is [false](../../swift/false.md). This method should invoke super’s implementation before updating its view.

## See Also

### Adding editing behaviors to your view controller

- [editing](isediting.md) — A Boolean value indicating whether the view controller currently allows the user to edit the view contents.
- [editButtonItem](editbuttonitem.md) — Returns a bar button item that toggles its title and associated state between Edit and Done.
