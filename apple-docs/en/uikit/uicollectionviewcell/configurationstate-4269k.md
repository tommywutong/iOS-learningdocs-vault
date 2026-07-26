---
title: configurationState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcell/configurationstate-4269k
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/configurationstate-4269k'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/configurationstate-4269k.json'
content_hash: 'sha256:f7998c1d1a8e37ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# configurationState

<sub>Instance Property</sub>

The current configuration state of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) UICellConfigurationState * configurationState;
```

## Discussion

To add your own custom state, see [UIConfigurationStateCustomKey](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state

- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfigurationUsingState:](updateconfigurationusingstate_.md) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-ajhn.md) — A block for handling updates to the cell’s configuration using the current state.
- [UICollectionViewCellConfigurationUpdateHandler](../uicollectionviewcellconfigurationupdatehandler.md) — The type of block for handling updates to the cell’s configuration using the current state.
- [selected](isselected.md) — The selection state of the cell.
- [highlighted](ishighlighted.md) — The highlight state of the cell.
