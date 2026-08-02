---
title: Spotlight Overview
apple_id: TP40001268
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/MetadataIntro/Concepts/SpotlightAttrs.html
archived_at: '2026-07-15T05:23:34.375570Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Spotlight Overview](Introduction%20to%20Spotlight.md)


[Next](Security%20and%20Privacy%20Considerations.md)[Previous](How%20Does%20Spotlight%20Work.md)

# Spotlight Metadata Attributes

The first step in providing support for Spotlight is to decide what information a user will want to look for in documents they create using your application. Once you determine the data that should be extracted and provided to users, you need to assign those values to metadata attributes.

Spotlight defines standard metadata attributes that provide a wide range of options for storing your document’s metadata. Users can restrict searching to specific attributes, and so it is important that you should use Spotlight’s standard metadata attributes whenever possible.

For example, many documents contain a company name that should be extracted as metadata. Spotlight doesn’t provide an explicit company name attribute. It does, however, define an attribute that stores an “organization”—`kMDitemOrganizations`—which is appropriate for a company name. The Spotlight provided metadata attributes are documented in _[File Metadata Attributes Reference](../../File%20Metadata%20Attributes%20Reference/About%20the%20File%20Metadata%20Attributes%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmobz)_.

If an appropriate metadata attribute isn’t provided by Spotlight, you should look to third-party developers to see if they have already defined an appropriate attribute key. If no appropriate Spotlight or third-party metadata attribute has been defined, then you can create your own custom metadata attributes.

[Next](Security%20and%20Privacy%20Considerations.md)[Previous](How%20Does%20Spotlight%20Work.md)

