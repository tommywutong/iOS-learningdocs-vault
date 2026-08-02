---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships5.html
archived_at: '2026-07-18T01:18:51.257721Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20Relationships.md) [!Previous Section](Forming%20Relationships%20Across%20Models%20and%20Databases.md)

# Tips for Specifying Relationships

The following tips are useful to keep in mind as you specify relationships in your model:

- The relationships you define in your model must reflect a corresponding implementation in the database, as well as the features supported by your adaptor. EOModeler doesn't know, for example, if a relationship is to-one or to-many, or if your adaptor supports left outer joins. You need to know your database and your adaptor, and specify relationships accordingly.
- Use the diagram view to quickly create pairs of inverse relationships by control-dragging between source and destination attributes.
- Use the Relationship Inspector to specify information about a relationship, such as whether it's to-one or to-many, its semantics (that is, the type of join represented by the relationship), and the name of the destination model (if the destination isn't in the current model).
- Relationships are created as to-one relationships. You need to change this setting if the two entities have a to-many relationship (for example, a movie has many roles).
- A relationship can be compound, meaning that it can consist of multiple pairs of connected attributes. You can specify additional pairs of attributes only in the Relationship Inspector. Simply select a second source attribute and a second destination attribute, and click Connect a second time.
- A to-one relationship from one primary key to another primary key must always have exactly one row in the destination entity-if this isn't guaranteed to be the case, use a to-many relationship. This rule doesn't apply to a foreign key to primary key relationship, where a NULL value for the foreign key in the source row indicates that no row exists in the destination.
- To-one relationships must join on the complete primary key of the destination entity as the join component.

For more discussion about modeling relationships, see the chapter "Advanced Enterprise Object Modeling" in the book _Enterprise Objects Framework Developer's Guide_.

[!Table of Contents](Creating%20Relationships.md) [!Next Section](Adding%20Referential%20Integrity%20Rules.md)
