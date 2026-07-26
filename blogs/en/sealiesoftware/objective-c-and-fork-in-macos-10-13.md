---
title: Objective-C and fork() in macOS 10.13
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html'
original_language: en
published: 2017-06-05
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:9a00adfc7fb64ea3'
translated: false
---

> 原文：[Objective-C and fork() in macOS 10.13](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

[archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Non-pointer isa](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html)

**Objective-C and fork() in macOS 10.13** ([2017-6-5 12:05 PM](http://sealiesoftware.com/blog/archive/2017/6/5/Objective-C_and_fork_in_macOS_1013.html))

The rules for using Objective-C between `fork()` and `exec()` have changed in macOS 10.13. Incorrect code that happened to work most of the time in the past may now fail. Some workarounds are available.

#### `fork()` and Objective-C

Before macOS 10.13, the Objective-C runtime did not support use between `fork()` and `exec()` in the child process of a multithreaded parent process. Calling any Objective-C method in that interval was not allowed. Most of the time it might work. Sometimes it would fail: for example, if a thread in the parent process happened to be holding one of the Objective-C runtime's locks when the `fork()` occurred, the child process would deadlock when it tried to take that lock.

As of macOS 10.13, the Objective-C runtime now supports use between `fork()` and `exec()` in applications built with the 10.13 SDK. There are restrictions involving `+initialize` methods. Previously incorrect code may now be correct, or it may fail consistently due to `+initialize` behavior.

Note that the Objective-C classes defined by the OS frameworks remain `fork`-unsafe. As a first approximation it is still incorrect to do anything between `fork()` and `exec()`.

#### `fork()` and `+initialize`

`+initialize` methods still have restrictions around `fork()`. The problem is that the thread-safety guarantees of `+initialize` implicitly introduce locks around state that the Objective-C runtime does not control. There is no good way to make `+initialize` both thread-safe and `fork`-safe. Instead the Objective-C runtime simply halts the process instead of running any `+initialize` override in the child process:

```
      +[SomeClass initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead.
```

If you have a class that needs to be `fork`-safe and also overrides `+initialize`, you can use the "prepare" side of `pthread_atfork()` to force `+initialize` to run. Then the child process will see a consistent state without a `+initialize` deadlock threat.

#### Workarounds for compatibility

There are three ways to get the old behavior back for source- or binary-compatibility.

- Build your app with an SDK older than macOS 10.13.
- Define environment variable `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`.
- Add a `__DATA,__objc_fork_ok` section to your executable.

Be warned that incorrect code is more likely to deadlock on macOS 10.13 than before, even with one of these workarounds in place.

#### Scripting languages

Some scripting languages use `fork()` without `exec()` as a substitute for threads. Python's `multiprocessing` module is one example. The `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES` environment variable described above may temporarily get your scripts running again.

#### Summary of fixes

Possible fixes for `fork`-safety problems, from best to worst:

1. Use `NSTask` or `posix_spawn()` instead of `fork()` and `exec()`.
2. Do nothing between `fork()` and `exec()`.
3. Use only async-signal-safe operations between `fork()` and `exec()`.
4. Use ObjC classes with no `+initialize` overrides between `fork()` and `exec()`.
5. Use `pthread_atfork()` to force your `+initialize` methods to run before `fork()`.
6. Define environment variable `OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES`, or add a `__DATA,__objc_fork_ok` section, or build using an SDK older than macOS 10.13. Then cross your fingers.

[Sealie Software](http://sealiesoftware.com/index.html)
