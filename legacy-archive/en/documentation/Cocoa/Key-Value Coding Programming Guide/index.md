---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html
archived_at: '2026-07-15T07:16:17.113389Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## About Key-Value Coding

Key-value coding is a mechanism enabled by the `NSKeyValueCoding` informal protocol that objects adopt to provide indirect access to their properties. When an object is key-value coding compliant, its properties are addressable via string parameters through a concise, uniform messaging interface. This indirect access mechanism supplements the direct access afforded by instance variables and their associated accessor methods.

You typically use accessor methods to gain access to an object’s properties. A get accessor (or getter) returns the value of a property. A set accessor (or setter) sets the value of a property. In Objective-C, you can also directly access a property’s underlying instance variable. Accessing an object property in any of these ways is straightforward, but requires calling on a property-specific method or variable name. As the list of properties grows or changes, so also must the code which accesses these properties. In contrast, a key-value coding compliant object provides a simple messaging interface that is consistent across all of its properties.

Key-value coding is a fundamental concept that underlies many other Cocoa technologies, such as key-value observing, Cocoa bindings, Core Data, and AppleScript-ability. Key-value coding can also help to simplify your code in some cases.

### Using Key-Value Coding Compliant Objects

Objects typically adopt key-value coding when they inherit from `NSObject` (directly or indirectly), which both adopts the `NSKeyValueCoding` protocol and provides a default implementation for the essential methods. Such an object enables other objects, through a compact messaging interface, to do the following:

- __Access object properties.__ The protocol specifies methods, such as the generic getter [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) and the generic setter [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue), for accessing object properties by their name, or key, parameterized as a string. The default implementation of these and related methods use the key to locate and interact with the underlying data, as described in [Accessing Object Properties](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq).
- __Manipulate collection properties.__ The default implementations of the access methods work with an object’s collection properties (such as `NSArray` objects) just like any other property. In addition, if an object defines collection accessor methods for a property, it enables key-value access to the contents of the collection. This is often more efficient than direct access and allows you to work with custom collection objects through a standardized interface, as described in [Accessing Collection Properties](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq).
- __Invoke collection operators on collection objects.__ When accessing a collection property in a key-value coding compliant object, you can insert a _collection operator_ into the key string, as described in [Using Collection Operators](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq). Collection operators instruct the default `NSKeyValueCoding` getter implementation to take an action on the collection, and then return either a new, filtered version of the collection, or a single value representing some characteristic of the collection.
- __Access non-object properties.__ The default implementation of the protocol detects non-object properties, including both scalars and structures, and automatically wraps and unwraps them as objects for use on the protocol interface, as described in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq). In addition, the protocol declares a method allowing a compliant object to provide a suitable action for the case when a `nil` value is set on a non-object property through the key-value coding interface.
- __Access properties by key path.__ When you have a hierarchy of key-value coding compliant objects, you can use key path based method calls to drill down, getting or setting a value deep within the hierarchy using a single call.

### Adopting Key-Value Coding for an Object

In order to make your own objects key-value coding compliant, you ensure that they adopt the `NSKeyValueCoding` informal protocol and implement the corresponding methods, such as [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) as a generic getter and [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue) as a generic setter. Fortunately, as described above, [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSObject/Description.html#//apple_ref/occ/intf/NSObject) adopts this protocol and provides default implementations for these and other essential methods. Therefore, if you derive your objects from `NSObject` (or any of its many subclasses), much of the work is already done for you.

In order for the default methods to do their work, you ensure your object’s accessor methods and instance variables adhere to certain well-defined patterns. This allows the default implementation to find your object’s properties in response to key-value coded messages. You then optionally extend and customize key-value coding by providing methods for validation and for handling certain special cases.

### Key-Value Coding with Swift

Swift objects that inherit from `NSObject` or one of its subclasses are key-value coding compliant for their properties by default. Whereas in Objective-C, a property’s accessors and instance variables must follow certain patterns, a standard property declaration in Swift automatically guarantees this. On the other hand, many of the protocol’s features are either not relevant or are better handled using native Swift constructs or techniques that do not exist in Objective-C. For example, because all Swift properties are objects, you never exercise the default implementation’s special handling of non-object properties.

Therefore, while the key-value coding protocol methods translate straightforwardly to Swift, this guide focuses primarily on Objective-C, where you need to do more to ensure compliance, and where key-value coding is often most useful. Situations that call for a significantly different approach in Swift are noted throughout the guide.

For more information about using Swift with Cocoa technologies, read _Using Swift with Cocoa and Objective-C (Swift 3)_. For a complete description of Swift, read _The Swift Programming Language (Swift 3)_.

### Other Cocoa Technologies Rely on Key-Value Coding

An object that is key-value coding compliant can participate in a wide range of Cocoa technologies that depend upon this kind of access, including:

- __Key-value observing.__ This mechanism enables objects to register for asynchronous notifications driven by changes in another object’s properties, as described in _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_.
- __Cocoa bindings.__ This collection of technologies fully implement a Model-View-Controller paradigm, where models encapsulate application data, views display and edit that data, and controllers mediate between the two. Read _[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ to learn more about Cocoa Bindings.
- __Core Data.__ This framework provides generalized and automated solutions to common tasks associated with object life cycle and object graph management, including persistence. You can read about Core Data in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.
- __AppleScript.__ This scripting language enables direct control of scriptable apps and of many parts of macOS. Cocoa’s scripting support takes advantage of key-value coding to get and set information in scriptable objects. The methods in the `NSScriptKeyValueCoding` informal protocol provide additional capabilities for working with key-value coding, including getting and setting key values by index in multi-value keys and coercing (or converting) a key-value to the appropriate data type. _[AppleScript Overview](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_ provides a high-level overview of AppleScript and its related technologies.

[Accessing Object Properties](BasicPrinciples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3talkciffekqkjivcq)
