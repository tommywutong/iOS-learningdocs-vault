---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/FetchSpecs5.html
archived_at: '2026-07-18T01:18:28.900815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Fetch%20Specifications.md) [!Previous Section](Assigning%20a%20Sort%20Ordering.md)

# Specifying Prefetching and Other Options

There are numerous options you can configure to tune a fetch specification's behavior. This section describes the options on the Prefetching and Options tabs.

## Configuring Prefetching

Use this tab to identify relationships that should be fetched along with the objects specified by the fetch specification. For example, when fetching Rental objects, you can prefetch associated Fees and Units. Doing so forces a rental's fees and unit to be retrieved along with the rental itself (as opposed to having faults created for them).
Although prefetching increases the initial fetch cost, it can improve overall performance by reducing the number of round trips made to the database server.
To specify a relationship to prefetch, select the relationship in the Fetch Specification Builder's browser and click Add, as shown in [Figure 44](#apple-ge3diojq).

!

Figure 44. Specifying Relationships to Prefetch

Setting a Fetch Limit
To specify the maximum number of objects to fetch with a fetch specification, go to the Options tab of the Fetch Specification Builder, as shown in [Figure 45](#apple-ge3dkobv). There you can specify the maximum number of objects to fetch. The default fetch limit is zero, indicating that there is no fetch limit. Type a number in the Max Rows text field to specify a maximum number.

Use the "Prompt on limit" box to specify what the Framework should do when the fetch limit is reached. If the box is checked, the Framework prompt the user about whether to continue fetching after the maximum has been reached. If the box isn't checked, the Framework simply stops fetching when it reaches the limit.
For more information on managing fetch limits, see the EOFetchSpecification class description and the EOEditingContext EOMessageHandlers interface description in the _Enterprise Objects Framework Reference_.

!

Figure 45. The Options Tab

## Other Options

The other options on the Options tabs are explained below:
Perform deep inheritance fetch
An indicator of whether to fetch deeply or not. This is used with inheritance hierarchies when fetching for an entity with sub-entities. A deep fetch produces all instances of the entity and its sub-entities, while a shallow fetch produces instances only of the entity in the fetch specification.
Fetch distinct rows
An indicator of whether to produce distinct results or not. Normally if a record or object is selected several times, such as when forming a join, it appears several times in the fetched results. A fetch specification that fetches distinct rows filters out duplicates so that each record or object selected appears exactly once in the result set.
Lock all fetched objects
If a fetch specification locks fetched objects, it locks each object as it selects it.
Refresh refetched objects
If a fetch specification refreshes refetched objects, existing objects are overwritten with newly fetched values when they've been updated or changed. With fetch specifications that don't refresh, existing objects aren't updated when their data is refetched (the fetched data is simply discarded).
Require all variable bindings
Specifies whether a missing value for a qualifier variable is ignored or whether the Framework requires that each qualifier variable have a value assigned to it. If "Require all variable bindings" is checked, the Framework throws an exception during variable substitution. If it isn't checked, any qualifier nodes for which there are no variable bindings are pruned from the qualifier.

[!Table of Contents](Fetch%20Specifications.md) [!Next Section](Configuring%20Raw%20Row%20Fetching.md)
