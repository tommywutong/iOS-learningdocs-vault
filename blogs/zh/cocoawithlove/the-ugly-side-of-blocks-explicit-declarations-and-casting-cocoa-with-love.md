---
title: 'Block 丑陋的一面：显式声明与类型转换 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/10/ugly-side-of-blocks-explicit.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:137965566ec3a7b4'
translated: true
---

> 原文：[The ugly side of blocks: explicit declarations and casting. | Cocoa with Love](https://www.cocoawithlove.com/2009/10/ugly-side-of-blocks-explicit.html)　·　Cocoa with Love (Matt Gallagher)

Snow Leopard 中的 block 是 C/Objective-C/C++/Objective-C++ 一个受欢迎的新增特性，但它们也带来了标准 C 中最糟糕的一面：函数指针声明和类型转换语法。在这篇文章中，我将向你展示如何理解 block 和函数指针的声明与类型转换语法，即使是在最糟糕的场景下。

## 简单的 block 声明与类型转换

按预期用途（简单的内联代码实现）使用 block 时，它们相当优雅。这归功于它们的一个优势：在简单情况下，你不需要指定返回类型——它可以从 block 本身的 return 语句推断出来。

因此，声明一个返回 `int` 的 block 可以简单如下：

```objc
int (^alwaysReturnIntZero)() = ^{ return 0; };
```

不过，在这种情况下，一个无修饰的整型值会被正确地假定为 `int`。如果我们希望 block 返回一个 `NSInteger`，我们需要要么对返回类型进行类型转换，要么不依赖类型推断并完整声明返回类型：

```objc
NSInteger (^alwaysReturnNSIntegerZero)() = ^ NSInteger (){ return 0; };
```

注意，_block 字面量_（右侧）与 _block 声明_（左侧）的结构不同。block 字面量采用了直接的「脱字符、返回类型、参数列表」顺序，但 block 声明使用的是 C 函数指针声明语法，这种语法可能变得更复杂（我稍后会展示）。不过目前，两者的复杂度还差不多。

对 block 进行类型转换看起来很像声明一个 block，只是去掉了声明中的变量名。

```objc
long long (^alwaysReturnLongLongZero)() = (long long (^)())alwaysReturnNSIntegerZero;
```

如果你看看这里做了什么，为某个值创建与变量类型匹配的类型转换所需的一切，就是复制该变量的声明，用括号括住复制的声明，然后去掉变量名。

### 函数指针

Block 借用了标准 C 函数指针的语法。在几乎所有情况下，block 声明或类型转换与函数指针声明或类型转换的唯一区别在于，block 使用 `^` 字符，而函数指针使用 `*` 字符。例如：

```objc
long long (*fnAlwaysReturnLongLongZero)() = (long long (*)())fnAlwaysReturnNSIntegerZero;
```

当然，函数不能内联声明，所以你不能像拥有 block 字面量那样拥有函数字面量。不过，所有其他语法特征保持不变。

## 正确理解声明

不幸的是，block 遵循典型的 C 声明规则，当你试图返回某些东西时，这些规则变得完全令人困惑。在事情变得复杂之前，我要解释一下关于 C 声明的一些简单内容。

思考一下指针是如何声明的：

```objc
int *myVariable;
```

如果你正在阅读这篇博客，你应该知道这条语句创建了一个名为 `myVariable` 的指针，它指向一个 `int`。

但这里使用的运算符是"解引用"，而不是"取得指针"（取地址）运算符。正确解读这一行的方法是：

1. 声明一个变量：  
  `myVariable`
2. 它可以被解引用（因此_隐含地_是一个指针）  
  `*myVariable`
3. 如果它被解引用，那么解引用产生的值应该被视为一个 `int`：  
  `int *myVariable;`。

让我们再看看上面的 `alwaysReturnIntZero` 声明，并将同样的解读方法应用于它。

```objc
int (^alwaysReturnIntZero)() = ^{ return 0; };
```

1. 声明一个变量：  
  `alwaysReturnIntZero`
2. 它可以被解引用以产生 block 信息（因此_隐含地_是一个 block 指针）：  
  `^alwaysReturnIntZero`
3. 它的 block 实现不接受任何参数并返回一个 `int`：  
  `int (^alwaysReturnIntZero)()`

这种解读声明的方法很简单，但你需要用它来理解下一节。

## 声明一个返回 block 的 block

想象一下，你想用一个 block 来比较一个 `double` 和一个 `int`，如果 `double` 大于 `int` 则返回 `true`，如果 double 等于或小于则返回 `false`。在简单情况下，可能如下所示：

```objc
bool (^compareDoubleToInt)(int i, double j) = ^{ return j > i; };
```

这很容易理解。但想象一下，现在你想将其拆分为两部分：

1. 第一个 block 只接受 `int` 并返回第二个 block，这个第二个 block 预先配置好使用这个 `int`。
2. 第二个 block 随后接受 `double`，将其与预先配置的 `int` 进行比较，并返回结果。

那么第一个 block 就是一个_工厂 block_，它创建第二个 block 的实例，这些实例像上面显示的 `compareDoubleToInt` 那样工作，但针对的是单个预先配置的 `i` 值。

完整的实现如下：

```objc
bool (^(^newDoubleToIntComparison)(int))(double) =
    ^(int i)
    {
        return Block_copy(^ (double j)
        {
            return j > i;
        });
    };
```

> 请特别注意名称中的"new"——这用于提醒你，在完成使用后，必须对以这种方式创建的任何 block 调用 `Block_destroy`。

如果第一行（声明）中的语法对你来说立马可以理解，那么你可以认为自己擅长句法递归。

大多数人觉得这难以阅读的原因是，口头描述这个场景时的顺序非常不同：

1. 声明一个变量：  
  `newDoubleToIntComparison`
2. 它可以被解引用以产生 block 信息（因此_隐含地_是一个 block 指针）：  
  `^newDoubleToIntComparison`
3. block 接受一个 `int` 参数：  
  `(^newDoubleToIntComparison)(int)`
4. 它的返回值可以被解引用以产生 block 信息（因此_隐含地_返回值是一个 block 指针）：  
  `(^(^newDoubleToIntComparison)(int))`
5. 这个返回的 block 接受一个 `double` 参数  
  `(^(^newDoubleToIntComparison)(int))(double)`
6. 并且返回的 block 返回一个 `bool`  
  `bool (^(^newDoubleToIntComparison)(int))(double);`

如果 C 声明从左到右阅读，就不会那么令人困惑了。然而，我们面临的情况是，返回 block 的 block 递归地嵌套在彼此内部。

当然，大多数人通过对他们使用的每个函数指针都使用 `typedef` 来缓解这个问题。对之前的 block 声明这样做，会变成：

```objc
typedef bool (^IsDoubleBiggerBlock)(double);
IsDoubleBiggerBlock (^newDoubleToIntComparison)(int);
```

## 返回 block 的函数或方法

了解声明一个返回 block 的 block 与定义一个返回 block 的函数之间的细微差别也可能有所帮助。

将前面例子中的_工厂 block_ 替换为_工厂函数_，会变成：

```objc
bool (^NewDoubleToIntComparisonFunction(int i))(double)
{
    return (bool (^)(double))Block_copy(^ (double j)
    {
        return j > i;
    });
};
```

这个函数接受一个 `int` 作为参数，但函数原型行的最后一个组成部分却是 `(double)`。函数实际接受的 `int` 参数和函数名嵌套在返回类型内部（返回类型包括右侧的 `double` 参数、脱字符以及左侧的 `bool` 返回值）。

另外请注意，你需要对 `Block_copy` 的输出进行类型转换，使其被识别为正确的返回类型。

与变量声明一样，这种嵌套行为通常被认为过于烦人，因此使用 typedef 来简化：

```objc
typedef bool (^IsDoubleBiggerBlock)(double);
IsDoubleBiggerBlock NewDoubleToIntComparisonFunction(int i)
{
    return (IsDoubleBiggerBlock)Block_copy(^ (double j)
    {
        return j > i;
    });
};
```

这样做有一个巨大的优点：它将函数的参数放回了它本来的位置——作为函数原型行的最后一个组成部分。

一个返回 block 的 Objective-C 方法则是更简单的情况，因为方法不会以同样的方式嵌套在返回类型内部。相反，返回类型看起来与返回的已复制 block 的类型转换完全一致，而方法的其余部分保持独立。

```objc
- (bool (^)(double))newDoubleToIntComparison:(int)i
{
    return (bool (^)(double))Block_copy(^ (double j)
    {
        return j > i;
    });
}
```

## 结论

C 函数指针的声明被广泛认为是该语言中最糟糕的语法。这有一个很好的理由：函数指针声明中的信息从最重要的组成部分（位于声明内部）流向最不重要的组成部分（环绕在外部）。它们本可以像句子一样从左到右流动，但实际上它们却从中间的某个标识符向外扩散。

可悲的是，block 沿袭了这一传统。你所能做的减轻这种痛苦的方法就是明智地使用 `typedef` 声明，并尽量保持你的 block 简单。毕竟，它们并不是真正为大量参数和复杂返回值而设计的。
