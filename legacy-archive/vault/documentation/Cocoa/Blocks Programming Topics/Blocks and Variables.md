---
title: Block 编程主题
apple_id: TP40007502
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/bxVariables.html
archived_at: '2026-07-15T07:11:19.280670Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [Block 编程主题](Introduction.md)


[下一页](Using%20Blocks.md)[上一页](Declaring%20and%20Creating%20Blocks.md)

# Block 与变量

本文描述 block 与变量之间的相互作用，包括内存管理方面的内容。

在 block 对象的代码主体内部，变量可以有五种不同的处理方式。

其中三种是标准类型的变量，你可以像在函数中那样引用它们：

- 全局变量，包括静态局部变量
- 全局函数（严格来说它们并不是变量）
- 来自外围作用域的局部变量和参数

block 还支持另外两种类型的变量：

1. 函数级别的 `__block` 变量。它们在 block 内部（以及外围作用域中）是可变的，并且只要有任何引用它们的 block 被拷贝到堆上，它们就会被保留下来。
2. `const` 导入变量。

最后，在方法实现内部，block 可以引用 Objective-C 实例变量——参见 [对象与 Block 变量](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltg)。

以下规则适用于 block 内部使用的变量：

1. 全局变量是可访问的，包括存在于外围词法作用域（lexical scope）中的静态变量。
2. 传给 block 的参数是可访问的（就像函数的参数一样）。
3. 外围词法作用域中的栈（非静态）局部变量会被捕获为 `const` 变量。

   它们的值取自程序中 block 表达式所在的那个位置。在嵌套的 block 中，值捕获自最近的外围作用域。
4. 外围词法作用域中用 `__block` 存储修饰符声明的局部变量是按引用提供的，因此是可变的。

   任何修改都会反映到外围词法作用域中，也包括在同一外围词法作用域中定义的其他所有 block。关于这一点，[__block 存储类型](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltm) 中有更详细的讨论。
5. 在 block 的词法作用域内部声明的局部变量，其行为与函数中的局部变量完全一致。

   block 每次被调用都会得到该变量的一份新副本。这些变量反过来又可以在嵌套于该 block 内部的 block 中被当作 `const` 变量或按引用变量使用。

下面的示例演示了局部非静态变量的用法：

```c
int x = 123;

void (^printXAndY)(int) = ^(int y) {

    printf("%d %d\n", x, y);
};

printXAndY(456); // 输出：123 456
```

如前所述，试图在 block 内部给 `x` 赋新值会导致错误：

```c
int x = 123;

void (^printXAndY)(int) = ^(int y) {

    x = x + y; // 错误
    printf("%d %d\n", x, y);
};
```

若想让某个变量能在 block 内部被修改，就要使用 `__block` 存储类型修饰符——参见 [__block 存储类型](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tkmbsfvbuqnrnknltm)。

你可以通过施加 `__block` 存储类型修饰符，指定某个被导入的变量是可变的——也就是可读写的。`__block` 存储与局部变量的 `register`、`auto`、`static` 存储类型类似，但彼此互斥。

`__block` 变量存放在一块由该变量的词法作用域、以及在该变量词法作用域内声明或创建的所有 block 及 block 副本共享的存储中。因此，如果在某个栈帧中声明的 block 有副本在该栈帧结束之后依然存活（例如被放入某个队列以待稍后执行），这块存储就会在栈帧销毁之后继续存在。同一词法作用域中的多个 block 可以同时使用一个共享变量。

作为一种优化手段，block 存储最初位于栈上——就像 block 自身一样。如果 block 通过 `Block_copy` 被拷贝（在 Objective-C 中则是向 block 发送 `copy` 消息），这些变量就会被拷贝到堆上。因此，`__block` _变量的地址可能随时间而改变_。

`__block` 变量还有另外两条限制：它们不能是可变长度数组，也不能是包含 C99 可变长度数组的结构体。

下面的示例演示了 `__block` 变量的用法：

```c
__block int x = 123; //  x 存在于 block 存储中

void (^printXAndY)(int) = ^(int y) {

    x = x + y;
    printf("%d %d\n", x, y);
};
printXAndY(456); // 输出：579 456
// x 现在是 579
```

下面的示例展示了 block 与几种不同类型的变量之间的相互作用：

```objc
extern NSInteger CounterGlobal;
static NSInteger CounterStatic;

{
    NSInteger localCounter = 42;
    __block char localCharacter;

    void (^aBlock)(void) = ^(void) {
        ++CounterGlobal;
        ++CounterStatic;
        CounterGlobal = localCounter; // localCounter 在 block 创建时就已固定
        localCharacter = 'a'; // 设置外围作用域中的 localCharacter
    };

    ++localCounter; // block 看不到这次修改
    localCharacter = 'b';

    aBlock(); // 执行该 block
    // localCharacter 现在是 'a'
}
```


block 支持把 Objective-C 和 C++ 对象以及其他 block 作为变量使用。

当一个 block 被拷贝时，它会对 block 内部用到的对象变量创建强引用。如果你在某个方法的实现内部使用 block：

- 如果你按引用访问某个实例变量，就会对 `self` 创建一个强引用；
- 如果你按值访问某个实例变量，就会对该变量创建一个强引用。

下面的示例演示了这两种不同的情形：

```objc
dispatch_async(queue, ^{
    // instanceVariable 是按引用使用的，会对 self 创建强引用
    doSomethingWithObject(instanceVariable);
});


id localVariable = instanceVariable;
dispatch_async(queue, ^{
    /*
      localVariable 是按值使用的，会对 localVariable 创建强引用
      （而不是对 self）。
    */
    doSomethingWithObject(localVariable);
});
```

若要针对某个特定的对象变量改变这一行为，可以用 `__block` 存储类型修饰符标记它。

一般来说，你可以在 block 内部使用 C++ 对象。在成员函数内部，对成员变量和成员函数的引用是通过一个隐式导入的 `this` 指针进行的，因此看起来是可变的。如果 block 被拷贝，有两点需要注意：

- 如果你对一个本该基于栈的 C++ 对象使用了 `__block` 存储类别，那么会使用通常的 `copy` 构造函数。
- 如果你在 block 内部使用任何其他基于栈的 C++ 对象，该对象必须具有 `const copy` 构造函数。届时 C++ 对象会通过该构造函数被拷贝。

当你拷贝一个 block 时，该 block 内部对其他 block 的引用会在必要时一并被拷贝——整棵树都可能被拷贝（自顶向下）。如果你持有 block 变量，并在 block 内部引用了某个 block，那么被引用的那个 block 就会被拷贝。

[下一页](Using%20Blocks.md)[上一页](Declaring%20and%20Creating%20Blocks.md)

