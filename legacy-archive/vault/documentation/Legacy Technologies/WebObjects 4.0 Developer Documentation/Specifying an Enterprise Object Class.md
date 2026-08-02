---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/Entities3.html
archived_at: '2026-07-18T01:18:13.851818Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Working%20with%20Entities.md) [!Previous Section](Using%20the%20Entity%20Inspector.md)

# Specifying an Enterprise Object Class

Specifying an enterprise object class for an entity applies the mapping defined in your model to your custom class, thereby enabling objects of the class to be created from database rows.
To specify the enterprise object class for an entity:

- Make sure that each of the properties you want to include in your enterprise object class has a Class Property icon set for it in the Inspector.
- If the entity does not already have a primary key specified, add a Primary Key icon for the property or properties that constitute the entity's primary key.

Remember that the primary key or keys you set for your enterprise object class must mirror the primary key or keys defined for the corresponding table in the database.

What you do after this point depends on how you plan to implement your enterprise object class. In all cases, an enterprise object class must conform to the EOKeyValueCoding interface (or informal protocol in Objective-C), which specifies methods for accessing values by name, or _key_ ("keys" in this context relates to key-value pairs, not to primary keys). But this can be accomplished very differently, depending on the approach you use.
You can use either of the following approaches, depending on the needs of your application:

- Use EOGenericRecord.

If you don't edit the Class field to specify a name for a custom class, the Framework uses EOGenericRecord as an enterprise object class by default. A generic record uses a dictionary to store key-value pairs that correspond to an entity's properties and the data associated with each property. Use EOGenericRecord when you don't need to define special behavior for your class.

- Create a custom class that uses the default implementation of key-value coding. If you plan to create a custom class, you must type its name in the Class field.

You can also use EOModeler to generate source code for your class; the resulting source files include definitions of instance variables and accessor methods that can be used by key-value coding. See[Generating Source Files](Generating%20Source%20Files.md#apple-geytona).

For more information on key-value coding and implementing enterprise object classes, see the chapter Designing Enterprise Objects in the book _Enterprise Objects Framework Developer's Guide_.

[!Table of Contents](Working%20with%20Entities.md) [!Next Section](Generating%20Source%20Files.md)
