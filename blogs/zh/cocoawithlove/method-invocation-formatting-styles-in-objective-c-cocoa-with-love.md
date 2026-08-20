---
title: 'Objective-C 中的方法调用格式化风格 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/11/method-invocation-formatting-styles-in.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:7a4d252dee4a00dd'
translated: true
---

> 原文：[Method invocation formatting styles in Objective-C | Cocoa with Love](https://www.cocoawithlove.com/2008/11/method-invocation-formatting-styles-in.html)　·　Cocoa with Love (Matt Gallagher)

尽管 Objective-C 的大多数特性都遵循一致的风格，但方法的调用格式化——可以说是该语言的一个定义性特征——却并非如此。在这篇文章中，我将探讨不同程序员用来格式化方法调用的几种方法，并讨论它们的优缺点。

## 方法调用的问题……

当一个方法调用太长而无法放在一行时，应该如何格式化它？从不同程序员使用的众多惯例来看，并没有明确的答案。

如何编写一个简短、简单的方法调用是没有歧义的：

```objc
[myColor set];
```

但如果一个方法超过了指定的屏幕宽度：

```objc
NSColor *myColor = [NSColor colorWithCalibratedRed:120.0/255.0 green:120.0/255.0 blue:120.0/255.0 alpha:1.0];
```

那么意见就开始出现分歧。

除了这个考虑之外，还有多少内容应该内联的问题。Cocoa 强烈建议，分配和初始化语句应该始终是一行：

```objc
id myObject = [[MyClass alloc] init];
```

但在将语句分解成单独的语句之前，应该继续内联到什么程度呢？例如：

```objc
// 完全内联……
NSColor *deviceColor = [[[NSColorPicker sharedColorPicker] color] colorUsingColorSpaceName:NSDeviceRGBColorSpace];

// 分解后……
NSColor *cur = [[NSColorPicker sharedColorPicker] color];
NSColor *devColor = [cur colorUsingColorSpaceName:NSDeviceRGBColorSpace];
```

以下是几种不同的方法……

## 风格 1：软换行且从不分解

格式化 Objective-C 方法调用最简单的方法是“什么都不做”的方法。这包括：

- 让你的文本编辑器在行宽超出页面时，用缩进进行换行
- 如果子方法只使用一次，则绝不分解语句

使用这种方法，`deviceColor` 的创建可能看起来像这样：

```objc
NSColor *deviceColor = [[[NSColorPicker sharedColorPicker] color]
    colorUsingColorSpaceName:NSDeviceRGBColorSpace];
```

这是 [Penny Arcade](http://www.penny-arcade.com/comic/2007/07/02/) [反复出现的角色](http://www.penny-arcade.com/comic/2008/11/26/) Wil Shipley 在其 [Pimp My Code 系列](http://www.wilshipley.com/blog/2005/10/pimp-my-code-part-5-special-apple.html) 中倡导的方法。Apple 也开始在 Xcode 的一些（但不是全部）项目模板中使用这种方法。

### 优势

作为代码的输入者，你永远不需要做任何事情。无需折腾，无需重新格式化。你也永远不需要声明一个只需要一次的变量；只需将所有内容内联。

对于 Apple 来说，在模板中提供代码，这种方法还有一个优势：如果用户更喜欢换行后的代码，那么 Xcode 用户将这种未换行的样式重新格式化为他们选择的换行样式，比将已经换行的代码重新格式化为另一种样式更快。

### 劣势

这种方法可能会降低清晰度。

来自 [Pimp My Code Part 5: Special Apple Sample Code Edition...](http://www.wilshipley.com/blog/2005/10/pimp-my-code-part-5-special-apple.html)：

```objc
    return [[NSSearchPathForDirectoriesInDomains(NSApplicationSupportDirectory,
        NSUserDomainMask, YES) objectAtIndex:0] 
        stringByAppendingPathComponent:[[NSProcessInfo processInfo]
        processName]];
```

这样的语句并不适合所有人。就个人而言，当我在键盘前工作几个小时后开始对代码难以集中注意力时，我无法很好地阅读这样的代码。语句的视觉层次与其包含的结构不匹配。缺失或多余的元素可能隐藏在任何地方。

这种方法还缺乏互操作性（interoperability）。对于在非换行编辑器中阅读你代码的人来说，代码的可读性会大大降低。因此，代码有时会以相同的方式格式化，但在 80 个字符处硬换行。

## 风格 2：所有参数在同一层级左对齐

对于我之前展示的 `myColor` 创建语句，左对齐所有参数会导致以下结果：

```objc
NSColor *myColor =
    [NSColor
        colorWithCalibratedRed:120.0/255.0
        green:120.0/255.0
        blue:120.0/255.0
        alpha:1.0];
```

### 优势

视觉结构遵循语句结构，因此可读性高。对于具有长参数列表的方法非常有效。这种方法也符合常见的 C 和 C++ 代码格式化风格。

这种风格的细微变化非常适合格式化结构化的内联数据。例如：

```objc
NSDictionary *myDictionary =
    [NSDictionary dictionaryWithObjectsAndKeys:
        [NSArray arrayWithObjects:
            [NSDictionary dictionaryWithObjectsAndKeys:
                @"value1", @"key1",
                @"value2", @"key2",
                @"value3", @"key3",
            nil],
        nil], @"keyForArray",
        @"topLevelValue1", @"topLevelKey1",
        @"topLevelValue2", @"topLevelKey2",
    nil];
```

### 劣势

相对于文本编辑器中的软换行，这种方法有很高的代码格式化和维护成本。需要输入、删除和移动大量的制表符、回车和空格。

教条式地将这种风格应用于结构复杂的语句可能会导致糟糕的结果。例如，用这种方式严格格式化的 Pimp My Code 示例：

```objc
    return
        [[NSSearchPathForDirectoriesInDomains(
                    NSApplicationSupportDirectory,
                    NSUserDomainMask,
                    YES)
                objectAtIndex:0] 
            stringByAppendingPathComponent:
                [[NSProcessInfo processInfo]
                    processName]];
```

## 风格 3：部分左对齐，部分分解

这是前一种格式化风格更平衡的变体，这种方法做了以下改变：

- 如果 self 访问/创建无法在一行内完成，则将其分解
- 仅当子语句无法放在其行内时才开始换行
- 将调用中的 self 组件放在与赋值或返回运算符同一行（可选）

从 Pimp My Code 中摘取的示例现在变成了：

```objc
    NSArray *searchPath = NSSearchPathForDirectoriesInDomains(
        NSApplicationSupportDirectory,
        NSUserDomainMask,
        YES);
    return [[searchPath objectAtIndex:0]
        stringByAppendingPathComponent:
            [[NSProcessInfo processInfo] processName]];
```

### 优势

比教条式地对齐每个参数更好地处理复合语句，同时保留了大部分结构清晰度。分解 self 访问，而不是对其换行，使语句的“主语”更加清晰。

### 劣势

需要做出一些判断，决定何时分解以及何时开始对语句进行换行。

可能是目前列出的风格中代码格式化维护要求最高的，因为选择分解或重新整合元素非常耗时。

## 风格 4：列对齐

这与各种方法调用格式化风格有关，这些风格试图对齐其行内换行数据的列，包括在冒号字符上对齐：

```objc
      [object methodWithParam:theParam
                      another:theOtherValue
                    something:theSomethingValue
                         else:theElseValue];
```

从我的角度来看，我现在很少看到人们编写这种类型的调用，所以在我看来这像是一种“旧式做法”。不过 Xcode 提供了帮助你实现这一点的支持（Preferences-\>Indentation-\>Syntax Aware Indenting-\>":"）。

我还见过使用以下风格：

```objc
    [someObject       instanceMethod:   parameter];
    [differentObject  otherMethod:      anotherParameter];
```

这是尝试在行上使用制表符对齐每个组件。

### 优势

如果你对对齐有特别的要求，那么也许这适合你。

### 劣势

很难说这些情况的最终结果是否值得生成和维护它们所付出的努力。文本编辑器对其中一些对齐提供了支持，但仍然需要维护。

这些方法也与任何需要换行的子语句不兼容，因此需要近乎完全地分解。

## 结论

如果你查看我的代码，我显然使用了近似于“风格 3”的方法，并根据我的感觉进行临时调整。在按照严格编码标准工作的多年之后，我居然没有对细节保持更多的关注，这似乎很奇怪，但事实就是如此。

当然，有时候我也考虑过将我的风格改为软换行。因为改变一行或觉得它笨拙而重新格式化代码是很烦人的（尽管我怀疑它是否真的像看起来那样消耗那么多时间）。

软换行的代码似乎也是 Apple 正在发展的方向，他们往往会带动许多 Mac 程序员跟随他们的步伐。

目前，我仍觉得换行后的代码在审美上不够令人满意，所以我继续忍受着格式化的负担。
