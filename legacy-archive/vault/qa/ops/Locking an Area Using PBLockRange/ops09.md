---
title: Locking an Area Using PBLockRange
apple_id: DTS10001490
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-05-14'
source_url: https://developer.apple.com/library/archive/qa/ops/ops09.html
archived_at: '2026-07-18T02:29:49.363186Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Carbon](https://developer.apple.com/library/archive/technicalqas/Carbon/index.html) > [File Management](https://developer.apple.com/library/archive/technicalqas/Carbon/idxFileManagement-date.html) >

|  |
| --- |
| Technical Q&A OPS09Locking an Area Using PBLockRange |

|  |
| --- |
| Q I'm locking a small area of a shared file, using PBLockRange, so others cannot write to it. When I try to _read_ the locked area from another machine (by calling FSRead), it returns a -45 (file locked) error. If I try to read over an unlocked area, it works fine. I've never used PBLockRange before, but all of the documentation on it (that I've found, anyway) says that the locking is for _writing_ not reading, and the documentation on FSRead never suggests that it might return a "file locked" error code. A PBLockRange is behaving properly in this situation, and has always behaved this way. The idea is that by locking a section of a file you want to control all access to the section. While the section is locked and you are making changes to it, other users should not be able to read the portion of the file that is changing. The information might not be properly synched with the changes made, so readers might be reading old information. By denying readers access to the locked portion of the file, you guarantee the integrity of the data to which readers have access. As page 2-50 of _Inside Macintosh: Files_ states:  "When a user needs to modify a portion of a file that has been opened with shared read/write permission, it is usually desirable to make that portion of the file unavailable to other users while the changes are made. You can call the PBLockRange function to lock a range of bytes before modifying the file and then PBUnlockRange to unlock that range after your changes are safely recorded in the file.  "Locking a range of bytes in a file gives the user exclusive read/write access to that range and makes it inaccessible to other users. Other users can neither write nor read the bytes in that range until you unlock it. If other users attempt to read data from a portion of a file that you have locked, they receive the fLckdErr result code." For a thorough description of working with files in a shared environment, see Technical Note [FL 37- "Want Permission to do What."](https://developer.apple.com/library/archive/technotes/fl/fl_37.html) Updated: 14-May-96 |

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
