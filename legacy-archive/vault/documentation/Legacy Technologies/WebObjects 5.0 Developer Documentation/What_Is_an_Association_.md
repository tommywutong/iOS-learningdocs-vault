---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JavaClient/Concepts/What_Is_an_Association_.html
archived_at: '2026-07-15T08:13:58.326779Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Are_EO_ngContexts_.md)[![Next](attachments/JavaClient/Images/next.gif)](When_Do_You_ject_Class_.md)

## What Is an Association?

In the tutorial, when you made a connection from the pop-up
list to an EODisplayGroup, you formed an association. Associations
were also involved when you created a table view by dragging an
entity from EOModeler into Interface Builder-the associations
were formed for you as a by-product of dragging in the entity.

EODisplayGroups use associations (EOAssociations) to mediate
between enterprise objects and the user interface. An association
ties a single user interface object, such as a table column, to
a key (a named property) in an enterprise object or objects managed
by the EODisplayGroup.

Associations keep the user interface synchronized with enterprise
object values. When an object changes, its display in the user interface
updates to reflect the change. Likewise, when the user edits the
user interface, the values in the object are updated accordingly.

Associations can have multiple aspects. For example, in the
preceding exercise you selected the `titles` aspect
for the EOValueSelectionAssociation to display all of the class keys
whose values you could choose to display in the pop-up list. EOValueSelectionAssociation
also has several other aspects: `selectedTitle`, `selectedIndex`, `selectedObject`,
and `enabled`.

Enterprise Objects Framework includes associations for different
types of user interface objects, such as table columns, text fields,
pop-up lists, and so on. Each association has multiple aspects.

For a complete discussion of this subject and a listing of
all possible associations, see the EOAssociation class and subclass
specifications in the _Enterprise Objects Framework Reference_.

[![Previous](attachments/JavaClient/Images/previous.gif)](What_Are_EO_ngContexts_.md)[![Next](attachments/JavaClient/Images/next.gif)](When_Do_You_ject_Class_.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
