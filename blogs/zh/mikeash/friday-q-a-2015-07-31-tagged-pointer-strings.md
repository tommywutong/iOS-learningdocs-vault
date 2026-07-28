---
title: 'Friday Q&A 2015-07-31：Tagged Pointer Strings'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35c80e270ee2896b'
translated: true
---

> 原文：[Friday Q&A 2015-07-31: Tagged Pointer Strings](https://www.mikeash.com/pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)　·　mikeash.com Friday Q&A

发布于 2015-07-31 14:10 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2015-08-14: An Xcode Plugin for Unsmoothed Text](https://www.mikeash.com/pyblog/friday-qa-2015-08-14-an-xcode-plugin-for-unsmoothed-text.html)  
上一篇文章：[Friday Q&A 2015-07-17: When to Use Swift Structs and Classes](https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2015-07-31：Tagged Pointer Strings

作者：[Mike Ash](https://www.mikeash.com/)

**回顾**  
对象在内存中对齐，其地址至少总是指针大小的整数倍，实际上通常都是 `16` 的倍数。对象指针以完整的 64 位整数存储，但这种对齐意味着某些位将始终为零。

tagged pointer 利用了这一事实，给那些位**不**为零的对象指针赋予了特殊含义。在 Apple 的 64 位 Objective-C 实现中，最低有效位被设置为 1（也就是奇数）的对象指针被视为 tagged pointer。它不再通过标准的 `isa` 解引用来确定类，而是将接下来的三个位作为索引，查找 tagged class 表。该索引用于获取 tagged pointer 的类。剩下的 `60` 位则留给 tagged class 随意使用。

一个简单的用法是，让合适的 `NSNumber` 实例成为 tagged pointer，用额外的 `60` 位来保存数值。最低位将被设置为 `1`。接下来的三个位将被设置为 `NSNumber` tagged class 对应的索引。之后的 `60` 位就可以用来保存，例如，任何能放进这个空间的整数值。

从外部来看，这样的指针看起来和行为方式与其他对象无异。它像其他对象一样响应消息，因为 `objc_msgSend` 知道 tagged pointer。如果你向它请求 `integerValue`，它会从那些 `60` 位中提取数据并返回给你。然而，你节省了一次内存分配，每次访问时省去了一个指针间接引用，而且引用计数可以是一个空操作，因为没有需要释放的内存。对于常用类来说，这可以带来显著的性能提升。

`NSString` 看起来不像是一个好的 tagged pointer 候选，因为它长度可变，并且可能比 tagged pointer 中的 `60` 位要长得多。然而，tagged class 可以与普通类共存，对一些值使用 tagged pointer，对另一些值使用普通指针。例如，对于 `NSNumber`，任何大于 `2^60 - 1` 的整数都无法放进 tagged pointer，而需要存储在内存中分配的普通 `NSNumber` 对象中。只要创建对象的代码编写得当，这一切都能正常工作。

`NSString` 可以做同样的事情。对于能放进 `60` 位的字符串，它可以创建一个 tagged pointer。其他字符串则会被放在普通对象中。这假设小字符串的使用频率足够高，以至于能带来显著的性能提升。在实际代码中，情况真的如此吗？看起来 Apple 认为是这样的，因为他们已经付诸实施。

**可能的实现方式**  
在我们查看 Apple 的做法之前，让我们先花点时间思考一下我们可以如何实现 tagged string 存储。基础很简单：将最低位设为 1，将接下来的几个位设为对应的 tagged class 索引，将剩下的位设为任意值。如何使用剩下的位是个大问题。我们想要最大化利用可用的 `60` 位。

一个 Cocoa 字符串在概念上是一个 Unicode 代码点的序列。有 1,112,064 个有效的 Unicode 代码点，所以一个代码点需要 `21` 位来表示。这意味着我们可以在这些 `60` 位中放入两个代码点，并且会浪费 `18` 位。我们可以借用一些额外的位来保存长度，这样 tagged string 可以是零个、一个或两个代码点。然而，限制在只有两个代码点似乎没什么用。

`NSString` API 实际上是基于 `UTF-16` 实现的，而不是原始的 Unicode 代码点。`UTF-16` 将 Unicode 表示为一个 `16` 位值的序列。最常见的代码点，位于基本多语言平面（BMP）内，适合单个 `16` 位值，而大于 65,535 的代码点则需要两个。我们可以将三个 `16` 位值放入可用的 `60` 位中，剩下 `12` 位。借用一些位作为长度将允许我们表示 0-3 个 `UTF-16` 代码单元。这将允许最多三个 BMP 内的代码点，以及一个 BMP 之外的代码点（再加上，可选地，一个 BMP 内的代码点）。不过，限制在三个仍然很紧凑。

大多数 App 中的字符串可能是 ASCII 的。即使 App 被本地化为非 ASCII 语言，字符串的用途也远不止显示 UI。它们用于 URL 组件、文件扩展名、对象键、plist 值等等。`UTF-8` 编码是一种兼容 ASCII 的编码，它将每个 ASCII 字符编码为单个字节，同时对其他 Unicode 代码点使用最多四个字节。我们可以在分配给我们的 `60` 位中放入七个字节，剩下 `4` 位用作长度。这使得我们的 tagged string 可以容纳七个 ASCII 字符，或者稍微少一些的非 ASCII 字符，具体取决于它们是什么。

如果我们针对 ASCII 进行优化，我们不妨完全放弃完整的 Unicode 支持。毕竟，包含非 ASCII 字符的字符串可以使用真正的对象。ASCII 是一种七位编码，那么如果我们每个字符只分配 `7` 位呢？这让我们可以在可用的 `60` 位中存储多达八个 ASCII 字符，并剩余 `4` 位用于长度。这开始听起来有用了。一个 App 中可能有很多字符串是纯 ASCII 且包含八个或更少的字符。

我们能更进一步吗？完整的 ASCII 范围包含了很多不常用的东西。例如，有很多控制字符以及不常见的符号。字母数字字符构成了使用的大部分内容。我们能塞进 `6` 位吗？

`6` 位可以得到 `64` 个可能的值。ASCII 字母表中有 `26` 个字母。包括大写和小写会增加到 `52`。包括所有数字 0-9 会增加到 `62`。还剩下两个位置，我们可以分配给，比如说，空格和句点。可能有很多字符串只包含这些字符。在每个 `6` 位的情况下，我们可以在 `60` 位的存储空间中放入十个！但是等等！我们没有任何剩余位来存储长度了。所以要么我们存储九个字符加上一个长度，要么我们去掉 `64` 个可能值中的一个（我提名空格出局），并对短于十个字符的字符串使用零作为终止符。

`5` 位呢？这并非完全荒谬。例如，可能有很多字符串只是小写字母。`5` 位给出 `32` 个可能的值。如果你包含整个小写字母表，会有 `6` 个额外的值，你可以将它们分配给更常见的大写字母，或者一些符号，或者数字，或者混合。如果你发现其中一些其他可能性更常见，你甚至可以移除一些不常见的小写字母，比如 `q`。如果我们为长度留出空间，每个字符 `5` 位可以得到十一个字符；如果我们借用了一个符号并使用终止符，则可以得到十二个字符。

我们能更进一步吗？对于固定大小的字母表来说，`5` 位已经差不多到了极限。你可以改用可变长度编码，例如使用 [Huffman 编码](https://en.wikipedia.org/wiki/Huffman_coding)。这将允许常见的字母 `e` 用比字母 `q` 更少的位来编码。在不太可能的情况下，如果你的字符串全是 `e`，这可能使得每个字符只需要 `1` 位。但这也带来了更复杂且可能更慢的代码作为代价。

Apple 采用了哪种方法？让我们来一探究竟。

**演练 tagged string**  
下面是一段代码，用于创建一个 tagged string 并打印其指针值：

```
    NSString *a = @"a";
    NSString *b = [[a mutableCopy] copy];
    NSLog(@"%p %p %@", a, b, object_getClass(b));
```

`mutableCopy`/`copy` 的转换是必要的，原因有二。首先，虽然像 `@"a"` 这样的字符串可以存储为 tagged pointer，但常量字符串永远不会是 tagged pointer。常量字符串必须在操作系统版本间保持二进制兼容，但 tagged pointer 的内部细节是不保证的。只要 tagged pointer 总是由 Apple 的代码在运行时生成，这就可以正常工作，但如果编译器将它们嵌入到你的二进制文件中（就像常量字符串的情况那样），它就会出问题。因此，我们需要复制常量字符串以获得 tagged pointer。

`mutableCopy` 是必要的，因为 `NSString` 对我们来说太聪明了，它知道不可变字符串的 `copy` 是一个无意义的操作，并将原始字符串作为 "copy" 返回。常量字符串是不可变的，所以 `[a copy]` 的结果就是 `a`。一个 mutable copy 强制它进行实际复制，然后对结果进行不可变 copy 就足以让系统给我们一个 tagged pointer string。

注意，你绝对不要在自己的代码中依赖这些细节！`NSString` 代码决定给你一个 tagged pointer 的情况随时可能改变，如果你编写了依赖它的代码，那段代码最终会出问题。幸运的是，你需要特意去做才能实现这一点，所有正常、合理的代码都能正常工作，完全不知道 tagged pointer 的存在。

以下是在我的电脑上上述代码打印的内容：

```
    0x10ba41038 0x6115 NSTaggedPointerString
```

你可以先看到原始指针，一个漂亮的整数，表明是对象指针。副本是第二个值，其 tagged 特性非常明显。它是一个奇数，这意味着它不可能是有效的对象指针。它也是一个很小的数字，完全在 64 位 Mac 地址空间开头那不可映射的 4GB 零页内，这使得它更加不可能是对象指针。

我们能从这个 `0x6115` 的值中推断出什么？我们知道底部四个位是 tagged pointer 机制本身的一部分。最低的半字节 `5` 在二进制中是 `0101`。最低的一位表明它是一个 tagged pointer。接下来的三个位表明 tagged class。这里这些位是 `010`，表明 tagged string class 占据索引 `2`。不过这个信息也没什么用。

开头的 `61` 很有暗示性。十六进制的 `61` 恰好是小写字母 `a` 的 ASCII 值，这正是字符串包含的内容。看起来这里使用的是直接的 ASCII 编码。方便！

类名清楚地表明了此类的作用，并为我们研究实现此功能的实际代码提供了一个很好的起点。我们稍后会讨论这个问题，但先让我们从外部做一些更深入的检查。

下面是一个循环，用于构建形式为 `abcdef...` 的字符串，并逐个打印，直到它不再返回 tagged pointer：

```
    NSMutableString *mutable = [NSMutableString string];
    NSString *immutable;
    char c = 'a';
    do {
        [mutable appendFormat: @"%c", c++];
        immutable = [mutable copy];
        NSLog(@"0x%016lx %@ %@", immutable, immutable, object_getClass(immutable));
    } while(((uintptr_t)immutable & 1) == 1);
```

第一次迭代打印：

```
    0x0000000000006115 a NSTaggedPointerString
```

这与我们上面看到的相符。注意，我打印的是完整的指针，包含所有前导零，以便在比较后续迭代时更清晰。让我们与第二次迭代比较：

```
    0x0000000000626125 ab NSTaggedPointerString
```

底部的四个位没有改变，正如我们所料。那个 `5` 将保持不变，始终表明这是一个 `NSTaggedPointerString` 类型的 tagged pointer。

原来的 `61` 保持在原位，现在旁边多了一个 `62`。`62` 当然是 `b` 的 ASCII 码，所以我们可以看到这种编码是使用 ASCII 的八位编码。终端 `5` 之前的四个位从 `1` 变成了 `2`，表明这可能就是长度。后续迭代证实了这一点：

```
    0x0000000063626135 abc NSTaggedPointerString
    0x0000006463626145 abcd NSTaggedPointerString
    0x0000656463626155 abcde NSTaggedPointerString
    0x0066656463626165 abcdef NSTaggedPointerString
    0x6766656463626175 abcdefg NSTaggedPointerString
```

大概这就是结束了。tagged pointer 满了，下一次迭代将分配一个对象并终止循环。对吧？错！

```
    0x0022038a01169585 abcdefgh NSTaggedPointerString
    0x0880e28045a54195 abcdefghi NSTaggedPointerString
    0x00007fd275800030 abcdefghij __NSCFString
```

循环在终止前又进行了两次迭代。长度部分继续增加，但 tagged pointer 的其余部分变成了乱码。这是怎么回事？让我们转向实现来找出答案。

**反汇编**  
`NSTaggedPointer` 类位于 CoreFoundation 框架中。它似乎应该位于 Foundation 中，但如今许多核心 Objective-C 类已经移到了 CoreFoundation，因为 Apple 逐渐放弃将 CoreFoundation 作为一个独立的实体。

让我们先看看 `-[NSTaggedPointerString length]` 的实现：

```
    push       rbp
    mov        rbp, rsp
    shr        rdi, 0x4
    and        rdi, 0xf
    mov        rax, rdi
    pop        rbp
    ret
```

Hopper 提供了这个方便的代码反编译：

```
    unsigned long long -[NSTaggedPointerString length](void * self, void * _cmd) {
        rax = self >> 0x4 & 0xf;
        return rax;
    }
```

简而言之，要获取长度，提取第 4-7 位并返回它们。这证实了我们上面的观察，即终端 `5` 之前的四个位表明字符串的长度。

`NSString` 子类的另一个基本方法是 `characterAtIndex:`。我将跳过冗长的反汇编，直接看 Hopper 反编译的输出，它非常可读：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long arg2) {
        rsi = _cmd;
        rdi = self;
        r13 = arg2;
        r8 = ___stack_chk_guard;
        var_30 = *r8;
        r12 = rdi >> 0x4 & 0xf;
        if (r12 >= 0x8) {
                rbx = rdi >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = r12;
                if (r12 < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (r12 <= r13) {
                rbx = r8;
                ___CFExceptionProem(rdi, rsi);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + r13 + 0xffffffffffffffc0) & 0xff;
        if (*r8 != var_30) {
                rax = __stack_chk_fail();
        }
        return rax;
    }
```

让我们稍微清理一下。前三行只是 Hopper 告诉我们哪个寄存器对应哪个参数。让我们继续将所有 `rsi` 的用法替换为 `_cmd`，所有 `rdi` 的用法替换为 `self`。`arg2` 实际上是 `index` 参数，所以让我们将所有 `r13` 的用法替换为 `index`。我们将去掉 `__stack_chk` 相关的东西，因为它只是一个安全加固措施，与方法实际工作无关。以下是按这种方式清理后的代码：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        r12 = self >> 0x4 & 0xf;
        if (r12 >= 0x8) {
                rbx = self >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = r12;
                if (r12 < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (r12 <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

在第一个 `if` 语句之前是这行代码：

```
    r12 = self >> 0x4 & 0xf
```

我们可以将其识别为与我们在 `-length` 实现中看到的相同的长度提取代码。让我们继续将整个代码中的 `r12` 替换为 `length`：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                rbx = self >> 0x8;
                rcx = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                rdx = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x3f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x6;
                        } while (rdx != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + rdx + 0xffffffffffffffbf) = *(int8_t *)((rbx & 0x1f) + rcx);
                                rdx = rdx - 0x1;
                                rbx = rbx >> 0x5;
                        } while (rdx != 0x0);
                }
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

查看 `if` 语句内部，第一行将 `self` 右移 `8` 位。底部的 `8` 位是簿记位：tagged pointer 指示符和字符串长度。剩下的部分，我们假定，是实际数据。让我们将 `rbx` 替换为 `stringData` 以便更清晰。接下来的一行似乎将某种查找表放入 `rcx`，所以让我们将 `rcx` 替换为 `table`。最后，`rdx` 获得 `length` 值的副本。它看起来后来被用作某种游标，所以让我们将 `rdx` 替换为 `cursor`。现在我们的代码是：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(rbp + cursor + 0xffffffffffffffbf) = *(int8_t *)((stringData & 0x3f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(rbp + cursor + 0xffffffffffffffbf) = *(int8_t *)((stringData & 0x1f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(rbp + index + 0xffffffffffffffc0) & 0xff;
        return rax;
    }
```

几乎所有东西都标上了。还有一个原始寄存器名：`rbp`。那实际上是帧指针（frame pointer），所以编译器在做一些狡猾的事情，直接通过帧指针索引。加上常量 `0xffffffffffffffbf` 是二进制补码（"一切最终是无符号整数"）方式减去 `65`。稍后，它减去了 `64`。这些很可能都是同一栈上的局部变量。鉴于正在进行的字节级索引，它可能是一个放在栈上的缓冲区。但这很奇怪，因为有一个代码路径只从那个缓冲区中_读取_，却从未写入。这是怎么回事？

原来，Hopper 忘记反编译那个外部 `if` 语句的 `else` 分支。相关的汇编如下：

```
    mov        rax, rdi
    shr        rax, 0x8
    mov        qword [ss:rbp+var_40], rax
```

`var_40` 是 Hopper 在反汇编中显示该偏移量 `64` 的方式。（`40` 是 `64` 的十六进制形式。）我们称这个位置的指针为 `buffer`。这个缺失分支的 C 语言版本看起来像：

```
    *(uint64_t *)buffer = self >> 8
```

让我们继续插入它，并将其他使用 `rbp` 访问 `buffer` 的地方替换为更易读的代码版本，并添加 `buffer` 的声明以提醒我们发生了什么：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        int8_t buffer[11];
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                *(int8_t *)(buffer + cursor - 1) = *(int8_t *)((stringData & 0x3f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                *(int8_t *)(buffer + cursor - 1) = *(int8_t *)((stringData & 0x1f) + table);
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        } else {
            *(uint64_t *)buffer = self >> 8;
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = *(int8_t *)(buffer + index) & 0xff;
        return rax;
    }
```

好多了。不过，那些疯狂的指针操作语句有点难读，它们实际上只是数组索引。让我们修复它们：

```
    unsigned short -[NSTaggedPointerString characterAtIndex:](void * self, void * _cmd, unsigned long long index) {
        int8_t buffer[11];
        length = self >> 0x4 & 0xf;
        if (length >= 0x8) {
                stringData = self >> 0x8;
                table = "eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX";
                cursor = length;
                if (length < 0xa) {
                        do {
                                buffer[cursor - 1] = table[stringData & 0x3f];
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x6;
                        } while (cursor != 0x0);
                }
                else {
                        do {
                                buffer[cursor - 1] = table[stringData & 0x1f];
                                cursor = cursor - 0x1;
                                stringData = stringData >> 0x5;
                        } while (cursor != 0x0);
                }
        } else {
            *(uint64_t *)buffer = self >> 8;
        }
        if (length <= index) {
                rbx = r8;
                ___CFExceptionProem(self, _cmd);
                [NSException raise:@"NSRangeException" format:@"%@: Index %lu out of bounds; string length %lu"];
                r8 = rbx;
        }
        rax = buffer[index];
        return rax;
    }
```

现在我们有所进展了。

我们可以看到有三种情况，取决于长度。长度值小于 8 会进入那个缺失的 `else` 分支，它仅将 `self` 移位后的值转储到 `buffer` 中。这是纯 ASCII 的情况。这里，`index` 用于对 `self` 的值进行索引，以提取给定的字节，然后返回给调用者。由于 ASCII 字符值匹配 ASCII 范围内的 Unicode 代码点，因此不需要额外的操作来使值正确输出。我们之前猜测在这种情况下字符串存储为纯 ASCII，这证实了这一点。

那么长度为 `8` 或更多的情况呢？如果长度是 `8` 或更多但小于 `10`（`0xa`），则代码进入一个循环。这个循环提取 `stringData` 的底部 `6` 位，将其用作 `table` 的索引，然后将该值复制到 `buffer` 中。然后它将 `stringData` 向下移动 `6` 位并重复，直到遍历完整个字符串。这是一个六位编码，从原始六位值到 ASCII 字符值的映射存储在表中。字符串的临时版本在 `buffer` 中构建，最后的索引操作从中提取请求的字符。

那么长度为 `10` 或更多的情况呢？那里的代码几乎相同，只是它一次处理五位而不是六位。这是一种更紧凑的编码，允许 tagged string 存储多达 `11` 个字符，但仅使用 `32` 个值的字母表。这将使用 `table` 的前半部分作为其缩减的字母表。

因此，我们可以看到 tagged pointer string 的结构是：

1. 如果长度在 `0` 到 `7` 之间，将字符串存储为原始的八位字符。
2. 如果长度是 `8` 或 `9`，使用六位编码存储字符串，使用字母表 `"eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX"`。
3. 如果长度是 `10` 或 `11`，使用五位编码存储字符串，使用字母表 `"eilotrm.apdnsIc ufkMShjTRxgC4013"`。

让我们与我们之前生成的数据进行比较：

```
    0x0000000000006115 a NSTaggedPointerString
    0x0000000000626125 ab NSTaggedPointerString
    0x0000000063626135 abc NSTaggedPointerString
    0x0000006463626145 abcd NSTaggedPointerString
    0x0000656463626155 abcde NSTaggedPointerString
    0x0066656463626165 abcdef NSTaggedPointerString
    0x6766656463626175 abcdefg NSTaggedPointerString
    0x0022038a01169585 abcdefgh NSTaggedPointerString
    0x0880e28045a54195 abcdefghi NSTaggedPointerString
    0x00007fbad9512010 abcdefghij __NSCFString
```

`0x0022038a01169585` 减去底部八位后，按六位块展开的二进制形式是：

```
    001000 100000 001110 001010 000000 010001 011010 010101
```

使用这些索引进入 table，我们可以看到这确实拼写出了 `"abcdefgh"`。类似地，`0x0880e28045a54195` 减去底部八位后，按六位块展开的二进制形式是：

```
    001000 100000 001110 001010 000000 010001 011010 010101 000001
```

我们可以看到它是相同的字符串，末尾加上了 `i`。

但随后它偏离了轨道。在此之后，它应该切换到五位编码并再给我们两个字符串，但相反，它在长度为 `10` 时开始分配对象。怎么回事？

五位字母表_极其_有限，并且不包含字母 `b`！那个字母肯定不够常见，不足以在五位字母表的 `32` 个神圣字符中占有一席之地。让我们再试一次，但这次从 `c` 开始。以下是输出：

```
    0x0000000000006315 c NSTaggedPointerString
    0x0000000000646325 cd NSTaggedPointerString
    0x0000000065646335 cde NSTaggedPointerString
    0x0000006665646345 cdef NSTaggedPointerString
    0x0000676665646355 cdefg NSTaggedPointerString
    0x0068676665646365 cdefgh NSTaggedPointerString
    0x6968676665646375 cdefghi NSTaggedPointerString
    0x0038a01169505685 cdefghij NSTaggedPointerString
    0x0e28045a54159295 cdefghijk NSTaggedPointerString
    0x01ca047550da42a5 cdefghijkl NSTaggedPointerString
    0x39408eaa1b4846b5 cdefghijklm NSTaggedPointerString
    0x00007fbd6a511760 cdefghijklmn __NSCFString
```

我们现在有了 tagged string，一直到长度为 `11`。最后两个 tagged string 的二进制展开是：

```
    01110 01010 00000 10001 11010 10101 00001 10110 10010 00010
    01110 01010 00000 10001 11010 10101 00001 10110 10010 00010 00110
```

这正是我们所期望的。

**创建 tagged string**  
既然我们知道 tagged string 是如何编码的，我就不详细讨论创建它们的代码了。相关代码位于一个名为 `__CFStringCreateImmutableFunnel3` 的私有函数中，该函数在一个巨大的函数中处理了所有可以想象的字符串创建情况。这个函数包含在 [opensource.apple.com](http://opensource.apple.com) 上提供的 CoreFoundation 开源版本中，但别激动：tagged pointer string 代码不包含在开源版本中。

这里的代码本质上是上述过程的逆过程。如果字符串的长度和内容适合 tagged pointer string 所能容纳的范围，它会逐位构建一个 tagged pointer，包含 ASCII、六位或五位字符。有一个查找表的逆表。上面作为常量字符串出现的表作为全局变量 `sixBitToCharLookup` 存在，并且在 `Funnel3` 函数中有一个对应的表 `charToSixBitLookup`。

**那个奇怪的表**  
完整的六位编码表是：

```
    eilotrm.apdnsIc ufkMShjTRxgC4013bDNvwyUL2O856P-B79AFKEWV_zGJ/HYX
```

一个自然的问题是：为什么顺序如此奇怪？

因为这个表同时用于六位和五位编码，所以它不完全按字母顺序排列是有道理的。最常用的字符应该放在前半部分，而较少使用的字符应该放在后半部分。这确保最大数量的较长字符串可以使用五位编码。

然而，在这种划分下，各个半部分内部的顺序并不重要。半部分本身可以按字母顺序排序，但它们并没有。

表中的前几个字母类似于英文字母出现的顺序，按频率排序。英语中最常见的字母是 E，然后是 T、A、O、I、N 和 S。E 刚好在表的开头，其他字母靠近开头。这个表似乎是按使用频率排序的。与英语的差异可能源于 Cocoa App 中的短字符串不是英语散文单词的随机选择，而是更专门的语言片段。

我推测 Apple 最初打算使用一种更高级的可变长度编码，可能基于 [Huffman 编码](https://en.wikipedia.org/wiki/Huffman_coding)。但这被证明太困难，或者不值得付出努力，或者他们只是时间不够了，所以他们将其缩减为上面看到的较不雄心勃勃的版本，即字符串在每字符八位、六位或五位的定长编码之间选择。这个奇怪的表作为一个遗留物留存下来，并且如果 Apple 决定在未来采用可变长度编码，它将作为一个起点。这纯粹是猜测，但在我看来就是这样。

**结论**  
tagged pointer 是一项非常酷的技术。字符串是它的一个不寻常的应用，但很明显 Apple 对此投入了大量思考，并且他们一定看到了显著的好处。了解它是如何组合在一起的，以及他们如何从非常有限的存储中获得最大收益，这很有趣。

今天就到这里。下次回来，我们将继续探索超凡之物的更多奇妙之处。Friday Q&A 由读者建议驱动，所以如果你有想在这里看到的话题想法，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正出售包含大量文章的整本书！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-07-31-tagged-pointer-strings.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被不经通知删除。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
