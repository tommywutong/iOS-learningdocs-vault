---
title: CoreAudio PublicUtility - Installing the CARingBuffer Update
apple_id: DTS40009294
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/qa/qa1665/_index.html
archived_at: '2026-07-18T02:33:24.781200Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1665

# CoreAudio PublicUtility - Installing the CARingBuffer Update

## Q:  How do I install the updated CARingBuffer files?

A: How do I install the updated CARingBuffer files?

The __CARingBuffer__ class (`CARingBuffer.h` and `CARingBuffer.cpp`) implements an easy to use ring buffer object for storing and fetching Audio Buffer Lists and is part of the Core Audio Public Utility set of classes which comes with the Xcode developer tools package.

A bug fix update was made to the __CARingBuffer__ class which prevents a crash when handling out of bounds reads and removes unused code. This update is strongly recommended for all Core Audio developers using Xcode 3.2 (Mac OS X 10.6 and iPhone OS 3) or Xcode 3.1.4 (Mac OS X 10.5.x and iPhone OS 3).

To update this class on Mac OS X 10.6.x follow these steps:

- Download the attached CARingBufferUpdate archive.
- Expand the .zip containing both the `CARingBuffer.h` and `CARingBuffer.cpp` files.
- Move both files to `/Developer/Extras/CoreAudio/PublicUtility/` replacing the older files of the same name.

To update this class on Mac OS X 10.5.x follow these steps:

- Download the attached CARingBufferUpdate archive.
- Expand the .zip containing both the `CARingBuffer.h` and `CARingBuffer.cpp` files.
- Move both files to `/Developer/Examples/CoreAudio/PublicUtility/` replacing the older files of the same name.

- CARingBuffer Update ("qa1665_CARingBufferUpdate.zip", 7.1K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-10-09 | New document that contains the updated CARingBuffer class files for the PublicUtility folder. |

