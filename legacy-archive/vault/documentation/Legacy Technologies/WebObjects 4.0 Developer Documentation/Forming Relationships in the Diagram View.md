---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships2.html
archived_at: '2026-07-18T01:18:45.077224Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20Relationships.md) [!Previous Section](Creating%20Relationships.md)

# Forming Relationships in the Diagram View

To create a relationship in diagram view, control-drag from a source attribute to the destination attribute, as shown in [Figure 24](#apple-ge2dgmru).

!

Figure 24. Control-Dragging to Create a Relationship

Control-dragging to create a relationship actually creates two relationships: one in the source attribute's entity and an inverse relationship in the destination attribute's entity. So in [Figure 24](#apple-ge2dgmru), control-dragging from the Movie entity's __studioId__ attribute to the Studio entity's __studioId__ attribute creates the relationships:

- __studio__, a to-one relationship in Movie to Studio
- __movies__, a to-many relationship in Studio to Movie

You can view the new relationships in the Model Editor's table mode and you can further configure them in the Relationship Inspectors as described in the next sections.

[!Table of Contents](Creating%20Relationships.md) [!Next Section](Forming%20Relationships%20in%20the%20Relationship%20Inspector.md)
