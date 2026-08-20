---
title: Using Background Printing When The Finder Isn't Present
apple_id: DTS10001894
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-03-04'
source_url: https://developer.apple.com/library/archive/qa/qd/qd41.html
archived_at: '2026-07-18T02:38:37.635353Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Printing](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxPrinting-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Printing > Hardware & Drivers](https://developer.apple.com/referencelibrary/Printing/idxHardwareDrivers-date.html)

|  |
| --- |
| Technical Q&A QD41Using Background Printing When The Finder Isn't Present |

|  |  |
| --- | --- |
| ---   Q: Is there any way we can use background printing while the Finder is off?  A: Yes, it is possible to use background printing when the Finder isn't present.    |  | | --- | | __Note:__  This isn't officially supported, and the methods used are likely to change, so you'll want to check new versions of System software to make sure your application still works correctly. This is a hard thing to do, and will only become harder under Copland (if it is possible at all). Note also that there are third-party background-printing solutions which are not covered here. You'll need to work with the various third parties to solve compatibility problems with their products. |    Here's the approach, in three parts: A: Old print architecture, no desktop printing Your application needs to monitor the Print Monitor Documents folder within the System Folder. On older versions of system software, this folder is called Spool Folder. When you see a file within that folder, you can launch PrintMonitor and the file will be sent to the printer. B: Old print architecture, with desktop printing installed Before quitting the Finder, make sure desktop printers are all done printing (Any jobs currently in desktop printers stop when the Finder goes away). Once all DTPs are clear, follow the same steps as A. C: QuickDraw GX Watch the Print Monitor Documents folder, and launch PrinterShare GX. Make sure to handle any events it passes back to you, since these are error conditions and the user will need to be alerted. Since PrinterShare GX looks for the Finder by looking for a process whose ProcessType is '`FNDR`', you'll have to mimic that behavior. You can use the application AETracker to find out which events you will need to handle. (AETracker is available on the Developer CD Series in the Testing & Debugging folder on the ToolChest Edition.) |

#### [Mar 04 1996]

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
