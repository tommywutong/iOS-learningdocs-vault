---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs6.html
archived_at: '2026-07-15T08:04:14.650284Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Specifying%20Prefetching%20and%20Other%20Options.md)

# Configuring Raw Row Fetching

When you perform a fetch in an Enterprise Objects Framework application, the information from the database is fetched and stored in a graph of enterprise objects. This object graph provides many advantages, but it can be large and complex. If you're creating a simple application, you may not need all of the benefits of the object graph. For example, a WebObjects application that merely displays information from a database without ever performing database updates and without ever traversing relationships might be just as well served by fetching the information into a set of dictionaries rather than a set of enterprise objects.
Enterprise Objects Framework 3.0 supports this concept of a simplified fetch, called _raw row_ fetching. In raw row fetching, each row from the database is fetched into an NSDictionary object.
When you use raw row fetching, you lose some important features:

- The NSDictionary objects are not uniqued.
- The NSDictionary objects aren't tracked by an editing context.
- You can't access to-many relationship information. (To access to-one relationship information, you use key paths such as "__movie.dateReleased__".)

To set up raw row fetching, go to the Raw Fetch tab of the Fetch Specification Builder as shown in [Figure 46](#apple-ge3dkmbv).

!

Figure 46. Specifying a Raw Row Fetch

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Using%20Custom%20SQL%20and%20Stored%20Procedures.md)
