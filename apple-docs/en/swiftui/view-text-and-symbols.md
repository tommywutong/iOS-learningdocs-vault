---
title: Text and symbol modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-text-and-symbols
source_url: 'https://developer.apple.com/documentation/swiftui/view-text-and-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-text-and-symbols.json'
content_hash: 'sha256:381642903e94b2a9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Text and symbol modifiers

<sub>API Collection</sub>

Manage the rendering, selection, and entry of text in your view.

## Overview

SwiftUI provides built-in views that display text to the user, like [Text](text.md) and [Label](label.md), or that collect text from the user, like [TextField](textfield.md) and [TextEditor](texteditor.md). Use text and symbol modifiers to control how SwiftUI displays and manages that text. For example, you can set a font, specify text layout parameters, and indicate what kind of input to expect.

To learn more about the kinds of views that you use to display text and the ways in which you can configure those views, see [Text input and output](text-input-and-output.md).

## Topics

### Fonts

- [font(_:)](<view/font(__).md>) — Sets the default font for text in this view.

### Dynamic type

- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.

### Text style

- [bold(_:)](<view/bold(__).md>) — Applies a bold font weight to the text in this view.
- [fontDesign(_:)](<view/fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWeight(_:)](<view/fontweight(__).md>) — Sets the font weight of the text in this view.
- [fontWidth(_:)](<view/fontwidth(__).md>) — Sets the font width of the text in this view.
- [italic(_:)](<view/italic(__).md>) — Applies italics to the text in this view.
- [monospaced(_:)](<view/monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<view/monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<view/textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [textRenderer(_:)](<view/textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — Applies an underline to the text in this view.
- [attributedTextFormattingDefinition(_:)](<view/attributedtextformattingdefinition(__).md>) — Apply a text formatting definition to nested views.

### Label configuration

- [labelIconToTitleSpacing(_:)](<view/labelicontotitlespacing(__).md>) — Set the spacing between the icon and title in labels.
- [labelReservedIconWidth(_:)](<view/labelreservediconwidth(__).md>) — Set the width reserved for icons in labels.

### Text layout

- [allowsTightening(_:)](<view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [baselineOffset(_:)](<view/baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<view/flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [kerning(_:)](<view/kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [lineHeight(_:)](<view/lineheight(__).md>) — A modifier for the default line height in the view hierarchy.
- [minimumScaleFactor(_:)](<view/minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [tracking(_:)](<view/tracking(__).md>) — Sets the tracking for the text in this view.
- [truncationMode(_:)](<view/truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) — Specifies the language for typesetting.
- [writingDirection(strategy:)](<view/writingdirection(strategy_).md>) — A modifier for the default text writing direction strategy in the view hierarchy.

### Multiline text

- [lineLimit(_:)](<view/linelimit(__).md>) — Sets to a closed range the number of lines that text can occupy in this view.
- [lineLimit(_:reservesSpace:)](<view/linelimit(__reservesspace_).md>) — Sets a limit for the number of lines text can occupy in this view.
- [lineSpacing(_:)](<view/linespacing(__).md>) — Sets the amount of space between lines of text in this view.
- [multilineTextAlignment(_:)](<view/multilinetextalignment(__).md>) — Sets the alignment of a text view that contains multiple lines of text.
- [multilineTextAlignment(strategy:)](<view/multilinetextalignment(strategy_).md>) — A modifier for the default text alignment strategy in the view hierarchy.

### Text selection

- [textSelection(_:)](<view/textselection(__).md>) — Controls whether people can select text within this view.
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.

### Data detection

- [dataDetection(_:options:)](<view/datadetection(__options_).md>) — Asynchronously detects data in the view’s content and styles them to indicate they are clickable. _(beta)_

### Text entry

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [keyboardType(_:)](<view/keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — Sets how often the shift key in the keyboard is automatically enabled.
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<view/textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [textInputFormattingControlVisibility(_:for:)](<view/textinputformattingcontrolvisibility(__for_).md>) — Specifies which system text formatting controls are available for people to format text.

### Find and replace

- [findNavigator(isPresented:)](<view/findnavigator(ispresented_).md>) — Programmatically presents the find and replace interface for text editor views.
- [findDisabled(_:)](<view/finddisabled(__).md>) — Prevents find and replace operations in a text editor.
- [replaceDisabled(_:)](<view/replacedisabled(__).md>) — Prevents replace operations in a text editor.

### Symbol appearance

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolColorRenderingMode(_:)](<view/symbolcolorrenderingmode(__).md>) — Sets the color rendering mode for symbol images.
- [symbolVariableValueMode(_:)](<view/symbolvariablevaluemode(__).md>) — Sets the variable value mode mode for symbol images within this view.
- [symbolVariant(_:)](<view/symbolvariant(__).md>) — Makes symbols within the view show a particular variant.

### Writing Tools

- [writingToolsAffordanceVisibility(_:)](<view/writingtoolsaffordancevisibility(__).md>) — Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.
- [writingToolsBehavior(_:)](<view/writingtoolsbehavior(__).md>) — Specifies the Writing Tools behavior for text and text input in the environment.
- [WritingToolsBehavior](writingtoolsbehavior.md) — The Writing Tools editing experience for text and text input.

## See Also

### Configuring view elements

- [Accessibility modifiers](view-accessibility.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md) — Configure a view’s foreground and background styles, controls, and visibility.
- [Auxiliary view modifiers](view-auxiliary-views.md) — Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md) — Configure charts that you declare with Swift Charts.
