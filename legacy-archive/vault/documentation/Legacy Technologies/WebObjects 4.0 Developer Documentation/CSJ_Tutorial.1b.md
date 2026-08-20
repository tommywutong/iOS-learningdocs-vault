---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.1b.html
archived_at: '2026-07-15T07:59:31.834373Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1a.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.1c.md)

##   Adding  Relationships

Creating an application that adds and modifies studios is just the first stage of the StudioManager application. Now you can enhance the application to display all of the movies owned by a selected studio.

The Studio, Movie, and Talent entities are not especially interesting when considered separately. Their real significance only becomes apparent in their relationships to each other. Every Movie has one corresponding Studio. One Studio can have many Movies. A particular actor (Talent) can star in several movies.

Relational databases model not just individual entities, but entities' relationships to one another. For example, a Movie entity has a corresponding Studio entity. This is modeled in the database by both the Movie entity and the Studio entity having a __studioID__
attribute. In Movie, __studioID__
is a foreign key, while in Studio it's a primary key. 

A foreign key correlates with the primary key of another table in order to model a relationship a source table (Movie) has to a destination table (Studio). In the following diagram, notice that the value in the __STUDIO_ID__
column for both movies is "501". This matches the value in the __STUDIO_ID__
column of the Columbia Pictures movie studio. In other words, the movies "Tootsie" and "Taxi Driver" both belong to Columbia Pictures.

###### 

!

This plays out in your running application as follows: Suppose you fetch a Movie object. Enterprise Objects Framework takes the value for the movie's __studioID__
attribute and looks up the studio with the corresponding primary key.

For your application to take advantage of such database-defined relationships, your model must specify the corresponding relationships. When you created the model using the wizard, EOModeler created relationships between your selection of entities based on matching primary and foreign keys; it assigned relationship names of the form "to_DestinationEntity_
". You might have reason now to examine these relationships, add new ones, delete generated ones, or modify things such as whether a relationship is to-one or a to-many.

__Note:__ Your model may already have some relationships in it, based on information EOModeler read from the database. For the purposes of this tutorial, you can just ignore these relationships.

You need to ensure that the following relationships are specified:

From the Studio (source) entity:

- Form a _to-many_ relationship to the Movie (destination) entity.

- The source attribute is __studioID__
  . The destination attribute is __studioID__
  .

- Name the relationship __movies__
  .

  From the Movie (source) entity:

  - Form a _to-one_ relationship to the Studio (destination) entity.

  - The source attribute is __studioID__
    . The destination attribute is __studioID__
    .

- Name the relationship __studio__
  .

  __1. Create a relationship.__

  > Display the attributes view for the entity you want to use as the source of the relationship.
  >
  > 
  >
  > Choose Property !
  > Add Relationship.
  >
  > 
  >
  > In the Relationship Inspector, enter the name of the relationship.
  >
  > 
  >
  > Select whether the relationship is to-one or to-many.
  >
  > 
  >
  > Select a destination entity.
  >
  > 
  >
  > Select a source attribute.
  >
  > 
  >
  > Select a destination attribute.
  >
  > 
  >
  > Connect them.
  >
  > ###### 
  >
  > !

  ---

  \xA9 1999 Apple Computer, Inc.

  [Previous](CSJ_Tutorial.1a.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.1c.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)
