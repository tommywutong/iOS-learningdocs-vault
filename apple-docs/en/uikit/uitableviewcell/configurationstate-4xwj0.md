---
title: configurationState
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewcell/configurationstate-4xwj0
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewcell/configurationstate-4xwj0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewcell/configurationstate-4xwj0.json'
content_hash: 'sha256:fb9b7ca278fbce26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewCell](../uitableviewcell.md)

# configurationState

<sub>Instance Property</sub>

The current configuration state of the cell.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UICellConfigurationState { get }
```

## Discussion

To add your own custom state, see [UIConfigurationStateCustomKey](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state

- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the cell to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-974.md) — A block for handling updates to the cell’s configuration using the current state.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the cell’s configuration using the current state.
