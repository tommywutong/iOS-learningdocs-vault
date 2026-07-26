---
title: 'configurationWithIdentifier:previewProvider:actionProvider:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontextmenuconfiguration/configurationwithidentifier:previewprovider:actionprovider:'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/configurationwithidentifier:previewprovider:actionprovider:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/configurationwithidentifier%3Apreviewprovider%3Aactionprovider%3A.json'
content_hash: 'sha256:147712572a2877f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# configurationWithIdentifier:previewProvider:actionProvider:

<sub>Type Method</sub>

Creates a menu configuration object with the specified action and preview providers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) configurationWithIdentifier:(id<NSCopying>) identifier previewProvider:(UIContextMenuContentPreviewProvider) previewProvider actionProvider:(UIContextMenuActionProvider) actionProvider;
```

## Parameters

- `identifier` — A unique identifier for the menu configuration object. If you want this method to generate a unique identifier for you, specify `nil`.

- `previewProvider` — An optional block that returns the custom view controller that you use to preview content. If you specify `nil`, UIKit uses a default preview view controller.

- `actionProvider` — An optional block that provides a contextual menu to display with the preview. If you specify `nil`, UIKit doesn’t display a contextual menu with the previewed content.

## Return Value

A new menu configuration object with the specified provider blocks.

## See Also

### Creating the menu configuration object

- [UIContextMenuContentPreviewProvider](../uicontextmenucontentpreviewprovider.md) — Returns the custom view controller to use when previewing your content.
- [UIContextMenuActionProvider](../uicontextmenuactionprovider.md) — Returns an action-based contextual menu, optionally incorporating the system-suggested actions.
