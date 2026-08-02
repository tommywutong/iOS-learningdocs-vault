---
title: File Wrappers with Core Data Documents
apple_id: DTS40008763
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreData
published: '2009-04-29'
source_url: https://developer.apple.com/library/archive/samplecode/PersistentDocumentFileWrappers/Introduction/Intro.html
archived_at: '2026-07-18T03:18:48.407543Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# File Wrappers with Core Data Documents

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-04-29 This sample demonstrates how directory file wrappers can be used with NSPersistentDocument. |
| __Build Requirements:__ | Xcode Tools 3.0 and Mac OS X Version 10.5 |
| __Runtime Requirements:__ | Mac OS X Version 10.5 |

A directory file wrapper allows you to adopt a package format for your documents. Document packages give the illusion of a single document to users but provide you with more flexibility in how you store the document data internally. The standard implementation of NSPersistentDocument does not support this functionality, but it may be useful for some Core Data Documents to be able to use a package format. For example, it may be preferable to store image data as separate files rather than embedding that data in the persistent store.

[Next](ReadMe.txt.md)

