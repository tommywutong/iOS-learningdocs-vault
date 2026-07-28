---
title: 'Friday Q&A 2009-08-14：实用 Block'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af10c3a33bd3115b'
translated: true
---

> 原文：[Friday Q&A 2009-08-14: Practical Blocks](https://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)　·　mikeash.com Friday Q&A

发表于 2009-08-14 20:06 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2009-08-21：编写可变参数宏与函数](https://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html)
上一篇：[Friday Q&A 2009-07-17：格式化字符串技巧与陷阱](https://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html)
标签：[blocks](https://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-08-14：实用 Block

作者：[Mike Ash](https://www.mikeash.com/)

虽然 Apple 尚未在其任何开发者工具中正式提供 block，但由于他们参与了开源编译器 gcc 和 clang，他们已经发布了 block 实现（blocks implementation）的代码。Landon 利用这些代码整合出了 [PLBlocks](http://code.google.com/p/plblocks/)，它允许在 Mac OS X 10.5 上构建和运行基于 block 的代码。尽管 10.5 上还没有基于 block 的 API（除了作为运行时基础部分的一些非常基本的功能），但它们仍然能发挥巨大作用。

我不打算在此介绍 PLBlocks 的安装或基本用法，因为 PLBlocks 页面已经详细说明了。如果你想跟着做，请去那里并按指引操作。关于 block 如何工作的更多信息，请参阅 Clang 的 [block 语言规范](http://clang.llvm.org/docs/BlockLanguageSpec.txt) 和 [实现规范](http://clang.llvm.org/docs/BlockImplementation.txt)。

我还假设你已经了解了 block 语法和用法的基本知识，这些内容已在[我上一篇关于该主题的 Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2008-12-26.html) 中介绍过。今天的文章本质上是那篇的续篇。如果你还没读过，请先去阅读那篇文章。

**基础**
Block 是 Objective-C 对象。当你在代码中编写一个 block 时，那是一个对象类型的表达式，很像 `@"..."` 常量字符串语法会给你一个对象类型的表达式。然后，你可以像使用任何其他 Objective-C 对象一样使用这个对象：向它发送它能响应的消息，将其放入容器，作为参数传递，返回它等等。

它与常量字符串语法有一个主要区别。与常量字符串不同，block 在每次执行同一段代码时并不完全相同。这是因为 block 会捕获其所在的封闭作用域（scope），而这个作用域每次被调用时都可能不同。简而言之，每次代码执行遇到 `^{...}` 构造时，都会创建一个新对象。

每次分配一个新对象可能会比较慢，所以 block 采取了一种不寻常的方法：从 `^{...}` 构造中获得的对象是一个_栈对象（stack object）_。这意味着它的生命周期与局部变量相同，并且在离开当前作用域时会自动销毁。有点奇怪，对吧？

让 block 的存活时间超过其创建的作用域通常很有用。例如，你可能想要返回一个 block，或者将其保存起来以备后用。为此，你必须复制（copy）这个 block。你可以像处理任何其他 Objective-C 对象一样，通过向其发送 `-copy` 消息来完成。并且，与任何其他 Objective-C 对象一样，如果你未在垃圾回收（Garbage Collection）环境下运行，那么你将拥有生成的对象，并最终必须使用 `-release` 或 `-autorelease` 来释放它。

因此，这是一个从方法返回 block 的示例：

```
    - (void (^)(void))block { return [[^{ ... } copy] autorelease]; }
```

请注意，默认情况下，对外部变量的捕获会提供这些变量的 const 副本。换句话说，以下代码是不合法的：

```
    int i;
    ^{ i++; };
```

解决这个问题的方法是使用 `__block` 关键字，如下所示：

```
    __block int i;
    ^{ i++; };
```

要求像这样显式标记局部变量的原因是，`__block` 变量的成本远高于常规变量，并且在应用于 Objective-C 对象指针时具有不同的语义（稍后会详细介绍），因此，与其找出一种一刀切的策略，block 的实现者决定让程序员自己选择会更好。

**示例**
我将展示一系列关于如何在 10.5 上使用 PLBlocks 来使用 block 的示例。想要跟着做的读者可能希望查看我构建的示例项目，你可以从我的公共 Subversion 仓库中获取：

```
    svn co http://www.mikeash.com/svn/PLBlocksPlayground/
```

如果你只想浏览代码，只需点击该命令中的链接即可。

**自定义 API**
以上就是它们工作原理的基本概念，现在让我们看看能用它们做什么。

正如我在第一篇关于 block 的文章中提到的，block 本质上允许你构建新的控制（control）构造，而无需修改语言。在开始之前，我想介绍一个小小的 `typedef` 来简化事情。大多数控制构造 block 都是不带参数且不返回值的 block。因此，将该类型封装成更易于编写的形式会很好：

```
    typedef void (^BasicBlock)(void);
```

作为一个非常简单的例子，我们来看一个 Cocoa 中相当常见的任务（task）：运行一些带有内部自动释放池（autorelease pool）的代码，以将内存峰值控制在较低水平。通常看起来像这样：

```
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    ...
    [pool release];
```

这并不算太糟，但有点冗长。我们可以编写一个宏（macro）来做到这一点，但宏相当邪恶，并且通常有隐藏的陷阱。相反，让我们使用 block 编写一个小的函数来实现这一点：

```
    void WithAutoreleasePool(BasicBlock block)
    {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        block();
        [pool release];
    }
```

然后，我们可以这样使用它：

```
    for(id obj in array)
        WithAutoreleasePool(^{
            [self createLotsOfTemporaryObjectsWith:obj];
        });
```

这比手动编写更快、更容易，并且最终同样可读。很好！

让我们来处理一些更复杂的事情。在 Cocoa 程序中，经常需要在一段短暂的延迟后运行一些代码，使用 `-performSelector:withObject:afterDelay:`。我们经常使用零延迟来表示“在返回 runloop 后立即运行这段代码”。这带来的问题是，它需要一个对象和一个单独的方法，并且传递相关的上下文（context）可能会很痛苦。让我们编写一个快速的 block 函数来代替：

```
    void RunAfterDelay(NSTimeInterval delay, BasicBlock block)
    {
        [[[block copy] autorelease] performSelector: @selector(my_callBlock) withObject: nil afterDelay: delay];
    }
```

注意，我们必须对 block 执行 copy/autorelease 操作，以便该对象在 perform 完成之前保持存活。这利用了 `NSObject` 上的一个小型分类（category）来实际调用 block，利用了 block 也是 NSObject 的事实：

```
    @implementation NSObject (BlocksAdditions)

    - (void)my_callBlock
    {
        void (^block)(void) = (id)self;
        block();
    }

    @end
```

然后我们可以这样使用它：

```
    NSString *something = ...;
    RunAfterDelay(0, ^{
        NSLog(@"%@", something);
        [self doWorkWithSomething: something];
    });
```

对于任何更复杂的情况，这都比典型的 Cocoa 模式更容易处理。

我们经常编写的另一件事是受锁（lock）保护的临界区代码。通常看起来像这样：

```
    [lock lock];
    ...do stuff...
    [lock unlock];
```

然而，这相当容易出错。例如，如果你忘记在某个代码路径中解锁锁，或者从中间返回，或者抛出异常，那么你的 App 将会死锁。编写上述代码最安全的方法是使用 `@try/@finally` 块，如下所示：

```
    [lock lock];
    @try
    {
        ...do stuff...
    }
    @finally
    {
        [lock unlock];
    }
```

这有点笨拙。我们可以将这个惯用法转换为 `NSLock` 上基于 block 的方法，以完全自动地处理加锁和解锁：

```
    @implementation NSLock (BlocksAdditions)

    - (void)whileLocked: (BasicBlock)block
    {
        [self lock];
        @try
        {
            block();
        }
        @finally
        {
            [self unlock];
        }
    }

    @end
```

这不完全相同。例如，使用显式的 `@try/@finally`，你可以从方法中从 `@try` 块内部返回一个值，并且它能正常工作，而从 block 内部这样做只会导致错误，因为你将改为从 block 返回值，这会使 block 的类型不兼容。这可以通过使用 `__block` 限定的变量来保存返回值来解决。在我看来，这更优越，因为它有助于阻止在临界区内的棘手行为，而临界区是错误的高发区。

**风格说明**
上述代码中有两个有趣的选择，都是出于同样的原因。第一个选择是这些是函数，而不是方法。由于 block 是 NSObject，因此可以将 NSObject 上的分类方法用于它们。我们可以编写一个 `NSObject` 上的 `-runAfterDelay:` 方法，而不是一个 `RunAfterDelay` 函数。第二个选择是始终将 block 参数放在最后，即使它是最重要的参数，放在第一位可能更有意义。

这两者的原因都是，你希望 block 绝对位于最后，这样当 block 被拆分成多行时，你的代码仍然可读。例如，想象一下使用上述函数（但改为使用方法）的一些嵌套 block 代码：

```
    [^{
        for(id obj in array)
            [^{
                [self doImportantWork:obj];
            } withAutoreleasePool];
    } runAfterDelay: 0];
```

这显著降低了可读性。代码出现在前面，而对它做什么只在最后才出现，这可能很远。当嵌套时，你必须以后进先出（LIFO）的顺序阅读所有内容。因此，使用方法来编写控制构造是一个坏主意，并且在将 block 作为参数时，始终将 block 放在最后。

**集合（Collection）**
将 block 与集合一起使用可以产生强大的循环构造。让我们从一个非常简单的、作为 `NSArray` 上方法的 `for` 循环替代品开始：

```
    - (void)do: (void (^)(id obj))block
    {
        for(id obj in self)
            block(obj);
    }
```

这实际上没什么意思。它最终就像一个 `for/in` 循环，但不能静态类型化对象。（在 Apple 引入 `for/in` 之前，这本来会很好，至少说明了使用 block 添加自己的控制构造的想法。）使用示例：

```
    NSArray *array = ...;
    [array do: ^(id obj){ NSLog(@"%@", obj); }];
```

不太令人兴奋。这里有一个更有趣的例子。它使用一个 block 将一个数组映射（map）到一个新数组：

```
    - (NSArray *)map: (id (^)(id obj))block
    {
        NSMutableArray *new = [NSMutableArray array];
        for(id obj in self)
        {
            id newObj = block(obj);
            [new addObject: newObj ? newObj : [NSNull null]];
        }
        return new;
    }
```

这展示了如何从一个人（people）数组构建一个姓名（name）字符串数组：

```
    NSArray *people = ...;
    NSArray *names = [people map: ^(id person){
        return [NSString stringWithFormat: @"%@ %@", [person firstName], [person lastName]];
    }];
```

这比手动编写封装在 `-map:` 方法中的循环要好得多。通过传递 block，我们只需要编写一次该循环，然后多次重用它。

再举一个例子，这个允许过滤数组：

```
    - (NSArray *)select: (BOOL (^)(id obj))block
    {
        NSMutableArray *new = [NSMutableArray array];
        for(id obj in self)
            if(block(obj))
                [new addObject: obj];
        return new;
    }
```

一个使用它来过滤掉太短字符串的例子：

```
    NSArray *longStrings = [strings select: ^ BOOL (id obj) { return [obj length] > 5; }];
```

注意显式的返回值。C 比较运算符的结果是 `int`，而不是 `BOOL`，因此让编译器推断返回值会产生一个类型不兼容的 block。另一种方法是在 return 语句中强制转换表达式。

这里是一个在 GUI 应用程序中使用的例子，用于获取特定视图（view）内的所有文本字段（text field）：

```
    NSArray *textFields = [[view subviews] select: ^(id obj){ return [obj isKindOfClass: [NSTextField class]]; }];
```

**回调（Callback）**
基于回调的 API 是 block 真正发光发热的地方。我们不传递选择器（selector）/委托（delegate）对，或函数指针/上下文指针对，而是传递一个 block。它使得传递上下文变得容易得多（因为 block 自动打包了所有需要的上下文），并且将所有代码保持在一起。

通知（notification）是回调的一个明显例子。虽然将通知分离成专门的方法通常有好处，但实现起来很容易，并且有时可以使代码更优雅：

```
    @implementation NSNotificationCenter (BlocksAdditions)

    - (void)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block
    {
        [self addObserver: [block copy] selector: @selector(my_callBlockWithObject:) name: name object: object];
    }

    @end
```

`my_callBlockWithObject:` 方法在 `NSObject` 的一个分类中实现，很像之前看到的 `my_callBlock` 方法，只是它接受一个参数并将该参数传递给 block。

你可以这样使用它：

```
    [[NSNotificationCenter defaultCenter] addObserverForName: NSApplicationDidBecomeActiveNotification
                                                      object: nil
                                                       block: ^(NSNotification *note){ NSLog(@"Did become active"); }];
```

请注意，没有提供停用通知 block 的机制。这可以添加，但需要调用者管理额外的状态。这样的机制留给读者作为练习。

表单（sheet）是 Cocoa 中一个痛苦的基于回调的 API 的好例子。你必须实现一个回调方法，然后将所有与表单相关的状态（通常很大）塞入所提供的单个 `void *` 上下文参数中，或塞入实例变量中。两种方式都不是特别令人愉快。

这是一个将此类 API 转换为使用 block 的小分类：

```
    @implementation NSApplication (SheetAdditions)

    - (void)beginSheet: (NSWindow *)sheet modalForWindow:(NSWindow *)docWindow didEndBlock: (void (^)(NSInteger returnCode))block
    {
        [self beginSheet: sheet
          modalForWindow: docWindow
           modalDelegate: self
          didEndSelector: @selector(my_blockSheetDidEnd:returnCode:contextInfo:)
             contextInfo: [block copy]];
    }

    - (void)my_blockSheetDidEnd: (NSWindow *)sheet returnCode: (NSInteger)returnCode contextInfo: (void *)contextInfo
    {
        void (^block)(NSInteger returnCode) = contextInfo;
        block(returnCode);
        [block release];
    }

    @end
```

现在，你可以简单地内联提供一个 block，就在你的其余代码中，并直接访问所有必要的上下文。

另一个同样痛苦的 API 例子是 `NSURLConnection`。它提供了两种模式：同步和异步。同步模式只能从副线程（secondary thread）使用，因为该线程可以被任意长时间地阻塞，毕竟任何网络操作都可能需要很长时间才能完成。异步模式需要编写大量样板代码。让我们编写一个添加异步模式的方法，该方法在完成时简单地对一个 block 进行一次调用，以传递数据、响应元数据和错误（如果有）。为此，我们只需在后台线程中使用同步 API。这段代码使用了两个函数 `RunInBackground` 和 `RunOnThread`，它们分别是用于生成新线程和在现有线程上运行 block 的基于 block 的 API。这些函数的实现相当直接，我就不在此重复了，但如果你需要，可以在示例项目中找到它们。

代码如下：

```
    @implementation NSURLConnection (BlocksAdditions)

    + (void)sendAsynchronousRequest: (NSURLRequest *)request
                    completionBlock: (void (^)(NSData *data, NSURLResponse *response, NSError *error))block
    {
        NSThread *originalThread = [NSThread currentThread];

        RunInBackground(^{
            WithAutoreleasePool(^{
                NSURLResponse *response = nil;
                NSError *error = nil;
                NSData *data = [self sendSynchronousRequest: request returningResponse: &response error: &error;];
                RunOnThread(originalThread, NO, ^{ block(data, response, error); });
            });
        });
    }

    @end
```

这里有几个值得注意的特性。首先，注意当前线程是如何保存到一个局部变量中，然后在稍后被另一个线程内部执行的 block 中访问的。这展示了如何轻松地在回调中使用 block 来传递上下文。然后，注意传递给 `RunInBackground` 的 block 以对 `RunOnThread` 的调用结束，后者使用另一个 block 回调到原始线程。这种嵌套的 block 消息传递对于以简洁的方式制作异步回调很方便。

以下是使用此 API 的示例：

```
    NSURLRequest *request = [NSURLRequest requestWithURL: [NSURL URLWithString: @"http://www.google.com/"]];
    [NSURLConnection sendAsynchronousRequest: request
                             completionBlock: ^(NSData *data, NSURLResponse *response, NSError *error){
        NSLog(@"data: %ld bytes  response: %@  error: %@", (long)[data length], response, error);
    }];
```

这非常好！使用异步 API 的等效代码将需要实现多个方法，并且可能需要一个全新的类。显式使用同步 API，并完成管理副线程的所有工作，以及在完成时回调到主线程（main thread），同时传递所有接收到的对象，将需要比这多得多的代码行。

**注意事项**
在使用 block 时，有一些需要注意的地方，这应该不足为奇。

当 block 被复制时，它们引用的任何局部对象变量都会被自动保留（retain）。然后当 block 被销毁时，这些变量会被自动释放（release）。这很方便，可以确保引用保持有效。任何对 `self` 的引用都是对局部对象变量的引用，导致 `self` 被保留。任何对实例变量的引用都是对 `self` 的隐式引用，也会导致同样的效果。然而，这在某些情况下很容易导致保留循环（retain cycle）。想象一下使用一个更完善的、允许取消注册通知的基于 block 的通知 API。如果你的 block 以任何方式引用了 `self`，并且你按照标准的 Cocoa 做法在 `-dealloc` 中取消注册通知，那么你的对象会泄漏，因为 block 会持有对你的对象的引用。

一个简单的解决方法是基于 `__block` 变量_不会被_保留这一事实。这是因为此类变量是可变的，对它们进行自动内存管理需要在每次改变（mutation）时在幕后生成内存管理代码。这被认为过于侵入性且难以正确处理，尤其是同一个 block 可能同时在多个线程上执行。因此，你可以像这样避免保留循环：

```
    __block MyClass *blockSelf = self;
    ^{
        [blockSelf message];
        [blockSelf->ivar message];
    };
```

捕获在非 `__block` 变量中的 CoreFoundation 类型需要 retain/release，就像 Objective-C 对象一样，因为它们实际上也是 Objective-C 对象。但是，编译器不会以这种方式看待它们。为了帮助解决这个问题，编译器添加了一个特性（attribute）`__attribute__((NSObject))`，它使得结构体指针在 block 的 retain/release 语义方面被视为 Objective-C 对象。我们可以假设 Apple 将在 10.6 上对所有 `CFTypes` 应用此特性。然而，在我们仍停留在 10.5 时，它们不会有这个特性，因此 CoreFoundation 对象在被 block 捕获时将不会被正确地内存管理。为避免问题，要么避免在 block 中捕获 CoreFoundation 对象（将变量声明为等效的 Objective-C 无缝桥接（toll-free bridged）类型将说服编译器对其执行 retain/release），要么确保 CF 对象的生命周期至少与 block 的生命周期一样长。

block 的另一个陷阱源于它们是栈对象这一事实。在幕后，使用 `^{...}` 语法本质上等同于声明一个局部变量然后获取其地址用于某些用途。地址可以被传递，但一旦你离开声明该局部变量的作用域，它就不再有效。因此，像这样看似无害的代码最终会是错误的：

```
    BasicBlock block;
    if(condition)
        block = ^{...};
    else
        block = ^{...};
```

`if` 语句（以及 `else` 子句）的主体是与主作用域分开的一个独立作用域，一旦控制流退出 `if`/`else` 子句，该作用域就会被销毁。存储在 `block` 中的 block 引用在控制流返回到主作用域时就立即失效了！只需通过复制 block 即可轻松解决此问题：

```
    BasicBlock block;
    if(condition)
        block = [[^{...} copy] autorelease];
    else
        block = [[^{...} copy] autorelease];
```

这方面主要的风险不在于它难以修复（实际上不难），而在于当你这样做时不一定容易注意到。

**结论**
本期 Friday Q&A 到此结束。你已经了解了如何让 block 在你当前的工具链上运行起来，看到了一些关于如何以有用方式使用它们的示例，以及一些需要注意的问题。现在你已经准备好立即开始在 10.5 App 中使用 block，无需等待 10.6 发布。

关于 block 有问题吗？你有自己关于如何最佳使用它们的主意吗？请在下方发表评论。

下周回来继续阅读新一期的 Friday Q&A。一如既往，Friday Q&A 由你的想法驱动。如果你有希望在这里看到的话题，请在下方发布或[通过电子邮件发送给我](mailto:mike@mikeash.com)。

你喜欢这篇文章吗？我还在卖收录此类文章的整本书！卷二和卷三现已出版！它们提供 ePub、PDF、印刷版，并在 iBooks 和 Kindle 上架。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页的评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-14-practical-blocks.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能由我全权酌情公开羞辱。

代码语法高亮致谢 [Pygments](http://pygments.org/)。
