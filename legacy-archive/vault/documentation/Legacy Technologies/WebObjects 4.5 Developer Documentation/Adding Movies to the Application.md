---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.27.html
archived_at: '2026-07-15T08:09:03.601316Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Adding%20Relationships.md) [!](Adding%20Relationships.md) [!](Creating%20a%20Master-Detail%20Interface.md)

---

#  Adding Movies to the Application

The relationships you specified in EOModeler now come into play in your application. In EOModeler you added a to-many relationship from Studio to Movie, because a Studio can have many Movies. You can now use this relationship to display the movies for the selected studio.

In this type of configuration, called 

master-detail, the master table holds records for the source of the relationship, while the detail table holds records for the destination. As individual records in the master table are selected, the contents of the detail table change to show the records that correspond to the selection in the master. In the StudioManager application, Studio is the master table and Movie is the detail table.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Adding%20Relationships.md) [!](Adding%20Relationships.md) [!](Creating%20a%20Master-Detail%20Interface.md)
