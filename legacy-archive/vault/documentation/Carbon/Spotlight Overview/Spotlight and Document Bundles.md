---
title: Spotlight Overview
apple_id: TP40001268
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/DocumentBundles.html
archived_at: '2026-07-15T05:23:31.368131Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Overview](Introduction%20to%20Spotlight.md)


[Next](Document%20Revision%20History.md)[Previous](Security%20and%20Privacy%20Considerations.md)

# Spotlight and Document Bundles

Spotlight is notified when an application creates or updates a document, and imports the metadata from the file. However, if your application saves documents as a document bundle Spotlight is often notified of the creation of the document bundle directory before an application has the opportunity to write the contents of the document to disk. There are several strategies available to work around this issue.

One technique for saving a document bundle is to take advantage of the fact that Spotlight does not import metadata from invisible files or directories.

Create the document bundle directory as an invisible directory by prefacing the filename with the “.” character. Your application should create the directory using a temporary and unique filename with the appropriate filename extension. To ensure file-system compatibility, the temporary name should not exceed the length of the user specified filename. The application then writes the contents of the document to the invisible document bundle as normal. When completed the application then renames the invisible document bundle to the original document name.

Cocoa applications can use the NSFileWrapper class to create the document bundle as a directory wrapper. When the NSFileWrapper instance is written to disk the document bundle is created in such a way that Spotlight is notified when the entire document bundle has been saved.

[Next](Document%20Revision%20History.md)[Previous](Security%20and%20Privacy%20Considerations.md)

