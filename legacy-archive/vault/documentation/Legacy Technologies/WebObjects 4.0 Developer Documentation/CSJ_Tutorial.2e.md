---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.2e.html
archived_at: '2026-07-15T07:59:57.188204Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.2d.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2f.md)

##   What is an Association?

In the previous exercise, when you made a connection from the pop-up list to an EODisplayGroup, you formed an _association_
. Associations were also involved when you created a table view by dragging an entity from EOModeler into Interface Builder--the associations were formed for you as a by-product of dragging in the entity.

EODisplayGroups use associations (EOAssociations) to mediate between enterprise objects and the user interface. An association ties a single user interface object, such as a table column, to a key (a named property) in an enterprise object or objects managed by the EODisplayGroup.

Associations keep the user interface synchronized with enterprise object values. When an object changes, its display in the user interface updates to reflect the change. Likewise, when the user edits the user interface, the values in the object are updated accordingly.

Associations can have multiple _aspects_
. For example, in the preceding exercise you selected the __titles__
aspect for the EOPopupAssociation to display all of the class keys whose values you could choose to display in the pop-up list. EOPopupAssociation also has several other aspects: __selectedTitle__
__,__
__selectedTag__
__,__
__selectedObject__
, and __enabled__
.

Enterprise Objects Framework includes associations for different types of user interface objects, such as table columns, text fields, pop-up lists, and so on. Each association has multiple aspects.

For a complete discussion of this subject and a listing of all possible associations, see the EOAssociation class and subclass specifications in the _Enterprise Objects Framework Reference_
.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.2d.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.2f.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
