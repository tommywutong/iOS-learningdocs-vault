---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.2c.html
archived_at: '2026-07-15T08:09:08.164840Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Generating%20Source%20Files.md)

---

#  Specifying Custom Enterprise Object Classes

If you create the model earlier with the help of the wizard, and choose the "Create Custom Enterprise objects" option, EOModeler derives both entity name and class name from the name of the associated database table. Otherwise, EOModeler maps entities to the EOGenericRecord class, which can be thought of as the default enterprise object class.

The EOGenericRecord class is sufficient when all you want the entity to do is get and set properties. However, when you want to add custom behavior to a class (for example, to assign default values when you create new objects or to perform validation), you need to implement a custom enterprise object class. This class includes the default behavior provided in EOGenericRecord as well as the custom behavior you implement.

1. 

   Specify custom enterprise object classes for the server and the client.

   In the Model Editor, select the model (StudioManager).

   If the Client-Side Class Name column is not visible, select Client-Side Class Name from the Add Column pull-down list at the bottom of the window.

   Select the Studio entity in the table.

   Double-click the Studio cell under Class Name.

   Type "businesslogic.server.Studio" in the cell ("businesslogic.server" is the package name).

   Double-click the adjoining cell under the Client-Side Class Name column.

   Type "businesslogic.client.Studio" in this cell ("businesslogic.client" is the package name).

   Repeat the above steps for the Talent entity (append "Talent" to the package names).

   !

For the StudioManager application, ensure that there are custom classes (with their package prefixes) corresponding to the appropriate entity; these classes should be named __businesslogic.server.Studio__
and __businesslogic.server.Talent__
under Class Name and __businesslogic.client.Studio__
and __businesslogic.client.Talent__
under Client-Side Class Name. Movie doesn't need to be a custom class since it doesn't have any specialized behavior. By convention, the names of classes (minus the package prefix) are based on the name of the corresponding entity and the initial letter of the name is capitalized.

There is no requirement that you create matching server and client classes. You can implement a class only on the server or the client, whichever suits your needs; the unimplemented class assumes the default behavior of EOGenericRecord.

Once you specify a custom class for an entity in EOModeler, you can generate source files for that entity.
__Related Concepts:__

[When Do You Use a Custom Enterprise Object Class?](When%20Do%20You%20Use%20a%20Custom%20Enterprise%20Object%20Class.md#apple-obtwmslehuytambwge2tc)

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md) [!](Generating%20Source%20Files.md)
