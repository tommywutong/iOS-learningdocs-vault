---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.26.html
archived_at: '2026-07-15T08:09:02.647915Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](What%20if%20It%20Doesn%27t%20Work.md) [!](Adding%20Movies%20to%20the%20Application.md)

---

#   Adding  Relationships

Creating an application that adds and modifies studios is just the first stage of the StudioManager application. Now you can enhance the application to display all of the movies owned by a selected studio.

The Studio, Movie, and Talent entities are not especially interesting when considered separately. Their real significance only becomes apparent in their relationships to each other. Every Movie has one corresponding Studio. One Studio can have many Movies. A particular actor (Talent) can star in several movies.

Relational databases model not just individual entities, but entities' relationships to one another. For example, a Movie entity has a corresponding Studio entity. This is modeled in the database by both the Movie entity and the Studio entity having a __studioID__ attribute. In Movie, __studioID__ is a foreign key, while in Studio it's a primary key. 

A foreign key correlates with the primary key of another table in order to model a relationship a source table (Movie) has to a destination table (Studio). In the following diagram, notice that the value in the __STUDIO_ID__ column for both movies is "501". This matches the value in the __STUDIO_ID__ column of the Columbia Pictures movie studio. In other words, the movies "Tootsie" and "Taxi Driver" both belong to Columbia Pictures.

!

This plays out in your running application as follows: Suppose you fetch a Movie object. Enterprise Objects Framework takes the value for the movie's __studioID__ attribute and looks up the studio with the corresponding primary key.

For your application to take advantage of such database-defined relationships, your model must specify the corresponding relationships. When you created the model using the wizard, EOModeler created relationships between your selection of entities based on matching primary and foreign keys; it assigned relationship names of the form "to_DestinationEntity_". You might have reason now to examine these relationships, add new ones, delete generated ones, or modify things such as whether a relationship is to-one or a to-many.
__Note:__

Your model may already have some relationships in it, based on information EOModeler read from the database. For the purposes of this tutorial, you can just ignore these relationships.

You need to ensure that the following relationships are specified:

From the Studio (source) entity:

- 

  Form a to-many relationship to the Movie (destination) entity.
- 

  The source attribute is __studioID__. The destination attribute is __studioID__.
- 

  Name the relationship __movies__.

From the Movie (source) entity:

- 

  Form a to-one relationship to the Studio (destination) entity.
- 

  The source attribute is __studioID__. The destination attribute is __studioID__.
- 

  Name the relationship __studio__.

1. 

   Create a relationship.

   Display the attributes view for the entity you want to use as the source of the relationship.

   Choose Property !
   Add Relationship.

   In the Relationship Inspector, enter the name of the relationship.

   Select whether the relationship is to-one or to-many.

   Select a destination entity.

   Select a source attribute.

   Select a destination attribute.

   Connect them.

   !

#### [Adding Movies to the Application](Adding%20Movies%20to%20the%20Application.md#apple-obtwm3dehuytambwg43ts)

#### [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-obtwmslehuytambwg44di)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](What%20if%20It%20Doesn%27t%20Work.md) [!](Adding%20Movies%20to%20the%20Application.md)
