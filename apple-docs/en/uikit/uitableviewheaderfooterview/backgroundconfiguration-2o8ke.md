---
title: backgroundConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-2o8ke
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-2o8ke'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/backgroundconfiguration-2o8ke.json'
content_hash: 'sha256:03ea2e195dff903a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# backgroundConfiguration

<sub>Instance Property</sub>

The current background configuration of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nullable) UIBackgroundConfiguration * backgroundConfiguration;
```

## Discussion

Using a background configuration, you can obtain system default background styling for a variety of different view states. Create a background configuration with one of the default system styles, customize the configuration to match your view’s style as necessary, and assign the configuration to this property.

```objc
UIBackgroundConfiguration *backgroundConfig = [UIBackgroundConfiguration listPlainHeaderFooterConfiguration];
[backgroundConfig setBackgroundColor: [UIColor systemGrayColor]];
[header setBackgroundConfiguration: backgroundConfig];
```

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets the following APIs to `nil`:

- [backgroundColor](../uiview/backgroundcolor.md)
- [backgroundView](backgroundview.md)

## See Also

### Configuring the background

- [defaultBackgroundConfiguration](defaultbackgroundconfiguration.md) — Retrieves a background configuration with system default values.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [backgroundView](backgroundview.md) — The background view of the header or footer.
