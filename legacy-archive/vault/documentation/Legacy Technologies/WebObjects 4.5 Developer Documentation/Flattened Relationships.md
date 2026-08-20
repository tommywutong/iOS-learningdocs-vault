---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/DerivedProperties3.html
archived_at: '2026-07-15T08:03:54.620551Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Adding%20Derived%20Properties.md) [!Previous Section](Flattened%20Attributes.md)

# Flattened Relationships

In addition to flattening attributes, you can also flatten relationships. Flattening a relationship gives a source entity access to relationships that a destination entity has with other entities. It's equivalent to performing a multi-table join. Note that flattening either an attribute or a relationship can result in degraded performance when the destination objects are accessed, since traversing multiple tables makes fetches slower.

## When Should You Use Flattened Relationships?

As discussed in [When Should You Use Flattened Attributes?](Flattened%20Attributes.md#apple-geydmny), flattening is a technique you should only use under certain conditions. Instead of flattening an attribute or a relationship, you can instead directly traverse the object graph, either programmatically or by using key paths. This ensures that your application has an internally consistent view of the data.

There is one scenario in which you might want to use a flattened relationship: if you're modeling a many-to-many relationship and you want to perform a multi-table hop to access a table that lies on the other side of an intermediate table. For example, in the Movie database, the Director table acts as an intermediate table between Movie and Talent. It's highly unlikely that you would ever need to fetch instances of Director into your application. In this situation, it makes sense to specify a relationship between Movie and Director, and flatten that relationship to give Movie access to the Talent table.

## Flattening a Relationship

To flatten a relationship:

- Add a relationship from one entity (_entity_1_) to a second entity (_entity_2_).

For example, you can add a to-many relationship called __toDirectors__ from Movie to Director since a movie can have more than one director.

- Add a relationship from _entity_2_ to a third entity (_entity_3_).

For example, you can add a to-one relationship called __talent__ from Director to Talent. For each director a movie has, there is a corresponding single entry in the Talent table.

- From _entity_1_, select the relationship to _entity_2_ to display its properties.

From Movie, select the relationship __toDirectors__ to display the properties of Director.

- In the list of properties for _entity_2_, select the relationship (__talent__) you want to flatten.
- Choose Property ! Flatten Property.

!

Figure 33. Flattening a Relationship

The flattened relationship (in this example, __toDirectors_talent__) appears in the list of properties for Movie. The format of the name reflects the traversal path: The relationship __talent__ is added to Movie by traversing the __toDirectors__ relationship.
[!Table of Contents](Adding%20Derived%20Properties.md) [!Next Section](Working%20with%20Entities.md)
