---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies31.html
archived_at: '2026-07-15T07:54:38.245340Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies30.md)

## Removing Primary and Foreign Keys as Class Properties

By default, EOModeler makes all of an entity's attributes _class properties_. When an attribute is a class property, it means that the property is a part of your enterprise object, usually as an instance variable.
You should mark as class properties only those attributes whose values are meaningful in the objects that are created when you fetch from the database. Attributes that are essentially database artifacts, such as primary and foreign keys, shouldn't be marked as class properties unless the key has meaning to the user and must be displayed in the user interface.
Eliminating primary and foreign keys as class properties has no adverse effect on how Enterprise Objects Framework manages enterprise objects in your application.

- In the left frame (or _tree view_), click the Movie entity.

The right frame switches from a view of the entities in the model to a view of Movie's attributes.

- Click in the Class Property column to remove the ! symbol for the __movieId__ attribute.
- Now repeat the previous step to remove __studioId__ as a class property.
!- In the MovieRole entity, remove __movieId__ and __talentId__ as class properties.
- In the Talent entity, remove __talentId__ as a class property.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies32.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
