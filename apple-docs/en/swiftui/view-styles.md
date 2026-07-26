---
title: View styles
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-styles
source_url: 'https://developer.apple.com/documentation/swiftui/view-styles'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-styles.json'
content_hash: 'sha256:6ebc98b280f1fd7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# View styles

<sub>API Collection</sub>

Apply built-in and custom appearances and behaviors to different types of views.

## Overview

SwiftUI defines built-in styles for certain kinds of views and automatically selects the appropriate style for a particular presentation context. For example, a [Label](label.md) might appear as an icon, a string title, or both, depending on factors like the platform, whether the view appears in a toolbar, and so on.

![](../../../attachments/7ba769e017aa157b1b47692780e74e9a/view-styles-hero@2x.png)

You can override the automatic style by using one of the style view modifiers. These modifiers typically propagate throughout a container view, so that you can wrap a view hierarchy in a style modifier to affect all the views of the given type within the hierarchy.

Any of the style protocols that define a `makeBody(configuration:)` method, like [ToggleStyle](togglestyle.md), also enable you to define custom styles. Create a type that conforms to the corresponding style protocol and implement its `makeBody(configuration:)` method. Then apply the new style using a style view modifier exactly like a built-in style.

## Topics

### Styling views with Liquid Glass

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md) — Configure, combine, and morph views using Liquid Glass effects.
- [Landmarks: Building an app with Liquid Glass](landmarks-building-an-app-with-liquid-glass.md) — Enhance your app experience with system-provided and custom Liquid Glass.
- [glassEffect(_:in:)](<view/glasseffect(__in_).md>) — Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](<view/glasseffectid(__in_).md>) — Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectTransition(_:)](<view/glasseffecttransition(__).md>) — Associates a glass effect transition with any glass effects defined within this view.
- [glassEffectUnion(id:namespace:)](<view/glasseffectunion(id_namespace_).md>) — Associates any Liquid Glass effects defined within this view to a union with the provided identifier.
- [interactive(_:)](<glass/interactive(__).md>) — Returns a copy of the structure configured to be interactive.
- [GlassEffectContainer](glasseffectcontainer.md) — A view that combines multiple Liquid Glass shapes into a single shape that can morph individual shapes into one another.
- [GlassEffectTransition](glasseffecttransition.md) — A structure that describes changes to apply when a glass effect is added or removed from the view hierarchy.
- [GlassButtonStyle](glassbuttonstyle.md) — A button style that applies glass border artwork based on the button’s context.
- [GlassProminentButtonStyle](glassprominentbuttonstyle.md) — A button style that applies prominent glass border artwork based on the button’s context.
- [DefaultGlassEffectShape](defaultglasseffectshape.md) — The default shape applied by glass effects, a capsule.

### Styling buttons

- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [ButtonStyle](buttonstyle.md) — A type that applies standard interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [ButtonStyleConfiguration](buttonstyleconfiguration.md) — The properties of a button.
- [PrimitiveButtonStyle](primitivebuttonstyle.md) — A type that applies custom interaction behavior and a custom appearance to all buttons within a view hierarchy.
- [PrimitiveButtonStyleConfiguration](primitivebuttonstyleconfiguration.md) — The properties of a button.
- [signInWithAppleButtonStyle(_:)](<view/signinwithapplebuttonstyle(__).md>) — Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [ButtonSizing](buttonsizing.md) — The sizing behavior of `Button`s and other button-like controls.

### Styling pickers

- [pickerStyle(_:)](<view/pickerstyle(__).md>) — Sets the style for pickers within this view.
- [PickerStyle](pickerstyle.md) — A type that specifies the appearance and interaction of all pickers within a view hierarchy.
- [datePickerStyle(_:)](<view/datepickerstyle(__).md>) — Sets the style for date pickers within this view.
- [DatePickerStyle](datepickerstyle.md) — A type that specifies the appearance and interaction of all date pickers within a view hierarchy.

### Styling menus

- [menuStyle(_:)](<view/menustyle(__).md>) — Sets the style for menus within this view.
- [MenuStyle](menustyle.md) — A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.
- [MenuStyleConfiguration](menustyleconfiguration.md) — A configuration of a menu.

### Styling toggles

