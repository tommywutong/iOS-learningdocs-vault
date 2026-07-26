---
title: UITableViewCell.ConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/configurationupdatehandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/configurationupdatehandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/configurationupdatehandler-swift.typealias.json'
content_hash: 'sha256:92d6292b515c0379'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# UITableViewCell.ConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the cell’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias ConfigurationUpdateHandler = (UITableViewCell, UICellConfigurationState) -> Void
```

## Parameters

- `cell` — The table view cell to configure.

- `state` — The new state to use for updating the cell’s configuration.

## See Also

### Managing the state

- [configurationState](configurationstate-4xwj0.md) — The current configuration state of the cell.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-974.md) — A block for handling updates to the cell’s configuration using the current state.
