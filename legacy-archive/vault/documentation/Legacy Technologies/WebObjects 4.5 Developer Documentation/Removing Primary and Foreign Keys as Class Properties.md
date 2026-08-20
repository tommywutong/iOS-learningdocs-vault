---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.1d.html
archived_at: '2026-07-15T08:08:55.671806Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Verifying%20and%20Modifying%20the%20Model.md) [!](Assigning%20Primary%20Keys.md) [!](Creating%20the%20User%20Interface.md)

---

#  Removing Primary and Foreign Keys as Class Properties

By default, EOModeler makes class properties for all of an entity's attributes (except for non-database attributes that you add to the entity). When an attribute is a class property, it means that the property will be included in your class definition and that it can be fetched from the database. To put it another way, only attributes that are marked as class properties become part of your enterprise objects.

You should only mark as class properties those attributes whose values are meaningful in the objects that are created when you fetch from the database. Attributes that are essentially database artifacts, such as primary and foreign keys, shouldn't be marked as class properties unless the key has meaning to the user and must be displayed in the user interface. For more discussion of primary and foreign keys, see the section [Adding Relationships](Adding%20Relationships.md#apple-gm3dmmrt)
.

Eliminating primary and foreign keys as class properties has no adverse effect on how Enterprise Objects Framework manages enterprise objects in your application.

1. 

   Remove primary and foreign keys as class properties.

   In the model-entity view of the Model Editor, select the entity you want to modify.

   Identify an attribute (typically a primary or foreign key) that you do not want to be a class property

   Click the diamond icon next to the attribute to remove it as a server-side class property.

   Click the double-arrow icon next to the attribute to remove it as a client-side class property.

   Save the model by choosing Save from the Model menu.

   !

You'll be returning to EOModeler to enhance your model in later exercises, but for now you're ready to build the first stage of the StudioManager application.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Verifying%20and%20Modifying%20the%20Model.md) [!](Assigning%20Primary%20Keys.md) [!](Creating%20the%20User%20Interface.md)
