---
title: cellUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewplaceholder/cellupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewplaceholder/cellupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewplaceholder/cellupdatehandler.json'
content_hash: 'sha256:0efc444efb3d6826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewPlaceholder](../uitableviewplaceholder.md)

# cellUpdateHandler

<sub>Instance Property</sub>

The block that updates the contents of the placeholder cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var cellUpdateHandler: ((UITableViewCell) -> Void)? { get set }
```

## Discussion

Specify a block that configures or updates the appearance of your placeholder cell. The table view calls this block when the placeholder cell becomes visible, and at other appropriate times.
