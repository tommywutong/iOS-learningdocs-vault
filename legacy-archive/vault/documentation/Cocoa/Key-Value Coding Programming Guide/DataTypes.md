---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/DataTypes.html
archived_at: '2026-07-15T07:16:13.068342Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 表示非对象值

`NSObject` 提供的键值编码协议方法默认实现既能处理对象属性，也能处理非对象属性。默认实现会在对象参数或返回值与非对象属性之间自动转换。因此，即使存储的属性是标量或结构体，基于键的 getter 和 setter 仍可保持一致的方法签名。

调用协议的某个 getter（例如 `valueForKey:`）时，默认实现会按照[访问器搜索模式](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)所述规则，确定为指定键提供值的具体访问器方法或实例变量。如果返回值不是对象，getter 会用该值初始化 `NSNumber` 对象（用于标量）或 `NSValue` 对象（用于结构体），并改为返回该对象。

同样，默认情况下，`setValue:forKey:` 等 setter 会根据给定键，确定属性访问器或实例变量所需的数据类型。如果该数据类型不是对象，setter 会先向传入的值对象发送相应的 `<type>Value` 消息以提取底层数据，然后存储该数据。

### 装箱与拆箱标量类型

表 5-1 列出了键值编码默认实现使用 `NSNumber` 实例装箱的标量类型。对于每种数据类型，表中首先给出用于根据底层属性值初始化 `NSNumber`、以提供 getter 返回值的创建方法，然后给出设置操作期间用于从 setter 输入参数提取值的访问器方法。

__表 5-1__　装箱为 `NSNumber` 对象的标量类型

| 数据类型 | 创建方法 | 访问器方法 |
| --- | --- | --- |
| `BOOL` | `numberWithBool:` | `boolValue`（在 iOS 中）`charValue`（在 macOS 中）\* |
| `char` | `numberWithChar:` | `charValue` |
| `double` | `numberWithDouble:` | `doubleValue` |
| `float` | `numberWithFloat:` | `floatValue` |
| `int` | `numberWithInt:` | `intValue` |
| `long` | `numberWithLong:` | `longValue` |
| `long long` | `numberWithLongLong:` | `longLongValue` |
| `short` | `numberWithShort:` | `shortValue` |
| `unsigned char` | `numberWithUnsignedChar:` | `unsignedChar` |
| `unsigned int` | `numberWithUnsignedInt:` | `unsignedInt` |
| `unsigned long` | `numberWithUnsignedLong:` | `unsignedLong` |
| `unsigned long long` | `numberWithUnsignedLongLong:` | `unsignedLongLong` |
| `unsigned short` | `numberWithUnsignedShort:` | `unsignedShort` |

### 装箱与拆箱结构体

[表 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tcljrha2dkobqfvbegskfircugrq)列出了默认访问器在装箱和拆箱常见的 `NSPoint`、`NSRange`、`NSRect` 和 `NSSize` 结构体时使用的创建方法与访问器方法。

__表 5-2__　使用 `NSValue` 装箱的常见结构体类型

| 数据类型 | 创建方法 | 访问器方法 |
| --- | --- | --- |
| `NSPoint` | [valueWithPoint:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithPoint:) | `pointValue` |
| `NSRange` | [valueWithRange:](https://developer.apple.com/documentation/foundation/nsvalue/1410315-valuewithrange) | `rangeValue` |
| `NSRect` | [valueWithRect:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithRect:)（仅限 macOS） | `rectValue` |
| `NSSize` | [valueWithSize:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/clm/NSValue/valueWithSize:) | `sizeValue` |

自动装箱和拆箱并不限于 `NSPoint`、`NSRange`、`NSRect` 和 `NSSize`。结构体类型（即 Objective-C 类型编码字符串以 `{` 开头的类型）可以装箱为 `NSValue` 对象。例如，请看清单 5-1 中声明的结构体和类接口。

__清单 5-1__　使用自定义结构体的示例类

1. `typedef struct {`
2. `float x, y, z;`
3. `} ThreeFloats;`
5. `@interface MyClass`
6. `@property (nonatomic) ThreeFloats threeFloats;`
7. `@end`

对于名为 `myClass` 的该类实例，可以通过键值编码获取 `threeFloats` 值：

1. `NSValue* result = [myClass valueForKey:@"threeFloats"];`

`valueForKey:` 的默认实现调用 `threeFloats` getter，然后将结果装箱为 `NSValue` 对象并返回。

同样，也可以使用键值编码设置 `threeFloats` 值：

1. `ThreeFloats floats = {1., 2., 3.};`
2. `NSValue* value = [NSValue valueWithBytes:&floats objCType:@encode(ThreeFloats)];`
3. `[myClass setValue:value forKey:@"threeFloats"];`

默认实现通过 [getValue:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSValue/Description.html#//apple_ref/occ/instm/NSValue/getValue:) 消息拆箱该值，然后以得到的结构体调用 `setThreeFloats:`。

[使用集合运算符](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)

[验证属性](ValidatingProperties.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedcobnknltc)
