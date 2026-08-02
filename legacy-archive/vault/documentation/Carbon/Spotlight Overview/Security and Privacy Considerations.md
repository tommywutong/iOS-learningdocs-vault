---
title: Spotlight Overview
apple_id: TP40001268
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/SecurityAndPrivacy.html
archived_at: '2026-07-15T05:23:33.814970Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Overview](Introduction%20to%20Spotlight.md)


[Next](Spotlight%20and%20Document%20Bundles.md)[Previous](Spotlight%20Metadata%20Attributes.md)

# Security and Privacy Considerations

On systems with separate user accounts, Spotlight respects the ownership of users’ files—even though the system store is shared. Spotlight filters all query results, removing any files that the user isn’t permitted to see.

However, developers should still be aware of users’ data privacy and security when extracting metadata from documents.

When determining the data to extract from your application’s documents you should consider the implications of making that data searchable. For example, could making the author of the document available be a liability? Should the full content of a document be available for indexing, or only selected fields?

Developers should provide users with information about which data is indexed by their Spotlight importers. Developers should also consider providing preferences that allow users control over what data is extracted as metadata.

Spotlight importers typically reside within an application wrapper. When first copied to the user’s computer an application is considered untrusted. The first time that the application is launched, OS X presents a warning to the user. If the user accepts, the application is launched and considered “trusted.”

Spotlight does not load and use a bundled importer if the associated application is not trusted.

[Next](Spotlight%20and%20Document%20Bundles.md)[Previous](Spotlight%20Metadata%20Attributes.md)

