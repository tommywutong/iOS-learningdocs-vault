---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/DefiningCollectionMethods.html
archived_at: '2026-07-15T07:16:13.583192Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Defining Collection Methods

When you create accessors and ivars using standard naming conventions, as described in [Achieving Basic Key-Value Coding Compliance](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq), the key-value coding protocol’s default implementation can locate them in response to key-value coded messages. This is as true for collection objects representing to-many relationships as it is for other properties. However, if you implement the collection accessor methods instead of, or in addition to, the basic accessors for a collection property, you can:

- __Model to-many relationships with classes other than NSArray or NSSet.__ When you implement the collection methods in your object, the default implementation of the key-value getter returns a proxy object that calls these methods in response to subsequent `NSArray` or `NSSet` messages that it receives. The underlying property object need not be an `NSArray` or `NSSet` itself, because the proxy object provides the expected behavior using your collection methods.
- __Achieve increased performance when mutating the contents of a to-many relationship.__ Instead of repeatedly creating new collection objects with the basic setter in response to every change, the protocol’s default implementation uses your collection methods to mutate the underlying property in place.
- __Provide key-value observing compliant access to the contents of your object’s collection properties.__ For more information about key-value observing, read _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_.

You implement one of two categories of collection accessors, depending on whether you want the relationship to behave like an indexed, ordered collection (like an `NSArray` object) or an unordered, uniqued collection (like an `NSSet` object). In either case, you implement at least one set of methods to support read access to the property, and then add an additional set to enable mutation of the collection’s contents.

> [!NOTE]
> 

### Accessing Indexed Collections

You add indexed accessor methods to provide a mechanism for counting, retrieving, adding, and replacing objects in an ordered relationship. The underlying object is often an instance of `NSArray` or `NSMutableArray`, but if you provide the collection accessors, you enable any object property for which you implement these methods to be manipulated as if it were an array.

### Indexed Collection Getters

For a collection property that has no default getter, if you provide the following indexed collection getter methods, the default implementation of the protocol, in response to a `valueForKey:` message, returns a proxy object that behaves like an `NSArray`, but calls the following collection methods to do its work.

> [!NOTE]
> 

- `countOf<Key>`

  This method returns the number of objects in the to-many relationship as an `NSUInteger`, just like the `NSArray` primitive method [count](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/count). In fact, when the underlying property is an `NSArray`, you use that method to provide a result.

  For example, for a to-many relationship representing a list of bank transactions and backed by an `NSArray` called `transactions`:

  1. `- (NSUInteger)countOfTransactions {`
  2. `return [self.transactions count];`
  3. `}`
- `objectIn<Key>AtIndex:` or `<key>AtIndexes:`

  The first returns the object at the specified index in the to-many relationship, while the second returns an array of objects at the indexes specified by the `NSIndexSet` parameter. These correspond to the `NSArray` methods [objectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectAtIndex:) and [objectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsarray/1411296-objectsatindexes), respectively. You only need to implement one of these. The corresponding methods for the `transactions` array are:

  1. `- (id)objectInTransactionsAtIndex:(NSUInteger)index {`
  2. `return [self.transactions objectAtIndex:index];`
  3. `}`
  5. `- (NSArray *)transactionsAtIndexes:(NSIndexSet *)indexes {`
  6. `return [self.transactions objectsAtIndexes:indexes];`
  7. `}`
- `get<Key>:range:`

  This method is optional, but can result in improved performance. It returns the objects from the collection that fall within the specified range, and corresponds to the `NSArray` method [getObjects:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:range:). The implementation for the transactions array is:

  1. `- (void)getTransactions:(Transaction * __unsafe_unretained *)buffer`
  2. `range:(NSRange)inRange {`
  3. `[self.transactions getObjects:buffer range:inRange];`
  4. `}`

### Indexed Collection Mutators

Supporting a mutable to-many relationship with indexed accessors requires implementing a different group of methods. When you provide these setter methods, the default implementation, in response to the `mutableArrayValueForKey:` message, returns a proxy object that behaves like an `NSMutableArray` object, but uses your object’s methods to do its work. This is generally more efficient than returning an `NSMutableArray` object directly. It also enables the contents of a to-many relationship to be key-value observing compliant (see _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_).

In order to make your object key-value coding compliant for a mutable ordered to-many relationship, implement the following methods:

- `insertObject:in<Key>AtIndex:` or `insert<Key>:atIndexes:`

  The first receives the object to insert and an `NSUInteger` that specifies the index where it should be inserted. The second inserts an array of objects into the collection at the indices specified by the passed `NSIndexSet`. These are analogous to the `NSMutableArray` methods [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:) and [insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insertobjects). Only one of these methods is required.

  For a `transactions` object declared as an `NSMutableArray`:

  1. `- (void)insertObject:(Transaction *)transaction`
  2. `inTransactionsAtIndex:(NSUInteger)index {`
  3. `[self.transactions insertObject:transaction atIndex:index];`
  4. `}`
  6. `- (void)insertTransactions:(NSArray *)transactionArray`
  7. `atIndexes:(NSIndexSet *)indexes {`
  8. `[self.transactions insertObjects:transactionArray atIndexes:indexes];`
  9. `}`
- `removeObjectFrom<Key>AtIndex:` or `remove<Key>AtIndexes:`

  The first receives an `NSUInteger` value specifying the index of the object to be removed from the relationship. The second receives an `NSIndexSet` object specifying the indexes of the objects to be removed from the relationship. These methods correspond to the `NSMutableArray` methods [removeObjectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectAtIndex:) and [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects) respectively. Only one of these methods is required.

  For the `transactions` object:

  1. `- (void)removeObjectFromTransactionsAtIndex:(NSUInteger)index {`
  2. `[self.transactions removeObjectAtIndex:index];`
  3. `}`
  5. `- (void)removeTransactionsAtIndexes:(NSIndexSet *)indexes {`
  6. `[self.transactions removeObjectsAtIndexes:indexes];`
  7. `}`
