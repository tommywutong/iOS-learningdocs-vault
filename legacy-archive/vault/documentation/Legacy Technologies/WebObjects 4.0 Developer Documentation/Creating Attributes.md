---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/CreatingAttributes.html
archived_at: '2026-07-18T01:28:11.029959Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOAttribute.md)
[!](Mapping%20Attributes.md)

---

# Creating Attributes

An attribute may be simple, derived, or flattened. A simple attribute typically corresponds to a single column in the database, and may be read or updated directly from or to the database. A simple EOAttribute may also be set as read-only with its [`setReadOnly`](../EOAttribute.md#apple-hezto) method. Read-only attributes of enterprise objects are never updated.

A derived attribute doesn't necessarily correspond to a single database column in its entity's database table, and is usually based on some other attribute, which is modified in some way. For example, if an Employee entity has a simple monthly salary attribute, you can define a derived `annualSalary` attribute as "salary \* 12". Derived attributes, since they don't correspond to actual values in the database, are read-only; it makes no sense to write a derived value.

A flattened attribute of an entity is actually an attribute of some other entity that's fetched through a relationship with a database join. A flattened attribute's external definition is a data path ending in an attribute name. For example, if the Employee entity has the relationship `toAddress` and the Address entity has the attribute `street`, you can define `streetName` as an attribute of your Employee EOEntity by creating an EOAttribute for it with a definition of "toAddress.street".

---

## Creating a Simple Attribute

A simple attribute needs at least the following characteristics:

- A name unique within its EOEntity
- The name of a column in the database table for its entity (the EOAttribute's external name)
- A declaration of the type of that column as defined by the database and adaptor (the EOAttribute's external type)
- A declaration of the Java class used to represent values outside the context of an enterprise object
- For Java value classes that require it, a subtype for such distinctions as between numeric types

You also have to set whether the attribute is part of its entity's primary key, is a class property, or is used for locking. See the EOEntity class description for more information.

---

## Creating a Derived Attribute

A derived attribute depends on another attribute, so you base it on a definition including that attribute's name rather than on an external name. Because a derived attribute isn't mapped directly to anything in the database, you shouldn't include it in the entity's set of primary key attributes or attributes used for locking.

---

## Creating a Flattened Attribute

A flattened attribute depends on a relationship, so you base it on a definition including that relationship's name rather than on an external name. Because a flattened attribute doesn't correspond directly to anything in its entity's table, you don't have to specify an external name, and shouldn't include it in the entity's set of primary key attributes or attributes used for locking.

Instead of flattening attributes in your model, a better approach is often to directly traverse the object graph through relationships. See the chapter "Using EOModeler" in the _Enterprise Objects Framework Developer's Guide_ for a discussion on when to use flattened attributes.

****

---

[!](EOAttribute.md)
[!](Mapping%20Attributes.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
