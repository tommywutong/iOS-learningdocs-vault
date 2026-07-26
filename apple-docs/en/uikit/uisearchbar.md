---
title: UISearchBar
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar.json'
content_hash: 'sha256:325a740a58f4c3ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchBar

<sub>Class</sub>

A specialized view for receiving search-related information from the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UISearchBar
```

## Overview

[UISearchBar](uisearchbar.md) provides a text field for entering text, a search button, a bookmark button, and a cancel button. A search bar doesn’t actually perform any searches. You use a delegate, an object conforming to the [UISearchBarDelegate](uisearchbardelegate.md) protocol, to implement the actions when the user enters text or clicks buttons. For details about interacting with the text field, accessing its content, and using tokens, see [UISearchTextField](uisearchtextfield.md) and [UISearchToken](uisearchtoken.md).

### Customize appearance

You can customize the appearance of search bars one at a time, or you can use the appearance proxy (`[UISearchBar appearance]`) to customize the appearance of all search bars in an app.

In general, you should specify a value for the normal state to be used by other states which don’t have a custom value set. Similarly, when a property is dependent on the bar metrics (on iPhone, in landscape orientation bars have a different height from standard), you should specify a value for `UIBarMetricsDefault`.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIBarPositioning](uibarpositioning.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UILookToDictateCapable](uilooktodictatecapable.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITextInputTraits](uitextinputtraits.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a search bar

- [- init](<uisearchbar/init().md>) — Initializes the search bar to its default state.
- [- initWithCoder:](<uisearchbar/init(coder_).md>) — Creates a search bar from data in a given unarchiver.
- [- initWithFrame:](<uisearchbar/init(frame_).md>) — Creates a search bar with a specified frame.

### Handling search bar interactions

- [delegate](uisearchbar/delegate.md) — The search bar’s delegate object.
- [UISearchBarDelegate](uisearchbardelegate.md) — A collection of optional methods that you implement to make a search bar control functional.

### Getting the search text

- [placeholder](uisearchbar/placeholder.md) — The string to display when there’s no other text in the text field.
- [prompt](uisearchbar/prompt.md) — A single line of text displayed at the top of the search bar.
- [text](uisearchbar/text.md) — The current or starting search text.
- [searchTextField](uisearchbar/searchtextfield.md) — The text field that the user enters a search query into.

### Configuring the search bar

- [enabled](uisearchbar/isenabled.md) — A Boolean value indicating whether the search bar is in the enabled state.
- [barTintColor](uisearchbar/bartintcolor.md) — The tint color to apply to the search bar background.
- [searchBarStyle](uisearchbar/searchbarstyle.md) — A search bar style that specifies the search bar’s appearance.
- [Style](uisearchbar/style.md) — Specifies whether the search bar has a background.
- [tintColor](uisearchbar/tintcolor.md) — The tint color to apply to key elements in the search bar.
- [translucent](uisearchbar/istranslucent.md) — A Boolean value that indicates whether the search bar is translucent (true) or not (false).
- [barStyle](uisearchbar/barstyle.md) — A bar style that specifies the search bar’s appearance.
- [UIBarStyle](uibarstyle.md) — Defines the stylistic appearance of different types of views.

### Customizing the keyboard shortcut items

- [inputAssistantItem](uisearchbar/inputassistantitem.md) — The input assistant to use for configuring the keyboard’s shortcuts bar.

### Configuring the search interface

- [showsBookmarkButton](uisearchbar/showsbookmarkbutton.md) — A Boolean value indicating whether the bookmark button is displayed.
- [showsCancelButton](uisearchbar/showscancelbutton.md) — A Boolean value indicating whether the cancel button is displayed.
- [- setShowsCancelButton:animated:](<uisearchbar/setshowscancelbutton(__animated_).md>) — Sets the display state of the cancel button optionally with animation.
- [showsSearchResultsButton](uisearchbar/showssearchresultsbutton.md) — A Boolean value indicating whether the search results button is displayed.
- [searchResultsButtonSelected](uisearchbar/issearchresultsbuttonselected.md) — A Boolean value indicating whether the search results button is selected.

### Customizing the search bar appearance

- [backgroundImage](uisearchbar/backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<uisearchbar/backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<uisearchbar/setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<uisearchbar/image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<uisearchbar/setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<uisearchbar/positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<uisearchbar/setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](uisearchbar/inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<uisearchbar/searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<uisearchbar/setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](uisearchbar/searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](uisearchbar/searchtextpositionadjustment.md) — The offset of the text within the search text field background.

### Configuring scope bar buttons

- [scopeButtonTitles](uisearchbar/scopebuttontitles.md) — An array of strings indicating the titles of the scope buttons.
- [selectedScopeButtonIndex](uisearchbar/selectedscopebuttonindex.md) — The index of the selected scope button.
- [showsScopeBar](uisearchbar/showsscopebar.md) — Specifies whether the scope bar is displayed.
- [- setShowsScopeBar:animated:](<uisearchbar/setshowsscope(__animated_).md>) — Specifies whether the scope bar is displayed, optionally using an animation.

### Customizing the scope bar appearance

- [scopeBarBackgroundImage](uisearchbar/scopebarbackgroundimage.md) — The background image for the scope bar.
- [- scopeBarButtonBackgroundImageForState:](<uisearchbar/scopebarbuttonbackgroundimage(for_).md>) — Returns the background image for the scope bar button in a given state.
- [- setScopeBarButtonBackgroundImage:forState:](<uisearchbar/setscopebarbuttonbackgroundimage(__for_).md>) — Sets the background image for the scope bar button in a given state.
- [- scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:](<uisearchbar/scopebarbuttondividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image to use for a given combination of left and right segment states.
- [- setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:](<uisearchbar/setscopebarbuttondividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the divider image to use for a given combination of left and right segment states.
- [- scopeBarButtonTitleTextAttributesForState:](<uisearchbar/scopebarbuttontitletextattributes(for_).md>) — Returns the text attributes for the search bar’s button’s title string for a given state.
- [- setScopeBarButtonTitleTextAttributes:forState:](<uisearchbar/setscopebarbuttontitletextattributes(__for_).md>) — Sets the text attributes for the search bar’ button’s title string for a given state.

### Managing dictation

- [lookToDictateEnabled](uisearchbar/islooktodictateenabled.md)
- [UILookToDictateCapable](uilooktodictatecapable.md)

### Constants

- [Icon](uisearchbar/icon.md) — Constants to identify the icons used in the search bar.

## See Also

### Search interface

- [UISearchContainerViewController](uisearchcontainerviewcontroller.md) — A view controller that manages the presentation of search results in your interface.
- [UISearchController](uisearchcontroller.md) — A view controller that manages the display of search results based on interactions with a search bar.
- [UISearchResultsUpdating](uisearchresultsupdating.md) — A set of methods that let you update search results based on information the user enters into the search bar.
- [Displaying searchable content by using a search controller](displaying-searchable-content-by-using-a-search-controller.md) — Create a user interface with searchable content in a table view.
- [Using suggested searches with a search controller](using-suggested-searches-with-a-search-controller.md) — Create a search interface with a table view of suggested searches.
