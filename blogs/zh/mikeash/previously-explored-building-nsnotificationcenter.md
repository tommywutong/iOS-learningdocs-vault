---
title: 'Friday Q&A 2011-07-08：让我们构建 NSNotificationCenter'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6c11a41cc9bd4a81'
translated: true
---

> 原文：[previously explored building NSNotificationCenter](https://www.mikeash.com/pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html)　·　mikeash.com Friday Q&A

发表于 2011-07-08 16:11 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2011-07-22：编写单元测试](https://www.mikeash.com/pyblog/friday-qa-2011-07-22-writing-unit-tests.html)  
上一篇：[Friday Q&A 再次延期](https://www.mikeash.com/pyblog/friday-qa-delayed-again.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [notifications](https://www.mikeash.com/pyblog/?tag=notifications)

Friday Q&A 2011-07-08：让我们构建 NSNotificationCenter

作者：[Mike Ash](https://www.mikeash.com/)

**代码**  
我构建的代码以完整单元的形式发布在 github 上：[https://github.com/mikeash/MANotificationCenter](https://github.com/mikeash/MANotificationCenter)。虽然我不认为它对实际工作有什么用处（你还不如直接用 `NSNotificationCenter`），但把它作为整体看一看会很有意思。

**接口**  
目标基本上是把 `NSNotificationCenter` 重新实现为一个类，我叫它 `MANotificationCenter`，不过为了让事情容易一点，我决定把 API 砍掉一些。`NSNotificationCenter` 最初提供的是基于观察者（observer）/选择器（selector）对的观察 API，后来在 10.6 中增加了第二个方法，改用 block 充当观察者。既然 block 对这类工作终究自然得多，我这版 API 只保留了基于 block 的方法：

```
    - (id)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block;
```

与 `NSNotificationCenter` 一样，这个方法返回一个不透明对象（opaque object），调用方应当用它来移除观察者：

```
    - (void)removeObserver: (id)observer;
```

较旧的对象/选择器 API 可以基于这一个来实现，所以只提供这一个并不会损失任何功能。幕后工作方式的基本思路也本质上相同，唯一的区别是到了通知观察者的时刻，你是调用一个 block，还是向一个对象发送选择器。

最后，我们还需要能发布一条通知：

```
    - (void)postNotification: (NSNotification *)note;
```

`NSNotificationCenter` 还有其他几个直接接受对象和名称的发布方法，但那些只是构造出 `NSNotification` 对象再转发到这里，所以同样，少掉那些方法我们毫无损失。它们其实只是这个方法的一行式包装。

API 就这么多了。相当简单。有意思的是，`NSNotificationCenter` 本身也没有复杂多少。它只有七个实例方法，其中两个还只是便利性包装。

**实现**  
在进入真正的 _代码_ 之前，先讲点理论。

一条通知由三样东西定义：发布通知的对象、通知的名称，以及附着在通知上的任意用户信息（user info）。对象和名称用来决定哪些观察者需要被通知。

最后这一点是关键。本质上，通知中心把 `object, name` 对映射到观察者。这里由于 `MANotificationCenter` 是基于 block 的，它会把这样的对映射到观察者 block。同一个 `object, name` 对上可以注册多个观察者，所以它们需要映射到一个能容纳多个观察者 block 的集合。

用 Cocoa 的词汇来说，我们讲"映射"（map）时，通常指的就是字典。遗憾的是，用"对"做字典键有点不方便，因为 `NSDictionary` 只接受单个对象作为键。为了化解这一点，我们会创建一个独立的"键"类，它持有这一对值，可以整体作为一个对象充当字典键。至于观察者 block 的集合，我们不关心顺序，直接用 `NSMutableSet` 就行。

因此，这个类会有一个主 `NSMutableDictionary`，把键映射到各个 `NSMutableSet` 实例，集合里装的才是单个的观察者 block。事情的全部就是这样。

**键类**  
键类相当简单，但还是值得讲讲它的工作方式，好让大家的理解一致。它只是个小类，持有一个名字和一个对象，并恰当地实现相等性、哈希与拷贝。有个小细节：对象引用必须是弱引用（weak reference），因为通知系统不应保留它所管理的对象（这些对象常常会在自己被释放时顺势注销观察，如果通知系统保留它们就会出问题）。

顺带一提，我经常警告普通弱引用的危险，并建议改用零值弱引用（zeroing weak reference）类，比如我自己的 [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef/)。不过为了简短清晰，这段代码里我将使用普通、危险、常规的弱引用。

这个类的接口很简单：两个实例变量，外加一个公开的类方法用于创建实例：

```
    @interface _MANotificationCenterDictionaryKey : NSObject
    {
        NSString *_name;
        id _object;
    }

    + (_MANotificationCenterDictionaryKey *)keyForName: (NSString *)name object: (id)obj;

    @end
```

那个公开方法走的只是 `alloc`、`init`、`autorelease` 的典型流程，内部借助一个私有的 `init` 方法：

```
    + (_MANotificationCenterDictionaryKey *)keyForName: (NSString *)name object: (id)obj
    {
        return [[[self alloc] _initWithName: name object: obj] autorelease];
    }
```

`init` 和 `dealloc` 方法同样简单，只是设置和清理实例变量：

```
    - (id)_initWithName: (NSString *)name object: (id)obj
    {
        if((self = [self init]))
        {
            _name = [name copy];
            _object = obj;
        }
        return self;
    }

    - (void)dealloc
    {
        [_name release];
        [super dealloc];
    }
```

接下来是相等性。我希望这个类能处理名称或对象为 `nil` 的情况（或两者都为 `nil`），因为稍后实现 `nil` 通配观察者时正好用得上：观察者可以注册 `nil` 名称，表示"来自给定对象的所有通知"；注册 `nil` 对象，表示"带给定名称的所有通知"；两者都注册 `nil`，则捕获流经系统的全部通知。然而，通知名称需要用 `isEqual:` 比较，而它与 `nil` 合不来。为了让事情简单些，我写了一个非常快的相等性检查辅助函数，它能正确处理 `nil`，只在两个对象都存在时才使用 `isEqual:`：

```
    static BOOL Equal(id a, id b)
    {
        if(!a && !b)
            return YES;
        else if(!a || !b)
            return NO;
        else
            return [a isEqual: b];
    }
```

有了这个辅助函数，`isEqual:` 的实现就简单了，遵循"先检查对方所属的类，再比较实例变量"的标准模式：

```
    - (BOOL)isEqual: (id)other
    {
        if(![other isKindOfClass: [_MANotificationCenterDictionaryKey class]])
            return NO;

        _MANotificationCenterDictionaryKey *otherKey = other;
        return Equal(_name, otherKey->_name) && _object == otherKey->_object;
    }
```

`hash` 的实现只是取两个实例变量的哈希，再把它们捏合到一起：

```
    - (NSUInteger)hash
    {
        return [_name hash] ^ (uintptr_t)_object;
    }
```

最后，要当字典键，还需要 `copyWithZone:`。由于这个类不可变，该方法直接保留 `self` 并返回即可：

```
    - (id)copyWithZone: (NSZone *)zone
    {
        return [self retain];
    }
```

键的部分到此为止。接下来说通知中心本身。

**通知中心的实现**  
`init` 和 `dealloc` 的实现很短。这里有一个 `NSMutableDictionary *_map` 实例变量，两个方法只是搭建和拆除它：

```
    - (id)init
    {
        if((self = [super init]))
        {
            _map = [[NSMutableDictionary alloc] init];
        }
        return self;
    }

    - (void)dealloc
    {
        [_map release];
        [super dealloc];
    }
```

接下来是 `-addObserverForName:object:block:` 的实现，大部分工作都发生在这里。它要做的第一件事是拿到一个键对象，好用它去操作观察者字典：

```
    - (id)addObserverForName: (NSString *)name object: (id)object block: (void (^)(NSNotification *note))block
    {
        _MANotificationCenterDictionaryKey *key = [_MANotificationCenterDictionaryKey keyForName: name object: object];
```

接着，它要取到该键对应的 `NSMutableSet` 观察者集合。这是一次直截了当的 `objectForKey:` 查找，唯一的变数是观察者集合可能还不存在。若真如此，就按需创建并放进观察者字典：

```
        NSMutableSet *observerBlocks = [_map objectForKey: key];
        if(!observerBlocks)
        {
            observerBlocks = [NSMutableSet set];
            [_map setObject: observerBlocks forKey: key];
        }
```

然后，把观察 block 塞进集合。由于 `NSMutableSet` 只会保留它的对象，而 block 若要留存就_必须_被拷贝，我们亲手先拷贝一份再交给集合：

```
        void (^copiedBlock)(NSNotification *note);
        copiedBlock = [block copy];

        [observerBlocks addObject: copiedBlock];

        [copiedBlock release];
```

差不多就是这样。现在观察者字典里的一切都已就位，`-postNotification:` 可以开工了。这个方法只缺一样东西：返回值。它应当返回某种对象，把它传给 `-removeObserver:` 时，就能移除这条观察记录。

这种对象通常要封装好重新找到并移除该条目所需的一切。在这个具体场景里，它需要持有键和拷贝出来的 block。这两个对象可以塞进某个 Cocoa 集合，比如 `NSArray` 或 `NSDictionary`，但那样在构造对象、再从中取值的整个过程中会有大量令人不快的装箱与拆箱操作。也可以存进一个自定义类，可为了这么个小用例专门多写一个类，实在恼人。

想了想之后，我决定返回一个 block。移除观察记录所需的全部信息在当前作用域里都拿得到，block 可以把它们统统捕获。附带的好处是，我们可以捕获现成的 `observerBlocks` 变量，这样集合不必再查第二遍。`-removeObserver:` 到时只需调用这个 block，一切圆满。我决定采用这个方案，而且我觉得效果相当不错。

移除 block 先把 block 从观察者集合里拉出来：

```
        void (^removalBlock)(void) = ^{
            [observerBlocks removeObject: copiedBlock];
```

接着，如果观察者集合已空，就把那个条目从观察者字典里整个移除。这可以避免对象销毁之后，字典里堆积一个个空的 `NSMutableSet` 实例：

```
            if([observerBlocks count] == 0)
                [_map removeObjectForKey: key];
        };
```

移除 block 到此完工。剩下的只是把它返回给调用方，就大功告成：

```
        return [[removalBlock copy] autorelease];
    }
```

有了这个实现，`-removeObserver:` 方法变得非常短。它只是把对象转换成正确的 block 类型，然后调用它：

```
    - (void)removeObserver: (id)observer
    {
        void (^removalBlock)(void) = observer;
        removalBlock();
    }
```

接下来是一个真正负责发送通知的辅助方法。它独立于 `-postNotification:` 存在，为的是能正确处理 `nil` 通配观察。这个稍后细说。该方法接受一条通知、一个名称和一个对象（是的，这些都存在通知里，但再说一遍，这对通配处理有帮助），在主字典里查找观察者集合，然后调用其中所有对应的 block：

```
    - (void)_postNotification: (NSNotification *)note name: (NSString *)name object: (id)object
    {
        _MANotificationCenterDictionaryKey *key = [_MANotificationCenterDictionaryKey keyForName: name object: object];
        NSSet *observerBlocks = [_map objectForKey: key];
        for(void (^block)(NSNotification *) in observerBlocks)
            block(note);
    }
```

最后是 `-postNotification:`。简单的实现是直接调用上面的方法，把 `[note name]` 和 `[note object]` 作为后两个参数传入。然而，为了照顾通配观察者，我们实际上要把上面的方法连续调用四次。第一次带着名称和对象调用。第二次只带名称，对象传 `nil`——这会通知到注册了该名称的通配观察者。第三次名称传 `nil`、带通知的对象——这会通知到针对该对象的通配观察者。最后两个参数都传 `nil`，这会通知到全局通配观察者。

方法长这样：

```
    - (void)postNotification: (NSNotification *)note
    {
        NSString *name = [note name];
        id object = [note object];

        [self _postNotification: note name: name object: object];
        [self _postNotification: note name: name object: nil];
        [self _postNotification: note name: nil object: object];
        [self _postNotification: note name: nil object: nil];
    }
```

让 `-addObserverForName:object:block:` 接受 `nil` 之后，实现通配行为几乎不需要再做别的。`nil` 的对象或名称被当作与任何其他键差不多的东西对待，只不过通知除了发给它们针对的具体对象之外，也会发给 `nil`。

**几点告诫**  
这份代码以教学为主要目的，还不太具备一个真实、实用实现该有的所有东西。

首先，它没有办法获取单例实例。这对通知来说真的很重要，因为通知的全部意义往往就在于让彼此并不怎么了解的对象之间通信，而如果还得到处传递通知中心实例，这个意义就差不多没了。当然，把它加上非常简单。

其次，它不是线程安全的。添加和移除观察者会修改共享的数据结构，那些结构需要用锁保护。把线程安全做出来可能相当复杂：最简单的实现会在发布通知时握着锁，但通知观察者这时可能反过来要捣鼓通知中心，造成死锁。更好的办法也许是使用 dispatch queue，把所有修改操作排进队列，等通知中心空闲时再执行。

最后，它也不可重入。如果某个通知观察者操纵了通知中心，最终可能修改到中心正在迭代的那个 `observerBlocks` 集合，抛出变更异常。它甚至可能让集合被整体释放，直接崩溃。某种存放修改操作的队列——dispatch queue 也好，别的什么也好——能解决这个问题。另一个慢一点的办法，是在迭代之前简单地把 `observerBlocks` 拷贝一份，这样修改就碰不到被迭代的那份了。

**结语**  
亲手实现一个能跑的 `NSNotificationCenter` 之类的东西，能让我们更清楚地看到它内部到底在干什么。最重要的是，它说明了内部毫无魔法。通知并不是什么难以理解的特殊语言特性，它其实只是一个简单的分发机制，一个基础实现一百行左右代码就能装下。

关于通知的一个常见疑问是：它到底在何时、何地执行。很多人一看到"通知"两个字，就开始联想到复杂的跨线程通信或者延迟投递机制。但我们已经看到，事情根本不是那样运作的。`-postNotification:` 被调用时，各个观察者就在这个方法里被挨个调用，等它们全部执行完它才返回。（注意：这不适用于 `NSNotificationCenter` 里那个同时接受 block 和 `NSOperationQueue` 的方法。为那个方法提供队列时，观察 block 会异步执行。）

本周就到这里。欢迎回来阅读下一期内容充实、主题大胆而不落俗套的 Friday Q&A。一如既往，这些主题来自读者的建议，如果你有想在这里看到的主题，请[发给我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-07-08-lets-build-nsnotificationcenter.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
