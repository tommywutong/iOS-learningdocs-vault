---
title: 'init(style:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitableviewcontroller/init(style:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcontroller/init(style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcontroller/init%28style%3A%29.json'
content_hash: 'sha256:fab99c2bc0a8791d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewController](../uitableviewcontroller.md)

# init(style:)

<sub>Initializer</sub>

Initializes a table view controller to manage a table view of a given style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(style: UITableView.Style)
```

## Parameters

- `style` — A constant that specifies the style of table view that the controller object is to manage ([UITableViewStylePlain](../uitableview/style-swift.enum/plain.md) or [UITableViewStyleGrouped](../uitableview/style-swift.enum/grouped.md)).

## Return Value

An initialized [UITableViewController](../uitableviewcontroller.md) object.

## Discussion

If you use the standard `init` method to initialize a [UITableViewController](../uitableviewcontroller.md) object, a table view in the plain style is created.

## See Also

### Creating a table view controller

- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a table view controller with the nib file in the specified bundle.
- [- initWithCoder:](<init(coder_).md>) — Creates a table view controller from data in an unarchiver.
