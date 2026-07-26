---
title: '[objc explain]：你在 objc_msgSend() 里崩溃了'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html'
original_language: en
published: 2008-09-22
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6cf68bad0382d80'
translated: true
---

> 原文：[[objc explain]：你在 objc_msgSend() 里崩溃了](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Mac OS X 版 Valgrind（需要自行组装）](http://sealiesoftware.com/blog/archive/2008/09/28/Valgrind_for_Mac_OS_X_some_assembly_required.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：异常与自动释放池](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html)

**[objc explain]：你在 objc_msgSend() 里崩溃了** ([2008-09-22 02:02 PM](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html))

好了，你在 `objc_msgSend()` 里崩溃了。现在该怎么办？

最有可能的情况是，你给一个已经被释放掉的对象发送了消息。又或者你的指针本身完全正确，但别人把这个对象的内容给弄乱了——也许是附近某块分配区里的缓冲区溢出，又或者是用了一个悬空指针，而这个指针曾经指向的内存现在正好被你的对象占用着。偶尔 `objc_msgSend()` 崩溃是因为某个内存错误砸坏了 runtime 自己的数据结构，但通常问题都出在接收者对象自身上。

不管你是在调试器里，还是在看一份崩溃日志，你都能从中恢复出比调用栈回溯（backtrace）更多的信息，来诊断这次崩溃。

#### 接收者和选择器寄存器

`objc_msgSend()` 在工作时，会把接收者对象和选择器存放在 CPU 寄存器里。这些值能帮你诊断问题。

寄存器的名字会因体系结构、以及所用的 `objc_msgSend()` 变体而不同。下面这张表对 Mac OS X Leopard 是准确的，对 Snow Leopard 大概率也依然准确。

|  | `receiver` | `SEL` | `receiver` | `SEL` |
|---|---|---|---|---|
| i386 | eax* | ecx | eax* | ecx |
| x86_64 | rdi | rsi | rsi | rdx |
| ppc | r3 | r4 | r4 | r5 |
| ppc64 | r3 | r4 | r4 | r5 |
| arm | r0 | r1 | r1 | r2 |
| arm64 | x0 | x1 | — | — |

* i386 说明：接收者在大多数崩溃里都在 eax 中，但不是全部。如果你设法在 `objc_msgSend()` 内部走得比较深才崩溃，那 eax 就可能是别的值了。

#### 解读接收者地址与无效地址

你可以利用接收者的地址、以及导致崩溃的那个无效地址，来获得一些关于底层问题的线索。在崩溃日志里，接收者的地址会在 Thread State 里、用上表中的寄存器名字标出；无效地址则列在顶部（通常类似 `KERN_PROTECTION_FAILURE at <invalid address>` 这样的形式）。在调试器控制台里，程序停下来时会打印出无效地址，而你可以用上表中的寄存器名字打印出接收者的地址。

```
    Program received signal EXC_BAD_ACCESS, Could not access memory.
    Reason: KERN_PROTECTION_FAILURE at address: 0x00000001
    0x00090ec4 in objc_msgSend ()
    (gdb) p/x $eax
    $1 = 0x1
```

我的测试程序在 `[(id)1 release]` 处崩溃了。在真实的崩溃里，这些值通常会更有意思一些。

通常会发生两种情况之一。要么接收者地址本身就是垃圾值，而无效地址和它是同一个值（或者相差 16 或 32 字节）。要么接收者地址看起来是合理的，而无效地址就是接收者的 `isa` 指针。后一种情况，通常就是你在使用一个已经被释放的对象，或者别人破坏了你那个有效的对象时会发生的事。

在你的崩溃里留意这些特殊值。也留意附近的值；在某些体系结构上，一个无效的 `isa` 会导致崩溃发生在 `isa+16` 或 `isa+32` 处，而不是 `isa` 本身。

不能被 16 整除——未对齐  `malloc()` 返回的是 16 字节对齐的内存块。如果你的接收者不是 16 字节对齐的，它大概从来就不是一个有效的对象指针。 最高两位和最低两位全部置位——malloc 空闲链表  一块内存被释放之后，内存分配器可能会往里面写入空闲链表指针。如果你在这之后又使用了这个已释放的对象，你会看到一个最高两位和最低两位全部置位的 `isa` 指针。 所有位都被取反——GC 空闲链表  和上面的 malloc 空闲链表情况类似，但这是垃圾回收器造成的。在这种情况下 `address` 看起来很糟糕，但 `~address` 却相当合理。 0xa1b1c1d3——CF 容器  CoreFoundation 的容器用这个值来表示已删除或为空的项。也许某个已释放的对象被重新分配成了一个容器，或者有人用了一个已释放的、被重新分配成了你这个对象的容器，又或者你从某个容器里读取了你的指针，而这个容器同时被另一个线程改动了，你却没有加上正确的锁。 ASCII 文本  也许某个已释放的对象被重新分配成了一个字符串，或者有人用了一个已释放的、被重新分配成了你这个对象的字符串，又或者某个字符串操作发生了缓冲区溢出。用 [asciify](http://sealiesoftware.com/asciify.c) 可以快速地按两种字节序把这些值打印出来。举个例子，下面这个看起来和 URL 有关：  % asciify 0x2e777777 ###.www### ###www.###

#### 审问选择器

由于编译器优化，调用栈回溯里第二帧所指向的调用点，可能并不是真正崩溃的那次调用。有可能那次调用是成功的，而它调用的那个方法做了一次*尾调用*，那才是真正崩溃的地方。由于尾调用优化，中间那一帧就会从调用栈回溯里消失。我们可以用选择器寄存器来确定真正崩溃的那次调用到底是什么。

选择器是指向一个唯一 C 字符串的指针。这一点在未来的操作系统版本里可能会变，但眼下拿它来调试还是很方便的。如果你在调试器里崩溃了，打开调试器控制台，运行下面这行命令，把其中的 `SEL` 寄存器换成上表里正确的那个：

```
    (gdb) x/s $ecx
    0xa1029: "release"
```

Snow Leopard 的崩溃报告器会替你把选择器名字加进崩溃日志里：

```
    Application Specific Information:
    objc_msgSend() selector name: release
```

除此之外，光靠一份崩溃日志去找回选择器名字是很困难的，也不总能成功。在你用上 Snow Leopard 之前，不妨死马当活马医，试试下面这个办法。

1. 从崩溃日志的 Thread State 里，用上表中的寄存器名字，找出 `SEL` 的值。

  ```
      ecx: 0x000a1029
  ```
2. 从崩溃日志的 Binary Images 里，找出地址范围包含这个 `SEL` 值的那个镜像。这通常要么是应用程序本身，要么是 `libobjc.A.dylib`。如果没有哪个镜像的地址范围覆盖这个值，那就放弃吧。  
  `    0x8b000 -   0x106ff7  libobjc.A.dylib ??? (???) <9b5973b7fa88f9aab7885530c7b278dd> /usr/lib/libobjc.A.dylib`
3. 找一份和崩溃日志里那个镜像相匹配的副本。用 UUID 来验证是否匹配。

  ```
      % dwarfdump -u /usr/lib/libobjc.A.dylib
      UUID: 26650299-C6EA-B1C8-52D6-072AC874D400 (ppc) /usr/lib/libobjc.A.dylib
      UUID: 9B5973B7-FA88-F9AA-B788-5530C7B278DD (i386) /usr/lib/libobjc.A.dylib
      UUID: D2A4E8E1-3C1C-E0D9-2249-125B6DD621F8 (x86_64) /usr/lib/libobjc.A.dylib
  ```

  这次崩溃和我本机安装的 i386 版 `libobjc.A.dylib` 是匹配的。如果这是一个系统库，你可能需要崩溃日志里所列那个操作系统版本对应的镜像。如果这是你自己的应用程序，你确实保留了你发布过的每一个版本吧？

  ```

  ```
4. 计算这个 `SEL` 在该镜像里的偏移量。

  ```
      0xa1029 - 0x8b000 = 0x16029
  ```
5. 在该镜像对应偏移量处打印出这个 C 字符串。记得指定正确的体系结构。

  ```
      % otool -v -arch i386 -s __TEXT __cstring /usr/lib/libobjc.A.dylib | grep 16029
      00016029  release
  ```

[Sealie Software](http://sealiesoftware.com/index.html)
