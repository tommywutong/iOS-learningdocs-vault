---
title: Lists
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/lists
source_url: 'https://developer.apple.com/documentation/swiftui/lists'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/lists.json'
content_hash: 'sha256:b5828ee8d4ec7cee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Lists

<sub>API Collection</sub>

Display a structured, scrollable column of information.

## Overview

Use a list to display a one-dimensional vertical collection of views.

![](../../../attachments/15c88d97bce9de9704854a5490b6aee5/lists-hero@2x.png)

The list is a complex container type that automatically provides scrolling when it grows too large for the current display. You build a list by providing it with individual views for the rows in the list, or by using a [ForEach](foreach.md) to enumerate a group of rows. You can also mix these strategies, blending any number of individual views and `ForEach` constructs.

Use view modifiers to configure the appearance and behavior of a list and its rows, headers, sections, and separators. For example, you can apply a style to the list, add swipe gestures to individual rows, or make the list refreshable with a pull-down gesture. You can also use the configuration associated with [Scroll views](scroll-views.md) to control the list’s implicit scrolling behavior.

For design guidance, see [Lists and tables](../design/human-interface-guidelines/lists-and-tables.md) in the Human Interface Guidelines.

## Topics

### Creating a list

- [Displaying data in lists](displaying-data-in-lists.md) — Visualize collections of data with platform-appropriate appearance.
- [List](list.md) — A container that presents rows of data arranged in a single column, optionally providing the ability to select one or more members.
- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.

### Disclosing information progressively

- [OutlineGroup](outlinegroup.md) — A structure that computes views and disclosure groups on demand from an underlying collection of tree-structured, identified data.
- [DisclosureGroup](disclosuregroup.md) — A view that shows or hides another content view, based on the state of a disclosure control.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.

### Configuring a list’s layout

- [listRowInsets(_:)](<view/listrowinsets(__).md>) — Applies an inset to the rows in a list.
- [listRowInsets(_:_:)](<view/listrowinsets(____).md>) — Sets the insets of rows in a list on the specified edges.
- [defaultMinListRowHeight](environmentvalues/defaultminlistrowheight.md) — The default minimum height of rows in a list.
- [defaultMinListHeaderHeight](environmentvalues/defaultminlistheaderheight.md) — The default minimum height of a header in a list.
- [listRowSpacing(_:)](<view/listrowspacing(__).md>) — Sets the vertical spacing between two adjacent rows in a List.
- [listSectionSpacing(_:)](<view/listsectionspacing(__).md>) — Sets the spacing between adjacent sections in a [List](list.md) to a custom value.
- [ListSectionSpacing](listsectionspacing.md) — The spacing options between two adjacent sections in a list.
- [listSectionMargins(_:_:)](<view/listsectionmargins(____).md>) — Set the section margins for the specific edges.

### Configuring rows

- [listItemTint(_:)](<view/listitemtint(__).md>) — Sets a fixed tint color for content in a list.
- [ListItemTint](listitemtint.md) — A tint effect configuration that you can apply to content in a list.

### Configuring headers

- [headerProminence(_:)](<view/headerprominence(__).md>) — Sets the header prominence for this view.
- [headerProminence](environmentvalues/headerprominence.md) — The prominence to apply to section headers within a view.
- [Prominence](prominence.md) — A type indicating the prominence of a view hierarchy.

### Configuring separators

- [listRowSeparatorTint(_:edges:)](<view/listrowseparatortint(__edges_).md>) — Sets the tint color associated with a row.
- [listSectionSeparatorTint(_:edges:)](<view/listsectionseparatortint(__edges_).md>) — Sets the tint color associated with a section.
- [listRowSeparator(_:edges:)](<view/listrowseparator(__edges_).md>) — Sets the display mode for the separator associated with this specific row.
- [listSectionSeparator(_:edges:)](<view/listsectionseparator(__edges_).md>) — Sets whether to hide the separator associated with a list section.

