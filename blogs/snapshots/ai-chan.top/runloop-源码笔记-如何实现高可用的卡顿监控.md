---
title: Runloop 源码笔记：如何实现高可用的卡顿监控
source_url: 'https://ai-chan.top/code/Runloop%E4%B8%8E%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7/'
source_domain: ai-chan.top
source_group: single-site
original_language: zh
published: 2016-03-22
archived_at: 2026-07-27
content_hash: 'sha256:9b5634d479913df7'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 2｜先会 RunLoop，再理解常驻线程与卡顿监测（对应 W4-03）
container: '//*[contains(@class,''post-body'')]'
container_source: map
---

> 原文：[Runloop 源码笔记：如何实现高可用的卡顿监控](https://ai-chan.top/code/Runloop%E4%B8%8E%E5%8D%A1%E9%A1%BF%E7%9B%91%E6%8E%A7/)

## 背景

群里有位网友提到自己使用的 `Runloop` 卡顿监控代码无法监测到 `-tableView:didSelectRowAtIndexPath:` 场景的卡顿。

本文会将通过分析 `Runloop` 源码的方式，提供一份高可用的 `Runloop` 卡顿监测方案。

## 一、Runloop 简介

`RunLoop` 是 iOS 开发中非常基础的一个概念。

如下，对于研究 `Runloop` 的 iOS 开发者，下图应该是最为人知的一张图片。

![blob.png](https://tva1.sinaimg.cn/large/0081Kckwly1glq533sac0j30bl08tgnq.jpg)

从图片中，我们可以看到 `Runloop` 类似与一个 `do-while` 循环。

> 注意：上面的图片内容与真正的 `Runloop` 运行逻辑不符， 因为不影响本文的内容，后续有机会再写文章分析。

## 二、卡顿监控常见方案

反馈问题的网友的卡顿监测方案如下：

> 以 ”**Runloop 卡顿** “为关键字的搜索结果基本上都是采用了同样方案。

### 1、示范代码

关键代码如下：

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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
```

```objc
 // 注册
- (void)beginMonitor {
    CFRunLoopObserverContext context = {0,(__bridge void*)self,NULL,NULL};
    CFRunLoopObserverRef runLoopObserver = CFRunLoopObserverCreate(kCFAllocatorDefault,
                                              kCFRunLoopAllActivities,
                                              YES,
                                              0,
                                              &runLoopObserverCallBack,
                                              &context);
    //将观察者添加到主线程runloop的common模式下的观察中
    CFRunLoopAddObserver(CFRunLoopGetMain(), runLoopObserver, kCFRunLoopCommonModes);

    //创建子线程监控
    dispatch_async(dispatch_get_global_queue(0, 0), ^{
        int i=0;
        //子线程开启一个持续的loop用来进行监控
        while (YES) {
            long semaphoreWait = dispatch_semaphore_wait(self->dispatchSemaphore, dispatch_time(DISPATCH_TIME_NOW, 80 * NSEC_PER_MSEC));
            NSLog(@"while%@",@(i++));
            printAct(self->runLoopActivity);
            if (semaphoreWait != 0) {
                if (!self->runLoopObserver) {
                    self->timeoutCount = 0;
                    self->dispatchSemaphore = 0;
                    self->runLoopActivity = 0;
                    return;
                }
                //两个runloop的状态，BeforeSources和AfterWaiting这两个状态区间时间能够检测到是否卡顿
                if (self->runLoopActivity == kCFRunLoopBeforeSources || self->runLoopActivity == kCFRunLoopAfterWaiting) {
                    //出现三次出结果
                    if (++self->timeoutCount < 3) {
                        continue;
                    }
                    NSLog(@"调试：监测到卡顿");
                } //end activity
            }// end semaphore wait
            self->timeoutCount = 0;
        }// end while
    });
}
// 记录状态
static void runLoopObserverCallBack(CFRunLoopObserverRef observer, CFRunLoopActivity activity, void *info){
    SMLagMonitor *lagMonitor = (__bridge SMLagMonitor*)info;
    lagMonitor->runLoopActivity = activity;

    printAct(activity);

    dispatch_semaphore_t semaphore = lagMonitor->dispatchSemaphore;
    dispatch_semaphore_signal(semaphore);
}
```

下面是笔者对上述代码的思路整理

- 创建一个 `CFRunLoopObserverRef`，并提供 `runLoopObserverCallBack` 记录 `Runloop` 的 `CFRunLoopActivity` 变化
- 向 `main Runloop` 添加该 `observer`
- 开启异步线程，并以指定间隔持续监测 `CFRunLoopActivity`
- 连续 3 次检测到 `kCFRunLoopBeforeSources` 或者 `kCFRunLoopAfterWaiting` 时，认为当前处于卡顿状态，触发 **卡顿** 的数据收集

### 2、测试代码

群友的测试代码如下，通过 `-tableView:didSelectRowAtIndexPath:` 环节添加大量计算进行验证：

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

```objective
- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    int a = 8;
    NSLog(@"调试：大量计算");
    for (long i = 0; i < 999999999; i++) {
        a = a + 1;
    }
    NSLog(@"调试：大量计算结束");
}
```

当用户点击 `cell` 时，上述代码会触发一次大量计算，具体的调用栈和调试日志如下所示：

![image-02214033496](https://tva1.sinaimg.cn/large/0081Kckwly1glq53k9h2vj32380ns7wh.jpg)

从红框的 `console` 日志，我们可以发现上面**卡顿监控代码，没有任何相关的卡顿提示**。

## 三、卡顿监控失效分析

### 1、代码执行顺序

首先，我们先将监控代码与 `Runloop` 的执行顺序合并到一起进行分析：

- `Runloop` 通知 **卡顿检测代码** 进入 `kCFRunLoopBeforeWaiting` 状态
- `Runloop` 执行 `UIKit` 的 **点击事件** 逻辑
- `Runloop` 进入 **休眠状态**

  ![image-17000108309](https://tva1.sinaimg.cn/large/0081Kckwly1glq541gcx0j30qc0wi0ut.jpg)

值得重点关注的是上图两个回调的执行顺序：`卡顿监控` 比 `点击事件` 更早接收到 `kCFRunLoopBeforeWaiting` 事件。

当 `点击事件` 执行时，异步线程会因为 `卡顿监控`先接到 `kCFRunLoopBeforeWaiting`状态，导致**错误认为 `Runloop` 处于睡眠状态**。

所以，**为了解决`卡顿监控` 代码无法检测 `tableView:didSelectRowAtIndexPath:` 的现象，我们需要将 `kCFRunLoopBeforeWaiting_卡顿监控` 调用时机进行调整**。

### 2、 `__CFRunLoopDoObservers` 函数的执行逻辑

为了**调整回调的执行顺序**，我们需要先了解 `__CFRunLoopDoObservers` 函数的执行逻辑。

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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
```

```objc
/* rl is locked, rlm is locked on entrance and exit */
static void __CFRunLoopDoObservers(CFRunLoopRef rl, CFRunLoopModeRef rlm, CFRunLoopActivity activity) __attribute__((noinline));
static void __CFRunLoopDoObservers(CFRunLoopRef rl, CFRunLoopModeRef rlm, CFRunLoopActivity activity) {    /* DOES CALLOUT */

    cf_trace(KDEBUG_EVENT_CFRL_IS_DOING_OBSERVERS | DBG_FUNC_START, rl, rlm, activity, 0);

    CHECK_FOR_FORK();
    // 获取 runLoopMode 的 observer 数量，如果小于1，则直接返回
    CFIndex cnt = rlm->_observers ? CFArrayGetCount(rlm->_observers) : 0;
    if (cnt < 1) return;

    /* Fire the observers */
    STACK_BUFFER_DECL(CFRunLoopObserverRef, buffer, (cnt <= 1024) ? cnt : 1);
    CFRunLoopObserverRef *collectedObservers = (cnt <= 1024) ? buffer : (CFRunLoopObserverRef *)malloc(cnt * sizeof(CFRunLoopObserverRef));
    CFIndex obs_cnt = 0;
    // 1、顺序遍历 _observers，
    // 因为每个 observer 可以观察不同的 activity，所以，需要通过 & 操作符过滤需要触发的 observer
    // 并组成新的数组 collectedObservers
    for (CFIndex idx = 0; idx < cnt; idx++) {
        CFRunLoopObserverRef rlo = (CFRunLoopObserverRef)CFArrayGetValueAtIndex(rlm->_observers, idx);
        // 【避免递归】1、通过 __CFRunLoopObserverIsFiring 判断是否处于执行状态
        if (0 != (rlo->_activities & activity) && __CFIsValid(rlo) && !__CFRunLoopObserverIsFiring(rlo)) {
            collectedObservers[obs_cnt++] = (CFRunLoopObserverRef)CFRetain(rlo);
        }
    }
    __CFRunLoopModeUnlock(rlm);
    __CFRunLoopUnlock(rl);
    // 2、顺序遍历 collectedObservers
    for (CFIndex idx = 0; idx < obs_cnt; idx++) {
        CFRunLoopObserverRef rlo = collectedObservers[idx];
        __CFRunLoopObserverLock(rlo);
        if (__CFIsValid(rlo)) {
            // 【非重复 observer】1、记录是否属于非重复 observer
            Boolean doInvalidate = !__CFRunLoopObserverRepeats(rlo);
            // 【避免递归】2、回调前，通过 __CFRunLoopObserverSetFiring 记录执行的状态
            __CFRunLoopObserverSetFiring(rlo);
            __CFRunLoopObserverUnlock(rlo);
            CFRunLoopObserverCallBack callout = rlo->_callout;
            void *info = rlo->_context.info;
            cf_trace(KDEBUG_EVENT_CFRL_IS_CALLING_OBSERVER | DBG_FUNC_START, callout, rlo, activity, info);
            // 3、执行 observer 的回调
            __CFRUNLOOP_IS_CALLING_OUT_TO_AN_OBSERVER_CALLBACK_FUNCTION__(callout, rlo, activity, info);
            cf_trace(KDEBUG_EVENT_CFRL_IS_CALLING_OBSERVER | DBG_FUNC_END, callout, rlo, activity, info);
            // 【非重复 observer】2、非重复 observer，在回调完毕后，直接销毁
            if (doInvalidate) {
                CFRunLoopObserverInvalidate(rlo);
            }
            // 【避免递归】3、回调后，通过 __CFRunLoopObserverUnsetFiring 恢复状态
            __CFRunLoopObserverUnsetFiring(rlo);
        } else {
            __CFRunLoopObserverUnlock(rlo);
        }
        CFRelease(rlo);
    }
    __CFRunLoopLock(rl);
    __CFRunLoopModeLock(rlm);

    if (collectedObservers != buffer)
        free(collectedObservers);

    cf_trace(KDEBUG_EVENT_CFRL_IS_DOING_OBSERVERS | DBG_FUNC_END, rl, rlm, activity, 0);
}
```

值得注意的是，`__CFRunLoopMode` 持有一个数组类型的结构成员： `_observers`

![image-17000157559](https://tva1.sinaimg.cn/large/0081Kckwly1glq54wc3dcj30g0080mxb.jpg)

- `__CFRunLoopDoObservers` 会先遍历 `_observers` ，并根据各种条件组成一个新的数组 `collectedObservers`
- 新的数组生成后，会再次遍历 `collectedObservers`，并通过 `__CFRUNLOOP_IS_CALLING_OUT_TO_AN_OBSERVER_CALLBACK_FUNCTION__` 回调监控函数

所以，我们可以得到第一个重要的结论：**通过控制 `_observers` 数组的排列顺序，能够改变调用时机**。

### 3、CFRunLoopAddObserver 函数的执行逻辑

为了控制 `_observers` 数组的排列顺序，我们还需要先看看 `CFRunLoopAddObserver` 函数的执行逻辑。

如下，创建 `CFRunLoopObserverRef` 时，开发者可以传入 `CFIndex order` 参数

```
1
```

```objective
CF_EXPORT CFRunLoopObserverRef CFRunLoopObserverCreate(CFAllocatorRef allocator, CFOptionFlags activities, Boolean repeats, CFIndex order, CFRunLoopObserverCallBack callout, CFRunLoopObserverContext *context);
```

![image-17000220812](https://tva1.sinaimg.cn/large/0081Kckwly1glq55ad1e3j30dc05amx8.jpg)

`CFRunLoopAddObserver` 函数内部会根据 `CFRunLoopObserverRef` 的 `_order` 逆序遍历 `CFRunLoopRef` 的 `_observers`，并找到合适的位置进行插入

具体的源码如下所示：

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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
```

```objc
// 添加 observer
void CFRunLoopAddObserver(CFRunLoopRef rl, CFRunLoopObserverRef rlo, CFStringRef modeName) {
    CHECK_FOR_FORK();
    CFRunLoopModeRef rlm;
    // 如果 runloop 处于销毁状态，直接返回
    if (__CFRunLoopIsDeallocating(rl)) return;
    // 如果主线程已经停止执行，则直接返回
    if (__CFMainThreadHasExited && rl == CFRunLoopGetMain()) {
        static dispatch_once_t onceToken;
        dispatch_once(&onceToken, ^{
            CFLog(kCFLogLevelError, CFSTR("Attempting to add observer to main runloop, but the main thread has exited. This message will only log once. Break on _CFRunLoopError_MainThreadHasExited to debug."));
        });
        _CFRunLoopError_MainThreadHasExited();
        return;
    }
    // 合规性校验 & 防止重入
    if (!__CFIsValid(rlo) || (NULL != rlo->_runLoop && rlo->_runLoop != rl)) return;

    __CFRunLoopLock(rl);
    // 1、如果监听 kCFRunLoopCommonModes，则遍历 _commonModes，并进行监听
    if (modeName == kCFRunLoopCommonModes) {
        CFSetRef set = rl->_commonModes ? CFSetCreateCopy(kCFAllocatorSystemDefault, rl->_commonModes) : NULL;
        if (NULL == rl->_commonModeItems) {
            rl->_commonModeItems = CFSetCreateMutable(kCFAllocatorSystemDefault, 0, &kCFTypeSetCallBacks);
        }
        CFSetAddValue(rl->_commonModeItems, rlo);
        if (NULL != set) {
            CFTypeRef context[2] = {rl, rlo};
            /* add new item to all common-modes */
            CFSetApplyFunction(set, (__CFRunLoopAddItemToCommonModes), (void *)context);
            CFRelease(set);
        }
    } else {
        rlm = __CFRunLoopFindMode(rl, modeName, true);
        if (NULL != rlm && NULL == rlm->_observers) {
            rlm->_observers = CFArrayCreateMutable(kCFAllocatorSystemDefault, 0, &kCFTypeArrayCallBacks);
        }
        if (NULL != rlm && !CFArrayContainsValue(rlm->_observers, CFRangeMake(0, CFArrayGetCount(rlm->_observers)), rlo)) {
                Boolean inserted = false;
                // 2、逆序遍历 _observers，并找到合适的位置进行插入
                for (CFIndex idx = CFArrayGetCount(rlm->_observers); idx--; ) {
                    CFRunLoopObserverRef obs = (CFRunLoopObserverRef)CFArrayGetValueAtIndex(rlm->_observers, idx);
                    if (obs->_order <= rlo->_order) {
                        CFArrayInsertValueAtIndex(rlm->_observers, idx + 1, rlo);
                        inserted = true;
                        break;
                    }
                }
                if (!inserted) {
                CFArrayInsertValueAtIndex(rlm->_observers, 0, rlo);
                }
            rlm->_observerMask |= rlo->_activities;
            __CFRunLoopObserverSchedule(rlo, rl, rlm);
        }
        if (NULL != rlm) {
            __CFRunLoopModeUnlock(rlm);
        }
    }
    __CFRunLoopUnlock(rl);
}
```

为了方便读者理解上面的逻辑，我们通过一个具体的示例进行讲解。

如下，假设现有的 `observers` 的 `order` 是 `0`、`8`、 `12`，新插入的 `observers` 的 `order` 分别是 `0` 和 `10`；

则，两个 `observers` 会分别插入到 `stub0` 和 `stub1` 位置。

所以，我们可以得到第二个重要结论： **通过调整 `CFRunLoopObserverCreate` 的 `order` 参数，可以调整两个回调的执行顺序。**

![image-17000244565](https://tva1.sinaimg.cn/large/0081Kckwly1glq55pda4gj30q40r6gn6.jpg)

## 四、高可用的 **Runloop 卡顿监测方案**

根据前面的两个结论，我们可以采用将 `order` 调整到 `LONG_MAX` 的方式改变调用顺序：

### 1、优化方案

```
1
2
3
4
5
6
```

```objc
runLoopObserver = CFRunLoopObserverCreate(kCFAllocatorDefault,
                                          kCFRunLoopAllActivities,
                                          YES,
                                          LONG_MAX,
                                          &runLoopObserverCallBack,
                                          &context);
```

重新编译&运行APP后，我们可以发现 `console` 的内容变成如下：

![image-03013224495](https://tva1.sinaimg.cn/large/0081Kckwly1glq55ujmrjj30ja0x27fq.jpg)

### 2、高可用方案

相信聪明的读者很容易发现**上面的优化方案仍然存在下面的badcase**。

当 `kCFRunLoopAfterWaiting_其它阻塞事件` 位置发生卡顿时，新方案因为执行顺序比较晚，卡顿监控代码仍然认为当前处于休眠状态，导致无法进行卡顿监控。

![image-17000304903](https://tva1.sinaimg.cn/large/0081Kckwly1glq562w40yj30rk0we40n.jpg)

针对上面的情况，我们可以使用的**双 `Observer`** 的方式处理：

- 第一个 **`Observer`** 的 `order` 调整到 `LONG_MIN`

    - 进入 `kCFRunLoopAfterWaiting` 状态时，第一个被调用，用于监控 `Runloop` 处于 **运行状态**
- 第二个 **`Observer`** 的 `order` 调整到 `LONG_MAX`

    - 进入 `kCFRunLoopBeforeWaiting` 状态时，最后一个被调用，用于判断 `Runloop` 处于 **睡眠状态**

如下图所示，通过 **双 `Observer`** ，我们可以更加准确的判断`Runloop` 的运行状态，从而对卡顿进行更加有效的监控。

![image-17000342009](https://tva1.sinaimg.cn/large/0081Kckwly1glq56pi1syj30u010o0vg.jpg)

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
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
```

```objc
- (void)addRunLoopObserver
{
    NSRunLoop *curRunLoop = [NSRunLoop currentRunLoop];

    // 第一个监控，监控是否处于 **运行状态**
    CFRunLoopObserverContext context = {0, (__bridge void *) self, NULL, NULL, NULL};
    CFRunLoopObserverRef beginObserver = CFRunLoopObserverCreate(kCFAllocatorDefault, kCFRunLoopAllActivities, YES, LONG_MIN, &myRunLoopBeginCallback, &context);
    CFRetain(beginObserver);
    m_runLoopBeginObserver = beginObserver;

    //  第二个监控，监控是否处于 **睡眠状态**
    CFRunLoopObserverRef endObserver = CFRunLoopObserverCreate(kCFAllocatorDefault, kCFRunLoopAllActivities, YES, LONG_MAX, &myRunLoopEndCallback, &context);
    CFRetain(endObserver);
    m_runLoopEndObserver = endObserver;

    CFRunLoopRef runloop = [curRunLoop getCFRunLoop];
    CFRunLoopAddObserver(runloop, beginObserver, kCFRunLoopCommonModes);
    CFRunLoopAddObserver(runloop, endObserver, kCFRunLoopCommonModes);

}

// 第一个监控，监控是否处于 **运行状态**
void myRunLoopBeginCallback(CFRunLoopObserverRef observer, CFRunLoopActivity activity, void *info)
{
    g_runLoopActivity = activity;
    g_runLoopMode = eRunloopDefaultMode;
    switch (activity) {
        case kCFRunLoopEntry:
            g_bRun = YES;
            break;
        case kCFRunLoopBeforeTimers:
            if (g_bRun == NO) {
                gettimeofday(&g_tvRun, NULL);
            }
            g_bRun = YES;
            break;
        case kCFRunLoopBeforeSources:
            if (g_bRun == NO) {
                gettimeofday(&g_tvRun, NULL);
            }
            g_bRun = YES;
            break;
        case kCFRunLoopAfterWaiting:
            if (g_bRun == NO) {
                gettimeofday(&g_tvRun, NULL);
            }
            g_bRun = YES;
            break;
        case kCFRunLoopAllActivities:
            break;
        default:
            break;
    }
}

//  第二个监控，监控是否处于 **睡眠状态**
void myRunLoopEndCallback(CFRunLoopObserverRef observer, CFRunLoopActivity activity, void *info)
{
    g_runLoopActivity = activity;
    g_runLoopMode = eRunloopDefaultMode;
    switch (activity) {
        case kCFRunLoopBeforeWaiting:
            gettimeofday(&g_tvRun, NULL);
            g_bRun = NO;
            break;
        case kCFRunLoopExit:
            g_bRun = NO;
            break;
        case kCFRunLoopAllActivities:
            break;
        default:
            break;
    }
}
```

## 五、总结

本文通过分析 `__CFRunLoopDoObservers` 函数 和 `CFRunLoopAddObserver` 函数的内部逻辑，分析了网络上广泛流传的 **Runloop 卡顿监测方案** 存在低可用性问题的原因，并给出了一份高可用的 **Runloop 卡顿监测方案** 。

> 完整代码，可以访问 腾讯 的 [matrix](https://github.com/Tencent/matrix/blob/master/matrix/matrix-iOS/Matrix/WCCrashBlockMonitor/CrashBlockPlugin/Main/BlockMonitor/WCBlockMonitorMgr.mm#L815-L844) 仓库获取
