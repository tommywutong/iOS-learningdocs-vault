---
title: Mounting a Remote File System
apple_id: DTS10001422
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-06-01'
source_url: https://developer.apple.com/library/archive/qa/nw/nw10.html
archived_at: '2026-07-18T02:29:44.383590Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Networking](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxNetworking-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Networking](https://developer.apple.com/referencelibrary/Networking/index.html)

|  |
| --- |
| Technical Q&A NW10Mounting a Remote File System |

|  |
| --- |
| ---   Q: I want to put a virtual 100-CD-ROM jukebox online. How can I mount an icon on the desktop that is associated with a remote file system? Is it possible to use the System 7 Pro catalog to do this in a way that would allow the catalog to be dynamic and to reflect my database of objects?  A: What you are really saying is that you want your virtual jukebox to be a network file system. You have two options, and which one you choose depends primarily on what you really want to do and how much work you want to put into it:  The first option is to create a remote disk driver. This would probably take two to three months to do, and you would be limited to read-only shared access.  Your other option is to create a Foreign File System. This would probably require six to eight months of work, but you would have read/write access.  Since your application is a CD-ROM jukebox, there is no need to maintain any coherency across writes, since there are no writes. There are many examples of how to write a RAM disk available, and you can create your driver by (basically) adding your network code to one of these (this approach also gives you a speed advantage).  If you need to share files (not disks), and you need to have read/write access and locking, you have no choice except to create a Foreign File System. This is a tremendous amount of work, as indicated by the following quote from the File System Manager guide:  "Important Note: Even though the File System Manager provides many services that simplify development of foreign file systems, developing a foreign file system is both a difficult and time-consuming process. A minimal foreign file system must implement over forty Macintosh file-system routines, while a networked, sharable file system has to implement as many as eighty Macintosh file-system routines."  To see the full text of this topic, see the __February 1995 Developer CD:__  __Feb 95:New System Software Extensions:File System Manager SDK__  Regardless of which option you choose, you should be aware that, with versions of the system software prior to System Update 3.0, mounting more than 20 volumes on the desktop crashes the system. Also, since the file system and the device manager both use 68K code (even on the PPC), you should consider compiling your application in 68K code, as this will eliminate a mode switch. |

#### [June 01 1995]

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
