---
title: 'Friday Q&A 2014-11-07：让我们构建 NSZombie'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-11-07-lets-build-nszombie.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7532230f3d59c519'
translated: true
---

> 原文：[Friday Q&A 2014-11-07: Let's Build NSZombie](https://www.mikeash.com/pyblog/friday-qa-2014-11-07-lets-build-nszombie.html)　·　mikeash.com Friday Q&A

发表于 2014-11-07 16:04 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2015-01-23：让我们构建 Swift 通知](https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html)  
上一篇：[短暂休整](https://www.mikeash.com/pyblog/a-brief-pause.html)  
标签：[braaaiiiinnnssss](https://www.mikeash.com/pyblog/?tag=braaaiiiinnnssss) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [zombie](https://www.mikeash.com/pyblog/?tag=zombie)

Friday Q&A 2014-11-07：让我们构建 NSZombie

作者：[Mike Ash](https://www.mikeash.com/)

**综述**  
僵尸（zombie）用来检测内存管理错误。具体来说，它们检测的是这样一种场景：一个 Objective-C 对象已被销毁，随后却有消息通过指向该对象原先所在位置的指针发送了出去。这是常见的「释放后使用（use after free）」错误的一种特例。

在正常情况下，这会导致消息被发送到一段可能已被改写或已归还内核的内存。如果内存已归还内核，就会崩溃；如果内存已被改写，也可能崩溃。如果那段内存被改写成了一个新的 Objective-C 对象，消息就会被发送到这个新对象上，而它多半与原来的对象毫无关系：这可能因无法识别的选择器（selector）而抛出异常；如果这个对象真的响应这条消息，甚至会引发种种怪异的行为。

还有一种可能：内存根本没被动过，仍然装着原来的对象，只是处于 `dealloc` 已执行完毕的状态。这可能导致另一些有趣而怪异的故障。举例来说，如果对象里含有一个 UNIX 文件句柄，它可能对同一个文件描述符调用两次 `close`，结果把程序其他部分拥有的某个文件描述符关掉了，让故障出现在离 bug 很远的地方。

ARC 已经大大降低了这类错误的出现频率，但并没有把它们彻底消灭。多线程问题、与非 ARC 代码的交互、不匹配的方法声明，或者滥用类型系统以致剥掉或改动了 ARC 存储修饰符，都可能让这些问题依然发生。

僵尸会挂进对象的销毁流程。在对象销毁的最后一步，僵尸不是释放底层的内存，而是把对象改换成一个能拦截所有发往它的消息的新僵尸类。任何发送到僵尸对象的消息，得到的都是一条诊断错误信息，而不是正常情况下那种怪异行为。还有一种模式是改写类之后照旧把内存释放掉，但那样通常没什么用，因为内存一般很快就会被复用，本文忽略这个选项。

要写出我们自己的僵尸实现，需要挂进对象销毁流程，并构建相应的僵尸类。开始吧！

**拦截所有消息**  
如果我们创建一个不带任何方法的根类（root class），那么发送到该类实例的任何消息都会进入运行时的转发机制（forwarding machinery）。这样看来，`forwardInvocation:` 似乎是个拦截消息的天然位置。然而它发生得有点太晚了。在 `forwardInvocation:` 能运行之前，运行时需要一个方法签名来构造 `NSInvocation` 对象，也就是说 `methodSignatureForSelector:` 会先运行。因此，这才是拦截发送到僵尸对象的消息的重写点（override point）。

**动态分配的类**  
除了被发送的选择器，僵尸还会记住对象原来的类。然而，对象的内存里未必有地方存放指向那个原始类的引用。如果原始类没有额外的实例变量，那就没有可以挪作存储之用的空间。因此，原始类必须存放在僵尸类里而不是僵尸对象里，这意味着僵尸类需要动态分配。每个类只要有实例变成了僵尸，就会得到一个属于自己的僵尸类。

下一个问题是把指向原始类的引用存到哪里。可以在分配类时附带一些额外的存储来放这类东西，但用起来有点麻烦。更简单的办法是直接利用类名。由于 Objective-C 的类全都住在一个大命名空间里，类名足以在进程内唯一地标识一个类。在原始类名前面加一个前缀来生成僵尸类名，得到的东西既能自述来历，又能据此还原出原始类名。我们用 `MAZombie_` 作为前缀。

**方法实现**  
注意，这里的所有代码都是在没有 ARC 的情况下构建的，因为 ARC 的内存管理调用在这里真的很碍事。

先从一个简单的方法实现开始，它是空的：

```
    void EmptyIMP(id obj, SEL _cmd) {}
```

事实证明，Objective-C 运行时假定每个类都实现了 `+initialize`。在第一条消息发送给类之前，`+initialize` 会先发送给该类，让它有机会做任何需要的准备工作。如果没有实现，运行时照样会发送它，然后撞上转发机制，这在这里毫无用处。添加一个空的 `+initialize` 实现可以避开这个问题。`EmptyIMP` 将用作僵尸类上 `+initialize` 的实现。

`-methodSignatureForSelector:` 的实现更有意思一点：

```
    NSMethodSignature *ZombieMethodSignatureForSelector(id obj, SEL _cmd, SEL selector) {
```

它先取出对象所属的类以及该类的名字。此时这个名字就是僵尸类的名字：

```
        Class class = object_getClass(obj);
        NSString *className = NSStringFromClass(class);
```

把前缀去掉就能取回原始类名：

```
        className = [className substringFromIndex: [@"MAZombie_" length]];
```

然后它记录错误并调用 `abort()`，确保你注意到了：

```
        NSLog(@"Selector %@ sent to deallocated instance %p of class %@", NSStringFromSelector(selector), obj, className);
        abort();
    }
```

**创建类**  
`ZombifyClass` 函数接收一个普通的类，返回对应的僵尸类，必要时会创建它：

```
    Class ZombifyClass(Class class) {
```

僵尸类名既能用来检查僵尸类是否存在，也能在不存在时创建它：

```
        NSString *className = NSStringFromClass(class);
        NSString *zombieClassName = [@"MAZombie_" stringByAppendingString: className];
```

僵尸类是否存在可以用 `NSClassFromString` 检查。这个调用同时会把僵尸类给出来，所以如果它已经存在，就能立即返回：

```
        Class zombieClass = NSClassFromString(zombieClassName);
        if(zombieClass) return zombieClass;
```

注意这里有一个竞态条件（race condition）：如果同一个类的两个实例在两个线程上同时被僵尸化，它们会都去尝试创建僵尸类。在真实代码里，你需要把这一整段代码包进锁里，确保这种情况不会发生。

调用 `objc_allocateClassPair` 函数来分配僵尸类：

```
        zombieClass = objc_allocateClassPair(nil, [zombieClassName UTF8String], 0);
```

我们用 `class_addMethod` 函数添加 `-methodSignatureForSelector:` 的实现。`"@@::"` 这个签名表示它返回一个对象，并接受三个参数：一个对象（`self`）、一个选择器（`_cmd`），以及另一个选择器（显式传入的选择器参数）：

```
        class_addMethod(zombieClass, @selector(methodSignatureForSelector:), (IMP)ZombieMethodSignatureForSelector, "@@::");
```

那个空方法也被添加为 `+initialize` 的实现。没有单独的函数用来添加类方法，我们的做法是把方法添加到类的类上——也就是元类（metaclass）：

```
        class_addMethod(object_getClass(zombieClass), @selector(initialize), (IMP)EmptyIMP, "v@:");
```

类设置好之后，向运行时注册并返回：

```
        objc_registerClassPair(zombieClass);

        return zombieClass;
    }
```

**把对象变成僵尸**  
为了把对象变成僵尸，我们会替换 `NSObject` 的 `dealloc` 方法的实现。子类的 `dealloc` 方法仍然会运行，但一旦调用沿继承链上溯到 `NSObject`，僵尸代码就会运行。这会阻止对象被销毁，并提供了一个把对象的类改成僵尸类的位置。这个操作被包装成一个启用僵尸的函数：

```
    void EnableZombies(void) {
        Method m = class_getInstanceMethod([NSObject class], @selector(dealloc));
        method_setImplementation(m, (IMP)ZombieDealloc);
    }
```

然后，我们可以在 `main()` 开头或类似位置放一个对 `EnableZombies` 的调用，其余的事情会自行搞定。`ZombieDealloc` 的实现很直白：它调用 `ZombifyClass` 取得正在销毁的对象对应的僵尸类，然后用 `object_setClass` 把对象的类改成僵尸类：

```
    void ZombieDealloc(id obj, SEL _cmd) {
        Class c = ZombifyClass(object_getClass(obj));
        object_setClass(obj, c);
    }
```

**测试**  
来确认它真的有效：

```
    obj = [[NSIndexSet alloc] init];
    [obj release];
    [obj count];
```

我选 `NSIndexSet` 不完全是随意的：它是一个方便的类，不会碰上 CoreFoundation 桥接的怪异问题。启用僵尸后运行这段代码，得到：

```
    a.out[5796:527741] Selector count sent to deallocated instance 0x100111240 of class NSIndexSet
```

成功！

**结语**  
僵尸实现起来其实相当简单。通过动态分配类，我们可以轻松跟踪原始类，而不必依赖僵尸对象内部的存储。`methodSignatureForSelector:` 提供了一个方便的拦截点（choke point），可以拦截发送到僵尸对象的消息。在 `-[NSObject dealloc]` 上做一个简单的挂钩，就能在对象的引用计数（retain count）降到零时把对象变成僵尸，而不是销毁它。

今天就到这里。下次再来听更多恐怖故事。在那之前，请继续[把你的主题建议发给我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-11-07-lets-build-nszombie.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
