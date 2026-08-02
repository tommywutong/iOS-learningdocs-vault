---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/SafariServices.html
archived_at: '2026-07-18T02:51:33.900458Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# SafariServices Changes for Swift

### SafariServices (Added)

Added [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)Added [SFContentBlockerManager.getStateOfContentBlocker(withIdentifier: String, completionHandler: (SFContentBlockerState?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1639499-getstateofcontentblockerwithiden)Added [SFContentBlockerManager.reloadContentBlocker(withIdentifier: String, completionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1620151-reloadcontentblocker)Added [SFContentBlockerState](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate)Added [SFContentBlockerState.isEnabled](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate/1639520-isenabled)Added [SFErrorDomain [enum]](https://developer.apple.com/documentation/safariservices/sferrorcode)Added [SFErrorDomain.loadingInterrupted](https://developer.apple.com/documentation/safariservices/sferror/code/loadinginterrupted)Added [SFErrorDomain.noAttachmentFound](https://developer.apple.com/documentation/safariservices/sferror/code/noattachmentfound)Added [SFErrorDomain.noExtensionFound](https://developer.apple.com/documentation/safariservices/sferror/code/noextensionfound)Added [SFSafariApplication](https://developer.apple.com/documentation/safariservices/sfsafariapplication)Added [SFSafariApplication.getActiveWindow(completionHandler: (SFSafariWindow?) -> Swift.Void) [class]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639497-getactivewindow)Added [SFSafariApplication.openWindow(with: URL, completionHandler: ( (SFSafariWindow?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639493-openwindowwithurl)Added [SFSafariApplication.setToolbarItemsNeedUpdate() [class]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639521-settoolbaritemsneedupdate)Added [SFSafariApplication.showPreferencesForExtension(withIdentifier: String, completionHandler: ( (Error?) -> Swift.Void)?) [class]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/2202266-showpreferencesforextension)Added [SFSafariExtensionHandler](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandler)Added [SFSafariExtensionHandling](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling)Added [SFSafariExtensionHandling.contextMenuItemSelected()](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639488-contextmenuitemselected)Added [SFSafariExtensionHandling.messageReceived()](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639500-messagereceived)Added [SFSafariExtensionHandling.popoverDidClose(in: SFSafariWindow)](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639491-popoverdidclose)Added [SFSafariExtensionHandling.popoverViewController() -> SFSafariExtensionViewController](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1690338-popoverviewcontroller)Added [SFSafariExtensionHandling.popoverWillShow(in: SFSafariWindow)](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639502-popoverwillshowinwindow)Added [SFSafariExtensionHandling.toolbarItemClicked(in: SFSafariWindow)](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639511-toolbaritemclickedinwindow)Added [SFSafariExtensionHandling.validateToolbarItem(in: SFSafariWindow, validationHandler: (Bool, String) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639492-validatetoolbaritem)Added [SFSafariExtensionManager](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager)Added [SFSafariExtensionManager.getStateOfSafariExtension(withIdentifier: String, completionHandler: (SFSafariExtensionState?, Error?) -> Swift.Void) [class]](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/2122754-getstateofsafariextension)Added [SFSafariExtensionState](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate)Added [SFSafariExtensionState.isEnabled](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate/2122752-isenabled)Added [SFSafariExtensionViewController](https://developer.apple.com/documentation/safariservices/sfsafariextensionviewcontroller)Added [SFSafariPage](https://developer.apple.com/documentation/safariservices/sfsafaripage)Added [SFSafariPage.dispatchMessageToScript(withName: String, userInfo: [String : Any]?)](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639519-dispatchmessagetoscriptwithname)Added [SFSafariPage.getPropertiesWithCompletionHandler(_: (SFSafariPageProperties?) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639510-getpagepropertieswithcompletionh)Added [SFSafariPage.reload()](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639486-reload)Added [SFSafariPageProperties](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties)Added [SFSafariPageProperties.isActive](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638101-isactive)Added [SFSafariPageProperties.title](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638102-title)Added [SFSafariPageProperties.url](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638098-url)Added [SFSafariPageProperties.usesPrivateBrowsing](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638100-usesprivatebrowsing)Added [SFSafariTab](https://developer.apple.com/documentation/safariservices/sfsafaritab)Added [SFSafariTab.activate(completionHandler: ( () -> Swift.Void)?)](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639503-activate)Added [SFSafariTab.getActivePage(completionHandler: (SFSafariPage?) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639489-getactivepage)Added [SFSafariTab.getPagesWithCompletionHandler(_: ([SFSafariPage]?) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639496-getpageswithcompletionhandler)Added [SFSafariToolbarItem](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem)Added [SFSafariToolbarItem.setEnabled(_: Bool, withBadgeText: String?)](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/1639522-setenabled)Added [SFSafariWindow](https://developer.apple.com/documentation/safariservices/sfsafariwindow)Added [SFSafariWindow.getActiveTab(completionHandler: (SFSafariTab?) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639515-getactivetabwithcompletionhandle)Added [SFSafariWindow.getToolbarItem(completionHandler: (SFSafariToolbarItem?) -> Swift.Void)](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639509-gettoolbaritemwithcompletionhand)Added [SFSafariWindow.openTab(with: URL, makeActiveIfPossible: Bool, completionHandler: ( (SFSafariTab?) -> Swift.Void)?)](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639498-opentab)Added [SFErrorDomain](https://developer.apple.com/documentation/safariservices/sferrordomain)Added SFSafariServicesAvailable() -> Bool

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
