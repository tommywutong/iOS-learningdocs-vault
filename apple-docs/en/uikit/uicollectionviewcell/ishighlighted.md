---
title: isHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/ishighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/ishighlighted.json'
content_hash: 'sha256:30f4b3562bb07127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# isHighlighted

<sub>Instance Property</sub>

The highlight state of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

This property manages the highlight state of the cell only. The default value of this property is [false](../../swift/false.md), which indicates that the cell isn’t in a highlighted state.

You typically don’t set the value of this property directly. Instead, the preferred way to select the cell and highlight it’s to use the selection methods of the collection view object.

## See Also

### Managing the state

- [configurationState](configurationstate-4u37h.md) — The current configuration state of the cell.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-7rqbu.md) — A block for handling updates to the cell’s configuration using the current state.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the cell’s configuration using the current state.
- [selected](isselected.md) — The selection state of the cell.
