---
title: The header file 'alut.h' is missing from the OpenAL framework.
apple_id: DTS10004191
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: OpenAL
published: '2014-02-06'
source_url: https://developer.apple.com/library/archive/qa/qa1504/_index.html
archived_at: '2026-07-18T02:31:39.766157Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1504

# The header file 'alut.h' is missing from the OpenAL framework.

## Q:  Why does the compiler complain that the header file can't be found?

A: Why does the compiler complain that the header file can't be found?

As of Mac OS X 10.4.7, the OpenAL framework has been updated to version 1.1 of the OpenAL specification. The OpenAL framework now strictly conforms to the OpenAL specification and since ALUT is not an official part of the specification it will no longer be included as part of the OpenAL framework. The ALUT header files were removed as of the Xcode 2.4 update.

If you require ALUT functionality, Creative offers a new standalone library that is being developed under a separate specification. The freealut library includes source code and should be buildable on OS X. However, the freeault library defines the same symbol names as the OpenAL 1.0 ALUT declarations and you will need to rename these symbols or use compiler preprocessing macros to resolve the conflict this causes.

- [CoreAudio Documentation](https://developer.apple.com/documentation/MusicAudio/CoreAudio-date.html)
- [CoreAudio Mailing List](http://lists.apple.com/mailman/listinfo/coreaudio-api)
- [OpenAL web site](http://www.openal.org/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-02-06 | Removed link to openAL.org website. |
| 2007-02-06 | New document that aLUT headers were removed from OpenAL.framework with the Xcode 2.4. This Q&A describes how to regain access to those system-supplied symbols |

