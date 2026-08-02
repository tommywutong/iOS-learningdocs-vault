---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Carbon.html
archived_at: '2026-07-18T02:54:11.042483Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Carbon Changes

## Carbon

ASRegistry.hAdded cDynamicLibraryAdded cFrameworkAdded cScriptingAdditionAdded kASExcludingAdded kASImportingAdded kASMinimumVersionAdded kASUseEventCodeAdded pASRequiredImportItemsHTMLRendering.hRemoved DisposeHRNewCFURLUPP()Removed DisposeHRNewURLUPP()Removed DisposeHRURLToFSRefUPP()Removed DisposeHRURLToFSSpecUPP()Removed DisposeHRWasCFURLVisitedUPP()Removed DisposeHRWasURLVisitedUPP()Removed HRActivate()Removed HRDeactivate()Removed HRDisposeReference()Removed HRDraw()Removed HRDrawInPort()Removed HRForceQuickdraw()Removed HRFreeMemory()Removed HRGetBaseURL()Removed HRGetBaseURLAsCFString()Removed HRGetHTMLFile()Removed HRGetHTMLFileAsFSRef()Removed HRGetHTMLRenderingLibVersion()Removed HRGetHTMLURL()Removed HRGetHTMLURLAsCFURL()Removed HRGetRenderedImageSize()Removed HRGetRenderedImageSize32()Removed HRGetRootURL()Removed HRGetRootURLAsCFString()Removed HRGetTitle()Removed HRGetTitleAsCFString()Removed HRGoToAnchor()Removed HRGoToAnchorCFString()Removed HRGoToCFURL()Removed HRGoToData()Removed HRGoToFSRef()Removed HRGoToFile()Removed HRGoToPtr()Removed HRGoToURL()Removed HRHTMLRenderingLibAvailable()Removed HRIsHREvent()Removed HRNewCFURLProcPtrRemoved HRNewCFURLUPPRemoved HRNewReference()Removed HRNewReferenceInWindow()Removed HRNewURLProcPtrRemoved HRNewURLUPPRemoved HRReferenceRemoved HRRegisterNewCFURLUPP()Removed HRRegisterNewURLUPP()Removed HRRegisterURLToFSRefUPP()Removed HRRegisterURLToFSSpecUPP()Removed HRRegisterWasCFURLVisitedUPP()Removed HRRegisterWasURLVisitedUPP()Removed HRScreenConfigurationChanged()Removed HRScrollToImageLocation32()Removed HRScrollToLocation()Removed HRScrollbarStateRemoved HRSetDrawBorder()Removed HRSetEmbeddingControl()Removed HRSetGrafPtr()Removed HRSetGrowboxCutout()Removed HRSetRenderingRect()Removed HRSetScrollbarState()Removed HRSetWindowRef()Removed HRURLToFSRefProcPtrRemoved HRURLToFSRefUPPRemoved HRURLToFSSpecProcPtrRemoved HRURLToFSSpecUPPRemoved HRUnregisterNewCFURLUPP()Removed HRUnregisterNewURLUPP()Removed HRUnregisterURLToFSRefUPP()Removed HRUnregisterURLToFSSpecUPP()Removed HRUnregisterWasCFURLVisitedUPP()Removed HRUnregisterWasURLVisitedUPP()Removed HRUtilCreateFullCFURL()Removed HRUtilCreateFullURL()Removed HRUtilGetFSRefFromURL()Removed HRUtilGetFSSpecFromURL()Removed HRUtilGetURLFromFSRef()Removed HRUtilGetURLFromFSSpec()Removed HRWasCFURLVisitedProcPtrRemoved HRWasCFURLVisitedUPPRemoved HRWasURLVisitedProcPtrRemoved HRWasURLVisitedUPPRemoved InvokeHRNewCFURLUPP()Removed InvokeHRNewURLUPP()Removed InvokeHRURLToFSRefUPP()Removed InvokeHRURLToFSSpecUPP()Removed InvokeHRWasCFURLVisitedUPP()Removed InvokeHRWasURLVisitedUPP()Removed NewHRNewCFURLUPP()Removed NewHRNewURLUPP()Removed NewHRURLToFSRefUPP()Removed NewHRURLToFSSpecUPP()Removed NewHRWasCFURLVisitedUPP()Removed NewHRWasURLVisitedUPP()Removed URLSourceTypeRemoved eHRScrollbarAutoRemoved eHRScrollbarOffRemoved eHRScrollbarOnRemoved kHRLookingForEmbeddedRemoved kHRLookingForFrameRemoved kHRLookingForHTMLSourceRemoved kHRLookingForImageRemoved kHRLookingForImageMapRemoved kHRRendererHTML32TypeICAApplication.hAdded kICASandboxViolationSecCertificateSupport.hModified SecChooseIdentity()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified SecChooseIdentityAsSheet()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified SecDisplayCertificate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified SecDisplayCertificateGroup()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified SecEditTrust()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified SecEditTrustAsSheet()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

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
