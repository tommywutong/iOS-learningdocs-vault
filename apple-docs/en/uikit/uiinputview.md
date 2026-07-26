---
title: UIInputView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputview
source_url: 'https://developer.apple.com/documentation/uikit/uiinputview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputview.json'
content_hash: 'sha256:82fc4c11eac0441a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInputView

<sub>Class</sub>

An object that displays and manages custom input for a view when that view becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIInputView
```

## Overview

The [UIInputView](uiinputview.md) class is designed to match the appearance of the standard system keyboard when used as an input view with a responder. When defining your own custom input views or input accessory views, you can use a [UIInputView](uiinputview.md) object as the root view and add any subviews you want to create your input view. The input view and its subviews receive tinting and blur effects based on the options you specify at initialization time.

> [!note] Note
> The effects offered by this class are applied only when the view is attached to a responder as either an input view or input accessory view. For subviews to receive style effects, they must conform to the [UIAppearance](uiappearance.md) protocol.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Initializing an input view

- [- initWithFrame:inputViewStyle:](<uiinputview/init(frame_inputviewstyle_).md>) — Initializes and returns an input view using the specified style information.
- [- initWithCoder:](<uiinputview/init(coder_).md>) — Creates an input view from data in an unarchiver.

### Getting the input style

- [inputViewStyle](uiinputview/inputviewstyle.md) — The style for the content of the view.
- [Style](uiinputview/style.md) — Constants that indicate the appearance changes for an input view.

### Sizing the input view

- [allowsSelfSizing](uiinputview/allowsselfsizing.md) — A Boolean value that indicates whether the input view is responsible for its own size.

## See Also

### Custom keyboards

- [Creating a custom keyboard](creating-a-custom-keyboard.md) — Add an extension to your Xcode project to provide systemwide customized text input.
- [UIInputViewController](uiinputviewcontroller.md) — The primary view controller for a custom keyboard app extension.
- [UILexicon](uilexicon.md) — A read-only array of term pairs, each in a lexicon entry object, for a custom keyboard.
- [UILexiconEntry](uilexiconentry.md) — A read-only term pair, available within a lexicon object, for a custom keyboard.
- [UITextDocumentProxy](uitextdocumentproxy.md) — An object that provides textual context to a custom keyboard.