- [toggleStyle(_:)](<view/togglestyle(__).md>) — Sets the style for toggles in a view hierarchy.
- [ToggleStyle](togglestyle.md) — The appearance and behavior of a toggle.
- [ToggleStyleConfiguration](togglestyleconfiguration.md) — The properties of a toggle instance.

### Styling indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [GaugeStyle](gaugestyle.md) — Defines the implementation of all gauge instances within a view hierarchy.
- [GaugeStyleConfiguration](gaugestyleconfiguration.md) — The properties of a gauge instance.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.
- [ProgressViewStyle](progressviewstyle.md) — A type that applies standard interaction behavior to all progress views within a view hierarchy.
- [ProgressViewStyleConfiguration](progressviewstyleconfiguration.md) — The properties of a progress view instance.

### Styling views that display text

- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.
- [LabelStyle](labelstyle.md) — A type that applies a custom appearance to all labels within a view.
- [LabelStyleConfiguration](labelstyleconfiguration.md) — The properties of a label.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [TextFieldStyle](textfieldstyle.md) — A specification for the appearance and interaction of a text field.
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — Sets the style for text editors within this view.
- [TextEditorStyle](texteditorstyle.md) — A specification for the appearance and interaction of a text editor.
- [TextEditorStyleConfiguration](texteditorstyleconfiguration.md) — The properties of a text editor.

### Styling collection views

- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.
- [ListStyle](liststyle.md) — A protocol that describes the behavior and appearance of a list.
- [tableStyle(_:)](<view/tablestyle(__).md>) — Sets the style for tables within this view.
- [TableStyle](tablestyle.md) — A type that applies a custom appearance to all tables within a view.
- [TableStyleConfiguration](tablestyleconfiguration.md) — The properties of a table.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
- [DisclosureGroupStyle](disclosuregroupstyle.md) — A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.

### Styling navigation views

- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — Sets the style for navigation split views within this view.
- [NavigationSplitViewStyle](navigationsplitviewstyle.md) — A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — Sets the style for the tab view within the current environment.
- [TabViewStyle](tabviewstyle.md) — A specification for the appearance and interaction of a tab view.

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyle](controlgroupstyle.md) — Defines the implementation of all control groups within a view hierarchy.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [IndexViewStyle](indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.

### Styling windows from a view inside the window

- [presentedWindowStyle(_:)](<view/presentedwindowstyle(__).md>) — Sets the style for windows created by interacting with this view.
- [presentedWindowToolbarStyle(_:)](<view/presentedwindowtoolbarstyle(__).md>) — Sets the style for the toolbar in windows created by interacting with this view.

### Adding a glass background on views in visionOS

- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [GlassBackgroundDisplayMode](glassbackgrounddisplaymode.md) — The display mode of a glass background.
- [GlassBackgroundEffect](glassbackgroundeffect.md) — A specification for the appearance of a glass background.
- [AutomaticGlassBackgroundEffect](automaticglassbackgroundeffect.md) — The automatic glass background effect.
- [GlassBackgroundEffectConfiguration](glassbackgroundeffectconfiguration.md) — A configuration used to build a custom effect.
- [FeatheredGlassBackgroundEffect](featheredglassbackgroundeffect.md) — The feathered glass background effect.
- [PlateGlassBackgroundEffect](plateglassbackgroundeffect.md) — The plate glass background effect.

## See Also

### Views

- [View fundamentals](view-fundamentals.md) — Define the visual elements of your app using a hierarchy of views.
- [View configuration](view-configuration.md) — Adjust the characteristics of views in a hierarchy.
- [Animations](animations.md) — Create smooth visual updates in response to state changes.
- [Text input and output](text-input-and-output.md) — Display formatted text and get text input from the user.
- [Images](images.md) — Add images and symbols to your app’s user interface.
- [Controls and indicators](controls-and-indicators.md) — Display values and get user selections.
- [Menus and commands](menus-and-commands.md) — Provide space-efficient, context-dependent access to commands and controls.
- [Shapes](shapes.md) — Trace and fill built-in and custom shapes with a color, gradient, or other pattern.
- [Drawing and graphics](drawing-and-graphics.md) — Enhance your views with graphical effects and customized drawings.
