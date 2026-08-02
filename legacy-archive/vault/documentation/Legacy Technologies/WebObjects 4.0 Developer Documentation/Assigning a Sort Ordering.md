---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs4.html
archived_at: '2026-07-18T01:18:26.607150Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Building%20a%20Qualifier.md)

# Assigning a Sort Ordering

To specify the order in which the fetch specification fetches its objects, use the Sort Ordering tab in the Fetch Specification Builder, as shown in [Figure 43](#apple-ge3dcmzx).

!

Figure 43. Assigning a Sort Ordering

Simply choose an attribute to sort on, and click Add. The order in which you add the attributes specifies the weight to assign to them. In [Figure 43](#apple-ge3dcmzx), the fetch specification sorts first on title and then on category.

Additionally, for each attribute you sort on, you can specify an ascending or descending order and whether to perform a case-sensitive or case-insensitive comparison.

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Specifying%20Prefetching%20and%20Other%20Options.md)
