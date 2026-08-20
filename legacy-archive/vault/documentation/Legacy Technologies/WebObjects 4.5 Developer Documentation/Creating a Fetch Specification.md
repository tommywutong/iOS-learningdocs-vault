---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs2.html
archived_at: '2026-07-15T08:04:08.661180Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Fetch%20Specifications.md)

# Creating a Fetch Specification

To create a fetch specification in EOModeler:

- Select the entity with which the fetch specification will be associated.
- Choose Property ! Add Fetch Specification or click the ! button in the tool bar.

!

Figure 40. Adding a Fetch Specification to an Entity

- Type a name for the fetch specification in the Fetch Specification Name field.

There are many different ways to configure the fetch specification. The most common way is to build a qualifier for the fetch specification to fetch with. For more information, see the section [Building a Qualifier](Building%20a%20Qualifier.md#apple-ge2tqnrs). Alternatively, you can also configure a fetch specification to fetch using custom SQL or a stored procedure. For more information, see [Using Custom SQL and Stored Procedures](Using%20Custom%20SQL%20and%20Stored%20Procedures.md#apple-ge2tqnzu).

In addition to specifying how a fetch specification retrieves its data, you can specify other options, such as sort orderings and performance tuning settings. The following sections describe the possible configurations and their uses.

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Building%20a%20Qualifier.md)
