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
doc_path: /documentation/uikit/uitableviewheaderfooterview/configurationstate-7xj7r
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationstate-7xj7r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/configurationstate-7xj7r.json'
content_hash: 'sha256:e33df247724e710b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# configurationState

<sub>Instance Property</sub>

The current configuration state of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @objc(_bridgedConfigurationState) @preconcurrency dynamic var configurationState: UIViewConfigurationState { get }
```

## Discussion

To add your own custom state, see [UIConfigurationStateCustomKey](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state

- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the view to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.
- [ConfigurationUpdateHandler](configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the view’s configuration using the current state.
