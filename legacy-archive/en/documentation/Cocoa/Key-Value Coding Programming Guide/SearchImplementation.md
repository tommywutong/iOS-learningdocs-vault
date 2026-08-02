---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html
archived_at: '2026-07-15T07:16:16.112679Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Accessor Search Patterns

The default implementation of the `NSKeyValueCoding` protocol provided by `NSObject` maps key-based accessor calls to an object’s underlying properties using a clearly defined set of rules. These protocol methods use a key parameter to search their own object instance for accessors, instance variables, and related methods that follow certain naming conventions. Although you rarely modify this default search, it can be helpful to understand how it works, both for tracing the behavior of key-value coded objects, and for making your own objects compliant.

> [!NOTE]
> 

### Search Pattern for the Basic Getter

The default implementation of `valueForKey:`, given a `key` parameter as input, carries out the following procedure, operating from within the class instance receiving the `valueForKey:` call.

1. Search the instance for the first accessor method found with a name like `get<Key>`, `<key>`, `is<Key>`, or `_<key>`, in that order. If found, invoke it and proceed to step 5 with the result. Otherwise proceed to the next step.
2. If no simple accessor method is found, search the instance for methods whose names match the patterns `countOf<Key>` and `objectIn<Key>AtIndex:` (corresponding to the primitive methods defined by the `NSArray` class) and `<key>AtIndexes:` (corresponding to the [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) method `objectsAtIndexes:`).

   If the first of these and at least one of the other two is found, create a collection proxy object that responds to all `NSArray` methods and return that. Otherwise, proceed to step 3.

   The proxy object subsequently converts any `NSArray` messages it receives to some combination of `countOf<Key>`, `objectIn<Key>AtIndex:`, and `<key>AtIndexes:` messages to the key-value coding compliant object that created it. If the original object also implements an optional method with a name like `get<Key>:range:`, the proxy object uses that as well, when appropriate. In effect, the proxy object working together with the key-value coding compliant object allows the underlying property to behave as if it were an `NSArray`, even if it is not.
3. If no simple accessor method or group of array access methods is found, look for a triple of methods named `countOf<Key>`, `enumeratorOf<Key>`, and `memberOf<Key>:` (corresponding to the primitive methods defined by the [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet) class).

   If all three methods are found, create a collection proxy object that responds to all `NSSet` methods and return that. Otherwise, proceed to step 4.

   This proxy object subsequently converts any `NSSet` message it receives into some combination of `countOf<Key>`, `enumeratorOf<Key>`, and `memberOf<Key>:` messages to the object that created it. In effect, the proxy object working together with the key-value coding compliant object allows the underlying property to behave as if it were an `NSSet`, even if it is not.
4. If no simple accessor method or group of collection access methods is found, and if the receiver's class method [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) returns `YES``true`, search for an instance variable named `_<key>`, `_is<Key>`, `<key>`, or `is<Key>`, in that order. If found, directly obtain the value of the instance variable and proceed to step 5. Otherwise, proceed to step 6.
5. If the retrieved property value is an object pointer, simply return the result.

   If the value is a scalar type supported by `NSNumber`, store it in an `NSNumber` instance and return that.

   If the result is a scalar type not supported by NSNumber, convert to an `NSValue` object and return that.
6. If all else fails, invoke [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value). This raises an exception by default, but a subclass of `NSObject` may provide key-specific behavior.

### Search Pattern for the Basic Setter

The default implementation of `setValue:forKey:`, given `key` and `value` parameters as input, attempts to set a property named `key` to `value` (or, for non-object properties, the unwrapped version of `value`, as described in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)) inside the object receiving the call, using the following procedure:

1. Look for the first accessor named `set<Key>:` or `_set<Key>`, in that order. If found, invoke it with the input value (or unwrapped value, as needed) and finish.
2. If no simple accessor is found, and if the class method `accessInstanceVariablesDirectly` returns `YES``true`, look for an instance variable with a name like `_<key>`, `_is<Key>`, `<key>`, or `is<Key>`, in that order. If found, set the variable directly with the input value (or unwrapped value) and finish.
3. Upon finding no accessor or instance variable, invoke `setValue:forUndefinedKey:`. This raises an exception by default, but a subclass of `NSObject` may provide key-specific behavior.

### Search Pattern for Mutable Arrays

The default implementation of [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey), given a `key` parameter as input, returns a mutable proxy array for a property named `key` inside the object receiving the accessor call, using the following procedure:

1. Look for a pair of methods with names like `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:` (corresponding to the [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray) primitive methods [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:) and [removeObjectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectAtIndex:) respectively), or methods with names like `insert<Key>:atIndexes:` and `remove<Key>AtIndexes:` (corresponding to the [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray)[insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insertobjects) and [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects) methods).

   If the object has at least one insertion method and at least one removal method, return a proxy object that responds to `NSMutableArray` messages by sending some combination of `insertObject:in<Key>AtIndex:`, `removeObjectFrom<Key>AtIndex:`, `insert<Key>:atIndexes:`, and `remove<Key>AtIndexes:` messages to the original receiver of [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey).

   When the object receiving a [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) message also implements an optional replace object method with a name like `replaceObjectIn<Key>AtIndex:withObject:` or `replace<Key>AtIndexes:with<Key>:`, the proxy object utilizes those as well when appropriate for best performance.
