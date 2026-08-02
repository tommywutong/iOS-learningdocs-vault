---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships1.html
archived_at: '2026-07-15T08:04:24.667340Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

!Table of Contents [!Previous Section](Working%20with%20Relationships.md)

# Creating Relationships

If the database on which your model is based includes definitions for foreign keys, these definitions will automatically be expressed in your model as ready-made relationships.
You can also explicitly form a relationship between entities if one doesn't already exist. This relationship must reflect an actual relationship between the entities' corresponding tables in the database.
Forming a relationship allows you to access data in a destination table that relates to data in a source table (it's also possible to have a reflexive relationship, in which the source and destination tables are the same). For example, to find all of the roles in a particular movie, you can form a relationship between the MovieRole and Movie entities.
EOModeler provides two mechanisms for forming relationships. You can form them in the Model Editor's diagram view or in the Relationship Inspector. Using the diagram is the quickest way to create a new relationship, but using the Relationship Inspector gives you access to more relationship characteristics. Each mechanism is discussed in the following sections.

!Table of Contents [!Next Section](Forming%20Relationships%20in%20the%20Diagram%20View.md)
