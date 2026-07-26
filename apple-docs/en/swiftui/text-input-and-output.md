---
title: Text input and output
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text-input-and-output
source_url: 'https://developer.apple.com/documentation/swiftui/text-input-and-output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text-input-and-output.json'
content_hash: 'sha256:6b3e742e69789cfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Text input and output

<sub>API Collection</sub>

Display formatted text and get text input from the user.

## Overview

To display read-only text, or read-only text paired with an image, use the built-in [Text](text.md) or [Label](label.md) views, respectively. When you need to collect text input from the user, use an appropriate text input view, like [TextField](textfield.md) or [TextEditor](texteditor.md).

![](../../../attachments/a8d0f352ff6dabd1c3d1e3fdfb577250/text-input-and-output-hero@2x.png)

You add view modifiers to control the text’s font, selectability, alignment, layout direction, and so on. These modifiers also affect other views that display text, like the labels on controls, even if you don’t define an explicit [Text](text.md) view.

For design guidance, see [Typography](../design/human-interface-guidelines/typography.md) in the Human Interface Guidelines.

## Topics

### Displaying text

- [Text](text.md) — A view that displays one or more lines of read-only text.
- [Label](label.md) — A standard label for user interface items, consisting of an icon with a title.
- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.

### Getting text input

- [Building rich SwiftUI text experiences](building-rich-swiftui-text-experiences.md) — Build an editor for formatted text using SwiftUI text editor views and attributed strings.
- [TextField](textfield.md) — A control that displays an editable text interface.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [SecureField](securefield.md) — A control into which people securely enter private text.
- [TextEditor](texteditor.md) — A view that can display and edit long-form text.

### Selecting text

