---
title: Deprecated modifiers
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/view-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view-deprecated.json'
content_hash: 'sha256:53eeba13f5eef550'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [View fundamentals](view-fundamentals.md) · [View](view.md)

# Deprecated modifiers

<sub>API Collection</sub>

Review unsupported modifiers and their replacements.

## Overview

Avoid using deprecated modifiers in your app. Select a modifier to see the replacement that you should use instead.

## Topics

### Accessibility modifiers

- [accessibility(label:)](<view/accessibility(label_).md>) — Adds a label to the view that describes its contents. _(deprecated)_
- [accessibility(value:)](<view/accessibility(value_).md>) — Adds a textual description of the value that the view contains. _(deprecated)_
- [accessibility(hidden:)](<view/accessibility(hidden_).md>) — Specifies whether to hide this view from system accessibility features. _(deprecated)_
- [accessibility(identifier:)](<view/accessibility(identifier_).md>) — Uses the specified string to identify the view. _(deprecated)_
- [accessibility(selectionIdentifier:)](<view/accessibility(selectionidentifier_).md>) — Sets a selection identifier for this view’s accessibility element. _(deprecated)_
- [accessibility(hint:)](<view/accessibility(hint_).md>) — Communicates to the user what happens after performing the view’s action. _(deprecated)_
- [accessibility(activationPoint:)](<view/accessibility(activationpoint_).md>) — Specifies the point where activations occur in the view. _(deprecated)_
- [accessibility(inputLabels:)](<view/accessibility(inputlabels_).md>) — Sets alternate input labels with which users identify a view. _(deprecated)_
- [accessibility(addTraits:)](<view/accessibility(addtraits_).md>) — Adds the given traits to the view. _(deprecated)_
- [accessibility(removeTraits:)](<view/accessibility(removetraits_).md>) — Removes the given traits from this view. _(deprecated)_
- [accessibility(sortPriority:)](<view/accessibility(sortpriority_).md>) — Sets the sort priority order for this view’s accessibility element, relative to other elements at the same level. _(deprecated)_

### Appearance modifiers

- [colorScheme(_:)](<view/colorscheme(__).md>) — Sets this view’s color scheme. _(deprecated)_
- [listRowPlatterColor(_:)](<view/listrowplattercolor(__).md>) — Sets the color that the system applies to the row background when this view is placed in a list. _(deprecated)_
- [background(_:alignment:)](<view/background(__alignment_).md>) — Layers the given view behind this view. _(deprecated)_
- [overlay(_:alignment:)](<view/overlay(__alignment_).md>) — Layers a secondary view in front of this view. _(deprecated)_
- [foregroundColor(_:)](<view/foregroundcolor(__).md>) — Sets the color of the foreground elements displayed by this view. _(deprecated)_
- [complicationForeground()](<view/complicationforeground().md>) — Promotes this view to the foreground in a complication. _(deprecated)_

### Text modifiers

- [autocapitalization(_:)](<view/autocapitalization(__).md>) — Sets whether to apply auto-capitalization to this view. _(deprecated)_
- [disableAutocorrection(_:)](<view/disableautocorrection(__).md>) — Sets whether to disable autocorrection for this view. _(deprecated)_

### Auxiliary view modifiers

