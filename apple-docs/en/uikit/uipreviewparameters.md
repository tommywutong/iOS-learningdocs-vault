---
title: UIPreviewParameters
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipreviewparameters
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewparameters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewparameters.json'
content_hash: 'sha256:304c6dbcd7c2f6bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPreviewParameters

<sub>Class</sub>

Additional parameters to use when animating a preview interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIPreviewParameters
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIDragPreviewParameters](uidragpreviewparameters.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating preview parameters

- [- init](<uipreviewparameters/init().md>) — Creates a default set of preview parameters.
- [- initWithTextLineRects:](<uipreviewparameters/init(textlinerects_).md>) — Creates a preview parameters object with information about the text you want to preview.

### Configuring the preview attributes

- [backgroundColor](uipreviewparameters/backgroundcolor.md) — The background color to display behind the preview.
- [visiblePath](uipreviewparameters/visiblepath.md) — The portion of the view to show in the preview.
- [shadowPath](uipreviewparameters/shadowpath.md) — The path to use for drawing the preview’s shadow.

## See Also

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — An interaction object that you use to display relevant actions for your content.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [UITargetedPreview](uitargetedpreview.md) — An object describing the view to use during preview-related animations.
- [UIPreviewTarget](uipreviewtarget.md) — An object that specifies the container view to use for animations.
