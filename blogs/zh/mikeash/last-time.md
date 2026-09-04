---
title: 'Friday Q&A 2013-01-25：让我们构建 NSObject'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af9fac8d2731cb8f'
translated: true
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)　·　mikeash.com Friday Q&A

发表于 2013-01-25 15:32 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2013-02-08：让我们构建键值编码](https://www.mikeash.com/pyblog/friday-qa-2013-02-08-lets-build-key-value-coding.html)  
上一篇：[Friday Q&A 2013-01-11：Mach 异常处理器](https://www.mikeash.com/pyblog/friday-qa-2013-01-11-mach-exception-handlers.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-01-25：让我们构建 NSObject

作者：[Mike Ash](https://www.mikeash.com/)

**根类的组成部分**  
根类究竟要做什么？就 Objective-C 语言本身而言，要求只有一条：根类的第一个实例变量必须是 `isa`，它是一个指向对象所属类的指针。分发消息时，`isa` 用来判断一个对象是什么类。从严格的语言角度看，必须做的就这么多。

当然，一个只提供这些的根类不会有多大用处。`NSObject` 提供的东西多得多，其功能可以分为三类：

1. **内存管理：** `retain`、`release` 这类标准内存管理方法都在 `NSObject` 中实现，`alloc` 方法也在那里实现。
2. **内省（introspection）：** `NSObject` 提供了一堆本质上是对 Objective-C 运行时功能做包装的方法，比如 `class`、`respondsToSelector:` 和 `isKindOfClass:`。
3. **杂项方法的默认实现：** 有一批方法是我们指望每个对象都实现的，比如 `isEqual:` 和 `description`。为了确保每个对象都有实现，`NSObject` 提供了默认实现，任何子类如果不自己实现，就会继承这一份。

**代码**  
我将以 `MAObject` 为名重新实现 `NSObject` 的功能。本文的完整代码发布在 GitHub 上：

[https://github.com/mikeash/MAObject](https://github.com/mikeash/MAObject)

注意，这份代码是在没有 ARC 的情况下构建的。ARC 虽好，应当尽量使用，但在实现根类时它真的碍事：根类需要亲自实现内存管理，而 ARC 更倾向于让你把内存管理留给编译器。

**实例变量**  
`MAObject` 有两个实例变量。第一个是 `isa` 指针，第二个是对象的引用计数（reference count）：

```
    @implementation MAObject {
        Class isa;
        volatile int32_t retainCount;
    }
```

引用计数将用 `OSAtomic.h` 里的函数来管理以保证线程安全，这就是它的定义有点不寻常、而不是直接用 `NSUInteger` 之类的原因。

`NSObject` 实际上是把引用计数放在外部的。它有一张全局表，把对象的地址映射到引用计数。这样能省内存，因为引用计数为常见的 `1` 时，表里干脆没有条目。不过这个技巧既复杂又有点慢，所以我自己这版没有采用。

**内存管理**  
`MAObject` 需要能做的第一件事是创建实例。这通过实现 `+alloc` 方法完成。（我跳过了已废弃且很少用到的 `+allocWithZone:`，如今它做的事一样，反正也会忽略自己的参数。）

子类很少重写 `+alloc`，而是依赖根类为它们分配内存。这意味着 `MAObject` 不仅要能分配 `MAObject` 自己的实例，还要能分配任何子类的实例。这利用了这样一个事实：类方法里 `self` 的值就是消息实际发送到的那个类。如果代码执行 `[SomeSubclass alloc]`，`self` 持有的就是指向 `SomeSubclass` 的指针。随后可以用这个类去查询运行时，弄清该分配多少内存，并把 `isa` 指针设置正确。引用计数也按新分配对象的惯例初始化为 `1`：

```
    + (id)alloc
    {
        MAObject *obj = calloc(1, class_getInstanceSize(self));
        obj->isa = self;
        obj->retainCount = 1;
        return obj;
    }
```

`retain` 方法只用 `OSAtomicIncrement32` 把引用计数加一，然后返回 `self`：

```
    - (id)retain
    {
        OSAtomicIncrement32(&retainCount);
        return self;
    }
```

release 方法做的事情多一些。它先把引用计数减一。如果引用计数被减到了 `0`，对象就需要销毁，于是代码调用 `dealloc`：

```
    - (oneway void)release
    {
        uint32_t newCount = OSAtomicDecrement32(&retainCount);
        if(newCount == 0)
            [self dealloc];
    }
```

`autorelease` 的实现调用 `NSAutoreleasePool`，把 `self` 加进当前的自动释放池（autorelease pool）。自动释放池如今已是运行时的一部分，所以这是一条颇为迂回的路径，但运行时里的 autorelease API 是私有的，目前我们也只能做到这一步：

```
    - (id)autorelease
    {
        [NSAutoreleasePool addObject: self];
        return self;
    }
```

`retainCount` 方法只是把实例变量里存的值返回：

```
    - (NSUInteger)retainCount
    {
        return retainCount;
    }
```

最后是 `dealloc` 方法。在普通类里，`dealloc` 需要清理各个实例变量，然后调用 `super`。而根类必须真正处置对象本身占用的内存。这里就只是简单地调用 `free`：

```
    - (void)dealloc
    {
        free(self);
    }
```

还有几个辅助方法。`NSObject` 为了一致性提供一个什么都不做的 `init` 方法，让子类永远可以放心调用 `[super init]`：

```
    - (id)init
    {
        return self;
    }
```

还有一个 `new` 方法，它只是 `alloc` 和 `init` 的包装：

```
    + (id)new
    {
        return [[self alloc] init];
    }
```

另有一个空的 `finalize` 方法。`NSObject` 实现它是为了支持垃圾回收（garbage collection）。`MAObject` 本来就不支持垃圾回收，但既然 `NSObject` 有，我也把它带上：

```
    - (void)finalize
    {
    }
```

**内省**  
许多内省方法只是对运行时函数的包装。这不太有意思，所以我顺带简单讲讲这些运行时函数在幕后做了什么。

最简单的内省方法是 `class`，它只返回 `isa` 的值：

```
    - (Class)class
    {
        return isa;
    }
```

严格来说，这个方法在 tagged pointer 上会出问题。严谨的实现应当调用 `object_getClass`，它对 tagged pointer 表现正确，而对普通指针则提取 `isa`。

`superclass` 实例方法等价于对对象的类调用 `superclass` 类方法，所以该方法正是这么做的：

```
    - (Class)superclass
    {
        return [[self class] superclass];
    }
```

这些也都有对应的类方法。`+class` 方法只返回 `self`，也就是类对象。这有点怪，但 `NSObject` 就是这么做的。`[obj class]` 返回对象的类，而 `[MyClass class]` 只返回指向 `MyClass` 自身的指针。这并不一致——`MyClass` 也有自己的类，即 `MyClass` 的元类（metaclass）——但事情就是这么办的：

```
    + (Class)class
    {
        return self;
    }
```

`+superclass` 方法名副其实。它通过调用 `class_getSuperclass` 实现，后者只是在运行时维护的类结构里翻找，把指向超类的指针掏出来。

```
    + (Class)superclass
    {
        return class_getSuperclass(self);
    }
```

还有查询对象的类是否匹配某个特定类的方法。简单的是 `isMemberOfClass:`，它做严格比较，不考虑子类。实现很直接：

```
    - (BOOL)isMemberOfClass: (Class)aClass
    {
        return isa == aClass;
    }
```

`isKindOfClass:` 方法还会检查子类，因此 `[subclassInstance isKindOfClass: [Superclass class]]` 返回 `YES`。这个方法的结果与类方法 `isSubclassOfClass:` 基本相同，所以它直接转发调用：

```
    - (BOOL)isKindOfClass: (Class)aClass
    {
        return [isa isSubclassOfClass: aClass];
    }
```

那个方法更有意思一点。它从 `self` 出发沿类层次向上走，每一层都与目标类比较。找到匹配就返回 `YES`；如果一路走到类层次的顶端都没有匹配，就返回 `NO`：

```
    + (BOOL)isSubclassOfClass: (Class)aClass
    {
        for(Class candidate = self; candidate != nil; candidate = [candidate superclass])
            if (candidate == aClass)
                return YES;

        return NO;
    }
```

值得注意的是，这个检查并不特别高效。对一个身处类层次深处的类调用它，可能要经过很多轮循环才会返回 `NO`。正因如此，`isKindOfClass:` 检查可能比消息发送慢得多，在某些情况下甚至会实打实地成为瓶颈。这也是"能不用就不用"的又一个理由。

`respondsToSelector:` 方法直接转发调用运行时函数 `class_respondsToSelector`。后者在类的方法表里查找该选择器（selector），看有没有对应条目：

```
    - (BOOL)respondsToSelector: (SEL)aSelector
    {
        return class_respondsToSelector(isa, aSelector);
    }
```

还有一个类方法 `instancesRespondToSelector:`，几乎一样。唯一的区别是传的是 `self`——在这个语境下是类本身——而不是 `isa`，后者在这里会是元类：

```
    + (BOOL)instancesRespondToSelector: (SEL)aSelector
    {
        return class_respondsToSelector(self, aSelector);
    }
```

还有两个 `conformsToProtocol:` 方法，一个面向实例，一个面向类。它们同样只是包装运行时函数——这个函数会查一张表，里面列着该类遵循的每一个协议，看看给定的协议在不在：

```
    - (BOOL)conformsToProtocol: (Protocol *)aProtocol
    {
        return class_conformsToProtocol(isa, aProtocol);
    }

    + (BOOL)conformsToProtocol: (Protocol *)protocol
    {
        return class_conformsToProtocol(self, protocol);
    }
```

接下来是 `methodForSelector:`，以及它的类方法版兄弟 `instanceMethodForSelector:`。两者都转发调用 `class_getMethodImplementation`，它在类的方法表中查找选择器并返回对应的 `IMP`：

```
    - (IMP)methodForSelector: (SEL)aSelector
    {
        return class_getMethodImplementation(isa, aSelector);
    }

    + (IMP)instanceMethodForSelector: (SEL)aSelector
    {
        return class_getMethodImplementation(self, aSelector);
    }
```

这些方法有个有趣的点：`class_getMethodImplementation` 总是返回一个 `IMP`，哪怕选择器是未知的。类没有真正实现某个方法时，它返回一个特殊的转发 IMP，把消息参数打包起来，走上调用 `forwardInvocation:` 的路径。

`methodSignatureForSelector:` 方法只是包装对应的类方法：

```
    - (NSMethodSignature *)methodSignatureForSelector: (SEL)aSelector
    {
        return [isa instanceMethodSignatureForSelector: aSelector];
    }
```

那个类方法又包装了几次运行时调用。它先取得给定选择器的 `Method`。找不到就说明类没有实现该方法，返回 `nil`。否则，取出表示方法类型的 C 字符串，包进一个 `NSMethodSignature` 对象：

```
    + (NSMethodSignature *)instanceMethodSignatureForSelector: (SEL)aSelector
    {
        Method method = class_getInstanceMethod(self, aSelector);
        if(!method)
            return nil;

        const char *types = method_getTypeEncoding(method);
        return [NSMethodSignature signatureWithObjCTypes: types];
    }
```

最后是 `performSelector:`，以及接受参数的两个 `withObject:` 变体。它们严格说不算内省，但同属"包装更底层运行时功能"这个大类。它们只是取出给定选择器的 `IMP`，转换成相应的函数指针类型，然后调用：

```
    - (id)performSelector: (SEL)aSelector
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL))imp)(self, aSelector);
    }

    - (id)performSelector: (SEL)aSelector withObject: (id)object
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL, id))imp)(self, aSelector, object);
    }

    - (id)performSelector: (SEL)aSelector withObject: (id)object1 withObject: (id)object2
    {
        IMP imp = [self methodForSelector: aSelector];
        return ((id (*)(id, SEL, id, id))imp)(self, aSelector, object1, object2);
    }
```

**默认实现**  
`MAObject` 为一批方法提供默认实现。先从 `isEqual:` 和 `hash` 的默认实现开始，它们只用对象的指针来判定同一性：

```
    - (BOOL)isEqual: (id)object
    {
        return self == object;
    }

    - (NSUInteger)hash
    {
        return (NSUInteger)self;
    }
```

对"相等"有更宽泛定义的子类需要重写这两个方法；而对象只可能等于自身的子类，直接用这套实现就行。

`description` 方法是另一个值得有默认实现的方法。这个实现只是生成一个形如 `<MAObject: 0xdeadbeef>` 的字符串，包含对象的类和指针值。

```
    - (NSString *)description
    {
        return [NSString stringWithFormat: @"<%@: %p>", [self class], self];
    }
```

类的惯例是在自己的 `description` 里只返回类名，所以还有一个类方法，从运行时取到这个名字并返回：

```
    + (NSString *)description
    {
        return [NSString stringWithUTF8String: class_getName(self)];
    }
```

`doesNotRecognizeSelector:` 是一个不太出名的工具方法。它抛出一个异常，制造出对象其实并不响应该选择器的假象。适合用来构造"子类必须实现某个方法"这类重写点（override point）：

```
    - (void)subclassesMustOverride
    {
        // 假装我们这里并没有实现这个方法
        [self doesNotRecognizeSelector: _cmd];
    }
```

代码相当简单。唯一真正棘手的是格式化方法名。我们想显示成 `-[Class method]` 的样子，但类方法前面需要 `+`，比如 `+[Class classMethod]`。为判断当前所处的语境，代码检查 `isa` 是不是元类。是，则 `self` 是个类，应当用 `+` 变体；否则 `self` 是实例，用 `-` 变体。剩下的代码只是抛出相应的 `NSException`：

```
    - (void)doesNotRecognizeSelector: (SEL)aSelector
    {
        char *methodTypeString = class_isMetaClass(isa) ? "+" : "-";
        [NSException raise: NSInvalidArgumentException format: @"%s[%@ %@]: unrecognized selector sent to instance %p", methodTypeString, [[self class] description], NSStringFromSelector(aSelector), self];
    }
```

最后还有一堆小方法：要么对显而易见的问题给出显而易见的答案（比如 `self` 方法），要么为了让子类总能安全调用 `super` 而存在（比如空的 `+initialize` 方法），要么就是重写点（比如抛出异常的 `copy` 实现）。这些都不太有意思，但为了完整性一并附上：

```
    - (id)self
    {
        return self;
    }

    - (BOOL)isProxy
    {
        return NO;
    }

    + (void)load
    {
    }

    + (void)initialize
    {
    }

    - (id)copy
    {
        [self doesNotRecognizeSelector: _cmd];
        return nil;
    }

    - (id)mutableCopy
    {
        [self doesNotRecognizeSelector: _cmd];
        return nil;
    }

    - (id)forwardingTargetForSelector: (SEL)aSelector
    {
        return nil;
    }

    - (void)forwardInvocation: (NSInvocation *)anInvocation
    {
        [self doesNotRecognizeSelector: [anInvocation selector]];
    }

    + (BOOL)resolveClassMethod:(SEL)sel
    {
        return NO;
    }

    + (BOOL)resolveInstanceMethod:(SEL)sel
    {
        return NO;
    }
```

**结语**  
`NSObject` 是一大包不同功能的集合体，但没什么太奇怪的东西。它的主要职责是处理内存的分配与管理，让你真能创建出对象；它还为每个对象都该支持的方法提供了一堆顺手的重写点，并把一批运行时函数包装成更友好的 API。

`NSObject` 提供的一大块功能我跳过了：键值编码。它复杂到值得单独写一篇文章，改天再回来讲它。

今天就到这里。Friday Q&A 由读者的点子驱动——万一你竟然还不知道的话——请[把你的主题建议发给我](mailto:mike@mikeash.com)。下次见，别写出连我都不会写的代码。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-01-25-lets-build-nsobject.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
