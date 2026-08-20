---
title: Remote or Two-Machine Debugging Applications with GDB
apple_id: DTS10002318
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1279.html
archived_at: '2026-07-18T02:38:30.678627Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Tools](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxTools-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Tools > Compiling & Debugging](https://developer.apple.com/referencelibrary/DeveloperTools/idxCompilersDebuggers-date.html)

|  |
| --- |
| Technical Q&A QA1279Remote or Two-Machine Debugging Applications with GDB |

|  |  |  |
| --- | --- | --- |
| ---   Q: I cannot use GDB to debug my application because it interferes with the code that I'm trying to debug, what can I do?  A: You may experience this situation if you try to debug, for example, a drag and drop operation between two applications, a complex activate / deactivate / update case, or an application which grabs the entire screen (this is not an exhaustive list). In those situations, the window displaying GDB (whether in Project Builder or in Terminal) will interfere with the code that you want to debug. A very good solution to that problem is to do two-machine debugging, aka remote debugging: you just need another Macintosh and have both machines connected to the same network.    You will debug the target Macintosh through GDB that you will use within the Terminal application on the Macintosh in control. It may be easier, in the future, to use GDB within Xcode on the Macintosh in control, but it is currently impractical.  1) On the target Macintosh, which contains the application or applications to debug, you enable "Remote Login" by using the "Sharing" pane of the System Preferences. When you turn that service on, a message will appear giving you the command line information you need in order to connect (ie. type "ssh yourname@yournetwork.com")       |  | | --- | | __Note:__  You could also just use "ssh xx.xx.xx.xx" if you know the IP address of the target Macintosh. |      2) On the Macintosh in control, you launch the Terminal application and open as many windows as there are applications to debug (two in the drag and drop scenario, one in the others).  3) In each window, you first ssh to the target Macintosh by typing the command line information you got in the Sharing pane (you will be asked the password associated with that user), and then, you launch GDB (the GDB tool launched is the one on the target machine) and either run the application or attach to its pid (please, read the GDB manual for more details). You can also use the symbols files of the application[s] you need to debug (again read the GDB manual for more details).       |  | | --- | | __Note:__  If you have two windows, each running GDB, it's advisable to tile them so that you can see both of them at the same time in order to easily notice breakpoints interrupts or messages from either application. |      4) After you're done debugging, don't forget to quit GDB, quit Terminal, and, if you no longer have a need for it, disable the Remote Login service on the target Macintosh.   ---  [Sep 09, 2003] |

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
