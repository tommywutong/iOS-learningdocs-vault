---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/DefiningCollectionMethods.html
archived_at: '2026-07-15T07:16:13.583192Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 定义集合方法

按照[实现基本的键值编码规范符合性](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq)所述，使用标准命名约定创建访问器和实例变量后，键值编码协议的默认实现便能在响应键值编码消息时找到它们。这既适用于表示对多关系的集合对象，也适用于其他属性。不过，如果为集合属性实现集合访问器方法，以替代或补充基本访问器，就可以：

- __使用 `NSArray` 或 `NSSet` 以外的类建模对多关系。__ 在对象中实现集合方法后，键值 getter 的默认实现会返回代理对象；该代理对象收到后续 `NSArray` 或 `NSSet` 消息时会调用这些方法。底层属性对象本身不必是 `NSArray` 或 `NSSet`，因为代理对象会使用你的集合方法提供预期行为。
- __提高修改对多关系内容时的性能。__ 协议的默认实现不会在每次发生变化时都通过基本 setter 反复创建新集合对象，而是使用你的集合方法就地修改底层属性。
- __以符合键值观察规范的方式访问对象集合属性的内容。__ 有关键值观察的更多信息，请阅读《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)》。

根据关系应表现为索引式有序集合（如 `NSArray` 对象），还是无序且元素唯一的集合（如 `NSSet` 对象），需要实现两类集合访问器之一。无论哪种情况，都至少要实现一组支持读取属性的方法，然后再添加另一组方法，以便修改集合内容。

### 访问索引式集合

可以添加索引式访问器方法，为有序关系中的对象提供计数、检索、添加和替换机制。底层对象通常是 `NSArray` 或 `NSMutableArray` 实例；但只要提供集合访问器，任何实现了这些方法的对象属性都可以像数组一样进行操作。

### 索引式集合取值方法

对于没有默认 getter 的集合属性，如果提供以下索引式集合 getter 方法，协议的默认实现会在响应 `valueForKey:` 消息时返回一个行为类似 `NSArray` 的代理对象，但该对象会调用以下集合方法完成工作。

- `countOf<Key>`

  此方法以 `NSUInteger` 返回对多关系中的对象数量，与 `NSArray` 的基础方法 [count](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/count) 相同。事实上，底层属性为 `NSArray` 时，正是使用该方法提供结果。

  例如，对于表示银行交易列表、由名为 `transactions` 的 `NSArray` 支持的对多关系：

  1. `- (NSUInteger)countOfTransactions {`
  2. `return [self.transactions count];`
  3. `}`
- `objectIn<Key>AtIndex:` 或 `<key>AtIndexes:`

  第一个方法返回对多关系中指定索引处的对象，第二个方法返回 `NSIndexSet` 参数所指定各索引处的对象数组。它们分别对应 `NSArray` 的 [objectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/objectAtIndex:) 和 [objectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsarray/1411296-objectsatindexes) 方法。只需实现其中一个。`transactions` 数组的相应方法如下：

  1. `- (id)objectInTransactionsAtIndex:(NSUInteger)index {`
  2. `return [self.transactions objectAtIndex:index];`
  3. `}`
  5. `- (NSArray *)transactionsAtIndexes:(NSIndexSet *)indexes {`
  6. `return [self.transactions objectsAtIndexes:indexes];`
  7. `}`
- `get<Key>:range:`

  此方法为可选方法，但可以提升性能。它返回集合中位于指定范围内的对象，对应 `NSArray` 的 [getObjects:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/getObjects:range:) 方法。`transactions` 数组的实现如下：

  1. `- (void)getTransactions:(Transaction * __unsafe_unretained *)buffer`
  2. `range:(NSRange)inRange {`
  3. `[self.transactions getObjects:buffer range:inRange];`
  4. `}`

### 索引式集合修改器

要使用索引式访问器支持可变对多关系，需要实现另一组方法。提供这些 setter 方法后，默认实现会在响应 `mutableArrayValueForKey:` 消息时返回一个行为类似 `NSMutableArray` 对象的代理对象，但该对象会使用你的对象方法完成工作。这样通常比直接返回 `NSMutableArray` 对象更高效，还能使对多关系的内容符合键值观察规范（参阅《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)》）。

要使对象的可变有序对多关系符合键值编码规范，请实现以下方法：

- `insertObject:in<Key>AtIndex:` 或 `insert<Key>:atIndexes:`

  第一个方法接收要插入的对象，以及指定插入位置索引的 `NSUInteger`。第二个方法在传入的 `NSIndexSet` 所指定各索引处，将对象数组插入集合。它们分别类似于 `NSMutableArray` 的 [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:) 和 [insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insertobjects) 方法。只需实现其中一个。

  对于声明为 `NSMutableArray` 的 `transactions` 对象：

  1. `- (void)insertObject:(Transaction *)transaction`
  2. `inTransactionsAtIndex:(NSUInteger)index {`
  3. `[self.transactions insertObject:transaction atIndex:index];`
  4. `}`
  6. `- (void)insertTransactions:(NSArray *)transactionArray`
  7. `atIndexes:(NSIndexSet *)indexes {`
  8. `[self.transactions insertObjects:transactionArray atIndexes:indexes];`
  9. `}`
