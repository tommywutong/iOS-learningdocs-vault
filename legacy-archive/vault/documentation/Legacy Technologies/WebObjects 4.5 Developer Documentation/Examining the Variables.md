---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.34.html
archived_at: '2026-07-15T08:07:49.098633Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Examining%20Your%20Project-2.md) [!](Examining%20Your%20Project-2.md) [!](Examining%20the%20Bindings.md)

---

#  Examining the Variables

1. 

   Double-click __Main.wo__ in Project Builder's Web Components category to open the Main component in WebObjects Builder.

   There are four variables in the object browser: the __application__ and __session__ variables that are available in all components and two others, __movie__ and __movieDisplayGroup__.

   The __movie__ variable is an enterprise object that represents a row fetched from the MOVIE table. __movieDisplayGroup__ is a _display group_--an object that interacts with a database, indirectly through classes in the Enterprise Objects Framework. Display groups are used to fetch, insert, update, and delete enterprise objects that are associated with a single entity. The entity of __movieDisplayGroup__ is Movie, which you specified in the wizard's "Choose an entity" page.
2. 

   In Project Builder, look at the class file __Main.java__ to see how __movie__ is declared.

   The __movie__ declaration (shown below) declares __movie__ to be an EOEnterpriseObject--a Java interface that describes the general behavior that all enterprise objects must have.

   /\*\* @TypeInfo Movie \*/

   protected EOEnterpriseObject movie;

   At runtime, __movie__ is a EOGenericRecord object. Recall that EOGenericRecord is used to represent enterprise objects unless you specify a custom class. Since you didn't check the "Use custom enterprise objects" box in the wizard's "Choose what to include in your model" page, your application uses EOGenericRecord for all its entities.

   The comment (/\*\* @TypeInfo Movie \*/) is used by WebObjects Builder to identify __movie__'s entity (Movie). Knowing the entity allows WebObjects Builder to display __movie__'s attributes (__category__, __dateReleased__, and so on). You can see __movie__'s attributes if you select the __movie__ variable in the WebObjects Builder's object browser.
3. 

   In Project Builder, examine the __movieDisplayGroup__ declaration in __Main.java__.

   The declaration (shown below) declares __movieDisplayGroup__ to be a WODisplayGroup.

   protected WODisplayGroup movieDisplayGroup;

   Also note the comment explaining how __movieDisplayGroup__ is initialized. The __Main.java__ class doesn't have any code to create and initialize the display group. Instead, it's instantiated from an archive file, __Main.woo__, that's stored in the __Main.wo__ component. You shouldn't edit __woo__ files by hand; they're maintained by WebObjects Builder. The __woo__ file archiving mechanism is described in more detail later in [Specifying a Sort Order](Specifying%20a%20Sort%20Order.md#apple-ge2dmmru)
   .

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Examining%20Your%20Project-2.md) [!](Examining%20Your%20Project-2.md) [!](Examining%20the%20Bindings.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
