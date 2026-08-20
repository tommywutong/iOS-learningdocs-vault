---
title: 'Inside Macintosh: Processes Errata'
apple_id: DTS10002526
resource_type: Technical Note
platform: macOS
topic: null
technology: null
published: '1994-10-01'
source_url: https://developer.apple.com/library/archive/technotes/im_errata/im_errata_06.html
archived_at: '2026-07-26T19:53:37.476163Z'
---
> 导航：[总目录](../../../README.md) · [technotes](../../../_indexes/technotes.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Notes](https://developer.apple.com/library/archive/technicalnotes/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalnotes/LegacyTechnologies/idxCarbon-date.html) >

# Legacy Document[close button](javascript:closeWatermark())

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Carbon > Process Management](https://developer.apple.com/referencelibrary/Carbon/idxProcessManagement-date.html)

|  |
| --- |
| Technical Note IMERRATA06Inside Macintosh: Processes Errata |

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | |  | | --- | | images/tnmenutop.gif | | CONTENTS | | [Topics](#)   [Chapter 1 - Introduction to Processes and Tasks](#)   [Chapter 4 - Vertical Retrace Manager](#)   [Chapter 6 - Deferred Task Manager](#)   [Chapter 8 - Shutdown Manager](#)   [Glossary](#)    [References](#)   [Downloadables](#) | | images/tnmenubottom.gif | | This Technical Note discusses known errors and omissions in _Inside Macintosh: Processes_.  [Oct 01 1994] |       ---      Topics  - Correction to Figure 1-1 October 1994 - Clarification of Installing Persistent VBL Tasks October 1994 - Clarification of `GetVBLQHdr` October 1994 - Clarification of Interrupt Priorities During VBL Tasks October 1994 - Correction to Listing 8-1 October 1994 - Correction to Glossary Entry October 1994   [Back to top](#) Chapter 1 - Introduction to Processes and TasksCorrection to Figure 1-1 Page 1-4, The Cooperative Multitasking Environment  Figure 1-1 shows the wrong application icon in the menu bar. The SurfWriter icon should be in the menu bar labeling the application menu, not the Finder icon.  [Back to top](#) Chapter 4 - Vertical Retrace ManagerClarification of Installing Persistent VBL Tasks Page 4-20, Installing a Persistent VBL Task  The description of installing a persistent VBL task is partly incorrect. The documentation states that "if you want to install a persistent system-based VBL task, you need to load its VBL task record into the system partition." This is incorrect, and it is not what is demonstrated in Listing 4-15. Listing 4-15 shows how to put the VBL task _code_ (or enough of it to fool the Vertical Retrace Manager) into the system partition.  However, Listing 4-15 needs a call to `FlushInstructionCache` added immediately before the call to `VInstall`. In addition, it is preferable to code the error-handling part of Listing 4-15 like this:   |  | | --- | | ``` SysHeapPtr := NewPtrSys(kJMPSize); IF SysHeapPtr = NIL THEN     BEGIN         InstallPersistentVBL := MemError;         Exit(InstallPersistentVBL );     END;  ``` |  Clarification of GetVBLQHdr Page 4-28  `GetVBLQHdr` returns a pointer to the head of the VBL queue. One of the bits of the `qFlags` field of the VBL queue header indicates whether a VBL task is currently executing. The correct bit is bit 6 of the _first_ byte of the `qFlags` field, or bit 14 of the entire two-byte field. Versions of A/UX prior to 3.1 incorrectly used bit 6 of the entire two-byte field.  [Back to top](#) Chapter 6 - Deferred Task ManagerClarification of Interrupt Priorities During VBL Tasks Pages 6-3, 6-5, About the Deferred Task Manager  The documentation states "If the current application is then interrupted by a vertical retrace interrupt, the interrupt priority is set to 1 during the servicing of the interrupt and restored to 0 upon completion." This is not strictly correct. T he Vertical Retrace Manager actually restores the interrupt mask to 0 before running VBL tasks. As a result, VBL tasks can be interrupted by future level-1 interrupts, although a VBL task cannot interrupt another VBL task.  On page 6-5, the documentation states "Suppose that your application installs and activates a Time Manager task, which is triggered by level-2 interrupts." Actually, Time Manager interrupts are level-1 interrupts.  Also on page 6-5, there is occasional mention of the status register being restored to 0. In fact, only three bits of the status register (the processor priority level) are restored to 0. All other bits are unchanged.  [Back to top](#) Chapter 8 - Shutdown ManagerCorrection to Listing 8-1 Page 8-8, Sending a Shutdown or Restart Event  Listing 8-1 on page 8-8 contains several errors. The constant `kFinderSig` should be defined to be '`MACS'`. In addition, that constant cannot be passed directly to the `AECreateDesc` function. Instead, you must declare a variable of type `OSType` and assign `kFinderSig` to it, as follows:   |  | | --- | | ``` CONST     kFinderSig = 'MACS'; VAR     ...     signature: OSType BEGIN     signature := kFinderSig;     myErr := AECreateDesc(typeApplSignature, @signature, ...);     ...  ``` |   [Back to top](#) GlossaryCorrection to Glossary Entry Page GL-2  The entry __interrupt handle__ should be __interrupt handler.__  [Back to top](#) References _Inside Macintosh: Processes_  [Back to top](#)   Downloadables  |  |  |  | | --- | --- | --- | | Acrobat gif | Acrobat version of this Note (40K) | [Download](https://developer.apple.com/library/archive/technotes/im_errata/pdf/im_errata_06.pdf) |    [Back to top](#) |

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
