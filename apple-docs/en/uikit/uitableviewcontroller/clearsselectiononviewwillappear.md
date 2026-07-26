---
title: clearsSelectionOnViewWillAppear
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcontroller/clearsselectiononviewwillappear
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcontroller/clearsselectiononviewwillappear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcontroller/clearsselectiononviewwillappear.json'
content_hash: 'sha256:ae62aad12a8b541e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewController](../uitableviewcontroller.md)

# clearsSelectionOnViewWillAppear

<sub>Instance Property</sub>

A Boolean value indicating if the controller clears the selection when the table appears.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsSelectionOnViewWillAppear: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md). When [true](../../swift/true.md), the table view controller clears the table’s current selection when it receives a [- viewWillAppear:](<../uiviewcontroller/viewwillappear(__).md>) message. Setting this property to [false](../../swift/false.md) preserves the selection.
