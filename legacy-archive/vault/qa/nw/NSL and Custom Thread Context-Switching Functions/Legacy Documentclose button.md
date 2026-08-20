---
title: NSL and Custom Thread Context-Switching Functions
apple_id: DTS10001477
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-01-31'
source_url: https://developer.apple.com/library/archive/qa/nw/nw65.html
archived_at: '2026-07-18T02:29:47.892976Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW65NSL and Custom Thread Context-Switching Functions |

|  |
| --- |
| ---   Q: I'm working on an application that uses both the Thread Manager and the Network Services Library (NSL) Manager. When the app quits, it crashes. What could be causing this?  A: Once NSL is initialized either through `NSLOpenNavigationAPI` or internally through a call to `NSLStandardGetURL,` NSL and the SLP plug-in start several threads for their own use. These threads do not go away when `NSCloseNavigationAPI` is called; instead, they wait for the CFM termination routine to be invoked. The CFM termination routines are called when the libraries are being unloaded, which, for a standard application linked against the NSL shared library NSLPPCLib, is after the application has disposed all of its data and exited its `main`function.  The issue arises if the application uses the Thread Manager function `SetThreadSwitcher` to install custom inner and outer context-switching functions on the main thread. When the application is exiting it typically disposes of all of its threads and any internal data structures that refer to these threads. The main thread still exists (it's still running), but the application's internal references to it are gone.  After the app exits `main` the NSL/SLP termination routine disposes of its threads. This causes the app's outer context-switching function to be invoked for the main thread. If this function assumes that its internal data structure referring to this thread is still present, the scene is set for a crash. Two possible workarounds are for the application at exit time to:   - set the context-switching functions to   `NULL` or - not dispose of any internal data structures used by   the outer context-switching function that refer to the   main thread.   An example of this issue can be found in the PowerPlant framework from Metrowerks. The PowerPlant `LThread` class installs inner and outer context-switching functions on the main thread. When a PowerPlant application exits, it disposes of all of its threads and their respective `LThread` objects. Then the NSL/SLP termination routine disposes of its threads. This causes the app's main outer context-switching function to be called and crash since its cover `LThread` instance is already gone. There are two PowerPlant fixes that can be applied:   - in `ExitThreads` set the context-switching   functions to `NULL` - in `ExitThreads` do not dispose of the   main `LThread`.   This issue may be resolved in a future version of NSL [2425291] but you will need to use one of these workarounds on current systems. |

#### [Jan 31 2000]

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

---
