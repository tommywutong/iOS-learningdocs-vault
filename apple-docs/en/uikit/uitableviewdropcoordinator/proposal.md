---
title: proposal
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewdropcoordinator/proposal
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewdropcoordinator/proposal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewdropcoordinator/proposal.json'
content_hash: 'sha256:92a6aa055d0b2860'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewDropCoordinator](../uitableviewdropcoordinator.md)

# proposal

<sub>Instance Property</sub>

The proposal for how to incorporate the dropped items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var proposal: UITableViewDropProposal { get }
```

## Discussion

If your drag delegate implements the [- tableView:dropSessionDidUpdate:withDestinationIndexPath:](<../uitableviewdropdelegate/tableview(__dropsessiondidupdate_withdestinationindexpath_).md>) method, this object contains the information that you provided when making your drop proposal for the given location.

## See Also

### Getting the session information

- [session](session.md) — The drop session containing information about the transaction.
