---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies31.html
archived_at: '2026-07-18T01:22:32.162899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Refining%20Your%20Model.md)

## Removing Primary and Foreign Keys as Class Properties

By default, the wizard makes all of an entity's attributes, except primary keys, _class properties_. When an attribute is a class property, it means that the property is a part of your enterprise object, usually as an instance variable.
You should mark as class properties only those attributes whose values are meaningful in the objects that are created when you fetch from the database. Attributes that are essentially database artifacts, such as primary and foreign keys, shouldn't be marked as class properties unless the key has meaning to the user and must be displayed in the user interface.
Eliminating primary and foreign keys as class properties has no adverse effect on how Enterprise Objects Framework manages enterprise objects in your application.

- In the left frame (or _tree view_), click the Movie entity.

The right frame switches from a view of the entities in the model to a view of Movie's attributes.

- Click in the Class Property column to remove the !
  symbol for the __studioId__ attribute (the wizard already removed __movieId__ as a class property).
!- In the MovieRole entity, remove __movieId__ and __talentId__ as class properties.
- If you are using OpenBase Lite, remove the __RowId__ attributes from the Movie, MovieRole, and Talent entities, since they are not used in this tutorial.

While __RowId__ is selected, choose Cut from the Edit menu.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies32.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
