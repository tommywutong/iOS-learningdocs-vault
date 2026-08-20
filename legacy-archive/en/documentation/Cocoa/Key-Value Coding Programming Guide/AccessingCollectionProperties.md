---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessingCollectionProperties.html
archived_at: '2026-07-15T07:16:10.051889Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Accessing Collection Properties

Key-value coding compliant objects expose their to-many properties in the same way that they expose other properties. You can get or set a collection object just as you would any other object using `valueForKey:` and `setValue:forKey:` (or their key path equivalents). However, when you want to manipulate the content of these collections, it’s usually most efficient to use the mutable proxy methods defined by the protocol.

The protocol defines three different proxy methods for collection object access, each with a key and a key path variant:

- [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) and [mutableArrayValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1414937-mutablearrayvalueforkeypath)

  These return a proxy object that behaves like an `NSMutableArray` object.
- [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) and [mutableSetValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1408115-mutablesetvalue)

  These return a proxy object that behaves like an `NSMutableSet` object.
- [mutableOrderedSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415479-mutableorderedsetvalue) and [mutableOrderedSetValueForKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1407188-mutableorderedsetvalue)

  These return a proxy object that behaves like an `NSMutableOrderedSet` object.

When you operate on the proxy object, adding objects to, removing objects from, or replacing objects in it, the default implementation of the protocol modifies the underlying property accordingly. This is more efficient than obtaining a non-mutable collection object with `valueForKey:`, creating a modified one with altered content, and then storing it back to the object with a `setValue:forKey:` message. In many cases, it is also more efficient than working directly with a mutable property. These methods provide the additional benefit of maintaining key-value observing compliance for the objects held in the collection object (see _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ for details.

[Accessing Object Properties](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)

[Using Collection Operators](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)
