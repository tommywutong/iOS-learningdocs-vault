---
title: Appearance modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-appearance
source_url: 'https://developer.apple.com/documentation/swiftui/view-appearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-appearance.json'
content_hash: 'sha256:36f7ec08c414d447'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Appearance modifiers

<sub>API Collection</sub>

Configure a view’s foreground and background styles, controls, and visibility.

## Overview

Use these modifiers to configure the appearance of a view, including the use of color and tint, and the application of overlays and background elements. Control the visibility of a view and specific elements within a view. Manage the shape and size of various controls.

For information about configuring views, see [View configuration](view-configuration.md).

## Topics

### Colors and patterns

- [backgroundStyle(_:)](<view/backgroundstyle(__).md>) — Sets the specified style to render backgrounds within the view.
- [foregroundStyle(_:)](<view/foregroundstyle(__).md>) — Sets a view’s foreground elements to use a given style.
- [foregroundStyle(_:_:)](<view/foregroundstyle(____).md>) — Sets the primary and secondary levels of the foreground style in the child view.
- [foregroundStyle(_:_:_:)](<view/foregroundstyle(______).md>) — Sets the primary, secondary, and tertiary levels of the foreground style.
- [allowedDynamicRange(_:)](<view/alloweddynamicrange(__).md>) — Returns a new view configured with the specified allowed dynamic range.

### Tint

- [tint(_:)](<view/tint(__).md>) — Sets the tint color within this view.
- [listRowSeparatorTint(_:edges:)](<view/listrowseparatortint(__edges_).md>) — Sets the tint color associated with a row.
- [listSectionSeparatorTint(_:edges:)](<view/listsectionseparatortint(__edges_).md>) — Sets the tint color associated with a section.
- [listItemTint(_:)](<view/listitemtint(__).md>) — Sets a fixed tint color for content in a list.

### Light and dark appearance

- [preferredColorScheme(_:)](<view/preferredcolorscheme(__).md>) — Sets the preferred color scheme for this presentation.
- [preferredSurroundingsEffect(_:)](<view/preferredsurroundingseffect(__).md>) — Applies an effect to passthrough video.

### Foreground elements

- [border(_:width:)](<view/border(__width_).md>) — Adds a border to this view with the specified style and width.
- [overlay(alignment:content:)](<view/overlay(alignment_content_).md>) — Layers the views that you specify in front of this view.
- [overlay(_:ignoresSafeAreaEdges:)](<view/overlay(__ignoressafeareaedges_).md>) — Layers the specified style in front of this view.
- [overlay(_:in:fillStyle:)](<view/overlay(__in_fillstyle_).md>) — Layers a shape that you specify in front of this view.
- [spatialOverlay(alignment:content:)](<view/spatialoverlay(alignment_content_).md>) — Adds secondary views within the 3D bounds of this view.
- [spatialOverlayPreferenceValue(_:alignment:_:)](<view/spatialoverlaypreferencevalue(__alignment___).md>) — Uses the specified preference value from the view to produce another view occupying the same 3D space of the first view.

### Background elements

