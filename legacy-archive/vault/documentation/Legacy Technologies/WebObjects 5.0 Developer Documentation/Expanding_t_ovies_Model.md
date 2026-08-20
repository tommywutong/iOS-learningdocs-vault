---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Enhancing/Expanding_t_ovies_Model.html
archived_at: '2026-07-15T08:14:36.066847Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](Adding_Relationships.md)[![Next](attachments/JavaClient/Images/next.gif)](Adding_Beha_ise_Objects.md)

## Expanding the Movies Model

You are almost ready to add custom behavior to your enterprise
objects. But first you need to add additional relationships to the
Movies model.

If you used the example Movies model, you can skip most of
this section. However, you should, review [Table 3-1](#apple-ijbusskjinces) to make sure that the
relationship names in the your model match the ones defined in the
table.

Movies tell stories using a series of events or _plot_.
In the plot, people or objects interact according to their particular
roles in the movie. Those _movie roles_ are portrayed
by actors, or _talent_. To help cast a movie,
actors' _photos_ can be examined to determine
if they have the appropriate "look" for a role.

In the Movies model, Movie is associated to PlotSummary through
the `plotSummary` relationship.
There are reciprocal relationships between the Movie and MovieRole
objects. The Movie entity has a `movieRoles` relationship
that associates a Movie with its MovieRoles. In turn, the MovieRole
entity has a `movie` relationship
that associates a MovieRole with the Movie that it belongs to.

The Talent entity has relationships that associate it with
the TalentPhoto and MovieRole entities. The `movieRoles` relationship
determines the roles the Talent object (actor) stars in. The `photo` relationship
associates Talent objects with the actor's picture, or TalentPhoto object.

You will now add the remaining relationships to the model.

1. Open the
   Movies model file.

   In the Groups & Files list of Project
   Builder's main window, open the Resources group.

   Double-click `Movies.eomodeld`.
2. Add the Movie to MovieRole relationship.
   1. Create the relationship.

      Select
      the Movie entity.

      Choose Property > Add Relationship.

      Choose
      Tools > Inspector.

      Select To Many in the Destination
      group.

      Select MovieRole as the destination entity.

      Select
      movieId as the source attribute in the Joins group.

      Select
      movieId as the destination attribute.

      Click Connect.

      EOModeler
      names the relationship `movieRoles` because
      the relationship's target is MovieRole and it's a to-many relationship.
      It is strongly recommended that you use the names that EOModeler
      provides as they describe both the target of the relationship and
      its type. However, you are free to use a naming convention that will
      help the users of your model to easily understand it.
   2. Make the relationship a client-side class property.

      In
      the Movie Relationships Table, click in the ![[image: ../Art/clientsideclassproperty.gif]](../Art/clientsideclassproperty.gif)
      column in
      the movieRoles relationship information row, to make it a client-side
      class property.
3. Add the MovieRole to Movie relationship.
   1. Create the relationship.

      Select
      the MovieRole entity.

      Choose Property > Add Relationship.

      Ensure
      To One is selected in the Destination group.

      Select
      Movie as the destination entity.

      Ensure movieId is selected
      as the source and destination attribute.

      Click Connect.

      EOModeler
      names the relationship "movie."
   2. Make the relationship a client-side class property.

      In
      the MovieRoles Relationships table, click in the
      ![[image: ../Art/clientsideclassproperty.gif]](../Art/clientsideclassproperty.gif)
      column in the movie relationship
      information row, to make it a client-side class property.
4. Add the remaining relationships.

   [Table 3-1](#apple-ijbusskjinces) lists all the relationships
   that the Movies model should contain. Make sure all of them are
   entered in your model. Also remember to make them client-side class properties
   (see ["Using EOModeler to Add Relationships"](Adding_Relationships.md#apple-ijbusrkji5ees) for details).

   __Table
   3-1 Movies model relationships__

   __|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Source | Destination | Name | Type | Attribute |__| Movie | MovieRole | `movieRoles` | to-many | `movieId` |
| Movie | PlotSummary | `plotSummary` | to-one | `movieId` |
| Movie | Studio | `studio` | to-one | `studioId` |
| MovieRole | Movie | `movie` | to-one | `movieId` |
| MovieRole | Talent | `talent` | to-one | `talentId` |
| PlotSummary | Movie | `movie` | to-one | `movieId` |
| Studio | Movie | `movies` | to-many | `studioId` |
| Talent | MovieRole | `movieRoles` | to-many | `talentId` |
| Talent | TalentPhoto | `talentPhoto` | to-one | `talentId` |
| TalentPhoto | Talent | `talent` | to-one | `talentId` |

When finished, your model's diagram should look like the
one in [Figure 3-2](#apple-ijbusrscivceg).

__Figure
3-2 Diagram of the Movies model__

![[image: ../Art/largemodel.gif]](../Art/largemodel.gif)

At this point your model is complete.

[![Previous](attachments/JavaClient/Images/previous.gif)](Adding_Relationships.md)[![Next](attachments/JavaClient/Images/next.gif)](Adding_Beha_ise_Objects.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
