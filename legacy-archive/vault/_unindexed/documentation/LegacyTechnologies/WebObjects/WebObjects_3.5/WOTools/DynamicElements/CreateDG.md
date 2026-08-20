---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/CreateDG.htm
archived_at: '2026-07-15T07:56:22.118028Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](ConfigDG.md)

### Creating a Detail Display Group

While a display group manages objects associated with a single entity, you can access other kinds of objects through an entity's relationships. In a _master-detail_ configuration, a master display group holds enterprise objects for the source of a relationship, while a detail display group holds records for the destination. As individual records are selected in the master display group, the detail display group gets a new set of enterprise objects to correspond to the selection in the master.
To create a detail display group, you can use the Display Group Options panel:

- Check "Has detail data source."

The Master Entity pop-up list is enabled. It lists the all entities in the models in your project.

- Select the Master Entity from the pop-up list.

The Detail Key pop-up list now contains the keys representing the master entity's relationships.

- Select the Detail Key from the pop-up list.

You can also create a detail display group by dragging a to-many relationship from EOModeler into your component.!

As with other display groups, you can use the Display Group Options panel to immediately configure the newly created display group.

[!Table of Contents](DynElTOC.md) [!Next Section](Binding.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
