---
title: Scroll views
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scroll-views
source_url: 'https://developer.apple.com/documentation/swiftui/scroll-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scroll-views.json'
content_hash: 'sha256:baad9b7528489a95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Scroll views

<sub>API Collection</sub>

Enable people to scroll to content that doesn’t fit in the current display.

## Overview

When the content of a view doesn’t fit in the display, you can wrap the view in a [ScrollView](scrollview.md) to enable people to scroll on one or more axes. Configure the scroll view using view modifiers. For example, you can set the visibility of the scroll indicators or the availability of scrolling in a given dimension.

![](../../../attachments/fc9311e17b13443bf22043d6155e0e7f/scroll-views-hero@2x.png)

You can put any view type in a scroll view, but you most often use a scroll view for a layout container with too many elements to fit in the display. For some container views that you put in a scroll view, like lazy stacks, the container doesn’t load views until they are visible or almost visible. For others, like regular stacks and grids, the container loads the content all at once, regardless of the state of scrolling.

[Lists](lists.md) and [Tables](tables.md) implicitly include a scroll view, so you don’t need to add scrolling to those container types. However, you can configure their implicit scroll views with the same view modifiers that apply to explicit scroll views.

For design guidance, see [Scroll views](../design/human-interface-guidelines/scroll-views.md) in the Human Interface Guidelines.

## Topics

### Creating a scroll view

- [ScrollView](scrollview.md) — A scrollable view.
- [ScrollViewReader](scrollviewreader.md) — A view that provides programmatic scrolling, by working with a proxy to scroll to known child views.
- [ScrollViewProxy](scrollviewproxy.md) — A proxy value that supports programmatic scrolling of the scrollable views within a view hierarchy.

### Managing scroll position

- [scrollPosition(_:anchor:)](<view/scrollposition(__anchor_).md>) — Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](<view/defaultscrollanchor(__).md>) — Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [defaultScrollAnchor(_:for:)](<view/defaultscrollanchor(__for_).md>) — Associates an anchor to control the position of a scroll view in a particular circumstance.
- [ScrollAnchorRole](scrollanchorrole.md) — A type defining the role of a scroll anchor.
- [ScrollPosition](scrollposition.md) — A type that defines the semantic position of where a scroll view is scrolled within its content.

### Defining scroll targets

- [scrollTargetBehavior(_:)](<view/scrolltargetbehavior(__).md>) — Sets the scroll behavior of views scrollable in the provided axes.
- [scrollTargetLayout(isEnabled:)](<view/scrolltargetlayout(isenabled_).md>) — Configures the outermost layout as a scroll target layout.
- [ScrollTarget](scrolltarget.md) — A type defining the target in which a scroll view should try and scroll to.
- [ScrollTargetBehavior](scrolltargetbehavior.md) — A type that defines the scroll behavior of a scrollable view.
- [ScrollTargetBehaviorContext](scrolltargetbehaviorcontext.md) — The context in which a scroll target behavior updates its scroll target.
- [PagingScrollTargetBehavior](pagingscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to container-based geometry.
- [ViewAlignedScrollTargetBehavior](viewalignedscrolltargetbehavior.md) — The scroll behavior that aligns scroll targets to view-based geometry.
- [AnyScrollTargetBehavior](anyscrolltargetbehavior.md) — A type-erased scroll target behavior.
- [ScrollTargetBehaviorProperties](scrolltargetbehaviorproperties.md) — Properties influencing the scroll view a scroll target behavior applies to.
- [ScrollTargetBehaviorPropertiesContext](scrolltargetbehaviorpropertiescontext.md) — The context in which a scroll target behavior can decide its properties.

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionPhase](scrolltransitionphase.md) — The phases that a view transitions between when it scrolls among other views.
- [ScrollTransitionConfiguration](scrolltransitionconfiguration.md) — The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhase](scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.

### Showing scroll indicators

- [scrollIndicatorsFlash(onAppear:)](<view/scrollindicatorsflash(onappear_).md>) — Flashes the scroll indicators of a scrollable view when it appears.
- [scrollIndicatorsFlash(trigger:)](<view/scrollindicatorsflash(trigger_).md>) — Flashes the scroll indicators of scrollable views when a value changes.
- [scrollIndicators(_:axes:)](<view/scrollindicators(__axes_).md>) — Sets the visibility of scroll indicators within this view.
- [horizontalScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md) — The visibility to apply to scroll indicators of any horizontally scrollable content.
- [verticalScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md) — The visiblity to apply to scroll indicators of any vertically scrollable content.
- [ScrollIndicatorVisibility](scrollindicatorvisibility.md) — The visibility of scroll indicators of a UI element.

### Managing content visibility

- [scrollContentBackground(_:)](<view/scrollcontentbackground(__).md>) — Specifies the visibility of the background for scrollable views within this view.
- [scrollClipDisabled(_:)](<view/scrollclipdisabled(__).md>) — Sets whether a scroll view clips its content to its bounds.
- [ScrollContentOffsetAdjustmentBehavior](scrollcontentoffsetadjustmentbehavior.md) — A type that defines the different kinds of content offset adjusting behaviors a scroll view can have.

### Disabling scrolling

- [scrollDisabled(_:)](<view/scrolldisabled(__).md>) — Disables or enables scrolling in scrollable views.
- [isScrollEnabled](environmentvalues/isscrollenabled.md) — A Boolean value that indicates whether any scroll views associated with this environment allow scrolling to occur.

### Configuring scroll bounce behavior

- [scrollBounceBehavior(_:axes:)](<view/scrollbouncebehavior(__axes_).md>) — Configures the bounce behavior of scrollable views along the specified axis.
- [horizontalScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md) — The scroll bounce mode for the horizontal axis of scrollable views.
- [verticalScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md) — The scroll bounce mode for the vertical axis of scrollable views.
- [ScrollBounceBehavior](scrollbouncebehavior.md) — The ways that a scrollable view can bounce when it reaches the end of its content.

### Configuring scroll edge effects

- [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) — Configures the scroll edge effect style for scroll views within this hierarchy.
- [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) — Hides any scroll edge effects for scroll views within this hierarchy.
- [ScrollEdgeEffectStyle](scrolledgeeffectstyle.md) — A structure that specifies blur transitions between scrolling content and an area with controls, such as toolbars.
- [safeAreaBar(edge:alignment:spacing:content:)](<view/safeareabar(edge_alignment_spacing_content_).md>) — Shows the specified content as a custom bar beside the modified view.

### Interacting with a software keyboard

- [scrollDismissesKeyboard(_:)](<view/scrolldismisseskeyboard(__).md>) — Configures the behavior in which scrollable content interacts with the software keyboard.
- [scrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md) — The way that scrollable content interacts with the software keyboard.
- [ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode.md) — The ways that scrollable content can interact with the software keyboard.

### Managing scrolling for different inputs

- [scrollInputBehavior(_:for:)](<view/scrollinputbehavior(__for_).md>) — Enables or disables scrolling in scrollable views when using particular inputs.
- [ScrollInputKind](scrollinputkind.md) — Inputs used to scroll views.
- [ScrollInputBehavior](scrollinputbehavior.md) — A type that defines whether input should scroll a view.

## See Also

### View layout

- [Layout fundamentals](layout-fundamentals.md) — Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md) — Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md) — Place views in custom arrangements and create animated transitions between layout types.
- [Lists](lists.md) — Display a structured, scrollable column of information.
- [Tables](tables.md) — Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md) — Present views in different kinds of purpose-driven containers, like forms or control groups.
