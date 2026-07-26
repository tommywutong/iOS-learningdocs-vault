---
title: macOS 10.13 中的 Objective-C 与 fork()
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html'
original_language: en
published: 2017-06-05
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9a00adfc7fb64ea3'
translated: true
---

> 原文：[macOS 10.13 中的 Objective-C 与 fork()](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **博客**  
 [最近](http://sealiesoftware.com/blog/index.html)  
 [归档](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **项目**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium 归档

[归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：非指针 isa](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html)

**macOS 10.13 中的 Objective-C 与 fork()** ([2017-6-5 12:05 PM](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html))

在 macOS 10.13 中，`fork()` 和 `exec()` 之间使用 Objective-C 的规则发生了变化。过去那些大部分时候碰巧能跑通的错误代码，现在可能会失败。目前有一些变通办法可用。

#### `fork()` 与 Objective-C

在 macOS 10.13 之前，Objective-C runtime 不支持在一个多线程父进程的子进程中、于 `fork()` 与 `exec()` 之间使用它。在这段区间内调用任何 Objective-C 方法都是不允许的。大多数时候它可能能跑通。但有时会失败：比如说，如果父进程中的某个线程在 `fork()` 发生时恰好持有 Objective-C runtime 的某把锁，子进程在试图获取那把锁时就会死锁。

从 macOS 10.13 起，用 10.13 SDK 构建的应用中，Objective-C runtime 现在支持在 `fork()` 与 `exec()` 之间使用它了。这里有一些和 `+initialize` 方法相关的限制。以前不正确的代码现在可能变得正确了，也可能因为 `+initialize` 的行为而稳定地失败。

请注意，操作系统框架定义的 Objective-C 类依然是不支持 `fork` 的。作为第一近似的判断，在 `fork()` 与 `exec()` 之间做任何事情仍然是不正确的。

#### `fork()` 与 `+initialize`

`+initialize` 方法在 `fork()` 周围仍然有限制。问题在于 `+initialize` 的线程安全保证，隐式地在 Objective-C runtime 无法控制的状态周围引入了锁。没有什么好办法能让 `+initialize` 同时做到线程安全和 `fork` 安全。于是 Objective-C runtime 索性直接让进程停止运行，而不是在子进程里运行任何 `+initialize` 的重写实现：

```
      +[SomeClass initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead.
```

如果你有一个既需要 `fork` 安全、又重写了 `+initialize` 的类，你可以用 `pthread_atfork()` 的 "prepare" 那一侧来强制让 `+initialize` 先运行。这样子进程就会看到一个一致的状态，而不会有 `+initialize` 死锁的风险。

#### 兼容性方面的变通办法

有三种方式可以为了源码兼容或二进制兼容而恢复旧的行为。

- 用早于 macOS 10.13 的 SDK 构建你的 App。
- 定义环境变量 `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`。
- 给你的可执行文件添加一个 `__DATA,__objc_fork_ok` section。

需要提醒的是，即便用上了这些变通办法中的某一个，在 macOS 10.13 上，不正确的代码依然比以前更容易死锁。

#### 脚本语言

有些脚本语言会用不带 `exec()` 的 `fork()` 来替代线程。Python 的 `multiprocessing` 模块就是一例。上面提到的 `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` 环境变量，或许能让你的脚本暂时重新跑起来。

#### 修复方案汇总

针对 `fork` 安全问题的可能修复方案，从最好到最差依次是：

1. 用 `NSTask` 或 `posix_spawn()` 代替 `fork()` 和 `exec()`。
2. 在 `fork()` 和 `exec()` 之间什么都不做。
3. 在 `fork()` 和 `exec()` 之间只使用异步信号安全（async-signal-safe）的操作。
4. 在 `fork()` 和 `exec()` 之间，使用没有重写 `+initialize` 的 ObjC 类。
5. 用 `pthread_atfork()` 强制让你的 `+initialize` 方法在 `fork()` 之前运行。
6. 定义环境变量 `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`，或添加一个 `__DATA,__objc_fork_ok` section，或者用早于 macOS 10.13 的 SDK 构建。然后祈祷吧。

[Sealie Software](http://sealiesoftware.com/index.html)
