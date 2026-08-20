---
title: File Metadata Search Programming Guide
apple_id: TP40001841
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2011-09-28'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/SearchScope.html
archived_at: '2026-07-15T05:24:41.723455Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File Metadata Search Programming Guide](About%20File%20Metadata%20Queries.md)


[Next](Searching%20File%20Metadata%20with%20NSMetadataQuery.md)[Previous](About%20File%20Metadata%20Queries.md)

# Searching iCloud and the Desktop

The Spotlight search capabilities are available on both iOS v5.0 and OS X. Using these search queries iOS can search iCloud content and OS X can search both iCloud, desktop, and networked files.

Spotlight is ubiquitous on OS X. The Finder uses it to search for allow the user to search for files. Mail uses Spotlight to find messages during the search process, and any application can use Spotlight to search the User’s home directory, the local file system, any attached networked file systems, and iCloud.

The OS X Objective-C interface to the Spotlight API includes classes to search ([NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery)), inspect the file metadata ([NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem)), and the ability to have the `NSMetadataQuery` return a more complicated set of data using the [NSMetadataQueryAttributeValueTuple](https://developer.apple.com/documentation/foundation/nsmetadataqueryattributevaluetuple) class. In addition a Core Foundation API exists that correspond to each of the Objective-C classes (in fact the classes are built upon the Core Foundation base.

iOS allows metadata searches within iCloud to find files corresponding files. It provides only the Objective-C interface to file metadata query, `NSMetadataQuery` and `NSMetadataItem`, as well as only supporting the search scope that searches iCloud.

Unlike the desktop, the iOS application’s sandbox is not searchable using the metadata classes. In order to search your application’s sandbox, you will need to traverse the files within the sandbox file system recursively using the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class. Once matching file or files is found, you can access that file in the manner that you require. You are also able to use the `NSMedatataItem` class to retrieve metadata for that particular file.

[Next](Searching%20File%20Metadata%20with%20NSMetadataQuery.md)[Previous](About%20File%20Metadata%20Queries.md)

