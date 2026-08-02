---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/ModelEditor3.html
archived_at: '2026-07-18T01:18:38.571399Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Using%20the%20Model%20Editor.md) [!Previous Section](Navigating%20a%20Model%20With%20the%20Tree%20View.md)

# Displaying a Model's Components in the Table Mode

The Model Editor's table changes depending on what's selected in the tree view. When the model itself is selected, the table displays the model's entities, one entity per row. The columns of the table display information about the entities-entity name, name of the corresponding database table, and so on.
When an entity is selected, the display changes to show two tables: one for the entity's attributes and one for the entity's relationships (shown in [Figure 14](#apple-geztembz)).

!

Figure 14. Displaying an Entity's Attributes and Relationships

## The Open Entity Icon

When the model is selected in the tree view and the table is displaying the model's entities, the Model Editor displays an ! icon to the left each entity in the table. Double-clicking this icon _opens_ that entity, selecting that entity and displaying its attributes and relationships in the table. You can accomplish the same thing by selecting the entity in the tree view.

!

Figure 15. Navigating from the Table View

## Adding Columns with the Add Column Menu

You use the Add Column menu to add columns to the table view. The items in the menu depend on what modeling component the table is displaying and on what columns the table contains. As you add columns to the table, the corresponding menu items are removed from the Add Column menu.

!

[!Table of Contents](Using%20the%20Model%20Editor.md) [!Next Section](Using%20Other%20Display%20Modes.md)
