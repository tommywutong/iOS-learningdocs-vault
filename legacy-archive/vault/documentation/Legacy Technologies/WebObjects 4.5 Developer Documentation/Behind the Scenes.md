---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/BehindSc.html
archived_at: '2026-07-15T08:02:50.105476Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Top](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

#

# Behind the Scenes

---

Using Application Kit applications as examples, this chapter answers the following questions about what Enterprise Objects Framework does behind the scenes:

- What is the sequence of events when objects are fetched from the database?
- How does an EOEditingContext manage changes to its objects?
- What happens when changes to objects are saved to the database?
- How does Enterprise Objects Framework manage transactions?

Enterprise Objects Framework provides hooks so that your code can intervene in each of these scenarios. In addition to describing what happens behind the scenes in an Enterprise Objects Framework application, this chapter lists the delegate methods and notifications your code can use at every stage of an application to do custom processing.
Most of the information in this chapter can also be applied to other types of applications (command-line and web applications), but some of the details vary from what's illustrated here with Application Kit applications.

[__Fetching Objects__](Fetching%20Objects.md)
[****
: EODisplayGroup Receives a fetch Message](BehindSc1.md#apple-giyds)
[****
: Inside EODatabaseContext](BehindSc1.md#apple-ha2dqma)[****
: Inside EODatabaseChannel](BehindSc1.md#apple-gyzdomy)[****
: Flow of Data During a Fetch](BehindSc1.md#apple-he3ti)[****
: Uniquing, Snapshots, and Faults](BehindSc1.md#apple-gqyto)

[__How Changes are Distributed and Applied__](How%20Changes%20are%20Distributed%20and%20Applied.md)

[****
: How an EOEditingContext Manages Changes to Its Objects](BehindSc2.md#apple-g4zdg)[__Saving Changes__](Saving%20Changes.md)
[****
: Locking and Update Strategies](BehindSc3.md#apple-g4ytmnq)
[__Transactions__](Transactions.md)
[****
: Transactions and Optimistic Locking](BehindSc4.md#apple-gi2tq)
[****
: Transactions and Pessimistic Locking](BehindSc4.md#apple-haytc)[****
: Transactions and On-Demand Locking](BehindSc4.md#apple-ha4dc)
[!First Section](Fetching%20Objects.md)
