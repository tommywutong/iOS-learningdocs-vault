---
title: 揭开 NSDictionary 的面纱 – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/exposing-nsdictionary/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6ef6e44026a9aea'
translated: true
---

> 原文：[Exposing NSDictionary – Bartosz Ciechanowski](https://ciechanow.ski/exposing-nsdictionary/)　·　Bartosz Ciechanowski

# [揭开 NSDictionary 的面纱](https://ciechanow.ski/exposing-nsdictionary/)

哈希表简直太棒了。直到今天，我仍然觉得能在常数时间内根据任意键查找对应的对象是一件神奇的事。虽然 iOS 6.0 已经引入了[显式的哈希表](http://nshipster.com/nshashtable-and-nsmaptable/)，但在实际的关联存储中，几乎都还是在使用 `NSDictionary`。

`NSDictionary` 并没有对内部实现做出任何保证。把字典数据完全随机地存储起来显然不合理，但这个假设并没有回答关键问题：`NSDictionary` 是否真的使用了哈希表？这正是我决定去探究的。

为什么不直接分析功能完备的 `NSMutableDictionary`？可变字典显然要复杂得多，需要阅读的反汇编代码量也大得吓人。而普通的 `NSDictionary` 仍然为 ARM64 反汇编带来了不小的挑战。尽管它是不可变的，但这个类的一些实现细节却非常有趣，希望能让你在接下来的阅读中获得乐趣。

这篇博文有一个[配套仓库](https://github.com/Ciechan/NSDictionaryExplorer)，里面包含讨论到的代码片段。虽然整个调查基于面向 64 位设备的 iOS 7.1 SDK，但无论是 iOS 7.0 还是 32 位设备，都不影响最终的发现。

# 这个类[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-class)

很多 Foundation 类都是类簇（class clusters），`NSDictionary` 也不例外。在很长一段时间里，`NSDictionary` 都使用 `CFDictionary` 作为其默认实现，但从 iOS 6.0 开始，情况发生了变化：

```plain
(lldb) po [[NSDictionary new] class]
__NSDictionaryI
```

和 `__NSArrayM` 类似，`__NSDictionaryI` 也位于 CoreFoundation 框架内，尽管它在公开层面上是 Foundation 的一部分。通过 class-dump 分析这个库，可以得到以下实例变量布局：

```objc
@interface __NSDictionaryI : NSDictionary
{
    NSUInteger _used:58;
    NSUInteger _szidx:6;
}
```

短得令人惊讶。似乎没有任何指向键或对象存储的指针。我们很快就会看到，`__NSDictionary` 的字面意思就是“把存储藏在自己身上”。

# 存储[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-storage)

## 实例创建[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#instance-creation)

要理解 `__NSDictionaryI` 把内容放在哪里，我们先快速浏览一下实例创建的过程。负责生成 `__NSDictionaryI` 新实例的只有一个类方法。根据 class-dump，这个方法有以下签名：

```objc
+ (id)__new:(const id *)arg1:(const id *)arg2:(unsigned long long)arg3:(_Bool)arg4:(_Bool)arg5;
```

它接受五个参数，只有第一个参数有名字。如果你要在 `@selector` 语句中使用它，它的形式会是 `@selector(__new:::::)`。前三个参数很容易推断：在这个方法上设置断点，然后查看 `x2`、`x3` 和 `x4` 寄存器的内容，它们分别包含键数组、对象数组以及键（对象）的数量。注意，与公开 API 相比，键和对象数组的顺序是相反的，公开 API 的形式是：

```objc
+ (instancetype)dictionaryWithObjects:(const id [])objects forKeys:(const id <NSCopying> [])keys count:(NSUInteger)cnt;
```

参数是定义为 `const id *` 还是 `const id []` 并不重要，因为[数组在作为函数参数时会退化为指针](http://c-faq.com/aryptr/aryptrparam.html)。

弄清楚了三个参数，我们还剩下两个未识别的布尔参数。我深入查看了一些汇编代码，结果如下：第四个参数控制是否应该复制键，最后一个参数决定是否_不_保留（retain）参数。现在我们可以用命名参数重写这个方法：

```objc
+ (id)__new:(const id *)keys :(const id *)objects :(unsigned long long)count :(_Bool)copyKeys :(_Bool)dontRetain;
```

不幸的是，我们无法直接访问这个私有方法，所以通过常规方式分配时，最后两个参数总是分别设置为 `YES` 和 `NO`。尽管如此，`__NSDictionaryI` 能够对键和对象进行更精细的控制，这仍然很有趣。

## 索引实例变量[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#indexed-ivars)

浏览 `+ __new:::::` 的反汇编代码后发现，其中既没有使用 `malloc` 也没有使用 `calloc`。相反，这个方法调用了 `__CFAllocateObject2`，第一个参数是 `__NSDictionaryI` 类，第二个参数是请求的存储大小。深入 ARM64 的代码海洋中可以看到，`__CFAllocateObject2` 做的第一件事就是用完全相同的参数调用 `class_createInstance`。

幸运的是，我们此时可以访问 Objective-C 运行时的[源代码](https://opensource.apple.com/source/objc4/objc4-551.1/)，这使得进一步的研究变得容易得多。

`class_createInstance(Class cls, size_t extraBytes)` 函数只是简单地调用了 `_class_createInstanceFromZone`，并将 `zone` 参数设为 `nil`，但这是对象分配的最终步骤。虽然该函数本身针对不同的情况有许多额外的检查，但它的核心可以用三行代码概括：

```c
_class_createInstanceFromZone(Class cls, size_t extraBytes, void *zone)
{
    ...
    size_t size = cls->alignedInstanceSize() + extraBytes;
    ...
    id obj = (id)calloc(1, size);
    ...
    return obj;
}
```

`extraBytes` 参数的名字再清晰不过了。它字面意思就是扩充默认实例大小的额外字节数。另外，请注意，正是 `calloc` 调用确保了对象分配时所有实例变量都被清零。

索引实例变量（indexed ivars）部分不过是位于常规实例变量末尾的一块额外空间：

![分配对象](https://ciechanow.ski/images/dictionaryIndexedIvars@2x.jpg)

分配对象

仅仅分配空间听起来没什么意思，所以运行时提供了一个访问器：

```objc
void *object_getIndexedIvars(id obj)
```

这个函数没有任何魔法，它只是返回一个指向索引实例变量段起始位置的指针：

![索引实例变量段](https://ciechanow.ski/images/dictionaryGetIndexedIvars@2x.jpg)

索引实例变量段

索引实例变量有几个很酷的地方。首先，每个实例可以有_不同_数量的专用额外字节。这正是 `__NSDictionaryI` 使用的特性。

其次，它们提供了更快的存储访问。这归根结底是出于[缓存友好](http://stackoverflow.com/a/16699282/558816)的考虑。一般来说，跳转到随机的内存位置（通过解引用指针）可能代价很高。由于对象刚刚被访问过（有人调用了它的方法），它的索引实例变量很可能已经进入了缓存。通过将所有需要的数据保持得非常接近，该对象可以提供尽可能好的性能。

最后，索引实例变量可以用作一种粗糙的防御措施，使对象的内部结构对 class-dump 这类工具不可见。这是一种非常基本的保护，因为一个坚定的攻击者可以在反汇编代码中查找 `object_getIndexedIvars` 调用，或者随机探测实例在常规实例变量段之后的部分来弄清楚发生了什么。

虽然功能强大，但索引实例变量有两个限制。首先，`class_createInstance` 不能在 ARC 下使用，所以你必须在类的某些部分使用 `-fno-objc-arc` 标志来编译才能使用它。其次，运行时不会在任何地方保留索引实例变量的大小信息。即使 `dealloc` 会清理所有内容（因为它内部调用了 `free`），但如果你使用了_可变_数量的额外字节，你应该在某处保留存储大小。

# 查找键并获取对象[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#looking-for-key-and-fetching-object)

## 分析汇编[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#analyzing-assembly)

虽然此时我们可以通过探查 `__NSDictionaryI` 实例来弄清楚它们的工作原理，但最终的真相在于汇编代码。我们不打算通读整面 ARM64 汇编代码，而是讨论等价的 Objective-C 代码。

这个类本身实现了很少的方法，但我认为最重要的是 `objectForKey:`——这就是我们要详细讨论的内容。既然我已经做了汇编分析，你可以在[单独的页面](https://ciechanow.ski/extra/objectforkeyassembly/index.html)上阅读它。内容很密集，但仔细阅读后应该能让你相信下面的代码或多或少是正确的。

## C 代码[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#the-c-code)

不幸的是，我无法访问 Apple 的代码库，所以下面逆向工程得到的代码与原始实现并_不_完全相同。另一方面，它似乎工作得很好，而且我还没有发现任何边界情况下的行为与原始方法不同。

以下代码是从 `__NSDictionaryI` 类的角度编写的：

```objc
- (id)objectForKey:(id)aKey
{
    NSUInteger sizeIndex = _szidx;
    NSUInteger size = __NSDictionarySizes[sizeIndex];
    
    id *storage = (id *)object_getIndexedIvars(dict);
    
    NSUInteger fetchIndex = [aKey hash] % size;
    
    for (int i = 0; i < size; i++) {
        id fetchedKey = storage[2 * fetchIndex];

        if (fetchedKey == nil) {
            return nil;
        }
        
        if (fetchedKey == aKey || [fetchedKey isEqual:aKey]) {
            return storage[2 * fetchIndex + 1];
        }

        fetchIndex++;
        
        if (fetchIndex == size) {
            fetchIndex = 0;
        }
    }
    
    return nil;
}
```

当你仔细查看 C 代码时，可能会注意到键的获取方式有些奇怪。它总是在偶数偏移位置获取，而返回的对象位于下一个索引。这清楚地揭示了 `__NSDictionaryI` 的内部存储方式——它交替存储键和对象：

![键和对象交替存储](https://ciechanow.ski/images/dictionaryLayout@2x.jpg)

键和对象交替存储

**更新：** Joan Lluch [提供](#comment-1345004966)了一个非常有说服力的解释来解释这种布局。原始代码可能使用了非常简单的结构体数组：

```objc
struct KeyObjectPair {
    id key;
    id object;
};
```

`objectForKey:` 方法非常直接，我强烈建议你用心走一遍。不过，还是有几点值得指出。首先，`_szidx` 实例变量被用作 `__NSDictionarySizes` 数组的索引，因此它很可能代表“大小索引”。

其次，传入的键上唯一调用的方法是 `hash`。用键的哈希值除以字典大小得到的余数，用于计算索引实例变量段内的偏移量。

如果偏移量处的键是 `nil`，我们就直接返回 `nil`，工作完成：

![当键槽为空时，返回 nil](https://ciechanow.ski/images/dictionaryMiss@2x.jpg)

当键槽为空时，返回 nil

然而，如果偏移量处的键不是 `nil`，则可能发生两种情况。如果键相等，则返回相邻的对象。如果它们不相等，则发生了哈希碰撞，我们必须继续向后查找。`__NSDictionaryI` 只是继续查找，直到找到匹配项或 `nil`：

![一次碰撞后找到键](https://ciechanow.ski/images/dictionaryHit@2x.jpg)

一次碰撞后找到键

这种搜索方式被称为[线性探测 (linear probing)](http://en.wikipedia.org/wiki/Linear_probing)。注意 `__NSDictionaryI` 是如何在到达存储末尾时回绕 `fetchIndex` 的。`for` 循环用于限制检查次数——如果存储已满且缺少循环条件，我们将无限查找下去。

## __NSDictionarySizes 与 __NSDictionaryCapacities[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#__nsdictionarysizes--__nsdictionarycapacities)

我们已经知道 `__NSDictionarySizes` 是一个存储 `__NSDictionaryI` 不同可能大小的数组。我们可以推断它是一个 `NSUInteger` 数组，确实，如果我们让 Hopper 将这些值视为 64 位无符号整数，它就突然变得非常有意义了：

```s
___NSDictionarySizes:
0x00000000001577a8         dq         0x0000000000000000
0x00000000001577b0         dq         0x0000000000000003
0x00000000001577b8         dq         0x0000000000000007
0x00000000001577c0         dq         0x000000000000000d
0x00000000001577c8         dq         0x0000000000000017
0x00000000001577d0         dq         0x0000000000000029
0x00000000001577d8         dq         0x0000000000000047
0x00000000001577e0         dq         0x000000000000007f
...
```

以更熟悉的十进制形式表示，它呈现为一个漂亮的 64 个质数列表，起始序列如下：0, 3, 7, 13, 23, 41, 71, 127。注意，这些不是连续的质数，这就引出了一个问题：相邻两个数的平均比率是多少？实际上大约是 `1.637`——非常接近 `1.625`，后者是 `NSMutableArray` 的增长因子。关于为何使用质数作为存储大小的细节，[这个 Stack Overflow 回答](http://stackoverflow.com/a/1147232/558816)是一个很好的起点。

我们已经知道 `__NSDictionaryI` 可以拥有多大的存储空间，但它是如何在初始化时知道该选哪一个大小索引的呢？答案在于前面提到的 `+ __new:::::` 类方法中。将汇编的部分内容转换回 C 语言，可以得到以下代码：

```objc
int szidx;
for (szidx = 0; szidx < 64; szidx++) {
    if (__NSDictionaryCapacities[szidx] >= count) {
        break;
    }
}

if (szidx == 64) {
    goto fail;
}
```

该方法线性地遍历 `__NSDictionaryCapacities` 数组，直到 `count` 能容纳到该大小中。快速查看 Hopper 可以看到数组的内容：

```s
___NSDictionaryCapacities:
0x00000000001579b0         dq         0x0000000000000000
0x00000000001579b8         dq         0x0000000000000003
0x00000000001579c0         dq         0x0000000000000006
0x00000000001579c8         dq         0x000000000000000b
0x00000000001579d0         dq         0x0000000000000013
0x00000000001579d8         dq         0x0000000000000020
0x00000000001579e0         dq         0x0000000000000034
0x00000000001579e8         dq         0x0000000000000055
...
```

转换为十进制得到 0, 3, 6, 11, 19, 32, 52, 85 等等。注意这些数字_小于_之前列出的质数。如果你要往 `__NSDictionaryI` 中放入 32 个键值对，它会为 41 个键值对分配空间，保守地保留了一些空槽位。这有助于减少哈希碰撞的次数，使查找时间尽量接近常数。除了 3 个元素这种微不足道的情况外，`__NSDictionaryI` 的存储永远不会占满，平均填充率最多为 62%。

作为一条冷知识，`__NSDictionaryCapacities` 的最后一个非空值是 0x11089481C742，即十进制的 18728548943682。你很难_不_把键值对数量限制用满，至少在 64 位架构上是这样。

### 非导出符号[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#non-exported-symbols)

如果你想在代码中通过将 `__NSDictionarySizes` 声明为 `extern` 数组来使用它，你很快就会意识到这并不容易。代码会因为链接器错误而无法编译——`__NSDictionarySizes` 符号未定义。使用 nm 工具检查 CoreFoundation 库：

```bash
nm CoreFoundation | grep ___NSDictionarySizes
```

……清楚地表明这些符号是存在的（分别针对 ARMv7、ARMv7s 和 ARM64）：

```bash
00139c80 s ___NSDictionarySizes
0013ac80 s ___NSDictionarySizes
0000000000156f38 s ___NSDictionarySizes
```

不幸的是，nm 手册明确说明：

> 如果符号是局部的（非外部的），则符号的类型由相应的小写字母表示。

`__NSDictionarySizes` 的符号根本没有被导出——它们是为库的内部使用而设计的。我做了一些研究，试图弄清楚是否有可能与非导出的符号进行链接，但显然这是不可能的（_请_告诉我如果可能的话！）。我们无法访问它们。也就是说，我们无法轻松访问它们。

### 偷偷潜入[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#sneaking-in)

这里有一个有趣的观察：在 iOS 7.0 和 7.1 中，`kCFAbsoluteTimeIntervalSince1904` 常量正好被布局在 `__NSDictionarySizes`_之前_：

```s
_kCFAbsoluteTimeIntervalSince1904:
0x00000000001577a0         dq         0x41e6ceaf20000000
___NSDictionarySizes:
0x00000000001577a8         dq         0x0000000000000000
```

关于 `kCFAbsoluteTimeIntervalSince1904` 最棒的一点是，它_是_被导出的！我们将这个常量的地址加上 8 个字节（`double` 的大小），然后将结果重新解释为指向 `NSUInteger` 的指针：

```objc
NSUInteger *Explored__NSDictionarySizes = (NSUInteger *)((char *)&kCFAbsoluteTimeIntervalSince1904 + 8);
```

然后我们可以通过方便的索引来访问它的值：

```objc
(lldb) p Explored__NSDictionarySizes[0]
(NSUInteger) $0 = 0
(lldb) p Explored__NSDictionarySizes[1]
(NSUInteger) $1 = 3
(lldb) p Explored__NSDictionarySizes[2]
(NSUInteger) $2 = 7
```

这个技巧非常脆弱，很可能在将来失效，但这只是一个测试项目，所以完全没问题。

# __NSDictionaryI 的特性[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#__nsdictionaryi-characteristics)

既然我们已经发现了 `__NSDictionaryI` 的内部结构，我们就可以利用这些信息来弄清楚为什么事物会像它们那样工作，以及当前 `__NSDictionaryI` 的实现会带来哪些不可预见的后果。

## 打印代码[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#printout-code)

为了让我们的调查稍微容易一点，我们将创建一个辅助的 `NSDictionary` 分类方法，用于打印实例的内容：

```objc
- (NSString *)explored_description
{
    assert([NSStringFromClass([self class]) isEqualToString:@"__NSDictionaryI"]);
    
    BCExploredDictionary *dict = (BCExploredDictionary *)self;

    NSUInteger count = dict->_used;
    NSUInteger sizeIndex = dict->_szidx;
    NSUInteger size = Explored__NSDictionarySizes[sizeIndex];
    
    __unsafe_unretained id *storage = (__unsafe_unretained id *)object_getIndexedIvars(dict);
    
    NSMutableString *description = [NSMutableString stringWithString:@"\n"];
    
    [description appendFormat:@"Count: %lu\n", (unsigned long)count];
    [description appendFormat:@"Size index: %lu\n", (unsigned long)sizeIndex];
    [description appendFormat:@"Size: %lu\n", (unsigned long)size];

    for (int i = 0; i < size; i++) {
        [description appendFormat:@"[%d] %@ - %@\n", i, [storage[2*i] description], [storage[2*i + 1] description]];
    }
    
    return description;
}
```

## 枚举时键/对象的顺序与存储中的键/对象顺序相同[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#order-of-keysobjects-on-enumeration-is-the-same-as-order-of-keysobjects-in-storage)

让我们创建一个包含四个值的简单字典：

```objc
NSDictionary *dict = @{@1 : @"Value 1",
                       @2 : @"Value 2",
                       @3 : @"Value 3",
                       @4 : @"Value 4"};

NSLog(@"%@", [dict explored_description]);
```

`explored_description` 的输出是：

```plain
Count: 4
Size index: 2
Size: 7
[0] (null) - (null)
[1] 3 - Value 3
[2] (null) - (null)
[3] 2 - Value 2
[4] (null) - (null)
[5] 1 - Value 1
[6] 4 - Value 4
```

有了这个，让我们快速枚举一下字典：

```objc
[dict enumerateKeysAndObjectsUsingBlock:^(id key, id obj, BOOL *stop) {
    NSLog(@"%@ - %@", key, obj);
}];
```

输出是：

```plain
3 - Value 3
2 - Value 2
1 - Value 1
4 - Value 4
```

枚举似乎只是简单地遍历存储，忽略 `nil` 键，只对非空槽位调用 block。对于快速枚举、`keyEnumerator`、`allKeys` 和 `allValues` 方法也是如此。这完全合理。`NSDictionary` 是无序的，所以以什么顺序提供键和值并不重要。使用内部布局是最简单、也可能是最快的选择。

## 如果你搞砸了，__NSDictionaryI 可能会为 nil 键返回某些内容[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#if-you-mess-up-__nsdictionaryi-may-return-something-for-nil-key)

让我们考虑一个例子。假设我们正在构建一个简单的太空 3D 策略游戏。整个宇宙被分割成立方体状的扇区，虚构的派系可以在这些扇区上进行争夺。一个扇区可以通过其 `i`、`j` 和 `k` 索引来引用。我们不应该使用 3D 数组来存储扇区信息——游戏空间巨大，而且大部分是空的，所以存储 `nil` 指针会浪费内存。相反，我们将使用一个采用 `NSDictionary` 形式的稀疏存储（sparse storage），并带有一个自定义的键类，使得查询给定位置是否有东西变得非常容易。

以下是键类 `BC3DIndex` 的接口：

```objc
@interface BC3DIndex : NSObject <NSCopying>

@property (nonatomic, readonly) NSUInteger i, j, k; // 你实际上可以这样做

- (instancetype)initWithI:(NSUInteger)i j:(NSUInteger)j k:(NSUInteger)k;

@end
```

以及同样简单的实现：

```objc
@implementation BC3DIndex

- (instancetype)initWithI:(NSUInteger)i j:(NSUInteger)j k:(NSUInteger)k
{
    self = [super init];
    if (self) {
        _i = i;
        _j = j;
        _k = k;
    }
    return self;
}

- (BOOL)isEqual:(BC3DIndex *)other
{
    return other.i == _i && other.j == _j && other.k == _k;
}

- (NSUInteger)hash
{
    return _i ^ _j ^ _k;
}

- (id)copyWithZone:(NSZone *)zone
{
    return self; // 我们不可变，所以没问题
}

@end
```

注意，我们是如何成为一个合格的子类化公民的：我们同时实现了 `isEqual:` 和 `hash` 方法，并确保如果两个 3D 索引相等，那么它们的哈希值也相等。对象相等性的要求_确实_得到了满足。

这里有一个小问题：以下代码会打印什么？

```objc
NSDictionary *indexes = @{[[BC3DIndex alloc] initWithI:2 j:8 k:5] : @"A black hole!",
                          [[BC3DIndex alloc] initWithI:0 j:0 k:0] : @"Asteroids!",
                          [[BC3DIndex alloc] initWithI:4 j:3 k:4] : @"A planet!"};

NSLog(@"%@", [indexes objectForKey:nil]);
```

应该是 `(null)` 对吗？不：

```plain
Asteroids!
```

为了进一步调查，让我们获取字典的描述：

```c
Count: 3
Size index: 1
Size: 3
[0] <BC3DIndex: 0x17803d340> - A black hole!
[1] <BC3DIndex: 0x17803d360> - Asteroids!
[2] <BC3DIndex: 0x17803d380> - A planet!
```

事实证明，`__NSDictionaryI` 并不检查传入 `objectForKey:` 的 `key` 是否为 `nil`（我认为这是一个_好的_设计决策）。对 `nil` 调用 `hash` 方法返回 `0`，这导致该类将索引 `0` 处的键与 `nil` 进行比较。这一点很重要：执行 `isEqual:` 方法的是_存储的_键，而不是传入的键。

第一次比较失败了，因为“A black hole!”的 `i` 索引是 `2`，而 `nil` 的是零。键不相等，这导致字典继续查找，遇到了另一个存储的键：即“Asteroids!”的那个。这个键的所有三个属性 `i`、`j`、`k` 都等于 `0`，而这正是 `nil` 在被询问其属性时（通过 `objc_msgSend` 内部的 `nil` 检查）也会返回的值。

这就是问题的核心。`BC3DIndex` 的 `isEqual:` 实现，在某些条件下，可能会对 `nil` 比较返回 `YES`。如你所见，这是一种非常危险的行为，很容易把事情搞砸。_始终_确保你的对象不等于 `nil`。

## 一个辅助键类[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#a-helper-key-class)

对于接下来的两个测试，我们将构建一个特殊的键类，它具有可配置的哈希值，并在执行 `hash` 和 `isEqual:` 方法时将信息打印到控制台。

这是它的接口：

```objc
@interface BCNastyKey : NSObject <NSCopying>

@property (nonatomic, readonly) NSUInteger hashValue;

+ (instancetype)keyWithHashValue:(NSUInteger)hashValue;

@end
```

以及实现：

```objc
@implementation BCNastyKey

+ (instancetype)keyWithHashValue:(NSUInteger)hashValue
{
    return [[BCNastyKey alloc] initWithHashValue:hashValue];
}

- (instancetype)initWithHashValue:(NSUInteger)hashValue
{
    self = [super init];
    if (self) {
        _hashValue = hashValue;
    }
    return self;
}

- (id)copyWithZone:(NSZone *)zone
{
    return self;
}

- (NSUInteger)hash
{
    NSLog(@"Key %@ is asked for its hash", [self description]);

    return _hashValue;
}

- (BOOL)isEqual:(BCNastyKey *)object
{
    NSLog(@"Key %@ equality test with %@: %@", [self description], [object description], object == self ? @"YES" : @"NO");

    return object == self;
}

- (NSString *)description
{
    return [NSString stringWithFormat:@"(&:%p #:%lu)", self, (unsigned long)_hashValue];
}

@end
```

这个键很糟糕：我们只与自身相等，但却返回任意的哈希值。注意，这_没有_违反相等性约定。

## 匹配键不一定需要调用 `isEqual`[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#isequal-doesnt-have-to-be-called-to-match-the-key)

让我们创建一个键和一个字典：

```objc
BCNastyKey *key = [BCNastyKey keyWithHashValue:3];
NSDictionary *dict = @{key : @"Hello there!"};
```

以下调用：

```c
[dict objectForKey:key];
```

在控制台打印出：

```plain
Key (&:0x17800e240 #:3) is asked for its hash
```

如你所见，`isEqual:` 方法并没有被调用。这非常酷！由于大多数键都是 `NSString` 字面量，它们在整个应用程序中共享_相同的_地址。即使键是一个非常长的字符串字面量，`__NSDictionaryI` 也不会执行可能耗时的 `isEqual:` 方法，除非绝对必要。而且由于 64 位架构引入了 tagged pointers，一些 `NSNumber`、`NSDate` 和[显然](https://twitter.com/Catfish_Man/status/393238389266194434) `NSIndexPath` 的实例也因此受益于这种优化。

## 最坏情况性能是线性的[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#worst-case-performance-is-linear)

让我们创建一个非常简单的测试用例：

```objc
BCNastyKey *targetKey = [BCNastyKey keyWithHashValue:36];

NSDictionary *b = @{[BCNastyKey keyWithHashValue:1] : @1,
                    [BCNastyKey keyWithHashValue:8] : @2,
                    [BCNastyKey keyWithHashValue:15] : @3,
                    [BCNastyKey keyWithHashValue:22] : @4,
                    [BCNastyKey keyWithHashValue:29] : @5,
                    targetKey : @6
                    };
```

一行关键的代码：

```objc
NSLog(@"Result: %@", [[b objectForKey:targetKey] description]);
```

揭示了灾难：

```plain
Key (&:0x170017640 #:36) is asked for its hash
Key (&:0x170017670 #:1) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017660 #:8) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017680 #:15) equality test with (&:0x170017640 #:36): NO
Key (&:0x1700176e0 #:22) equality test with (&:0x170017640 #:36): NO
Key (&:0x170017760 #:29) equality test with (&:0x170017640 #:36): NO
Result: 6
```

这是一个极其病态的情况——字典中的每一个键都经过了相等性测试。尽管每个哈希值都不同，但它们仍然与所有其他键碰撞，因为这些键的哈希值在模 7 下彼此[同余 (congruent modulo)](http://en.wikipedia.org/wiki/Modular_arithmetic#Congruence_relation)，而 7 恰好是这个字典的存储大小。

如前所述，注意最后一次 `isEqual:` 测试缺失了。`__NSDictionaryI` 只是简单地比较了指针，并确定它必须是同一个键。

你是否应该担心这种线性时间查找？完全不必。我不太擅长哈希分布的统计分析，但你得_极其_倒霉才会让你的所有哈希值都与字典的大小模同余。总会发生一些碰撞，这是哈希表的本质，但你很可能永远不会遇到线性时间的问题。也就是说，除非你把 `hash` 函数搞砸了。

# 结语[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/exposing-nsdictionary/#final-words)

`__NSDictionaryI` 竟然如此简单，这让我着迷。不用说，这个类当然达成了它的目的，而且没有必要把事情搞得太复杂。对我来说，实现中最美妙的部分是键-对象-键-对象的布局。这是一个绝妙的想法。

如果要从这篇文章中带走一条建议，那么我会选择留意你的 `hash` 和 `isEqual:` 方法。诚然，很少有人会编写自定义的键类用于字典，但这些规则同样适用于 `NSSet`。

我知道在将来的某个时候，`NSDictionary` 会发生变化，我的发现也将过时。将当前的实现细节内化，可能会成为未来的负担，因为那时记忆中的假设将不再适用。然而，就在此时此刻，了解事物的运作方式本身就是一件非常有趣的事情，希望你也能分享我的兴奋之情。
