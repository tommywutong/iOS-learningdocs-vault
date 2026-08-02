---
title: Using Temporary Memory with OpenPicture
apple_id: DTS10001779
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1996-02-01'
source_url: https://developer.apple.com/library/archive/qa/qd/qd20.html
archived_at: '2026-07-18T02:38:36.433498Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Graphics & Imaging](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxGraphicsImaging-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Graphics & Imaging](https://developer.apple.com/referencelibrary/GraphicsImaging/index.html)

|  |
| --- |
| Technical Q&A QD20Using Temporary Memory with OpenPicture |

|  |
| --- |
| ---   Q: I use the `OpenPicture`, draw, `ClosePicture` sequence to create a picture handle. Since the handle can be quite large, and since I dispose of it fairly quickly, it would make sense to allocate it in temporary memory. But I haven't found any reasonable way to do that. Any suggestions? Both these situations arise because my application runs in a fairly small (800K) partition. I do this so that other applications have adequate space to work with it, since one of my main functions is to interact with other applications using Apple events. However, I occasionally need more memory for a few seconds at a time.  A: There are two ways to cause `OpenPicture` to use temporary memory. A simple way to do it is to allocate a block of temporary memory, then create a new heap zone in that block and make it the current zone just before you call `OpenPicture`. This will cause subsequent memory allocations to happen in your temporary block, and will work fine.  Another way is to replace the `putPicProc`, as is commonly done when spooling a picture to disk, and instead spool it to temporary memory.  You create a handle in temporary memory the size of a picture and fill in its size and `picFrame` fields so that it looks like a normal picture handle. In your `putPicProc` you copy the data in, continually resizing the handle if necessary to fit the data. After you call `ClosePicture`, remove your `putPicProc`; then you can use the temporary handle just like a normal picture.  The advantage of this method over the first one is that you can make the picture as large as temporary memory will let you, and you end up using just enough memory. The first technique, while technically easier to implement, limits you to the size of the heap you initially create, and you also may use a lot more temporary memory than you need. If you're able to come up with a good guess of how large your pictures are going to be, use the first technique; if not, use the second one. See _Inside Macintosh: Memory_ for more information about creating heap zones.  If you're not familiar with picture spooling, see _Inside Macintosh Volume V_, page 89, which has code for spooling a picture to disk as it's created. This is the same technique as documented there, only it spools the picture to temporary memory instead. |

#### [Sep 15 1995]

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
