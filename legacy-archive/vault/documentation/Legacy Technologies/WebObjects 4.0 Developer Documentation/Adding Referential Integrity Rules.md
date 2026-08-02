---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships6.html
archived_at: '2026-07-18T01:18:51.345672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20Relationships.md) [!Previous Section](Tips%20for%20Specifying%20Relationships.md)

# Adding Referential Integrity Rules

You can use the Advanced Relationship Inspector to add referential integrity rules for a relationship.
To add referential integrity rules:

- Select the relationship for which you want to add rules.
- In the Relationship Inspector, click the Advanced Relationship Inspector icon as shown in [Figure 28](#apple-geydinq).

!

Figure 28. Advanced Relationship Inspector

You can use the fields in the Advanced Relationship Inspector to further specify a relationship. The options in this inspector are described in the following sections.
Batch Faulting
Normally when a fault is triggered, just that object (or array of objects for a to-many relationship) is fetched from the database. You can take advantage of this expensive round trip to the database by batching faults together. The value you type in the Batch Size field indicates the number of faults for the same relationship that should be triggered along with the first fault. For more discussion of batch faulting, see the class specification for EODatabaseContext in the _Enterprise Objects Framework Reference_.
Optionality
This field lets you specify whether a relationship is optional or mandatory. For example, you could require all departments to have a location (mandatory), but not require every employee to have a manager (optional).
Delete Rule
This field lets you specify the delete rules that should be applied to an entity that's involved in a relationship. For example, you could have a department with multiple employees. When a user tried to delete the department, you could:

- Delete the department and remove any back reference the employee has to the department (Nullify).
- Delete the department and all of the employees it contains (Cascade).
- Refuse the deletion if the department contains employees (Deny).
- Allow the deletion and do nothing to the destination objects (No Action).

The No Action rule is useful for tuning performance. However, you should use this delete rule with great caution since it can result in dangling references in your object graph. For more information, see the class specification for EOClassDescription in the _Enterprise Objects Framework Reference_.
Owns Destination
The Owns Destination checkbox lets you set a source object as owning its destination objects. When a source object owns its destination objects and you remove a destination object from the source object's relationship array, this also has the effect of deleting it from the database (alternatively, you can transfer it to a new owner). This is because ownership implies that the owned object can't exist without an owner-for example, line items can't exist outside of a purchase order.
Propagate Primary Key
The Propagate Primary Key checkbox lets you specify that the primary key of the source entity should be propagated to newly inserted objects in the destination of the relationship. This is typically used for an owning relationship, where the owned object has the same primary key as the source. For example, in the Movies database the TalentPhoto entity has the same primary key as the entity that owns it, Talent.
[!Table of Contents](Creating%20Relationships.md) [!Next Section](Adding%20Derived%20Properties.md)
