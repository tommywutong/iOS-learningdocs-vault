---
title: 'Friday Q&A 2011-10-14：GCD 的新功能'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3ce62b643792e9ce'
translated: true
---

> 原文：[Friday Q&A 2011-10-14: What's New in GCD](https://www.mikeash.com/pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)　·　mikeash.com Friday Q&A

发布于 2011-10-14 12:01 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2011-10-28: Generic Block Proxying](https://www.mikeash.com/pyblog/friday-qa-2011-10-28-generic-block-proxying.html)  
上一篇文章：[Friday Q&A 2011-09-30: Automatic Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd)

Friday Q&A 2011-10-14：GCD 的新功能

作者：[Mike Ash](https://www.mikeash.com/)

**预备阅读**  
如果你不熟悉 GCD，建议先了解基础内容，再深入探索 Lion 中的新功能。网上有很多很好的参考资料，包括我自己写的系列文章，从 [Grand Central Dispatch 介绍（一）：基础与 Dispatch Queues](https://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html) 开始。

**概述**  
GCD 仍然是我们熟悉和喜爱的那套出色库，但现在多了不少新特性。

首先，有一个新的全局队列可用，通过传递 `DISPATCH_QUEUE_PRIORITY_BACKGROUND` 来访问。这个队列以极低的优先级运行，并且磁盘 IO 会受到限制。这使得它适用于那些需要最小化对系统交互使用影响的持续任务。

接下来，我们现在可以创建自定义并发队列了。以前，自定义队列总是串行的，GCD 支持的唯一并发队列是全局队列。自定义并发队列可以轻松挂起并行化的任务。与此同时，GCD 现在提供了 dispatch barriers，使自定义并发队列可以像读写锁（reader/writer lock）一样使用。

最后，期待已久的 GCD IO 来了。可以为路径或文件描述符创建 Dispatch IO 对象。这不仅提供了比 dispatch source API 更简单的 IO 接口，还让 GCD 能够更智能地协调 IO 活动，避免磁盘抖动。与此相关的还有一个新的 dispatch data 类型，它能高效管理不连续的数据。

关于新的全局后台队列其实没什么更多可说的了，我们直接进入……

**自定义并发队列与 Barriers**  
创建自定义并发队列很简单：向 `dispatch_queue_create` 函数传递 `DISPATCH_QUEUE_CONCURRENT`。串行队列仍然可以通过传递 `NULL` 或 `DISPATCH_QUEUE_SERIAL` 获得。

创建后，并发队列的行为正如你预期的那样。如果系统负载和能力允许，提交给它的多个 block 可以并行运行。与全局队列不同，你仍然可以暂停/恢复自定义并发队列，这在管理一组并行操作时非常有用。

Dispatch barriers 与自定义并发队列配合使用。它们可以通过两个函数使用：`dispach_barrier_async` 和 `dispatch_barrier_sync`。它们的工作方式与 `dispatch_async` 和 `dispatch_sync` 类似，不同之处在于，如果在自定义并发队列上使用，通过 `barrier` 函数提交的 block 不会与该队列上的其他工作并发运行。相反，它会等待队列上当前正在执行的所有内容完成，然后在执行 barrier block 时阻塞队列上的所有其他内容。一旦 barrier 完成，执行恢复正常。

请注意，这些 barrier 函数在串行队列上没有意义，因为每个工作单元都会阻塞该队列上的其他工作。在全局队列上使用时，它们是非功能性的，只是执行普通的 `dispatch_async` 或 `dispatch_sync`。这是因为全局队列是共享资源，允许单个组件为所有人阻塞它们是不合理的。

自定义并发队列和 barriers 允许高效操作可以并发读取但不能并发写入的数据结构。如果你熟悉它们，它们基本上提供了与传统多线程技术中的读写锁相同的功能。

举个例子，假设我们有一个用作缓存的 `NSMutableDictionary`。`NSMutableDictionary` 对于读取是线程安全的，但在修改其内容时不允许任何并发访问，即使其他访问只是简单的读取也不行。

使用自定义并发队列和 barriers 很容易实现这一点。首先，我们创建字典和队列：

```
    _cache = [[NSMutableDictionary alloc] init];
    _queue = dispatch_queue_create("com.mikeash.cachequeue", DISPATCH_QUEUE_CONCURRENT);
```

要从缓存中读取，我们可以使用 `dispatch_sync`：

```
    - (id)cacheObjectForKey: (id)key
    {
        __block obj;
        dispatch_sync(_queue, ^{
            obj = [[_cache objectForKey: key] retain];
        });
        return [obj autorelease];
    }
```

因为队列是并发的，这允许并发访问缓存，因此在常见情况下多个线程之间不会产生争用。

要写入缓存，我们需要一个 barrier：

```
    - (void)setCacheObject: (id)obj forKey: (id)key
    {
        dispatch_barrier_async(_queue, ^{
            [_cache setObject: obj forKey: key];
        });
    }
```

因为使用了 `barrier` 函数，这确保了在 block 运行时对缓存的独占访问。它不仅排除了所有其他写入缓存的尝试，还排除了所有其他读取，使修改安全。

对于这样一个简单的字典，收益并不明显，但对于更复杂的用例，当读取方需要执行昂贵的原子操作序列时，它可以轻松编写快速、安全的并发代码。

**Dispatch Data**  
Dispatch data 对象显然是为了方便 dispatch IO 而包含的，但它们本身也是独立的，可以作为通用的数据容器使用。Dispatch data 对象很像 `NSData` 对象，都是围绕原始指针和长度的简单对象包装器。数据的含义以及如何使用完全由你决定。

然而，与 `NSData` 有一个主要区别，即 dispatch data 对象可以是**不连续的**。从根本上说，`NSData` 是一个单一的缓冲区。Dispatch data 对象是多个此类缓冲区的集合。这可以显著提高性能，因为通常无需复制任何数据。例如，当连接两个 `NSData` 对象时，至少需要复制其中一个缓冲区，很可能两个都需要复制。当连接 dispatch data 对象时，不需要复制任何内容。在内部，这是通过创建一个 dispatch data 对象的树来实现的，叶子节点包含一个连续的缓冲区，其他节点指向包含各个缓冲区的对象。

当然，许多代码希望处理连续数据，但幸运的是，GCD 可以轻松地将 dispatch data 对象压缩成一个单一的缓冲区。对于更灵活的代码，可以轻松地遍历数据对象中包含的各个缓冲区。

要创建一个基本的 dispatch data 对象，请使用 `dispatch_data_create` 函数。它接受一个指针、长度、析构器 block 以及一个用于运行析构器的队列。通过请求默认析构器，数据将立即复制到由 GCD 管理的存储中：

```
    dispatch_data_t data = dispatch_data_create(buffer, length, NULL, DISPATCH_DATA_DESTRUCTOR_DEFAULT);
    // buffer 现在可以释放了
```

当然，这一切的重点是避免复制，因此最好提供一个显式的析构器来释放内存，以避免被复制。一个常见的情况是用 `malloc` 分配的内存，`DISPATCH_DATA_DESTRUCTOR_FREE` 析构器会调用 `free`：

```
    void *buffer = malloc(length);
    // 填充 buffer
    dispatch_data_t data = dispatch_data_create(buffer, length, NULL, DISPATCH_DATA_DESTRUCTOR_FREE);
    // buffer 将在 data 被销毁时释放
```

对于其他类型的缓冲区，我们可以提供一个自定义的 block 来做任何必要的事情。例如，下面是一个简单的函数，它创建了一个包装 `NSData` 对象的 dispatch data 对象：

```
    dispatch_data_t CreateDispatchDataFromNSData(NSData *nsdata)
    {
        // 在这里复制数据对象，以防它是可变的
        // 如果它是不可变的，这只会进行 retain
        nsdata = [nsdata copy];

        dispatch_queue_t queue = dispatch_get_global_queue(0, 0);
        return dispatch_data_create([nsdata bytes], [nsdata length], queue, ^{
            // 平衡上面的 copy
            [nsdata release];
        });
    }
```

要连接两个 dispatch data 对象，只需使用 `dispatch_data_create_concat`。要提取数据对象的一部分，`dispatch_data_create_subrange` 可以获取一个精确的子范围，而 `dispatch_data_copy_region` 可以获取特定位置周围的区域，这给了 GCD 更大的灵活性以提高效率。

要访问数据对象的内容，最简单的方法是调用 `dispatch_data_create_map`，它会将所有数据连接成一个单一的连续缓冲区：

```
    const void *buffer;
    size_t length;
    dispatch_data_t tmpData = dispatch_data_create_map(data, &buffer, &length);
    // 在这里使用 buffer 和 length
    dispatch_release(tmpData);
```

然而，这可能需要复制各个数据片段以创建连续缓冲区，而这正是整个系统试图避免的。为了更高效地访问内容，可以使用 `dispatch_data_apply`，它会遍历各个片段，并在每个片段上调用一个 block。

例如，下面是一个函数，它使用 `dispatch_data_apply` 将包含 ASCII 数据的 data 对象转换为 `NSString`，以避免不必要的复制：

```
    NSString *StringFromDispatchData(dispatch_data_t data)
    {
        NSMutableString *s = [NSMutableString stringWithCapacity: dispatch_data_get_size(data)];
        dispatch_data_apply(data, ^(dispatch_data_t region, size_t offset, const void *buffer, size_t size) {
            [s appendFormat: @"%.*s", size, buffer];
            return (_Bool)true;
        });
        return s;
    }
```

请注意，applier block 返回一个布尔值，指示 apply 操作是否应继续。由于这个 block 无条件地继续，它只返回 `true`，并通过一些类型转换来安抚编译器。

**Dispatch IO**  
现在我们来到了 GCD 中真正重要的新功能。最初的 GCD API 可以通过 dispatch sources 与 IO 集成。Dispatch source 可用于监视文件描述符，并在可以读取或写入数据时运行处理程序。然而，这种方法仍然给程序员留下了许多工作，他们必须手动读取和写入相关数据，并管理文件描述符的生命周期。通过将更多责任交给 GCD，它还能够更智能地管理多个并发 IO 操作，以减少抖动和资源争用。

Dispatch IO 对象被称为通道（channels）。一个通道包装了一个文件描述符。要创建一个，使用 `dispatch_io_create` 函数，它接受一个通道类型（流或随机访问）、文件描述符、要与通道关联的队列以及一个清理处理程序。以下是一个为标准输入创建通道的快速示例：

```
    dispatch_io_t stdinChannel = dispatch_io_create(DISPATCH_IO_STREAM, STDIN_FILENO, dispatch_get_global_queue(0, 0), ^(int error) {
        if(error)
            fprintf(stderr, "got an error from stdin: %d (%s)\n", error, strerror(error));
    });
```

我们想从这个通道读取，但首先需要配置它。我们可以通过设置通道的高水位和低水位值来告诉 GCD 我们想要数据的频率。低水位值设置了 GCD 在调用读取处理程序之前尝试收集的数据量。标准输入通常是交互式的，在这种情况下，我们希望 GCD 在任何数据进来时（无论多小）都调用读取处理程序，因此我们将低水位标记设置为仅一个字节：

```
    dispatch_io_set_low_water(stdinChannel, 1);
```

没有理由限制最大数据量，因此我们将高水位值保留为默认的 `SIZE_MAX`，这基本上是无限的。如果出于某种原因需要限制它，只需调用 `dispatch_io_set_high_water`。

还有一个 `dispatch_io_set_interval` 函数，它告诉 GCD 定期调用读取处理程序，允许代码监视 IO 操作的进度。对于简单地从标准输入读取来说，这也是不必要的。

现在通道已配置好，我们将使用 `dispatch_io_read` 告诉 GCD 从其中读取。此函数接受一个通道、偏移量（对于像这样的流通道，该参数被忽略）、长度、队列和处理程序 block：

```
    dispatch_io_read(stdinChannel, 0, SIZE_MAX, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {
        if(data)
        {
            // 处理数据
        }
        if(error)
        {
            // 处理错误，或者让通道的处理程序来处理
        }
        if(done)
        {
            // 我们已经处理完所有标准输入，因此退出
            exit(0);
        }
    });
```

类似地，我们可以使用 `dispatch_io_write` 写入通道。通过创建另一个通道并在上面的处理程序中插入一些代码，程序变成了一个简单的回显工具：

```
    dispatch_io_t stderrChannel = dispatch_io_create(DISPATCH_IO_STREAM, STDERR_FILENO, dispatch_get_global_queue(0, 0), ^(int error) {
        if(error)
            fprintf(stderr, "got an error from stdout: %d (%s)\n", error, strerror(error));
    });

    dispatch_io_read(stdinChannel, 0, SIZE_MAX, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {
        if(data)
        {
            dispatch_io_write(stderrChannel, 0, data, dispatch_get_global_queue(0, 0), ^(bool done, dispatch_data_t data, int error) {});
        }
        ...
```

除了处理原始文件描述符之外，GCD 还提供了 `dispatch_io_create_with_path`，这是一个便捷函数，用于直接获取指向磁盘上文件的 IO 通道。这基本上结合了 `dispatch_io_create` 和 `open`，方便之处在于只需要在一个地方处理错误。

当 IO 通道使用完毕后，只需调用 `dispatch_io_close` 显式关闭通道，并且不要忘记使用 `dispatch_release` 来平衡 create 调用。

对于简单的用例，GCD 还提供了 `dispatch_read` 和 `dispatch_write` 调用，它们可以在不设置通道的情况下，从文件描述符执行基于 GCD 的简单 IO。这使得一次性读取一大块数据变得简单，尽管对于更复杂的用途，创建通道更高效且更易于使用。

Dispatch IO 通道可以与几乎任何类型的文件描述符通信，使得这个 API 不仅对操作文件有用，对操作 socket 和管道也有用。

**结论**  
Lion 和 iOS 5 为 GCD 带来了一些令人兴奋且期待已久的补充。新的全局后台队列适用于长时间运行、低影响的任务。创建自定义并发队列的能力允许更好地管理并行化任务，而 barriers 允许在读取时安全地并行访问共享数据，并在写入时提供独占访问。最后，dispatch IO API 将 GCD 的智能和系统范围的集成带到了文件访问和网络通信中。

今天就到这里。你现在可以回去等待你的崭新 iPhone 了。Friday Q&A 由读者想法驱动，所以如果你在玩新玩具时想到什么想在这里看到的内容，[请发送给我](mailto:mike@mikeash.com:)！

喜欢这篇文章吗？我正在出售整本充满文章的书！第二卷和第三卷现已推出！它们提供 ePub、PDF、印刷版，以及在 iBooks 和 Kindle 上购买。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-10-14-whats-new-in-gcd.html)

发表你的想法，添加评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