### Configuring backgrounds

- [listRowBackground(_:)](<view/listrowbackground(__).md>) — Places a custom background view behind a list row item.
- [alternatingRowBackgrounds(_:)](<view/alternatingrowbackgrounds(__).md>) — Overrides whether lists and tables in this view have alternating row backgrounds.
- [AlternatingRowBackgroundBehavior](alternatingrowbackgroundbehavior.md) — The styling of views with respect to alternating row backgrounds.
- [backgroundProminence](environmentvalues/backgroundprominence.md) — The prominence of the background underneath views associated with this environment.
- [BackgroundProminence](backgroundprominence.md) — The prominence of backgrounds underneath other views.

### Displaying a badge on a list item

- [badge(_:)](<view/badge(__).md>) — Generates a badge for the view from a localized string resource.
- [badgeProminence(_:)](<view/badgeprominence(__).md>) — Specifies the prominence of badges created by this view.
- [badgeProminence](environmentvalues/badgeprominence.md) — The prominence to apply to badges associated with this environment.
- [BadgeProminence](badgeprominence.md) — The visual prominence of a badge.

### Configuring interaction

- [swipeActions(edge:allowsFullSwipe:content:)](<view/swipeactions(edge_allowsfullswipe_content_).md>) — Adds custom swipe actions to a row in a list.
- [selectionDisabled(_:)](<view/selectiondisabled(__).md>) — Adds a condition that controls whether users can select this view.
- [listRowHoverEffect(_:)](<view/listrowhovereffect(__).md>) — Requests that the containing list row use the provided hover effect.
- [listRowHoverEffectDisabled(_:)](<view/listrowhovereffectdisabled(__).md>) — Requests that the containing list row have its hover effect disabled.

### Refreshing a list’s content

- [refreshable(action:)](<view/refreshable(action_).md>) — Adds an asynchronous handler that can update the data the view displays when a person initiates a request, such as by pulling to refresh.
- [refresh](environmentvalues/refresh.md) — A refresh action stored in a view’s environment.
- [RefreshAction](refreshaction.md) — An action that initiates a refresh operation.

### Editing a list

- [moveDisabled(_:)](<view/movedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is movable.
- [deleteDisabled(_:)](<view/deletedisabled(__).md>) — Adds a condition for whether the view’s view hierarchy is deletable.
- [editMode](environmentvalues/editmode.md) — An indication of whether the user can edit the contents of a view associated with this environment.
- [EditMode](editmode.md) — A mode that indicates whether the user can edit a view’s content.
- [EditActions](editactions.md) — A set of edit actions on a collection of data that a view can offer to a user.
- [EditableCollectionContent](editablecollectioncontent.md) — An opaque wrapper view that adds editing capabilities to a row in a list.
- [IndexedIdentifierCollection](indexedidentifiercollection.md) — A collection wrapper that iterates over the indices and identifiers of a collection together.

### Configuring a section index

- [listSectionIndexVisibility(_:)](<view/listsectionindexvisibility(__).md>) — Changes the visibility of the list section index.
- [sectionIndexLabel(_:)](<view/sectionindexlabel(__).md>) — Sets the label that is used in a section index to point to this section, typically only a single character long.

## See Also

### View layout

- [Layout fundamentals](layout-fundamentals.md) — Arrange views inside built-in layout containers like stacks and grids.
- [Layout adjustments](layout-adjustments.md) — Make fine adjustments to alignment, spacing, padding, and other layout parameters.
- [Custom layout](custom-layout.md) — Place views in custom arrangements and create animated transitions between layout types.
- [Tables](tables.md) — Display selectable, sortable data arranged in rows and columns.
- [View groupings](view-groupings.md) — Present views in different kinds of purpose-driven containers, like forms or control groups.
- [Scroll views](scroll-views.md) — Enable people to scroll to content that doesn’t fit in the current display.
