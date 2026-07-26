---
title: UITextView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview
source_url: 'https://developer.apple.com/documentation/uikit/uitextview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview.json'
content_hash: 'sha256:e925c4a2291b3747'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextView

<sub>Class</sub>

A scrollable, multiline text region.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITextView
```

## Overview

A text view displays multiple lines of text and supports editing, custom styles, and rich formatting. Use it when you need to display or edit a body of text, such as the contents of a document.

For rich text, set the [attributedText](uitextview/attributedtext.md) property to provide per-range style information. You can also use [font](uitextview/font.md), [textColor](uitextview/textcolor.md), and [textAlignment](uitextview/textalignment.md) to apply a single style across all text in the view.

### Manage the keyboard

When someone taps in an editable text view, it becomes the first responder and the system displays the keyboard. Because the keyboard can obscure parts of your interface, reposition any views that would otherwise be hidden. Some system views, like table views, scroll the first responder into view automatically. If the first responder is at the bottom of the scrolling region, you may still need to resize or reposition the scroll view to keep it visible.

Your app is responsible for dismissing the keyboard. Dismiss it in response to a user action, such as tapping a Done button. To dismiss the keyboard, call [- resignFirstResponder](<uiresponder/resignfirstresponder().md>) on the text view that’s currently the first responder. This ends the editing session and hides the keyboard, with your delegate’s consent.

To customize the keyboard, use the properties from the [UITextInputTraits](uitextinputtraits.md) protocol, which text views implement. You can set the keyboard type (ASCII, Numbers, URL, Email, and others) and configure text entry behavior like autocapitalization and autocorrection.

### Keyboard notifications

When the system shows or hides the keyboard, it posts notifications that include the keyboard’s size and position. Register for these notifications to reposition or resize views as needed:

- [UIKeyboardWillShowNotification](uiresponder/keyboardwillshownotification.md)
- [UIKeyboardDidShowNotification](uiresponder/keyboarddidshownotification.md)
- [UIKeyboardWillHideNotification](uiresponder/keyboardwillhidenotification.md)
- [UIKeyboardDidHideNotification](uiresponder/keyboarddidhidenotification.md)

For more information about these notifications, see [UIWindow](uiwindow.md).

### State preservation

If you assign a value to this view’s [restorationIdentifier](uiview/restorationidentifier.md) property, the view preserves the following information:

- The selected range of text.
- The editing state of the text view, as reported by the [editable](uitextview/iseditable.md) property.

On the next launch, the view restores these properties. If the saved selection range doesn’t apply to the current text, no text is selected.

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/components/content/text-views/).

## Relationships

- **Inherits From**: [UIScrollView](uiscrollview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTextViewportLayoutControllerDelegate](nstextviewportlayoutcontrollerdelegate.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentSizeCategoryAdjusting](uicontentsizecategoryadjusting.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFindInteractionDelegate](uifindinteractiondelegate.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md), [UIKeyInput](uikeyinput.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UILetterformAwareAdjusting](uiletterformawareadjusting.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITextDraggable](uitextdraggable.md), [UITextDroppable](uitextdroppable.md), [UITextInput](uitextinput.md), [UITextInputTraits](uitextinputtraits.md), [UITextPasteConfigurationSupporting](uitextpasteconfigurationsupporting.md), [UITextSearching](uitextsearching-3wkjv.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Initializing the text view

- [- initWithFrame:textContainer:](<uitextview/init(frame_textcontainer_).md>) — Creates a new text view with the specified text container.
- [+ textViewUsingTextLayoutManager:](<uitextview/init(usingtextlayoutmanager_).md>) — Creates a new text view, with or without a text layout manager depending on the Boolean value you specify.
- [- initWithCoder:](<uitextview/init(coder_).md>) — Creates a text view from data in an unarchiver.

### Specifying the text content

- [text](uitextview/text.md) — The text that the text view displays.
- [attributedText](uitextview/attributedtext.md) — The styled text that the text view displays.

### Responding to text view changes

- [delegate](uitextview/delegate.md) — The text view’s delegate.
- [UITextViewDelegate](uitextviewdelegate.md) — The methods for receiving editing-related messages for text view objects.

### Configuring appearance attributes

- [font](uitextview/font.md) — The font of the text.
- [textColor](uitextview/textcolor.md) — The color of the text.
- [textAlignment](uitextview/textalignment.md) — The technique for aligning the text.
- [typingAttributes](uitextview/typingattributes.md) — The attributes to apply to new text that the user enters.
- [linkTextAttributes](uitextview/linktextattributes.md) — The attributes to apply to links.
- [borderStyle](uitextview/borderstyle-swift.property.md) — The border style for the text field.
- [textHighlightAttributes](uitextview/texthighlightattributes.md)
- [- drawTextHighlightBackgroundForTextRange:origin:](<uitextview/drawtexthighlightbackground(for_origin_).md>)
- [BorderStyle](uitextview/borderstyle-swift.enum.md) — The type of border around the text view.

### Configuring layout attributes

- [textContainerInset](uitextview/textcontainerinset.md) — The inset of the text container’s layout area within the text view’s content area.
- [usesStandardTextScaling](uitextview/usesstandardtextscaling.md) — A Boolean value that determines the rendering scale of the text.
- [sizingRule](uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.

### Formatting special data in text

- [dataDetectorTypes](uitextview/datadetectortypes.md) — The types of data that convert to tappable URLs in the text view.
- [UIDataDetectorTypes](uidatadetectortypes.md) — Constants that define the types of information to detect in text-based content.

### Managing the editing behavior

- [editable](uitextview/iseditable.md) — A Boolean value that indicates whether the text view is editable.
- [allowsEditingTextAttributes](uitextview/allowseditingtextattributes.md) — A Boolean value that indicates whether the text view allows the user to edit style information.
- [UITextViewTextDidBeginEditingNotification](uitextview/textdidbegineditingnotification.md) — A notification that alerts observers when an editing session begins in a text view.
- [UITextViewTextDidChangeNotification](uitextview/textdidchangenotification.md) — A notification that alerts observers when the text in a text view changes.
- [UITextViewTextDidEndEditingNotification](uitextview/textdidendeditingnotification.md) — A notification that alerts observers when the editing session ends for a text view.

### Working with the selection

- [selectedRange](uitextview/selectedrange.md) — The current selection range of the text view. _(deprecated)_
- [- scrollRangeToVisible:](<uitextview/scrollrangetovisible(__).md>) — Scrolls the text view until the text in the specified range is visible.
- [clearsOnInsertion](uitextview/clearsoninsertion.md) — A Boolean value that indicates whether inserting text replaces the previous contents.
- [selectable](uitextview/isselectable.md) — A Boolean value that indicates whether the text view is selectable.

### Replacing the system input views

- [inputView](uitextview/inputview.md) — The custom input view to display when the text view becomes the first responder.
- [inputAccessoryView](uitextview/inputaccessoryview.md) — The custom accessory view to display when the text view becomes the first responder.

### Supporting Find and Replace

- [findInteractionEnabled](uitextview/isfindinteractionenabled.md) — A Boolean value that enables a text view’s built-in find interaction.
- [findInteraction](uitextview/findinteraction.md) — The text view’s built-in find interaction.

### Getting the Writing Tools configuration

- [writingToolsBehavior](uitextview/writingtoolsbehavior.md) — The level of Writing Tools support to use in the text view.
- [allowedWritingToolsResultOptions](uitextview/allowedwritingtoolsresultoptions.md) — The type of content Writing Tools generates for your text view.
- [writingToolsActive](uitextview/iswritingtoolsactive.md) — A Boolean value that indicates whether the writing tools are currently interacting with the text view’s content.
- [writingToolsCoordinator](uitextview/writingtoolscoordinator.md) — The object that coordinates interactions between Writing Tools and the text view.
- [subclassForWritingToolsCoordinator](uitextview/subclassforwritingtoolscoordinator.md)

### Accessing TextKit Objects

- [textLayoutManager](uitextview/textlayoutmanager.md) — The text layout manager that lays out text for the text view’s text container.
- [layoutManager](uitextview/layoutmanager.md) — The layout manager that lays out text for the text view’s text container.
- [textContainer](uitextview/textcontainer.md) — The text container object that defines the area where text displays in the text view.
- [textStorage](uitextview/textstorage.md) — The text storage object holding the text that displays in the text view.

### Customizing viewport layout

- [- viewportBoundsForTextViewportLayoutController:](<uitextview/viewportbounds(for_).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls to request the current viewport, which is the view visible bounds plus the overdraw area. Requires a call to super. _(beta)_
- [- textViewportLayoutControllerWillLayout:](<uitextview/textviewportlayoutcontrollerwilllayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller starts its layout process. Requires a call to super. _(beta)_
- [- textViewportLayoutControllerDidLayout:](<uitextview/textviewportlayoutcontrollerdidlayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller finishes its layout process. Requires a call to super. _(beta)_
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<uitextview/textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller receives a `setNeedsLayout` call. Requires a call to super. _(beta)_

### Managing attachment view reuse

- [- registerTextAttachmentViewProviderReusePolicy:forTextAttachmentViewProviderType:](<uitextview/register(__fortextattachmentviewprovidertype_).md>) — Register the UITextAttachmentViewProviderReusePolicy for all instances of a particular subclass of NSTextAttachmentViewProvider. _(beta)_
- [UITextAttachmentViewProviderReusePolicy](uitextattachmentviewproviderreusepolicy.md) — An option set that controls whether a text view reuses attachment view providers when scrolling or editing.

### Supporting state restoration

- [interactionState](uitextview/interactionstate.md)

### Structures

- [TextDidBeginEditingMessage](uitextview/textdidbegineditingmessage.md)
- [TextDidChangeMessage](uitextview/textdidchangemessage.md)
- [TextDidEndEditingMessage](uitextview/textdidendeditingmessage.md)

### Instance Properties

- [selectedRanges](uitextview/selectedranges-70g3h.md)
- [textFormattingConfiguration](uitextview/textformattingconfiguration.md) — For text views that have flag `allowsEditingTextAttributes` set, this configuration will be used for `UITextFormattingViewController` when its presentation is requested.

### Instance Methods

- [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<uitextview/textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the layout controller lays out a text layout fragment in the UI. Requires a call to super. _(beta)_

## See Also

### Text views

- [UILabel](uilabel.md) — A view that displays one or more lines of informational text.
- [UITextField](uitextfield.md) — An object that displays an editable text area in your interface.
- [Drag and drop customization](drag-and-drop-customization.md) — Extend the standard drag and drop support for text views to include custom types of content.
