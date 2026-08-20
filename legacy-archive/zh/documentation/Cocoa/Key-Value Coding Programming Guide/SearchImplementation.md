---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/SearchImplementation.html
archived_at: '2026-07-15T07:16:16.112679Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 访问器搜索模式

`NSObject` 提供的 `NSKeyValueCoding` 协议默认实现会按照一组明确定义的规则，将基于键的访问器调用映射到对象的底层属性。这些协议方法使用键参数，在自身对象实例中搜索遵循特定命名约定的访问器、实例变量和相关方法。虽然很少需要修改这种默认搜索，但了解其工作方式有助于追踪键值编码对象的行为，并让自己的对象符合规范。

### 基本取值方法的搜索模式

`valueForKey:` 的默认实现接收 `key` 参数作为输入，并在收到 `valueForKey:` 调用的类实例内部执行以下过程：

1. 按顺序在实例中搜索名称类似 `get<Key>`、`<key>`、`is<Key>` 或 `_<key>` 的第一个访问器方法。如果找到，则调用该方法，并携带结果转到第 5 步；否则继续下一步。
2. 如果未找到简单访问器方法，则在实例中搜索名称符合 `countOf<Key>` 和 `objectIn<Key>AtIndex:` 模式（对应 `NSArray` 类定义的基础方法）以及 `<key>AtIndexes:` 模式（对应 [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) 的 `objectsAtIndexes:` 方法）的方法。

   如果找到其中第一个方法和另外两个方法中的至少一个，则创建并返回一个响应所有 `NSArray` 方法的集合代理对象；否则转到第 3 步。

   随后，代理对象会将收到的任何 `NSArray` 消息转换为 `countOf<Key>`、`objectIn<Key>AtIndex:` 和 `<key>AtIndexes:` 消息的某种组合，并发送给创建它的键值编码规范对象。如果原始对象还实现了名称类似 `get<Key>:range:` 的可选方法，代理对象也会在适当时使用该方法。实际上，代理对象与符合键值编码规范的对象协同工作，使底层属性即使不是 `NSArray`，也能表现得像 `NSArray`。
3. 如果未找到简单访问器方法或数组访问方法组，则查找名为 `countOf<Key>`、`enumeratorOf<Key>` 和 `memberOf<Key>:` 的三个方法（对应 [NSSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSSet) 类定义的基础方法）。

   如果三个方法均找到，则创建并返回一个响应所有 `NSSet` 方法的集合代理对象；否则转到第 4 步。

   随后，该代理对象会将收到的任何 `NSSet` 消息转换为 `countOf<Key>`、`enumeratorOf<Key>` 和 `memberOf<Key>:` 消息的某种组合，并发送给创建它的对象。实际上，代理对象与符合键值编码规范的对象协同工作，使底层属性即使不是 `NSSet`，也能表现得像 `NSSet`。
4. 如果未找到简单访问器方法或集合访问方法组，并且接收者的类方法 [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) 返回 `YES`（`true`），则按顺序搜索名为 `_<key>`、`_is<Key>`、`<key>` 或 `is<Key>` 的实例变量。如果找到，则直接获取实例变量的值并转到第 5 步；否则转到第 6 步。
5. 如果获取的属性值是对象指针，直接返回结果。

   如果值是 `NSNumber` 支持的标量类型，则将其存入 `NSNumber` 实例并返回。

   如果结果是 `NSNumber` 不支持的标量类型，则将其转换为 `NSValue` 对象并返回。
6. 如果其他方法都失败，则调用 [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value)。该方法默认会引发异常，但 `NSObject` 的子类可以提供特定于键的行为。

### 基本设值方法的搜索模式

`setValue:forKey:` 的默认实现接收 `key` 和 `value` 参数作为输入，并按以下过程，尝试在接收调用的对象中将名为 `key` 的属性设为 `value`（对于非对象属性，则设为 `value` 的拆箱版本，如[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)所述）：

