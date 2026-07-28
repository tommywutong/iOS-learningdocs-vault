---
title: 'Friday Q&A 2009-03-20: Objective-C 消息发送'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f7038ddac043dc7a'
translated: true
---

> 原文：[Friday Q&A 2009-03-20: Objective-C Messaging](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)　·　mikeash.com Friday Q&A

发表于 2009-03-21 01:59 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2009-03-27: Objective-C 消息转发](https://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)
上一篇文章：[Friday Q&A 2009-03-13: Objective-C Runtime 入门](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-20: Objective-C 消息发送

作者：[Mike Ash](https://www.mikeash.com/)

本文也提供[中文版（neoman 翻译）](https://github.com/0oneo/iOSArchive/wiki/%E7%BF%BB%E8%AF%91%3A-Objective-C-%E6%B6%88%E6%81%AF%E5%8F%91%E9%80%81)。

**术语定义**
在开始讨论机制之前，我们需要先定义术语。例如，很多人对“方法（method）”和“消息（message）”的确切区别并不清楚，但这对于理解消息发送系统在底层是如何工作的至关重要。

- **方法（Method）：** 与某个类关联的实际代码片段，并被赋予特定的名称。例如：`- (int)meaning { return 42; }`
- **消息（Message）：** 一个名称和一组参数，发送给某个对象。例如：将 "meaning" 和无参数发送给对象 `0x12345678`。
- **选择器（Selector）：** 表示消息或方法名称的一种特定方式，其类型为 `SEL`。选择器本质上是不透明的字符串，经过管理后，可以使用简单的指针相等性进行比较，从而实现更高的速度。（实现方式可能不同，但外表看起来就是这样。）例如：`@selector(meaning)`。
- **消息发送（Message send）：** 接收一条**消息**，找到并执行相应**方法**的过程。

**方法**
接下来我们需要讨论的是，方法在机器层面到底是什么。根据定义，它是一段带有名称并与特定类关联的代码，但它在你的 App 二进制文件中最终会生成什么？

方法最终会生成为标准的 C 函数，并带有两个额外的参数。你可能知道 `self` 作为一个隐式参数传递，最终会变成一个显式参数。另一个不太为人所知的隐式参数 `_cmd`（包含所发送消息的选择器）是第二个这样的隐式参数。编写一个像这样的方法：

```
    - (int)foo:(NSString *)str { ...
```

会被转换成类似这样的函数：

```
    int SomeClass_method_foo_(SomeClass *self, SEL _cmd, NSString *str) { ...
```

（这种名称修饰仅为说明之用，gcc 实际上根本不为方法生成链接器可见的符号。）

那么，当我们编写类似这样的代码时，会发生什么？

```
    int result = [obj foo:@"hello"];
```

编译器最终会生成执行以下等效操作的代码：

```
    int result = ((int (*)(id, SEL, NSString *))objc_msgSend)(obj, @selector(foo:), @"hello");
```

抱歉，你是不是被吓跑了？我先稍等片刻，让大家回过神来并返回……

等号后面那段荒谬的代码所做的是，获取作为 Objective-C runtime 一部分定义的 `objc_msgSend` 函数，并将其转换为不同的类型。具体来说，它从一个返回 `id` 并接受 `id`、`SEL` 以及之后的可变参数的函数，转换为一个匹配所调用方法原型的函数。

换句话说，编译器生成的代码会调用 `objc_msgSend`，但其参数和返回值的约定与调用的方法相匹配。

那些真正清醒且没有被吓破胆的读者现在会注意到，编译器即使只能处理正在发送的**消息**，却需要知道该**方法**的原型。编译器如何处理这种不一致？很简单，它作弊了。它根据到目前为止解析到的声明中可见的方法来猜测方法原型。如果找不到，或者找到的声明与实际运行时执行的方法不匹配，就会发生糟糕的事情。这就是为什么 Objective-C 在处理方法名相同但参数/返回类型不同的多个方法时表现如此糟糕的原因。

**消息发送**
代码中的消息发送会变成对 `objc_msgSend` 的调用，那么它做了什么呢？从高层来看，答案应该相当明显。既然这是唯一的函数调用，它必须查找合适的方法实现，然后调用它。调用很容易：它只需跳转到合适的地址。但是如何查找呢？

Objective-C 头文件 `runtime.h` 在其（现已不透明、遗留的）`objc_class` 结构体成员中包含以下内容：

```
    struct objc_method_list **methodLists                    OBJC2_UNAVAILABLE;
```

该结构体的定义如下：

```
    struct objc_method_list {
        struct objc_method_list *obsolete                        OBJC2_UNAVAILABLE;

        int method_count                                         OBJC2_UNAVAILABLE;
    #ifdef __LP64__
        int space                                                OBJC2_UNAVAILABLE;
    #endif
        /* variable length structure */
        struct objc_method method_list[1]                        OBJC2_UNAVAILABLE;
    }                                                            OBJC2_UNAVAILABLE;
```

这只是在声明一个包含 `objc_method` 结构体的变长结构体。而 `objc_method` 的定义如下：

```
    struct objc_method {
        SEL method_name                                          OBJC2_UNAVAILABLE;
        char *method_types                                       OBJC2_UNAVAILABLE;
        IMP method_imp                                           OBJC2_UNAVAILABLE;
    }                                                            OBJC2_UNAVAILABLE;
```

所以，即使我们不应该直接操作这些结构体（别担心，所有操作它们的功能都通过头文件其他地方的函数提供），我们仍然可以看出 runtime 是如何看待方法的。它包括一个名称（以选择器的形式）、一个包含参数/返回类型编码的字符串（查阅 `@encode` 指令以获取更多信息），以及一个 `IMP`，它只是一个函数指针：

```
    typedef id 			(*IMP)(id, SEL, ...);
```

现在我们知道了足够的信息，可以理解这一切是如何工作的了。`objc_msgSend` 只需查找你给它的对象的类（通过解引用该对象并获取所有对象都包含的 `isa` 成员即可得到），获取该类的**方法列表**，然后在方法列表中搜索，直到找到具有正确选择器的方法。如果没找到，就搜索超类（superclass）的方法列表，以此类推，直到继承层次结构的顶端。一旦找到正确的方法，就跳转到该方法的 IMP。

这里还需要考虑一个细节。上述过程是可行的，但会非常慢。`objc_msgSend` 在 x86 架构上只需大约十几个 CPU 周期即可执行完毕，这清楚地表明它不会在每次调用时都经历这个冗长的过程。线索在另一个 `objc_class` 成员中：

```
    struct objc_cache *cache                                 OBJC2_UNAVAILABLE;
```

它在后面定义：

```
    struct objc_cache {
        unsigned int mask /* total = mask + 1 */                 OBJC2_UNAVAILABLE;
        unsigned int occupied                                    OBJC2_UNAVAILABLE;
        Method buckets[1]                                        OBJC2_UNAVAILABLE;
    }
```

这定义了一个哈希表，用于存储 `Method` 结构体，并使用选择器作为键。`objc_msgSend` 的*真正*工作方式是：首先对选择器进行哈希运算，并在类的方法缓存中查找。如果找到（几乎总是能找到），就可以直接跳转到方法实现，无需进一步处理。只有当缓存中找不到时，才需要进行更耗时的查找，并在查找结束时将条目插入缓存，以便将来的查找能够快速进行。

（其实还有一个更为重要的细节：如果针对给定的选择器完全找不到方法，会发生什么？但这实在太重要了，值得单独用一篇文章来讲述，所以下周见。）

**结论**
本周的版本到此结束。请下周再来获取更多内容。有问题吗？认为 Objective-C 的消息发送系统应该以不同的方式实现？请在下面留言。

请记住，Friday Q&A 是由你们的想法驱动的。如果你有一个主题的想法，请告诉我！在评论中发表你的想法，或[直接通过电子邮件发送给我](mailto:mike@mikeash.com)（除非你要求我不要透露，否则我会使用你的名字）。

喜欢这篇文章吗？我销售包含所有这些文章的整套书籍！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-03-20-objective-c-messaging.html)

发表你的想法，提交评论：

垃圾邮件和离题帖子将被删除，恕不通知。肇事者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
