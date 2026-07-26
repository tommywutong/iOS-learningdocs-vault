---
title: UITableViewHeaderFooterViewConfigurationUpdateHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterviewconfigurationupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterviewconfigurationupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterviewconfigurationupdatehandler.json'
content_hash: 'sha256:95f54ef41a9a16df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewHeaderFooterViewConfigurationUpdateHandler

<sub>Type Alias</sub>

The type of block for handling updates to the view’s configuration using the current state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(__kindof UITableViewHeaderFooterView *, UIViewConfigurationState *) UITableViewHeaderFooterViewConfigurationUpdateHandler;
```

## Parameters

- `cell` — The header footer view to configure.

- `state` — The new state to use for updating the header footer view’s configuration.

## See Also

### Managing the state

- [configurationState](uitableviewheaderfooterview/configurationstate-9l60r.md) — The current configuration state of the view.
- [- setNeedsUpdateConfiguration](<uitableviewheaderfooterview/setneedsupdateconfiguration().md>) — Informs the view to update its configuration for its current state.
- [updateConfigurationUsingState:](uitableviewheaderfooterview/updateconfigurationusingstate_.md) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-3oji2.md) — A block for handling updates to the view’s configuration using the current state.
