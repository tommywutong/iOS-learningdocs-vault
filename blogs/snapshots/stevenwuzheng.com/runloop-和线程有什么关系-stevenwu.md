---
title: runloop 和线程有什么关系？ - stevenwu
source_url: 'http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB'
source_domain: stevenwuzheng.com
source_group: single-site
original_language: zh
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:4143db317cdd3025'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 2｜了解原始线程，目的是理解上层抽象（对应 W3-03、W3-04）
container: '//div[contains(@class,''card-content'') and contains(@class,''article'')]'
container_source: map
---

> 原文：[runloop 和线程有什么关系？ - stevenwu](http://stevenwuzheng.com/archives/runloop%E5%92%8C%E7%BA%BF%E7%A8%8B%E6%9C%89%E4%BB%80%E4%B9%88%E5%85%B3%E7%B3%BB)

2021-12-08

# runloop 和线程有什么关系？

### runloop 和线程有什么关系？

首先，iOS 开发中能遇到两个线程对象: pthread_t 和 NSThread。过去苹果有份文档标明了 NSThread 只是 pthread_t 的封装，但那份文档已经失效了，现在它们也有可能都是直接包装自最底层的 mach thread。苹果并没有提供这两个对象相互转换的接口，但不管怎么样，可以肯定的是 pthread_t 和 NSThread 是一一对应的。

比如，你可以通过 pthread_main_thread_np()或 [NSThread mainThread]来获取主线程； 也可以通过 pthread_self()或[NSThread currentThread]来获取当前线程。

CFRunLoop 是基于 pthread 来管理的。  
 苹果不允许直接创建 RunLoop，它只提供了两个自动获取的函数：CFRunLoopGetMain()和 CFRunLoopGetCurrent()。

这两个函数内部的逻辑大概是下面这样:

```
    /// 全局的Dictionary，key 是 pthread_t， value 是 CFRunLoopRef
    static CFMutableDictionaryRef loopsDic;
    /// 访问 loopsDic 时的锁
    static CFSpinLock_t loopsLock;
     
    /// 获取一个 pthread 对应的 RunLoop。
    CFRunLoopRef _CFRunLoopGet(pthread_t thread) {
        OSSpinLockLock(&loopsLock);
        
        if (!loopsDic) {
            // 第一次进入时，初始化全局Dic，并先为主线程创建一个 RunLoop。
            loopsDic = CFDictionaryCreateMutable();
            CFRunLoopRef mainLoop = _CFRunLoopCreate();
            CFDictionarySetValue(loopsDic, pthread_main_thread_np(), mainLoop);
        }
        
        /// 直接从 Dictionary 里获取。
        CFRunLoopRef loop = CFDictionaryGetValue(loopsDic, thread));
        
        if (!loop) {
            /// 取不到时，创建一个
            loop = _CFRunLoopCreate();
            CFDictionarySetValue(loopsDic, thread, loop);
            /// 注册一个回调，当线程销毁时，顺便也销毁其对应的 RunLoop。
            _CFSetTSD(..., thread, loop, __CFFinalizeRunLoop);
        }
        
        OSSpinLockUnLock(&loopsLock);
        return loop;
    }
     
    CFRunLoopRef CFRunLoopGetMain() {
        return _CFRunLoopGet(pthread_main_thread_np());
    }
     
    CFRunLoopRef CFRunLoopGetCurrent() {
        return _CFRunLoopGet(pthread_self());
    }
```

从上面的代码可以看出，线程和 RunLoop 之间是一一对应的，其关系是保存在一个全局的 Dictionary 里。线程刚创建时并没有 RunLoop，如果你不主动获取，那它一直都不会有。RunLoop 的创建是发生在第一次获取时，RunLoop 的销毁是发生在线程结束时。你只能在一个线程的内部获取其 RunLoop（主线程除外）。
