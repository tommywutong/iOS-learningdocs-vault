---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/ModelEditor2.html
archived_at: '2026-07-18T01:18:36.977479Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Using%20the%20Model%20Editor.md) [!Previous Section](The%20Model%20Editor%20in%20Table%20Mode.md)

# Navigating a Model With the Tree View

You navigate a model by clicking icons in the Model Editor's tree view. In [Figure 12](#apple-he2tm), the icon labeled Movies (in the upper left corner of the tree view) represents the model itself. You double-click this icon to expand and contract the tree view. When the tree view is expanded, it shows the model's entities.

!

Figure 12. Expanding the Tree View

Similarly, you can expand a model's entities and stored procedures folder. As shown in [Figure 12](#apple-he2tm), expanding an entity displays the entity's relationships. A relationship in the tree view represents the relationship's destination entity. Expanding the relationship in the tree view in displays the destination entity's relationships, and so on. Expanding the stored procedures folder displays the model's stored procedures.

You control what's displayed in the Model Editor's table by selecting icons in the tree view. When the model is selected (as shown in [Figure 13](#apple-gezdsmju)), the Model Editor displays the model's entities in the table. To display an entity's attributes and relationships in the table, select the entity. Similarly, to display a stored procedure's attributes, select it.

!

Figure 13. Changing the Table's Contents

You can also use the icons in the tree view in drag and drop operations-for example, to drag an entity into the Data Browser (described in the chapter[Interacting with a Database](Interacting%20with%20a%20Database.md#apple-ge2tmnzr)) or into WebObjects Builder (described in the chapter "Creating a WebObjects Database Application" in the book _Getting Started with WebObjects_).

[!Table of Contents](Using%20the%20Model%20Editor.md) [!Next Section](Displaying%20a%20Model%27s%20Components%20in%20the%20Table%20Mode.md)
