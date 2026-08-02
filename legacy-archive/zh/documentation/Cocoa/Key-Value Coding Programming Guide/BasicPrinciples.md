---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html
archived_at: '2026-07-15T07:16:11.064656Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 访问对象属性

对象通常在接口声明中指定_属性_，这些属性分为以下几类：

- __属性。__ 这是标量、字符串或布尔值等简单值。`NSNumber` 等值对象以及 `NSColor` 等其他不可变类型也被视为属性。
- __对一关系。__ 这是自身拥有属性的可变对象。对象的属性可以发生变化，而对象本身不变。例如，银行账户对象可以有一个 `owner` 属性，它是 `Person` 对象的实例，而该实例本身又有 `address` 属性。所有者的地址可能发生变化，但银行账户保存的所有者引用并未变化；账户所有者没有改变，只有其地址发生了变化。
- __对多关系。__ 这是集合对象。通常使用 `NSArray` 或 `NSSet` 实例保存这类集合，也可以使用自定义集合类。

清单 2-1 声明的 `BankAccount` 对象分别展示了上述每种属性。

__清单 2-1__　`BankAccount` 对象的属性

1. `@interface BankAccount : NSObject`
3. `@property (nonatomic) NSNumber* currentBalance; // 一个属性`
4. `@property (nonatomic) Person* owner; // 对一关系`
5. `@property (nonatomic) NSArray< Transaction* >* transactions; // 对多关系`
7. `@end`

为了保持封装，对象通常会为接口中的属性提供访问器方法。对象的作者可以显式编写这些方法，也可以依赖编译器自动合成。无论采用哪种方式，使用这些访问器的代码都必须在编译前将属性名写入代码，访问器方法名会成为使用它的代码中的静态部分。例如，对于清单 2-1 中声明的银行账户对象，编译器会合成一个可针对 `myAccount` 实例调用的 setter：

1. `[myAccount setCurrentBalance:@(100.0)];`

这种方式直接，但缺乏灵活性。相比之下，符合键值编码规范的对象提供一种更通用的机制，可以使用字符串标识符访问对象属性。

### 使用键和键路径标识对象属性

_键_是用于标识特定属性的字符串。按照惯例，表示某个属性的键通常就是该属性在代码中出现的名称。键必须使用 ASCII 编码，不能包含空白字符，并且通常以小写字母开头（但也有例外，例如许多类中的 `URL` 属性）。

由于清单 2-1 中的 `BankAccount` 类符合键值编码规范，它可以识别作为其属性名的 `owner`、`currentBalance` 和 `transactions` 键。无需调用 `setCurrentBalance:` 方法，可以按键设置值：

1. `[myAccount setValue:@(100.0) forKey:@"currentBalance"];`

事实上，可以使用同一个方法并传入不同的键参数，设置 `myAccount` 对象的所有属性。由于参数是字符串，因此它可以是在运行时操作的变量。

_键路径_是由点号分隔的键组成的字符串，用于指定要遍历的一系列对象属性。序列中第一个键的属性相对于接收者，后续每个键都相对于前一个属性的值求值。键路径可通过一次方法调用深入对象层级结构。

例如，假设 `Person` 和 `Address` 类也符合键值编码规范，将键路径 `owner.address.street` 应用于银行账户实例时，它指向该账户所有者地址中存储的街道字符串值。

### 使用键获取属性值

对象采用 `NSKeyValueCoding` 协议后，即符合键值编码规范。继承自 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 的对象会自动采用该协议并获得特定默认行为，因为 `NSObject` 提供了协议基本方法的默认实现。这类对象至少实现以下基于键的基本 getter：