- [textSelection(_:)](<view/textselection(__).md>) — Controls whether people can select text within this view.
- [TextSelectability](textselectability.md) — A type that describes the ability to select text.
- [TextSelection](textselection.md) — Represents a selection of text.
- [textSelectionAffinity(_:)](<view/textselectionaffinity(__).md>) — Sets the direction of a selection or cursor relative to a text character.
- [textSelectionAffinity](environmentvalues/textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [TextSelectionAffinity](textselectionaffinity.md) — A representation of the direction or association of a selection or cursor relative to a text character. This concept becomes much more prominent when dealing with bidirectional text (text that contains both LTR and RTL scripts, like English and Arabic combined).
- [AttributedTextSelection](attributedtextselection.md) — Represents a selection of attributed text.

### Setting a font

- [Applying custom fonts to text](applying-custom-fonts-to-text.md) — Add and use a font in your app that scales with Dynamic Type.
- [font(_:)](<view/font(__).md>) — Sets the default font for text in this view.
- [fontDesign(_:)](<view/fontdesign(__).md>) — Sets the font design of the text in this view.
- [fontWeight(_:)](<view/fontweight(__).md>) — Sets the font weight of the text in this view.
- [fontWidth(_:)](<view/fontwidth(__).md>) — Sets the font width of the text in this view.
- [font](environmentvalues/font.md) — The default font of this environment.
- [Font](font.md) — An environment-dependent font.

### Adjusting text size

- [textScale(_:isEnabled:)](<view/textscale(__isenabled_).md>) — Applies a text scale to text in the view.
- [dynamicTypeSize(_:)](<view/dynamictypesize(__).md>) — Sets the Dynamic Type size within the view to the given value.
- [dynamicTypeSize](environmentvalues/dynamictypesize.md) — The current Dynamic Type size.
- [DynamicTypeSize](dynamictypesize.md) — A Dynamic Type size, which specifies how large scalable content should be.
- [ScaledMetric](scaledmetric.md) — A dynamic property that scales a numeric value.
- [TextVariantPreference](textvariantpreference.md) — A protocol for controlling the size variant of text views.
- [FixedTextVariant](fixedtextvariant.md) — The default text variant preference that chooses the largest available variant.
- [SizeDependentTextVariant](sizedependenttextvariant.md) — The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.

### Controlling text style

- [bold(_:)](<view/bold(__).md>) — Applies a bold font weight to the text in this view.
- [italic(_:)](<view/italic(__).md>) — Applies italics to the text in this view.
- [underline(_:pattern:color:)](<view/underline(__pattern_color_).md>) — Applies an underline to the text in this view.
- [strikethrough(_:pattern:color:)](<view/strikethrough(__pattern_color_).md>) — Applies a strikethrough to the text in this view.
- [textCase(_:)](<view/textcase(__).md>) — Sets a transform for the case of the text contained in this view when displayed.
- [textCase](environmentvalues/textcase.md) — A stylistic override to transform the case of `Text` when displayed, using the environment’s locale.
- [monospaced(_:)](<view/monospaced(__).md>) — Modifies the fonts of all child views to use the fixed-width variant of the current font, if possible.
- [monospacedDigit()](<view/monospaceddigit().md>) — Modifies the fonts of all child views to use fixed-width digits, if possible, while leaving other characters proportionally spaced.
- [AttributedTextFormattingDefinition](attributedtextformattingdefinition.md) — A protocol for defining how text can be styled in a view.
- [AttributedTextValueConstraint](attributedtextvalueconstraint.md) — A protocol for defining a constraint on the value of a certain attribute.
- [AttributedTextFormatting](attributedtextformatting.md) — A namespace for types related to attributed text formatting definitions.

### Managing text layout

- [truncationMode(_:)](<view/truncationmode(__).md>) — Sets the truncation mode for lines of text that are too long to fit in the available space.
- [truncationMode](environmentvalues/truncationmode.md) — A value that indicates how the layout truncates the last line of text to fit into the available space.
- [allowsTightening(_:)](<view/allowstightening(__).md>) — Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [allowsTightening](environmentvalues/allowstightening.md) — A Boolean value that indicates whether inter-character spacing should tighten to fit the text into the available space.
- [minimumScaleFactor(_:)](<view/minimumscalefactor(__).md>) — Sets the minimum amount that text in this view scales down to fit in the available space.
- [minimumScaleFactor](environmentvalues/minimumscalefactor.md) — The minimum permissible proportion to shrink the font size to fit the text into the available space.
- [baselineOffset(_:)](<view/baselineoffset(__).md>) — Sets the vertical offset for the text relative to its baseline in this view.
- [kerning(_:)](<view/kerning(__).md>) — Sets the spacing, or kerning, between characters for the text in this view.
- [tracking(_:)](<view/tracking(__).md>) — Sets the tracking for the text in this view.
- [flipsForRightToLeftLayoutDirection(_:)](<view/flipsforrighttoleftlayoutdirection(__).md>) — Sets whether this view mirrors its contents horizontally when the layout direction is right-to-left.
- [TextAlignment](textalignment.md) — An alignment position for text along the horizontal axis.

### Rendering text

- [Creating visual effects with SwiftUI](creating-visual-effects-with-swiftui.md) — Add scroll effects, rich color treatments, custom transitions, and advanced effects using shaders and a text renderer.
- [TextAttribute](textattribute.md) — A value that you can attach to text views and that text renderers can query.
- [textRenderer(_:)](<view/textrenderer(__).md>) — Returns a new view such that any text views within it will use `renderer` to draw themselves.
- [TextRenderer](textrenderer.md) — A value that can replace the default text view rendering behavior.
- [TextProxy](textproxy.md) — A proxy for a text view that custom text renderers use.

### Limiting line count for multiline text

- [lineLimit(_:)](<view/linelimit(__).md>) — Sets to a closed range the number of lines that text can occupy in this view.
- [lineLimit(_:reservesSpace:)](<view/linelimit(__reservesspace_).md>) — Sets a limit for the number of lines text can occupy in this view.
- [lineLimit](environmentvalues/linelimit.md) — The maximum number of lines that text can occupy in a view.

### Formatting multiline text

- [lineSpacing(_:)](<view/linespacing(__).md>) — Sets the amount of space between lines of text in this view.
- [lineSpacing](environmentvalues/linespacing.md) — The distance in points between the bottom of one line fragment and the top of the next.
- [multilineTextAlignment(_:)](<view/multilinetextalignment(__).md>) — Sets the alignment of a text view that contains multiple lines of text.
- [multilineTextAlignment](environmentvalues/multilinetextalignment.md) — An environment value that indicates how a text view aligns its lines when the content wraps or contains newlines.

### Formatting date and time

- [SystemFormatStyle](systemformatstyle.md) — A collection of format styles for displaying live-updating time information in text views.
- [TimeDataSource](timedatasource.md) — A source of time related data.

### Managing text entry

- [autocorrectionDisabled(_:)](<view/autocorrectiondisabled(__).md>) — Sets whether to disable autocorrection for this view.
- [autocorrectionDisabled](environmentvalues/autocorrectiondisabled.md) — A Boolean value that determines whether the view hierarchy has auto-correction enabled.
- [keyboardType(_:)](<view/keyboardtype(__).md>) — Sets the keyboard type for this view.
- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [textContentType(_:)](<view/textcontenttype(__).md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textInputAutocapitalization(_:)](<view/textinputautocapitalization(__).md>) — Sets how often the shift key in the keyboard is automatically enabled.
- [TextInputAutocapitalization](textinputautocapitalization.md) — The kind of autocapitalization behavior applied during text input.
- [textInputBorderShape(_:)](<view/textinputbordershape(__).md>) — Sets the border shape for text input controls in the view hierarchy. _(beta)_
- [TextInputBorderShape](textinputbordershape.md) — A shape used to draw the border of a text input control. _(beta)_
- [textInputCompletion(_:)](<view/textinputcompletion(__).md>) — Associates a fully formed string with the value of this view when used as a text input suggestion
- [textInputSuggestions(_:)](<view/textinputsuggestions(__).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:content:)](<view/textinputsuggestions(__content_).md>) — Configures the text input suggestions for this view.
- [textInputSuggestions(_:id:content:)](<view/textinputsuggestions(__id_content_).md>) — Configures the text input suggestions for this view.
- [textContentType(_:)](<view/textcontenttype(__)-4dqqb.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on a watchOS device.
- [textContentType(_:)](<view/textcontenttype(__)-6fic1.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on macOS.
- [textContentType(_:)](<view/textcontenttype(__)-ufdv.md>) — Sets the text content type for this view, which the system uses to offer suggestions while the user enters text on an iOS or tvOS device.
- [textInputFormattingControlVisibility(_:for:)](<view/textinputformattingcontrolvisibility(__for_).md>) — Specifies which system text formatting controls are available for people to format text.
- [TextInputFormattingControlPlacement](textinputformattingcontrolplacement.md) — A structure defining the system text formatting controls available on each platform.

### Dictating text

- [searchDictationBehavior(_:)](<view/searchdictationbehavior(__).md>) — Configures the dictation behavior for any search fields configured by the searchable modifier.
- [TextInputDictationActivation](textinputdictationactivation.md)
- [TextInputDictationBehavior](textinputdictationbehavior.md)

### Configuring the Writing Tools behavior

- [writingToolsBehavior(_:)](<view/writingtoolsbehavior(__).md>) — Specifies the Writing Tools behavior for text and text input in the environment.
- [WritingToolsBehavior](writingtoolsbehavior.md) — The Writing Tools editing experience for text and text input.
- [writingToolsAffordanceVisibility(_:)](<view/writingtoolsaffordancevisibility(__).md>) — Specifies whether the system should show the Writing Tools affordance for text input views affected by the environment.

### Specifying text equivalents

- [typeSelectEquivalent(_:)](<view/typeselectequivalent(__).md>) — Sets an explicit type select equivalent text in a collection, such as a list or table.

### Localizing text

- [Preparing views for localization](preparing-views-for-localization.md) — Specify hints and add strings to localize your SwiftUI views.
- [LocalizedStringKey](localizedstringkey.md) — The key used to look up an entry in a strings file or strings dictionary file.
- [locale](environmentvalues/locale.md) — The current locale that views should use.
- [typesettingLanguage(_:isEnabled:)](<view/typesettinglanguage(__isenabled_).md>) — Specifies the language for typesetting.
- [TypesettingLanguage](typesettinglanguage.md) — Defines how typesetting language is determined for text.

### Deprecated types

- [ContentSizeCategory](contentsizecategory.md) — The sizes that you can specify for content. _(deprecated)_

## See Also

### Views

- [View fundamentals](view-fundamentals.md) — Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md) — Adjust the characteristics of views in a hierarchy.
- [View styles](view-styles.md) — Apply built-in and custom appearances and behaviors to different types of views.
- [Animations](animations.md) — Create smooth visual updates in response to state changes.
- [Images](images.md) — Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md) — Display values and get user selections.
- [Menus and commands](menus-and-commands.md) — Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md) — Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md) — Enhance your views with graphical effects and customized drawings.
