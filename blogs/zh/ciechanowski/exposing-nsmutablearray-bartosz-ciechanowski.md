---
title: 揭示 NSMutableArray——Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/exposing-nsmutablearray/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:65140d08fc8fc675'
translated: true
---

> 原文：[Exposing NSMutableArray – Bartosz Ciechanowski](https://ciechanow.ski/exposing-nsmutablearray/)　·　Bartosz Ciechanowski

# [揭示 NSMutableArray](https://ciechanow.ski/exposing-nsmutablearray/)

我一直好奇 `NSMutableArray` 内部是如何工作的。别误会，不可变数组确实有巨大的好处：它们不仅是线程安全的，而且复制它们基本没有开销。但这改变不了它们相当呆板的事实——它们的内容不能被修改。我觉得实际的内存操作细节很迷人，这就是为什么这篇文章专注于可变数组。

由于我或多或少描述了用来研究 `NSMutableArray` 的完整过程，所以这篇文章相当技术性。有一整节讨论了 ARM64 汇编，如果你觉得那很无聊，请随意跳过。一旦我们完成了底层细节，我会介绍这个类的 _非显而易见_ 的特性。

`NSMutableArray` 的实现细节不公开是有原因的。它们随时可能改变，无论是在底层的子类及其 ivar 布局，还是在支撑算法和数据结构方面。尽管有这些警告，一探 `NSMutableArray` 的内部机制，弄清楚它是如何工作的以及你可以期望什么，仍然是值得的。以下研究基于 iOS 7.0 SDK。

像往常一样，你可以在 [我的 GitHub](https://github.com/Ciechan/NSMutableArrayExplorer) 上找到附带的 Xcode 项目。

# 普通 C 数组的问题[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#the-problem-of-plain-old-c-arrays)

每个有自尊的程序员都知道 C 数组是如何工作的。它归结为一段连续的内存，可以轻松地读取和写入。虽然数组和指针不是一回事（参见 [《Expert C Programming》](http://www.amazon.com/Expert-Programming-Peter-van-Linden/dp/0131774298) 或 [这篇文章](http://eli.thegreenplace.net/2009/10/21/are-pointers-and-arrays-equivalent-in-c/)），但将 "`malloc`-ed 的内存块" 视为数组也不算滥用。

使用线性内存最明显的缺点之一是在索引 0 处插入元素需要通过 `memmove` 移动所有其他元素：

![在索引 0 处向 C 数组插入](https://ciechanow.ski/images/arrayCInsert@2x.jpg)

在索引 0 处向 C 数组插入

类似地，删除第一个元素也需要移动操作，假设你想保持相同的内存指针作为第一个元素的地址：

![在索引 0 处从 C 数组删除](https://ciechanow.ski/images/arrayCRemove@2x.jpg)

在索引 0 处从 C 数组删除

对于非常大的数组，这很快就会成为一个问题。显然，直接指针访问不一定是数组世界中的最高抽象级别。虽然 C 风格数组通常很有用，但想要一个可变、索引容器的 Obj-C 程序员的日常工作首选是 `NSMutableArray`。

# NSMutableArray[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#nsmutablearray)

## 深入探究[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#diving-in)

尽管 Apple [公开了许多库的源代码](http://opensource.apple.com)，但 Foundation 及其 `NSMutableArray` 并未开源。然而，有一些工具可以让揭示其奥秘变得稍微容易一些。我们从尽可能高的层次开始我们的旅程，深入到较低的层次以获取原本无法访问的细节。

### 获取并转储类[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#getting--dumping-class)

`NSMutableArray` 是一个类簇（class cluster）——它的具体实现实际上是 `NSMutableArray` 本身的子类。`+[NSMutableArray new]` 实际返回的是哪个类的实例？有了 LLDB，我们甚至不需要编写任何代码就能弄清楚：

```plain
(lldb) po [[NSMutableArray new] class]
__NSArrayM
```

有了类名，我们使用 [class-dump](http://stevenygard.com/projects/class-dump/)。这个方便的实用程序通过分析提供的二进制文件来伪造类头文件。使用下面的一行命令，我们可以提取我们感兴趣的 ivar 布局：

```bash
./class-dump --arch arm64 /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS7.0.sdk/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation | pcregrep -M "^[@\w\s]*__NSArrayM[\s\w:{;*]*}"
```

我正则表达式很烂，所以上面用的那个可能不是杰作，但它产生了丰硕的结果：

```objc
@interface __NSArrayM : NSMutableArray
{
    unsigned long long _used;
    unsigned long long _doHardRetain:1;
    unsigned long long _doWeakAccess:1;
    unsigned long long _size:62;
    unsigned long long _hasObjects:1;
    unsigned long long _hasStrongReferences:1;
    unsigned long long _offset:62;
    unsigned long long _mutations;
    id *_list;
}
```

原始输出中的位域是用 `unsigned int` 声明的，但显然你无法将 62 位放入一个 32 位整数中——class-dump 尚未针对正确解析 ARM64 库得到修补。尽管有这些小缺陷，仅通过查看其 ivar 就可以了解该类的很多信息。

### 反汇编类[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#disassembling-class)

我的研究中最重要的工具是 [Hopper](http://www.hopperapp.com)。我深爱这个反汇编器。对于必须知道一切如何运作的好奇灵魂来说，它是一个必不可少的工具。Hopper 最好的特性之一是它能生成类似 C 的伪代码，这通常足够清晰以把握实现的要点。

理解 `__NSArrayM` 的关键方法是 `- objectAtIndex:`。虽然 Hopper 在提供 ARMv7 的伪代码方面做得很好，但这个功能对 ARM64 还不起作用。我认为手动完成这项工作，并从其 ARMv7 对应物中获得一些提示，将是一个极好的练习。

# 剖析方法[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#dissecting-the-method)

一手拿着 [ARMv8 指令集概述](https://silver.arm.com/download/ARM_and_AMBA_Architecture/AR100-DA-70501-r0p0-00eac5/ARMv8_ISA_PRD03-GENC-010197-30-0.pdf)（需要注册），另一手拿着一堆有根据的猜测，我 _认为_ 我已经正确地破译了汇编。然而，你不应该将以下分析视为智慧的终极来源。我对此还是个新手。

## 传递参数[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#passing-arguments)

作为起点，让我们注意每个 Obj-C 方法实际上都是一个 C 函数，带有两个额外的参数。第一个是 `self`，它是一个指向作为方法调用接收者的对象的指针。第二个是 `_cmd`，它代表当前的选择器（selector）。

可以说 `- objectAtIndex:` 函数等效的 C 风格声明是：

```objc
id objectAtIndex(NSArray *self, SEL _cmd, NSUInteger index);
```

因为在 ARM64 上，这些类型的参数被传递到连续的寄存器中，我们可以预期 `self` 指针在 `x0` 寄存器中，`_cmd` 在 `x1` 寄存器中，对象的 `index` 在 `x2` 寄存器中。有关参数传递的详细信息，请参考 [ARM 过程调用标准](http://infocenter.arm.com/help/topic/com.arm.doc.ihi0055b/IHI0055B_aapcs64.pdf)，注意 Apple 的 iOS 版本有 [一些差异](https://developer.apple.com/library/ios/documentation/Xcode/Conceptual/iPhoneOSABIReference/Articles/ARM64FunctionCallingConventions.html)。

## 分析汇编[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#analyzing-assembly)

这看起来会有些吓人。由于一次分析一大段汇编是不理智的，我们将逐步浏览下面的代码，弄清楚每一行的作用。

```s
0xc2d4         stp        x29, x30, [sp, #0xfffffff0]!
0xc2d8         mov        x29, sp
0xc2dc         sub        sp, sp, #0x20
0xc2e0         adrp       x8, #0x1d1000
0xc2e4         ldrsw      x8, [x8, #0x2c]
0xc2e8         ldr        x8, [x0, x8]
0xc2ec         cmp        x8, x2
0xc2f0         b.ls       0xc33c

0xc2f4         adrp       x8, #0x1d1000
0xc2f8         ldrsw      x8, [x8, #0x30]
0xc2fc         ldr        x8, [x0, x8]
0xc300         lsr        x8, x8, #0x2
0xc304         adrp       x9, #0x1d1000
0xc308         ldrsw      x9, [x9, #0x34]
0xc30c         ldr        x9, [x0, x9]
0xc310         add        x9, x2, x9, lsr #2
0xc314         cmp        x8, x9
0xc318         csel       x8, xzr, x8, hi
0xc31c         sub        x8, x9, x8
0xc320         adrp       x9, #0x1d1000
0xc324         ldrsw      x9, [x9, #0x38]
0xc328         ldr        x9, [x0, x9]
0xc32c         ldr        x0, [x9, x8, lsl #3]
0xc330         mov        sp, x29
0xc334         ldp        x29, x30, [sp], #0x10
0xc338         ret  
```

### 设置[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#the-setup)

我们从一个看起来像是 ARM64 [函数序言](http://en.wikipedia.org/wiki/Function_prologue) 的部分开始。我们在栈上保存 `x29` 和 `x30` 寄存器，然后将当前栈指针 `sp` 移动到 `x29` 寄存器：

```s
0xc2d4         stp        x29, x30, [sp, #0xfffffff0]!
0xc2d8         mov        x29, sp
```

我们在栈上留出一些空间（减法，因为栈向下增长）：

```s
0xc2dc         sub        sp, sp, #0x20
```

我们感兴趣的代码路径似乎没有使用这个空间。然而，“越界”异常抛出代码确实调用了其他一些函数，因此序言必须为这两种情况提供便利。

### 获取计数[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#fetching-count)

接下来的两行执行 [程序计数器相对寻址](http://en.wikipedia.org/wiki/Addressing_mode#PC-relative_2)。地址编码的具体细节 [相当复杂](http://kitoslab.blogspot.com/2012/10/armv8-aarch64-instruction-encoding.html)，而且文献很少，但是，Hopper 自动计算了更合理的偏移量：

```s
0xc2e0         adrp       x8, #0x1d1000
0xc2e4         ldrsw      x8, [x8, #0x2c]
```

这两行将获取位于 `0x1d102c` 的内存内容并将其存储到 `x8` 寄存器中。那里有什么？Hopper 很乐意帮助我们：

```s
_OBJC_IVAR_$___NSArrayM._used:
0x1d102c         dd         0x00000008
```

这是 `__NSArrayM` 类中 `_used` ivar 的偏移量。为什么还要费心去额外获取，而不是直接把值 `8` 放入汇编中？这是因为 [脆弱基类](http://en.wikipedia.org/wiki/Fragile_base_class) 问题。现代 Objective-C 运行时通过给自己一个选项来覆盖 `0x1d102c` 处的值（以及所有其他 ivar 偏移量）来处理这个问题。如果 `NSObject`、`NSArray` 或 `NSMutableArray` 添加了新的 ivar，旧的二进制文件仍然可以工作。

![运行时可以动态修改 ivar 的偏移量而不会破坏兼容性](https://ciechanow.ski/images/arrayFragile@2x.jpg)

运行时可以动态修改 ivar 的偏移量而不会破坏兼容性

虽然 CPU 必须做一次额外的内存读取，但这是一个漂亮的解决方案，[Hamster Emporium](http://www.sealiesoftware.com/blog/archive/2009/01/27/objc_explain_Non-fragile_ivars.html) 和 [Cocoa with Love](http://www.cocoawithlove.com/2010/03/dynamic-ivars-solving-fragile-base.html) 对其有更详细的解释。

此时我们知道 `_used` 在类中的偏移量。由于 Obj-C 对象只不过是 `struct`，并且我们在 `x0` 中有指向这个结构体的指针，我们所要做的就是获取值：

```s
0xc2e8         ldr        x8, [x0, x8]
```

上面代码的 C 等效项是：

```obj
    unsigned long long newX8 = *(unsigned long long *)((char *)(__bridge void *)self + x8);
```

我想我更喜欢汇编版本。快速分析 `__NSArrayM` 的反汇编后的 `- count` 方法显示，`_used` ivar 包含了 `__NSArrayM` 中的元素数量，此时此刻我们在 `x8` 寄存器中有了这个值。

### 检查边界[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#checking-bounds)

代码比较了 `x2` 中的请求索引和 `x8` 中的计数：

```s
0xc2ec         cmp        x8, x2
0xc2f0         b.ls       0xc33c
```

当 `x8` 的值小于或等于 `x2` 时，我们跳转到地址 `0xc33c` 处的代码，该代码处理异常抛出。这本质上就是边界检查。如果我们未能通过测试（计数小于或等于索引），我们会抛出异常。我不打算讨论反汇编的那部分，因为它们并没有引入什么新东西。如果我们通过了测试（计数大于索引），那么我们就按顺序继续执行指令。

### 计算内存偏移量[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#calculating-memory-offset)

我们以前见过这个，这次我们获取位于 `0x1d1030` 的 `_size` ivar 的偏移量：

```s
0xc2f4         adrp       x8, #0x1d1000
0xc2f8         ldrsw      x8, [x8, #0x30]
```

然后我们检索它的内容，并将其向右移动两位：

```s
0xc2fc         ldr        x8, [x0, x8]
0xc300         lsr        x8, x8, #0x2
```

为什么要移位？让我们看看转储的头文件：

```objc
unsigned long long _doHardRetain:1;
unsigned long long _doWeakAccess:1;
unsigned long long _size:62;
```

原来，这三个位域共享同一个存储空间，所以要获得 `_size` 的实际值，我们必须将值右移，丢弃 `_doHardRetain` 和 `_doWeakAccess` 的位。`_doHardRetain` 和 `_doWeakAccess` 的 ivar 偏移量完全相同，但它们的位访问代码显然不同。

继续，同样的操作，我们将位于 `0x1d1034` 的 `_offset` ivar 的内容放入 `x9` 寄存器：

```s
0xc304         adrp       x9, #0x1d1000
0xc308         ldrsw      x9, [x9, #0x34]
0xc30c         ldr        x9, [x0, x9]
```

在下一行中，我们将存储在 `x2` 中的请求索引添加到右移了 2 位的 `_offset`（它也是一个 62 位宽的位域）中，然后将所有结果存回 `x9`。汇编是不是很神奇？

```s
0xc310         add        x9, x2, x9, lsr #2
```

接下来的三行是最重要的。首先，我们比较 `_size`（在 `x8` 中）与 `_offset + index`（在 `x9` 中）：

```s
0xc314         cmp        x8, x9
```

然后我们根据前一个比较的结果有条件地选择一个寄存器的值：

```s
0xc318         csel       x8, xzr, x8, hi
```

这或多或少等同于 C 中的 ?: 运算符：

```c
x8 = hi ? xzr : x8;      /* csel       x8, xzr, x8, hi */
```

`xzr` 寄存器是一个 _零寄存器_，包含值 `0`，而 `hi` 是 `csel` 指令应该检查的 [条件码](http://en.wikipedia.org/wiki/Status_register) 的名称。在这种情况下，我们检查比较结果是否为“高于”（如果 `x8` 的值大于 `x9` 的值）。

最后，我们从 `_offset + index`（在 `x9` 中）减去 `x8` 的新值，并将其再次存储在 `x8` 中：

```s
0xc31c         sub        x8, x9, x8
```

那么刚才发生了什么？首先，让我们看一下等效的 C 代码：

```objc
int tempIndex = _offset + index;        /* add        x9, x2, x9, lsr #2   */
BOOL isInRange = _size > tempIndex;     /* cmp        x8, x9   */
int diff = isInRange ? 0 : _size;       /* csel       x8, xzr, x8, hi   */
int fetchIndex = tempIndex - diff;      /* sub        x8, x9, x8   */
```

在 C 代码中，我们不需要对 `_size` 或 `_offset` 进行右移，因为编译器会自动为位域访问做这件事。

### 获取数据[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#getting-the-data)

我们快完成了。让我们将 `_list` ivar（`0x1d1038`）的内容放入 `x9` 寄存器：

```s
0xc320         adrp       x9, #0x1d1000
0xc324         ldrsw      x9, [x9, #0x38]
0xc328         ldr        x9, [x0, x9]
```

此时，`x9` 指向包含数据的内存段的起始位置。

最后，将存储在 `x8` 中的获取索引值左移 3 位，将其加到 `x9` 上，并将该位置的内存内容放入 `x0`：

```s
0xc32c         ldr        x0, [x9, x8, lsl #3]
```

这里有两点很重要。首先，每个数据偏移量都是以字节为单位的。将一个值左移 3 位相当于将其乘以 8，即 64 位架构上指针的大小。其次，结果进入 `x0`，这是存储返回 `NSUInteger` 的函数返回值的寄存器。

至此我们就完成了。我们已经获取了存储在数组中的正确值。

### 函数结尾[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#function-epilog)

剩下的是在调用前恢复寄存器状态和栈指针的一些样板操作。我们反转函数的序言并返回：

```s
0xc330         mov        sp, x29
0xc334         ldp        x29, x30, [sp], #0x10
0xc338         ret        
```

# 总结归纳[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#putting-it-all-together)

我解释了代码 _做了什么_，但现在我们要回答的问题是 _为什么_？

## ivar 的含义[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#the-meaning-of-ivars)

让我们快速总结一下每个 ivar 的含义：

- `_used` 是数量（count）
- `_list` 是指向缓冲区（buffer）的指针
- `_size` 是缓冲区的大小
- `_offset` 是存储在缓冲区中的数组的第一个元素的索引

## C 代码[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#the-c-code)

考虑到 ivar 的含义并分析了反汇编，我们现在可以编写执行完全相同操作的等效 Objective-C 代码：

```objc
- (id)objectAtIndex:(NSUInteger)index
{
    if (_used <= index) {
        goto ThrowException;
    }
    
    NSUInteger fetchOffset = _offset + index;
    NSUInteger realOffset = fetchOffset - (_size > fetchOffset ? 0 : _size);
    
    return _list[realOffset];
    
ThrowException:
    // 异常抛出代码
}
```

汇编肯定冗长得多。

## 内存布局[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#memory-layout)

最关键的部分是确定 `realOffset` 应该等于 `fetchOffset`（减去零）还是 `fetchOffset` 减去 `_size`。因为盯着枯燥的代码不一定能描绘出完美的画面，让我们考虑两个例子来说明对象获取是如何工作的。

### `_size > fetchOffset`[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#_size--fetchoffset)

在这个例子中，偏移量相对较低：

![一个简单的例子](https://ciechanow.ski/images/arrayIvars@2x.jpg)

一个简单的例子

要获取索引 `0` 处的对象，我们计算 `fetchOffset` 为 `3 + 0`。由于 `_size` 大于 `fetchOffset`，`realOffset` 也等于 `3`。代码返回 `_list[3]` 的值。获取索引 `4` 处的对象使得 `fetchOffset` 等于 `3 + 4`，代码返回 `_list[7]`。

### `_size <= fetchOffset`[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#_size--fetchoffset-1)

当偏移量很大时会发生什么？

![一个更困难的例子](https://ciechanow.ski/images/arrayIvars2@2x.jpg)

一个更困难的例子

获取索引 `0` 处的对象使得 `fetchOffset` 等于 `7 + 0`，并且调用按预期返回 `_list[7]`。然而，获取索引 `4` 处的对象使得 `fetchOffset` 等于 `7 + 4 = 11`，这大于 `_size`。要获得 `realOffset`，需要从 `fetchOffset` 中减去 `_size` 的值，使其变为 `11 - 10 = 1`，方法返回 `_list[1]`。

我们本质上是在做模运算，当跨越缓冲区边界时，_环绕_ 回到缓冲区的另一端。

## 数据结构[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#data-structure)

你可能已经猜到了，`__NSArrayM` 使用了 [环形缓冲区](http://en.wikipedia.org/wiki/Circular_buffer)。这种数据结构极其简单，但比常规的数组/缓冲区要稍微复杂一些。环形缓冲区的内容可以在到达任一端时环绕。

环形缓冲区有一些非常酷的特性。值得注意的是，除非缓冲区已满，否则从任一端插入/删除不需要移动任何内存。让我们分析该类如何利用环形缓冲区，使其行为优于 C 数组。

# __NSArrayM 的特性[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#__nsarraym-characteristics)

虽然逆向工程其余反汇编的方法会提供 `__NSArrayM` 内部结构的明确解释，但我们可以利用已发现的数据点在更高层次上研究该类。

## 运行时检查[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#inspecting-at-runtime)

要在运行时检查 `__NSArrayM`，我们不能简单地粘贴转储的头文件。首先，如果不为 `__NSArrayM` 类至少提供一个空的 `@implementation` 块，测试应用将无法链接。添加这个 `@implementation` 块可能不是一个好主意。虽然应用可以构建并实际运行，但我不完全确定运行时如何决定使用哪个类（如果你 _确实_ 知道，请告诉我）。为了安全起见，我将类名重命名为唯一的名字 - `BCExploredMutableArray`。

其次，ARC 不会让我们在未指定其所有权（ownership）的情况下编译 `id *_list` ivar。我们不会写入这个 ivar，所以在 `id` 前面加上 `__unsafe_unretained` _应该_ 不会干扰 ARC 的内存管理。但是，我选择将 ivar 声明为 `void **_list`，原因很快就会清楚。

## 输出代码[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#printout-code)

我们可以为 `NSMutableArray` 创建一个分类（category），它将打印 ivar 的内容以及数组中包含的所有指针的列表：

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
```

```objc
- (NSString *)explored_description
{
    assert([NSStringFromClass([self class]) isEqualToString:@"__NSArrayM"]);

    BCExploredMutableArray *array = (BCExploredMutableArray *)self;

    NSUInteger size = array->_size;
    NSUInteger offset = array->_offset;
    
    NSMutableString *description = [NSMutableString stringWithString:@"\n"];
    
    [description appendFormat:@"Size: %lu\n", (unsigned long)size];
    [description appendFormat:@"Count: %llu\n", (unsigned long long)array->_used];
    [description appendFormat:@"Offset: %lu\n", (unsigned long)offset];
    [description appendFormat:@"Storage: %p\n", array->_list];
    
    for (int i = 0; i < size; i++) {
        [description appendFormat:@"[%d] %p\n", i, array->_list[i]];
    }

    return description;
}
```

## 结果[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#the-results)

### 在两端插入和删除都很快[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#insertion-and-deletion-is-fast-at-both-ends)

让我们考虑一个非常简单的例子：

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
```

```objc
NSMutableArray *array = [NSMutableArray array];

for (int i = 0; i < 5; i++) {
    [array addObject:@(i)];
}

[array removeObjectAtIndex:0];
[array removeObjectAtIndex:0];

NSLog(@"%@", [array explored_description]);
```

输出显示，在索引 0 处删除对象两次只是清除了指针并相应地移动了 `_offset` ivar：

```plain
Size: 6
Count: 3
Offset: 2
Storage: 0x178245ca0
[0] 0x0
[1] 0x0
[2] 0xb000000000000022
[3] 0xb000000000000032
[4] 0xb000000000000042
[5] 0x0
```

下面是正在发生的事情的可视化解释：

![在索引 0 处删除对象两次](https://ciechanow.ski/images/arrayNSMRemove@2x.jpg)

在索引 0 处删除对象两次

那么添加对象呢？让我们在一个全新的数组上运行另一个测试：

```
1
2
3
4
5
6
```

```objc
    NSMutableArray *array = [NSMutableArray array];

    for (int i = 0; i < 4; i++) {
        [array addObject:@(i)];
    }
    [array insertObject:@(15) atIndex:0];
```

在索引 0 处插入对象利用了环形缓冲区的魔力，将新插入的对象放在缓冲区的末尾：

```plain
Size: 6
Count: 5
Offset: 5
Storage: 0x17004a560
[0] 0xb000000000000002
[1] 0xb000000000000012
[2] 0xb000000000000022
[3] 0xb000000000000032
[4] 0x0
[5] 0xb0000000000000f2
```

可视化解释：

![在索引 0 处添加对象](https://ciechanow.ski/images/arrayNSMInsert@2x.jpg)

在索引 0 处添加对象

这是极好的消息！这意味着 `__NSArrayM` 可以从 _任何一边_ 被处理。你可以将 `__NSArrayM` 用作栈（stack）或队列（queue），而没有任何性能损失。

顺便提一下，你可以看到在 64 位架构上 `NSNumber` 如何使用 [tagged pointers](http://objectivistc.tumblr.com/post/7872364181/tagged-pointers-and-fast-pathed-cfnumber-integers-in) 来进行存储。

### 非整数增长因子[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#non-integral-growth-factor)

好吧，这个我稍微作弊了。虽然我也做了一些经验测试，但我想得到精确的值，所以我偷看了 `insertObject:atIndex:` 的反汇编。每当缓冲区变满时，它会被重新分配为原来的 1.625 倍大小。对其不等于 2 我感到相当惊讶。

**更新：** Mike Curtiss [提供了](https://twitter.com/mcurtiss/status/441432739523198977) 一个 [非常好的解释](https://github.com/facebook/folly/blob/master/folly/docs/FBVector.md#memory-handling)，说明为什么使缩放因子等于 2 不是最优的。

### 一旦增长，不会缩小[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#once-grown-doesnt-shrink)

这很令人震惊——`__NSArrayM` 永远不会减小其大小！让我们运行以下测试代码：

```
1
2
3
4
5
6
```

```objc
NSMutableArray *array = [NSMutableArray array];

for (int i = 0; i < 10000; i++) {
    [array addObject:[NSObject new]];
}
[array removeAllObjects];
```

即使此时数组是空的，它仍然保留着大的缓冲区：

```plain
Size: 14336
```

除非你用 `NSMutableArray` 加载大量数据然后清除数组以释放空间，否则你不需要担心这个。

### 初始容量几乎无关紧要[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#initial-capacity-almost-doesnt-matter)

让我们分配初始容量设置为连续 2 的幂的新数组：

```
1
2
3
```

```objc
for (int i = 0; i < 16; i++) {
    NSLog(@"%@", [[[NSMutableArray alloc] initWithCapacity:1 << i] explored_description]);
}
```

惊喜惊喜：

```plain
Size:2     // 请求的容量 - 1
Size:2     // 请求的容量 - 2
Size:4     // 请求的容量 - 4
Size:8     // 请求的容量 - 8
Size:16    // 请求的容量 - 16
Size:16    // 请求的容量 - 32
Size:16    // 请求的容量 - 64
Size:16    // 请求的容量 - 128
... // Size:16 一直到底
```

### 删除时不清空指针[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#it-doesnt-clean-up-its-pointers-on-deletion)

这一点不太重要，但我发现它仍然很有趣：

```
1
2
3
4
5
6
7
8
```

```objc
NSMutableArray *array = [NSMutableArray array];

for (int i = 0; i < 6; i++) {
    [array addObject:@(i)];
}
[array removeObjectAtIndex:1];
[array removeObjectAtIndex:1];
[array removeObjectAtIndex:1];
```

输出：

```plain
Size: 6
Count: 3
Offset: 3
Storage: 0x17805be10
[0] 0xb000000000000002
[1] 0xb000000000000002
[2] 0xb000000000000002
[3] 0xb000000000000002
[4] 0xb000000000000042
[5] 0xb000000000000052
```

`__NSArrayM` 在向前移动其对象时，并不费心去清除先前的空间。然而，这些对象 _确实_ 被释放了。这也不是 `NSNumber` 在施展它的魔法，`NSObject` 的表现也类似。

这解释了我为什么选择将 `_list` ivar 定义为 `void **`。如果 `_list` 被声明为 `id *`，那么下面的循环会在 `object` 赋值时崩溃：

```objc
for (int i = 0; i < size; i++) {
    id object = array->_list[i];
    NSLog("%p", object);
}
```

ARC 隐式地插入了一个 retain/release 对，导致它访问已释放的对象。虽然在 `id object` 前面加上 `__unsafe_unretained` 可以解决这个问题，但我绝对不想要 _任何东西_ 对这堆游离指针调用任何方法。这就是我选择 `void **` 的原因。

### 最坏情况是从中间添加/删除[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#worst-case-scenario-is-addingremoving-from-the-middle)

在这两个例子中，我们将从数组的大致中间位置删除元素：

```
1
2
3
4
5
6
```

```objc
NSMutableArray *array = [NSMutableArray array];

for (int i = 0; i < 6; i++) {
    [array addObject:@(i)];
}
[array removeObjectAtIndex:3];
```

在输出中，我们看到上半部分向下移动，即向较低的索引移动（注意 `[5]` 处的游离指针）

```plain
[0] 0xb000000000000002
[1] 0xb000000000000012
[2] 0xb000000000000022
[3] 0xb000000000000042
[4] 0xb000000000000052
[5] 0xb000000000000052
```

![在索引 3 处删除对象](https://ciechanow.ski/images/arrayNSMcenterRemove@2x.jpg)

在索引 3 处删除对象

然而，当我们改为调用 `[array removeObjectAtIndex:2]` 时，下半部分向上移动，即向较高的索引移动：

```plain
[0] 0xb000000000000002
[1] 0xb000000000000002
[2] 0xb000000000000012
[3] 0xb000000000000032
[4] 0xb000000000000042
[5] 0xb000000000000052
```

![在索引 2 处删除对象](https://ciechanow.ski/images/arrayNSMcenterRemove2@2x.jpg)

在索引 2 处删除对象

在中间插入对象也有非常类似的结果。合理的解释是 `__NSArrayM` 试图最小化移动的内存量，因此它最多移动其元素的 _一半_。

## 做一个好的子类化公民[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#being-a-good-subclassing-citizen)

正如 [NSMutableArray 类参考](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSMutableArray_Class/Reference/Reference.html) 中讨论的，每个 `NSMutableArray` 子类**必须**实现以下七个方法：

- `- count`
- `- objectAtIndex:`
- `- insertObject:atIndex:`
- `- removeObjectAtIndex:`
- `- addObject:`
- `- removeLastObject`
- `- replaceObjectAtIndex:withObject:`

毫不奇怪，`__NSArrayM` 满足了这个要求。然而，`__NSArrayM` 实现的所有方法的列表相当短，并不包含 `NSMutableArray` 头文件中列出的另外 21 个方法。谁负责执行这些方法？

原来它们都是 `NSMutableArray` 类本身的一部分。这非常方便——任何 `NSMutableArray` 的子类可以只实现七个最基本的方法。所有其他更高级的抽象都建立在这些之上。例如，`- removeAllObjects` 方法简单地反向迭代，逐个调用 `- removeObjectAtIndex:`。以下是伪代码：

```
 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
```

```objc
// 我们实际上知道这是安全的，因为 count 存储在 62 位上
// 转换为 NSInteger 将 *不会* 溢出
NSInteger count = (NSInteger)[self count];
if (count == 0) {
	return;                          
}

count--;
do {
	[self removeObjectAtIndex:count];     
	count--;
} while (count >= 0);
```

然而，在合理的地方，`__NSArrayM` _确实_ 重新实现了其超类的一些方法。例如，虽然 `NSArray` 为 [NSFastEnumeration](https://developer.apple.com/library/mac/documentation/Cocoa/Reference/NSFastEnumeration_protocol/) 协议的 `- countByEnumeratingWithState:objects:count:` 方法提供了默认实现，但 `__NSArrayM` 也有自己的代码路径。知道其内部存储结构，`__NSArrayM` 可以提供更高效的实现。

# Foundation 框架[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#foundations)

我一直认为 Foundation 是 CoreFoundation 的一个薄包装。我的论点很简单——当 CF* 对应物可用时，没有必要用全新的 NS* 类实现来重新发明轮子。我震惊地发现 `NSArray` 和 `NSMutableArray` 都与 `CFArray` 毫无共同之处。

## CFArray[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#cfarray)

关于 CFArray 最好的事情是它是 [开源的](http://opensource.apple.com/source/CF/CF-855.11/CFArray.c)。这将是一个非常快速的概述，因为源代码是公开可用的，随时等待被阅读。`CFArray` 中最重要的函数是 [_CFArrayReplaceValues](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L923)。它被以下函数调用：

- [CFArrayAppendValue](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L693)
- [CFArraySetValueAtIndex](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L703)
- [CFArrayInsertValueAtIndex](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L729)
- [CFArrayRemoveValueAtIndex](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L760)
- [CFArrayReplaceValues](https://gist.github.com/Ciechan/9258194#file-cfarray-c-L918)（注意缺少前导下划线）

基本上，`CFArray` 会移动内存以适应变更，以最高效的方式，类似于 `__NSArrayM` 的工作方式。然而，`CFArray` _没有_ 使用环形缓冲区！相反，它有一个更大的缓冲区，两端用零填充，这使得枚举和获取正确的对象更容易。在任一端添加元素只是消耗剩余的填充空间。

# 结语[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsmutablearray/#final-words)

尽管 `CFArray` 必须服务于稍微更通用的目的，但我发现它的内部工作方式与 `__NSArrayM` 不同，这一点很吸引人。虽然我认为找到共同点并制作一个单一的、规范化的实现是有意义的，但也许有其他因素影响了这种分离。

它们两个有什么共同点？它们都是被称为 [双端队列（deque）](http://en.wikipedia.org/wiki/Double-ended_queue) 的抽象数据类型的具体实现。尽管名字叫 `NSMutableArray`，但它是一个增强版的数组，摆脱了 C 风格对应物的缺点。

就个人而言，我最满意的是在任一端插入/删除的常量时间性能。我不再需要质疑自己是否将 `NSMutableArray` 用作队列。它工作得非常好。
