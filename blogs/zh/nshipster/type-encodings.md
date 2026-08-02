---
title: 类型编码
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/type-encodings/'
original_language: en
published: 2013-02-04
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:21660b3f9dee5bbb'
translated: true
---

> 原文：[Type Encodings](https://nshipster.com/type-encodings/)　·　NSHipster (Mattt)

# [类型编码](https://nshipster.com/type-encodings/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　2013 年 2 月 4 日

从[数字电台](https://en.wikipedia.org/wiki/Numbers_station)、[数字命理学](https://en.wikipedia.org/wiki/Numerology)，到[象形文字](https://en.wikipedia.org/wiki/Egyptian_hieroglyphs)与[流浪汉暗号](https://en.wikipedia.org/wiki/Hobo#Hobo_.28sign.29_code)，在显而易见之处找出隐藏含义这件事，总有一种真正迷人的吸引力。隐藏信息本身很少有多大用处或多么有趣，但寻觅它们所带来的刺激，会触动我们内心最深的好奇。

本期 NSHipster 正是抱着这种精神，来看看 [Objective-C 类型编码](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html)。

---

[上周](https://nshipster.com/nsvalue/)讨论 `NSValue` 时，提到过 `+valueWithBytes:objCType:`；它的第二个参数应由 Objective-C 的 `@encode()` 编译器指令创建。

`@encode` 是 [`@` 编译器指令](https://nshipster.com/at-compiler-directives/)之一。它会返回一个 C 字符串，用来编码给定类型的内部表示（例如 `@encode(int)` → `i`），类似 ANSI C 的 `typeof` 运算符。Apple 的 Objective-C runtime 在内部使用类型编码来协助完成消息派发。

下面列出所有不同的 Objective-C 类型编码：

| 编码 | 含义 |
|---|---|
| `c` | `char` |
| `i` | `int` |
| `s` | `short` |
| `l` | `long``l` 在 64 位程序中按 32 位量处理。 |
| `q` | `long long` |
| `C` | `unsigned char` |
| `I` | `unsigned int` |
| `S` | `unsigned short` |
| `L` | `unsigned long` |
| `Q` | `unsigned long long` |
| `f` | `float` |
| `d` | `double` |
| `B` | C++ `bool` 或 C99 `_Bool` |
| `v` | `void` |
| `*` | 字符串（`char *`） |
| `@` | 对象（无论静态类型还是 `id` 类型） |
| `#` | 类对象（`Class`） |
| `:` | 方法选择器（`SEL`） |
| [_array type_] | 数组 |
| {_name=type..._} | 结构体 |
| (_name_=_type..._) | 联合体 |
| `b`num | 由 _num_ 位组成的位域 |
| `^`type | 指向 _type_ 的指针 |
| `?` | 未知类型（除其他用途外，此编码用于函数指针） |

表格固然不错，但亲自在代码中试验会更好：

```
NSLog(@"int        : %s", @encode(int));
NSLog(@"float      : %s", @encode(float));
NSLog(@"float *    : %s", @encode(float*));
NSLog(@"char       : %s", @encode(char));
NSLog(@"char *     : %s", @encode(char *));
NSLog(@"BOOL       : %s", @encode(BOOL));
NSLog(@"void       : %s", @encode(void));
NSLog(@"void *     : %s", @encode(void *));

NSLog(@"NSObject * : %s", @encode(NSObject *));
NSLog(@"NSObject   : %s", @encode(NSObject));
NSLog(@"[NSObject] : %s", @encode(typeof([NSObject class])));
NSLog(@"NSError ** : %s", @encode(typeof(NSError **)));

int intArray[5] = {1, 2, 3, 4, 5};
NSLog(@"int[]      : %s", @encode(typeof(intArray)));

float floatArray[3] = {0.1f, 0.2f, 0.3f};
NSLog(@"float[]    : %s", @encode(typeof(floatArray)));

typedef struct _struct {
    short a;
    long long b;
    unsigned long long c;
} Struct;
NSLog(@"struct     : %s", @encode(typeof(Struct)));
```

结果：

| 类型 | 编码 |
|---|---|
| `int` | `i` |
| `float` | `f` |
| `float *` | `^f` |
| `char` | `c` |
| `char *` | `*` |
| `BOOL` | `c` |
| `void` | `v` |
| `void *` | `^v` |
| `NSObject *` | `@` |
| `NSObject` | `#` |
| `[NSObject]` | `{NSObject=#}` |
| `NSError **` | `^@` |
| `int[]` | `[5i]` |
| `float[]` | `[3f]` |
| `struct` | `{_struct=sqQ}` |

这里有几个值得注意的结论：

- 指针的标准编码是前置的 `^`，但 `char *` 有自己的编码：`*`。从概念上说这很合理，因为 C 字符串被视为独立实体，而不是指向别的东西的指针。
- `BOOL` 是 `c`，而不是你或许预期的 `i`。原因在于 `char` 比 `int` 小；Objective-C 最初在 20 世纪 80 年代设计时，比特（很像美元）比今天更值钱。`BOOL` 专门定义为 `signed char`（即使设置了 `-funsigned-char` 也是如此），以确保不同编译器之间的类型一致，因为 `char` 可以是 `signed` 或 `unsigned`。
- 直接传入 `NSObject` 会得到 `#`。但传入 `[NSObject class]` 会得到名为 `NSObject`、包含一个类字段 `isa` 的结构体；`NSObject` 实例通过该字段标识自己的类型。

## 方法编码

正如 Apple 的 [《Objective-C Runtime 编程指南》](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ObjCRuntimeGuide/Articles/ocrtTypeEncodings.html)所述，有少数类型编码仅供内部使用，无法通过 `@encode` 返回。

下面是协议中声明的方法会使用的类型限定符：

| 编码 | 含义 |
|---|---|
| `r` | `const` |
| `n` | `in` |
| `N` | `inout` |
| `o` | `out` |
| `O` | `bycopy` |
| `R` | `byref` |
| `V` | `oneway` |

熟悉 [NSDistantObject](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSDistantObject_Class/Reference/Reference.html) 的人，多半会认出它们是[分布式对象](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)留下的痕迹。

虽然在 iOS 时代 DO 已不再流行，它曾是 Cocoa 应用之间的进程间消息传递协议，甚至可以在网络上的不同机器之间运行。在这些约束下，额外的上下文确实有其价值。

例如，分布式对象消息中的参数默认以代理方式传递。若代理造成不必要的效率损失，可以加入 `bycopy` 限定符，确保发送对象的完整副本。参数默认也是 `inout`，表示发送消息时对象需要来回传递。将参数指定为 `in` 或 `out`，应用就能避免一次往返开销。

---

理解 Objective-C 类型编码究竟能带来什么？说实话，并没有太多（除非你在做疯狂的元编程）。

不过，正如开头所说，尝试破译秘密信息本身也有其智慧。

观察类型编码会揭示 Objective-C runtime 内部的细节，而这本身就是一项值得追求的事。再往兔子洞深处走，就会发现分布式对象的秘史，以及那些[至今仍然遗留着](https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSNumberFormatter_Class/Reference/Reference.html%23jumpTo_22)的晦涩参数限定符。
