---
title: Style modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-style-modifiers
source_url: 'https://developer.apple.com/documentation/swiftui/view-style-modifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-style-modifiers.json'
content_hash: 'sha256:9d72df49f3e7ec40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Style modifiers

<sub>API Collection</sub>

Apply built-in styles to different types of views.

## Overview

SwiftUI defines built-in styles for certain kinds of views, and chooses the appropriate style for a particular presentation context. For example, a [Label](label.md) might appear as an icon, a string title, or both, depending on factors like the platform, whether the view appears in a toolbar, and so on.

You can override the automatic style by using one of the style modifiers. These modifiers typically propagate through container views, so you can wrap an entire view hierarchy in a style modifier to affect all the views of the given type within the hierarchy. Some view types enable you to create custom styles, which you also apply using style modifiers.

For more information about styling views, see [View styles](view-styles.md).

## Topics

### Liquid Glass

- [glassEffect(_:in:)](<view/glasseffect(__in_).md>) — Applies the Liquid Glass effect to a view.
- [glassEffectID(_:in:)](<view/glasseffectid(__in_).md>) — Associates an identity value to Liquid Glass effects defined within this view.
- [glassEffectTransition(_:)](<view/glasseffecttransition(__).md>) — Associates a glass effect transition with any glass effects defined within this view.
- [glassEffectUnion(id:namespace:)](<view/glasseffectunion(id_namespace_).md>) — Associates any Liquid Glass effects defined within this view to a union with the provided identifier.

### Controls

- [buttonStyle(_:)](<view/buttonstyle(__).md>) — Sets the style for buttons within this view to a button style with a custom appearance and standard interaction behavior.
- [buttonSizing(_:)](<view/buttonsizing(__).md>) — The preferred sizing behavior of buttons in the view hierarchy.
- [datePickerStyle(_:)](<view/datepickerstyle(__).md>) — Sets the style for date pickers within this view.
- [menuStyle(_:)](<view/menustyle(__).md>) — Sets the style for menus within this view.
- [pickerStyle(_:)](<view/pickerstyle(__).md>) — Sets the style for pickers within this view.
- [toggleStyle(_:)](<view/togglestyle(__).md>) — Sets the style for toggles in a view hierarchy.

### Indicators

- [gaugeStyle(_:)](<view/gaugestyle(__).md>) — Sets the style for gauges within this view.
- [progressViewStyle(_:)](<view/progressviewstyle(__).md>) — Sets the style for progress views in this view.

### Text

- [labelStyle(_:)](<view/labelstyle(__).md>) — Sets the style for labels within this view.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [textFieldStyle(_:)](<view/textfieldstyle(__).md>) — Sets the style for text fields within this view.
- [textEditorStyle(_:)](<view/texteditorstyle(__).md>) — Sets the style for text editors within this view.

### Collections

- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.
- [tableStyle(_:)](<view/tablestyle(__).md>) — Sets the style for tables within this view.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.

### Presentation

- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — Sets the style for navigation split views within this view.
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — Sets the style for the tab view within the current environment.
- [presentedWindowStyle(_:)](<view/presentedwindowstyle(__).md>) — Sets the style for windows created by interacting with this view.
- [presentedWindowToolbarStyle(_:)](<view/presentedwindowtoolbarstyle(__).md>) — Sets the style for the toolbar in windows created by interacting with this view.

### Groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.

## See Also

### Drawing views

- [Layout modifiers](view-layout.md) — Tell a view how to arrange itself within a view hierarchy by adjusting its size, position, alignment, padding, and so on.
- [Graphics and rendering modifiers](view-graphics-and-rendering.md) — Affect the way the system draws a view, for example by scaling or masking a view, or by applying graphical effects.
