---
title: 'Friday Q&A 2010-08-12：实现 NSCoding'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bedbbc37d6bf9ee9'
translated: true
---

> 原文：[Friday Q&A 2010-08-12: Implementing NSCoding](https://www.mikeash.com/pyblog/friday-qa-2010-08-12-implementing-nscoding.html)　·　mikeash.com Friday Q&A

发表于 2010-08-13 16:35 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2010-08-27：Cocoa 中的防御性编程](https://www.mikeash.com/pyblog/friday-qa-2010-08-27-defensive-programming-in-cocoa.html)  
上一篇：[Friday Q&A 2010-07-30：CoreFoundation 对象的零值弱引用](https://www.mikeash.com/pyblog/friday-qa-2010-07-30-zeroing-weak-references-to-corefoundation-objects.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [nscoding](https://www.mikeash.com/pyblog/?tag=nscoding) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec) [serialization](https://www.mikeash.com/pyblog/?tag=serialization)

Friday Q&A 2010-08-12：实现 NSCoding

作者：[Mike Ash](https://www.mikeash.com/)

**序列化**  
内存中的对象无法被直接保存或转移到其他程序。它们包含的数据——比如指针——只在你的进程内存空间的语境里才有效。把一个对象的内容挪进另一个程序，所有那些指针顿时失去意义。序列化（serialization）就是把对象不可移植的内存表示转换为可移植字节流的过程，这种字节流可以存储、也可以在进程之间搬动。

Cocoa 提供两种内建的序列化方式。最常用的是属性列表（property list）序列化，由 `NSPropertyListSerialization` 类实现。属性列表序列化速度快、输出易于理解，但能力相当有限：它只能存储少数支持属性列表序列化的类（如 `NSDictionary` 和 `NSString`），而且无法扩展它支持的类。

Cocoa 提供的另一种方式是归档（archiving）。归档能把以任意方式相连的任意对象序列化，并按需重构整个对象网。它极其强大，但并非完全自动，需要程序员写一些代码，让自己的类可以被归档。

归档分成两块。一块是真正的归档器（archiver）和解档器（unarchiver）类，即 `NSKeyedArchiver` 与 `NSKeyedUnarchiver`（以及它们的非键控版本）。它们负责把一堆对象转换为一堆字节的全部杂务。

另一块是 `NSCoding` 协议。这是由_你_来实现的代码，用来告诉归档器如何编码和解码你的类的实例。

**`NSCoding`**  
`NSCoding` 协议简短而简单，只包含两个方法：

```
    @protocol NSCoding
    
    - (void)encodeWithCoder:(NSCoder *)aCoder;
    - (id)initWithCoder:(NSCoder *)aDecoder;
    
    @end
```

你实现 `encodeWithCoder:` 来告诉归档器如何把你的对象序列化成字节，实现 `initWithCoder:` 来告诉归档器如何把序列化后的表示变成新对象。两个方法都必须实现。

注意，`encodeWithCoder:` 的参数虽然类型标作 `NSCoder`，实际却是你正在使用的那个具体归档器实例（例如一个 `NSKeyedArchiver`）。同样，`initWithCoder:` 的参数实际是你正在使用的那个具体解档器实例（例如 `NSKeyedUnarchiver`）。

**`NSCoding` 的基本实现**  
要实现 `encodeWithCoder:`，你应当遍历对象的全部必要属性，用 `NSCoder` 上的各种方法把它们编码。对象属性直接用 `encodeObject:forKey:`。键可以是任何描述被编码属性的简短字符串：

```
    - (void)encodeWithCoder: (NSCoder *)coder
    {
        [coder encodeObject: [self name] forKey: @"name"];
        [coder encodeObject: [self title] forKey: @"title"];
    }
```

`initWithCoder:` 的实现大体上是对称的。不过有几种不同的实现方式，取决于你的个人口味。

一种方式是把它实现为普通初始化方法，直接设置实例变量：

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        if((self = [self init]))
        {
            _name = [[coder decodeObjectForKey: @"name"] retain];
            _title = [[coder decodeObjectForKey: @"title"] retain];
        }
        return self;
    }
```

**重要提示：** 如果你使用这种风格且没有启用垃圾回收，_你必须保留（retain）从 `decodeObjectForKey:` 取出的对象_。这一步很容易忘，但该方法遵循 Cocoa 标准内存管理规则，返回的是你不拥有的对象。不保留它，它就会消失，你就会崩溃。

另一种方式是使用设置方法（setter），而不是直接设置实例变量：

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        if((self = [self init]))
        {
            [self setName: [coder decodeObjectForKey: @"name"]];
            [self setTitle: [coder decodeObjectForKey: @"title"];
        }
        return self;
    }
```

用设置方法还是直接设置实例变量哪个更好，当然[是个颇有争议的话题](https://www.mikeash.com/pyblog/friday-qa-2009-11-27-using-accessors-in-init-and-dealloc.html)。

最后，你还可以基于普通初始化方法来实现它。先解码对象，再转发调用你的普通初始化方法：

```
    - (id)initWithCoder: (NSCoder *)coder
    {
        NSString *name = [coder decodeObjectForKey: @"name"];
        NSString *title = [coder decodeObjectForKey: @"title"];
        
        return [self initWithName: name title: title];
    }
```

在所有这些可能性中，最后一种大概能让整体最简单。别的不说，它为需要实现初始化方法的子类提供了单一的重写点。

**键控归档与非键控归档**  
如果你细看 `NSCoder`，会注意到多数方法都有一个带键的变体和一个不带键的变体。例如：

```
    - (void)encodeObject:(id)object;
    - (void)encodeObject:(id)objv forKey:(NSString *)key;
```

为什么要有两个？

在 Mac OS X 10.2 发布之前的黑暗年代，只有非键控变体。它们要求编码与解码的调用序列严格一致，任何偏差都会导致错误，因为归档器无从得知你的意图。随着代码库日积月累地修改，这造成了巨大的麻烦。如果你新增了第三个需要编码的属性，又想让代码仍能读取旧归档（为新属性使用默认值），那你就得钻过许多痛苦的圈套。

键控变体灵活得多。你可以按任意顺序编码和解码；可以编码了数据却不去解码它；解码时可以检查某个键是否存在，缺失时提供默认值或改走别的路径。

今天，支持非键控归档基本已经没有理由。（在 Distributed Objects 中使用 `NSPortCoder` 时它仍有用处，但那极为罕见。）因此总的来说，编写你的 `NSCoding` 实现时应当假定键控编码，并使用 `NSKeyedArchiver` 和 `NSKeyedUnarchiver`。

如果出于某种原因你确实需要两者都支持，可以检查 `[coder allowsKeyedCoding]` 来判断面对的是哪一种，再采取相应行动。

**条件编码**  
`NSCoding` 的一大优点是让编码大型、复杂的对象图（object graph）变得容易。编码器会自动确保循环引用不会造成无限循环，也确保对同一对象的多次引用不会被编码成多份副本。

但有时你并不想编码整个对象图。设想一个棋盘游戏的实现，有一个棋盘类和一个棋子类：

```
    @interface GameBoard : NSObject <NSCoding>
    {
        NSMutableArray *_gamePieces;
    }
    @end
```

```
    @interface GamePiece : NSObject <NSCoding>
    {
        GameBoard *_gameBoard; // 弱引用，避免保留环
    }
    @end
```

你希望能序列化整个棋盘，并让所有棋子自动包含在内。这当然简单：让 `GameBoard` 编码它的 `_gamePieces` 数组即可。你还希望保住 `GamePiece` 指回棋盘的反向引用。这可以直接编码、解码它来实现。由于它是弱引用，解码时不保留它就好。

只要你序列化的是整个棋盘，这个方案就没问题。但也许你还想单独序列化一个棋子。那时会发生什么？

按实现 `NSCoding` 的朴素做法，你最终序列化的将不只是那个棋子，还有它所属的棋盘、棋盘上的所有其他棋子，以及棋盘包含的任何其他数据。更糟的是，由于 `_gameBoard` 引用是弱引用，解码之后棋盘会被销毁，留下悬空指针（dangling pointer）。你的归档又大，代码有时又在加载时莫名其妙地崩溃。这可不是你想要的！

为了解决这个问题，`NSCoder` 提供了_条件对象_（conditional object）。它让你_只有当别处无条件地编码了某个对象时_才编码它。如果没有任何东西_需要_这个对象，它就不会被编码；这种情况下，解码时你得到的是 `nil`。

条件对象非常适合编码大对象图中的一小部分。`GamePiece` 编码 `_gameBoard` 时可以使用条件对象。如果你显式编码了整个棋盘，条件对象就会指向它；而如果你只编码单个棋子，棋盘就_不会_被编码，因为从没有谁无条件地编码过它。

于是，解决这个问题的办法就是把 `-[GamePiece encodeWithCoder:]` 改成这样：

```
    - (void)encodeWithCoder: (NSCoder *)coder
    {
        [coder encodeConditionalObject: _gameBoard forKey: @"gameBoard"];
    }
```

一般来说，内存中的弱引用在你的 `NSCoding` 实现里都应该编码为条件对象。

**编码非对象数据**  
到目前为止我讲了很多编码对象的内容，但那些四处飘着的非对象数据怎么办？

对于基本类型，`NSCoder` 提供了编码各种整数和浮点类型的方法。你可以直接调用 `encodeInteger:forKey:` 或 `encodeDouble:forKey:` 保存你的各个值。遇到不支持的类型（比如 `short`），可以把它编码成更大的受支持兼容类型，比如 `int`。

结构体会更麻烦一些。非键控归档其实支持编码和解码任意结构体，但不知为何这个能力在键控归档器里被去掉了。也许是因为它太脆弱：结构体一改，所有旧归档全毁。

一般来说，处理结构体的最佳方式是把它的每个字段分开编码和解码。如果那样太笨拙，就该考虑把这个结构体重写成支持 `NSCoding` 的 Objective-C 类，这样就能直接编码它的实例。

对于 `NSRect` 这类 Cocoa 内建结构体，使用内建函数把它们转换成 `NSString`。例如调用 `NSStringFromRect` 编码得到的字符串，解码后再用 `NSRectFromString` 转回来。这样做效率略低，但编码和调试都容易得多。

最难啃的是数组。归档 C 数组没有内建支持。根据数组的大小和你愿意写多少代码，有几种变通办法：

1. 把 C 数组转换成一个装着 `NSValue` 实例的 `NSArray`，然后编码它。你可以在 `-initWithCoder:` 的实现里从 C 数组构造一个临时 `NSArray`，也可以做彻底的转换、全程使用 `NSArray`。
2. 动态构造键，把数组里的每个条目分开编码。可以写这样的循环：

  ```
          for(int i = 0; i < arrayLength; i++)
              [coder encodeInt: intArray[i] forKey: [NSString stringWithFormat: @"intArray%d", i]];
  ```

  解码时写一个类似的循环。
3. 用 `encodeBytes:length:forKey:` 编码原始字节。这需要特别留意字节序（endianness）和数据类型问题。（`NSInteger` 或 `CGFloat` 的数组，在不同机器上大小_不一定相同_；任何多字节值的数组，在不同机器上格式也可能不同。）如何处理这些问题多少超出了本文的范围，研究一下字节序和原始 C 数据的序列化即可覆盖。

C 字符串是数组的特例，最简单的处理办法大概是把它转成 `NSString` 再编码。把 C 字符串走一遍 `encodeBytes:length:forKey:` 也是安全的。

**读取旧归档**  
只要你的代码活得够久，迟早会改动编码和解码的内容。通常你仍希望代码在改动之后还能读取旧归档。

对于简单改动，比如给类新增一个属性，通常什么都不用做。你的 `decodeObject:forKey:` 调用会返回 `nil`；`decodeIntForKey:` 之类的方法会返回 `0`。把新代码写成能容忍这种情况，事情就完了。

有时你需要做更多。如果改动足够复杂，你也许想建两条独立的代码路径，一条走旧数据结构，一条走新的。这种情况下，在 `NSCoding` 实现里加一个 `version` 键就能轻松区分二者。解码时检查这个键的值，就知道该走哪条路。

注意，加 `version` 键不需要提前未雨绸缪。你可以在新代码里补上。旧归档里缺少 `version` 键这件事本身就把它们标识为旧版。如果你编码一个简单整数、把新版本号定为 `1`，那么尝试读取旧归档的版本号会恰好得到 `0`，将来还需要改动时也留有余地。

如果你重构代码，可能会改类名。这些类如果被归档过，就会出现不兼容：旧类名存在于旧归档里，解档器解码时找不到它就会失败。

绕开的办法是在解档前使用 `-setClass:forClassName:`：

```
    [unarchiver setClass: [NewClass class] forClassName: @"OldClass"];
```

**用旧代码读取新归档**  
反过来你也经常需要。往归档格式里加了新信息，并不意味着要让新归档与旧版软件不兼容。向后兼容不总是能维持，但如果改动简单，它可以很容易。

如果给类新增了属性，确保既有属性彼此保持一致，并且就旧版软件的需求而言是完整的。这样旧版本几乎不用费力就能继续工作。例如，设想你给 `Person` 类加了 `title` 属性。旧版本只会看到旧的 `name` 属性，丢失 `title`，但除此之外一切照常。

如果你彻底改造了一个类，可以考虑既编码新属性，_也_编码一套面向旧代码的兼容属性。新代码读新属性，旧代码读旧属性，至少还能以某种方式继续工作。

最后，如果你改了类名，不做补偿就会破坏旧版软件，正如改类名会破坏旧归档。修复办法是用 `setClassName:forClass:` 方法告诉归档器以旧名保存你的类：

```
    [archiver setClassName: @"OldClass" forClass: [NewClass class]];
```

向后兼容可能很难，特别是当你新增大量数据或能力时。而且它通常也远不如向前兼容重要。权衡好其中的取舍，不要害怕打破向后兼容。只需确保：如果真打破了，把新归档加载进旧版软件时能体面地失败。

**结语**  
`NSCoding` 是序列化对象的利器，让你能在进程间传递对象或把它们存进文件。在你想要序列化的自定义对象上实现 `NSCoding` 协议，然后用 `NSKeyedArchiver` 序列化、`NSKeyedUnarchiver` 反序列化。

本期 Friday Q&A 就到这里。下次再见，届时又是 Mac 编程世界里的一场精彩冒险。在那之前，如果你有想在这里看到的话题，请[把你的建议发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-08-12-implementing-nscoding.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
