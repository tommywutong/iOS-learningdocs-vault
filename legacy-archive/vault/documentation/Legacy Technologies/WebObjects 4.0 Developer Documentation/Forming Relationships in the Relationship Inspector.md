---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Relationships3.html
archived_at: '2026-07-18T01:18:45.660895Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20Relationships.md) [!Previous Section](Forming%20Relationships%20in%20the%20Diagram%20View.md)

# Forming Relationships in the Relationship Inspector

Creating a relationship with the Relationship Inspector is a more manual process than creating one in the diagram view. The inspector provides only the ability to configure a relationship that already exists. Consequently, unlike with the diagram view, you have to create a relationship before you can edit it with the Relationship Inspector.

- Select a source entity in the Model Editor, such as Movie.
- Choose Property ! Add Relationship.

!

Figure 25. Adding a Relationship

Alternatively, you can click the ! button in the toolbar. In either case, the text "Relationship" appears in the relationship table at the bottom of the window.

- Select the new relationship in the Model Editor.
- Open the Relationship Inspector, either from the toolbar or by choosing Tools ! Inspector.

!

Figure 26. The Relationship Inspector

- In the Inspector, select the destination entity (Studio) in the Destination browser.

Typically, you form a relationship by connecting a primary key in one entity and a corresponding foreign key in another entity. In a to-one relationship, the source entity usually holds the foreign key, while the destination entity holds the primary key. The opposite is true for a to-many relationship. For example, __studioId__ is a foreign key for Movie, while it's the primary key for Studio.

- Select the source attribute (__studioId__) in the Source Attributes browser.
- Select the destination attribute (__studioId__) in the Destination Attributes browser
- Make sure the relationship has the proper cardinality (in this example it should be set to To One since a movie has only one Studio).
- Click Connect.

EOModeler assigns the relationship a default name; in this example it's "studio." You can edit this name if desired using either the Inspector or the table view.

[!Table of Contents](Creating%20Relationships.md) [!Next Section](Forming%20Relationships%20Across%20Models%20and%20Databases.md)
