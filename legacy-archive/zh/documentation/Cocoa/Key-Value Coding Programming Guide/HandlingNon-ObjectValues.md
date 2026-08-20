---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/HandlingNon-ObjectValues.html
archived_at: '2026-07-15T07:16:14.063018Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 处理非对象值

通常，符合键值编码规范的对象会依赖键值编码的默认实现，自动装箱和拆箱非对象属性，如[表示非对象值](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq)所述。不过，你也可以重写默认行为。最常见的原因是处理试图将 `nil` 值存入非对象属性的情况。

如果符合键值编码规范的对象收到 `setValue:forKey:` 消息，并且传入 `nil` 作为非对象属性的值，默认实现没有合适的通用处理方式。因此，它会向自身发送可以被重写的 `setNilValueForKey:` 消息。`setNilValueForKey:` 的默认实现会引发 [NSInvalidArgumentException](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/data/NSInvalidArgumentException) 异常，但你可以提供适合具体实现的行为。

例如，清单 10-1 中的代码在有人试图将某人的年龄设为 `nil` 时，改为将年龄设为 0，这对于浮点值更合适。请注意，对于重写方法未显式处理的键，它会调用对象的超类实现。

__清单 10-1__　`setNilValueForKey:` 的示例实现

1. `- (void)setNilValueForKey:(NSString *)key`
2. `{`
3. `if ([key isEqualToString:@"age"]) {`
4. `[self setValue:@(0) forKey:@"age"];`
5. `} else {`
6. `[super setNilValueForKey:key];`
7. `}`
8. `}`

[定义集合方法](DefiningCollectionMethods.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcnznknltc)

[添加验证](Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tglkdjjbeiqsiinba)
