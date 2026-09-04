---
title: 'Friday Q&A 2010-01-29：方法替换的乐趣与收益'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6daafc048ee16cd6'
translated: true
---

> 原文：[Friday Q&A 2010-01-29: Method Replacement for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)　·　mikeash.com Friday Q&A

发表于 2010-01-29 19:00 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2010-02-05：以续体传递风格（Continuation Passing Style）返回错误](https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html)  
上一篇：[Friday Q&A 2010-01-22：Toll Free Bridging 内部原理](https://www.mikeash.com/pyblog/friday-qa-2010-01-22-toll-free-bridging-internals.html)  
标签：[evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [override](https://www.mikeash.com/pyblog/?tag=override) [swizzling](https://www.mikeash.com/pyblog/?tag=swizzling)

Friday Q&A 2010-01-29：方法替换的乐趣与收益

作者：[Mike Ash](https://www.mikeash.com/)

**重写方法**  
 在几乎任何面向对象语言里，重写方法（method overriding）都是一项常见任务。大多数时候你通过派生子类来做到这一点，这是一种历史悠久的技巧：派生子类，在子类里实现该方法，在需要时实例化子类，于是子类的实例就会使用重写后的方法。人人都知道该怎么做。

不过有时，你需要重写的方法位于一些你无法控制其实例化的对象身上。这时派生子类就不够用了，因为你没法让那部分代码去实例化你的子类。你的方法重写只能闲坐在那里，无所事事，什么也做不成。

**扮演**  
 扮演（posing）是一种有趣的技巧，可惜如今已经过时，因为 Apple 在“新的”（64 位和 iPhone）Objective-C 运行时里不再支持它。通过扮演，你先派生子类，然后让这个子类扮演它的超类。运行时会施一些魔法，子类突然之间就在所有地方被使用了，方法重写也就重新变得有用。由于这已经不再受支持，我就不展开细节了。

**分类**  
 利用分类（category），你可以轻松重写一个既有类中的方法：

```
    @implementation NSView (MyOverride)
    
    - (void)drawRect: (NSRect)r
    {
        // 这里运行的代码会取代正常的 -[NSView drawRect:]
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
    
    @end
```

然而，只有当你要重写的方法实现在目标类的某个超类里时，这种做法才真正可行。如果要重写的方法就存在于你想重写它的那个类本身，用分类来做重写会带来两个问题：

1. 无法再调用到该方法原本的实现。新实现会直接取代原实现，原实现就那样丢失了。大多数重写都想在原有功能上做加法，而不是彻底取而代之，但用分类做不到这一点。
2. 涉及的这个类也可能在分类里实现这个方法，而当两个分类含有同名方法时，运行时并不保证哪个实现会“获胜”。

**方法调配**  
 通过一种叫做方法调配（method swizzling）的技巧，你可以在分类里替换一个既有方法，既不用纠结哪个实现“获胜”，又能保留调用回旧方法的能力。诀窍在于给重写起一个不同的方法名，然后用运行时函数把两者交换。

首先，用一个不同的名字实现重写：

```
    @implementation NSView (MyOverride)
    
    - (void)override_drawRect: (NSRect)r
    {
        // 其实这就是在调用原始实现
        [self override_drawRect: r];
        
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
    
    @end
```

注意，这里调用回原实现的方式是调用 _同一个_ 方法，看起来就像一次递归调用。之所以能行，是因为这个方法已经与原始实现交换过了。在运行时，名为 `override_drawRect:` 的方法实际上是 _原始_ 实现！

要交换方法，你需要一小段代码把新实现挪进去、把旧实现挪出来：

```
    void MethodSwizzle(Class c, SEL origSEL, SEL overrideSEL)
    {
        Method origMethod = class_getInstanceMethod(c, origSEL);
        Method overrideMethod = class_getInstanceMethod(c, overrideSEL);
```

要做到完全通用，这段代码必须处理两种情况。第一种情况：要重写的方法 _并不_ 实现在涉及的类本身，而是在某个超类里。第二种情况：该方法就存在于这个类自身。这两种情况的处理方式略有不同。

对于方法只存在于超类的情况，第一步是用重写作为实现，给这个类添加一个新方法。这一步完成之后，再把重写方法替换成原始实现。

添加新方法这一步还可以顺便充当检测，判断实际处于哪种情况。运行时函数 `class_addMethod` 在方法已存在时会失败，因此可以用来做这个检测：

```
        if(class_addMethod(c, origSEL, method_getImplementation(overrideMethod), method_getTypeEncoding(overrideMethod)))
        {
```

如果添加成功，就用原始实现替换重写方法，完成这次（概念上的）交换：

```
            class_replaceMethod(c, overrideSEL, method_getImplementation(origMethod), method_getTypeEncoding(origMethod));
        }
```

如果添加失败，那就是第二种情况：两个方法都存在于涉及的类里。对于这种情况，运行时提供了一个顺手的函数 method_exchangeImplementations，直接把两个方法原地交换：

```
        else
        {
            method_exchangeImplementations(origMethod, overrideMethod);
        }
    }
```

你会注意到，`method_exchangeImplementations` 调用用的正是代码前面已经取到的那两个方法，你可能会想：为什么不直接用它，跳过中间那些烦人的步骤呢？

代码需要区分两种情况的原因在于：如果实现位于超类，`class_getInstanceMethod` 实际返回的是 _超类_ 的 `Method`。替换那个实现就会替换错误类上的方法！

举个具体的例子，设想你要替换 `-[NSView description]`。如果 `NSView` 没有实现 `-description`（这很有可能），你拿到的就会是 `NSObject` 的 `Method`。如果你对那个 `Method` 调用 `method_exchangeImplementations`，你就会把 `NSObject` 上的 `-description` 方法换成你自己的代码，这可不是你想要的！

（在那种情况下，一个简单的分类方法就能胜任，根本不需要这段代码。问题在于，你无法知道一个类是否重写了来自其超类的方法，而且这一点甚至可能随操作系统版本而变，所以你必须假定该类可能自己实现了这个方法，并编写能够处理这种情况的代码。）

最后，我们只需要确保这段代码在程序启动时真的会被调用。这很容易：给 `MyOverride` 分类添加一个 `+load` 方法：

```
    + (void)load
    {
        MethodSwizzle(self, @selector(drawRect:), @selector(override_drawRect:));
    }
```

**直接重写**  
 不过，这有点复杂。调配的概念有些怪异，尤其是调用回原始实现的那种方式，颇为烧脑。这是一项相当标准的技巧，但我想提出一种我认为更简单的做法，无论在理解还是实现上都更容易一些。

事实证明，我们没有必要让原方法继续以“方法”的形式存在。`[self override_drawRect: r]` 里包含的动态分发（dynamic dispatch）完全是多余的——我们从一开始就知道自己要的是哪个实现。

与其把原方法挪到另一个方法里，不如直接把它的实现挪进一个全局函数指针：

```
    void (*gOrigDrawRect)(id, SEL, NSRect);
```

然后在 `+load` 里用原始实现填充这个全局变量：

```
    + (void)load
    {
        Method origMethod = class_getInstanceMethod(self, @selector(drawRect:));
        gOrigDrawRect = (void *)method_getImplementation(origMethod);
```

（这类场合我喜欢转换成 `void *`，因为它比又长又怪的函数指针类型好敲得多；而且多亏 C 语言的魔法，`void *` 反正会被隐式转换成正确的指针类型。）

接下来，替换原始实现。和之前一样，有两种情况要考虑，所以我先添加方法，如果发现方法已存在，再替换它：

```
        if(!class_addMethod(self, @selector(drawRect:), (IMP)OverrideDrawRect, method_getTypeEncoding(origMethod)))
            method_setImplementation(origMethod, (IMP)OverrideDrawRect);
    }
```

最后，实现这个重写。与之前不同，它现在是一个函数，而不是方法：

```
    static void OverrideDrawRect(NSView *self, SEL _cmd, NSRect r)
    {
        gOrigDrawRect(self, _cmd, r);
        [[NSColor blueColor] set];
        NSRectFill(r);
    }
```

确实丑了一点，但我觉得它更简单、更容易看懂。

**必不可少的警告**  
 在不属于你的类上重写方法是一件危险的事。你的重写可能破坏相关类的种种假设，从而引发问题。只要还有一丝可能，就请避开它。如果非做不可，写你的重写时务必慎之又慎。

**结语**  
 本周就到这里。现在你已经了解了 Objective-C 中方法重写的全部可能，包括一种我在别处很少见到有人讨论的变体。请把这份力量用在正道上，别用来作恶！

七天后请回来阅读下一期。在那之前，[欢迎继续把你的主题建议发给我](mailto:mike@mikeash.com)。Friday Q&A 靠读者的投稿驱动，如果你有想在这里看到的主题，就发过来吧！

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-01-29-method-replacement-for-fun-and-profit.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
