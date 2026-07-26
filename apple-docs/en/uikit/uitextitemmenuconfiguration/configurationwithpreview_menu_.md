---
title: 'configurationWithPreview:menu:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextitemmenuconfiguration/configurationwithpreview:menu:'
source_url: 'https://developer.apple.com/documentation/uikit/uitextitemmenuconfiguration/configurationwithpreview:menu:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextitemmenuconfiguration/configurationwithpreview%3Amenu%3A.json'
content_hash: 'sha256:f280f9ae448288b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [MenuConfiguration](../uitextitem/menuconfiguration.md)

# configurationWithPreview:menu:

<sub>Type Method</sub>

Creates a menu configuration with the specified menu and custom preview.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) configurationWithPreview:(UITextItemMenuPreview *) preview menu:(UIMenu *) menu;
```

## Parameters

- `preview` — The preview associated with the menu. Specify @c nil for no preview.

- `menu` — The menu to be presented.

## See Also

### Creating a menu configuration

- [configurationWithMenu:](configurationwithmenu_.md) — Creates a menu configuration with the specified menu and a default preview.
- [UITextItemMenuPreview](../uitextitemmenupreview.md) — An object representing the preview for a text item.
