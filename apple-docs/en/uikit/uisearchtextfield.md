---
title: UISearchTextField
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield.json'
content_hash: 'sha256:675e6e7a933eb11d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchTextField

<sub>Class</sub>

A view for displaying and editing text and search tokens.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UISearchTextField
```

## Overview

Use a search text field to display search criteria represented as text and tokens, and allow the user to edit that criteria. Tokens are discrete representations of nontextual content that your app can create and use to represent filters that limit the search results. Tokens always occur contiguously before any text in the search field.

[UISearchBar](uisearchbar.md) hosts a search text field, but you may also use a search text field in other roles, such as the title view of a [UINavigationItem](uinavigationitem.md).

> [!note] Note
> The search field assigns text positions ([UITextPosition](uitextposition.md)) to tokens as well as text so that users can interact with tokens using selection gestures and keyboard input. If the current selection includes any tokens, [selectedTextRange](uitextinput/selectedtextrange.md) includes their positions. Use the search field’s [textualRange](uisearchtextfield/textualrange.md) property to access the range of just the text without the tokens.

Tokens can be programmatically selected by including their position in a range assigned to the [selectedTextRange](uitextinput/selectedtextrange.md) property.

## Relationships

- **Inherits From**: [UITextField](uitextfield.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md), [UIContextMenuInteractionDelegate](uicontextmenuinteractiondelegate.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UIKeyInput](uikeyinput.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UILetterformAwareAdjusting](uiletterformawareadjusting.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITextDraggable](uitextdraggable.md), [UITextDroppable](uitextdroppable.md), [UITextInput](uitextinput.md), [UITextInputTraits](uitextinputtraits.md), [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Converting text into tokens

- [- replaceTextualPortionOfRange:withToken:atIndex:](<uisearchtextfield/replacetextualportion(of_with_at_).md>) — Converts text in a search field into a search token.
- [textualRange](uisearchtextfield/textualrange.md) — The range of the field’s text content.

### Supporting token interactions

- [allowsDeletingTokens](uisearchtextfield/allowsdeletingtokens.md) — A Boolean that indicates whether the user can remove tokens from the search field.
- [allowsCopyingTokens](uisearchtextfield/allowscopyingtokens.md) — A Boolean that indicates whether the user can copy or drag tokens from the search field.
- [delegate](uitextfield/delegate.md) — The text field’s delegate.
- [UISearchTextFieldDelegate](uisearchtextfielddelegate.md) — The interface for the delegate of a search field.
- [UISearchTextFieldPasteItem](uisearchtextfieldpasteitem.md) — A protocol that supports pasting tokens.

### Adding and removing tokens

- [tokens](uisearchtextfield/tokens.md) — The collection of tokens in the search text field.
- [- insertToken:atIndex:](<uisearchtextfield/inserttoken(__at_).md>) — Adds a search token at a specific index.
- [- removeTokenAtIndex:](<uisearchtextfield/removetoken(at_).md>) — Removes a particular search token from the search text field.

### Customizing token behavior

- [tokenBackgroundColor](uisearchtextfield/tokenbackgroundcolor.md) — The background color for all tokens in the search text field.
- [- tokensInRange:](<uisearchtextfield/tokens(in_).md>) — Returns the search field’s tokens that are within a given range.
- [- positionOfTokenAtIndex:](<uisearchtextfield/positionoftoken(at_).md>) — Converts a token index into a text position.

### Providing search suggestions

- [searchSuggestions](uisearchtextfield/searchsuggestions.md) — A list of suggestions to offer as shortcuts below the search field.

## See Also

### Search field

- [UISearchToken](uisearchtoken.md) — Search criteria in a search text field, represented by text and an optional icon.
- [UISearchTextFieldDelegate](uisearchtextfielddelegate.md) — The interface for the delegate of a search field.
