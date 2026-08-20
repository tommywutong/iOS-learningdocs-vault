---
title: '星期五问答 2010-11-19：在运行时创建类，乐趣与收益'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3a4193738af1db40'
translated: true
---

> 原文：[Friday Q&A 2010-11-19: Creating Classes at Runtime for Fun and Profit](https://www.mikeash.com/pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html)　·　mikeash.com Friday Q&A

发布于 2010-11-19 17:53 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2010-12-03: Accessors, Memory Management, and Thread Safety](https://www.mikeash.com/pyblog/friday-qa-2010-12-03-accessors-memory-management-and-thread-safety.html)  
上一篇：[Summary of the Current State of my Publications](https://www.mikeash.com/pyblog/summary-of-the-current-state-of-my-publications.html)  
标签：[fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

星期五问答 2010-11-19：在运行时创建类，乐趣与收益

作者：[Mike Ash](https://www.mikeash.com/)

**`MAObjCRuntime`**  
 在上一篇文章中，为了展示如何直接使用 Objective-C runtime，我避免使用我的面向对象封装库 [`MAObjCRuntime`](http://github.com/mikeash/MAObjCRuntime)。既然我已经展示了如何直接调用 runtime，今天我将使用 `MAObjCRuntime`，以使代码更易于读写。如果你更喜欢老派做法，`MAObjCRuntime` 的调用方式非常直接地对应 runtime 调用，只是更冗长且不那么方便。

虽然我认为这些调用会很直观，但你可能希望在继续之前阅读 [`MAObjCRuntime`](https://github.com/mikeash/MAObjCRuntime) 的 readme，以了解其工作原理。

**条件性子类化**  
 Mac 和 iOS 开发中的一个常见问题是如何同时支持多个操作系统版本。通常需要在新版本上使用某个类，而在不可用的旧版本上避免使用它。通常可以通过 `NSClassFromString` 等方法解决。然而，有时需要为这些类之一创建子类，而编写 `@interface YourClass : ThisMightNotExist` 的常规技术并不理想。

（可以通过弱链接来引入可能不存在的类，从而使用常规语法。不幸的是，Objective-C 类的弱链接还不够成熟，你必须等到它在你支持的最早操作系统版本上也能正常工作。）

通过在运行时仅在超类存在时创建子类，你可以编写出在这两种情况下都能正常工作的代码，而无需太多额外工作。

作为示例，我将展示如何为一个可能在运行时不存在的假设类 `NSFoo` 创建子类。该子类将重写其超类的一个方法 `-bar`，使其不执行任何操作。

首先，编写实现 `-bar` 方法的函数。如你上次所记，只需编写一个 C 函数，将 `id self` 和 `SEL _cmd` 作为前两个参数，其他参数和返回类型照常。以下是一个简单的空操作函数：

```
    static void BarOverride(id self, SEL _cmd)
    {
    }
```

现在，编写创建子类的函数。首先使用 `rt_createSubclassNamed:` 创建类。

```
    static Class CreateMyFoo(void)
    {
        Class NSFoo = NSClassFromString(@"NSFoo");
        if(!NSFoo)
            return nil;
        
        Class myFoo = [NSFoo rt_createSubclassNamed: @"MyFoo"];
```

现在添加新的 `-bar` 方法。首先从超类获取该方法以借用其类型签名字符串，然后创建一个新的 `RTMethod` 并将其添加到子类中：

```
        SEL sel = @selector(bar);
        RTMethod *nsBar = [NSFoo rt_methodForSelector: sel];
        RTMethod *myBar = [RTMethod methodWithSelector: sel implementation: (IMP)BarOverride signature: [nsBar signature]];
        [myFoo rt_addMethod: myBar];
```

就这样！现在只需返回新创建的类：

```
        return myFoo;
    }
```

为了完善代码，我们只需编写一个简单的包装函数，该函数创建上述类一次并存储它，然后按需返回。（我使用 GCD 来保证线程安全，这可能会违背兼容旧系统的初衷，但可以轻松替换为其他方法。）

```
    static Class MyFoo(void)
    {
        static Class c = nil;
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
            c = CreateMyFoo();
        });
        
        return c;
    }
```

因为 `CreateMyFoo` 在 `NSFoo` 不存在时返回 `nil`，所以 `MyFoo` 在这种情况下也会返回 `nil`。调用者使用 `MyFoo` 只需要这样做：

```
    Class myFoo = MyFoo();
    if(myFoo)
    {
        id foo = [[myFoo alloc] init];
        // ...
    }
```

**调用 `super`**  
 在重写的方法中调用 `super` 非常常见。不幸的是，`super` 关键字在 C 函数中无效，即使你用它来实现 Objective-C 方法。

但仍然是可行的，而且并不太难，只是需要稍微绕个弯。你需要手动从超类获取方法指针，然后直接调用它。下面是 `BarOverride` 仅调用 `super` 的样子：

```
    static void BarOverride(id self, SEL _cmd)
    {
        Class superclass = NSClassFromString(@"NSFoo");
        void (*superIMP)(id, SEL) = (void *)[superclass instanceMethodForSelector: @selector(bar)];
        superIMP(self, _cmd);
    }
```

仅仅调用 `super` 并没有太大用处，但你可以在调用前后添加自己的代码来增强它。

**示例子类**  
 下面是一个更现实的示例，它为假设的 `NSMysteryView` 创建子类，以添加自定义绘制和事件处理：

```
    static DrawRect(id self, SEL _cmd, NSRect rect)
    {
        // 绘制原始内容，但放在黑色背景之上
        [[NSColor blackColor] setFill];
        NSRectFill(rect);
        
        // 黑色背景已绘制完成，现在绘制原始内容
        Class superclass = NSClassFromString(@"NSMysteryView");
        void (*superIMP)(id, SEL, NSRect) = [superclass instanceMethodForSelector: @selector(drawRect:)];
        superIMP(self, _cmd, rect);
    }
    
    static MouseUp(id self, SEL _cmd, NSEvent *event)
    {
        // 如果在该视图中点击鼠标，则发出哔声
        NSBeep();
    }
    
    // 封装重写已有方法所需的代码
    static void Override(Class c, SEL sel, void *fptr)
    {
        RTMethod *superMethod = [[c superclass] rt_methodForSelector: sel];
        RTMethod *newMethod = [RTMethod methodWithSelector: sel implementation: fptr signature: [superMethod signature]];
        [c rt_addMethod: newMethod];
    }
    
    static Class CreateMyMysteryView(void)
    {
        Class NSMysteryView = NSClassFromString(@"NSMysteryView");
        if(!NSMysteryView)
            return nil;
        
        Class c = [NSMysteryView rt_createSubclassNamed: @"MyMysteryView"];
        Override(c, @selector(drawRect:), DrawRect);
        Override(c, @selector(mouseUp:), MouseUp);
        
        return c;
    }
```

**通过动态子类化拦截调用**  
 有时你需要在事先不知道目标对象的情况下拦截对某个任意对象的调用。通过在运行时创建目标对象类的子类，然后交换（swizzling）目标对象的类，你可以实现这种拦截。Cocoa 的 [Key-Value Observing](https://www.mikeash.com/pyblog/friday-qa-2009-01-23.html) 以及我自己的 [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef) 都采用了这种方法。在这里，我将逐步介绍如何为你自己实现这一点。作为一个简单的例子，我将展示如何通过重写对象的 `dealloc` 方法来观察其何时被释放，这类似于 `MAZeroingWeakRef` 的轻量版本。

快速提示：为了保持简单，我将展示的所有代码都不是线程安全的。由于这是你可能希望从多个线程使用的低级代码（特别是因为 `dealloc` 可能在其他线程上发生），请记住，更实用的版本需要锁定对所有共享数据的访问。

当对象即将被销毁时，它将发布一个通知。当然，我们需要一个常量来保存通知名称：

```
    NSString *MyObjectWillDeallocateNotification = @"MyObjectWillDeallocateNotification";
```

现在，我们只想为任何给定的类创建一个子类。如果系统中有两个相同类的对象，它们都应该被交换到同一个动态子类，而不是创建两个相同的动态子类。为此，我们将维护一个从类到子类的字典。同时维护一个已创建子类的集合也很有用：

```
    static NSMutableDictionary *gSubclassesDict;
    static NSMutableSet *gSubclasses;
```

现在，一个小函数来查询字典，要么返回已有的内容，要么调用一个创建子类的函数，将其插入字典并返回：

```
    static Class GetSubclassForClass(Class c)
    {
        Class subclass = [gSubclassesDict objectForKey: c];
        if(!subclass)
        {
            subclass = CreateSubclassForClass(c);
            [gSubclassesDict setObject: subclass forKey: c];
            [gSubclasses addObject: subclass];
        }
        return subclass;
    }
```

在编写 `CreateSubclassForClass` 之前，我们需要编写一个 `dealloc` 的重写函数。这个重写函数需要做的就是发布通知，然后调用 `[super dealloc]`。然而，调用 `super` 很复杂，因为这不仅是一个动态分配的类，而且其超类在编译时未知。因此，我们需要在运行时进行搜索，找到正确的超类。

在这种情况下，*不能*简单地使用 `[self superclass]`。虽然我们的动态子类*可能*是最后设置的类，因此 `[self superclass]` *可能*返回正确的答案，但这并不保证。其他代码（如 KVO）可能在我们之后使用了相同的动态子类化技巧，这意味着它们的类会处于最底层，而不是我们的类。为了真正健壮，我们必须循环搜索，直到找到一个在 `gSubclassesDict` 中有条目的类，然后才向那个类发送我们的 `dealloc` 消息。

以下是完整的 `dealloc` 重写函数的实现：

```
    static void Dealloc(id self, SEL _cmd)
    {
        [[NSNotificationCenter defaultCenter] postNotificationName: MyObjectWillDeallocateNotification object: self];
        
        Class c = [self rt_class];
        while(c && ![gSubclassesDict objectForKey: c])
            c = [c superclass];
        
        // 如果找不到，说明出了严重问题
        assert(c);
        
        void (*superIMP)(id, SEL) = [c instanceMethodForSelector: @selector(dealloc)];
        superIMP(self, _cmd);
    }
```

现在我们准备编写 `CreateSubclassForClass`。这里没有复杂之处，它看起来就像我们之前编写的其他子类创建代码：

```
    static Class CreateSubclassForClass(Class c)
    {
        // 为子类指定一个合理的名称
        NSString *name = [NSString stringWithFormat: @"%@_MyDeallocNotifying", [class name]];
        Class subclass = [c rt_createSubclassNamed: name];
        
        // 使用上面的 Override 函数
        Override(c, @selector(dealloc), Dealloc);
        
        return subclass;
    }
```

最后，一个转换对象以使其发布此通知的函数。我们首先通过检查对象的类层级中是否已有我们的子类来判断它是否已经被添加：

```
    void MakeObjectPostDeallocNotification(id obj)
    {
        Class c = [obj rt_class];
        while(c && ![gSubclasses containsObject: c])
            c = [c superclass];
        // 如果找到了一个，则无需再做其他事情
        if(c)
            return;
        
        // 尚未设置，获取子类
        c = GetSubclassForClass([obj rt_class]);
        // 将对象的类设置为子类
        [obj rt_setClass: c];
    }
```

就这样！你现在可以调用 `MakeObjectPostDeallocNotification(obj)`，然后使用 `NSNotificationCenter` 来监听通知。

**注意事项**  
 这种技术有一些陷阱。从易到难排列：

1. **归档：**如果目标对象被归档，归档器会记录自定义子类。解归档时，它会尝试实例化该自定义子类。由于这些类是动态创建的，该类可能不存在，从而阻止解归档器实例化对象。要解决此问题，你可以在子类中重写 `classForCoder` 以返回超类，这样归档器就会记录正确的类。
2. **KVO 子类：**如前所述，KVO 使用了相同的技术。不幸的是，Apple 的代码不容忍在其自定义类之下创建子类。要解决此问题，你可以为“真正的”类创建子类，然后将你的新子类插入到 KVO 类和“真正的”类之间的类层级中。[`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef/blob/master/Source/MAZeroingWeakRef.m) 展示了如何做到这一点，只需搜索“KVO”。
3. **CoreFoundation 桥接类：**由于 toll-free bridging 的实现方式，你无法为桥接类创建子类，也无法以其他方式可靠地拦截发送给它们的消息。根据你具体要做什么，你可以尝试[使用一些非常肮脏的 hack](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)，但通常最好的办法是根本不要试图干涉桥接类。

**结论**  
 在运行时创建类是一项强大的技术。今天，我展示了如何使用它在编译时无法引用的类上创建子类，以及如何为任意类动态创建子类以拦截对它们的调用。这类技术用好了可以做大事情，但也很容易搬起石头砸自己的脚，但它也能让你做到一些原本无法做到的事情。

今天就到这里。两周后回来再看另一篇星期五问答。一如既往，如果你有想在这里看到的话题创意，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我出售包含它们的整本书！卷 II 和卷 III 现已出版！它们以 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式提供。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-11-19-creating-classes-at-runtime-for-fun-and-profit.html)

发表你的想法，添加评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
