---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.43.html
archived_at: '2026-07-15T08:09:16.706866Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md) [!](When%20Do%20You%20Use%20a%20Custom%20Enterprise%20Object%20Class.md)

---

#   What is an Association?

In the previous exercise, when you made a connection from the pop-up list to an EODisplayGroup, you formed an _association_
. Associations were also involved when you created a table view by dragging an entity from EOModeler into Interface Builder--the associations were formed for you as a by-product of dragging in the entity.

EODisplayGroups use associations (EOAssociations) to mediate between enterprise objects and the user interface. An association ties a single user interface object, such as a table column, to a key (a named property) in an enterprise object or objects managed by the EODisplayGroup.

Associations keep the user interface synchronized with enterprise object values. When an object changes, its display in the user interface updates to reflect the change. Likewise, when the user edits the user interface, the values in the object are updated accordingly.

Associations can have multiple _aspects_
. For example, in the preceding exercise you selected the __titles__ aspect for the EOPopupAssociation to display all of the class keys whose values you could choose to display in the pop-up list. EOPopupAssociation also has several other aspects: __selectedTitle____,__
__selectedTag____,__
__selectedObject__, and __enabled__.

Enterprise Objects Framework includes associations for different types of user interface objects, such as table columns, text fields, pop-up lists, and so on. Each association has multiple aspects.

For a complete discussion of this subject and a listing of all possible associations, see the EOAssociation class and subclass specifications in the _Enterprise Objects Framework Reference_.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20are%20EODisplayGroups%20and%20EOEditingContexts.md) [!](When%20Do%20You%20Use%20a%20Custom%20Enterprise%20Object%20Class.md)