- [background(alignment:content:)](<view/background(alignment_content_).md>) — Layers the views that you specify behind this view.
- [background(_:ignoresSafeAreaEdges:)](<view/background(__ignoressafeareaedges_).md>) — Sets the view’s background to a style.
- [background(ignoresSafeAreaEdges:)](<view/background(ignoressafeareaedges_).md>) — Sets the view’s background to the default background style.
- [background(_:in:fillStyle:)](<view/background(__in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with a style.
- [background(in:fillStyle:)](<view/background(in_fillstyle_).md>) — Sets the view’s background to an insettable shape filled with the default background style.
- [alternatingRowBackgrounds(_:)](<view/alternatingrowbackgrounds(__).md>) — Overrides whether lists and tables in this view have alternating row backgrounds.
- [listRowBackground(_:)](<view/listrowbackground(__).md>) — Places a custom background view behind a list row item.
- [scrollContentBackground(_:)](<view/scrollcontentbackground(__).md>) — Specifies the visibility of the background for scrollable views within this view.
- [containerBackground(_:for:)](<view/containerbackground(__for_).md>) — Sets the container background of the enclosing container using a view.
- [containerBackground(for:alignment:content:)](<view/containerbackground(for_alignment_content_).md>) — Sets the container background of the enclosing container using a view.
- [glassBackgroundEffect(displayMode:)](<view/glassbackgroundeffect(displaymode_).md>) — Fills the view’s background with an automatic glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(_:displayMode:)](<view/glassbackgroundeffect(__displaymode_).md>) — Fills the view’s background with a custom glass background effect and container-relative rounded rectangle shape.
- [glassBackgroundEffect(in:displayMode:)](<view/glassbackgroundeffect(in_displaymode_).md>) — Fills the view’s background with an automatic glass background effect and a shape that you specify.
- [glassBackgroundEffect(_:in:displayMode:)](<view/glassbackgroundeffect(__in_displaymode_).md>) — Fills the view’s background with a custom glass background effect and a shape that you specify.
- [backgroundExtensionEffect()](<view/backgroundextensioneffect().md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.
- [backgroundExtensionEffect(isEnabled:)](<view/backgroundextensioneffect(isenabled_).md>) — Adds the background extension effect to the view. The view will be duplicated into mirrored copies which will be placed around the view on any edge with available safe area. Additionally, a blur effect will be applied on top to blur out the copies.

### Passthrough

- [breakthroughEffect(_:)](<view/breakthrougheffect(__).md>) — Ensures that the view is always visible to the user, even when other content is occluding it, like 3D models.

### Control configuration

- [defaultWheelPickerItemHeight(_:)](<view/defaultwheelpickeritemheight(__).md>) — Sets the default wheel-style picker item height.
- [horizontalRadioGroupLayout()](<view/horizontalradiogrouplayout().md>) — Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [controlSize(_:)](<view/controlsize(__).md>) — Sets the size for controls within this view.
- [buttonBorderShape(_:)](<view/buttonbordershape(__).md>) — Sets the border shape for buttons in this view.
- [buttonRepeatBehavior(_:)](<view/buttonrepeatbehavior(__).md>) — Sets whether buttons in this view should repeatedly trigger their actions on prolonged interactions.
- [headerProminence(_:)](<view/headerprominence(__).md>) — Sets the header prominence for this view.
- [scrollDisabled(_:)](<view/scrolldisabled(__).md>) — Disables or enables scrolling in scrollable views.
- [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) — Configures the bounce behavior of scrollable views along the specified axis.
- [scrollIndicatorsFlash(onAppear:)](<view/scrollindicatorsflash(onappear_).md>) — Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicatorsFlash(trigger:)](<view/scrollindicatorsflash(trigger_).md>) — Flashes the scroll indicators of scrollable views when a value changes.
- [menuOrder(_:)](<view/menuorder(__).md>) — Sets the preferred order of items for menus presented from this view.
- [menuActionDismissBehavior(_:)](<view/menuactiondismissbehavior(__).md>) — Tells a menu whether to dismiss after performing an action.
- [paletteSelectionEffect(_:)](<view/paletteselectioneffect(__).md>) — Specifies the selection effect to apply to a palette item.
- [typeSelectEquivalent(_:)](<view/typeselectequivalent(__).md>) — Sets an explicit type select equivalent text in a collection, such as a list or table.

### Symbol effects

- [symbolEffect(_:options:isActive:)](<view/symboleffect(__options_isactive_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffect(_:options:value:)](<view/symboleffect(__options_value_).md>) — Returns a new view with a symbol effect added to it.
- [symbolEffectsRemoved(_:)](<view/symboleffectsremoved(__).md>) — Returns a new view with its inherited symbol image effects either removed or left unchanged.

### Privacy and redaction

- [privacySensitive(_:)](<view/privacysensitive(__).md>) — Marks the view as containing sensitive, private user data.
- [redacted(reason:)](<view/redacted(reason_).md>) — Adds a reason to apply a redaction to this view hierarchy.
- [unredacted()](<view/unredacted().md>) — Removes any reason to apply a redaction to this view hierarchy.
- [invalidatableContent(_:)](<view/invalidatablecontent(__).md>) — Mark the receiver as their content might be invalidated.
- [contentCaptureProtected(_:)](<view/contentcaptureprotected(__).md>)

### Visibility

- [hidden()](<view/hidden().md>) — Hides this view unconditionally.
- [labelsHidden()](<view/labelshidden().md>) — Hides the labels of any controls contained within this view.
- [labelsVisibility(_:)](<view/labelsvisibility(__).md>) — Controls the visibility of labels of any controls contained within this view.
- [menuIndicator(_:)](<view/menuindicator(__).md>) — Sets the menu indicator visibility for controls within this view.
- [listRowSeparator(_:edges:)](<view/listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
- [listSectionSeparator(_:edges:)](<view/listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.
- [listSectionIndexVisibility(_:)](<view/listsectionindexvisibility(__).md>) — Changes the visibility of the list section index.
- [persistentSystemOverlays(_:)](<view/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.
- [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [scrollClipDisabled(_:)](<view/scrollclipdisabled(__).md>) — Sets whether a scroll view clips its content to its bounds.
- [sliderThumbVisibility(_:)](<view/sliderthumbvisibility(__).md>) — Sets the thumb visibility for `Slider`s within this view.
- [tableColumnHeaders(_:)](<view/tablecolumnheaders(__).md>) — Controls the visibility of a `Table`’s column header views.
- [upperLimbVisibility(_:)](<view/upperlimbvisibility(__).md>) — Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](immersivespace.md) scene is presented.
- [volumeBaseplateVisibility(_:)](<view/volumebaseplatevisibility(__).md>) — Sets the visibility of the baseplate of a volume, which appears when a user looks towards the ‘floor’ of a volume and during resize. Both `automatic` and `visible` will show the baseplate. `hidden` will never show it.

### Sensory feedback

- [sensoryFeedback(_:trigger:)](<view/sensoryfeedback(__trigger_).md>) — Plays the specified `feedback` when the provided `trigger` value changes.
- [sensoryFeedback(trigger:_:)](<view/sensoryfeedback(trigger___).md>) — Plays feedback when returned from the `feedback` closure after the provided `trigger` value changes.
- [sensoryFeedback(_:trigger:condition:)](<view/sensoryfeedback(__trigger_condition_).md>) — Plays the specified `feedback` when the provided `trigger` value changes and the `condition` closure returns `true`.

### Widget configuration

- [widgetAccentable(_:)](<view/widgetaccentable(__).md>) — Adds the view and all of its subviews to the accented group.
- [widgetCurvesContent(_:)](<view/widgetcurvescontent(__).md>) — Displays the widget’s content along a curve if the context allows it.
- [widgetLabel(_:)](<view/widgetlabel(__).md>) — Returns a localized text label that displays additional content outside the accessory family widget’s main SwiftUI view.
- [widgetLabel(label:)](<view/widgetlabel(label_).md>) — Creates a label for displaying additional content outside an accessory family widget’s main SwiftUI view.
- [dynamicIsland(verticalPlacement:)](<view/dynamicisland(verticalplacement_).md>) — Specifies the vertical placement for a view of an expanded Live Activity that appears in the Dynamic Island.
- [accessoryWidgetGroupStyle(_:)](<view/accessorywidgetgroupstyle(__).md>) — The view modifier that can be applied to `AccessoryWidgetGroup` to specify the shape the three content views will be masked with. The value of `style` is set to `.automatic`, which is `.circular` by default.
- [controlWidgetActionHint(_:)](<view/controlwidgetactionhint(__).md>) — The action hint of the control described by the modified label.
- [controlWidgetStatus(_:)](<view/controlwidgetstatus(__).md>) — The status of the control described by the modified label.

### Window behaviors

- [windowDismissBehavior(_:)](<view/windowdismissbehavior(__).md>) — Configures the dismiss functionality for the window enclosing `self`.
- [windowFullScreenBehavior(_:)](<view/windowfullscreenbehavior(__).md>) — Configures the full screen functionality for the window enclosing `self`.
- [windowToolbarFullScreenVisibility(_:)](<view/windowtoolbarfullscreenvisibility(__).md>) — Configures the visibility of the window toolbar when the window enters full screen mode.
- [windowMinimizeBehavior(_:)](<view/windowminimizebehavior(__).md>) — Configures the minimize functionality for the window enclosing `self`.
- [windowResizeAnchor(_:)](<view/windowresizeanchor(__).md>) — Sets the window anchor point used when the size of the view changes such that the window must resize.
- [windowResizeBehavior(_:)](<view/windowresizebehavior(__).md>) — Configures the resize functionality for the window enclosing `self`.
- [preferredWindowClippingMargins(_:_:)](<view/preferredwindowclippingmargins(____).md>) — Requests additional margins for drawing beyond the bounds of the window.

## See Also

### Configuring view elements

- [Accessibility modifiers](view-accessibility.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Text and symbol modifiers](view-text-and-symbols.md) — Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md) — Add and configure supporting views, like toolbars and context menus.
- [Chart view modifiers](view-chart-view.md) — Configure charts that you declare with Swift Charts.
