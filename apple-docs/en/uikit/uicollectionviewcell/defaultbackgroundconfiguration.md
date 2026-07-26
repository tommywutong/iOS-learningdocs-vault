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
doc_path: /documentation/uikit/uicollectionviewcell/defaultbackgroundconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcell/defaultbackgroundconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcell/defaultbackgroundconfiguration.json'
content_hash: 'sha256:31a67dd1bdc57396'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewCell](../uicollectionviewcell.md)

# defaultBackgroundConfiguration

<sub>Instance Method</sub>

Retrieves a background configuration with system default values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIBackgroundConfiguration *) defaultBackgroundConfiguration;
```

## Return Value

A default background configuration. The system determines default values for the configuration according to the section where the cell appears.

## See Also

### Configuring the background

- [backgroundConfiguration](backgroundconfiguration-39dc0.md) — The current background configuration of the cell.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the cell automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The view that displays behind the cell’s other content.
- [selectedBackgroundView](selectedbackgroundview.md) — The view that displays just above the background view for a selected cell.
