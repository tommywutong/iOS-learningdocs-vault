---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Introduction/Intro.html
archived_at: '2026-07-18T03:18:44.588847Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](PackagedDocument-main.m.md)

# Packaged Document for OS X

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2017-03-09 Upgraded to macOS 10.12 SDK, removed some compiler warnings, upgraded to use the modern Objective-C syntax, now uses Storyboard. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteojvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | macOS 10.12 SDK or later |
| __Runtime Requirements:__ | OS X 10.10 or later, an iCloud account |

"PackagedDocument" is a text editing application for opening, editing and saving packaged documents using NSDocument and NSFileWrapper. It is also equipped to demonstrate how to save packaged documents to iCloud.

File Format and NSFileWrapper: Choices you make in designing your document format can impact network transfer performance to and from iCloud for your app’s documents. The most important choice is to be sure to use a file package for your document format. If your document data format consists of multiple distinct pieces, use a file package for your document file format. A file package, which you access by way of an NSFileWrapper object, lets you store the elements of a document as individual files and folders that can be read and written separately—while still appearing to the user as a single file. The iCloud upload and download machinery makes use of this factoring of content within a file package; only changed elements are uploaded or downloaded.

Three distinctive components of the document format: This sample demonstrates the use of NSFileWrapper by writing three distinctive files: text, image and plist files. Each document window allows the user to add text and an image. The plist file is used as an internal metadata file used to hold misc information about that document, in particular the disclosure state of the image section of the window. It writes and reads the plist file using NSPropertyListSerialization.

[Next](PackagedDocument-main.m.md)

