---
title: 属性列表编程指南
apple_id: 10000048i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2010-03-24'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html
archived_at: '2026-07-15T07:18:02.575834Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [属性列表编程指南](Introduction%20to%20Property%20Lists.md)


[下一页](Document%20Revision%20History.md)[上一页](Reading%20and%20Writing%20Property-List%20Data.md)

# 旧式 ASCII 属性列表

Cocoa 所源自的 OpenStep 框架使用一种 ASCII 格式来存储属性列表。这类文件所存储的信息与 XML 属性列表中的信息等价，Cocoa 至今仍然支持它们，但只支持读取。保留旧式 plist 支持主要是出于兼容历史遗留内容的考虑。你可以调用 [NSPropertyListSerialization](https://developer.apple.com/documentation/foundation/nspropertylistserialization) 的 [propertyListFromData:mutabilityOption:format:errorDescription:](https://developer.apple.com/documentation/foundation/propertylistserialization/1411993-propertylistfromdata) 方法来读取旧式属性列表。

ASCII 属性列表支持四种主要的属性列表数据类型：NSString、NSData、NSArray 和 NSDictionary。以下各节介绍这些类型各自的 ASCII 语法。

字符串用双引号括起来，例如：

```
"This is a string"
```

如果字符串完全由字母和数字组成且不含空白字符，引号可以省略（在属性列表中数字按字符串处理）。虽然属性列表格式对字符串使用 ASCII，但要注意 Cocoa 使用的是 Unicode。由于字符串编码因地区而异，这种表示方式使得该格式比较脆弱。你可能会看到字符串中包含无法阅读的 ASCII 字符序列，它们是用来表示 Unicode 字符的。

二进制数据用尖括号括起来，并以十六进制 ASCII 编码。空格会被忽略。例如：

```
<0fbd777 1c2735ae>
```


数组用圆括号括起来，元素之间用逗号分隔。例如：

```
("San Francisco", "New York", "Seoul", "London", "Seattle", "Shanghai")
```

各元素不必都是同一种类型（比如全是字符串）——但通常都是。数组可以包含字符串、二进制数据、其他数组或字典。

字典用花括号括起来，其中包含一系列键及其对应的值。每个键值对以分号结尾。例如：

```
{ user = wshakesp; birth = 1564; death = 1616; }
```

注意，由单个词构成的字母数字字符串省略了引号。各个值也不必是同一种类型，因为它们的类型通常由使用它们的程序来定义。字典可以包含字符串、二进制数据、数组和其他字典。

下面是一个更复杂的属性列表示例。属性列表本身是一个字典，其键为“AnimalSmells”“AnimalSounds”等；每个值也是一个字典，由键值对组成。

```
{
    AnimalSmells = { pig = piggish; lamb = lambish; worm = wormy; };
    AnimalSounds = { pig = oink; lamb = baa; worm = baa;
                    Lisa = "Why is the worm talking like a lamb?"; };
    AnimalColors = { pig = pink; lamb = black; worm = pink; };
}
```

[下一页](Document%20Revision%20History.md)[上一页](Reading%20and%20Writing%20Property-List%20Data.md)

