---
title: 'Friday Q&A 2009-03-13：Objective-C 运行时简介'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7d52dcef2146418c'
translated: true
---

> 原文：[Friday Q&A 2009-03-13: Intro to the Objective-C Runtime](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)　·　mikeash.com Friday Q&A

发布于 2009-03-13 14:13 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-03-20：Objective-C 消息发送](https://www.mikeash.com/pyblog/friday-qa-2009-03-20-objective-c-messaging.html)  
上一篇：[Friday Q&A 2009-03-06：使用 Clang 静态分析器](https://www.mikeash.com/pyblog/friday-qa-2009-03-06-using-the-clang-static-analyzer.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2009-03-13：Objective-C 运行时简介

作者：[Mike Ash](https://www.mikeash.com/)

许多 Cocoa 程序员对 Objective-C 运行时只有模糊的认识。他们知道它存在（有些人甚至不知道！），知道它很重要，没有它就无法运行 Objective-C，但认识也仅限于此了。

今天我想详细解释 Objective-C 在运行时层面是如何工作的，以及你可以用它做哪些事情。

（注：我只讨论 10.5 及更高版本上 Apple 的运行时。10.4 及更早版本的运行时缺少许多 API，迫使你直接访问结构体，而 GNU 和 Cocotron 的运行时则完全是另一种东西。）

**对象**  
 在 Objective-C 中我们时时刻刻都在与对象打交道，但对象**到底**是什么？让我们来仔细看看，并构造一些能告诉我们答案的东西。

首先，我们知道对象是通过指针来引用的，比如 `NSObject *`。而且我们知道使用 `+alloc` 方法来创建它们。该方法的文档只说它会调用 `+allocWithZone:`。顺着文档链再往下走一点，我们会发现 `NSDefaultMallocZone`，然后看到它们只是用 `malloc` 分配的内存。简单！

但当它们被分配后，内存里到底是什么样的？让我们来看看：

```
    #import <Foundation/Foundation.h>
    
    @interface A : NSObject { @public int a; } @end
    @implementation A @end
    @interface B : A { @public int b; } @end
    @implementation B @end
    @interface C : B { @public int c; } @end
    @implementation C @end
    
    int main(int argc, char **argv)
    {
        [NSAutoreleasePool new];
        
        C *obj = [[C alloc] init];
        obj->a = 0xaaaaaaaa;
        obj->b = 0xbbbbbbbb;
        obj->c = 0xcccccccc;
        
        NSData *objData = [NSData dataWithBytes:obj length:malloc_size(obj)];
        NSLog(@"Object contains %@", objData);
        
        return 0;
    }
```

我们构造了一个类层级结构，其中包含一些实例变量（instance variable），然后给每个 ivar 赋上明显的值。接着我们使用 `malloc_size` 获取正确的长度，再用 `NSData` 把数据以漂亮的十六进制形式输出。结果如下：

```
    2009-01-27 15:58:04.904 a.out[22090:10b] Object contains <20300000 aaaaaaaa bbbbbbbb cccccccc>
```

这里我们可以看到，类在内存中只是按顺序排列。首先是 A 的 ivar，然后 B 的，最后是 C 的。简单！

但开头的 `20300000` 是什么？它出现在 A 的 ivar 之前，所以它一定是 NSObject 的。来看看 NSObject 的定义：

```
    /***********    基类          ***********/
    
    @interface NSObject  {
        Class	isa;
    }
```

果然，还有一个 ivar。但这个 `Class` 是什么？如果我们让 Xcode 跳转到定义，会来到 `/usr/include/objc/objc.h`，其中包含：

```
    typedef struct objc_class *Class;
```

再往下找，来到 `/usr/include/objc/runtime.h`，其中包含：

```
    struct objc_class {
        Class isa;
    
    #if !__OBJC2__
        Class super_class                                        OBJC2_UNAVAILABLE;
        const char *name                                         OBJC2_UNAVAILABLE;
        long version                                             OBJC2_UNAVAILABLE;
        long info                                                OBJC2_UNAVAILABLE;
        long instance_size                                       OBJC2_UNAVAILABLE;
        struct objc_ivar_list *ivars                             OBJC2_UNAVAILABLE;
        struct objc_method_list **methodLists                    OBJC2_UNAVAILABLE;
        struct objc_cache *cache                                 OBJC2_UNAVAILABLE;
        struct objc_protocol_list *protocols                     OBJC2_UNAVAILABLE;
    #endif
    
    } OBJC2_UNAVAILABLE;
```

所以 `Class` 是一个指向结构体的指针，而这个结构体……开头又是一个 `Class`。

再来看另一个根类 `NSProxy`：

```
    @interface NSProxy  {
        Class	isa;
    }
```

也在那里。再看一个地方，`id` 的定义——Objective-C 中代表「任意对象」的类型：

```
    typedef struct objc_object {
        Class isa;
    } *id;
```

又出现了。显然每个 Objective-C 对象都必须以 `Class isa` 开头，即使是类对象也不例外。但这到底是什么？

正如名称和类型所暗示的，`isa` ivar 指明了特定对象所属的类。每个 Objective-C 对象都必须以一个 isa 指针开头，否则运行时不知道如何处理它。关于某个对象类型的一切都包含在这个小小的指针里。对象的其余部分基本上只是一大块数据，对运行时来说它并不重要。这块数据的含义由各个类自己决定。

**类**  
 那么类里面到底包含什么？上面代码中那些标记为「unavailable」的结构体成员提供了很好的线索。（它们是为了兼容 Leopard 之前的运行时而存在的，如果你的目标系统是 Leopard 就不应该使用它们，但这些字段仍然能告诉我们里面包含了哪些信息。）首先是 `isa`，它允许类本身也像对象一样工作。接着是一个指向超类（superclass）的指针，构成了完整的类层级。随后是一些关于该类的其他基本信息。最后才是真正有趣的部分：实例变量列表、方法列表和协议（protocol）列表。这些信息在运行时都可以访问，也可以**在运行时修改**。

我跳过了 `cache` 成员，因为它对运行时操作没什么实际用处，但它揭示了一个有趣的实现细节。每次你发送消息（`[foo bar]`）时，运行时都需要在目标对象的类的方法列表中搜索，找到要调用的实际代码。然而，默认情况下方法存储在庞大的线性列表中，因此查找很慢。缓存只是一个将选择器（selector）映射到代码的哈希表。第一次发送消息时，你会进行一次缓慢的查找，但结果会被放入哈希表。后续的调用会在哈希表中找到该项，使过程快得多。

再看 `runtime.h` 的其余部分，你会看到许多用于访问和操作这些属性的函数。每个函数都以它操作的对象类型作为前缀。通用的运行时函数以 `objc_` 开头，操作类的函数以 `class_` 开头，以此类推。例如，你可以调用 `class_getInstanceMethod` 来获取某个特定方法的信息，比如参数/返回类型。或者你可以调用 `class_addMethod` 在运行时为现有类添加一个**新**方法。你甚至可以使用 `objc_allocateClassPair` 在运行时创建一个全新的类。

**实际应用**  
 利用这种运行时元信息可以做出许多有用的东西，以下是一些例子。

1. **自动 ivar/方法搜索。** Apple 的键值编码（Key-Value Coding）已经做了这类事情：你给它一个名字，它根据这个名字查找一个方法或 ivar，然后对它做些什么。你也可以自己做这类事情，比如需要根据名字查找 ivar 时。
2. **自动注册/调用子类。** 使用 `objc_getClassList` 可以获取运行时当前知道的所有类的列表。通过追踪类层级，你可以识别出哪些类是给定类的子类。这可以让你编写子类来处理特定的数据格式或其他类似情况，然后让超类自动找到它们，而不必繁琐地手动注册每个子类。
3. **在每个类上自动调用一个方法。** 这对于自定义单元测试框架等很有用。类似于第 2 点，但查找的是实现的方法，而不是特定的类层级。
4. **在运行时重写方法。** 运行时提供了一整套工具，用于将方法重新指向自定义实现，这样你就可以在不接触源代码的情况下改变类的行为。
5. **自动释放合成属性。** `@synthesize` 关键字很方便，可以让编译器生成 setter/getter，但它仍然迫使你在 `-dealloc` 中编写清理代码。通过读取类的属性元信息，你可以编写代码自动遍历并清理所有合成属性，而不必为每个属性编写代码。
6. **桥接。** 通过在运行时动态生成类，并按需查找必要的属性，你可以在 Objective-C 和另一个（足够动态的）语言之间建立桥接（bridge）。
7. **还有更多。** 不要局限于以上这些，发挥你自己的创意！

**总结**  
 Objective-C 是一种强大的语言，而全面的运行时 API 是它极其有用的组成部分。虽然在大量的 C 代码中摸索可能有点难看，但实际使用起来并不难，而且它提供的强大能力非常值得。

以上就是本周 Friday Q&A 的全部内容。请通过下面留言或[发邮件](mailto:mike@mikeash.com)给我发送你的建议（如果你不希望我提及你的名字，请告诉我）。Friday Q&A 依赖你们的建议来运行，所以请来信！

对 ObjC 运行时有什么最喜欢的用法？有什么不喜欢的？有什么技巧要分享？都在下面发表吧。

喜欢这篇文章吗？我有一整套书籍在卖！第 II 卷和第 III 卷已经出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)

发表你的想法，写评论：

垃圾邮件和离题的帖子将被删除，恕不另行通知。违规者可能会被公开羞辱，由我自行决定。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
