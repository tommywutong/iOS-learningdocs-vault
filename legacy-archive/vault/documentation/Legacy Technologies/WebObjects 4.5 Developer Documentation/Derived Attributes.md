---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/EOTools/DerivedProperties1.html
archived_at: '2026-07-15T08:03:49.611676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Tools and Techniques

[!Table of Contents](Adding%20Derived%20Properties.md) [!Previous Section](Adding%20Derived%20Properties.md)

# Derived Attributes

A derived attribute doesn't map directly to a single column in the root table of the entity. A derived attribute can be based on another attribute that's modified in some way, such as an __bonus__ attribute that's the result of a calculation performed on a __salary__ attribute. A derived attribute can also be an aggregate consisting of more than one attribute; for example, you can create a derived attribute __fullName__ that is an aggregate of __lastName__ and __firstName__.
Derived attributes, since they don't correspond to real values in the database, are read-only; it makes no sense to write a derived value.

## Adding a Derived Attribute

You can use the concept of derived attributes to add to an entity a new attribute that doesn't correspond to any database column. This attribute can contain a computed value, for example, or an aggregate of multiple attributes.
To add a new attribute to your entity:

- In the Model Editor, select the entity (such as Talent) to which you want to add an attribute.
- Choose Property ! Add Attribute.

Alternatively, you can use the ! button on the toolbar. In either case, a new attribute with the name "Attribute" appears in the entity's list of attributes.

- In the Attribute Inspector, edit the Name field to supply a new name for the attribute.

For example, you can create an attribute called __fullName__ that combines the __firstName__ and __lastName__ attributes.

Note that this is a contrived example. A safer way to achieve the same end would be to implement a method on your enterprise object-this would ensure that if the __firstName__ or __lastName__ attribute is modified, the derived attribute __fullName__ will immediately reflect the change.

- Use the pop-up list to the left of the Definition field to change the attribute type from Column to Derived.
- Edit the Definition field to supply the SQL needed to specify the derived attribute.

For example, to concatenate the __firstName__ and __lastName__ attributes in Oracle, type the text:

```
firstName||' '||lastName
```


The Sybase equivalent is:

```
firstName+' '+lastName
```

- In the External Type field, add the attribute's data type (VARCHAR2). This should be the data type as it is in the database.
- In the External Width field, type the width constraint for the attribute (this only applies to string and data values).

[Figure 29](#apple-ge2tgnzq) shows the Attribute Inspector with the new attribute __fullName__ specified.

!

Figure 29. Adding a Derived Attribute

The text you supply in the Definition field must be valid SQL for your database. While you can use either the internal or external names for simple attributes in this field, for derived and flattened attributes you have to use the internal names (flattened and derived attributes have no external names). For consistency's sake, you may want to use only internal names in this field.

[!Table of Contents](Adding%20Derived%20Properties.md) [!Next Section](Flattened%20Attributes.md)
