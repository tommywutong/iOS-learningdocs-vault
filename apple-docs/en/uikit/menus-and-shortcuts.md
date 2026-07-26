---
title: Menus and shortcuts
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/menus-and-shortcuts
source_url: 'https://developer.apple.com/documentation/uikit/menus-and-shortcuts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/menus-and-shortcuts.json'
content_hash: 'sha256:1dc15b08c0d24e48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# Menus and shortcuts

<sub>API Collection</sub>

Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.

## Topics

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](uimenuelement.md) — An object representing a menu, action, or command.
- [UIAction](uiaction.md) — A menu element that performs its action in a closure.
- [UICommand](uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.

### Edit menus

- [UIEditMenuInteraction](uieditmenuinteraction.md) — An interaction that provides edit operations using a menu.
- [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) — The methods for customizing the menu the interaction displays.
- [UIEditMenuConfiguration](uieditmenuconfiguration.md) — An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — A set of standard methods that apps can adopt to support editing.

### App menus

- [UIMenu](uimenu.md) — A container for grouping related menu elements in an app menu or contextual menu.
- [UIMenuBuilder](uimenubuilder.md) — An interface for adding and removing menus from a menu system.
- [UIMenuSystem](uimenusystem.md) — An object representing a main or contextual menu system.
- [UIMainMenuSystem](uimainmenusystem.md) — The main menu system.

### Contextual menus

- [UIContextMenuSystem](uicontextmenusystem.md) — The context menu system.
- [UIContextMenuInteraction](uicontextmenuinteraction.md) — An interaction object that you use to display relevant actions for your content.
- [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md) — The methods for providing the set of actions to perform on your content, and for customizing the preview of that content.
- [UITargetedPreview](uitargetedpreview.md) — An object describing the view to use during preview-related animations.
- [UIPreviewTarget](uipreviewtarget.md) — An object that specifies the container view to use for animations.
- [UIPreviewParameters](uipreviewparameters.md) — Additional parameters to use when animating a preview interface.

### Find and replace

- [UIFindInteraction](uifindinteraction.md) — An interaction that provides text finding and replacing operations using a system find panel.
- [UIFindInteractionDelegate](uifindinteractiondelegate.md) — A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [UIFindSession](uifindsession.md) — An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [UITextSearchingFindSession](uitextsearchingfindsession.md) — A find session object that wraps a searchable object implementing the text-searching protocol.
- [UITextSearching](uitextsearching-3wkjv.md) — The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [UITextSearchOptions](uitextsearchoptions.md) — An object containing the configurable options for a text search.
- [UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md) — Constants that describe the style a find session uses to decorate the text.
- [WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md) — Constants that describe the method to use when searching text for words that match a string.
- [SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md) — Constants that describe the results summary the find panel UI includes.

### Home Screen quick actions

- [Add Home Screen quick actions](add-home-screen-quick-actions.md) — Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.
- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.
- [UIApplicationShortcutIcon](uiapplicationshortcuticon.md) — An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.
- [UIMutableApplicationShortcutItem](uimutableapplicationshortcutitem.md) — A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.

## See Also

### User interactions

- [Touches, presses, and gestures](touches-presses-and-gestures.md) — Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Drag and drop](drag-and-drop.md) — Bring drag and drop to your app by using interaction APIs with your views.
- [Pointer interactions](pointer-interactions.md) — Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](apple-pencil-interactions.md) — Handle user interactions like double tap and squeeze on Apple Pencil.
- [Focus-based navigation](focus-based-navigation.md) — Navigate the interface of your UIKit app using a remote, game controller, or keyboard.
- [Accessibility for UIKit](accessibility-for-uikit.md) — Make your UIKit apps accessible to everyone who uses iOS and tvOS.
