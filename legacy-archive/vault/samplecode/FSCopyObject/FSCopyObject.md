---
title: FSCopyObject
apple_id: DTS10000472
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: CoreServices
published: '2004-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/FSCopyObject/Introduction/Intro.html
archived_at: '2026-07-18T03:08:06.988801Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# FSCopyObject

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2004-03-19 Fixed issue where a zero length object would be created when the current user did not have proper permissions to the source object or when there was not enough disk space to create the new object object |
| __Build Requirements:__ | Xcode, ProjectBuilder or CodeWarrior |
| __Runtime Requirements:__ | Mac OS 9 and Mac OS X |

Contains source to demonstrate how to copy/delete files and folders with HFS+ APIs. It also demonstrates a technique to rename an object if an object of the same name exists in the destination.

This sample shows how to perform these operations in an MP-safe way.

[Next](ReadMe.txt.md)

