---
title: Auxiliary view modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-auxiliary-views
source_url: 'https://developer.apple.com/documentation/swiftui/view-auxiliary-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-auxiliary-views.json'
content_hash: 'sha256:b706192e49b3e933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Auxiliary view modifiers

<sub>API Collection</sub>

Add and configure supporting views, like toolbars and context menus.

## Overview

Use these modifiers to manage supplemental views that present context-specific controls and information. For example, you can add titles and buttons to navigation bars, manage the status bar, create context menus, and add badges to many different kinds of views.

## Topics

### Navigation titles

- [Configure your apps navigation titles](configure-your-apps-navigation-titles.md) — Use a navigation title to display the current navigation state of an interface.
- [navigationTitle(_:)](<view/navigationtitle(__).md>) — Configures the view’s title for purposes of navigation, using a localized string resource.
- [navigationSubtitle(_:)](<view/navigationsubtitle(__).md>) — Configures the view’s subtitle for purposes of navigation, using a localized string resource.

### Navigation title configuration

- [navigationDocument(_:)](<view/navigationdocument(__).md>) — Configures the view’s document for purposes of navigation.
- [navigationDocument(_:preview:)](<view/navigationdocument(__preview_).md>) — Configures the view’s document for purposes of navigation.

### Navigation bars

- [navigationBarBackButtonHidden(_:)](<view/navigationbarbackbuttonhidden(__).md>) — Hides the navigation bar back button for the view.
- [navigationBarTitleDisplayMode(_:)](<view/navigationbartitledisplaymode(__).md>) — Configures the title display mode for this view.

### Navigation stacks and columns

- [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) — Associates a destination view with a presented data type for use within a navigation stack.
- [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) — Associates a destination view with a binding that can be used to push the view onto a [NavigationStack](navigationstack.md).
- [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>) — Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [navigationSplitViewColumnWidth(_:)](<view/navigationsplitviewcolumnwidth(__).md>) — Sets a fixed, preferred width for the column containing this view.
- [navigationSplitViewColumnWidth(min:ideal:max:)](<view/navigationsplitviewcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the column containing this view.
- [navigationLinkIndicatorVisibility(_:)](<view/navigationlinkindicatorvisibility(__).md>) — Configures whether navigation links show a disclosure indicator.
- [navigationTransition(_:)](<view/navigationtransition(__).md>) — Sets the navigation transition style for this view.

### Scroll view edges

- [scrollEdgeEffectStyle(_:for:)](<view/scrolledgeeffectstyle(__for_).md>) — Configures the scroll edge effect style for scroll views within this hierarchy.
- [scrollEdgeEffectHidden(_:for:)](<view/scrolledgeeffecthidden(__for_).md>) — Hides any scroll edge effects for scroll views within this hierarchy.

### Tab views

- [defaultAdaptableTabBarPlacement(_:)](<view/defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<view/defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](tabview.md) in the [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [sectionActions(content:)](<view/sectionactions(content_).md>) — Adds custom actions to a section.
- [tabBarMinimizeBehavior(_:)](<view/tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [tabViewBottomAccessory(content:)](<view/tabviewbottomaccessory(content_).md>) — Places a view as the bottom accessory of the tab view.
- [tabViewBottomAccessory(isEnabled:content:)](<view/tabviewbottomaccessory(isenabled_content_).md>) — Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [tabViewCustomization(_:)](<view/tabviewcustomization(__).md>) — Specifies the customizations to apply to the sidebar representation of the tab view.
- [tabViewSearchActivation(_:)](<view/tabviewsearchactivation(__).md>) — Configures the activation and deactivation behavior of search in the search tab.
- [tabViewSidebarHeader(content:)](<view/tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<view/tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<view/tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.

### Toolbars

- [toolbar(content:)](<view/toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [toolbar(id:content:)](<view/toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbar(_:for:)](<view/toolbar(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [contentToolbar(for:content:)](<view/contenttoolbar(for_content_).md>) — Populates the toolbar of the specified content view type with the views you provide.
- [toolbar(removing:)](<view/toolbar(removing_).md>) — Remove a toolbar item present by default
- [toolbarVisibility(_:for:)](<view/toolbarvisibility(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackground(_:for:)](<view/toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](<view/toolbarbackgroundvisibility(__for_).md>) — Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [toolbarItemHidden(_:)](<view/toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [toolbarForegroundStyle(_:for:)](<view/toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<view/toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarOverflowMenu(content:)](<view/toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [toolbarRole(_:)](<view/toolbarrole(__).md>) — Configures the semantic role for the content populating the toolbar.
- [toolbarMinimizationBehavior(_:for:)](<view/toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<view/toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<view/toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
- [toolbarTitleMenu(content:)](<view/toolbartitlemenu(content_).md>) — Configure the title menu of a toolbar.
- [toolbarTitleDisplayMode(_:)](<view/toolbartitledisplaymode(__).md>) — Configures the toolbar title display mode for this view.
- [ornament(visibility:attachmentAnchor:contentAlignment:ornament:)](<view/ornament(visibility_attachmentanchor_contentalignment_ornament_).md>) — Presents an ornament.

### Context menus

- [contextMenu(menuItems:)](<view/contextmenu(menuitems_).md>) — Adds a context menu to a view.
- [contextMenu(menuItems:preview:)](<view/contextmenu(menuitems_preview_).md>) — Adds a context menu with a custom preview to a view.
- [contextMenu(forSelectionType:menu:primaryAction:)](<view/contextmenu(forselectiontype_menu_primaryaction_).md>) — Adds an item-based context menu to a view.

### Badges

- [badge(_:)](<view/badge(__).md>) — Generates a badge for the view from a localized string resource.
- [badgeProminence(_:)](<view/badgeprominence(__).md>) — Specifies the prominence of badges created by this view.

### Lists

- [sectionIndexLabel(_:)](<view/sectionindexlabel(__).md>) — Sets the label that is used in a section index to point to this section, typically only a single character long.

### Help text

- [help(_:)](<view/help(__).md>) — Adds help text to a view using a localized string resource that you provide.

### Status bar

- [statusBarHidden(_:)](<view/statusbarhidden(__).md>) — Sets the visibility of the status bar. _(deprecated)_

### External displays

- [sceneAccessory(content:)](<view/sceneaccessory(content_).md>) — Defines any scene accessories associated with `self`. _(beta)_

### Touch Bar

- [touchBar(content:)](<view/touchbar(content_).md>) — Sets the content that the Touch Bar displays.
- [touchBar(_:)](<view/touchbar(__).md>) — Sets the Touch Bar content to be shown in the Touch Bar when applicable.
- [touchBarItemPrincipal(_:)](<view/touchbaritemprincipal(__).md>) — Sets principal views that have special significance to this Touch Bar.
- [touchBarCustomizationLabel(_:)](<view/touchbarcustomizationlabel(__).md>) — Sets a user-visible string that identifies the view’s functionality.
- [touchBarItemPresence(_:)](<view/touchbaritempresence(__).md>) — Sets the behavior of the user-customized view.

## See Also

### Configuring view elements

- [Accessibility modifiers](view-accessibility.md) — Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md) — Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md) — Manage the rendering, selection, and entry of text in your view.
- [Chart view modifiers](view-chart-view.md) — Configure charts that you declare with Swift Charts.
