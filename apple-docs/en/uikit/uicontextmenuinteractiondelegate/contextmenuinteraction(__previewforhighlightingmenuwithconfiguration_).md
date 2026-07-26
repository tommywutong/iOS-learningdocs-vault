---
title: 'contextMenuInteraction(_:previewForHighlightingMenuWithConfiguration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewforhighlightingmenuwithconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Apreviewforhighlightingmenuwithconfiguration%3A%29.json'
content_hash: 'sha256:645de65955c3cffe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:previewForHighlightingMenuWithConfiguration:)

<sub>Instance Method</sub>

Returns the source view to use when animating the appearance of the preview interface.

> [!warning] Deprecated
> Use [- contextMenuInteraction:configuration:highlightPreviewForItemWithIdentifier:](<contextmenuinteraction(__configuration_highlightpreviewforitemwithidentifier_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, previewForHighlightingMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

## Parameters

- `interaction` — The interaction object that triggered the preview.

- `configuration` — The configuration object associated with the current interaction.

## Return Value

An object containing the source view and configuration parameters for the animation.

## Discussion

UIKit calls this method before an interaction begins, to give you an opportunity to supply a custom source view for the presentation animations. If you didn’t provide a preview handler block in the `configuration` data, UIKit displays the specified view in the preview interface.

## See Also

### Deprecated

- [- contextMenuInteraction:previewForDismissingMenuWithConfiguration:](<contextmenuinteraction(__previewfordismissingmenuwithconfiguration_).md>) — Returns the destination view to use when animating the appearance of the preview interface. _(deprecated)_
