---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Relationships.html
archived_at: '2026-07-15T07:16:15.084456Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Describing Property Relationships

Class descriptions provide a method of describing the to-one and to-many properties in a class. Defining these relationships between class properties allows for more intelligent and flexible manipulation of these properties with key-value coding.

### Class Descriptions

`NSClassDescription` is a base class that provides the interface for obtaining meta-data about classes. A class description object records the available attributes of objects of a particular class and the relationships (one-to-one, one-to-many, and inverse) between objects of that class and other objects. For example the `attributeKeys` method returns the list of all attributes defined for a class; the methods `toManyRelationshipKeys` and `toOneRelationshipKeys` return arrays of keys that define to-many and to-one relationships; and `inverseRelationshipKey:` returns the name of the relationship pointing back to the receiver from the destination of the relationship for the provided key.

`NSClassDescription` does not define methods for defining the relationships. Concrete subclasses must define these methods. Once created, you register a class description with the NSClassDescription `registerClassDescription:forClass:` class method.

`NSScriptClassDescription` is the only concrete subclass of NSClassDescription provided in Cocoa. It encapsulates an application’s scripting information.

[Adding Validation](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba)

[Designing for Performance](Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tklkdjjbeiqsiinba)
