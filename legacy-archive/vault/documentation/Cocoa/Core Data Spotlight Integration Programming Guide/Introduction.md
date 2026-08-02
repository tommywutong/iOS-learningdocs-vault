---
title: Core Data Spotlight Integration Programming Guide
apple_id: TP40008065
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreData
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpotlightCoreData/Introduction/introSpotlightCoreData.html
archived_at: '2026-07-15T07:19:21.207140Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Store%20Metadata-Level%20Indexing.md)

# Introduction

Core Data helps you to manage a graph of objects in your program and to save the graph to a persistent store. Spotlight is a fast desktop search technology that allows users to organize and search for files based on metadata. To integrate a Core Data-based program with Spotlight, you have to provide the Spotlight indexer with information about the data in your persistent store. There are two ways to do this; which approach you take depends on whether or not you are developing a document-based application. In either case, you have to write a suitable importer for your Core Data stores.

You should read this document to learn how to integrate Spotlight searching with your Core Data-based program.

This document comprises the following articles:

- [Store Metadata-Level Indexing](Store%20Metadata-Level%20Indexing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgawvgvzr) describes how you support Spotlight indexing in a document-based application.
- [Record-Level Indexing](Record-Level%20Indexing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrvfvbuqmjqgewvgvzs) describes how you support Spotlight indexing in a non-document-based application.

There are other technologies, not fully covered in this document, that are fundamental to integrating Core Data-based programs into Spotlight. Refer to these documents for more details:

- _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ describes Core Data.
- _[Spotlight Overview](../../Carbon/Spotlight%20Overview/Introduction%20to%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenry)_ describes the Spotlight technology.
- _[Spotlight Importer Programming Guide](../../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_ describe the plug-ins that extract metadata from files.
- _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_ describe the metadata attributes provided by Apple.
[Next](Store%20Metadata-Level%20Indexing.md)

