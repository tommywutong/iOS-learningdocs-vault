---
title: Spotlight Overview
apple_id: TP40001268
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/MetadataIntro.html
archived_at: '2026-07-15T05:23:34.833347Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%20is%20Spotlight.md)

# Introduction to Spotlight

Spotlight is a fast desktop search technology that allows users to organize and search for files based on metadata. Spotlight is extensible, allowing developers to provide metadata importers for their application’s documents.

Spotlight is a fundamental feature of OS X, and all developers should be familiar with its capabilities. Developers of applications that save documents to disk should consider providing Spotlight support by implementing a metadata importer.

The following articles cover key concepts in understanding how Spotlight works:

- [What is Spotlight?](What%20is%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgayteobrfvbuuqsfjjbeqsa) provides an overview of what Spotlight provides.
- [How Does Spotlight Work?](How%20Does%20Spotlight%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbxfvbuuqsfjjbeqsa) describes how Spotlight creates metadata indexes, and how they are queried.
- [Spotlight Metadata Attributes](Spotlight%20Metadata%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjrfvbuuqsfjjbeqsa) provides an overview of metadata attributes.
- [Security and Privacy Considerations](Security%20and%20Privacy%20Considerations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnjsfvbuuqsfjjbeqsa) describes how Spotlight addresses security and privacy issues.
- [Spotlight and Document Bundles](Spotlight%20and%20Document%20Bundles.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdambxfvbuuqsfjjbeqsa) describes how an application should create document bundles with Spotlight in mind.

There are other technologies, not fully covered in this document, that are fundamental to integrating Spotlight into your applications. Refer to these documents for more details:

- _[File Metadata Search Programming Guide](../File%20Metadata%20Search%20Programming%20Guide/About%20File%20Metadata%20Queries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbr)_ describe how to query Spotlight from your applications.
- _[Spotlight Importer Programming Guide](../Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_ describe the plug-ins that extract metadata from document files.
- _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_ describe the metadata attributes provided by Apple.
- _[Core Data Spotlight Integration Programming Guide](../../Cocoa/Core%20Data%20Spotlight%20Integration%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrv)_ discusses how to take advantage of Spotlight features in an app that uses Core Data for document storage.
[Next](What%20is%20Spotlight.md)