- [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:)——返回键参数所命名属性的值。如果无法按照[访问器搜索模式](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)所述规则找到该属性，对象会向自身发送 [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) 消息。[valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) 的默认实现会引发 `NSUndefinedKeyException`，但子类可以重写此行为，更妥善地处理这种情况。
- [valueForKeyPath:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKeyPath:)——返回相对于接收者的指定键路径的值。如果键路径序列中的任何对象对某个键不符合键值编码规范，即 `valueForKey:` 的默认实现找不到访问器方法，该对象就会收到 [valueForUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413457-value) 消息。
- [dictionaryWithValuesForKeys:](https://developer.apple.com/documentation/objectivec/nsobject/1411319-dictionarywithvalues)——返回相对于接收者的一组键的值。该方法对数组中的每个键调用 `valueForKey:`。返回的 `NSDictionary` 包含数组中所有键的值。

使用键路径访问属性时，如果键路径中除最后一个键以外的任何键是对多关系（即引用集合），返回值就是一个集合，其中包含对多键右侧各键的所有值。例如，请求键路径 `transactions.payee` 的值会返回一个数组，其中包含所有交易的全部 `payee` 对象。键路径中包含多个数组时同样有效：键路径 `accounts.transactions.payee` 返回一个数组，其中包含所有账户中所有交易的全部收款人对象。

### 使用键设置属性值

与 getter 一样，符合键值编码规范的对象还会基于 [NSObject](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSObject/Description.html#//apple_ref/occ/cl/NSObject) 中的 `NSKeyValueCoding` 协议实现，提供一小组具有默认行为的通用 setter：

- [setValue:forKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415969-setvalue)——将消息接收对象中指定键的值设为给定值。`setValue:forKey:` 的默认实现会自动拆箱表示标量和结构体的 `NSNumber` 与 `NSValue` 对象，并将其赋给属性。有关装箱和拆箱语义的详细信息，请参阅[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)。

  如果指定键对应的属性并不存在于接收 setter 调用的对象中，该对象会向自身发送 [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) 消息。`setValue:forUndefinedKey:` 的默认实现会引发 `NSUndefinedKeyException`，但子类可以重写该方法，以自定义方式处理请求。
- [setValue:forKeyPath:](https://developer.apple.com/documentation/objectivec/nsobject/1418139-setvalue)——在相对于接收者的指定键路径处设置给定值。键路径序列中对某个键不符合键值编码规范的任何对象，都会收到 [setValue:forUndefinedKey:](https://developer.apple.com/documentation/objectivec/nsobject/1413490-setvalue) 消息。
- [setValuesForKeysWithDictionary:](https://developer.apple.com/documentation/objectivec/nsobject/1417515-setvaluesforkeyswithdictionary)——使用指定字典中的值设置接收者属性，并用字典键标识属性。默认实现对每个键值对调用 `setValue:forKey:`，并按需用 `nil` 替换 `NSNull` 对象。

在默认实现中，如果试图将非对象属性设为 `nil`，符合键值编码规范的对象会向自身发送 [setNilValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415174-setnilvalueforkey) 消息。`setNilValueForKey:` 的默认实现会引发 [NSInvalidArgumentException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSInvalidArgumentException)，但对象可以重写此行为，改为提供默认值或标记值，如[处理非对象值](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)所述。

### 使用键简化对象访问

要了解基于键的 getter 和 setter 如何简化代码，请看以下示例。在 macOS 中，[NSTableView](https://developer.apple.com/documentation/appkit/nstableview) 和 [NSOutlineView](https://developer.apple.com/documentation/appkit/nsoutlineview) 对象会为每一列关联一个标识符字符串。如果表格背后的模型对象不符合键值编码规范，表格的数据源方法就必须依次检查每个列标识符，找到应返回的正确属性，如清单 2-2 所示。今后为模型（本例中的 `Person` 对象）添加其他属性时，还必须重新修改数据源方法，增加用于测试新属性并返回相关值的条件。

__清单 2-2__　不使用键值编码的数据源方法实现

1. `- (id)tableView:(NSTableView *)tableview objectValueForTableColumn:(id)column row:(NSInteger)row`
2. `{`
3. `id result = nil;`
4. `Person *person = [self.people objectAtIndex:row];`
6. `if ([[column identifier] isEqualToString:@"name"]) {`
7. `result = [person name];`
8. `} else if ([[column identifier] isEqualToString:@"age"]) {`
9. `result = @([person age]); // 将标量 age 装箱为 NSNumber`
10. `} else if ([[column identifier] isEqualToString:@"favoriteColor"]) {`
11. `result = [person favoriteColor];`
12. `} // 依此类推……`
14. `return result;`
15. `}`

另一方面，清单 2-3 利用符合键值编码规范的 `Person` 对象，给出了同一数据源方法更紧凑的实现。该数据源方法只使用 [valueForKey:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/instm/NSObject/valueForKey:) getter，将列标识符作为键返回适当的值。它不仅更短，也更通用：只要列标识符始终与模型对象的属性名匹配，以后添加新列时仍可保持不变并继续工作。

__清单 2-3__　使用键值编码的数据源方法实现

1. `- (id)tableView:(NSTableView *)tableview objectValueForTableColumn:(id)column row:(NSInteger)row`
2. `{`
3. `return [[self.people objectAtIndex:row] valueForKey:[column identifier]];`
4. `}`

[关于键值编码](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydolktk4yq)

[访问集合属性](AccessingCollectionProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedilktk4yq)
