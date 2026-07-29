---
title: '周五问答 2011-06-03：Objective-C Blocks 与 C++0x Lambdas：对决！'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8c7de33f54d030cc'
translated: true
---

> 原文：[Friday Q&A 2011-06-03: Objective-C Blocks vs. C++0x Lambdas: Fight!](https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)　·　mikeash.com Friday Q&A

发表于 2011-06-03 15:11 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2011-06-17: gdb Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2011-06-17-gdb-tips-and-tricks.html)  
上一篇：[Friday Q&A 2011-05-20: The Inner Life of Zombies](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)  
标签：[blocks](https://www.mikeash.com/pyblog/?tag=blocks) [c++](https://www.mikeash.com/pyblog/?tag=c%2B%2B) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

周五问答 2011-06-03：Objective-C Blocks 与 C++0x Lambdas：对决！

作者：[Mike Ash](https://www.mikeash.com/)

**术语说明**  
我将把 Apple 的 block 扩展称为“Objective-C blocks”，尽管这并不完全准确。它实际上是 C 语言的一个扩展（甚至可以在 C++ 中使用），并添加了一些额外行为使其在 Objective-C 中更有用。然而，它们在实现上与 Objective-C 紧密交织，而“C blocks”又太含糊，所以我认为“Objective-C blocks”是这里最合适的称呼。

C++0x lambdas 仅属于 C++，不能用于 C。如果编译器支持 C++0x，它们大概可以在 Objective-C++ 中使用。

作为同时指代 Objective-C blocks 和 C++0x lambdas 的通用术语，我将使用“匿名函数（anonymous function）”。

**语法**  
Objective-C blocks 和 C++0x lambdas 的基本目标相同：允许编写匿名的内联函数。无论被称为闭包、block、lambda，还是仅仅叫作匿名函数，这些都是高级语言中的常见特性。它们对于构建便捷、简洁的库非常有用，例如数组迭代、多线程、延迟计算以及许多其他场景。

作为较低层的语言，C 和 C++ 原本没有匿名函数的概念。为了添加它们，必须创建新的语法。因此，Objective-C blocks 和 C++0x lambdas 最终产生了略有不同的语法。一个空的 Objective-C block 看起来像这样：

```
    ^{}
```

而一个空的 C++0x lambda 看起来像这样：

```
    []{}
```

到目前为止差别不大。两者都使用标准的 C 语言 `{}` 符号来分隔代码块，并使用一个特殊符号来表明这是 block 或 lambda，而不是普通的 C 代码块。在这两种情况下，`{}` 部分都容纳普通代码。

匿名函数可以通过在引导符后面的括号中写入参数来接受参数，类似于函数参数的写法：

```
    ^(int x, NSString *y){} // ObjC, take int and NSString*
    [](int x, std::string y){} // C++, take int and std::string
```

在这两种语言中，都可以返回值，并且返回类型可以从 return 语句推断：

```
    ^{ return 42; } // ObjC, returns int
    []{ return 42; } // C++, returns int
```

在这一点上，两者开始出现差异。对于 C++0x lambdas，只有当 lambda 只包含一条语句，且该语句是 return 语句时，才能推断返回类型。因此，虽然上面的代码是有效的，但下面的代码无效：

```
    []{ if(something) return 42; else return 43; }
```

在更复杂的、具有推断返回类型的 lambda 中，返回类型总是被推断为 `void`。因此，上面的代码会产生错误，因为从返回类型为 `void` 的东西中返回 `42` 是非法的。

相比之下，无论 block 内部的代码多么复杂，Objective-C blocks 都能进行返回类型推断。如果没有 return 语句，则类型推断为 `void`。否则，它会检查 block 中的所有 return 语句。如果它们都返回相同的类型，则 block 的返回类型被推断为该类型。如果它们冲突，则会生成错误。因此，与无效的 C++0x lambda 示例等效的 Objective-C 示例可以正常编译：

```
    ^{ if(something) return 42; else return 43; }
```

两者都允许显式声明返回类型。这对于 C++0x lambdas 至关重要，因为这是让复杂的 lambda 返回值的唯一方法。在 Objective-C 中，这只是一个便利，但对于避免在 return 语句中进行强制类型转换通常很有用。

对于 Objective-C blocks，返回类型在 `^` 之后立即声明。在 C++0x 中，返回类型通过在 lambda 的参数列表后面放置 `->type` 来声明。以下是两个带有显式返回类型的示例，这使得它们在两种语言中都能正常工作：

```
    []()->int { if(something) return 42; else return 43; }
    ^int { if(something) return 42; else return 43; }
```

注意，对于 C++0x lambdas，如果声明了显式返回类型，则需要参数声明，即使它可以为空。Objective-C blocks 可以分别声明返回类型或参数列表，或者同时拥有两者。为了完整起见，这里是带有参数列表的相同示例：

```
    ^int (void) { if(something) return 42; else return 43; }
```

最后，Objective-C blocks 和 C++0x lambdas 的调用方式相同：对适当类型的表达式使用标准的 `()` 运算符。如果需要，传递参数。这将调用匿名函数。

**类型**  
Objective-C blocks 引入了一类新的语言级类型来表示 block 类型。它们符合 C 函数指针类型的标准（但很棘手）语法，但使用 `^` 代替 `*`：

```
    void (*)(int) // function pointer taking int and returning void
    void (^)(int) // block taking int and returning void
```

这些类型可用于函数/方法参数、返回类型、局部变量、实例变量等。

C++0x 采用了完全不同的方法。Lambdas 拥有一个实现 `operator()` 的唯一匿名类型。换句话说，你可以调用它，但除此之外，你无法像 Objective-C blocks 那样拥有一个可访问的类型。为了将它们存储在变量中、传递给函数或从函数返回，必须使用 C++ 模板或 C++0x 的 `auto` 关键字（它会根据初始化器的类型推断变量类型）。

**捕获变量**  
这些匿名函数最重要的特性之一就是能够从封闭作用域捕获变量。例如：

```
    int x = 42;
    void (^block)(void) = ^{ printf("%d\n", x); };
    block(); // prints 42
```

这两种结构在变量捕获方面有显著不同，因此我将逐一讨论。

Objective-C blocks 可以通过在 block 内简单地引用变量来捕获它们，如上所示。默认情况下，所有捕获的变量都会在 block 创建时被复制，并且不能在 block 内被修改。

如果一个 block 捕获另一个 block 变量，该 block 的内存将自动管理。它会在必要时被复制和释放。Objective-C 对象指针也会通过必要的 retain 和 release 自动管理。这种与 Objective-C 内存管理的深度、隐式集成使得许多任务变得更容易，因为在大多数情况下，blocks 会自动对它们捕获的变量做出正确的处理。

如果 block 需要能够修改捕获的变量，则该变量必须使用特殊的 `__block` 限定符声明，以标记其为可变的：

```
    __block int x = 42;
    void (^block)(void) = ^{ x = 43; };
    block(); // x is now 43
```

需要注意的是，对于使用 `__block` 限定的变量，_不_会自动管理 block 和对象指针的内存，因此程序员需要确保所有内容都能够承受这一点。对于像上面 `x` 这样的原始类型，则无需担心。

毫不奇怪，C++0x lambdas 在这方面提供了更大的灵活性，但也带来了更大的复杂性。C++ 的总体理念似乎是给程序员提供尽可能多的工具和选择，这有利有弊。

C++0x lambda 开头的 `[]` 控制着局部变量的捕获方式。如果像这样留空，则完全无法捕获变量。为了捕获变量，需要告诉编译器你想要做什么。

最明确的方法是将要捕获的变量列在 `[]` 内。直接按名称列出的任何变量都按值捕获。任何带有前导 `&` 列出的变量都按引用捕获。例如：

```
    int x = 42;
    int y = 99;
    auto lambda = [x, &y]{ y = 100; };
    lambda(); // y is now 100
```

在这种情况下无法修改 `x`，因为 lambda 的 `operator()` 默认是 `const`。然而，这可以通过将其声明为 `mutable` 来覆盖：

```
    int x = 42;
    int y = 99;
    auto lambda = [x, &y]() mutable {
        x++, y++;
        printf("%d, %d\n", x, y);
    };
    lambda(); // prints 43, 100
    printf("%d, %d\n", x, y); // prints 42, 100
    lambda(); // prints 44, 101!
```

因为 `x` 是按值捕获的，所以在 lambda 内部所做的更改在其外部是不可见的。此时基本上有两个 `x` 的副本，它们互不影响。

列出每个要捕获的变量可能会很不方便，因此可以通过在 `[]` 内放置 `=` 或 `&` 来指定默认捕获行为。例如：

```
    int x = 42;
    int y = 99;
    auto lambda = [&] {
        x++, y++;
    };
    lambda(); // x, y are now 43, 100
```

甚至可以组合两者，以获得具有例外的默认捕获：

```
    int x = 42;
    int y = 99;
    int z = 1001;
    auto lambda = [=, &z] {
        // 不能在此处修改 x 或 y，但可以读取它们
        z++;
        printf("%d, %d, %d\n", x, y, z);
    };
    lambda(); // prints 42, 99, 1002
    // z 现在是 1002
```

通过允许每个 lambda 指定其捕获方式，C++0x 系统提供了更大的灵活性。对于 Objective-C blocks，给定的变量要么是 `__block`，要么不是。每个捕获该变量的 block 都必须以相同的方式捕获它。C++0x lambdas 允许每个 lambda 自行决定如何捕获。`mutable` 关键字甚至允许它们按值捕获，但保留内部更改副本的能力。其缺点则是复杂性显著增加。

**内存管理**  
Objective-C blocks 和 C++0x lambdas 最初都是作为栈（stack）对象存在的。然而，在那之后，它们产生了显著的分歧。

Objective-C blocks 同时也是 Objective-C 对象。与所有 Objective-C 对象一样，它们通过引用存储，从不通过值存储。当编写 block 字面量时，block 对象在栈上创建，并且字面量表达式的计算结果为该 block 的地址。

为了让一个 block 的寿命超越其在栈上的插槽，必须复制它。因为值只是一个引用，仅仅使用 `=` 进行赋值是不够的：

```
    void (^block)(void);
    {
        block = ^{ printf("hello world"); };
    }
    block(); // bad!
```

相反，必须复制它，要么通过 Objective-C 的 `copy` 方法，要么通过 C 的 `Block_copy` 函数：

```
    void (^block)(void);
    {
        block = ^{ printf("hello world"); };
        block = [block copy];
    }
    block(); // good!
```

Blocks 遵循标准的 Objective-C 引用计数（reference counting）语义。每一个 `copy` 必须与一个 `release` 或 `autorelease` 平衡，每一个 `Block_copy` 必须与一个 `Block_release` 平衡。第一次复制会将 block 移到堆（heap）上，后续的复制只会增加引用计数。当最后一个活引用被释放时，block 被销毁，任何捕获的对象或 blocks 也被释放。

C++0x lambdas 通过值存储，而不是通过引用。如果需要，它们可以被复制到堆上，但这个过程完全是手动的。所有捕获的变量都作为成员变量存储在匿名的 lambda 对象中，因此当 lambda 被复制时，这些变量也会被复制，从而触发适当的构造函数和析构函数。

这种行为的一个极其重要的方面是，按引用捕获的变量作为引用存储在 lambda 对象中。在这方面，它们没有得到特殊对待。这意味着，在原始封闭作用域被销毁后访问其中一个变量的 lambda 会引发未定义行为，并且很可能会崩溃。相比之下，对于 `__block` 变量，其存储会被透明地移动到堆上，并保证至少与 block 一样长寿。

另一方面，只要没有按引用捕获任何东西，C++0x lambda 无需额外工作就可以返回。返回值会复制它，并且副本将继续正常工作。对于 Objective-C blocks，在返回之前必须显式复制它们，否则它们会立即变得无效。

**性能**  
Objective-C blocks 是包含内嵌函数指针的对象。对 block 的调用会转换为对该函数指针的调用，并将 block 作为隐式参数传递：

```
    block();
    // 等效于：
    block->impl(block);
```

因此，调用 block 的开销大约与调用 C 函数的开销相同。由于需要先查找实现指针，开销略高，但只是略微高一点。

在大多数使用场景中，优化的机会很少。例如，以下代码调用一个方法，使用 block 迭代数组：

```
    [array do: ^(id obj) {
        NSLog(@"Obj is %@", obj);
    }];
```

`-do:` 的实现无法了解传递给它的 block 的任何信息，因此它必须在每次循环迭代时执行完全的间接引用和调用。

可以优化 blocks 的情况主要是一开始就不需要它们的情况，例如在相同作用域中定义并随后调用它们。一个可以做出有用优化的地方是接受 block 参数的内联函数，因为优化器能够根据调用代码改进内联代码。然而，据我所知，目前没有支持 blocks 的编译器执行这些优化，尽管我没有深入研究过。

C++0x lambdas 是具有 `operator()` 的对象。不涉及动态派发，因此调用 lambda 相当于一次简单的函数调用，无需预先进行间接引用。

因为将 lambda 传递给另一个函数涉及模板，所以有更多优化的机会。考虑以下用于迭代向量的代码：

```
    for_each(v.begin(), v.end(), [](int x) {
        printf("x is %d\n", x);
    });
```

`for_each` 是一个模板函数，这意味着它会针对这个特定类型进行特化。这使其成为内联的绝佳候选，优化编译器很可能会为上述代码生成与等效 for 循环性能相当的代码。

这是 C++ 和 Objective-C 之间典型的权衡。C++ 通常倾向于在单个函数级别生成尽可能快的代码，牺牲编译的便捷性和速度，有时甚至牺牲编程的便利性来达到此目的。Objective-C 更常倾向于更容易创建、编译和使用的实现，代价是额外的运行时开销。

**结论**  
Objective-C blocks 和 C++0x lambdas 是具有相似目标和截然不同方法的类似语言特性。Objective-C blocks 在编写和使用上稍微简单一些，尤其是当用于异步或后台任务（background task），block 必须被复制并在其创建的作用域生命周期之外保持活跃时。C++0x lambdas 最终提供了更大的灵活性和潜在的速度，但代价是增加了相当大的复杂性。在比较两者时，我认为 Apple 最终做出了更好的权衡，至少在我自己的编程中可能使用 blocks 的场景下是这样。

本周的内容到此结束。两周后再来看下一期令人困惑的版本。像我每次说的那样，周五问答是由读者的想法驱动的。如果你有一个想在这里看到的话题，请[发送给我](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我在销售包含这些文章的全套书籍！卷二和卷三现已出版！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)

添加你的想法，发表评论：

垃圾邮件和跑题内容将被删除，恕不另行通知。违规者可能由我自行决定被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
