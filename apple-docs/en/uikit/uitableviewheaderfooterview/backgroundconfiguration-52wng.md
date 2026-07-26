---
title: backgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-52wng
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-52wng'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-52wng.json'
content_hash: 'sha256:8cb39dd24752df32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# backgroundConfiguration

<sub>Instance Property</sub>

The current background configuration of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var backgroundConfiguration: UIBackgroundConfiguration? { get set }
```

## Discussion

Using a background configuration, you can obtain system default background styling for a variety of different view states. Create a background configuration with one of the default system styles, customize the configuration to match your view’s style as necessary, and assign the configuration to this property.

```swift
var backgroundConfig = UIBackgroundConfiguration.listPlainHeaderFooter()
backgroundConfig.backgroundColor = .systemGray
header.backgroundConfiguration = backgroundConfig
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [backgroundColor](../uiview/backgroundcolor.md)
- [backgroundView](backgroundview.md)

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The background view of the header or footer.
