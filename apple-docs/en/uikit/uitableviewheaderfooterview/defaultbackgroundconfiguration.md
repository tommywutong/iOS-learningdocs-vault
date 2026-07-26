---
title: defaultBackgroundConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/defaultbackgroundconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/defaultbackgroundconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/defaultbackgroundconfiguration.json'
content_hash: 'sha256:8eacfee4d5917a31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# defaultBackgroundConfiguration

<sub>Instance Method</sub>

Retrieves a background configuration with system default values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIBackgroundConfiguration *) defaultBackgroundConfiguration;
```

## Return Value

A default background configuration. The system determines default values for the configuration according to the section where the view appears.

## See Also

### Configuring the background

- [backgroundConfiguration](backgroundconfiguration-2o8ke.md) — The current background configuration of the view.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The background view of the header or footer.
