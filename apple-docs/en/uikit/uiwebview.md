---
title: UIWebView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview.json'
content_hash: 'sha256:bb363e17355cab70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWebView

<sub>Class</sub>

A view that embeds web content in your app.

> [!warning] Deprecated
> Use [WKWebView](../webkit/wkwebview.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UIWebView
```

## Overview

> [!note] Note
> In apps that run in iOS 8 and later, use the [WKWebView](../webkit/wkwebview.md) class instead of using [UIWebView](uiwebview.md). Additionally, consider setting the [WKPreferences](../webkit/wkpreferences.md) property [javaScriptEnabled](../webkit/wkpreferences/javascriptenabled.md) to [false](../swift/false.md) if you render files that aren’t supposed to run JavaScript.

> [!important] Important
> An iOS app linked on or after iOS 10.0 must include in its `Info.plist` file the usage description keys for the types of data it needs to access or it will crash. To access a user’s photo data specifically, it must include [NSPhotoLibraryUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW17) and [NSCameraUsageDescription](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW24).

Use the [- loadHTMLString:baseURL:](<uiwebview/loadhtmlstring(__baseurl_).md>) method to begin loading local HTML files or the [- loadRequest:](<uiwebview/loadrequest(__).md>) method to begin loading web content. Use the [- stopLoading](<uiwebview/stoploading().md>) method to stop loading, and the [loading](uiwebview/isloading.md) property to find out if a web view is in the process of loading.

If you allow the user to move back and forward through the webpage history, then you can use the [- goBack](<uiwebview/goback().md>) and [- goForward](<uiwebview/goforward().md>) methods as actions for buttons. Use the [canGoBack](uiwebview/cangoback.md) and [canGoForward](uiwebview/cangoforward.md) properties to disable the buttons when the user can’t move in a direction.

By default, a web view automatically converts telephone numbers that appear in web content to Phone links. When a Phone link is tapped, the Phone app launches and dials the number. To turn off this default behavior, set the [dataDetectorTypes](uiwebview/datadetectortypes.md) property with a [UIDataDetectorTypes](uidatadetectortypes.md) bitfield that doesn’t contain the [UIDataDetectorTypePhoneNumber](uidatadetectortypes/phonenumber.md) flag.

You can also use the [scalesPageToFit](uiwebview/scalespagetofit.md) property to programmatically set the scale of web content the first time it’s displayed in a web view. Thereafter, the user can change the scale using gestures.

Set the [delegate](uiwebview/delegate.md) property to an object conforming to the [UIWebViewDelegate](uiwebviewdelegate.md) protocol if you want to track the loading of web content.

> [!important] Important
> You shouldn’t embed [UIWebView](uiwebview.md) or [UITableView](uitableview.md) objects in [UIScrollView](uiscrollview.md) objects. If you do so, unexpected behavior can result because touch events for the two objects can be mixed up and wrongly handled.

You can debug the HTML, CSS, and JavaScript contained inside a [UIWebView](uiwebview.md) with Web Inspector. Read Debugging Web Content on iOS to learn how to configure Web Inspector for iOS. Read the rest of [Safari Web Content Guide](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/Introduction/Introduction.html#//apple_ref/doc/uid/TP40002051) to learn how to create web content that’s optimized for Safari on iPhone and iPad.

For information about basic view behaviors, see [View Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009503).

### Supported file formats

In addition to HTML content, [UIWebView](uiwebview.md) objects can be used to display other content types, such as Keynote, PDF, and Pages documents. For the best rendering of plain and rich text in your app, however, you should use [UITextView](uitextview.md) instead.

### State preservation

In iOS 6 and later, if you assign a value to this view’s [restorationIdentifier](uiviewcontroller/restorationidentifier.md) property, it attempts to preserve its URL history, the scaling and scrolling positions for each page, and information about which page is currently being viewed. During restoration, the view restores these values so that the web content appears just as it did before. For more information about how state preservation and restoration works, see [App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072).

### Subclassing notes

The [UIWebView](uiwebview.md) class shouldn’t be subclassed.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIScrollViewDelegate](uiscrollviewdelegate.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Essentials

- [Replacing UIWebView in your app](../webkit/replacing-uiwebview-in-your-app.md) — Find a suitable alternative to handle your app’s web content.

### Responding to web view changes

- [delegate](uiwebview/delegate.md) — The receiver’s delegate. _(deprecated)_
- [UIWebViewDelegate](uiwebviewdelegate.md) — The `UIWebViewDelegate` protocol defines methods that a delegate of a [UIWebView](uiwebview.md) object can optionally implement to intervene when web content is loaded.

### Loading content

- [- loadData:MIMEType:textEncodingName:baseURL:](<uiwebview/load(__mimetype_textencodingname_baseurl_).md>) — Sets the main page contents, MIME type, content encoding, and base URL. _(deprecated)_
- [- loadHTMLString:baseURL:](<uiwebview/loadhtmlstring(__baseurl_).md>) — Sets the main page content and base URL. _(deprecated)_
- [- loadRequest:](<uiwebview/loadrequest(__).md>) — Connects to a given URL by initiating an asynchronous client request. _(deprecated)_
- [request](uiwebview/request.md) — The URL request identifying the location of the content to load. _(deprecated)_
- [loading](uiwebview/isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- stopLoading](<uiwebview/stoploading().md>) — Stops the loading of any web content managed by the receiver. _(deprecated)_
- [- reload](<uiwebview/reload().md>) — Reloads the current page. _(deprecated)_

### Moving back and forward

- [canGoBack](uiwebview/cangoback.md) — A Boolean value indicating whether the receiver can move backward. _(deprecated)_
- [canGoForward](uiwebview/cangoforward.md) — A Boolean value indicating whether the receiver can move forward. _(deprecated)_
- [- goBack](<uiwebview/goback().md>) — Loads the previous location in the back-forward list. _(deprecated)_
- [- goForward](<uiwebview/goforward().md>) — Loads the next location in the back-forward list. _(deprecated)_

### Setting web content properties

- [allowsLinkPreview](uiwebview/allowslinkpreview.md) — A Boolean value that determines whether pressing on a link displays a preview of the destination for the link. _(deprecated)_
- [scalesPageToFit](uiwebview/scalespagetofit.md) — A Boolean value determining whether the webpage scales to fit the view and the user can change the scale. _(deprecated)_
- [scrollView](uiwebview/scrollview.md) — The scroll view associated with the web view. _(deprecated)_
- [suppressesIncrementalRendering](uiwebview/suppressesincrementalrendering.md) — A Boolean value indicating whether the web view suppresses content rendering until it is fully loaded into memory. _(deprecated)_
- [keyboardDisplayRequiresUserAction](uiwebview/keyboarddisplayrequiresuseraction.md) — A Boolean value indicating whether web content can programmatically display the keyboard. _(deprecated)_
- [dataDetectorTypes](uiwebview/datadetectortypes.md) — The types of data converted to clickable URLs in the web view’s content. _(deprecated)_

### Running JavaScript

- [- stringByEvaluatingJavaScriptFromString:](<uiwebview/stringbyevaluatingjavascript(from_).md>) — Returns the result of running a JavaScript script. _(deprecated)_

### Managing media playback

- [allowsInlineMediaPlayback](uiwebview/allowsinlinemediaplayback.md) — A Boolean value that determines whether HTML5 videos play inline or use the native full-screen controller. _(deprecated)_
- [mediaPlaybackRequiresUserAction](uiwebview/mediaplaybackrequiresuseraction.md) — A Boolean value that determines whether HTML5 videos can play automatically or require the user to start playing them. _(deprecated)_
- [mediaPlaybackAllowsAirPlay](uiwebview/mediaplaybackallowsairplay.md) — A Boolean value that determines whether Air Play is allowed from this view. _(deprecated)_
- [allowsPictureInPictureMediaPlayback](uiwebview/allowspictureinpicturemediaplayback.md) — A Boolean value that determines whether Picture in Picture playback is allowed from this view. _(deprecated)_

### Managing pages

- [gapBetweenPages](uiwebview/gapbetweenpages.md) — The size of the gap, in points, between pages. _(deprecated)_
- [pageCount](uiwebview/pagecount.md) — The number of pages produced by the layout of the web view. _(deprecated)_
- [pageLength](uiwebview/pagelength.md) — The size of each page, in points, in the direction that the pages flow. _(deprecated)_
- [paginationBreakingMode](uiwebview/paginationbreakingmode-swift.property.md) — The manner in which column- or page-breaking occurs. _(deprecated)_
- [paginationMode](uiwebview/paginationmode-swift.property.md) — The layout of content in the web view. _(deprecated)_

### Constants

- [NavigationType](uiwebview/navigationtype.md) — Constant indicating the user’s action.
- [PaginationBreakingMode](uiwebview/paginationbreakingmode-swift.enum.md) — The manner in which column- or page-breaking occurs.
- [PaginationMode](uiwebview/paginationmode-swift.enum.md) — The layout of content in the web view, which determines the direction that the pages flow.
- [UIDataDetectorTypes](uidatadetectortypes.md) — Constants that define the types of information to detect in text-based content.

## See Also

### Deprecated classes

- [UIActionSheet](uiactionsheet.md) — A view that presents a set of alternatives for how to proceed with a task. _(deprecated)_
- [UIAlertView](uialertview.md) — A view that displays an alert message. _(deprecated)_
- [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md) — A list of all the available document providers for a given file type and mode, in addition to custom menu items that you add. _(deprecated)_
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
- [UIUserNotificationAction](uiusernotificationaction.md) — A custom action that your app can perform in response to a remote or local notification. _(deprecated)_
- [UIUserNotificationCategory](uiusernotificationcategory.md) — Information about custom actions that your app can perform in response to a local or push notification. _(deprecated)_
