---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships4.html
archived_at: '2026-07-18T01:18:48.707908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20Relationships.md) [!Previous Section](Forming%20Relationships%20in%20the%20Relationship%20Inspector.md)

# Forming Relationships Across Models and Databases

The entities in one model can have relationships to the entities in another model. You can form such relationships even if the models map to different databases and different database servers.
When you add a model to a project, it becomes part of a model group, even if the model group only contains that one model (for more information on model groups, see the EOModelGroup class specification in the _Enterprise Objects Framework Reference_). Each subsequent model that you add to the project-either directly by adding the model to the project's Resources suitcase or indirectly by adding a framework that includes a model-automatically becomes part of the group. Entity names must be unique within a model group; you can't use the same entity name in two different models in the same group. Put another way, all the entities used in an application must have unique names.
To form a relationship from one model to another, use the Relationship Inspector as follows:

- Add a relationship to the entity you want to use as the source of the relationship.

For example, you can form a to-one relationship between the Movie entity in the Movies sample database and the VideoTape entity in the Rentals sample database.

- In the Relationship Inspector, use the Model pop-up list to choose the model containing the entity you want to use as the destination of the relationship.

!

Figure 27. Creating a Relationship Across Models

- Specify the relationship as you normally would.

__Note:__  You can't flatten properties across databases, nor can you map inheritance hierarchies across databases (though you can do both of these things across models that map to the same database).

[!Table of Contents](Creating%20Relationships.md) [!Next Section](Tips%20for%20Specifying%20Relationships.md)
