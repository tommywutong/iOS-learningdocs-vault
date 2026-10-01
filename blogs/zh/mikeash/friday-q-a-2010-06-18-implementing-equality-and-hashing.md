---
title: 'Friday Q&A 2010-06-18：实现相等性与哈希'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d146eb094026bbce'
translated: true
---

> 原文：[Friday Q&A 2010-06-18: Implementing Equality and Hashing](https://www.mikeash.com/pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)　·　mikeash.com Friday Q&A

发表于 2010-06-18 14:48 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[俄语版 Blocks 与 GCD](https://www.mikeash.com/pyblog/blocks-and-gcd-in-russian.html)  
上一篇：[Friday Q&A 2010-05-28：Leopard 集合类](https://www.mikeash.com/pyblog/friday-qa-2010-05-28-leopard-collection-classes.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hash](https://www.mikeash.com/pyblog/?tag=hash) [isequal](https://www.mikeash.com/pyblog/?tag=isequal) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-06-18：实现相等性与哈希

作者：[Mike Ash](https://www.mikeash.com/)

**相等性（equality）**  
对象相等性是一个到处都会用到的基本概念。在 Cocoa 中，它通过 `isEqual:` 方法来实现。像 `[array indexOfObject:]` 这样简单的操作都会用到它，所以让你的对象支持它非常重要。

它重要到 Cocoa 干脆在 `NSObject` 上为我们提供了默认实现。默认实现只是比较指针。换句话说，一个对象只等于它自身，永远不等于另一个对象。该实现在功能上等价于：

```
    - (BOOL)isEqual: (id)other
    {
        return self == other;
    }
```

虽然在很多情况下这过于简化，但对大量对象来说这其实已经足够。例如，一个 `NSView` 永远不会被看作等于另一个 `NSView`，只会等于它自己。对 `NSView` 以及许多行为类似的类来说，默认实现就够用了。这是好消息：这意味着如果你的类恰好也是这种相等性语义，你什么都不用做，就能白白得到正确的行为。

**实现自定义相等性**  
有时你需要更深入的相等性实现。对象很常见的一种情况是：它和另一个对象是两个不同的对象，但在逻辑上与后者相等——这种对象通常就是你所说的「值对象」（value object）。例如：

```
    // 使用可变字符串，因为这样能保证是不同的对象
    NSMutableString *s1 = [NSMutableString stringWithString: @"Hello, world"];
    NSMutableString *s2 = [NSMutableString stringWithFormat: @"%@, %@", @"Hello", @"world"];
    BOOL equal = [s1 isEqual: s2]; // 会得到 YES！
```

当然，这种情况下 `NSMutableString` 已经替你实现了。可如果你有一个自定义对象，也想让它能做到同样的事呢？

```
    MyClass *c1 = ...;
    MyClass *c2 = ...;
    BOOL equal = [c1 isEqual: c2];
```

这时你就需要实现自己的 `isEqual:` 版本。

多数时候，测试相等性相当直接。收集你的类里相关的属性，对它们逐一测试相等性。只要有任何一个不相等，就返回 `NO`；否则返回 `YES`。

这其中有一个微妙之处：你对象所属的类本身也是一个需要测试的重要属性。拿一个 `MyClass` 和一个 `NSString` 比较相等性是完全合法的，但这种比较永远不应返回 `YES`（当然，除非 `MyClass` 是 `NSString` 的子类）。

一个不那么微妙的要点是：只测试那些真正影响相等性的属性。像缓存这类不影响对象外部可见的值的东西，不应参与测试。

假设你的类是这样的：

```
    @interface MyClass : NSObject
    {
        int _length;
        char *_data;
        NSString *_name;
        NSMutableDictionary *_cache;
    }
```

你的相等性实现于是会是这个样子：

```
    - (BOOL)isEqual: (id)other
    {
        return ([other isKindOfClass: [MyClass class]] &&
                [other length] == _length &&
                memcmp([other data], _data, _length) == 0 &&
                [[other name] isEqual: _name])
                // 注意：不比较 _cache
    }
```

**哈希（hash）**  
哈希表（hash table）是一种常用的数据结构，`NSDictionary` 和 `NSSet` 等等都用它来实现。无论你往容器里放多少对象，它都能实现快速查找。

如果你已经熟悉哈希表的工作原理，可以跳过下面的一两段。

哈希表基本上就是一个带特殊索引的大数组。对象按照与其哈希相对应的索引放进数组。哈希本质上是一个由对象属性生成的伪随机数。思路是让索引足够随机，使两个对象不太可能拥有相同的哈希，同时又完全可复现。插入对象时，用哈希来决定它该放到哪里；查找对象时，用它的哈希来决定该去哪里找。

用更正式的话说，对象哈希的定义是：只要两个对象相等，它们就拥有相同的哈希。注意反过来并不成立，而且也不可能成立：两个对象可以哈希相同却不相等。你要尽量避开这种情况，因为当两个不相等的对象拥有相同的哈希时（即发生所谓的_碰撞_（collision）），哈希表就必须采取特殊措施来处理，而那样做很慢。不过，可以证明碰撞不可能被完全避免。

在 Cocoa 中，哈希通过 `hash` 方法实现，它有这样一个签名：

```
    - (NSUInteger)hash;
```

和相等性一样，`NSObject` 也为你提供了一个默认实现，它只使用对象的同一性（identity）。大致来说，它相当于：

```
    - (NSUInteger)hash
    {
        return (NSUInteger)self;
    }
```

实际的值可能有所不同，但关键在于：它基于 `self` 的实际指针值。而且和相等性一样，如果你需要的只是「对象同一性」意义上的相等，默认实现就够你用了。

**实现自定义哈希**  
由于 `hash` 的语义，如果你重写了 `isEqual:`，就_必须_重写 `hash`。不这么做的话，就可能出现两个对象相等、哈希却不同的情形。如果你把这样的对象放进字典、集合或者其他任何使用哈希表的东西里，那么好戏就要上演了。

由于对象哈希的定义与相等性贴得如此之近，`hash` 的实现也同样紧贴着 `isEqual:` 的实现。

这方面有一个例外：`hash` 的定义里不需要包含对象所属的类。那基本上是 `isEqual:` 里的一道保险，确保在跟不同的对象比较时，其余的检查还有意义。而你的哈希很可能与另一个类的哈希截然不同——单凭你在对不同的属性做哈希、并使用不同的数学方法来组合它们，就足以如此。

**生成属性哈希**  
对属性做相等性测试通常很直接，但对它们做哈希却不一定。如何哈希一个属性，取决于它是哪一种对象。

对数值属性来说，哈希可以直接就是这个数值。

对对象属性来说，你可以向该对象发送 `hash` 消息，然后用它返回的值。

对数据型属性（data-like properties）来说，你需要用某种哈希算法来生成哈希。可以用 CRC32，甚至可以用 MD5 这种完全杀鸡用牛刀的东西。还有一种做法稍微慢一点但很好用：把数据包进一个 `NSData`，向它要哈希，本质上是把活儿外包给 Cocoa。在上面的例子里，你可以这样计算 `_data` 的哈希：

```
    [[NSData dataWithBytes: _data length: _length] hash]
```

**组合属性哈希**  
现在你知道怎么给每个属性生成哈希了，可怎么把它们合到一起呢？

最简单的办法是把它们直接相加，或者利用按位异或（bitwise xor）的性质。然而这会损害哈希的唯一性，因为这些运算是对称的，不同属性之间的区分信息会丢失。举个例子，考虑一个包含名和姓的对象，哈希实现如下：

```
    - (NSUInteger)hash
    {
        return [_firstName hash] ^ [_lastName hash];
    }
```

现在想象你有两个对象，一个表示「George Frederick」，另一个表示「Frederick George」。尽管它们明显不相等，哈希出的值却会相同。而且，虽然哈希碰撞不可能完全避免，我们也应该设法让碰撞比这更难出现！

怎样最好地组合哈希是个复杂的课题，没有唯一答案。不过，任何不对称的数值组合方式都是好的开端。我喜欢在异或之外再用一个按位旋转（bitwise rotation）来组合它们：

```
    #define NSUINT_BIT (CHAR_BIT * sizeof(NSUInteger))
    #define NSUINTROTATE(val, howmuch) ((((NSUInteger)val) << howmuch) | (((NSUInteger)val) >> (NSUINT_BIT - howmuch)))
    
    - (NSUInteger)hash
    {
        return NSUINTROTATE([_firstName hash], NSUINT_BIT / 2) ^ [_lastName hash];
    }
```

**自定义哈希示例**  
现在我们可以把上面的所有内容都用上，为示例类产出一个 `hash` 方法。它遵循相等性方法的基本形式，并用上面的技巧来获取、组合各个属性的哈希：

```
    - (NSUInteger)hash
    {
        NSUInteger dataHash = [[NSData dataWithBytes: _data length: _length] hash];
        return NSUINTROTATE(dataHash, NSUINT_BIT / 2) ^ [_name hash];
    }
```

如果你有更多属性，可以加入更多旋转和更多异或运算符，效果照样成立。你会想为每个属性调整不同的旋转量，让每一项都有所区别。

**关于派生子类的注意事项**  
派生一个实现了自定义相等性和哈希的类时，你必须小心。特别要注意的是：你的子类不应暴露任何相等性所依赖的新属性。如果暴露了，那么它就不得与超类的任何实例比较为相等。

要弄明白为什么，考虑给前面的名/姓类派生一个子类，它增加了一个生日，并把生日纳入自己的相等性计算。不过，与超类的实例比较相等性时它又不能把生日算进去，所以它的相等性方法会是这样：

```
    - (BOOL)isEqual: (id)other
    {
        // 如果超类那边不认，那我们就不相等
        if(![super isEqual: other])
            return NO;
        
        // 如果它不是子类的实例，就相信超类的判断
        // 超类那边相等，那我们这边也认为相等
        if(![other isKindOfClass: [MySubClass class]])
            return YES;
        
        // 它是子类的实例，超类的属性都已经相等
        // 所以再检查子类新增的属性
        return [[other birthday] isEqual: _birthday];
    }
```

现在有一个表示「John Smith」的超类实例，我把它叫作 `A`；还有一个表示「John Smith」、生日为 1982 年 5 月 31 日的子类实例，我把它叫作 `B`。按照上面的相等性定义，`A` 等于 `B`，`B` 也等于它自己，符合预期。

再考虑一个表示「John Smith」、生日为 1994 年 6 月 7 日的子类实例，我把它叫作 `C`。`C` 不等于 `B`，这正是我们预期的。`C` 等于 `A`，同样在预期之内。但问题来了：`A` 既等于 `B` 又等于 `C`，可 `B` 和 `C` 却互不相等！这破坏了相等性运算符标准的传递性（transitivity），会导致极其出乎意料的结果。

一般来说，这不该是什么大问题。如果你的子类增加了会影响对象相等性的属性，那多半说明你的类层次结构本身就有设计问题。与其用古怪的 `isEqual:` 实现去绕这个弯子，不如考虑重新设计你的类层次结构。

**关于字典的注意事项**  
如果你想把自己的对象用作 `NSDictionary` 里的键，就需要实现哈希和相等性，但还需要实现 `-copyWithZone:`。具体做法超出了本文的范围，但你应当知道：这种情况需要多做一些工作。

**结论**  
Cocoa 为相等性和哈希提供的默认实现对许多对象来说都够用；但如果你希望自己的对象即使是在内存里互不相同的对象，也照样被认定为相等，就必须额外做一些工作。好在这并不难，而且一旦实现，你的类就能与许多 Cocoa 集合类无缝协作。

本周就到这里。两周后再来看新一期。在那之前，请继续把你们想看的主题发给我。Friday Q&A 由读者投稿驱动，所以如果你有想在这里看到的话题，请[发邮件告诉我](mailto:mike@mikeash.com)。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-06-18-implementing-equality-and-hashing.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
