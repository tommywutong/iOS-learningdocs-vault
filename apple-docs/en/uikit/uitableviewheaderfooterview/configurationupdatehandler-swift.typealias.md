---
title: UITableViewHeaderFooterView.ConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-swift.typealias
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/configurationupdatehandler-swift.typealias.json'
content_hash: 'sha256:d6909d33446707e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# UITableViewHeaderFooterView.ConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the view’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias ConfigurationUpdateHandler = (UITableViewHeaderFooterView, UIViewConfigurationState) -> Void
```

## Parameters

- `headerFooterView` — The header footer view to configure.

- `state` — The new state to use for updating the header footer view’s configuration.

## See Also

### Managing the state

- [configurationState](configurationstate-7xj7r.md) — The current configuration state of the view.
- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the view to update its configuration for its current state.
- [updateConfiguration(using:)](<updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.
