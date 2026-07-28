---
title: 'Friday Q&A 2012-07-27：构建 Tagged Pointer'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:af51233dc62f68c4'
translated: true
---

> 原文：[Tagged pointers](https://www.mikeash.com/pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)　·　mikeash.com Friday Q&A

发布于 2012-07-27 13:35 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-08-10: A Tour of CommonCrypto](https://www.mikeash.com/pyblog/friday-qa-2012-08-10-a-tour-of-commoncrypto.html)  
上一篇：[Friday Q&A 2012-07-06: Let's Build NSNumber](https://www.mikeash.com/pyblog/friday-qa-2012-07-06-lets-build-nsnumber.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-07-27：构建 Tagged Pointer

作者：[Mike Ash](https://www.mikeash.com/)

**指针对齐（Pointer Alignment）理论**

众所周知，指针是一个被当作内存地址来使用的整数。在底层，保存对象指针的变量实际上只是一个保存着像 `0x7f84a41000c0` 这样的整数值的整数。这个值的指针特性完全取决于程序如何使用它。在 C 语言中，我们可以通过简单的类型转换来提取指针的整数值：

```
    void *somePointer = ...;
    uintptr_t pointerIntegerValue = (uintptr_t)somePointer;
```

（`uintptr_t` 类型是标准 C 中的一个 `typedef`，它定义了一个足够大、可以容纳指针的整数类型。这很有用，因为指针大小在不同平台上会有所不同。）

大多数计算机架构都有**指针对齐（pointer alignment）**的概念。这意味着指向特定数据类型的指针应该是2的某次幂的倍数。例如，指向一个4字节整数的指针在大多数架构上都应该是4的倍数。违反对齐限制会导致性能问题（在某些平台上，这种尝试会抛出硬件异常，需要由操作系统来模拟处理），并且在某些对性能敏感的架构上，可能会直接崩溃。正确的对齐对于诸如内存的原子读写等操作也是必需的。简而言之，指针对齐很重要，你需要遵守它。

如果你创建一个局部变量，编译器可以确保对齐正确：

```
    void f(void)
    {
        int x;
        // x 已正确对齐，因为
        // 编译器完全可以控制
        // 它的位置
    }
```

然而，对于动态分配的内存，情况就没那么简单了：

```
    int *ptr = malloc(sizeof(*ptr));
    // ptr 对齐正确吗？
```

`malloc` 并不知道程序将要存储何种类型的数据。它收到一个请求要4个字节（假设 `int` 是4个字节），但它不知道这是用于存储一个 `int`、一个指针（在32位平台上）、两个 `short`、四个 `char` 还是其他什么内容。

为了确保正确对齐，`malloc` 采取了一种保守的方法，返回的指针对齐到足以保证无论存储何种数据类型都能正确对齐的边界上。在 Mac OS X 上，`malloc` 总是返回对齐到16字节边界的指针。

由于对齐的存在，任何对齐后的指针都会有未使用的位。一个16字节对齐指针的十六进制表示类似于：

```
    0x-------0
```

最后一个十六进制数字**总是** `0`。可能存在不遵守这一规则的合法指针（例如，`char *` 没有对齐限制），但对象指针的末尾总是会有一些零位。

**Tagged Pointer 理论**

有些对象包含的数据非常少。`NSNumber` 就是一个很好的例子：根据对象存储的数字类型不同，它存储的数据可能只有1、2、4或8个字节。为这些数据分配一个完整的对象，进行内存分配和释放，并在每次访问时通过指针进行间接引用，这种做法是浪费的。

如果我们利用指针中那些未使用的低位来表明这不是一个真正的指针，会怎么样呢？如果我们随后将对象数据内联存储在这个非指针的其余部分，而不是存放在单独分配的内存中，又会怎么样呢？这样做出来的就是 Tagged Pointer。

使用 Tagged Pointer 的系统需要一个额外的检查。每当对象指针被使用时，系统都会检查低位。如果它是 0，那么这就是一个真实的对象指针，并按正常方式处理。如果低位是 1，那么它不可能是真正的指针，因为它没有正确对齐。在这种情况下，指针会被特殊处理。通常，对象的类型编码在指针的低位，而对象数据在高位。一个正常的指针看起来像这样：

```
    ....0000
        ^ all zeroes at the end
```

而一个 Tagged Pointer 看起来像这样：

```
    ....xxx1
        ^ type encoded in bottom bits
```

这里有一些变体。例如，标签指针可以设置底部四位中的**任意**位。通过利用其他架构特性，你甚至可以拥有更多的标签（tag）位。例如，`x86_64` 实际上只使用了指针的48位，除了因为对齐而得到的4位，你还剩16位空闲。利用这些，你可以做诸如把指针塞进浮点数的“非数字（not a number）”值里这类疯狂的事情。

无论出于什么原因，Objective-C 对标签指针的实现中，标签指针的最低比特位总是设置为 `1`，另外三个位用于指示标签指针的类。我不确定他们为什么选择这种方式来实现，但我的猜测是综合了速度（只检查最低位可能更容易，而且这必须在 `objc_msgSend` 的热路径上完成）和编程便利性。

**Tagged Pointer 的用途**

标签指针经常出现在一切皆为对象的语言中。当数字 `3` 是一个对象，而像 `3 + 4` 这样的表达式涉及两个对象并创建第三个对象时，对象创建和值提取对性能就变得至关重要。

我们通常认为对象是单独分配的内存块，通过指针引用。在标签指针出现之前，Objective-C 中一直是这种情况，许多其他语言也是如此。然而，内存分配和管理会产生巨大的开销。当计算 `3 + 4` 时，为结果 `7` 分配内存然后最终在没有人使用时释放它的开销，远远超过了实际执行加法的成本。

通过指针引用一切也会仅仅为了访问数据而带来开销。为了加载 `3` 对象的值，CPU 必须先加载指向该对象的指针的值，然后再加载对象内部存储的原始 `3`。由于内存访问速度较慢，这种额外的访问可能代价高昂。

通过使用标签指针，对于适合放入标签指针的数据，可以消除这些成本。小整数是绝佳候选，因为它们很容易放进去，并且使用频率很高。整数 `3` 通常表示为：

```
    0000 0000 0000 0000 0000 0000 0000 0011
                                         ^ binary 3
```

使用标签指针时，它看起来像这样：

```
    0000 0000 0000 0000 0000 0000 0011 1011
                                    ^  ^  ^ tag bit
                                    |  |
                                    |  tagged pointer class (5)
                                    |
                                    binary 3
```

实际的值被移了一位，并设置了适当的标签位。在这个例子中，我假设整数类由标签位中的值 `5` 标识，但这完全是任意的，系统会决定标签位中每个值的含义。

细心的读者会注意到，用于存储值的空间比普通整数要小。在32位系统上，使用4位作为标签后，剩余28位用于存储值；在64位系统上，剩余60位。需要超过28位或60位才能存储的整数无法放入标签指针，而必须存储在常规对象中。

当所有数据都能放入标签指针时，就不需要单独的内存分配了。这意味着没有分配或销毁内存的开销。不需要额外的内存加载，因为所有数据都在指针里。会有一些额外的开销，因为需要一些移位和掩码操作来提取 `3`，但 CPU 对这些操作非常快速，并且比访问单独的内存块快得多。

除了速度优势之外，这还减少了内存使用，因为不需要分配单独的内存块来保存这些整数。对于像 `3 + 4` 这样的单个表达式，这无关紧要，但对于大量使用整数的代码，它可以显著节省资源。

通过使用标签位来区分多个标签指针类，可以存储的不仅仅是整数。浮点数也可以存储在标签指针中。甚至像短字符串这样的冷门内容也可以存储。（一个64位指针除了标签位之外还可以容纳八个 ASCII 字符）。一个包含单个（非 tagged）对象指针的单元素数组也可以放入标签指针。任何既小又频繁使用的类都是标签指针的良好候选。

尽管 Objective-C 有原始整数类型，并非每个数学表达式都使用对象，但在大量 Objective-C 代码中，数字对象仍然很常见。每当我们把数字放入数组或字典时，我们必须使用 `NSNumber` 将它们装箱（box）成对象。每当我们编码或解码属性列表（property list）或 JSON 时，我们必须让所有数字都通过 `NSNumber`。由于 `NSNumber` 使用频繁，并且主要用于存储适合放入标签指针的数字，所以 `NSNumber` 是标签指针的绝佳候选，实际上 Cocoa 也正是这么做的。标签指针也用于合适的 `NSDate` 对象。此外还有充足的空间可用于扩展到其他用途。

**标签指针的实践**

理论说得够多了，让我们写点代码。

你们可能还记得上次提到的 `NSNumber` 的替代品 `MANumber`。我现在将为 `MANumber` 添加标签指针支持。

请注意，标签指针非常、非常、非常私有，无论如何都不能在任何真实代码中使用。可用的标签指针类数量极其有限。由于只有三个标签位可用于指示类，因此只能使用八个 tagged 类。如果你的 tagged 类与框架中的某个类冲突，那就完蛋了。此外，由于标签指针实现的细节没有通过任何公共 API 公开，它们可能会随时更改，恕不另行通知。标签位的含义或数量可能会变化，或者如果认为不值得花费这些麻烦，整个机制可能被抛弃。

然而，通过使用适当的私有 API，我们是可以**实验**标签指针的，尽管我们永远不能安全地使用它们。

具体来说，私有函数 `_objc_insert_tagged_isa` 允许将类与特定的标签关联。它的原型是：

```
    void _objc_insert_tagged_isa(unsigned char slotNumber, Class isa);
```

你给它一个插槽编号（标签）和一个类，它就会设置相应的表条目，以便在运行时中将两者关联起来。

几乎所有标签指针类都需要一个非 tagged 类作为补充。在这种情况下，我们需要常规的 `MANumber` 来存储不适合标签指针的整数，以及存储 `double` 值——这些值**非常**难以塞进标签指针，因此我跳过了。根据要存储的值，我们要么创建一个标签指针，要么分配一个普通的实例。

这里有两种方法。一种是创建两个完全不同的类，通过某种公共超类来共享公共代码。另一种是两者使用同一个类，并在代码查找内部数据（如实例变量）时为 tagged 和非 tagged 指针提供两条代码路径。我在这里选择了后一种方法，因为在这种情况下它似乎更简单。

大部分情况下，`MANumber` 可以保持不变。我将一些直接的实例变量访问路由到访问器（accessor）中，以便将所有条件代码分组到一个地方，但类的大部分内容保持不变。`MANumber` 使用一个 `union` 来存储实际值，我发现将其提取出来以便用于传递值（而不仅仅作为实例变量）是很有用的：

```
    union Value
    {
        long long i;
        unsigned long long u;
        double d;
    };
```

接下来是用于操作标签指针的一些常量。首先是用于 `MANumber` 的标签指针插槽，我任意选择为 `1`：

```
    const int kSlot = 1;
```

我还将标签位的数量放入一个常量中，因为它用于编码和解码标签指针：

```
    const int kTagBits = 4;
```

我决定在标签指针中保持 `MANumber` 的基本结构。它存储了一个值以及一个用于说明如何解释该值的类型。类型可以是整数、无符号整数或 `double`。由于所有内容都需要尽可能紧凑地打包，我想用最少的位数来表示类型。因为有三种类型，我预留了两位来存放类型：

```
    const int kTypeBits = 2;
```

注意，尽管我不在标签指针中支持 `double`，但我仍然预留了足够的空间来表示它的类型。这样做纯粹是为了保持一致性，并便于将来某个时候添加对 `double` 的支持。

最后，由于我们要存储的整数类型是 `long long`，知道它确切有多少位是很有用的：

```
    const int kLongLongBits = sizeof(long long) * CHAR_BIT;
```

在这段代码中，我假设 `long long` 的大小与指针大小相同。我没有尝试创建标签指针代码的32位兼容版本。

为了更好地操作标签指针，我编写了一些辅助函数。第一个函数从一个值和类型构造一个 tagged `MANumber` 指针：

```
    static id TaggedPointer(unsigned long long value, unsigned type)
    {
```

回顾一下标签指针的结构。最低有效位总是 `1`。接下来的三位是标签或插槽，它指示对象的类。之后是类自己的数据。在这种情况下，接下来的两位是类型，剩下的所有位都是值。下面这行代码通过位操作（移位和“或”）将这些组件组合在一起：

```
        id ptr = (__bridge id)(void *)((value << (kTagBits + kTypeBits)) | (type << kTagBits) | (kSlot << 1) | 1);
```

注意这里奇怪的两次转换（double cast）。我在使用 ARC 编译，它对转换很挑剔。在对象指针和非对象指针之间进行转换时，你需要使用 `__bridge`，而且 ARC 根本不允许在对象指针和整数之间进行转换。为了在标签指针的整数版本和对象版本之间进行转换，我首先必须将整数转换为 `void *`，然后才能将结果转换为对象。

需要做的就这么多了，所以我返回新构造的指针：

```
        return ptr;
    }
```

我还写了一个函数来检查一个指针是否是 tagged 的。这只需检查最低有效位，但需要丑陋的转换来满足 ARC 的要求，所以把它封装在一个函数里是件好事：

```
    static BOOL IsTaggedPointer(id pointer)
    {
        uintptr_t value = (uintptr_t)(__bridge void *)pointer;
        return value & 1;
    }
```

最后，有一个函数可以将标签指针分解成它的组成部分。由于 C 不支持多返回值，我创建了一个 `struct` 来保存要返回的两个值：值和类型。

```
    struct TaggedPointerComponents
    {
        unsigned long long value;
        unsigned type;
    };
```

函数本身首先将指针转换为整数，使用上面展示的奇怪的双重转换的逆操作：

```
    static struct TaggedPointerComponents ReadTaggedPointer(id pointer)
    {
        uintptr_t value = (uintptr_t)(__bridge void *)pointer;
```

接下来，它提取相关字段。标签位本身可以被忽略，因为它们不影响 `MANumber` 的值或类型。通过将指针向下移动适当的位数来提取 `MANumber` 的值：

```
        struct TaggedPointerComponents components = {
            value >> (kTagBits + kTypeBits),
```

类型必须同时进行掩码和移位。掩码是通过将 `1` 左移 `kTypeBits` 位，生成二进制值 `100`，然后从中减去 `1`，得到二进制值 `11`。通过使用该值进行逻辑“与”操作，我们可以去除指针中除了表示类型的位之外的所有位：

```
            (value >> kTagBits) & ((1ULL << kTypeBits) - 1)
        };
```

现在组件被提取出来了，函数只需返回它们。

```
        return components;
    }
```

在某些时候，我们必须通过调用 `_objc_insert_tagged_isa` 来实际告诉运行时我们想要作为一个标签指针类来运作。显而易见的地方是在 `+initialize` 中。我实际上调用了两次，一次是清除任何先前的条目，另一次是插入新条目。作为保护措施，如果你试图直接覆盖标签指针表中的现有类，Objective-C 运行时会非常不高兴：

```
    + (void)initialize
    {
        if(self == [MANumber class])
        {
            _objc_insert_tagged_isa(kSlot, nil);
            _objc_insert_tagged_isa(kSlot, self);
        }
    }
```

现在我们可以开始实际构造标签指针了。我写了两个新方法：`+numberWithLongLong:` 和 `+numberWithUnsignedLongLong:`。如果可能，这些方法会尝试从其参数构造一个标签指针，否则会回退到分配一个类的实例。

这些方法只有在值在特定限制内时才能创建标签指针。也就是说，该值必须能够放入 `kLongLongBits - kTagBits - kTypeBits` 位（在64位系统上是58位）的空间内。能放入该空间的最大 `long long` 是 2^57-1。能放入的最小 `long long` 是 -2^57。由于 `long long` 是有符号的，所以需要一位作为符号位。基于此，我们计算 tagged `long long` 的最小值和最大值：

```
    + (id)numberWithLongLong: (long long)value {
        long long taggedMax = (1ULL << (kLongLongBits - kTagBits - kTypeBits - 1)) - 1;
        long long taggedMin = -taggedMax - 1;
```

剩下的就很简单了。如果值超出了范围，我们只需执行常规的 `alloc`/`init` 流程。如果值在范围内，我们调用 `TaggedPointer`，传入值和 `INT` 来构造标签指针：

```
        if(value > taggedMax || value < taggedMin)
            return [[self alloc] initWithLongLong: value];
        else
            return TaggedPointer(value, INT);
    }
```

`unsigned long long` 的代码类似。这种情况下只有一个限制，即 2^58-1：

```
    + (id)numberWithUnsignedLongLong:(unsigned long long)value {
        unsigned long long taggedMax = (1ULL << (kLongLongBits - kTagBits - kTypeBits)) - 1;

        if(value > taggedMax)
            return [[self alloc] initWithUnsignedLongLong: value];
        else
            return (id)TaggedPointer(value, UINT);
    }
```

接下来，我们需要一个能处理标签指针的 `type` 访问器，这样其余代码就可以简单地调用 `[self type]`，而无需担心位和掩码等问题。这相当简单。它所要做的就是调用 `IsTaggedPointer`，如果指针是 tagged 的则调用 `ReadTaggedPointer`，否则直接返回 `_type` 实例变量：

```
    - (int)type
    {
        if(IsTaggedPointer(self))
            return ReadTaggedPointer(self).type;
        else
            return _type;
    }
```

还有一个 `value` 访问器，但由于需要处理结果值的符号扩展（sign extension），它稍微复杂一些。它做的第一件事是检查指针是否是 tagged 的，如果不是，则返回 `_value` 实例变量：

```
    - (union Value)value
    {
        if(!IsTaggedPointer(self))
        {
            return _value;
        }
```

对于标签指针，它首先从 `ReadTaggedPointer` 读取值。这个值以 `unsigned long long` 形式出现，因此在实际类型是有符号的情况下需要一些处理：

```
        else
        {
            unsigned long long value = ReadTaggedPointer(self).value;
```

它还创建了一个 `union Value` 类型的局部变量来保存返回值：

```
            union Value v;
```

如果值是无符号的，那么生活很简单：只需将 `value` 塞入 `v`：

```
            int type = [self type];
            if(type == UINT)
            {
                v.u = value;
            }
```

然而，有符号整数稍微复杂一些。它做的第一件事是检查符号位，在这个例子中它位于第 `57` 位：

```
            else if(type == INT)
            {
                unsigned long long signBit = (1ULL << (kLongLongBits - kTagBits - kTypeBits - 1));
```

如果符号位被设置，那么数字中超出 `57` 位的所有其他位也必须设置为 `1`，以便生成的 `long long` 被视为一个正确的64位负数。这个过程称为[符号扩展（sign extension）](http://en.wikipedia.org/wiki/Sign_extension)，它之所以这样工作，是因为现代计算机实现有符号整数的方式。简而言之，一个负数由开头的一串 `1` 组成，而第一个 `0` 实际上是数字的第一个有效位。为了加宽一个正数，你只需在左边添加 `0`。为了加宽一个负数，你需要在左边添加 `1`：

```
                if(value & signBit)
                {
                    unsigned long long mask = (((1ULL << kTagBits + kTypeBits) - 1) << (kLongLongBits - kTagBits - kTypeBits));
                    value |= mask;
                }
```

对于正数不需要做任何处理，因为它们左边已经填满了额外的 `0`。需要做的只是将值赋给 `v` 中的正确字段：

```
                v.i = value;
            }
```

如果类型是其他值，那么说明出了问题，所以要进行检查并调用 `abort`：

```
            else
                abort();
```

最后，返回 `v`：

```
            return v;
        }
    }
```

有了这些代码，所有其他的 `MANumber` 代码无需任何更改就能工作，只需修改这些代码以调用这些访问器而不是直接访问实例变量即可。你可以随意混合使用 tagged 和 untagged 的 `MANumber` 实例，甚至可以在混合对象上使用 `compare:` 和 `isEqual:`。

**结论**

标签指针是 Cocoa 和 Objective-C 运行时的一个伟大补充，它们提高了 `NSNumber` 对象的速度并减少了内存使用。通过将对象数据直接塞入指针，标签指针消除了对单独内存分配的需求，以及在检索值时额外一层间接引用的需要。

通过使用私有运行时调用和一些位操作，我们可以实现自己的标签指针类，这让我们深入了解 `NSNumber` 在幕后所做的事情。然而，由于标签指针类的数量有限，我们无法在自己的代码中安全地使用标签指针。它们纯粹是 Cocoa 为了提升性能而使用的机制。它们完美地完成了这项工作，并让 `NSNumber` 的使用不再那么痛苦。

今天就到这里！下次回来，我们将带来更多疯狂的花招。Friday Q&A 由读者建议驱动，所以如果你有想在这里看到的话题想法，请[发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正出售整套书籍！第二卷和第三卷现已上市！提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上阅读。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-07-27-lets-build-tagged-pointers.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
