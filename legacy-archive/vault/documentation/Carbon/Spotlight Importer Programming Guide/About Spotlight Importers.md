---
title: Spotlight Importer Programming Guide
apple_id: TP40001267
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MDImporters/MDImporters.html
archived_at: '2026-07-15T05:23:21.740661Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Extracting%20Metadata%20from%20Files.md)

# About Spotlight Importers

Spotlight metadata importers extract metadata from custom file formats after files are saved, copied, or moved. That custom metadata can then be searched from applications, both System applications and custom applications,. The files can be searched on local disks and networked storage on OS X.

If your applications supports saving its custom file formats to disk, you should consider providing Spotlight support by implementing a metadata importer.

Read this document to learn how metadata importers work and how to write an importer.

The following articles cover key concepts in understanding how metadata importers work:

- [Extracting Metadata from Files](Extracting%20Metadata%20from%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgayteobtfvbuuqsfjjbeqsa) describes the role of the metadata importer and its components.
- [Assigning Values to Metadata Attributes](Assigning%20Values%20to%20Metadata%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzxfvbuuqsfjjbeqsa) provides an overview of the Spotlight metadata attributes and explains how to define your own attributes.
- [Spotlight Importer Schema Format](Spotlight%20Importer%20Schema%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzsfvbuuqsfjjbeqsa) describes the format of a Spotlight importer schema file.

These articles explain how to implement metadata importers:

- [Spotlight Importer Performance](Spotlight%20Importer%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmzwfvbuuqsfjjbeqsa) describes important performance considerations.
- [Writing a Spotlight Importer](Writing%20a%20Spotlight%20Importer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenzvfvbuuqsfjjbeqsa) explains how to write a metadata importer.
- [Troubleshooting Spotlight Importers](Troubleshooting%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojqfvbuuqsfjjbeqsa) answers questions you might have when you’re testing your Spotlight importers.

There are other aspects of Spotlight metadata, not covered, by this document,that are fundamental to implementing a metadata importer. For example, this document does not explain the commonly used metadata keys or provide guidelines on using those keys to their full potential. Refer to these documents for more details:

- _[Spotlight Overview](../Spotlight%20Overview/Introduction%20to%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenry)_ explains concepts that are key to understanding how search, including Spotlight, work.
- _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_ describes the metadata keys Apple provides.
- _[File Metadata Search Programming Guide](../File%20Metadata%20Search%20Programming%20Guide/About%20File%20Metadata%20Queries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbr)_ describes how to search for files using Spotlight metadata.
- _[Core Data Spotlight Integration Programming Guide](../../Cocoa/Core%20Data%20Spotlight%20Integration%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrv)_ discusses how to take advantage of Spotlight features in an app that uses Core Data for its document storage.
[Next](Extracting%20Metadata%20from%20Files.md)

