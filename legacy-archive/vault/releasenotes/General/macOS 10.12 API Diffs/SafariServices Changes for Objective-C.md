---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/SafariServices.html
archived_at: '2026-07-18T02:50:45.056066Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# SafariServices Changes for Objective-C

### SafariServices (Added)

#### SFContentBlockerManager.h (Added)

Added [SFContentBlockerManager](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager)Added [+[SFContentBlockerManager getStateOfContentBlockerWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1639499-getstateofcontentblocker)Added [+[SFContentBlockerManager reloadContentBlockerWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfcontentblockermanager/1620151-reloadcontentblocker)

#### SFContentBlockerState.h (Added)

Added [SFContentBlockerState](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate)Added [SFContentBlockerState.enabled](https://developer.apple.com/documentation/safariservices/sfcontentblockerstate/1639520-enabled)

#### SFError.h (Added)

Added [SFErrorCode](https://developer.apple.com/documentation/safariservices/sferrorcode)Added [SFErrorDomain](https://developer.apple.com/documentation/safariservices/sferrordomain)Added [SFErrorLoadingInterrupted](https://developer.apple.com/documentation/safariservices/sferror/code/loadinginterrupted)Added [SFErrorNoAttachmentFound](https://developer.apple.com/documentation/safariservices/sferrorcode/sferrornoattachmentfound)Added [SFErrorNoExtensionFound](https://developer.apple.com/documentation/safariservices/sferrorcode/sferrornoextensionfound)

#### SFFoundation.h (Added)

Added #def SF_AVAILABLE_MAC_SAFARIAdded #def SF_AVAILABLE_MAC_SAFARI_10_0Added #def SF_CLASS_AVAILABLE_MAC_SAFARIAdded #def SF_CLASS_AVAILABLE_MAC_SAFARI_10_0Added #def SF_ENUM_AVAILABLE_MAC_SAFARIAdded #def SF_ENUM_AVAILABLE_MAC_SAFARI_10_0Added #def SF_EXTERN

#### SFSafariApplication.h (Added)

Added [SFSafariApplication](https://developer.apple.com/documentation/safariservices/sfsafariapplication)Added [+[SFSafariApplication getActiveWindowWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639497-getactivewindowwithcompletionhan)Added [+[SFSafariApplication openWindowWithURL:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639493-openwindowwithurl)Added [+[SFSafariApplication setToolbarItemsNeedUpdate]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/1639521-settoolbaritemsneedupdate)Added [+[SFSafariApplication showPreferencesForExtensionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariapplication/2202266-showpreferencesforextension)

#### SFSafariExtensionHandler.h (Added)

Added [SFSafariExtensionHandler](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandler)

#### SFSafariExtensionHandling.h (Added)

Added [SFSafariExtensionHandling](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling)Added [-[SFSafariExtensionHandling contextMenuItemSelectedWithCommand:inPage:userInfo:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639488-contextmenuitemselected)Added [-[SFSafariExtensionHandling messageReceivedWithName:fromPage:userInfo:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639500-messagereceived)Added [-[SFSafariExtensionHandling popoverDidCloseInWindow:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639491-popoverdidcloseinwindow)Added [-[SFSafariExtensionHandling popoverViewController]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1690338-popoverviewcontroller)Added [-[SFSafariExtensionHandling popoverWillShowInWindow:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639502-popoverwillshow)Added [-[SFSafariExtensionHandling toolbarItemClickedInWindow:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639511-toolbaritemclickedinwindow)Added [-[SFSafariExtensionHandling validateToolbarItemInWindow:validationHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/1639492-validatetoolbariteminwindow)

#### SFSafariExtensionManager.h (Added)

Added [SFSafariExtensionManager](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager)Added [+[SFSafariExtensionManager getStateOfSafariExtensionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariextensionmanager/2122754-getstateofsafariextension)

#### SFSafariExtensionState.h (Added)

Added [SFSafariExtensionState](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate)Added [SFSafariExtensionState.enabled](https://developer.apple.com/documentation/safariservices/sfsafariextensionstate/2122752-enabled)

#### SFSafariExtensionViewController.h (Added)

Added [SFSafariExtensionViewController](https://developer.apple.com/documentation/safariservices/sfsafariextensionviewcontroller)

#### SFSafariPage.h (Added)

Added [SFSafariPage](https://developer.apple.com/documentation/safariservices/sfsafaripage)Added [-[SFSafariPage dispatchMessageToScriptWithName:userInfo:]](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639519-dispatchmessagetoscriptwithname)Added [-[SFSafariPage getPagePropertiesWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639510-getpropertieswithcompletionhandl)Added [-[SFSafariPage reload]](https://developer.apple.com/documentation/safariservices/sfsafaripage/1639486-reload)

#### SFSafariPageProperties.h (Added)

Added [SFSafariPageProperties](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties)Added [SFSafariPageProperties.active](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638101-isactive)Added [SFSafariPageProperties.title](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638102-title)Added [SFSafariPageProperties.url](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638098-url)Added [SFSafariPageProperties.usesPrivateBrowsing](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties/1638100-usesprivatebrowsing)

#### SFSafariTab.h (Added)

Added [SFSafariTab](https://developer.apple.com/documentation/safariservices/sfsafaritab)Added [-[SFSafariTab activateWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639503-activate)Added [-[SFSafariTab getActivePageWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639489-getactivepage)Added [-[SFSafariTab getPagesWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafaritab/1639496-getpageswithcompletionhandler)

#### SFSafariToolbarItem.h (Added)

Added [SFSafariToolbarItem](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem)Added [-[SFSafariToolbarItem setEnabled:withBadgeText:]](https://developer.apple.com/documentation/safariservices/sfsafaritoolbaritem/1639522-setenabled)

#### SFSafariWindow.h (Added)

Added [SFSafariWindow](https://developer.apple.com/documentation/safariservices/sfsafariwindow)Added [-[SFSafariWindow getActiveTabWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639515-getactivetab)Added [-[SFSafariWindow getToolbarItemWithCompletionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639509-gettoolbaritemwithcompletionhand)Added [-[SFSafariWindow openTabWithURL:makeActiveIfPossible:completionHandler:]](https://developer.apple.com/documentation/safariservices/sfsafariwindow/1639498-opentab)

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
