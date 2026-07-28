---
title: 'Friday Q&A 2013-08-16：我们来构建 Dispatch Groups'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a1f209eeb687030b'
translated: true
---

> 原文：[Friday Q&A 2013-08-16: Let's Build Dispatch Groups](https://www.mikeash.com/pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)　·　mikeash.com Friday Q&A

发布于 2013-08-17 02:19 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章：[Friday Q&A 2013-08-30：使用 Property List 进行模型序列化](https://www.mikeash.com/pyblog/friday-qa-2013-08-30-model-serialization-with-property-lists.html)
前一篇文章：[Friday Q&A 2013-08-02：使用单字段结构体实现类型安全的标量](https://www.mikeash.com/pyblog/friday-qa-2013-08-02-type-safe-scalars-with-single-field-structs.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [gcd](https://www.mikeash.com/pyblog/?tag=gcd) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2013-08-16：我们来构建 Dispatch Groups

作者：[Mike Ash](https://www.mikeash.com/)

**概述**
Dispatch Groups 提供了四种基本操作：

1. `Enter`，表示一个任务已开始。
2. `Exit`，表示一个任务已完成。
3. `Notify`，当每个 `enter` 都有对应的 `exit` 时，调用一个 `block`。
4. `Wait`，类似于 `notify`，但是同步的。

你可以借助它启动一系列并行操作并等待它们完成：

```
    dispatch_group_t group = dispatch_group_create();
    for(int i = 0; i < 100; i++)
    {
        dispatch_group_enter(group);
        DoAsyncWorkWithCompletionBlock(^{
            dispatch_group_leave(group);
        });
    }
    dispatch_group_wait(group, DISPATCH_TIME_FOREVER);
```

你也可以在它们全部完成后异步调用一个 `block`：

```
    dispatch_group_t group = dispatch_group_create();
    for(int i = 0; i < 100; i++)
    {
        dispatch_group_enter(group);
        DoAsyncWorkWithCompletionBlock(^{
            dispatch_group_leave(group);
        });
    }
    dispatch_group_notify(group, dispatch_get_main_queue(), ^{
        UpdateUI();
    });
```

由于这是 GCD 的一部分，并且我们在讨论异步操作，因此不言而喻，dispatch groups 的一个主要特性是所有操作都是线程安全的。

**代码**
像往常一样，我已经将这份重新实现的完整代码发布在 GitHub 上：

[https://github.com/mikeash/MADispatchGroup](https://github.com/mikeash/MADispatchGroup)

**接口**
`ma_dispatch_group` 的 API 与 `dispatch_group` 紧密对应：

```
    typedef struct ma_dispatch_group_internal *ma_dispatch_group_t;

    ma_dispatch_group_t ma_dispatch_group_create(void);
    void ma_dispatch_group_destroy(ma_dispatch_group_t group);
    void ma_dispatch_group_enter(ma_dispatch_group_t group);
    void ma_dispatch_group_leave(ma_dispatch_group_t group);
    void ma_dispatch_group_notify(ma_dispatch_group_t group, void (^block)(void));
    void ma_dispatch_group_wait(ma_dispatch_group_t group);
```

与 `dispatch_group` 接口相比存在一些差异：

1. `ma_dispatch_group_t` 不是一个 dispatch 对象，因此它不使用 retain/release 语义，而是使用单一的 `destroy` 函数来清理它。
2. `dispatch_group_async` 函数被省略了。它们只是围绕 `enter`、`leave` 和 `dispatch_async` 的简单包装，因此并不那么重要。
3. `notify` 函数不接受 dispatch queue，而是在最后调用 `leave` 的那段代码的上下文中立即调用 `block`。将 `block` 包裹在 `dispatch_async` 中是很简单的，因此这并不是重大变化。
4. `wait` 函数不接受超时。这大大简化了代码，同时仍然展示了整体概念。

**字段**
`struct ma_dispatch_group_internal` 包含两个字段：一个计数器和一个动作 `block`：

```
    struct ma_dispatch_group_internal {
        uint32_t counter;
        void (^action)(void);
    };
```

计数器跟踪的是在调用 `enter` 后尚未有对应 `exit` 的次数。动作 `block` 是由 `notify` 函数设置的动作。

**创建与销毁**
创建一个新的分组非常简单。只需分配一块内存，使用 `calloc` 确保其被清零：

```
    ma_dispatch_group_t ma_dispatch_group_create(void)
    {
        ma_dispatch_group_t group = calloc(1, sizeof *group);
        return group;
    }
```

销毁一个分组同样简单。我假定任何通过 `notify` 设置的动作在分组被销毁前总是会触发，并且动作 `block` 会作为该过程的一部分被销毁。因此，除了简单地调用 `free` 之外，`destroy` 中不需要进行清理：

```
    void ma_dispatch_group_destroy(ma_dispatch_group_t group)
    {
        free(group);
    }
```

**Enter**
`ma_dispatch_group_enter` 的实现非常简单。它只是一个原子递增，使用的是编译器的内建原子操作：

```
    void ma_dispatch_group_enter(ma_dispatch_group_t group)
    {
        __sync_fetch_and_add(&group->counter, 1);
    }
```

使用内建原子操作确保了它的线程安全性。`ma_dispatch_group_leave` 的实现稍微复杂一些。它首先执行原子递减：

```
    void ma_dispatch_group_leave(ma_dispatch_group_t group)
    {
        uint32_t newCounterValue = __sync_sub_and_fetch(&group->counter, 1);
```

`__sync_sub_and_fetch` 内建函数首先执行原子递减，然后返回计数器的新值。如果这是最后一次 `leave` 调用，那么 `newCounterValue` 将为 `0`，此时就该执行分组的通知动作了。

```
        if(newCounterValue == 0)
        {
```

动作可能尚未存在，例如，如果在调用 `notify` 之前所有的 `enter` 调用都已与 `leave` 平衡，因此需检查这一点：

```
            if(group->action)
            {
```

如果已设置动作，则执行它：

```
                group->action();
```

一旦执行完毕，释放 `block` 并将动作设置为 `NULL`：

```
                Block_release(group->action);
                group->action = NULL;
            }
        }
    }
```

**Notify**
`ma_dispatch_group_notify` 的实现很有趣，但最终也非常简单。从概念上讲，需要考虑两种完全独立的情况：

1. 仍有一些 `enter` 调用未与 `leave` 平衡。在这种情况下，设置分组的 `action` `block`。
2. 所有 `enter` 调用都已与 `leave` 平衡。在这种情况下，立即执行 `block`。

这看起来足够直接。然而，第一种情况的简单实现会导致竞态条件（race condition）。考虑以下事件序列：

1. `notify` 函数检查 `count`，发现它非零。
2. 待处理的动作调用 `leave`，将计数减为零。
3. 将计数减为零的动作检查动作 `block`。没有设置动作，因此它什么也不做。
4. `notify` 函数设置分组的动作。
5. 动作从未运行，因为没有剩下的代码来运行它。

有一种优雅的解决方案既能修复这个竞态条件，又能将两种独立的情况合并到一条代码路径中。解决方案是将动作的赋值包裹在一对 `enter`/`leave` 中。这有效地消除了第二种情况，因为在分配动作时至少有一个未平衡的 `enter`。这也解决了潜在的竞态条件，因为赋值发生在至少一个待处理的 `leave` 调用之前。这个函数看起来像这样：

```
    void ma_dispatch_group_notify(ma_dispatch_group_t group, void (^block)(void))
    {
        ma_dispatch_group_enter(group);
        group->action = Block_copy(block);
        ma_dispatch_group_leave(group);
    }
```

**Wait**
`ma_dispatch_group_wait` 的实现概念上很简单，尽管代码略微复杂一些。它使用 `ma_dispatch_group_notify` 完成大部分工作。其思路很简单：调用 `notify` 并传入一个 `block`，该 `block` 在被运行时做出标记，然后等待该 `block` 运行。诀窍在于如何高效地等待。

可以不考虑效率而只是轮询。例如，这是一个有效但笨拙的实现：

```
    void ma_dispatch_group_wait(ma_dispatch_group_t group)
    {
        __block volatile int done = 0;
        ma_dispatch_group_notify(group, ^{
            done = 1;
        });

        while(!done)
            /* nothing */;
    }
```

然而，让 CPU 无故以 100% 占用率空转是个坏主意，所以我们试着做得更好。

实现这一点有很多不同的方法。我选择了使用 `pthread` 条件变量（condition variable）。条件变量与互斥锁（mutex）配对，允许一个线程阻塞并等待另一个线程向它发送信号。在发送信号的线程中，你执行：

```
    pthread_mutex_lock(&lock);
    // 做出你的更改
    pthread_cond_broadcast(&cond); // 或 _signal
    pthread_mutex_unlock(&lock);
```

锁确保相对于等待线程来说，更改是原子的。然后 `cond_broadcast` 调用通知任何正在等待的线程是时候唤醒了。

在等待线程中，你执行：

```
    pthread_mutex_lock(&lock);
    while(!condition)
        pthread_cond_wait(&cond);
    pthread_mutex_unlock(&lock);
```

锁确保对条件的检查相对于信号发送线程是原子的。`while` 循环有两个目的。首先，条件可能在之前就已经被设置了。在这种情况下，`while` 避免了调用 `pthread_cond_wait`，否则由于信号已经发出，它会永远等待下去。其次，即使在没有任何东西向条件变量发送信号的情况下，`pthread_cond_wait` 也可能返回。这被称为[虚假唤醒（spurious wakeup）](http://en.wikipedia.org/wiki/Spurious_wakeup)，是条件变量内部实现方式的结果。在虚假唤醒的情况下，`while` 循环确保等待线程不会过早退出。

`ma_dispatch_group_wait` 函数首先声明并初始化一个互斥锁和一个条件变量：

```
    void ma_dispatch_group_wait(ma_dispatch_group_t group)
    {
        pthread_mutex_t mutex;
        pthread_cond_t cond;

        pthread_mutex_init(&mutex, NULL);
        pthread_cond_init(&cond, NULL);
```

接下来，它获取这些变量的指针：

```
        pthread_mutex_t *mutexPtr = &mutex;
        pthread_cond_t *condPtr = &cond;
```

这样做是为了解决与 `block` 的一个不幸冲突。如果传递给 `notify` 的 `block` 直接捕获 `mutex` 和 `cond`，它们会被拷贝。这些数据类型不能容忍被拷贝。具体来说，`pthread_mutex_t` 有一些内部的对齐（alignment）检查，至少在部分实现上是如此。与其弄清楚如何强制编译器满足库的对齐需求，不如在内部为 `pthread_mutex_t` 设置一些额外的存储空间，然后在初始化时计算出内部存储的合适对齐。本质上，有一个内部字段（至少）有两个可能的位置，其位置由 `init` 决定。当变量被拷贝时，这个对齐可能就不再正确，这可能导致崩溃。通过转而捕获这些变量的指针，可以避免拷贝和潜在的崩溃。

还声明了一个 `done` 变量来跟踪 `block` 实际执行的时间：

```
        __block int done = 0;
```

现在使用一个 `block` 调用 `notify`，该 `block` 会获取锁、设置 `done`、通知等待线程、并释放锁：

```
        ma_dispatch_group_notify(group, ^{
            pthread_mutex_lock(mutexPtr);
            done = 1;
            pthread_cond_broadcast(condPtr);
            pthread_mutex_unlock(mutexPtr);
        });
```

准备好这些之后，函数等待 `done` 被设置：

```
        pthread_mutex_lock(mutexPtr);
        while(!done)
            pthread_cond_wait(condPtr, mutexPtr);
        pthread_mutex_unlock(mutexPtr);
    }
```

以上就是全部内容！

**结论**
Dispatch Groups 是一个非常实用的 API，它使得协调多个异步操作并在它们全部完成后执行后续代码变得很容易。这个 API 虽简洁，但功能强大。这样一个有用的工具实现起来相对简单。只要有正确的思路，少量代码就能发挥很大作用。

今天就到这里。下次回来将有更多奇妙的冒险。Friday Q&A 由读者建议驱动，所以在此期间，请[将你希望讨论的话题创意发送给我](mailto:mikeash.com)。

你喜欢这篇文章吗？我正在销售包含这些文章的整本书！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2013-08-16-lets-build-dispatch-groups.html)

发表你的想法，写下评论：

垃圾信息和偏离主题的帖子将被不经通知地删除。违规者可能会由我自行决定公开示众。

代码语法高亮感谢 [Pygments](http://pygments.org/) 提供支持。
