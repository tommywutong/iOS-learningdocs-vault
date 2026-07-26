---
title: UICollectionViewCellConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcellconfigurationupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcellconfigurationupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcellconfigurationupdatehandler.json'
content_hash: 'sha256:ea4143b5b066b5ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewCellConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof UICollectionViewCell *, UICellConfigurationState *) UICollectionViewCellConfigurationUpdateHandler;
```

## Parameters

- `cell` — The collection view cell to configure.

- `state` — The new state to use for updating the cell’s configuration.

## See Also

### Managing the state

- [configurationState](uicollectionviewcell/configurationstate-4269k.md) — The current configuration state of the cell.
- [- setNeedsUpdateConfiguration](<uicollectionviewcell/setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfigurationUsingState:](uicollectionviewcell/updateconfigurationusingstate_.md) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-ajhn.md) — A block for handling updates to the cell’s configuration using the current state.
- [selected](uicollectionviewcell/isselected.md) — The selection state of the cell.
- [highlighted](uicollectionviewcell/ishighlighted.md) — The highlight state of the cell.
