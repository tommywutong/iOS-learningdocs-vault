---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DynamicElements8.html
archived_at: '2026-07-18T01:26:29.043063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DynamicElements7-2.md)

### Creating a Detail Display Group

While a display group manages objects associated with a single entity, you can access other kinds of objects through an entity's relationships. In a _master-detail_ configuration, a master display group holds enterprise objects for the source of a relationship, while a detail display group holds records for the destination. As individual records are selected in the master display group, the detail display group gets a new set of enterprise objects to correspond to the selection in the master.
To create a detail display group, you can use the Display Group Options panel:

- Check "Has detail data source."

The Master Entity pop-up list is enabled. It lists all entities in the models in your project.

- Select the Master Entity from the pop-up list.

The Detail Key pop-up list now contains the keys representing the master entity's relationships.

- Select the Detail Key from the pop-up list.

You can also create a detail display group by dragging a to-many relationship from EOModeler into your component.!

As with other display groups, you can use the Display Group Options panel to immediately configure the newly created display group.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Binding%20Elements-2.md)
