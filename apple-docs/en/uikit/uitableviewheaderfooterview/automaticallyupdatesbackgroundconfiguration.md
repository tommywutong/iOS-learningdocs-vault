---
title: automaticallyUpdatesBackgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration.json'
content_hash: 'sha256:2954312e455d5cb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# automaticallyUpdatesBackgroundConfiguration

<sub>Instance Property</sub>

A Boolean value that determines whether the view automatically updates its background configuration when its state changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var automaticallyUpdatesBackgroundConfiguration: Bool { get set }
```

## Discussion

When this value is [true](../../swift/true.md), the cell automatically calls `updated(for:)` on its [backgroundConfiguration](backgroundconfiguration-52wng.md) when the view’s [configurationState](configurationstate-7xj7r.md) changes, and applies the updated configuration back to the view. The default value is [true](../../swift/true.md).

If you override [updateConfiguration(using:)](<updateconfiguration(using_).md>) to manually update and customize the background configuration, disable automatic updates by setting this property to [false](../../swift/false.md).

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-52wng.md) — The current background configuration of the view.
- [backgroundView](backgroundview.md) — The background view of the header or footer.
