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
doc_path: /documentation/uikit/uitableviewheaderfooterview/configurationstate-9l60r
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/configurationstate-9l60r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/configurationstate-9l60r.json'
content_hash: 'sha256:67ca98cf4e293983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# configurationState

<sub>Instance Property</sub>

The current configuration state of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) UIViewConfigurationState * configurationState;
```

## Discussion

To add your own custom state, see [UIConfigurationStateCustomKey](../uiconfigurationstatecustomkey.md).

## See Also

### Managing the state

- [- setNeedsUpdateConfiguration](<setneedsupdateconfiguration().md>) — Informs the view to update its configuration for its current state.
- [updateConfigurationUsingState:](updateconfigurationusingstate_.md) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](configurationupdatehandler-3oji2.md) — A block for handling updates to the view’s configuration using the current state.
- [UITableViewHeaderFooterViewConfigurationUpdateHandler](../uitableviewheaderfooterviewconfigurationupdatehandler.md) — The type of block for handling updates to the view’s configuration using the current state.
