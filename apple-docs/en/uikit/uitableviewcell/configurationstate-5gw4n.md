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
doc_path: /documentation/uikit/uitableviewcell/configurationstate-5gw4n
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/configurationstate-5gw4n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/configurationstate-5gw4n.json'
content_hash: 'sha256:153b348e538aeec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

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
- [configurationUpdateHandler](configurationupdatehandler-746ya.md) — A block for handling updates to the cell’s configuration using the current state.
- [UITableViewCellConfigurationUpdateHandler](../uitableviewcellconfigurationupdatehandler.md) — The type of block for handling updates to the cell’s configuration using the current state.
