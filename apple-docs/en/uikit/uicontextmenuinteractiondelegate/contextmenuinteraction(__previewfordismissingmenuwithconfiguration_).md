---
title: 'contextMenuInteraction(_:previewForDismissingMenuWithConfiguration:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（16.0 起废弃）, iPadOS 13.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction(_:previewfordismissingmenuwithconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuinteractiondelegate/contextmenuinteraction%28_%3Apreviewfordismissingmenuwithconfiguration%3A%29.json'
content_hash: 'sha256:bcd613596e2c4adc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuInteractionDelegate](../uicontextmenuinteractiondelegate.md)

# contextMenuInteraction(_:previewForDismissingMenuWithConfiguration:)

<sub>Instance Method</sub>

Returns the destination view to use when animating the appearance of the preview interface.

> [!warning] Deprecated
> Use [- contextMenuInteraction:configuration:dismissalPreviewForItemWithIdentifier:](<contextmenuinteraction(__configuration_dismissalpreviewforitemwithidentifier_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func contextMenuInteraction(_ interaction: UIContextMenuInteraction, previewForDismissingMenuWithConfiguration configuration: UIContextMenuConfiguration) -> UITargetedPreview?
```

## Parameters

- `interaction` — The interaction object that triggered the preview.

- `configuration` — The configuration object associated with the current interaction.

## Return Value

An object containing the destination view and configuration parameters for the animation.

## Discussion

When the user dismisses the preview interface, UIKit animates that interface to the view you specify in the returned [UITargetedPreview](../uitargetedpreview.md) object.

## See Also

### Deprecated

- [- contextMenuInteraction:previewForHighlightingMenuWithConfiguration:](<contextmenuinteraction(__previewforhighlightingmenuwithconfiguration_).md>) — Returns the source view to use when animating the appearance of the preview interface. _(deprecated)_
