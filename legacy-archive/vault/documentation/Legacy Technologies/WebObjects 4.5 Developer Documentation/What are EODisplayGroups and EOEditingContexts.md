---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.42.html
archived_at: '2026-07-15T08:09:16.674737Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20a%20Model.md) [!](What%20is%20an%20Association.md)

---

#   What  are EODisplayGroups and EOEditingContexts?

####  EODisplayGroup

EODisplayGroups transport values between an enterprise object and a user interface object. You also need an EODatabaseDataSource, which acts on behalf of the EODisplayGroup to fetch enterprise objects from the database. In combination, EODisplayGroup and EODatabaseDataSource coordinate the flow of data between the user interface and the database. The EODisplayGroup that's created when you drag an entity from EOModeler into Interface Builder is actually a compound object that consists of both an EODisplayGroup and an EODatabaseDataSource.

####  EOEditingContext

When you drag an entity into the nib file window from your model, an EOEditingContext object is added to your application along with the EODisplayGroup that's created from the entity. An EOEditingContext manages the graph of enterprise objects in your application. The EOEditingContext is responsible for ensuring that all parts of your application stay in sync. When an enterprise object changes, the EOEditingContext broadcasts a notification so that other parts of the application (such as the user interface) can update themselves accordingly. The EOEditingContext also manages undo, and is the object through which you save changes to the database. For more information, see the EOEditingContext class specification in the _Enterprise Objects Framework Reference_.

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Enterprise%20Objects%20Framework%20Concepts.md) [!](What%20is%20a%20Model.md) [!](What%20is%20an%20Association.md)
