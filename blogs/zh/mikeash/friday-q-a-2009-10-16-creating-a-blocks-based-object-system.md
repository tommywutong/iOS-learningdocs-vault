---
title: 'Friday Q&A 2009-10-16：创建一个基于 Block 的对象系统'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:53969ea4af9353ad'
translated: true
---

> 原文：[Friday Q&A 2009-10-16: Creating a Blocks-Based Object System](https://www.mikeash.com/pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html)　·　mikeash.com Friday Q&A

发布于 2009-10-16 15:50 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文文本订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2009-10-23：即将推出的功能预览](https://www.mikeash.com/pyblog/friday-qa-2009-10-23-a-preview-of-coming-attractions.html)  
上一篇文章：[XBolo 已发布！](https://www.mikeash.com/pyblog/xbolo-is-out.html)  
标签：[blocks](https://www.mikeash.com/pyblog/?tag=blocks) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna)

Friday Q&A 2009-10-16：创建一个基于 Block 的对象系统

作者：[Mike Ash](https://www.mikeash.com/)

**警告**  
 本系统怪异且相当不实用。本文的目的是探索这个系统，并思考从中可以学到哪些能应用到更现实场景中的经验。它**并非**意在让你实际拿出去使用。

**源代码**  
 希望在家里跟着实践的读者，可以[从我的公开 Subversion 仓库](http://www.mikeash.com/svn/blockobj/)获取我基础版基于 block 的对象系统的完整源代码，以及一个小型示例类和某些测试代码。

**C 语言中的面向对象**  
 多年来，C 语言中出现过许多对象系统，并不只有那些带有语言扩展（如 C++ 和 Objective-C）的系统。在 C 语言中编程的一种常见方式是使用不透明结构体（opaque structs）并提供操作它们的函数。CoreFoundation 就是一个很好的例子。下面是这种方式的典型样子：

```
    typedef struct MyFakeClass *MyFakeClassRef;
    
    MyFakeClassRef NewMyFakeClass(void);
    void DoSomethingInterestingWithFakeClass(MyFakeClassRef obj, int foo);
    void DestroyMyFakeClass(MyFakeClassRef obj);
```

这样，无需离开 C 语言就能获得面向对象编程的许多优势。你得到了封装的数据（其他代码不知道 `MyFakeClass` 的内容是什么），数据结构与操作其的代码之间有了强关联，更好的组织性等等。

当然，它也缺少面向对象的一些关键特性，比如继承。你可以通过将“方法”实际作为结构体的成员来弥补这一点：

```
    struct MyFakeClass
    {
        void (*doSomethingInteresting)(struct MyFakeClass *obj, int foo);
        void (*destroy)(struct MyFakeClass *obj);
    };
```

这种做法的问题在于有点冗余：既要使用对象来找到函数指针，又必须将它作为参数传递：

```
    struct MyFakeClass *obj = ...;
    obj->doSomethingInteresting(obj /* UGLY! */, 42);
```

然后你还需要在某处引用对象的数据，最自然的位置就是放在结构体中，紧挨着所有函数指针，暴露无遗。

**Block 登场**  
 Apple 新增的 C 语言 block 扩展给了我们与函数指针非常相似的东西，但它带有隐式上下文。调用 block 时，它们可以自动访问任何必要的数据，而无需调用者显式提供。结构体于是变成了这样：

```
    struct MyFakeClass
    {
        void (^doSomethingInteresting)(int foo);
        void (^destroy)(void);
    };
```

你可以像这样调用它上面的方法：

```
    struct MyFakeClass *obj = ...;
    obj->doSomethingInteresting(42);
```

非常不错！

这个系统允许通过简单地放入一个新的 block 来覆盖现有的“方法”，并且该新 block 可以调用到原来的那个 block。为“子类”定义全新的“方法”会稍微复杂一点，但并不难。定义子类以包含父类：

```
    struct MyFakeSubclass
    {
        struct MyFakeClass parent;
        
        void (^additionalMethod)(void);
    };
```

然后调用方可以像这样调用父类的方法：

```
    struct MyFakeSubclass *obj = ...;
    obj->parent.doSomethingInteresting(42);
```

那个 `parent` 并不理想，但可行。作为额外的好处，这种技术将覆盖现有方法与实现同名的全新方法这两个概念分开了。在大多数面向对象系统中，不可能实现一个同名的全新方法，因为它会自动被视为覆盖。在这里，它们是两个独立的操作。

将 `parent` 放在开头，可以实现子类型多态（subtype polymorphism）。通过将 `MyFakeSubclass` 的实例强制转换为 `struct MyFakeClass *`，结果仍然是一个有效的对象，它继续作为其超类的实例工作，但具有其子类给出的任何覆盖行为。

**构建系统**  
 理论就这些。现在我们实际来构建它。

第一个问题是对象实际看起来会是什么样。我们将它们定义为包含 block 指针成员的结构体，可能还带有一个指向父结构体/类的指针。这些就是我们的方法。结构体中不包含其他任何东西：任何与对象相关的数据都使用会被方法 block 捕获的局部变量来实现。

然后我们可以像这样定义一个根对象：

```
    struct RootObject
    {
        void (^retain)(void);
        void (^release)(void);
        void (^dealloc)(void);
        
        struct String *(^copyDescription)(void);
        int (^isEqual)(struct RootObject *);
    };
```

我们需要一个函数来创建根对象的新实例。我们将其命名为 `NewRootObject`。它接受一个参数：要分配的对象的大小。子类可能更大，并且内存需要是连续的，所以 `NewRootObject` 需要知道要分配多少。

为了简化创建新对象（以及计算要分配多少内存）的任务，我们将创建一个约定：新对象总是使用名为 `NewClassName` 的函数创建，该函数接受一个 size 参数。然后我们可以创建一个用于创建新对象的宏：

```
    #define Alloc(classname) New ## classname(sizeof(struct classname))
```

使用这个宏，你可以这样分配根类的一个新实例：

```
    struct RootObject *obj = Alloc(RootObject);
```

现在，`NewRootObject` 实际是什么样子的呢？

它首先需要的是“实例变量”，在这里它们只是带有 `__block` 限定符的局部变量。

```
    struct RootObject *NewRootObject(size_t size)
    {
        // "实例变量"
        __block int retainCount = 1;
```

接下来，它需要实际分配内存：

```
        // 创建对象
        struct RootObject *self = calloc(size, 1);
```

然后它可以开始填充方法。做法是声明一些 block，并将它们赋值给对应的槽位。有一个小问题：由于这些 block 需要比其封闭作用域活的更久，我们需要对它们调用 `Block_copy`：

```
        // "方法"
        self->retain = Block_copy(^{ retainCount++; });
        self->release = Block_copy(^{
            retainCount--;
            if(retainCount <= 0)
                self->dealloc();
        });
```

当然，这意味着我们最终需要 `Block_release` 它们。不过，在 `dealloc` 中手动逐一释放每个方法会非常繁琐且容易出错。为了解决这个问题，`dealloc` 方法可以扫描整个对象，找到所有 block 指针并自动释放它们。由于对象结构体本身中唯一的数据就是 block 指针，我们可以一次扫描一个指针大小的块来获取所有指针。因为我们使用 `calloc` 分配对象，我们知道由于 `malloc` 分配了多于所需的内存而导致的任何“末尾”内存都会被清零，因此任何 NULL 指针都将作为停止信号。`dealloc` 方法看起来像这样：

```
        self->dealloc = Block_copy(^{
            size_t size = malloc_size(self);
            for(void **methodPtr = (void **)self;
                 *methodPtr && ((intptr_t)methodPtr + sizeof(*methodPtr) - 1 - (intptr_t)self) < size;
                 methodPtr++)
                Block_release(*methodPtr);
            free(self);
        });
```

最后，我们定义 `copyDescription` 方法（使用尚未可见的 `String` 类的方法）并返回新对象：

```
        self->copyDescription = Block_copy(^{
            return Alloc(String)->initWithFormat("<Object %p>", self);
        });
        
        return self;
    }
```

**创建新类**  
 既然我们已经完成了所有这些，那么如何创建一个子类呢？我们来创建 `String` 类，因为根类无论如何都依赖于它。

如前所述，子类在其顶部获得一个用于其父类的 `struct`，然后在其后跟上它自己的方法，像这样：

```
    struct String
    {
        struct RootObject parent;
        
        struct String *(^initWithFormat)(char *fmt, ...);
        const char *(^cstring)(void);
    };
```

然后它只需要一个 `NewString` 函数来创建它。与 `NewRootObject` 一样，函数的第一部分用于“实例变量”：

```
    struct String *NewString(size_t size)
    {
        __block char *str = NULL;
```

接下来，和之前一样，我们分配对象。只是这次，我们不再分配原始内存，而是通过调用父类的 `New` 函数来分配对象。

```
        struct String *self = (void *)NewRootObject(size);
```

接下来，我们想要覆盖根对象的一些方法。我们想覆盖的第一个方法是 `copyDescription`。由于我们不需要调用原始实现，我们可以直接释放旧的 block，然后分配一个新的：

```
        Block_release(self->parent.copyDescription);
        self->parent.copyDescription = Block_copy(^{
            self->parent.retain();
            return self;
        });
```

接下来，我们需要覆盖 `dealloc` 以释放 `str` 变量。但这有点棘手，因为我们需要在完成后调用原始实现。为此，我们将原始实现保存到一个局部变量中，然后调用它。我们还必须注意释放原始实现：

```
        void (^superdealloc)(void) = self->parent.dealloc;
        self->parent.dealloc = Block_copy(^{
            free(str);
            superdealloc();
        });
        Block_release(superdealloc);
```

这是一个有点棘手的内存管理问题。乍一看似乎没问题，但深入思考会发现，`Block_release(superdealloc)` 调用得太早了！新的 `dealloc` block 的主体直到对象被销毁时才会运行，但 `Block_release` 在对象仍在创建时就运行了。

这实际上最终工作得非常完美，因为编译器在引用 `superdealloc` 的新 block 捕获它时，会自动对 `superdealloc` 实例变量执行 `Block_copy`。后台有一些自动的引用计数，这确保了该 block 在需要时保持存活。

最后，我们将定义 `String` 特有的方法并返回新对象：

```
        self->initWithFormat = Block_copy(^(char *fmt, ...){
            va_list args;
            va_start(args, fmt);
            vasprintf(&str, fmt, args);
            va_end(args);
            
            return self;
        });
        self->cstring = Block_copy(^{ return (const char *)str; });
        
        return self;
    }
```

我们现在有了一个功能完备、尽管简单且有点冗长的对象系统。

**自定义类** 让我们再创建一个类来巩固一下做法。我们将其命名为 `MyObject`，它只保存两个数字。这是类的结构体：

```
    struct MyObject
    {
        struct RootObject parent;
        
        struct MyObject *(^initWithNumbers)(int a, int b);
    };
```

这是创建新实例的函数：

```
    struct MyObject *NewMyObject(size_t size)
    {
        __block int numbers[2];
        
        struct MyObject *self = (void *)NewRootObject(size);
        
        // 覆盖父类方法
        Block_release(self->parent.copyDescription);
        self->parent.copyDescription = Block_copy(^{
            return Alloc(String)->initWithFormat("<MyObject %d %d>", numbers[0], numbers[1]);
        });
        
        self->initWithNumbers = Block_copy(^(int a, int b){
            numbers[0] = a;
            numbers[1] = b;
            return self;
        });
        
        return self;
    }
```

最后，是一些使用它的示例代码：

```
    struct MyObject *myobj = Alloc(MyObject);
    myobj->initWithNumbers(42, 65535);
    description = myobj->parent.copyDescription();
    printf("myobj is %s\n", description->cstring());
    description->parent.release();
    myobj->parent.release();
```

输出如你所料：

```
    myobj is <MyObject 42 65535>
```

总结一下，使用这个系统创建一个新类需要做什么：

1. 使用适当的名称定义一个新的 `struct`。
2. 作为 `struct` 的第一个成员，添加一个用于父类的 `struct`。
3. 对于 `struct` 的后续成员，为每个方法添加 block 指针。
4. 喘口气。
5. 定义适当命名的 `New` 函数。
6. 在顶部，使用 `__block` 限定符定义你需要的任何“实例变量”。
7. 通过调用父类的 `New` 函数来分配对象。
8. 通过释放原始的 block 指针并重新赋值来覆盖任何父类方法。如果需要调用原始实现，将其保存到一个局部变量中，并在重新赋值后释放该局部变量。
9. 通过赋值来初始化任何新方法。

**优点和缺点**  
 这是一个不寻常的对象系统。需要明确的是，这**不是** Objective-C（或 C++ 或 Java...）在幕后所做的。（有关 Objective-C 在幕后做了什么的信息，请查看[我的 Objective-C 运行时系列](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)）。它更类似于 JavaScript 等语言中基于原型的对象系统。

这些差异有些是好的，有些是坏的。先来看坏的方面。有很多。

- 它相当丑陋和冗长。几乎所有东西都是由约定定义的，而不是语法。调用被覆盖的父类实现尤其糟糕，但总体来说，其中有很多冗余。一组精心设计的宏可以帮助改善这一点。
- 每个对象的内存占用空间很大。在像 Objective-C 这样的语言中，一个对象是一块连续的内存，包含一个指向其类的指针，后跟该对象类所需的任何实例特定数据。对象的大小只随其包含的数据量增长。在这个系统中，一个对象是一块内存，其中包含该对象类实现的每个方法对应的一个指针。每个指针都指向一块新的内存，这些内存不与该类的其他对象共享。最后，所有这些都指向该对象类的“实例变量”以及每个父类的“实例变量”的共享存储块。那是大量的内存分配，其数量和规模远超你在 Objective-C 等语言中看到的情况。
- 对象创建和销毁非常慢。所有这些分配都需要被创建和填充。
- 类的层次结构被强制暴露给客户端代码，因为父类方法的访问方式如此。如果 `MyObject` 改为继承自 `String` 而不是 `RootObject`，任何对 `myobj->parent.release()` 的调用都必须替换为 `myobj->parent.parent.release()`。
- 完全没有元数据或内省（introspection）可用。
- 为了实现子类型多态而进行的指针强制转换在 C 语言中实际上没有定义的结果，尽管它在你能找到的几乎所有实际实现中都能工作。

为我辩解一句，这个对象系统本就不是为了实用而设计的，我大约花了一个小时构建它。

尽管如此，它还是有些优点：

- 它在纯 C 语言中工作（使用 Apple 的 block 扩展），不需要 Objective-C、C++ 或类似的东西。
- 由于它是一个单独的结构体成员加载，然后是一个 block 调用（也就是另一个结构体成员加载后跟一个函数指针调用），调用方法应该比在 Objective-C 中快。
- 方法可以在任何时候在单个对象上动态替换。例如，这就是我测试以确保当对象的 retain 计数达到零时确实调用了 `dealloc` 方法的方式：

  ```
      obj = Alloc(RootObject);
      void (^olddealloc)(void) = obj->dealloc;
      obj->dealloc = Block_copy(^{
          printf("dealloc was called!\n");
          olddealloc();
      });
      obj->release();
      Block_release(olddealloc);
  ```

  这类事情在 Objective-C 中要难得多。
- 覆盖父类方法与在子类中实现新方法完全是两个独立的行为，消除了意外覆盖，并允许子类实现一个刚好同名的完全独立的方法。
- 整个对象系统只占一页纸的篇幅，可以在短时间内很容易地理解。

再次说明，我不推荐将这个对象系统用于任何实际用途，但它仍然是一个有趣的结构。

**结论**  
 我们现在有了一个功能完备、尽管有些奇怪、基于 block 的对象系统，而且不到 100 行代码。这个对象系统虽然不完全实用，但有趣地展示了 block 为语言增加的那种能力。

本周的 Friday Q&A 就到这里。下周同一时间回来，迎接另一期激动人心的内容。由于 Friday Q&A 由你的建议驱动，请务必提出你的想法！如果你喜欢本周的文章并希望看到更多类似内容，请沿着这些路线给我更多创意。另一方面，如果你讨厌这篇文章并希望不再看到类似内容，请给我其他方向的想法！无论你有什么想法，都可以[通过邮件发送](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在销售包含全部文章的书籍！第二卷和第三卷现已出版！它们提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2009-10-16-creating-a-blocks-based-object-system.html)

发表你的想法，提交评论：

垃圾邮件和无关帖子将被删除，恕不另行通知。违规者可能会由我全权酌情决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
