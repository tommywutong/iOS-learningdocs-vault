---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.1c.html
archived_at: '2026-07-15T08:08:54.780842Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Verifying%20and%20Modifying%20the%20Model.md) [!](Verifying%20and%20Modifying%20the%20Model.md) [!](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md)

---

#   Assigning  Primary Keys

In a relational database, each table has a column or combination of columns whose values are guaranteed to uniquely identify each row in that table. For example, in the Movies database the MOVIE table has as its primary key the column MOVIE_ID. Each row in the MOVIE table has a different value in the MOVIE_ID column, which uniquely identifies that row. Two movies could have the same name, but still be distinguished from each other by their primary keys.

!

Enterprise Objects Framework uses primary keys to uniquely identify enterprise objects and to map them to the appropriate database row. Therefore, you must make sure that each of your entities has a primary key assigned to it in EOModeler. If your database has primary keys defined in it, this information is automatically included when you create a model--in that case, you don't need to assign primary keys yourself.

1. 

   Make sure that each entity has a primary key.

   !

The following table lists the primary keys that should be assigned to each of the entities in the model. Note that entities (such as MovieRole) can have a compound primary key; that is, a primary key that is composed of more than one attribute. However, EOModeler can assign compound primary keys (such as rowId and movieId) when only a single primary key is necessary. For more discussion of this subject, see the appendix "Entity-Relationship Modeling" in the Enterprise Objects Framework Developer's Guide.

| __ The entity...__ |  Should have the primary key attributes... |
| --- | --- |
|   Director |   movieId and talentId |
|   Movie |   movieId |
|   MovieRole |   movieId and talentId |
|   PlotSummary |   movieId |
|   Review |   reviewId |
|   Studio |   studioId |
|   Talent |   talentId |
|   TalentPhoto |   talentId |
|   Voting |   movieId |

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Verifying%20and%20Modifying%20the%20Model.md) [!](Verifying%20and%20Modifying%20the%20Model.md) [!](Removing%20Primary%20and%20Foreign%20Keys%20as%20Class%20Properties.md)