- `replaceObjectIn<Key>AtIndex:withObject:` or `replace<Key>AtIndexes:with<Key>:`

  These replacement accessors provide the proxy object with a means to replace an object in the collection directly, without having to successively remove one object and insert another. They correspond to the `NSMutableArray` methods [replaceObjectAtIndex:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectAtIndex:withObject:) and [replaceObjectsAtIndexes:withObjects:](https://developer.apple.com/documentation/foundation/nsmutablearray/1418287-replaceobjects). You optionally provide these methods when profiling of your app reveals performance issues.

  For the `transactions` object:

  1. `- (void)replaceObjectInTransactionsAtIndex:(NSUInteger)index`
  2. `withObject:(id)anObject {`
  3. `[self.transactions replaceObjectAtIndex:index`
  4. `withObject:anObject];`
  5. `}`
  7. `- (void)replaceTransactionsAtIndexes:(NSIndexSet *)indexes`
  8. `withTransactions:(NSArray *)transactionArray {`
  9. `[self.transactions replaceObjectsAtIndexes:indexes`
  10. `withObjects:transactionArray];`
  11. `}`

### Accessing Unordered Collections

You add unordered collection accessor methods to provide a mechanism for accessing and mutating objects in an unordered relationship. Typically, this relationship is an instance of an `NSSet` or `NSMutableSet` object. However, when you implement these accessors, you enable any class to model the relationship and be manipulated using key-value coding just as if it were an instance of `NSSet`.

### Unordered Collection Getters

When you provide the following collection getter methods to return the number of objects in the collection, iterate over the collection objects, and test if an object is already present in the collection, the default implementation of the protocol, in response to a `valueForKey:` message, returns a proxy object that behaves like an `NSSet`, but calls the following collection methods to do its work.

> [!NOTE]
> 

- `countOf<Key>`

  This required method returns the number of items in the relationship, corresponding to the `NSSet` method [count](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/count). When the underlying object is an `NSSet`, you call on this method directly. For example, for an `NSSet` object called `employees` containing `Employee` objects:

  1. `- (NSUInteger)countOfEmployees {`
  2. `return [self.employees count];`
  3. `}`
- `enumeratorOf<Key>`

  This required method returns an `NSEnumerator` instance that is used to iterate over the items in the relationship. See [Enumeration: Traversing a Collection’s Elements](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Enumerators.html#//apple_ref/doc/uid/20000135) in _[Collections Programming Topics](../Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)_ for more information about enumerators. The method corresponds to the `NSSet` method [objectEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/objectEnumerator). For the `employees` set:

  1. `- (NSEnumerator *)enumeratorOfEmployees {`
  2. `return [self.employees objectEnumerator];`
  3. `}`
- `memberOf<Key>:`.

  This method compares the object passed as a parameter with the contents of the collection and returns the matching object as a result, or `nil` if no matching object is found. If you implement comparisons manually, you typically use `isEqual:` to compare the objects. When the underlying object is an NSSet object, you can use the equivalent [member:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/member:) method:

  1. `- (Employee *)memberOfEmployees:(Employee *)anObject {`
  2. `return [self.employees member:anObject];`
  3. `}`

### Unordered Collection Mutators

Supporting a mutable to-many relationship with unordered accessors requires implementing additional methods. Implement the mutable unordered accessors to allow your object to supply an unordered set proxy object in response to the `mutableSetValueForKey:` method. Implementing these accessors is much more efficient than relying on an accessor that returns a mutable object directly for making changes to the data in the relationship. It also makes your class key-value observing compliant for the collected objects (see _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_).

In order to be key-value coding complaint for a mutable unordered to-many relationship implement the following methods:

- `add<Key>Object:` or `add<Key>:`

  These methods add a single item or a set of items to the relationship. When adding a set of items to the relationship, ensure that an equivalent object is not already present in the relationship. These are analogous to the `NSMutableSet` methods [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObject:) and [unionSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/unionSet:). Only one of these methods is required. For the `employees` set:

  1. `- (void)addEmployeesObject:(Employee *)anObject {`
  2. `[self.employees addObject:anObject];`
  3. `}`
  5. `- (void)addEmployees:(NSSet *)manyObjects {`
  6. `[self.employees unionSet:manyObjects];`
  7. `}`
- `remove<Key>Object:` or `remove<Key>:`

  These methods remove a single item or a set of items from the relationship. They are analogous to the `NSMutableSet` methods [removeObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/removeObject:) and [minusSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/minusSet:). Only one of these methods is required. For example:

  1. `- (void)removeEmployeesObject:(Employee *)anObject {`
  2. `[self.employees removeObject:anObject];`
  3. `}`
  5. `- (void)removeEmployees:(NSSet *)manyObjects {`
  6. `[self.employees minusSet:manyObjects];`
  7. `}`
- `intersect<Key>:`

  This method, which receives an `NSSet` parameter, removes from the relationship all the objects that aren’t common to both the input set and the collection set. This is the equivalent of the `NSMutableSet` method [intersectSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/intersectSet:). You optionally implement this method when profiling indicates performance issues surrounding updates to the collection content. For example:

  1. `- (void)intersectEmployees:(NSSet *)otherObjects {`
  2. `return [self.employees intersectSet:otherObjects];`
  3. `}`

[Achieving Basic Key-Value Coding Compliance](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq)

[Handling Non-Object Values](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)
