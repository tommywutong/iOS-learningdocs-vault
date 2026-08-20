---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.45.html
archived_at: '2026-07-15T08:08:05.964531Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Refining%20Your%20Model.md) [!](Opening%20Your%20Model.md) [!](Adding%20Relationships%20to%20Your%20Model.md)

---

#  Removing Foreign Keys as Class Properties

By default, the wizard makes all of an entity's attributes, except primary keys, _class properties_. When an attribute is a class property, it means that the property is a part of your enterprise object, usually as an instance variable.

You should mark as class properties only those attributes whose values are meaningful in the objects that are created when you fetch from the database. Attributes that are essentially database artifacts, such as primary and foreign keys, shouldn't be marked as class properties unless the key has meaning to the user and must be displayed in the user interface.

Eliminating primary and foreign keys as class properties has no adverse effect on how Enterprise Objects Framework manages enterprise objects in your application.

1. 

   In the left frame (or _tree view_), click the Movie entity.

   The right frame switches from a view of the entities in the model to a view of Movie's attributes.

   A ! symbol in the first column means that the attribute is a primary key for the selected entity. A ! symbol in the second column means that the attribute is a class property.
2. 

   Click in the Class Property column to remove the ! symbol for the __studioId__ attribute, which is a foreign key. The wizard didn't make __movieId__ a class property because it is a primary key.

!

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Refining%20Your%20Model.md) [!](Opening%20Your%20Model.md) [!](Adding%20Relationships%20to%20Your%20Model.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
