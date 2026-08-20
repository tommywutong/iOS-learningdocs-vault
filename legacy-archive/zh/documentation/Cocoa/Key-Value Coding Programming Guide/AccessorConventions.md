---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessorConventions.html
archived_at: '2026-07-15T07:16:10.549450Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 实现基本的键值编码规范符合性

让对象采用键值编码时，可令其继承自 `NSObject` 或其众多子类之一，从而使用 `NSKeyValueCoding` 协议的默认实现。默认实现又要求你按照明确定义的模式来定义对象的实例变量（简称 _ivar_）和访问器方法，这样它在收到 `valueForKey:`、`setValue:forKey:` 等键值编码消息时，才能将键字符串与属性关联起来。

在 Objective-C 中，通常只需使用 `@property` 语句声明属性，并允许编译器自动合成实例变量和访问器，即可遵循标准模式。编译器默认会按照预期模式进行合成。

如果确实需要在 Objective-C 中手动实现访问器或实例变量，请遵循本节指南以保持基本规范符合性。要在任何语言中提供额外功能，增强与对象集合属性的交互，请实现[定义集合方法](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)中介绍的方法。要进一步为对象增加键值验证，请实现[添加验证](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba)中介绍的方法。

### 基本取值方法

要实现一个返回属性值且可能执行额外自定义工作的 getter，请使用与属性同名的方法。例如，对于 `title` 字符串属性：

1. `- (NSString*)title`
2. `{`
3. `// 额外的 getter 逻辑……`
5. `return _title;`
6. `}`

对于保存布尔值的属性，也可以使用带有 `is` 前缀的方法。例如，对于布尔属性 `hidden`：

1. `- (BOOL)isHidden`
2. `{`
3. `// 额外的 getter 逻辑……`
5. `return _hidden;`
6. `}`

当属性是标量或结构体时，键值编码的默认实现会将其值装箱为对象，以便在协议方法接口中使用，如[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)所述。无需执行任何特殊操作来支持此行为。

### 基本设值方法

要实现用于存储属性值的 setter，请使用以 `set` 为前缀、后接首字母大写属性名的方法。对于 `hidden` 属性：

1. `- (void)setHidden:(BOOL)hidden`
2. `{`
3. `// 额外的 setter 逻辑……`
5. `_hidden = hidden;`
6. `}`

当属性是非对象类型（例如布尔值 `hidden`）时，协议的默认实现会检测底层数据类型，并在将来自 `setValue:forKey:` 的对象值（本例中为 `NSNumber` 实例）交给 setter 前进行拆箱，如[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)所述。无需在 setter 本身处理此事。不过，如果非对象属性有可能被写入 `nil` 值，应重写 [setNilValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1415174-setnilvalueforkey) 以处理这种情况，如[处理非对象值](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)所述。对于 `hidden` 属性，合适的行为可以是直接将 `nil` 解释为 `NO`（`false`）：

1. `- (void)setNilValueForKey:(NSString *)key`
2. `{`
3. `if ([key isEqualToString:@"hidden"]) {`
4. `[self setValue:@(NO) forKey:@"hidden"];`
5. `} else {`
6. `[super setNilValueForKey:key];`
7. `}`
8. `}`

即使允许编译器合成 setter，也应在适当时提供上述方法重写。

### 实例变量

当某个键值编码访问器方法的默认实现找不到属性访问器时，它会查询所属类的 [accessInstanceVariablesDirectly](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/EOF/EOControl/Classes/NSObjectAdditions/Description.html#//apple_ref/occ/clm/NSObject/accessInstanceVariablesDirectly) 方法，确认该类是否允许直接使用实例变量。默认情况下，该类方法返回 `YES`（`true`），但可以重写它以返回 `NO`（`false`）。

如果允许使用实例变量，请确保它们采用常规命名方式，即在属性名前加下划线（`_`）。通常，编译器在自动合成属性时会替你完成此项工作；但如果使用显式 `@synthesize` 指令，可以自行强制采用这种命名：

1. `@synthesize title = _title;`

在某些情况下，你不会使用 `@synthesize` 指令或让编译器自动合成属性，而是使用 `@dynamic` 指令告知编译器将在运行时提供 getter 和 setter。这样做可能是为了避免自动合成 getter，转而提供集合访问器，如[定义集合方法](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)所述。在这种情况下，需要在接口声明中自行声明实例变量：

1. `@interface MyObject : NSObject {`
2. `NSString* _title;`
3. `}`
5. `@property (nonatomic) NSString* title;`
7. `@end`

[访问器搜索模式](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)

[定义集合方法](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)
