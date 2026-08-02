---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.11.html
archived_at: '2026-07-15T07:59:17.155319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.10.md) | [Back Up One Level](CSJ_Tutorial.10.md) | [Next](CSJ_Tutorial.12.md)

###   Assigning  Primary Keys

In a relational database, each table has a column or combination of columns whose values are guaranteed to uniquely identify each row in that table. For example, in the Movies database the MOVIE table has as its primary key the column MOVIE_ID. Each row in the MOVIE table has a different value in the MOVIE_ID column, which uniquely identifies that row. Two movies could have the same name, but still be distinguished from each other by their primary keys.

###### 

!

Enterprise Objects Framework uses primary keys to uniquely identify enterprise objects and to map them to the appropriate database row. Therefore, you must make sure that each of your entities has a primary key assigned to it in EOModeler. If your database has primary keys defined in it, this information is automatically included when you create a model--in that case, you don't need to assign primary keys yourself.

__1. Make sure that each entity has a primary key.__
> ###### 
>
> !
>
> 

The following table lists the primary keys that should be assigned to each of the entities in the model. Note that entities (such as MovieRole) can have a compound primary key; that is, a primary key that is composed of more than one attribute. However, EOModeler can assign compound primary keys (such as rowId and movieId) when only a single primary key is necessary. For more discussion of this subject, see the appendix "Entity-Relationship Modeling" in the Enterprise Objects Framework Developer's Guide.

|   The entity... |   Should have the primary key attributes... |
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

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.10.md) | [Back Up One Level](CSJ_Tutorial.10.md) | [Next](CSJ_Tutorial.12.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
