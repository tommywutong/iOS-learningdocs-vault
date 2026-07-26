---
title: UIResponderStandardEditActions
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponderstandardeditactions
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions.json'
content_hash: 'sha256:806a50fcbc4104b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIResponderStandardEditActions

<sub>Protocol</sub>

A set of standard methods that apps can adopt to support editing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIResponderStandardEditActions : NSObjectProtocol
```

## Overview

Responder objects can implement the methods of this protocol to handle standard editing-related actions. For example, a [UIEditMenuInteraction](uieditmenuinteraction.md) object displays the actions in an edit menu using these methods. UIKit searches the responder chain for an object that implements the appropriate method, calling the method on the first object that implements it.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIAccessibilityElement](uiaccessibilityelement.md), [UIActionSheet](uiactionsheet.md), [UIActivityIndicatorView](uiactivityindicatorview.md), [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UIAlertView](uialertview.md), [UIApplication](uiapplication.md), [UIBackgroundExtensionView](uibackgroundextensionview.md), [UIButton](uibutton.md), [UICalendarView](uicalendarview.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionReusableView](uicollectionreusableview.md), [UICollectionView](uicollectionview.md), [UICollectionViewCell](uicollectionviewcell.md), [UICollectionViewController](uicollectionviewcontroller.md), [UICollectionViewListCell](uicollectionviewlistcell.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIColorWell](uicolorwell.md), [UIContentUnavailableView](uicontentunavailableview.md), [UIControl](uicontrol.md), [UIDatePicker](uidatepicker.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIEventAttributionView](uieventattributionview.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIImageView](uiimageview.md), [UIInputView](uiinputview.md), [UIInputViewController](uiinputviewcontroller.md), [UILabel](uilabel.md), [UIListContentView](uilistcontentview.md), [UINavigationBar](uinavigationbar.md), [UINavigationController](uinavigationcontroller.md), [UIPageControl](uipagecontrol.md), [UIPageViewController](uipageviewcontroller.md), [UIPasteControl](uipastecontrol.md), [UIPickerView](uipickerview.md), [UIPopoverBackgroundView](uipopoverbackgroundview.md), [UIProgressView](uiprogressview.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UIRefreshControl](uirefreshcontrol.md), [UIResponder](uiresponder.md), [UIScene](uiscene.md), [UIScrollView](uiscrollview.md), [UISearchBar](uisearchbar.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISearchTextField](uisearchtextfield.md), [UISegmentedControl](uisegmentedcontrol.md), [UISlider](uislider.md), [UISplitViewController](uisplitviewcontroller.md), [UIStackView](uistackview.md), [UIStandardTextCursorView](uistandardtextcursorview.md), [UIStepper](uistepper.md), [UISwitch](uiswitch.md), [UITabBar](uitabbar.md), [UITabBarController](uitabbarcontroller.md), [UITableView](uitableview.md), [UITableViewCell](uitableviewcell.md), [UITableViewController](uitableviewcontroller.md), [UITableViewHeaderFooterView](uitableviewheaderfooterview.md), [UITextField](uitextfield.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UITextView](uitextview.md), [UIToolbar](uitoolbar.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md), [UIVisualEffectView](uivisualeffectview.md), [UIWebView](uiwebview.md), [UIWindow](uiwindow.md), [UIWindowScene](uiwindowscene.md)

## Topics

### Handling copy, cut, paste, and delete commands

- [- cut:](<uiresponderstandardeditactions/cut(__).md>) — Removes the selected content and writes the data for it to the pasteboard.
- [- copy:](<uiresponderstandardeditactions/copy(__).md>) — Copies the selected content to the pasteboard.
- [- paste:](<uiresponderstandardeditactions/paste(__).md>) — Pastes the current contents of the pasteboard into your app’s interface.
- [- pasteAndGo:](<uiresponderstandardeditactions/pasteandgo(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [- pasteAndMatchStyle:](<uiresponderstandardeditactions/pasteandmatchstyle(__).md>) — Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [- pasteAndSearch:](<uiresponderstandardeditactions/pasteandsearch(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [- delete:](<uiresponderstandardeditactions/delete(__).md>) — Removes the selected content from your interface.

### Handling find and replace commands

- [- find:](<uiresponderstandardeditactions/find(__).md>) — Begins a search for content in your app’s interface.
- [- findNext:](<uiresponderstandardeditactions/findnext(__).md>) — Finds the next match in your app’s interface.
- [- findPrevious:](<uiresponderstandardeditactions/findprevious(__).md>) — Finds the previous match in your app’s interface.
- [- findAndReplace:](<uiresponderstandardeditactions/findandreplace(__).md>) — Begins a search for content in your app’s interface and provides a replacement.
- [- useSelectionForFind:](<uiresponderstandardeditactions/useselectionforfind(__).md>) — Begins a search for the selected content in your app’s interface.

### Handling selection commands

- [- select:](<uiresponderstandardeditactions/select(__).md>) — Selects the content in your responder.
- [- selectAll:](<uiresponderstandardeditactions/selectall(__).md>) — Selects all of the content in the current responder.

### Handling data commands

- [- duplicate:](<uiresponderstandardeditactions/duplicate(__).md>) — Duplicates data.
- [- export:](<uiresponderstandardeditactions/export(__).md>) — Exports data in different file formats or to other apps.
- [- move:](<uiresponderstandardeditactions/move(__).md>) — Prompts a person to specify a new location and moves data to that location.
- [- rename:](<uiresponderstandardeditactions/rename(__).md>) — Changes a title.

### Handling a print command

- [- print:](<uiresponderstandardeditactions/printcontent(__).md>) — Tells your app to print available content.

### Handling styled text editing

- [- toggleBoldface:](<uiresponderstandardeditactions/toggleboldface(__).md>) — Toggles the bold style information of the selected text.
- [- toggleItalics:](<uiresponderstandardeditactions/toggleitalics(__).md>) — Toggles the italic style information of the selected text.
- [- toggleUnderline:](<uiresponderstandardeditactions/toggleunderline(__).md>) — Toggles the underline style information of the selected text.

### Handling writing direction changes

- [- makeTextWritingDirectionLeftToRight:](<uiresponderstandardeditactions/maketextwritingdirectionlefttoright(__).md>) — Changes the writing direction to left-to-right.
- [- makeTextWritingDirectionRightToLeft:](<uiresponderstandardeditactions/maketextwritingdirectionrighttoleft(__).md>) — Changes the writing direction to right-to-left.

### Handling size changes

- [- increaseSize:](<uiresponderstandardeditactions/increasesize(__).md>) — Increases the size of the current object by one unit.
- [- decreaseSize:](<uiresponderstandardeditactions/decreasesize(__).md>) — Decreases the size of the current object by one unit.

### Handling other text formatting changes

- [- updateTextAttributesWithConversionHandler:](<uiresponderstandardeditactions/updatetextattributes(conversionhandler_).md>) — Tells your app to update the attributes of the currently selected text.

### Instance Methods

- [- alignCenter:](<uiresponderstandardeditactions/aligncenter(__).md>)
- [- alignJustified:](<uiresponderstandardeditactions/alignjustified(__).md>)
- [- alignLeft:](<uiresponderstandardeditactions/alignleft(__).md>)
- [- alignRight:](<uiresponderstandardeditactions/alignright(__).md>)
- [- newFromPasteboard:](<uiresponderstandardeditactions/newfrompasteboard(__).md>)
- [- performClose:](<uiresponderstandardeditactions/performclose(__).md>)
- [- showWritingTools:](<uiresponderstandardeditactions/showwritingtools(__).md>)
- [- toggleInspector:](<uiresponderstandardeditactions/toggleinspector(__).md>)
- [- toggleSidebar:](<uiresponderstandardeditactions/togglesidebar(__).md>)

## See Also

### Edit menus

- [UIEditMenuInteraction](uieditmenuinteraction.md) — An interaction that provides edit operations using a menu.
- [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) — The methods for customizing the menu the interaction displays.
- [UIEditMenuConfiguration](uieditmenuconfiguration.md) — An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
