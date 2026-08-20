---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.47.html
archived_at: '2026-07-15T08:10:43.201692Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](Adding%20Display%20Groups.md) [!](Configuring%20the%20Display%20Group.md) [!](Binding%20Elements-2.md)

---

#   Creating a Detail Display Group

While a display group manages objects associated with a single entity, you can access other kinds of objects through an entity's relationships. In a _master-detail_
configuration, a master display group holds enterprise objects for the source of a relationship, while a detail display group holds records for the destination. As individual records are selected in the master display group, the detail display group gets a new set of enterprise objects to correspond to the selection in the master.

To create a detail display group, you can use the Display Group Options panel:

1. 

   Check "Has detail data source."

   The Master Entity pop-up list is enabled. It lists all entities in the models in your project.
2. 

   Select the Master Entity from the pop-up list.

   The Detail Key pop-up list now contains the keys representing the master entity's relationships.
3. 

   Select the Detail Key from the pop-up list.

You can also create a detail display group by dragging a to-many relationship from EOModeler into your component.

!

As with other display groups, you can use the Display Group Options panel to immediately configure the newly created display group.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](Adding%20Display%20Groups.md) [!](Configuring%20the%20Display%20Group.md) [!](Binding%20Elements-2.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
