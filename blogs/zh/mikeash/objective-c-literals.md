---
title: Objective-C 字面量
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6f12c1aef344d269'
translated: true
---

> 原文：[Objective-C Literals](https://www.mikeash.com/pyblog/friday-qa-2012-06-22-objective-c-literals.html)　·　mikeash.com Friday Q&A

发布于 2012-06-22 14:17 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2012-07-06: 让我们构建 NSNumber](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)  
上一篇文章：[Friday Q&A 2012-06-01: PLWeakCompatibility 漫游：第二部分](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)  
标签: [clang](https://www.mikeash.com/pyblog/?tag=clang) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-06-22: Objective-C 字面量

作者：[Mike Ash](https://www.mikeash.com/)

本文还提供[印地语版本 (Priti Agarwal 翻译)](http://moviehustle.com/objective-c-literals/) 和[匈牙利语版本 (Szabolcs Csintalan 翻译)](http://fertlond.com/objective-c-allandok/)。

**字面量**  
对于不熟悉编程语言中这个术语的人，所谓“字面量”（literal）是指在源代码中可以直接写出的任何值。例如，`42` 在 C（以及很多其他语言）中就是一个字面量。通常我们会根据它产生的值的类型来称呼，所以 `42` 是整数字面量，`"hello"` 是字符串字面量，而 `'x'` 是字符字面量。

字面量是大多数编程语言的基础构件，因为代码中总需要*某种*方式来写出常量值。它们并非严格必要——你完全可以在运行时构造任何所需的值——但它们通常能让编写代码变得容易得多。例如，我们可以不使用任何字面量来构造 `42`：

```
    int fortytwo(void)
    {
        static int zero; // statics are initialized to 0
        static int fortytwo;
        if(!fortytwo)
        {
            int one = ++zero;
            int two = one + one;
            int four = two * two;
            int eight = four * two;
            int thirtytwo = eight * four;
            fortytwo = thirtytwo + eight + two;
        }
        return fortytwo;
    }
```

然而，如果我们对每个使用的整数都得这么做，大概所有人都会放弃计算机编程，转而从事那些工具不那么折磨人的职业。同样，我们也可以用手工从字符构造 C 字符串，但字符串太常用了，以至于语言提供了简洁的写法。

集合（collection）也同样常用。C 语言最初没有集合字面量的设施，但初始化复合数据类型变量的能力已经非常接近了：

```
    int array[] = { 1, 2, 3, 4, 5 };
    struct foo = { 99, "string" };
```

但这并非总是完全方便，所以 C99 增加了*复合字面量*（compound literal），它允许在代码中的任何地方直接写出这样的内容：

```
    DoWorkOnArray((int[]){ 1, 2, 3, 4, 5 });
    DoWorkOnStruct((struct foo){ 99, "string" });
```

集合字面量在其他语言中也很常见。例如，流行的 JSON 序列化（serialization）格式就是 JavaScript 字面量语法的规范形式。下面的 JSON 代码在 JavaScript、Python 以及可能某些其他语言中也是合法的语法，用于创建字典（dictionary）数组：

```
    [{ "key": "obj" }, { "key": "obj2" }]
```

直到最近，Objective-C 还没有针对 Objective-C 集合的任何语法。上面代码的等价写法是：

```
    [NSArray arrayWithObjects:
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"obj", @"key", nil],
        [NSDictionary dictionaryWithObjectsAndKeys:
            @"obj2", @"key", nil],
        nil];
```

这实在过于冗长，不仅输入起来令人痛苦，也掩盖了实际在做什么。C 可变参数传递的限制还要求在每个容器创建调用的末尾加上一个 `nil` 哨兵值，如果忘记写入，会以极其怪异的方式失败。总而言之，情况并不理想。

**容器字面量**  
最新版的 clang 现在支持 Objective-C 中的容器字面量。语法类似于 JSON 和现代脚本语言，但加入了 Objective-C 传统的 `@`。我们的示例数组/字典看起来像这样：

```
    @[@{ @"key" : @"obj" }, @{ @"key" : @"obj2" }]
```

这里确实有点 `@` 过载，但与之前的状态相比已是巨大的进步。`@[]` 语法根据内容创建一个数组，内容必须全部是对象。`@{}` 语法根据内容创建一个字典，内容写成 `key : value` 形式，而不是 `NSDictionary` 方法中那个完全荒谬的 `value, key` 语法。

因为这是语言内置的特性，所以不需要终止用的 `nil`。事实上，在这些字面量中的任何地方使用 `nil` 都会在运行时抛出错误，因为 Cocoa 集合拒绝包含 `nil`。与往常一样，请使用 `[NSNull null]` 在集合中表示 `nil`。

对于 `NSSet` 没有等效的语法。数组字面量语法让事情变得好了一点，因为你可以做类似 `[NSSet setWithArray: @[ contents ]]` 的事情，但还没有像字面量语法那样简洁的东西。

放入这样的数组或字典中的每个值仍然必须是对象。你不能通过写出 `@[ 1, 2, 3 ]` 来用数字填充对象数组。不过，随着下面内容的引入，这件事变得容易多了……

**装箱表达式**  
装箱表达式（Boxed expression）本质上允许对应原始类型（primitive type）的字面量。语法是 `@(contents)`，它会生成一个对象，将该圆括号内表达式的结果装箱。

对象的类型取决于表达式的类型。数值类型会被转换为 `NSNumber` 对象。例如，`@(3)` 生成一个包含 `3` 的 `NSNumber`，就像你写了 `[NSNumber numberWithInt: 3]` 一样。C 字符串会被转换为 `NSString` 对象，使用 UTF-8 编码，因此 `@("stuff goes here")` 会生成一个包含那些内容的 `NSString`。

这些表达式可以包含任意表达式，而不仅仅是常量，所以它们超越了简单的字面量。例如，`@(sqrt(2))` 会生成一个包含 `2` 的平方根的 `NSNumber`。表达式 `@(getenv("FOO"))` 等价于 `[NSString stringWithUTF8String: getenv("FOO")]`。

作为一种快捷方式，数字字面量可以不带圆括号进行装箱。与其写 `@(3)`，你可以直接写 `@3`。应用于字符串，我们得到了熟悉而古老的构造 `@"object string"`。注意，表达式**不能**这样工作。`@2+2` 和 `@sqrt(2)` 会产生错误，必须用圆括号括起来写成 `@(2+2)` 和 `@(sqrt(2))`。

使用这个特性，我们可以轻松创建一个包含数字的对象数组：

```
    @[ @1, @2, @3 ]
```

再一次，有点 `@` 过载，但与没有新语法时的等价写法相比好得多。

注意，装箱表达式只对数值类型和 `char *` 有效，不适用于其他指针或结构体。你仍然需要用冗长的手动方式来处理你的 `NSRect` 或 `SEL`。

**对象下标**  
等等，还有更多！现在有简洁的语法来获取和设置数组和字典的元素。这严格来说与对象字面量无关，但同时出现在 clang 中，并延续了让容器使用更简便的主题。

熟悉的 `[]` 访问数组的语法现在也适用于 `NSArray` 对象：

```
    int carray[] = { 12, 99, 42 };
    NSArray *nsarray = @[ @12, @99, @42 ];

    carray[1]; // 99
    nsarray[1]; // @99
```

它也适用于设置可变数组中的元素：

```
    NSMutableArray *nsarray = [@[ @12, @99, @42 ] mutableCopy];
    nsarray[1] = @33; // now contains 12, 33, 42
```

但注意，不能通过这种方式向数组添加元素，只能替换已有的元素。如果数组索引超出了数组末尾，数组不会增长以匹配，反而会抛出一个错误。

它对字典的工作方式相同，只是下标是一个对象键（key）而不是索引。由于字典没有任何索引限制，它也可以用于设置新条目：

```
    NSMutableDictionary *dict = [NSMutableDictionary dictionary];
    dict[@"suspect"] = @"Colonel Mustard";
    dict[@"weapon"] = @"Candlestick";
    dict[@"room"] = @"Library";

    dict[@"weapon"]; // Candlestick
```

与字面量一样，`NSSet` 没有等效的符号，可能是因为对集合使用下标没有太大意义。

**自定义下标方法**  
一个非常酷的动作是，clang 开发者使对象下标操作符完全通用化。它们实际上并没有以任何方式绑定到 `NSArray` 或 `NSDictionary`。它们只是简单地转换为任何类都可以实现的简单方法。

总共有四个方法：整数下标有一个 setter 和一个 getter，对象下标有一个 setter 和一个 getter。整数下标 getter 的原型如下：

```
    - (id)objectAtIndexedSubscript: (NSUInteger)index;
```

然后你可以实现这个方法来执行任何你想要支持的操作。代码只是机械地转换：

```
    NSLog(@"%@", yourobj[99]);
    // 转换为
    NSLog(@"%@", [yourobj objectAtIndexedSubscript: 99]);
```

你的代码可以从内部数组中获取索引，根据索引构建一个新对象，记录错误，调用 `abort()`，启动一局乒乓（Pong）游戏，或者任何你想要的。

对应的 setter 有以下原型：

```
    - (void)setObject: (id)obj atIndexedSubscript: (NSUInteger)index;
```

你获得索引和正在设置的对象，然后根据需要做任何需要做的事情来实现你想要的语义。同样，这只是简单的机械转换：

```
    yourobj[12] = @"hello";
    // 转换为
    [yourobj setObject: @"hello" atIndexedSubscript: 12];
```

用于对象下标的两个方法是类似的。它们的原型是：

```
    - (id)objectForKeyedSubscript: (id)key;
    - (void)setObject: (id)obj forKeyedSubscript: (id)key;
```

可以在同一个类上实现所有四个方法。编译器通过检查下标的类型来决定调用哪个。整数下标调用带索引的变体，对象调用带键的变体。

这实际上是 Objective-C 中现在可用的一小部分操作符重载，而 Objective-C 传统上完全避免了它。与往常一样，请谨慎使用，确保你的自定义实现保持下标操作符的精神。不要为了实现追加对象或通过网络发送消息而实现下标语法。如果你将其限制为获取和设置对象的元素，那么该语法的使用保持一致，并且你可以在不需要了解所有细节的情况下更容易地理解代码在做什么。

**初始化器**  
C 有一个奇怪的特性：全局变量的任何初始化器都必须是编译时常量。这包括简单表达式，但不包括函数调用。例如，以下全局变量声明是合法的：

```
    int x = 2 + 2;
```

但以下则不是：

```
    float y = sin(M_PI);
```

C 字符串字面量是编译时常量，因此这是合法的：

```
    char *cstring = "hello, world";
```

`NSString` 字面量也是编译时常量，因此 Cocoa 中对应的写法是合法的：

```
    NSString *nsstring = @"hello, world";
```

需要特别注意的是，没有任何新的字面量语法是编译时常量。假设数组是一个全局变量，以下代码是*不*合法的：

```
    NSArray *array = @[ @"one", @"two" ];
```

这是因为 `@[]` 语法字面上转换为对 `NSArray` 方法的调用。编译器无法在编译时计算出该方法的结果，因此在这种情况下，它不是一个合法的初始化器。

探索一下为什么会出现这种情况是很有趣的。编译器在你的二进制文件中排列全局变量，它们被直接加载到内存中。用 `2 + 2` 初始化的全局变量会导致字面量 `4` 被写入内存。C 字符串初始化器会导致字符串内容被写入程序的数据段，然后将指向这些内容的指针作为全局变量的值写入。

注意，C++（因此也包括 Objective-C++）*确实*允许全局变量的非常量初始化器。当 C++ 编译器遇到这样的表达式时，会将其打包到一个函数中，并安排该函数在二进制文件加载时被调用。因为初始化器代码运行得如此之早，使用它可能有点危险，因为其他代码（如 `NSArray`）可能尚未准备好。无论如何，如果你看到非常量初始化器编译通过了，并且想知道为什么，那很可能是因为它被编译为 C++。

`NSString` 字面量也是编译时常量，这是由于编译器和库之间的紧密耦合。有一个特殊的 `NSString` 子类叫做 `NSConstantString`，它具有固定的 ivar 布局：

```
    @interface NSSimpleCString : NSString {
    @package
        char *bytes;
        int numBytes;
    #if __LP64__
        int _unused;
    #endif
    }
    @end

    @interface NSConstantString : NSSimpleCString
    @end
```

它只包含一个 `isa`（从 `NSObject` 继承）、一个指向字节的指针和一个长度。当这样的字面量被用作全局变量初始化器时，编译器只需写出字符串内容，然后写出这个简单的对象结构，最后用指向该结构的指针初始化全局变量。

你可能已经注意到，你不需要像对待其他对象那样来 retain 和 release `NSString` 字面量（尽管出于习惯这样做仍然是个好主意）。事实上，你可以任意多次释放它们，它们也不会产生任何效果。这是因为 `NSString` 字面量不像大多数 Objective-C 对象那样是动态分配的。相反，它们在编译时分配为二进制文件的一部分，并在进程的整个生命周期中存在。

这种紧密耦合有优点，例如生成合法的全局变量初始化器，并且不需要额外运行代码来在运行时构建对象。然而，也有很大的缺点。`NSConstantString` 的布局被永远固定了。这个类必须以完全相同的布局来维护，因为这个数据布局已经硬编码在数以千计的第三方 App 中。如果 Apple 更改了布局，这些第三方 App 就会崩溃，因为它们包含具有旧布局的 `NSConstantString` 对象。

如果 `NSArray` 字面量是编译时常量，就需要有一个类似的 `NSConstantArray` 类，具有编译器可以生成的固定布局，并且必须与其他 `NSArray` 实现分开维护。这样的代码不能在缺少这个 `NSConstantArray` 类的旧版操作系统上运行。对于新字面量可以生成的其他类也存在同样的问题。

这在 `NSNumber` 字面量的情况下尤其有趣。Lion 引入了 tagged pointer，它允许将 `NSNumber` 的内容直接嵌入到指针中，消除了对单独的动态分配对象的需要。如果编译器发出 tagged pointer，它们的格式将永远无法更改，并且与旧版操作系统的兼容性将丢失。如果编译器发出常量 `NSNumber` 对象，那么 `NSNumber` 字面量将与其他 `NSNumber` 有本质区别，并可能导致显著的性能损失。

相反，编译器只是发出对框架的调用，就像你手动做的那样构建对象。这会导致一定的运行时开销，但不会比自己手动构建（不使用新语法）更差，并且使得设计更干净。

**兼容性**  
我们什么时候可以开始使用这种新语法？Xcode 4.3.3 是最新的已发布版本，尚未包含这些新增特性。我们可以合理地预期，下一个版本（大概随 Mountain Lion 一起发布）会将这些更改纳入其版本的 clang 中。

对于操作系统兼容性，字面量只是生成调用标准 Cocoa 初始化器的代码。结果与手动编写代码没有区别。

对于下标（subscripting）来说情况要复杂一些。这需要目前 Cocoa 中不存在的新方法。不过，下标方法直接映射到现有的 `NSArray` 和 `NSDictionary` 方法，因此我们可以预期会出现一个兼容性垫片（compatibility shim），类似于 `ARCLite` 垫片允许在早于 ARC 的操作系统上使用 `ARC`。

**结论**  
Objective-C 中新的对象字面量和下标语法可以显著减少大量处理数组和字典的代码的冗余程度。该语法类似于常见脚本语言中的语法，除了少量多余的 `@` 符号外，它使代码更容易阅读和编写。

今天就到这里。下次再见，我们将再次友好地探索编程世界。Friday Q&A 一如既往地由读者建议驱动，因此，如果你有一个希望在这里看到的话题，请[发送给我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我出售整本整本的书籍！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 格式。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-06-22-objective-c-literals.html)

发表你的想法，添加评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
