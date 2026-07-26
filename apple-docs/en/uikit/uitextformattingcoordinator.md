---
title: UITextFormattingCoordinator
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextformattingcoordinator
source_url: 'https://developer.apple.com/documentation/uikit/uitextformattingcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextformattingcoordinator.json'
content_hash: 'sha256:92dd4f4ec30ed44c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextFormattingCoordinator

<sub>Class</sub>

An object that coordinates text formatting using the standard Mac font panel.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextFormattingCoordinator
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIFontPickerViewControllerDelegate](uifontpickerviewcontrollerdelegate.md)

## Topics

### Creating a Text-Formatting Coordinator

- [+ textFormattingCoordinatorForWindowScene:](<uitextformattingcoordinator/init(for_).md>) — Creates a text-formatting coordinator for the specified window scene.
- [- initWithWindowScene:](<uitextformattingcoordinator/init(windowscene_).md>) — Initializes and returns a new text-formatting coordinator for the specified window scene.

### Showing the Font Panel

- [fontPanelVisible](uitextformattingcoordinator/isfontpanelvisible.md) — A Boolean value that indicates whether the font panel is visible.
- [+ toggleFontPanel:](<uitextformattingcoordinator/togglefontpanel(__).md>) — Toggles the visibility of the font panel.

### Configuring the Font Panel

- [- setSelectedAttributes:isMultiple:](<uitextformattingcoordinator/setselectedattributes(__ismultiple_).md>) — Configures the initial display state of the font panel with the attributes of the selected text.

### Applying Updated Text Attributes

- [delegate](uitextformattingcoordinator/delegate.md) — The delegate of the text-formatting coordinator.
- [UITextFormattingCoordinatorDelegate](uitextformattingcoordinatordelegate.md) — The methods that delegates of text-formatting coordinators implement to apply font panel settings to the currently selected text.

### Initializers

- [init(forWindowScene:)](<uitextformattingcoordinator/init(forwindowscene_).md>)

## See Also

### Text formatting

- [UITextAttributesConversionHandler](uitextattributesconversionhandler.md) — A handler for updating text with current font panel settings.
