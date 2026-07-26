---
title: UITableViewCellConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcellconfigurationupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcellconfigurationupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcellconfigurationupdatehandler.json'
content_hash: 'sha256:df08f9857679677d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewCellConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof UITableViewCell *, UICellConfigurationState *) UITableViewCellConfigurationUpdateHandler;
```

## Parameters

- `cell` — The table view cell to configure.

- `state` — The new state to use for updating the cell’s configuration.

## See Also

### Managing the state

- [configurationState](uitableviewcell/configurationstate-5gw4n.md) — The current configuration state of the cell.
- [- setNeedsUpdateConfiguration](<uitableviewcell/setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfigurationUsingState:](uitableviewcell/updateconfigurationusingstate_.md) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uitableviewcell/configurationupdatehandler-746ya.md) — A block for handling updates to the cell’s configuration using the current state.
