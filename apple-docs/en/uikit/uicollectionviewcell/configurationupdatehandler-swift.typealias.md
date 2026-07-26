---
title: UICollectionViewCell.ConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/configurationupdatehandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationupdatehandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/configurationupdatehandler-swift.typealias.json'
content_hash: 'sha256:22208ad0fee26b1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# UICollectionViewCell.ConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias ConfigurationUpdateHandler = (UICollectionViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell` — The collection view cell to configure.

- `state` — The new state to use for updating the cell’s configuration.

## See Also

### Managing the state

- [configurationState](configurationstate-4u37h.md) — The current configuration state of the cell.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-7rqbu.md) — A block for handling updates to the cell’s configuration using the current state.
- [selected](isselected.md) — The selection state of the cell.
- [highlighted](ishighlighted.md) — The highlight state of the cell.