- [navigationBarTitle(_:)](<view/navigationbartitle(__).md>) — Sets the title in the navigation bar for this view. _(deprecated)_
- [navigationBarTitle(_:displayMode:)](<view/navigationbartitle(__displaymode_).md>) — Sets the title and display mode in the navigation bar for this view. _(deprecated)_
- [navigationBarItems(leading:)](<view/navigationbaritems(leading_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(leading:trailing:)](<view/navigationbaritems(leading_trailing_).md>) — Sets the navigation bar items for this view. _(deprecated)_
- [navigationBarItems(trailing:)](<view/navigationbaritems(trailing_).md>) — Configures the navigation bar items for this view. _(deprecated)_
- [navigationBarHidden(_:)](<view/navigationbarhidden(__).md>) — Hides the navigation bar for this view. _(deprecated)_
- [statusBar(hidden:)](<view/statusbar(hidden_).md>) — Sets the visibility of the status bar. _(deprecated)_
- [contextMenu(_:)](<view/contextmenu(__).md>) — Adds a context menu to the view. _(deprecated)_

### Style modifiers

- [menuButtonStyle(_:)](<view/menubuttonstyle(__).md>) — Sets the style for menu buttons within this view. _(deprecated)_
- [navigationViewStyle(_:)](<view/navigationviewstyle(__).md>) — Sets the style for navigation views within this view. _(deprecated)_

### Layout modifiers

- [frame()](<view/frame().md>) — Positions this view within an invisible frame. _(deprecated)_
- [edgesIgnoringSafeArea(_:)](<view/edgesignoringsafearea(__).md>) — Changes the view’s proposed area to extend outside the screen’s safe areas. _(deprecated)_
- [coordinateSpace(name:)](<view/coordinatespace(name_).md>) — Assigns a name to the view’s coordinate space, so other code can operate on dimensions like points and sizes relative to the named space. _(deprecated)_

### Graphics and rendering modifiers

- [accentColor(_:)](<view/accentcolor(__).md>) — Sets the accent color for this view and the views it contains. _(deprecated)_
- [mask(_:)](<view/mask(__).md>) — Masks this view using the alpha channel of the given view. _(deprecated)_
- [animation(_:)](<view/animation(__)-1hc0p.md>) — Applies the given animation to all animatable values within this view. _(deprecated)_
- [cornerRadius(_:antialiased:)](<view/cornerradius(__antialiased_).md>) — Clips this view to its bounding frame, with the specified corner radius. _(deprecated)_

### Input and events modifiers

- [dropDestination(for:action:isTargeted:)](<view/dropdestination(for_action_istargeted_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify. _(deprecated)_
- [onChange(of:perform:)](<view/onchange(of_perform_).md>) — Adds an action to perform when the given value changes. _(deprecated)_
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_)-36x9h.md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(deprecated)_
- [onLongPressGesture(minimumDuration:maximumDistance:pressing:perform:)](<view/onlongpressgesture(minimumduration_maximumdistance_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onLongPressGesture(minimumDuration:pressing:perform:)](<view/onlongpressgesture(minimumduration_pressing_perform_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(deprecated)_
- [onPasteCommand(of:perform:)](<view/onpastecommand(of_perform_)-4f78f.md>) — Adds an action to perform in response to the system’s Paste command. _(deprecated)_
- [onPasteCommand(of:validator:perform:)](<view/onpastecommand(of_validator_perform_)-964k1.md>) — Adds an action to perform in response to the system’s Paste command with items that you validate. _(deprecated)_
- [onDrop(of:delegate:)](<view/ondrop(of_delegate_)-2vr9o.md>) — Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate. _(deprecated)_
- [onDrop(of:isTargeted:perform:)](<view/ondrop(of_istargeted_perform_).md>) — Defines the destination of a drag-and-drop operation that handles the dropped content with a closure that you specify.
- [focusable(_:onFocusChange:)](<view/focusable(__onfocuschange_).md>) — Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus. _(deprecated)_
- [onContinuousHover(coordinateSpace:perform:)](<view/oncontinuoushover(coordinatespace_perform_)-8gyrl.md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds. _(deprecated)_

### View presentation modifiers

- [actionSheet(isPresented:content:)](<view/actionsheet(ispresented_content_).md>) — Presents an action sheet when a given condition is true. _(deprecated)_
- [actionSheet(item:content:)](<view/actionsheet(item_content_).md>) — Presents an action sheet using the given item as a data source for the sheet’s content. _(deprecated)_
- [alert(isPresented:content:)](<view/alert(ispresented_content_).md>) — Presents an alert to the user. _(deprecated)_
- [alert(item:content:)](<view/alert(item_content_).md>) — Presents an alert to the user. _(deprecated)_

### Search modifiers

- [searchable(text:placement:prompt:suggestions:)](<view/searchable(text_placement_prompt_suggestions_).md>) — Marks this view as searchable, which configures the display of a search field. _(deprecated)_

### Tab modifiers

- [tabItem(_:)](<view/tabitem(__).md>) — Sets the tab bar item associated with this view. _(deprecated)_

### Generating image modifiers

- [imagePlaygroundPersonalizationPolicy(_:)](<view/imageplaygroundpersonalizationpolicy(__).md>) — Policy determining whether to support the usage of people in the playground or not. _(deprecated)_

### Technology-specific modifiers

- [postToPhotosSharedAlbumSheet(isPresented:items:photoLibrary:defaultAlbumIdentifier:completion:)](<view/posttophotossharedalbumsheet(ispresented_items_photolibrary_defaultalbumidentifier_completion_).md>) — Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album. _(deprecated)_
- [offerCodeRedemption(isPresented:onCompletion:)](<view/offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_
- [subscriptionPromotionalOffer(offer:signature:)](<view/subscriptionpromotionaloffer(offer_signature_).md>) — Selects a promotional offer to apply to a purchase a customer makes from a subscription store view. _(deprecated)_
