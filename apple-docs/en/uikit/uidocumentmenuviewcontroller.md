---
title: UIDocumentMenuViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uidocumentmenuviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenuviewcontroller.json'
content_hash: 'sha256:48a94f487ada193d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDocumentMenuViewController

<sub>Class</sub>

A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add.

> [!warning] Deprecated
> Use [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIDocumentMenuViewController
```

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a document menu

- [- initWithDocumentTypes:inMode:](<uidocumentmenuviewcontroller/init(documenttypes_in_).md>) — Initializes and returns a document menu to import or open the given file types. _(deprecated)_
- [- initWithURL:inMode:](<uidocumentmenuviewcontroller/init(url_in_).md>) — Initializes and returns a document menu to export or move the given document. _(deprecated)_
- [- initWithCoder:](<uidocumentmenuviewcontroller/init(coder_).md>) — Creates a document menu from data in an unarchiver. _(deprecated)_

### Getting the user-selected document picker

- [delegate](uidocumentmenuviewcontroller/delegate.md) — The document menu’s delegate. _(deprecated)_
- [UIDocumentMenuDelegate](uidocumentmenudelegate.md) — A set of methods that you must implement to track user interactions with a document menu view controller. _(deprecated)_

### Configuring a document menu

- [- addOptionWithTitle:image:order:handler:](<uidocumentmenuviewcontroller/addoption(withtitle_image_order_handler_).md>) — Adds a custom menu item to the list of document pickers. _(deprecated)_
- [UIDocumentMenuOrder](uidocumentmenuorder.md) — The insertion point for custom menu items. _(deprecated)_

### Initializers

- [init(URL:inMode:)](<uidocumentmenuviewcontroller/init(url_inmode_).md>) _(deprecated)_
- [init(documentTypes:inMode:)](<uidocumentmenuviewcontroller/init(documenttypes_inmode_).md>) _(deprecated)_

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UILocalNotification](uilocalnotification.md) — A notification that an app can schedule for presentation at a specific date and time. _(deprecated)_
- [UIMenuController](uimenucontroller.md) — The menu interface for the Cut, Copy, Paste, Select, Select All, and Delete commands. _(deprecated)_
- [UIMenuItem](uimenuitem.md) — A custom item in the editing menu managed by the menu controller. _(deprecated)_
- [UIMutableUserNotificationAction](uimutableusernotificationaction.md) — A modifiable version of the user notification action class. _(deprecated)_
- [UIMutableUserNotificationCategory](uimutableusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
- [UIPopoverController](uipopovercontroller.md) — An object that manages the presentation of content in a popover. _(deprecated)_
- [UIPreviewAction](uipreviewaction.md) — A preview action, or _peek quick action_, that displays below a peek when a user swipes the peek upward. _(deprecated)_
- [UIPreviewActionGroup](uipreviewactiongroup.md) — A group of one or more child quick actions, each an instance of the preview action class. _(deprecated)_
- [UISearchDisplayController](uisearchdisplaycontroller.md) — An object that manages the display of a search bar, along with a table view that displays search results. _(deprecated)_
- [UIStoryboardPopoverSegue](uistoryboardpopoversegue.md) — A specific type of segue for presenting content in a popover. _(deprecated)_
- [UIWebView](uiwebview.md) — A view that embeds web content in your app. _(deprecated)_
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