- `removeObjectFrom<Key>AtIndex:` 或 `remove<Key>AtIndexes:`

  第一个方法接收 `NSUInteger` 值，指定要从关系中移除的对象索引。第二个方法接收 `NSIndexSet` 对象，指定要从关系中移除的各对象索引。它们分别对应 `NSMutableArray` 的 [removeObjectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectAtIndex:) 和 [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects) 方法。只需实现其中一个。

  对于 `transactions` 对象：

  1. `- (void)removeObjectFromTransactionsAtIndex:(NSUInteger)index {`
  2. `[self.transactions removeObjectAtIndex:index];`
  3. `}`
  5. `- (void)removeTransactionsAtIndexes:(NSIndexSet *)indexes {`
  6. `[self.transactions removeObjectsAtIndexes:indexes];`
  7. `}`
- `replaceObjectIn<Key>AtIndex:withObject:` 或 `replace<Key>AtIndexes:with<Key>:`

  这些替换访问器使代理对象可以直接替换集合中的对象，而无需先移除一个对象再插入另一个。它们对应 `NSMutableArray` 的 [replaceObjectAtIndex:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/replaceObjectAtIndex:withObject:) 和 [replaceObjectsAtIndexes:withObjects:](https://developer.apple.com/documentation/foundation/nsmutablearray/1418287-replaceobjects) 方法。如果对应用进行性能分析时发现性能问题，可以选择提供这些方法。

  对于 `transactions` 对象：

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

### 访问无序集合

可以添加无序集合访问器方法，为访问和修改无序关系中的对象提供机制。通常，这种关系是 `NSSet` 或 `NSMutableSet` 对象的实例。不过，实现这些访问器后，任何类都可以建模该关系，并像 `NSSet` 实例一样通过键值编码进行操作。

### 无序集合取值方法

提供以下集合 getter 方法，以返回集合中的对象数量、遍历集合对象并测试某个对象是否已存在于集合中后，协议的默认实现会在响应 `valueForKey:` 消息时返回一个行为类似 `NSSet` 的代理对象，但该对象会调用以下集合方法完成工作。

- `countOf<Key>`

  此必需方法返回关系中的项目数量，对应 `NSSet` 的 [count](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/count) 方法。底层对象为 `NSSet` 时，可以直接调用该方法。例如，对于包含 `Employee` 对象、名为 `employees` 的 `NSSet` 对象：

  1. `- (NSUInteger)countOfEmployees {`
  2. `return [self.employees count];`
  3. `}`
- `enumeratorOf<Key>`

  此必需方法返回用于遍历关系中各项目的 `NSEnumerator` 实例。有关枚举器的更多信息，请参阅《[集合编程主题](../Collections%20Programming%20Topics/About%20Collections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazti2i)》中的[枚举：遍历集合元素](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Articles/Enumerators.html#//apple_ref/doc/uid/20000135)。该方法对应 `NSSet` 的 [objectEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/objectEnumerator) 方法。对于 `employees` 集合：

  1. `- (NSEnumerator *)enumeratorOfEmployees {`
  2. `return [self.employees objectEnumerator];`
  3. `}`
- `memberOf<Key>:`.

  此方法将作为参数传入的对象与集合内容进行比较，并返回匹配对象；如果找不到匹配对象，则返回 `nil`。手动实现比较时，通常使用 `isEqual:` 比较对象。底层对象为 `NSSet` 对象时，可以使用等效的 [member:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSSet/member:) 方法：

  1. `- (Employee *)memberOfEmployees:(Employee *)anObject {`
  2. `return [self.employees member:anObject];`
  3. `}`

### 无序集合修改器

要使用无序访问器支持可变对多关系，需要实现其他方法。实现可变无序访问器后，对象可以在响应 `mutableSetValueForKey:` 方法时提供无序集合代理对象。相比依赖直接返回可变对象的访问器来更改关系中的数据，实现这些访问器的效率高得多。它还能使类对所收集的对象符合键值观察规范（参阅《[键值观察编程指南](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)》）。

要使可变无序对多关系符合键值编码规范，请实现以下方法：

- `add<Key>Object:` 或 `add<Key>:`

  这些方法向关系添加单个项目或一组项目。向关系添加一组项目时，应确保关系中尚不存在等效对象。它们类似于 `NSMutableSet` 的 [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObject:) 和 [unionSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/unionSet:) 方法。只需实现其中一个。对于 `employees` 集合：

  1. `- (void)addEmployeesObject:(Employee *)anObject {`
  2. `[self.employees addObject:anObject];`
  3. `}`
  5. `- (void)addEmployees:(NSSet *)manyObjects {`
  6. `[self.employees unionSet:manyObjects];`
  7. `}`
- `remove<Key>Object:` 或 `remove<Key>:`

  这些方法从关系中移除单个项目或一组项目。它们类似于 `NSMutableSet` 的 [removeObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/removeObject:) 和 [minusSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/minusSet:) 方法。只需实现其中一个。例如：

  1. `- (void)removeEmployeesObject:(Employee *)anObject {`
  2. `[self.employees removeObject:anObject];`
  3. `}`
  5. `- (void)removeEmployees:(NSSet *)manyObjects {`
  6. `[self.employees minusSet:manyObjects];`
  7. `}`
- `intersect<Key>:`

  此方法接收 `NSSet` 参数，并从关系中移除不同时存在于输入集合与属性集合中的所有对象。它等效于 `NSMutableSet` 的 [intersectSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/intersectSet:) 方法。如果性能分析表明更新集合内容时存在性能问题，可以选择实现此方法。例如：

  1. `- (void)intersectEmployees:(NSSet *)otherObjects {`
  2. `return [self.employees intersectSet:otherObjects];`
  3. `}`

[实现基本的键值编码规范符合性](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq)

[处理非对象值](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)