2. If the object does not have the mutable array methods, look instead for an accessor method whose name matches the pattern `set<Key>:`. In this case, return a proxy object that responds to `NSMutableArray` messages by issuing a `set<Key>:` message to the original receiver of [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey).

   > [!NOTE]
   > 
3. If neither the mutable array methods, nor the accessor are found, and if the receiver's class responds `YES``true` to [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly), search for an instance variable with a name like `_<key>` or `<key>`, in that order.

   If such an instance variable is found, return a proxy object that forwards each `NSMutableArray` message it receives to the instance variable's value, which typically is an instance of `NSMutableArray` or one of its subclasses.
4. If all else fails, return a mutable collection proxy object that issues a [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) message to the original receiver of the [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) message whenever it receives an `NSMutableArray` message.

   The default implementation of setValue:forUndefinedKey: raises an `NSUndefinedKeyException`, but subclasses may override this behavior.

### Search Pattern for Mutable Ordered Sets

The default implementation of [mutableOrderedSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415479-mutableorderedsetvalue) recognizes the same simple accessor methods and ordered set accessor methods as `valueForKey:` (see [Default Search Pattern for the Basic Getter](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tkljrgm4demzu)), and follows the same direct instance variable access policies, but always returns a mutable collection proxy object instead of the immutable collection that `valueForKey:` returns. In addition, it does the following:

1. Search for methods with names like `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:` (corresponding to the two most primitive methods defined by the [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset) class), and also `insert<Key>:atIndexes:` and `remove<Key>AtIndexes:` (corresponding to [insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410287-insert) and [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1418161-removeobjectsatindexes)).

   If at least one insertion method and at least one removal method are found, the returned proxy object sends some combination of `insertObject:in<Key>AtIndex:`, `removeObjectFrom<Key>AtIndex:`, `insert<Key>:atIndexes:`, and `remove<Key>AtIndexes:` messages to the original receiver of the `mutableOrderedSetValueForKey:` message when it receives `NSMutableOrderedSet` messages.

   The proxy object also makes use of methods with names like `replaceObjectIn<Key>AtIndex:withObject:` or `replace<Key>AtIndexes:with<Key>:` when they exist in the original object.
2. If the mutable set methods are not found, search for an accessor method with a name like `set<Key>:`. In this case, the returned proxy object sends a `set<Key>:` message to the original receiver of `mutableOrderedSetValueForKey:` every time it receives a `NSMutableOrderedSet` message.

   > [!NOTE]
   > 
3. If neither the mutable set messages nor the accessor are found, and if the receiver’s [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) class method returns `YES``true`, search for an instance variable with a name like `_<key>` or `<key>`, in that order. If such an instance variable is found, the returned proxy object forwards any `NSMutableOrderedSet` messages it receives to the instance variable’s value, which is typically an instance of `NSMutableOrderedSet` or one of its subclasses.
4. If all else fails, the returned proxy object sends a `setValue:forUndefinedKey:` message to the original receiver of `mutableOrderedSetValueForKey:` whenever it receives a mutable set message.

   The default implementation of `setValue:forUndefinedKey:` raises an [NSUndefinedKeyException](https://developer.apple.com/documentation/foundation/nsexceptionname/1411656-undefinedkeyexception), but objects may override this behavior.

### Search Pattern for Mutable Sets

The default implementation of [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey), given a `key` parameter as input, returns a mutable proxy set for an array property named `key` inside the object receiving the accessor call, using the following procedure:

1. Search for methods with names like `add<Key>Object:` and `remove<Key>Object:` (corresponding to the [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) primitive methods [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObject:) and [removeObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/removeObject:) respectively) and also `add<Key>:` and `remove<Key>:` (corresponding to [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) methods [unionSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/unionSet:) and [minusSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/minusSet:)). If at least one addition method and at least one removal method are found, return a proxy object that sends some combination of `add<Key>Object:`, `remove<Key>Object:`, `add<Key>:`, and `remove<Key>:` messages to the original receiver of [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) for each [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) message it receives.

   The proxy object also makes use of the methods with a name like `intersect<Key>:` or `set<Key>:` for best performance, if they are available.
2. If the receiver of the [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) call is a managed object, the search pattern does not continue as it would for non-managed objects. See Managed Object Accessor Methods in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ for more information.
3. If the mutable set methods are not found, and if the object is not a managed object, search for an accessor method with a name like `set<Key>:`. If such a method is found, the returned proxy object sends a `set<Key>:` message to the original receiver of [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) for each `NSMutableSet` message it receives.

   > [!NOTE]
   > 
4. If the mutable set methods and the accessor method are not found, and if the [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) class method returns `YES``true`, search for an instance variable with a name like `_<key>` or `<key>`, in that order. If such an instance variable is found, the proxy object forwards each [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) message it receives to the instance variable's value, which is typically an instance of [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) or one of its subclasses.
5. If all else fails, the returned proxy object responds to any [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) message it receives by sending a [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) message to the original receiver of [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey).

[Validating Properties](ValidatingProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcobnknltc)

[Achieving Basic Key-Value Coding Compliance](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq)
