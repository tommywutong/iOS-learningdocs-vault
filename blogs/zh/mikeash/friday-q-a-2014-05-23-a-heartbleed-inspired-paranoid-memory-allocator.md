---
title: 'Friday Q&A 2014-05-23：受 Heartbleed 启发的偏执内存分配器'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5891cd01d0a66c02'
translated: true
---

> 原文：[Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)　·　mikeash.com Friday Q&A

发布于 2014-05-23 13:46 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2014-06-06：dispatch_once 的秘密](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)  
上一篇文章：[Friday Q&A 2014-05-09：何时 Autorelease 不是 Autorelease](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [heartbleed](https://www.mikeash.com/pyblog/?tag=heartbleed) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2014-05-23：受 Heartbleed 启发的偏执内存分配器

作者：[Mike Ash](https://www.mikeash.com/)

**背景**  
Heartbleed 漏洞涉及添加到 TLS 协议中的心跳消息，该协议用于安全 HTTP 连接和许多其他加密互联网协议。该消息是一种简单的 ping，一方可以询问“你还在吗？”，另一方会回复“是的。”与许多 ping 一样，请求方可以包含一个有效载荷，另一方会将其重复发送回来。有效载荷由一串字节组成，前面带有一个 16 位的长度字段，用于指示有效载荷中的字节数。

Heartbleed 漏洞的根本原因在于对长度前缀的处理不当。请求方可以发送一个请求，其中长度字段的值很大，但有效载荷却较短。对此，正确的处理方式应将其视为致命错误并终止连接。

OpenSSL 未能进行检查，因此在这种情况下继续执行了响应。它使用长度字段来决定要复制的字节数，将有效载荷从请求复制到响应中。如果实际有效载荷比长度字段声称的值短，它最终会复制入站数据包数据之后的内容。

OpenSSL 为此类任务以及其他任务使用内部分配器，该分配器在分配或释放内存时不会清零内存。因此，复制到响应中的额外数据最终会是恰好存储在该位置的、上次分配时留下的任意数据。由于同一个分配器也用于存储私钥等内容，这些数据最终可能会被发送回请求方。

为了尽可能多地获取数据，攻击者可以指定一个长度很长但没有有效载荷的字段。易受攻击的 TLS 实现随后会用其内部内存中数千字节的数据进行回复。取决于运气，攻击者有很大机会在该数据转储中获得一些有用的信息。如果没有有用信息，攻击者可以再次尝试。这个过程很快，并且可以无限重复。

**偏执内存分配器**  
Heartbleed 的正确修复方法是在发送回复之前，根据提供的有效载荷验证长度字段。有许多方法可以尝试避免这类安全漏洞。

一种方法是为开发安全关键软件制定更完善的流程。起初并没有特别好的理由将心跳扩展添加到 TLS 中，或在 OpenSSL 中实现它，因此整个事情本应在开始之前就被阻止。

另一种方法是使用静态分析工具，该工具能够检测到何时对输入数据过度信任。不幸的是，Heartbleed 漏洞对于大多数静态分析工具来说过于微妙，无法检测到。虽然此事推动了该领域的大量工作，但很难知道其中有多少工作将有助于检测未来的类似错误，以及有多少工作实际上只是帮助它们专门检测 Heartbleed。

最后，避免这些漏洞的另一种方法是使用比 C 更安全的语言进行编程。C 语言可能极其不宽容，其[未定义行为](http://www.catb.org/jargon/html/N/nasal-demons.html)的概念意味着错误很容易变成安全漏洞。使用更安全的语言这一建议已提出多年，但尽管存在这些问题，安全关键代码仍然用 C 语言编写。

有趣的是，我不太确定一种更好的语言是否能阻止这个特定的错误。即使在具有更强保证的语言中，重用缓冲区也相对自然，这最终也可能导致内容被重用。如果缓冲区没有被截断到每个传入数据包的实际长度，边界检查将无法捕获过大的复制。话虽如此，更好的语言可以杜绝一整类安全漏洞，并且认真考虑 C 语言的替代方案可能是个明智之举。

从理论上讲，上述措施应该足够了。但在实践中，采用分层方法进行安全防护是个好主意，不仅要努力避免漏洞，还要在漏洞发生时尝试减轻其影响。例如，OS X 和大多数其他操作系统会默认将内存标记为不可执行。这意味着，即使攻击者能够将机器代码写入你进程的内存并跳转到它，除非攻击者能首先将该代码标记为可执行，否则控制权的夺取尝试将会失败。

鉴于此，我思考了在为敏感数据（如私钥）分配内存时可以采取哪些措施，以帮助在漏洞被利用时仍能保证数据安全。我想到了以下特性：

1.  内存应在分配时清零，释放时再次清零。
2.  应在内存分配的前后放置不可读、不可写的保护页，这样来自相邻分配的溢出就会导致崩溃。
3.  用于存储的内存应保持最小权限。默认情况下应为不可读且不可写。当请求读取时，应将其更改为只读；当请求写入时，应将其更改为读写。
4.  API 的设计应使得难以在超出必要时间后仍保留读取或写入权限，尤其是难以意外地永久保留这些权限。

**代码**  
与往常一样，代码可在 GitHub 上获取：

[https://github.com/mikeash/MAParanoidAllocator](https://github.com/mikeash/MAParanoidAllocator)

**API**  
这是该类的公开 API：

```
    @interface MAParanoidAllocator : NSObject

    - (id)init;
    - (id)initWithSize: (size_t)size;

    - (size_t)size;
    - (void)setSize: (size_t)size;

    - (void)read: (void (^)(const void *ptr))block;
    - (void)write: (void (^)(void *ptr))block;

    @end
```

大部分显而易见，但 `read:` 和 `write:` 需要一些解释。

从概念上讲，该类类似于 `NSMutableData`。它是围绕任意字节块的对象封装。`NSMutableData` API 提供了用于读取的 `bytes` 方法，以及用于读取和写入的 `mutableBytes` 方法。然而，这些方法使得数据对象无法知道调用者何时完成读取或写入。可以添加一个在结束时调用的方法来显式指示操作已完成，这样调用代码看起来像：

```
    const void *ptr = [dataObject bytes];
    // ...在这里使用 ptr...
    [dataObject recycleBytes: ptr];
```

然而，很容易忘记调用 `recycleBytes:`，从而永久保持内存可读。

`read:` 和 `write:` 方法都接受一个 block 作为参数。该 block 被同步调用，并传入一个指向对象所持有内存的指针。该指针仅在 block 内部有效，一旦 block 返回，权限会自动重置，使内存变为不可读和不可写。

**实现策略**  
像 `malloc` 和 `free` 这样的常规内存分配 API 不适用于此类。

相反，它将使用 `mmap` 分配内存。这允许它使用 `mprotect` 更改内存的权限。`mmap` 和 `mprotect` 都按页粒度工作，意味着该类必须以 4kB 的块来分配内存。分配内存时，它会将请求的大小向上舍入到最接近的 4kB 倍数。它还将在大小上增加两个 4kB 页面，一个用于前面的保护页，一个用于后面的保护页。保护页将永久标记为不可读和不可写。中间分配的内存通常标记为不可读和不可写，但权限会在必要时使用 `mprotect` 临时更改。

要调整现有分配的大小，方法并不特别：分配新内存，复制内容，然后释放旧内存。由于内存是用 `mmap` 分配的，因此用 `munmap` 释放。出于偏执考虑，代码会在将分配的内存返还给操作系统之前将其清零。

**实例变量**  
该类需要三个实例变量：当前分配的大小、指向已分配内存的指针以及系统的页面大小。页大小可以是全局变量，但将其保留为实例变量稍微方便一些：

```
    @implementation MAParanoidAllocator {
        size_t _size;
        char *_memory;
        size_t _pageSize;
    }
```

**错误检查**  
这段代码并没有花太多力气去报告或从错误中恢复。这些调用通常不应失败，如果失败，那一定是出了严重问题。如果它们失败，代码只会记录错误，然后调用 `abort()`。错误检查在所有代码中都至关重要，对于安全关键代码尤其如此，因为未检查的错误很容易变成可利用的漏洞。（例如，请参阅[可利用的用户态 NULL 指针解引用](http://tk-blog.blogspot.com/2009/01/exploitable-userland-null-pointer.html)。）

我编写了一个简单的错误检查宏，它实际上只是一个自定义的 `assert`：

```
    #define CHECK(condition) do { \
            if(!(condition)) { \
                NSLog(@"%s: %s (%d)", #condition, strerror(errno), errno); \
                abort(); \
            } \
        } while(0)
```

除了记录失败的条件并调用 `abort()` 之外，它还会打印 `errno` 的值，以帮助指示出了什么问题。

**初始化与释放**  
`init` 方法调用 `super`，然后设置页面大小变量：

```
    - (id)init {
        if((self = [super init])) {
            CHECK((_pageSize = sysconf(_SC_PAGESIZE)) > 0);
        }
        return self;
    }
```

其他变量保持为零，表示一个新初始化的实例大小为 0。该类将被构建为，当大小为 0 时表示没有分配内存，也不需要释放资源。这意味着，首次分配只需用所需大小调用 `setSize:` 即可完成，而在 `dealloc` 中进行清理可以通过将大小设回 0 来完成。

因此，`initWithSize:` 方法仅调用 `init`，然后调用 `setSize:`：

```
    - (id)initWithSize: (size_t)size {
        self = [self init];
        [self setSize: size];
        return self;
    }
```

`dealloc` 方法再次仅调用 `setSize:`：

```
    - (void)dealloc {
        [self setSize: 0];
    }
```

**页大小舍入**  
API 承诺字节粒度，但后台的所有调用都必须处理整个页面。这不成问题，但确实需要将请求的大小向上舍入到页大小的最接近倍数。这个简单的方法解决了这个问题：

```
    - (size_t)roundToPageSize: (size_t)size {
        size_t pageCount = (size + _pageSize - 1) / _pageSize;
        return pageCount * _pageSize;
    }
```

**更改内存权限**  
代码中的几个地方需要对整个分配的内存块调用 `mprotect`。这需要将分配大小向上舍入到最接近的页大小，调用 `mprotect`，并检查错误。该过程被封装在一个小的辅助方法中：

```
    - (void)mprotect: (int)prot {
        size_t size = [self roundToPageSize: _size];
        if(size > 0) {
            CHECK(mprotect(_memory, size, prot) == 0);
        }
    }
```

**设置大小**  
该类的大部分复杂性在于 `setSize:`。这是分配、释放以及将数据从旧分配复制到新分配的地方。

它首先将新大小和旧大小都舍入为页面大小的倍数：

```
    - (void)setSize: (size_t)newSize {
        size_t beforeSize = [self roundToPageSize: _size];
        size_t afterSize = [self roundToPageSize: newSize];
```

这些值会被多次使用，因此最好一次性预先计算。接下来，检查它们是否真的不同。如果舍入后的大小相等，则无需重新分配内存：

```
        if(beforeSize != afterSize) {
```

如果它们不同，那么下一个任务是分配一个具有新大小的新内存块。由于大小为 0 时处理为不分配任何内存，因此仅当新大小不为 0 时才执行此操作：

```
            char *afterPointer = NULL;
            if(afterSize > 0) {
```

要分配的总内存量是新大小加上两个额外的保护页：

```
                size_t guardPagesSize = _pageSize * 2;
                size_t toAllocate = afterSize + guardPagesSize;
```

然后，调用 `mmap`。它请求一个匿名的、私有的映射（换句话说，它并不是在尝试内存映射文件或类似的东西），并具有读取和写入权限。它需要将现有数据复制到新分配中，因此使新内存不可读和不可写将在稍后进行。

```
                char *allocatedPointer;
                CHECK((allocatedPointer = mmap(NULL, toAllocate, PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, 0, 0)) != MAP_FAILED);
```

`mmap` 返回的指针指向前面的保护页。实际用于存储数据的内存指针在此之后的一页处：

```
                afterPointer = allocatedPointer + _pageSize;
```

`mmap` 返回的内存已被操作系统清零，因此无需在代码中显式清除它。

新的分配就位后，前导和尾随页面被设置为不可读且不可写，以便它们作为保护页：

```
                CHECK(mprotect(allocatedPointer, _pageSize, PROT_NONE) == 0);
                CHECK(mprotect(afterPointer + afterSize, _pageSize, PROT_NONE) == 0);
            }
```

如果存在现有分配和新的分配，则需要复制数据。新分配当前是可写的，但现有分配是完全不可访问的。因此，复制操作在对 `read:` 方法的调用内部完成：

```
            if(beforeSize > 0 && afterSize > 0) {
                [self read: ^(const void *ptr) {
                    memcpy(afterPointer, ptr, MIN(beforeSize, afterSize));
                }];
            }
```

此时，新内存已分配（如果需要），并且现有数据（如果有）已复制到其中。下一步是释放旧内存（如果有）：

```
            if(beforeSize > 0) {
```

在将其返还给操作系统之前，将其清零：

```
                [self write: ^(void *ptr) {
                    memset(ptr, 0, beforeSize);
                }];
```

这可能是不必要的。`munmap` 的文档不保证内存在释放后会被清零，但它应该是安全的，因为唯一能再次获得这块内存的方法是调用 `mmap`，而 `mmap` 在将内存提供给调用者之前会将其清零。然而，这是一个名称中带有“偏执”的类，而这种保证对于我的舒适度来说有点过于间接。

（顺便说一句：在此类代码中有一个常见问题，即 `memset` 调用会被编译器优化掉。编译器足够聪明，知道写入一个随后立即传递给 `free()` 的缓冲区是毫无意义的，因此写入可以被消除。虽然根据语言标准这是正确的，但对于像这样偏执的、注重安全的代码来说，这是不可取的行为。为了解决这个问题，C11 标准引入了 `memset_s` 函数。它做的事情与 `memset` 相同，但保证不会被优化掉。它在 Mac OS X 10.9 及 iOS 7 起始的 Apple 平台上可用。幸运的是，此处不需要 `memset_s`，因为在 block 中间接调用 `memset`，并且内存是使用 `munmap` 而不是 `free` 释放的，意味着它不能被优化掉。使用普通的 `memset` 允许此代码与更早的 OS 版本兼容。）

现在内存已清零，它必须计算原始分配的总大小，以及指向分配起始位置的指针，同时考虑前导和尾随保护页：

```
                size_t guardPagesSize = _pageSize * 2;
                size_t toDeallocate = beforeSize + guardPagesSize;
                char *pointerWithGuards = _memory - _pageSize;
```

然后调用 `munmap` 来释放内存。

```
                CHECK(munmap(pointerWithGuards, toDeallocate) == 0);
            }
```

新内存已分配，旧内存已释放，现在是更新实例变量的时候了：

```
            _memory = afterPointer;
            _size = newSize;
```

最后，新分配的内存可以被设置为不可读且不可写：

```
            [self mprotect: PROT_NONE];
```

在两次分配（舍入后）大小相同的情况下，不需要做太多事情。除了更新 `_size` 实例变量外，如果大小缩小，它还会清零新大小末尾之后的任何额外内存。这确保了在调用者预期敏感数据消失后，不会留有残留的潜在敏感数据：

```
        } else {
            if (newSize < _size) {
                [self write:^(void *ptr) {
                    memset((char *)ptr + newSize, 0, _size - newSize);
                }];
            }
            _size = newSize;
        }
    }
```

**size 获取方法**  
与 `setSize:` 相比，`size` 方法的实现有些乏味：

```
    - (size_t)size {
        return _size;
    }
```

**读取与写入**  
让我们看看 `read:` 和 `write:` 的实现。这两个方法都遵循相同的基本模式：`mprotect` 分配的内存以赋予某些权限，调用一个 block，然后再次 `mprotect` 分配的内存使其不可访问。这种模式可以封装到一个公共方法中：

```
    - (void)withProtections: (int)prot call: (void (^)(void))block {
        [self mprotect: prot];
        block();
        [self mprotect: PROT_NONE];
    }
```

有了它，`read:` 方法只需使用 `PROT_READ` 调用 `withProtections:call:`：

```
    - (void)read: (void (^)(const void *))block {
        [self withProtections: PROT_READ call: ^{
            block(_memory);
        }];
    }
```

`write:` 方法几乎相同，只是使用 `PROT_READ | PROT_WRITE`：

```
    - (void)write: (void (^)(void *))block {
        [self withProtections: PROT_READ | PROT_WRITE call: ^{
            block(_memory);
        }];
    }
```

**测试**  
我想确保测试此代码的所有特性。其中许多特性涉及确保在尝试访问提供的 API 之外的内容时代码会崩溃。我的第一个方法是编写会导致崩溃的代码，然后使用类似 [PLCrashReporter](https://www.plcrashreporter.org/) 的工具来捕获崩溃并恢复执行。不幸的是，这在调试器中效果不佳，因为 `lldb` 强烈坚持在程序崩溃时停止执行，即使崩溃本将被捕获。由于调试测试非常有用，我不想采用这种方法。

在尝试设置自定义 Mach 异常处理程序的过程中经历了大量痛苦和折腾之后，我意识到我可以使用像 `mach_vm_read` 和 `mach_vm_write` 这样的 Mach 调用来执行非法的内存读取和写入，而不会崩溃。这些调用允许读取和写入内存，但当给定的地址不可访问时，它们会返回错误而不是引发信号。这大大简化了测试代码。我不会在这里详细介绍细节，但如果你感兴趣，可以[在 GitHub 上阅读测试代码](https://github.com/mikeash/MAParanoidAllocator/blob/master/MAParanoidAllocator%20Tests/MAParanoidAllocator_Tests.m#L44)。

**结论**  
这段代码防御了一种本不应发生的情况，在这种情况下你实际上已经输了。允许攻击者触及此处使用的各种保护措施的 bug 一开始就不应该发生。然而，由于 bug 是不可避免的，采用分层安全方法有助于减轻其影响。我不确定在这种情况下它是否真正有用，但这是一个有趣的练习，并且在敏感数据未明确使用时使其不可读似乎也并非不合理。用于实现这一点的技术都是相当直接的 POSIX 调用，尽管它们在普通代码中不常用。

今天就到这里。下次再来看看更多令人惊恐的冒险。Friday Q&A 由读者的想法驱动，因此，像往常一样，如果你有一些希望在这里看到的主题想法，请[发邮件给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正出售包含这些文章的完整书籍！第 II 卷和第 III 卷现已出版！提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版本。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被不经通知地删除。违规者可能会根据我的唯一判断被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
