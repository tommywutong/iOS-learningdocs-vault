---
title: defaultContentConfiguration
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview/defaultcontentconfiguration
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview/defaultcontentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview/defaultcontentconfiguration.json'
content_hash: 'sha256:2ac4a5f50e7a185c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITableViewHeaderFooterView](../uitableviewheaderfooterview.md)

# defaultContentConfiguration

<sub>Instance Method</sub>

Retrieves a default list content configuration for the view’s style.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UIListContentConfiguration *) defaultContentConfiguration;
```

## Return Value

A default list content configuration. The system determines default values for the configuration according to the section where the view appears.

## Discussion

The default content configuration has preconfigured default styling, but doesn’t contain any content. After you get the default configuration, you assign your content to it, customize any other properties, and assign it to the view as the current [contentConfiguration](contentconfiguration-r49e.md).

## See Also

### Managing the content

- [contentConfiguration](contentconfiguration-r49e.md) — The current content configuration of the view.
- [automaticallyUpdatesContentConfiguration](automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [contentView](contentview.md) — The content view of the header or footer.
