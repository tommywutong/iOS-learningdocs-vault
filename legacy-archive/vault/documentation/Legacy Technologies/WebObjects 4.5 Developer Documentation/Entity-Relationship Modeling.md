---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/ApA_ERMd.html
archived_at: '2026-07-15T08:02:27.037800Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Top](Enterprise%20Objects%20Framework%20Developer%27s%20Guide.md)

# Entity-Relationship Modeling

---

A database server stores data in the structures that it defines: A relational database uses tables to store data, an object-oriented database uses objects, a file system uses files, and so on. The Enterprise Objects Framework uses the terminology of _Entity-Relationship modeling_ (or _E-R modeling_) to describe a server's data structures in a way that allows those data structures to be mapped to enterprise objects.
Entity-Relationship modeling isn't unique to the Enterprise Objects Framework; it's a popular discipline with a set of rules and terms that are documented in database literature. The Enterprise Objects Framework uses a modified version of the traditional rules of E-R modeling.
When your data store is a relational database, you can use the EOModeler application to specify the mapping between the database data and your enterprise objects. The model file you produce using EOModeler describes the server's data structures in terms that the Enterprise Objects Framework can understand. Note that if you're working with a data store other than a database, you must create your own data structures to map the server's data to your enterprise objects.
This chapter presents the E-R terms and concepts as they are used by the Framework. For instructions on putting these concepts into practice, see the book _Enterprise Objects Framework Tools and Techniques_.

[__Modeling Objects__](Modeling%20Objects.md)[__Entities and Attributes__](Entities%20and%20Attributes.md)
[****
: Names and the Data Dictionary](ApA_ERMd2.md#apple-gqzdk)[****
: Attribute Data](ApA_ERMd2.md#apple-gq3te)
[****
: The Primary Key](ApA_ERMd2.md#apple-gqyds)

[__Relationships__](Relationships.md#apple-gqyts)

[****
: Relationship Directionality](ApA_ERMd3.md#apple-gqydg)[****
: Naming Relationships](ApA_ERMd3.md#apple-gq2ta)[****
: Relationship Keys](ApA_ERMd3.md#apple-gqzdm)[****
: Relationship Cardinality](ApA_ERMd3.md#apple-guyti)[****
: Bidirectional Relationships](ApA_ERMd3.md#apple-gmzdonq)[****
: Reflexive Relationship](ApA_ERMd3.md#apple-gm4tk)[****
: Flattened Attributes](ApA_ERMd3.md#apple-guyto)
[!First Section](Modeling%20Objects.md)
