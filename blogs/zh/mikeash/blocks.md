---
title: blocks
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'http://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af10c3a33bd3115b'
translated: true
---

> 原文：[blocks](http://www.mikeash.com/pyblog/friday-qa-2009-08-14-practical-blocks.html)　·　mikeash.com Friday Q&A

发布于 2009-08-14 20:06 | [RSS 订阅](http://www.mikeash.com/pyblog/rss.py) ([全文 RSS](http://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](http://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2009-08-21: Writing Vararg Macros and Functions](http://www.mikeash.com/pyblog/friday-qa-2009-08-21-writing-vararg-macros-and-functions.html)  
上一篇：[Friday Q&A 2009-07-17: Format Strings Tips and Tricks](http://www.mikeash.com/pyblog/friday-qa-2009-07-17-format-strings-tips-and-tricks.html)  
标签：[blocks](http://www.mikeash.com/pyblog/?tag=blocks) [fridayqna](http://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-08-14：实用 Blocks

作者：[Mike Ash](http://www.mikeash.com/)

尽管 Apple 尚未在任何一个开发工具中正式发布 blocks，但由于他们参与了开源编译器 gcc 和 clang 的开发，他们已经发布了 blocks 实现的代码。Landon 利用这些代码制作了 [PLBlocks](http://code.google.com/p/plblocks/)，它允许在 Mac OS X 10.5 上构建和运行基于 blocks 的代码。虽然 10.5 上没有基于 blocks 的 API（除了属于运行时的一些非常基础的部分），但它们仍然可以被有效地使用。

我不会在这里介绍 PLBlocks 的安装或基本用法，因为 PLBlocks 页面已经提供了非常详细的说明。如果你想跟着做，可以去那个页面按照指示操作。关于 blocks 如何工作的更多信息，请参见 Clang 的 [blocks 语言规范](http://clang.llvm.org/docs/BlockLanguageSpec.txt) 和 [实现规范](http://clang.llvm.org/docs/BlockImplementation.txt)。

我还假设你已经了解 block 语法和用法的基础知识，这些内容在[我上一期关于这个主题的 Friday Q&A](http://www.mikeash.com/pyblog/friday-qa-2008-12-26.html) 中介绍过。今天是那期的第二部分。如果你还没读过，请先去阅读那一期。

**基础知识**
Blocks 是 Objective-C 对象。当你在代码中编写一个 block 时，它是一个对象类型的表达式，很像 `@"..."` 常量字符串语法会给你一个对象类型的表达式。然后你可以像使用其他任何 Objective-C 对象一样使用这个对象：向它发送它可以响应的消息，把它放入容器中，把它作为参数传递，返回它，等等。

与常量字符串语法有一个主要区别。与常量字符串不同，blocks 并非每次执行同一段代码时都完全相同。这是因为 blocks 会捕获它们的外层作用域，而这个作用域在每次被调用时都不同。简而言之，每次代码执行到一个 `^{...}` 构造时，都会创建一个新对象。

每次都分配一个新对象会有点慢，所以 blocks 采用了一种不同寻常的方式：从 `^{...}` 构造得到的对象是一个*栈对象*。这意味着它的生命周期与局部变量相同，并在离开当前作用域时自动销毁。很奇怪，对吧？

让一个 block 的生命周期超过其创建时所在的作用域是常有用的。例如，你可能想要返回一个 block，或者把它保存起来供以后使用。为了实现这一点，你必须拷贝（copy）这个 block。你可以像操作其他 Objective-C 对象那样，向它发送 `-copy` 消息来完成拷贝。并且，和其他 Objective-C 对象一样，如果你没有在垃圾回收（Garbage Collection）环境下运行，那么你拥有生成的对象，最终必须使用 `-release` 或 `-autorelease` 来释放它。

以下是一个从方法返回 block 的示例：

```
    - (void (^)(void))block { return [[^{ ... } copy] autorelease]; }
```

请注意，对外部变量的捕获默认会生成这些变量的 const 副本。换句话说，下面的代码是不合法的：

```
    int i;
    ^{ i++; };
```

解决这个问题的方法是使用 `__block` 关键字，像这样：

```
    __block int i;
    ^{ i++; };
```

要求像这样显式标记局部变量的原因是因为 `__block` 变量的成本比常规变量高得多，并且在应用于 Objective-C 对象指针时具有不同的语义（稍后会详细介绍），因此 blocks 的开发者们认为，与其制定一个一刀切的策略，不如让程序员自己选择。

**示例**
我将展示一系列示例，来说明如何借助 PLBlocks 在 10.5 上使用 blocks。想要跟着做的读者可能想看看我构建的示例项目，你可以从我的公共 subversion 仓库获取，地址如下：

```
    svn co http://www.mikeash.com/svn/PLBlocksPlayground/
```

如果你只想浏览代码，可以直接点击该命令中的链接。

**自定义 API**
这就是它们工作原理的基本概念，现在我们来看看可以用它们做什么。

正如我在第一篇关于 blocks 的文章中提到的，blocks 本质上允许你构建新的控制（control）构造，而无需修改语言本身。在深入之前，我想先介绍一个小巧的 typedef 来简化事情。大多数控制构造的 block 是不带参数且不返回值的 block。因此，将这种类型包装成写起来更友好的形式会很好：

```
    typedef void (^BasicBlock)(void);
```

作为一个非常简单的例子，让我们看看 Cocoa 中一个相当常见的任务：使用一个内部的自动释放池来运行一些代码，以保持内存高水位标记较低。通常看起来像这样：

```
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    ...
    [pool release];
```

这也不算太糟，但有点冗长。我们可以编写一个宏（macro）来做这件事，但宏相当邪恶，而且通常有隐藏的陷阱。相反，让我们用 blocks 编写一个小函数来做这件事：

```
    void WithAutoreleasePool(BasicBlock block)
    {
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        block();
        [pool release];
    }
```

然后我们可以像这样使用它：

```
    for(id obj in array)
        WithAutoreleasePool(^{
            [self createLotsOfTemporaryObjectsWith:obj];
        });
```

这比手动编写要更快更容易，而且最终同样可读。很棒！

让我们处理一些更复杂的事情。在 Cocoa App 中，经常需要使用 `-performSelector:withObject:afterDelay:` 在短暂的延迟后运行一些代码。我们经常使用零延迟来表示“在返回到运行循环后立即运行这段代码”。这样做的问题是它需要一个对象和一个单独的方法，并且传递相关的上下文可能很痛苦。让我们改为编写一个快速的 blocks 函数：

```
    void RunAfterDelay(NSTimeInterval delay, BasicBlock block)
    {
        [[[block copy] autorelease] performSelector: @selector(my_callBlock) withObject: nil afterDelay: delay];
    }
```

注意，我们必须对 block 进行 copy/autorelease，以便该对象在 perform 完成之前保持存活。这利用了一个在 NSObject 上的小分类（category）来实际调用这个 block，利用了 blocks 也是 NSObject 这一事实：

```
    @implementation NSObject (BlocksAdditions)
    
    - (void)my_callBlock
    {
        void (^block)(void) = (id)self;
        block();
    }
    
    @end
```

然后我们可以像这样使用它：

```
    NSString *something = ...;
    RunAfterDelay(0, ^{
        NSLog(@"%@", something);
        [self doWorkWithSomething: something];
    });
```

对于任何更复杂的情况，这比典型的 Cocoa 模式要容易处理得多。

我们经常编写的另一件事是由锁保护的临界区代码。通常看起来像这样：

```
    [lock lock];
    ...do stuff...
    [lock unlock];
```

然而，这有点容易出错。例如，如果你忘记在某个代码路径上解锁锁，或者从中间返回，或者抛出异常，那么你的 App 就会死锁。编写上述代码最安全的方法是使用 `@try/@finally` 块，像这样：

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

这有点笨重。我们可以把这个惯用写法转换为一个基于 blocks 的 NSLock 上的方法，以完全自动地处理加锁和解锁：

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

这并不完全相同。例如，使用显式的 `@try/@finally`，你可以从 `@try` 块内部的方法中返回一个值，这样做是有效的；而从 block 内部这样做只会出错，因为你将从 block 中返回一个值，这会使得 block 的类型不兼容。可以通过使用 `__block` 限定的变量来持有返回值来解决这个问题。在我看来，这样做更好，因为它有助于阻止在临界区内进行棘手的行为，而临界区的潜在 bug 风险很高。

**风格说明**
上面的代码中有两个有趣的选择，都是出于同样的原因。第一个选择是，这些是函数，而不是方法。由于 blocks 是 NSObject，因此可以在 NSObject 上使用分类方法。我们可以不在 NSObject 上编写一个 `-runAfterDelay:` 方法，而不是一个 `RunAfterDelay` 函数。第二个选择是总是把 block 参数放在最后，即使它是最重要的参数，放在第一位会更合理。

这两者的原因都是，你希望 block 绝对在最后，这样当 block 被分成多行时，你的代码仍然可读。例如，想象一些嵌套的 blocks 代码，使用上面的函数，但用方法重新实现：

```
    [^{
        for(id obj in array)
            [^{
                [self doImportantWork:obj];
            } withAutoreleasePool];
    } runAfterDelay: 0];
```

这显然可读性更差。代码出现在前面，而对它做什么只有在最后才出现，这可能会在很后面。当嵌套时，你必须以 LIFO 顺序阅读所有内容。出于这个原因，用方法编写控制构造是一个坏主意，并且在将 block 作为参数时，总是把 block 放在最后。

**集合**
将 blocks 与集合一起使用可以产生强大的循环构造。让我们从一个在 `NSArray` 上的方法开始，它非常简单，可替代 for 循环：

```
    - (void)do: (void (^)(id obj))block
    {
        for(id obj in self)
            block(obj);
    }
```

这实际上并不是那么有趣。它最终就像一个 `for/in` 循环，但没有静态类型化对象的能力。（至少在 Apple 引入 `for/in` 之前，它会很不错，这说明了使用 blocks 添加你自己的控制构造的想法。）使用示例：

```
    NSArray *array = ...;
    [array do: ^(id obj){ NSLog(@"%@", obj); }];
```

不太令人兴奋。这是一个更有趣的例子。它使用一个 block 将一个数组映射到一个新数组：

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

这展示了如何使用它来从一个人数组构造一个名字字符串数组：

```
    NSArray *people = ...;
    NSArray *names = [people map: ^(id person){
        return [NSString stringWithFormat: @"%@ %@", [person firstName], [person lastName]];
    }];
```

这比手动编写封装在 `-map:` 方法中的循环要好得多。通过传递 blocks，我们只需要编写一次那个循环，然后多次重用它。

再举一个例子，这允许过滤数组：

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

用它来过滤掉太短的字符串的示例：

```
    NSArray *longStrings = [strings select: ^ BOOL (id obj) { return [obj length] > 5; }];
```

注意显式的返回值。C 比较运算符的结果是 `int`，而不是 `BOOL`，所以让编译器推断返回值会产生一个类型不兼容的 block。另一种方法是在 return 语句中对表达式进行类型转换。

这是一个在 GUI App 中的使用示例，用于获取特定视图（view）内的所有文本字段：

```
    NSArray *textFields = [[view subviews] select: ^(id obj){ return [obj isKindOfClass: [NSTextField class]]; }];
```

**回调**
基于回调的 API 是 blocks 真正闪光的地方。与其传递一对选择器/委托（selector/delegate），或者一对函数指针/上下文指针，不如传递一个 block。它使得传递上下文变得容易得多（因为 block 自动打包了所有需要的上下文），并将所有代码保持在一起。

回调的一个明显例子是通知（notification）。虽然将通知分离成单独的方法通常有好处，但实现起来很容易，有时可以让代码更漂亮：

```
    @implementation NSNotificationCenter (BlocksAdditions)
    
    - (void)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block
    {
        [self addObserver: [block copy] selector: @selector(my_callBlockWithObject:) name: name object: object];
    }
    
    @end
```

`my_callBlockWithObject:` 方法是在 `NSObject` 的一个分类中实现的，很像前面看到的 `my_callBlock` 方法，除了它接受一个参数并将该参数传递给 block。

你可以像这样使用它：

```
    [[NSNotificationCenter defaultCenter] addObserverForName: NSApplicationDidBecomeActiveNotification
                                                      object: nil
                                                       block: ^(NSNotification *note){ NSLog(@"Did become active"); }];
```

请注意，没有提供停用通知 block 的机制。这可以添加，但需要调用者管理额外的状态。这种机制作为练习留给读者。

表单（sheet）是 Cocoa 中痛苦的基于回调的 API 的一个很好的例子。你必须实现一个回调方法，然后将与表单相关的所有状态（通常很大）塞进要么提供的单个 `void *` 上下文参数，要么塞进实例变量中。这两种方式都不特别好。

这里有一个小的分类，将这个 API 转换为使用 blocks：

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

现在你可以简单地提供一个内联的 block，直接放在你的其余代码中，并直接访问所有必需的上下文。

另一个类似痛苦 API 的例子是 `NSURLConnection`。它提供了两种模式：同步和异步。同步模式只能从辅助线程使用，该线程可以被任意长时间阻塞，因为任何网络操作都可能需要很长时间才能完成。异步模式需要编写大量样板代码。让我们编写一个添加异步模式的方法，该模式在完成时简单地调用一个 block 来交出数据、响应元数据和错误（如果有的话）。为此，我们只需在后台线程中使用同步 API。这段代码使用了两个函数，`RunInBackground` 和 `RunOnThread`，它们分别是用于生成新线程和在现有线程上运行 block 的基于 blocks 的 API。这些函数的实现相当直接，我不会在这里重复，但如果你需要，可以在示例项目中找到它们。

代码如下所示：

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

这里有几个值得注意的特性。首先，注意当前线程是如何被保存到一个局部变量中，然后稍后在一个将在不同线程上执行的 block 内部被访问的。这展示了 blocks 如何被用来在回调中轻松地传递上下文。然后，注意传递给 `RunInBackground` 的 block 以调用 `RunOnThread` 结束，后者使用另一个 block 回调到原始线程。这种嵌套的 block 消息传递对于简洁地实现异步回调很方便。

以下是使用此 API 的示例：

```
    NSURLRequest *request = [NSURLRequest requestWithURL: [NSURL URLWithString: @"http://www.google.com/"]];
    [NSURLConnection sendAsynchronousRequest: request
                             completionBlock: ^(NSData *data, NSURLResponse *response, NSError *error){
        NSLog(@"data: %ld bytes  response: %@  error: %@", (long)[data length], response, error);
    }];
```

这非常好！使用异步 API 的等效方法需要实现多个方法，并且可能还需要一个全新的类。显式地使用同步 API，并完成管理辅助线程的所有工作，以及在完成时回调到主线程，并传递所有接收到的对象，将需要比这多得多的代码行。

**注意事项**
使用 blocks 时需要注意一些事情，这应该不足为奇。

当 blocks 被拷贝时，它们引用的任何局部对象变量都会被自动 retain。然后当 block 被销毁时，它们被自动 release。这对于确保引用保持有效很方便。任何对 `self` 的引用都是对局部对象变量的引用，导致 `self` 被 retain。任何对实例变量（instance variable）的引用都是对 `self` 的隐式引用，并导致相同的情况。然而，这在某些情况下很容易引起 retain 循环。想象一下，使用一个更完善的、基于 blocks 的通知 API 版本，它允许注销通知。如果你的 block 以任何方式引用了 `self`，并且你做了标准 Cocoa 的做法，即在 `-dealloc` 中注销通知，你的对象将会泄漏，因为 block 会持有对你的对象的一个引用。

对此的一个简单解决方法在于 `__block` 变量*不会被* retain。这是因为这种变量是可变的，对它们进行自动内存管理会要求每次修改都在背后生成内存管理代码。这被认为过于侵入且难以正确实现，特别是当同一个 block 可能同时从多个线程执行时。因此，你可以像这样避免 retain 循环：

```
    __block MyClass *blockSelf = self;
    ^{
        [blockSelf message];
        [blockSelf->ivar message];
    };
```

CoreFoundation 类型在被捕获到非 `__block` 变量中时需要进行 retain/release，就像 Objective-C 对象一样，因为它们实际上也是 Objective-C 对象。然而，编译器并不这样看待它们。为了帮助解决这个问题，编译器添加了一个特性（attribute），`__attribute__((NSObject))`，它使得结构体指针在 block 的 retain/release 语义方面被当作 Objective-C 对象处理。我们可以假设 Apple 将在 10.6 上将此特性应用于所有 `CFTypes`。然而，当我们停留在 10.5 上时，它们不会有这个特性，因此 CoreFoundation 对象在被 blocks 捕获时不会被正确地内存管理。为了避免问题，要么避免在 blocks 中捕获 CoreFoundation 对象（将变量声明为等价的 Objective-C 免费桥接类型（toll-free bridged type），反而会说服编译器 retain/release 它们），要么确保 CF 对象的生命周期至少与 block 的生命周期一样长。

使用 blocks 的另一个陷阱是它们是一个栈对象。使用 `^{...}` 语法本质上等同于，在幕后，声明一个局部变量，然后获取它的地址，传递给别处。地址可以被传递，但一旦你离开声明局部变量的作用域，它就不再有效。因此，像这样无害的代码最终会成为有问题的代码：

```
    BasicBlock block;
    if(condition)
        block = ^{...};
    else
        block = ^{...};
```

`if` 语句（和 `else` 子句）的主体是一个与外部作用域（main body）分开的作用域，一旦控制流退出 `if`/`else` 子句，它就会被销毁。存储在 `block` 中的 block 引用在控制流返回到外部作用域时立即无效！只需通过拷贝 blocks 就可以轻松修复：

```
    BasicBlock block;
    if(condition)
        block = [[^{...} copy] autorelease];
    else
        block = [[^{...} copy] autorelease];
```

这方面主要的风险不是修复起来困难（并不困难），而是当你这样做时，不一定容易注意到。

**结论**
本周的 Friday Q&A 到此结束。你已经了解了如何在你当前的工具链中启动并运行 blocks，一些如何以有用方式使用它们的例子，以及一些需要注意的问题。现在你已经准备好立即开始在你的 10.5 App 中使用 blocks，无需等待 10.6 发布。

关于 blocks 有问题吗？对于最佳使用方式有自己的想法吗？请在下方发表评论。

下周回来收看新一期的 Friday Q&A。一如既往，Friday Q&A 由你的想法驱动。如果你有希望在这里看到的主题，请在下方发表，或者[通过电子邮件发送给我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我正在销售包含所有文章的完整书籍！第 II 卷和第 III 卷现已出版！有 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击此处获取更多信息](http://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](http://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-08-14-practical-blocks.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
