---
title: 'Friday Q&A 2011-05-20：僵尸的内在生活'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:948667e0dd9ba332'
translated: true
---

> 原文：[the implementation of zombies](https://www.mikeash.com/pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)　·　mikeash.com Friday Q&A

发表于 2011-05-20 16:00 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2011-06-03：Objective-C Blocks 与 C++0x Lambdas：对决！](https://www.mikeash.com/pyblog/friday-qa-2011-06-03-objective-c-blocks-vs-c0x-lambdas-fight.html)  
上一篇：[Friday Q&A 2011-05-06：MABlockClosure 漫游](https://www.mikeash.com/pyblog/friday-qa-2011-05-06-a-tour-of-mablockclosure.html)  
标签：[braaaiiiinnnssss](https://www.mikeash.com/pyblog/?tag=braaaiiiinnnssss) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [zombie](https://www.mikeash.com/pyblog/?tag=zombie)

Friday Q&A 2011-05-20：僵尸的内在生活

作者：[Mike Ash](https://www.mikeash.com/)

**僵尸概述**  
 [如果你还记得](http://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)的话，一个 Objective-C 对象就是一块分配好的内存。这块内存开头一个指针大小的部分就是 `isa` 指针，它指向对象所属的类。块的其余部分装着对象的实例变量。

对象被销毁时，容纳它的那块内存会被释放。通常这只是意味着它被标记为可供复用。如果你搞砸了，还留着指向这个已销毁对象的指针，就可能发生许多神秘的事情。

某些情况下，试图使用已销毁对象的代码会一切正常。如果那块内存实际上还没被改写，它仍会表现得像一个正常的 Objective-C 对象。

更常见的情况是，销毁后的内存会被复用来容纳一个新对象。这时，旧指针最终指向的就是这个新对象。使用旧指针的尝试会把消息发送给新对象，结果令人困惑。这就是为什么内存管理错误最常见的症状之一，是一个神秘对象……比如一个不知从哪来的 `NSString`，出现在你本以为是别的东西的位置上。

偶尔，内存会被不是对象的东西改写，你的代码随之崩溃。这是三种结果里最好的一种，因为它失败得更快，也更容易看清哪里出了问题，不过它往往比较少见。

僵尸极大地改善了针对这种常见场景的诊断手段。僵尸不会对已销毁的内存听之任之，而是把它接管过来，替换成一个能困住所有访问尝试的对象。这就是「僵尸（zombie）」一词的由来：死去的对象被复活成某种不生不死的存在。向僵尸对象发送消息时，它会记录一条错误并崩溃，同时提供一份便利的回溯（backtrace），让你能看清问题究竟出在哪里。

**使用僵尸**  
 把环境变量 `NSZombieEnabled` 设为 `YES` 就能启用僵尸。在 `gdb` 里运行你的 App，任何对死去对象的访问尝试都会引发崩溃。不过要小心：默认情况下，僵尸永远不会被销毁，所以你的 App 的内存占用可能变得极高。

另一个有用的选项是 Instruments 里的 Zombies instrument。它会启用僵尸，还会跟踪对象的引用计数（retain count），让你可以回头查看任何收到不当消息的对象的 retain/release 活动。

**探究僵尸**  
 我们来看看这些东西在幕后都做了些什么。为了便于调查，我写了一个小函数来转储（dump）对象的内容：

```
    void Dump(NSString *msg, id obj, int size)
    {
        NSString *s = [NSString stringWithFormat: @"%@ malloc_size %d - %@", msg, (int)malloc_size(obj), [NSData dataWithBytes: obj length: size]];
        printf("%s\n", [s UTF8String]);
    }
```

至于大小，调用方可以用 `malloc_size` 取得所分配内存块的大小。之所以留给调用方，是因为 `malloc_size` 对已销毁的内存块不起作用，所以调用方必须趁对象还活着时取出大小，然后把它保存下来。

我们来创建一个 `NSObject`，在它被销毁前后分别记录内容：

```
    id obj = [[NSObject alloc] init];
    int size = malloc_size(obj);
    Dump(@"Fresh NSObject", obj, size);
    [obj release];
    Dump(@"Destroyed NSObject", obj, size);
```

这是不启用僵尸时的正常运行结果：

```
    Fresh NSObject malloc_size 16 - <68046370 ff7f0000 00000000 00000000>
    Destroyed NSObject malloc_size 0 - <68046370 ff7f0000 00000000 00000000>
```

注意 `malloc_size` 在销毁后变成了 `0`，说明这块内存现在已释放。还要注意其他什么都没变。对象在销毁前后包含的内容一模一样。这个对象在销毁之后仍然可以使用。

再启用僵尸试一次：

```
    Fresh NSObject malloc_size 16 - <68046370 ff7f0000 00000000 00000000>
    Destroyed NSObject malloc_size 16 - <d0011100 01000000 00000000 00000000>
```

现在能看到一些差异了。首先，`malloc_size` 仍然报告 `16`，说明内存从未被释放。其次，对象的内容变了。`isa` 指针占据对象的前八个字节（这里运行在 64 位模式下），也就是上面转储结果里的前两组。之后 `isa` 指针变得完全不同。

后八个字节在这里没有用到。我们来写一个用到它的简单 Dummy 类，看看它的表现：

```
    @interface Dummy : NSObject
    {
        uintptr_t secondEight;
    }
    @end
```

```
    @implementation Dummy
    - (id)init
    {
        if((self = [super init]))
            secondEight = 0xdeadbeefcafebabeULL;
        return self;
    }
    @end
```

然后再加一点代码，把这类对象也转储一遍：

```
    obj = [[Dummy alloc] init];
    size = malloc_size(obj);
    Dump(@"Fresh Dummy", obj, size);
    [obj release];
    Dump(@"Destroyed Dummy", obj, size);
```

这是不启用僵尸时的一次运行：

```
    Fresh Dummy malloc_size 16 - <28110000 01000000 bebafeca efbeadde>
    Destroyed Dummy malloc_size 0 - <28110000 01000000 bebafeca efbeadde>
```

和之前一样，销毁时什么都没变。注意 `secondEight` 的内容是反着的，因为这段代码运行在小端（little-endian）架构上。

这是启用僵尸时的一次运行：

```
    Fresh Dummy malloc_size 16 - <28110000 01000000 bebafeca efbeadde>
    Destroyed Dummy malloc_size 16 - <e0071100 01000000 bebafeca efbeadde>
```

对象的其余部分原封不动，但 `isa` 指针再一次被改写了。来看看这个新的 `isa` 指针到底是什么：

```
    NSLog(@"%s", class_getName(object_getClass(obj)));
```

运行之后我们知道，这个类叫 `_NSZombie_Dummy`。可以看到，僵尸的工作方式是把 `isa` 指针改写成一个特殊的僵尸类。这个特殊的僵尸类把原始类的名字并入了自身，让人一眼就能看出原始类是什么，诊断也因此简单得多。

来看看这个类里到底有什么。下面这个函数会转储一个类的各种信息：

```
    void DumpClass(Class c)
    {
        printf("Dumping class %s\n", class_getName(c));
        
        printf("Superclass: %s\n", class_getName(class_getSuperclass(c)));
        
        printf("Ivars:\n");
        Ivar *ivars = class_copyIvarList(c, NULL);
        for(Ivar *cursor = ivars; cursor && *cursor; cursor++)
            printf("    %s %s %d\n", ivar_getName(*cursor), ivar_getTypeEncoding(*cursor), (int)ivar_getOffset(*cursor));
        free(ivars);
        
        printf("Methods:\n");
        Method *methods = class_copyMethodList(c, NULL);
        for(Method *cursor = methods; cursor && *cursor; cursor++)
            fprintf(stderr, "    %s %s\n", sel_getName(method_getName(*cursor)), method_getTypeEncoding(*cursor));
        free(methods);
    }
```

现在对 `Dummy` 已销毁的实例运行它：

```
    DumpClass(object_getClass(obj));
```

输出如下：

```
    Dumping class _NSZombie_Dummy
    Superclass: nil
    Ivars:
        isa # 0
    Methods:
```

这个类基本什么都没有。除了 `isa` 实例变量（每个类都必须有）之外，什么都没有。没有超类，没有其他实例变量，没有方法。

那么，尝试向这个空类的实例发送消息会发生什么？我在销毁对象之后的代码里加了 `[obj self]`，然后在 `gdb` 里运行。结果如下：

```
    2011-05-19 14:42:39.427 a.out[62888:a0f] *** -[Dummy self]: message sent to deallocated instance 0x1001106b0
    
    Program received signal SIGTRAP, Trace/breakpoint trap.
    0x00007fff82a4d6c6 in ___forwarding___ ()
    (gdb) bt
    #0  0x00007fff82a4d6c6 in ___forwarding___ ()
    #1  0x00007fff82a49a68 in __forwarding_prep_0___ ()
    #2  0x0000000100001c49 in main (argc=1, argv=0x7fff5fbff690) at zomb.m:62
```

`___forwarding___` 这些东西是运行时的一部分，当目标对象没有实现发给它的消息时，就由它接管。它之所以叫「转发（forwarding）」，是因为[把消息转发给其他对象](http://www.mikeash.com/pyblog/friday-qa-2009-03-27-objective-c-message-forwarding.html)正是它的主要用途之一。

转发机制抛出 `SIGTRAP`，是因为这个类没有实现最起码的转发方法。不过，往日志里写「message sent to deallocated instance」（消息被发送至已销毁实例）的又是谁？我们在 `CFLog` 上放一个断点，一探究竟：

```
    Breakpoint 2, 0x00007fff82a98327 in CFLog ()
    (gdb) bt
    #0  0x00007fff82a98327 in CFLog ()
    #1  0x00007fff82a4d6c5 in ___forwarding___ ()
    #2  0x00007fff82a49a68 in __forwarding_prep_0___ ()
    #3  0x0000000100001c49 in main (argc=1, argv=0x7fff5fbff690) at zomb.m:62
    (gdb) cont
    Continuing.
    2011-05-19 15:45:03.905 a.out[62938:a0f] *** -[Dummy self]: message sent to deallocated instance 0x1001106b0
```

由此我们可以看到，运行时的转发机制在检测到僵尸类之后，会自己发出这条日志。

**结语**  
 僵尸是调试内存问题的一件利器。在表象之下，僵尸的工作方式是把对象的 `isa` 指针改写成指向一个与原始类关联的特殊僵尸类。当消息发送到这个特殊僵尸类的实例时，它会被运行时的消息转发系统拦截，后者随后记录这一事件并让 App 崩溃。

今天就到这里。两周后再来读下一篇，正好赶上 WWDC。在此期间，一如既往，请继续[把你的主题点子发给我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-05-20-the-inner-life-of-zombies.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
