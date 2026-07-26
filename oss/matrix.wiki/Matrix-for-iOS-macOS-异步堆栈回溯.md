### 前言

------

在当前微信耗电监控上报的堆栈当中，我们发现了大量与 GCD 异步调用相关的系统堆栈，如下图所示。而真正与业务相关的堆栈却“不见踪影”，这样的堆栈信息无法帮助我们确定耗电问题出现的具体位置。
![image.png](https://i.loli.net/2019/11/12/TR3wUVBmqPzDHdv.png)
为了确定程序中真正耗电的函数，我们自然想到，如果能知道是谁发起了这个异步线程，那么问题就解决了。
在 iOS 开发过程中，使用 Xcode 对一段程序进行断点调试可以发现：对于异步执行的线程，它能够回溯到其调用线程，得到完整的线程堆栈。如下图所示。
![image.png](https://i.loli.net/2019/11/12/UjZmtuqMaA7l5P4.png)
经 Xcode 的启发，我们完善了 Matrix 耗电监控的堆栈上报过程，现在耗电监控也能获得异步线程完整的堆栈结果了。

### 异步堆栈回溯实现

------

对于 Xcode 异步堆栈的回溯方式，苹果在 [《QUEUE DEBUGGING USING STORED BACKTRACE INFORMATION》](http://www.freepatentsonline.com/9378117.html) 一文中详细介绍了其实现流程。其关键步骤为：

- 分别利用两个环境变量 `DYLD_LIBRARY_PATH` 和 `DYLD_INSERT_LIBRARIES` 完成了 dispatch 函数的 hook 和 backtrace 。

```
DYLD_LIBRARY_PATH = /usr/system/instropection
DYLD_INSERT_LIBRARIES = /Application/Xcode.app/Contents/Developer/user/lib/libBacktraceRecording.dylib
```

其中，`DYLD_LIBRARY_PATH` 决定了目标线程在调用 dispatch 函数时，将会使用 “instropection” 版本的库文件，而不是从标准库中去寻找。 而 “instropection” 版本的库文件，提供了能够使第三方模块 hook dispatch 函数的功能。

`DYLD_INSERT_LIBRARIES` 在 hook 到该函数后，将会插入新的动态库完成异步堆栈回溯的功能。

- 记录发起异步线程的堆栈，并与被发起的异步线程关联。
- 需要上报异步线程的堆栈时，将该异步线程回溯得到的堆栈与发起该异步线程的堆栈进行重组，得到完整的堆栈进行上报。

和苹果一样，我们参考上述思路完善了 Matrix 耗电监控的异步堆栈回溯过程，具体方案如下：
![](https://i.loli.net/2019/11/12/X1NcriM9ue2m7Ho.png)
首先，在每个线程发起异步线程时，我们会 hook 这个 dispatch 函数，并且获得此时的调用堆栈。如上图所示，线程 Thread 1 在某一时刻发起了异步任务 T1_1 ，Matrix 会在此时获取当前 Thread 1 线程的调用堆栈 SF1_1 。异步任务 T1_1 开启了一个新的线程 Thread 2 ，此时我们将该线程 Thread 2 与 SF1_1 关联起来，并保存到 Stack Pool 当中。

在这里，需要解释一下，在 Matrix 中 Stack Pool 是如何保存异步堆栈的？以及异步线程与之前的堆栈又是如何关联起来的？

在 Matrix 当中，Stack Pool 是利用一个名为 asyncOriginThreadDict 的全局 NSMutableDictionary 实现的，其中它的 key 记录了异步线程的线程 ID，value 记录了发起异步任务之前原始线程的堆栈信息。而异步线程与堆栈的关联，也就是通过将线程 ID 与当前的堆栈信息保存到 asyncOriginThreadDict 当中。如上图，Matrix 将 SF1_1 与 Thread 2 关联并保存到 Stack Pool 的过程，可以通过下面一行代码实现：

```objective-c
[asyncOriginThreadDict setObject:SF1_1 forKey:ID(Thread 2)];
```

其中：SF1_1 表示发起异步任务 T1_1 时，线程 Thread 1 的堆栈信息；ID(Thread 2) 表示 Thread 2 的线程 ID。

整个执行过程的部分代码如下：

```objective-c
/// hook the dispatch function, and associate the stack with async thread
/// @param block: the block submitted to dispatch queues
/// @return newBlock: the block after been hooked
static inline dispatch_block_t blockRecordAsyncTrace(dispatch_block_t block)
{
    // 1. get origin stack
    AsyncStackTrace stackTrace = getCurAsyncStackTrace();
    NSMutableArray *stackArray = [[NSMutableArray alloc] init];
    for (int i = 0; i < stackTrace.size; i++)
    {
        NSNumber *temp =[NSNumber numberWithUnsignedLong:(unsigned long)stackTrace.backTrace[i]];
        [stackArray addObject:temp];
    }
    
    // 2. execute the block
    dispatch_block_t newBlock = ^() {
        pthread_mutex_lock(&m_threadLock);
        thread_t current_thread = (thread_t)ksthread_self();
        NSNumber *key = [[NSNumber alloc] initWithInt:current_thread];

        // associate the stack with async thread
        [asyncOriginThreadDict setObject:stackArray forKey:key];
        pthread_mutex_unlock(&m_threadLock);
        
        block();
    };
    
    // 3. return the new block
    return newBlock;
}
```

当 Thread 2 执⾏到任务 T2_1 时，假设此时发生了耗电严重的情况，此时 Matrix 将对该线程进行回溯得到其堆栈 SF2_1。同时，Matrix 会到 Stack Pool 当中去查找，是否存在与 Thread 2 关联的堆栈，如果有则将其与 SF2_1 组合起来。在图中，Matrix 找到了发起异步线程 Thread 2 之前的堆栈 SF1_1 ，并将 SF1_1 与 SF2_1 组合形成一个完整的调用堆栈，进而将这个完整的调用堆栈作为线程 Thread 2 的耗电堆栈。

在程序实际执行的过程当中，耗电严重的情况可能是由多个线程一起作用造成的。按照上面的方式，Matrix 将所有耗电线程的堆栈进行回溯后拿到完整的耗电堆栈，作为此刻程序执行过程的耗电堆栈进行上报。

对于 dispatch 函数的 hook 过程，我们使用 [fishhook](https://github.com/facebook/fishhook) 去拦截 dispatch 的各个异步接口，进而记录各自的异步堆栈。

dispatch 的异步接口一共包括 async / async_f / after / after_f / barrier_async / barrier_async_f 六个，这六个接口按照执行函数的类型可以分为 block 和 func 两类，而我们的 hook 方式也是分为这两类来进行的。

- 对于 block 类型：

我们在 hook 到 async / after / barrier_async 函数的时候，首先我们将获得当前线程的堆栈，并在执行 block 之前，完成堆栈与异步线程的关联和存储，然后再执行 block。

- 对于 func 类型：

我们在 hook 到 async_f / after_f / barrier_async_f 函数的时候，首先同样获得当前线程的堆栈，在执行 func 之前，通过构建一个结构体，将 hook 得到参数、func、以及堆栈记录到该结构体当中，完成堆栈与异步线程的关联和存储，然后再接着执行 func 任务。

对于 hook 的具体实现细节，大家可以参考上述的这篇文章，这里就不再赘述了。

### 异步堆栈回溯改进效果

------

通过上述方案，完善后的耗电堆栈最终上报的结果如下图所示：
修改前：
![](https://i.loli.net/2019/11/12/KGilysP2M6hDApY.png)
修改后：
![](https://i.loli.net/2019/11/12/5wngTab73oDsUr8.png)

### iOS 13 下遇到的闪退问题

------

当上述开发看似一切顺利的时候，测试同学却过来反馈说，异步线程堆栈回溯的功能添加后，微信一打开就会闪退。查看闪退堆栈后发现，是 fishhook 造成的。深究其原因，原来是在 iOS 13 beta 中，苹果又更新了一些细节。

问题原因：iOS 13 beta 为了改善系统性能和安全性，静态连接器将标记为常量的全局变量移动到了一个新的段中：`__DATA_CONST`。这些全局变量可能由编译器生成的指针构成，动态链接器需要在加载期间修复这些指针。一旦动态链接器完成加载映像，它就会使 `__DATA_CONST` 变成只读。当 fishhook 函数 hook 到 `__DATA_CONST` 时，对其进行写操作将会造成 Crash。

解决办法：当 hook 到 `__DATA_CONST` 时，在写之前改变其属性，让它可以 writable。

更可喜的是，fishhook 在 #issue 66 中已经 fix 了这个问题，有用到 fishhook 的同事建议关注一下，看看你的代码中是否需要同步这个修改。