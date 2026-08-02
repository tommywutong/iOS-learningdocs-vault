---
title: 数值与值编程主题
apple_id: 10000038i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/Articles/DecimalNumbers.html
archived_at: '2026-07-15T07:17:17.489933Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数值与值编程主题](Introduction%20to%20Numbers%20and%20Other%20Values.md)


[下一页](Using%20NSNull.md)[上一页](Using%20Numbers.md)

# 使用十进制数

[NSDecimalNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/cl/NSDecimalNumber) 是 `NSNumber` 的不可变子类，为进行十进制运算提供面向对象的包装。一个实例可以表示任何能表达为 `尾数 x 10 指数` 形式的数，其中_尾数_是最长 38 位的十进制整数，_指数_是介于 -128 和 127 之间的整数。

在进行运算的过程中，某个方法可能产生计算错误，例如除以零。它也可能遇到需要在多种舍入方式中做出选择的情况。方法在此类情况下的处理方式称为它的“行为”（behavior）。

行为由 [NSDecimalNumberBehaviors](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSDecNumberBehaviors/Description.html#//apple_ref/occ/intf/NSDecimalNumberBehaviors) 协议中的方法设定。`NSDecimalNumber` 中每个名为 `behavior` 的参数都要求一个遵循该协议的对象。有关行为的更多内容，请参阅 [NSDecimalNumberBehaviors](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSDecNumberBehaviors/Description.html#//apple_ref/occ/intf/NSDecimalNumberBehaviors) 协议和 [NSDecimalNumberHandler](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumberHandler/Description.html#//apple_ref/occ/cl/NSDecimalNumberHandler) 类的规范，另请参阅 [defaultBehavior](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDecimalNumber/Description.html#//apple_ref/occ/clm/NSDecimalNumber/defaultBehavior) 方法说明。

你也可以通过一组 C 函数来使用 `NSDecimalNumber` 的算术和舍入方法：

|  |  |
| --- | --- |
| [NSDecimalAdd](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalAdd) |  |
| [NSDecimalCompact](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalCompact) |  |
| [NSDecimalCompare](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalCompare) |  |
| [NSDecimalCopy](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalCopy) |  |
| [NSDecimalDivide](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalDivide) |  |
| [NSDecimalIsNotANumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalIsNotANumber) |  |
| [NSDecimalMultiply](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalMultiply) |  |
| [NSDecimalMultiplyByPowerOf10](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalMultiplyByPowerOf10) |  |
| [NSDecimalNormalize](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalNormalize) |  |
| [NSDecimalPower](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalPower) |  |
| [NSDecimalRound](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalRound) |  |
| [NSDecimalString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalString) |  |
| [NSDecimalSubtract](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSDecimalSubtract) |  |

如果你不需要把十进制数当作对象来处理——也就是说，不需要把它们存入 `NSArray` 或 `NSDictionary` 实例这样的面向对象集合中——你可以考虑使用 C 接口。如果你追求最高效率，也可以考虑 C 接口。C 接口比 `NSDecimalNumber` 类更快，占用的内存也更少。

如果你需要可变性，可以把两种接口结合起来：使用 C 接口中的函数，再将其结果转换为 `NSDecimalNumber` 实例。

[下一页](Using%20NSNull.md)[上一页](Using%20Numbers.md)