1. 按顺序查找名为 `set<Key>:` 或 `_set<Key>` 的第一个访问器。如果找到，则以输入值（或按需拆箱后的值）调用它并结束。
2. 如果未找到简单访问器，并且类方法 `accessInstanceVariablesDirectly` 返回 `YES`（`true`），则按顺序查找名称类似 `_<key>`、`_is<Key>`、`<key>` 或 `is<Key>` 的实例变量。如果找到，则直接用输入值（或拆箱后的值）设置该变量并结束。
3. 如果找不到访问器或实例变量，则调用 `setValue:forUndefinedKey:`。该方法默认会引发异常，但 `NSObject` 的子类可以提供特定于键的行为。

### 可变数组的搜索模式

[mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 的默认实现接收 `key` 参数作为输入，并按以下过程，为接收访问器调用的对象中名为 `key` 的属性返回可变代理数组：

1. 查找名称类似 `insertObject:in<Key>AtIndex:` 和 `removeObjectFrom<Key>AtIndex:` 的一对方法（分别对应 [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray) 的基础方法 [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:) 和 [removeObjectAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObjectAtIndex:)），或名称类似 `insert<Key>:atIndexes:` 和 `remove<Key>AtIndexes:` 的方法（对应 [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray) 的 [insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1416482-insertobjects) 和 [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutablearray/1410154-removeobjects) 方法）。

   如果对象至少有一个插入方法和一个移除方法，则返回一个代理对象。该代理对象通过向 [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 的原始接收者发送 `insertObject:in<Key>AtIndex:`、`removeObjectFrom<Key>AtIndex:`、`insert<Key>:atIndexes:` 和 `remove<Key>AtIndexes:` 消息的某种组合，来响应 `NSMutableArray` 消息。

   如果接收 [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 消息的对象还实现了名称类似 `replaceObjectIn<Key>AtIndex:withObject:` 或 `replace<Key>AtIndexes:with<Key>:` 的可选对象替换方法，代理对象也会在适当时使用这些方法，以获得最佳性能。
2. 如果对象没有可变数组方法，则改为查找名称符合 `set<Key>:` 模式的访问器方法。此时，返回的代理对象会通过向 [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 的原始接收者发送 `set<Key>:` 消息来响应 `NSMutableArray` 消息。

3. 如果既未找到可变数组方法，也未找到访问器，并且接收者的类对 [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) 返回 `YES`（`true`），则按顺序搜索名称类似 `_<key>` 或 `<key>` 的实例变量。

   如果找到这样的实例变量，则返回一个代理对象，将收到的每个 `NSMutableArray` 消息转发给实例变量的值；该值通常是 `NSMutableArray` 或其子类的实例。
4. 如果其他方法都失败，则返回一个可变集合代理对象。该对象每次收到 `NSMutableArray` 消息时，都会向 [mutableArrayValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416339-mutablearrayvalueforkey) 消息的原始接收者发送 [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) 消息。

   `setValue:forUndefinedKey:` 的默认实现会引发 `NSUndefinedKeyException`，但子类可以重写此行为。

### 可变有序集合的搜索模式

[mutableOrderedSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415479-mutableorderedsetvalue) 的默认实现可以识别与 `valueForKey:` 相同的简单访问器方法和有序集合访问器方法（参阅[基本 Getter 的默认搜索模式](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tkljrgm4demzu)），并遵循相同的实例变量直接访问策略；但它始终返回可变集合代理对象，而不是 `valueForKey:` 返回的不可变集合。此外，它还会执行以下操作：

1. 搜索名称类似 `insertObject:in<Key>AtIndex:` 和 `removeObjectFrom<Key>AtIndex:` 的方法（对应 [NSMutableOrderedSet](https://developer.apple.com/documentation/foundation/nsmutableorderedset) 类定义的两个最基础方法），以及 `insert<Key>:atIndexes:` 和 `remove<Key>AtIndexes:`（对应 [insertObjects:atIndexes:](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1410287-insert) 和 [removeObjectsAtIndexes:](https://developer.apple.com/documentation/foundation/nsmutableorderedset/1418161-removeobjectsatindexes)）。

   如果至少找到一个插入方法和一个移除方法，返回的代理对象在收到 `NSMutableOrderedSet` 消息时，会向 `mutableOrderedSetValueForKey:` 消息的原始接收者发送上述方法消息的某种组合。

   如果原始对象中存在名称类似 `replaceObjectIn<Key>AtIndex:withObject:` 或 `replace<Key>AtIndexes:with<Key>:` 的方法，代理对象也会使用它们。
2. 如果未找到可变集合方法，则搜索名称类似 `set<Key>:` 的访问器方法。此时，返回的代理对象每次收到 `NSMutableOrderedSet` 消息，都会向 `mutableOrderedSetValueForKey:` 的原始接收者发送 `set<Key>:` 消息。

3. 如果既未找到可变集合消息，也未找到访问器，并且接收者的 [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) 类方法返回 `YES`（`true`），则按顺序搜索名称类似 `_<key>` 或 `<key>` 的实例变量。如果找到，返回的代理对象会将收到的任何 `NSMutableOrderedSet` 消息转发给实例变量的值；该值通常是 `NSMutableOrderedSet` 或其子类的实例。
4. 如果其他方法都失败，返回的代理对象每次收到可变集合消息时，都会向 `mutableOrderedSetValueForKey:` 的原始接收者发送 `setValue:forUndefinedKey:` 消息。

   `setValue:forUndefinedKey:` 的默认实现会引发 [NSUndefinedKeyException](https://developer.apple.com/documentation/foundation/nsexceptionname/1411656-undefinedkeyexception)，但对象可以重写此行为。

### 可变集合的搜索模式

[mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 的默认实现接收 `key` 参数作为输入，并按以下过程，为接收访问器调用的对象中名为 `key` 的数组属性返回可变代理集合：

1. 搜索名称类似 `add<Key>Object:` 和 `remove<Key>Object:` 的方法（分别对应 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 的基础方法 [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/addObject:) 和 [removeObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/removeObject:)），以及 `add<Key>:` 和 `remove<Key>:`（对应 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 的 [unionSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/unionSet:) 和 [minusSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/instm/NSMutableSet/minusSet:) 方法）。如果至少找到一个添加方法和一个移除方法，则返回代理对象；该对象对于收到的每个 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 消息，都会向 [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 的原始接收者发送上述方法消息的某种组合。

   如果有名称类似 `intersect<Key>:` 或 `set<Key>:` 的方法可用，代理对象也会使用它们以获得最佳性能。
2. 如果 [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 调用的接收者是托管对象，搜索模式不会像处理非托管对象时那样继续。更多信息请参阅《[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)》中的“托管对象访问器方法”。
3. 如果未找到可变集合方法，并且对象不是托管对象，则搜索名称类似 `set<Key>:` 的访问器方法。如果找到，返回的代理对象对于收到的每个 `NSMutableSet` 消息，都会向 [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 的原始接收者发送 `set<Key>:` 消息。

4. 如果未找到可变集合方法和访问器方法，并且 [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) 类方法返回 `YES`（`true`），则按顺序搜索名称类似 `_<key>` 或 `<key>` 的实例变量。如果找到，代理对象会将收到的每个 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 消息转发给实例变量的值；该值通常是 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 或其子类的实例。
5. 如果其他方法都失败，返回的代理对象会通过向 [mutableSetValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415105-mutablesetvalueforkey) 的原始接收者发送 [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) 消息，响应收到的任何 [NSMutableSet](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSSetClassCluster/Description.html#//apple_ref/occ/cl/NSMutableSet) 消息。

[验证属性](ValidatingProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcobnknltc)

[实现基本的键值编码规范符合性](AccessorConventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tilkciffekqkjivcq)
