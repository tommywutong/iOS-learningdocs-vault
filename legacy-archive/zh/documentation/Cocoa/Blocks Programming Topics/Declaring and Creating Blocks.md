---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxDeclaringCreating.html
archived_at: '2026-07-15T07:11:18.888197Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Block 编程主题](Introduction.md)


[下一页](Blocks%20and%20Variables.md)[上一页](Conceptual%20Overview.md)

# 声明与创建 Block

block 变量持有对 block 的引用。声明它们的语法与声明函数指针的语法类似，只不过用 `^` 代替 `*`。block 类型与 C 类型系统的其余部分完全互通。以下都是合法的 block 变量声明：

```c
void (^blockReturningVoidWithVoidArgument)(void);
int (^blockReturningIntWithIntAndCharArguments)(int, char);
void (^arrayOfTenBlocksReturningVoidWithIntArgument[10])(int);
```

block 同样支持可变参数（`...`）。不接受任何参数的 block 必须在参数列表中写明 `void`。

block 在设计上是完全类型安全的：它向编译器提供了完整的元数据，用于校验 block 的使用、传给 block 的参数以及返回值的赋值。你可以把一个 block 引用强制转换成任意类型的指针，反之亦然。但是，你不能通过指针解引用运算符（`*`）对 block 引用解引用——因此 block 的大小无法在编译期计算出来。

你也可以为 block 创建类型——当你在多个地方使用具有相同签名的 block 时，这样做通常被视为最佳实践：

```c
typedef float (^MyBlockType)(float, float);

MyBlockType myFirstBlock = // ... ;
MyBlockType mySecondBlock = // ... ;
```


你用 `^` 运算符来表示一个 block 字面量表达式的开始。它后面可以跟一个包含在 `()` 中的参数列表。block 的主体包含在 `{}` 中。下面的示例定义了一个简单的 block，并把它赋给一个此前已声明的变量（`oneFrom`）——注意这里 block 后面跟着用于结束 C 语句的普通 `;`。

```c
float (^oneFrom)(float);

oneFrom = ^(float aFloat) {
    float result = aFloat - 1.0;
    return result;
};
```

如果你不显式声明 block 表达式的返回值类型，编译器可以根据 block 的内容自动推断出来。如果返回类型是推断出来的，而参数列表又是 `void`，那么你连 `(void)` 参数列表也可以省略。如果出现多条 return 语句，它们的类型必须完全一致（必要时使用类型转换）。

在文件级别，你可以把 block 用作全局字面量：

```objc
#import <stdio.h>

int GlobalInt = 0;
int (^getGlobalInt)(void) = ^{ return GlobalInt; };
```

[下一页](Blocks%20and%20Variables.md)[上一页](Conceptual%20Overview.md)

