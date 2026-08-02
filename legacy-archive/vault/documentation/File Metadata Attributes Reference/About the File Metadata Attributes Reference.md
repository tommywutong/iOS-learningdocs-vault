---
title: File Metadata Attributes Reference
apple_id: TP40001689
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/MetadataAttrRef.html
archived_at: '2026-07-15T07:23:03.140725Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)


[Next](Spotlight%20Metadata%20Attributes.md)

# About the File Metadata Attributes Reference

File meta-data provides a collection of standard metadata attributes that are used by most files. Querying these standard attribute keys makes it easier to search based on standard metadata data. The file metadata attributes are used when performing searching or writing Spotlight importers on OS X. Metadata searches can be performed on local and network volumes when using OS X, and on iCloud when using iOS as well as OS X.

iCloud defines its own set of metadata attributes that are available only when files are stored, or transferring to or from, iCloud. These are defined in [iCloud Metadata Attributes](iCloud%20Metadata%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytenztfvjvomi).

You should read this document if you are creating metadata search queries to locate files. You should also use the standard Spotlight metadata attribute keys if writing a Spotlight importer. It is important to use existing keys whenever possible. Avoid creating new metadata keys if an existing key would be appropriate. For example, if your document tracks the photographer of an image, use the `kMDItemAuthors` key rather than defining a custom `photographer` key.All applications that support saving their own documents should consider providing a Spotlight importer using these metadata attribute keys.

The iCloud metadata attributes provide information on the status of files as they are uploaded and downloaded from iCloud. The abilities include checking for downloading or uploading status and tracking the upload and download percentages.

This article contains descriptions of the metadata attribute keys that Apple provides:

- [Spotlight Metadata Attributes](Spotlight%20Metadata%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojufvjvomi) describes Spotlight’s standard metadata attributes.
- [iCloud Metadata Attributes](iCloud%20Metadata%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytenztfvjvomi) list the metadata attributes that are only available to files that are iCloud specific.

This document is primarily a reference. You may want to read these additional topics for a better understanding of the concepts required to effectively use Spotlight and iCloud metadata.

- _[Spotlight Overview](../Carbon/Spotlight%20Overview/Introduction%20to%20Spotlight.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenry)_ covers the conceptual details surrounding file metadata usage
- _[File Metadata Search Programming Guide](../Carbon/File%20Metadata%20Search%20Programming%20Guide/About%20File%20Metadata%20Queries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqnbr)_ describes how to write search queries that use metadata attributes. Searches can be performed on both OS X and iOS and targeted to local or networked storage, or iCloud.
- _[Core Data Spotlight Integration Programming Guide](../Cocoa/Core%20Data%20Spotlight%20Integration%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4danrv)_ describes how to write Spotlight importers that use Core Data storage on OS X.
- _[Spotlight Importer Programming Guide](../Carbon/Spotlight%20Importer%20Programming%20Guide/About%20Spotlight%20Importers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytenrx)_ describes how to write and troubleshoot Spotlight importers on OS X.
[Next](Spotlight%20Metadata%20Attributes.md)

