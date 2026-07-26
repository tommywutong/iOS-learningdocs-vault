---
title: backgroundView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/backgroundview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/backgroundview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/backgroundview.json'
content_hash: 'sha256:1da65b0ecda9f76d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# backgroundView

<sub>Instance Property</sub>

The background view of the header or footer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundView: UIView? { get set }
```

## Discussion

The view in this property appears behind the view in the [contentView](contentview.md) property and displays static background content behind the header or footer. For example, you might assign an image view to this property and use it to display a custom background image.

A background configuration is mutually exclusive with background views, so you must use one approach or the other. Setting a non-`nil` value for this property resets [backgroundConfiguration](backgroundconfiguration-52wng.md) to `nil`.

## See Also

### Configuring the background

- [defaultBackgroundConfiguration()](<defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](backgroundconfiguration-52wng.md) — The current background configuration of the view.
- [automaticallyUpdatesBackgroundConfiguration](automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
