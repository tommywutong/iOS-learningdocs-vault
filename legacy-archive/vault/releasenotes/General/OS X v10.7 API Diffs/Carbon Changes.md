---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Carbon.html
archived_at: '2026-07-18T02:54:26.403008Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Carbon Changes

## Carbon

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

Appearance.hRemoved kThemeWidgetABoxRemoved kThemeWidgetBBoxRemoved kThemeWidgetBOffBoxAdded kThemeWidgetToolbarButtonCarbonEvents.hAdded kEventParamDirectionInvertedAdded kEventWindowFullScreenEnterCompletedAdded kEventWindowFullScreenEnterStartedAdded kEventWindowFullScreenExitCompletedAdded kEventWindowFullScreenExitStartedAdded kEventWindowGetFullScreenContentSizeAdded kEventWindowRestoredAfterRelaunchAdded kHICommandCloseAllAdded kHICommandQuitAndKeepWindowsControls.hRemoved AuxCtlHandle (no architecture available)Removed AuxCtlPtr (no architecture available)Removed AuxCtlRec (no architecture available)Removed ControlRecord (no architecture available)Dialogs.hRemoved DialogPeek (no architecture available)Removed DialogRecord (no architecture available)HIGeometry.hModified HIGetScaleFactor()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ICAApplication.hModified ICACopyObjectData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerGetParameters()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAShowDeviceBrowser()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerOpenSession()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICACopyObjectThumbnail()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICASendNotification()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerStatus()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICALoadDeviceModule()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAObjectSendMessage()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICARegisterForEventNotification()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICADownloadFile()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAUploadFile()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerInitialize()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerSetParameters()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAOpenSession()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerStart()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICACloseSession()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAImportImage()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICACopyObjectPropertyDictionary()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAScannerCloseSession()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICASendNotificationAndWaitForReply()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAGetDeviceList()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICAUnloadDeviceModule()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ICADevice.hModified ICDNewObject()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ICDDisposeObject()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

IMKInputSession.hAdded -[IMKTextInput firstRectForCharacterRange:actualRange:]Added -[IMKTextInput stringFromRange:actualRange:]Added -[IMKTextInput uniqueClientIdentifierString]MacApplication.hAdded kUIOptionAnimateMenuBarMacWindows.hRemoved AuxWinHandle (no architecture available)Removed AuxWinPtr (no architecture available)Removed AuxWinRec (no architecture available)Removed CWindowPeek (no architecture available)Removed CWindowRecord (no architecture available)Removed WindowPeek (no architecture available)Removed WindowRecord (no architecture available)Added HIWindowIsFullScreen()Added HIWindowToggleFullScreen()Added kHIWindowBitFullScreenAuxiliaryAdded kHIWindowBitFullScreenPrimaryModified HIWindowGetScaleMode()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified HIWindowSetDepth()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Menus.hRemoved MenuInfo (no architecture available)Removed MenuPtr (no architecture available)NSL.hRemoved DisposeNSLEventUPP()Removed DisposeNSLURLFilterUPP()Removed InvokeNSLEventUPP()Removed InvokeNSLURLFilterUPP()Removed [NSLDialogOptionFlags](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngei2lbnrxwot3qoruw63sgnrqwo4y)Removed [NSLDialogOptions](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngei2lbnrxwot3qoruw63tt)Removed [NSLEventProcPtr](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL33.md#apple-f4xwc4dqnrsv64tfmyxwgl3umrswml2okngek5tfnz2fa4tpmnihi4q)Removed NSLEventUPPRemoved [NSLFreeURL()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngem4tfmvkveta)Removed [NSLGetDefaultDialogOptions()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngeozluirswmylvnr2ei2lbnrxwot3qoruw63tt)Removed NSLSaveURLAliasToFolder()Removed [NSLStandardGetURL()](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/NSL32.md#apple-f4xwc4dqnrsv64tfmyxwgl3govxggl2okngfg5dbnzsgc4tei5sxivksjq)Removed NSLURLFilterProcPtrRemoved NSLURLFilterUPPRemoved NewNSLEventUPP()Removed NewNSLURLFilterUPP()Removed kNSLAddServiceTypesRemoved kNSLClientHandlesRecentsRemoved [kNSLDefaultNSLDlogOptions](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mirswmylvnr2e4u2mirwg6z2pob2gs33oom)Removed [kNSLNoURLTEField](../../../documentation/Networking/Network%20Services%20Location%20Manager%20%28Legacy%29/Network%20Services%20Location%20Manager%20Constants.md#apple-f4xwc4dqnrsv64tfmyxwgl3fmnxw443uf5vu4u2mjzxvkusmkrcum2lfnrsa)

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
