---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies14.html
archived_at: '2026-07-15T07:54:13.697826Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies13.md)

## Examining the Variables

- Double-click __Main.wo__ in Project Builder's WebObjects Components category to open the Main component in WebObjects Builder.

There are four variables in the object browser: the __application__ and __session__ variables that are available in all components and two others, __movie__ and __movieDisplayGroup__.

The __movie__ variable is an enterprise object that represents a row fetched from the MOVIE table. __movieDisplayGroup__ is a _display group_-an object that interacts with a database, indirectly through classes in the Enterprise Objects Framework. Display groups are used to fetch, insert, update, and delete enterprise objects that are associated with a single entity. __movieDisplayGroup__'s entity is Movie, which you specified in the wizard's "Choose an entity" page.

- In Project Builder, look at the class file __Main.java__ to see how __movie__ is declared.

The __movie__ declaration (shown below) declares __movie__ to be an EnterpriseObject-a Java interface that describes the general behavior that all enterprise objects must have.

```
/** @TypeInfo Movie */ protected EnterpriseObject movie;
```


At run time, __movie__ is a GenericRecord object. Recall that GenericRecord is used to represent enterprise objects unless you specify a custom class. Since you didn't check the "Use custom enterprise objects" box in the wizard's "Choose what to include in your model" page, your application defaults to using GenericRecord for all its entities.

The comment (/\*\* @TypeInfo Movie \*/) is used by WebObjects Builder to identify __movie__'s entity (Movie). Knowing the entity allows WebObjects Builder to display __movie__'s attributes (__category__, __dateReleased__, and so on). You can see __movie__'s attributes if you select the __movie__ variable in the WebObjects Builder's object browser.

- In Project Builder, examine __movieDisplayGroup__'s declaration in __Main.java__.

The declaration (shown below) declares __movieDisplayGroup__ to be a DisplayGroup.

```
protected DisplayGroup movieDisplayGroup;
```


Also note the comment explaining how __movieDisplayGroup__ is initialized. The __Main.java__ class doesn't have any code to create and initialize the display group. Instead, it's instantiated from an archive file, __Main.woo__, that's stored in the __Main.wo__ component. You shouldn't edit __woo__ files by hand; they're maintained by WebObjects Builder. The __woo__ file archiving mechanism is described in more detail later in ["Specifying a Sort Order"](Movies20.md#apple-ge2deoju).

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies15.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
