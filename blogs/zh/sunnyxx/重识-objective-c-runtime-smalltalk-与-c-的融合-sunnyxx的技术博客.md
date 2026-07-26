---
title: 重识 Objective-C Runtime - Smalltalk 与 C 的融合 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-0/'
original_language: zh
published: 2016-08-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c14c86c8bb1e7224'
translated: n/a
---

> 原文：[重识 Objective-C Runtime - Smalltalk 与 C 的融合 · sunnyxx的技术博客](http://blog.sunnyxx.com/2016/08/13/reunderstanding-runtime-0/)　·　sunnyxx (孙源)

# 重识 Objective-C Runtime - Smalltalk 与 C 的融合

2016年8月13日

这是**重识 Objective-C Runtime**系列文章的其中一篇：

- 重识 Objective-C Runtime - Smalltalk 与 C 的融合
- 重识 Objective-C Runtime - 看透 Type 与 Value
- 重识 Objective-C Runtime - 何为对象何为类
- 重识 Objective-C Runtime - Calling Conventions
- 重识 Objective-C Runtime - 能写完上面的就不错了

2014 年的时候，线下分享了一次 Runtime，为配合分享还出了[几个题目](http://blog.sunnyxx.com/2014/11/06/runtime-nuts/)，莫名其妙的被当成了面试题，导致大家各种补 Runtime 的知识和文章，甚至后来招人的时候，面试者都反问我为啥不考点 Runtime 的题 - -  
时隔快两年，随着最近对这块的理解的加深，咱们来重新认识一下 Runtime。

## [#Smalltalk-与-C-的融合](#Smalltalk-与-C-的融合)Smalltalk 与 C 的融合

三十几年前，Brad Cox 和 Tom Love 在主流且高效的 C 语言基础上，借鉴 Smalltalk 的面向对象与消息机制，想要搞出一个易用且轻量的 C 语言扩展，但 C 和 Smalltalk 的思想和语法格格不入，比如在 Smalltalk 中一切皆对象，一切调用都是发消息：

```c
233 log
```

再比如用一个工厂方法来实例化一个对象：

```
p := Person name: 'sunnyxx' age: 26
```

在当时来看，一个具有面向对象功能的 C 语言真的是非常有吸引力，但必须得解决消息语法的转换，于是乎他们开发了一个 Preprocessor，去解析 Smalltalk 风格的语法，再转换成 C 语言的代码，进而和其他 C 代码一起编译。这个过程和现在 JavaScript 里的 CoffeeScript、JSX 很相似，构建一个 DSL，用转化器转化成原始语言的代码。

想法很美好，但 Smalltalk 语法里面又是空格、又是冒号的，万一遇到个什么复杂嵌套调用，语法解析多难写呀，于是乎他们想，**诶呀别费劲了，把消息两边加个中括号吧**，这样 Parser 写起来简单多了呢对吧：

```objc
[Person name:"sunnyxx" age: 26];
```

这就造就了 Objective-C 奇怪的中括号、冒号四不像语法，这怎么看都是个临时的方案，但在当时可能是唯一方法，借用已有的 C 的编译器比重造一个成本低多了，而且完全兼容 C 语言。随着这几年 Apple 开发的火热，Objective-C 越来越成为 Apple 不爽的地方，先是恨透了在 GCC 上给 Objective-C 加支持，自己重建了个 Clang，后是干脆重新发明了个 Swift 来彻底代替，用 30 年的时间终于还完了这个技术债。

好的，虽然有了个 Preprocessor，但只能做到把 Smalltalk 风格的代码分析并转译成 C，还需要解决两个问题：

1. C 语言上实现一个 OOP 对象模型
2. 将 Smalltalk 风格的 Message 机制转换成 C 函数调用

**对象模型**的设计倒很省事，直接照搬 Smalltalk 的就好了：如 Class / Meta Class / Instance Method / Class Method 这些概念，还有一些关键字如 self / super / nil 等全都是 Smalltalk 的。这步转换在 Preprocessing 过程中就可以完成，因为重写后的 Class 就是原原本本的 C 语言的 Struct，只需要按 Smalltalk 中“类-元类”的模型设置好即可，无需额外的支持。

**消息机制**就不一样了，要实现向一个 target ( class / instance ) 发送消息名 ( selector ) 动态寻找到函数实现地址 ( IMP ) 并调用的过程，还要处理消息向父类传递、消息转发（ Smalltalk 中叫 “Message-Not-Understood”）等，这些行为无法在 Preprocessing 或 Build Time 实现，需要提供若干**运行时**的 C 函数进行支持，所有这些函数打个包，便形成了最原始的 **Runtime**。

所以最初的 **Objective-C = C + Preprocessor + Runtime**

> 注：GCC 中一开始用预处理器来支持 Objective-C，之后作为一个编译器模块，再后来都交给了 Clang 实现。

作为单纯的 C 语言扩展，Runtime 中只要实现几个最基础的函数（如 objc_msgSend）即可，但为了构建整套 Objective-C 面向对象的基础库（如 Foundation），Runtime 还需要提供像 NSObject 这样的 Root Class 作为面向对象的起点、提供运行时反射机制以及运行时对 Class 结构修改的 API 等。再后来，即便是 Objective-C 语言本身的不断发展，新语言特性的加入，也不外乎是扩展 Clang 和扩展 Runtime，比如：

- ，

  等，同时还要处理 dealloc 函数，自动加入对 super 的调用等，具体可以看

  这篇文章

  。
- Lightweight Generics：叫做 “轻量泛型” 是因为只增加了编译器检查的支持，而泛型信息并未影响到运行时，所以 Runtime 库无需改动。
- ）、Array Literal（

  ）、Dictionary Literal（

  ）和轻量泛型一样，只是把如

  在编译期 rewrite 成

  而已，无需改动 Runtime。
- 这篇文章

  。

因此，Runtime 的精髓并非在于平日里很少接触的那些所谓“黑魔法” Runtime API、也并非各种 Swizzle 大法，而是在 Objective-C 语言层面如何处理 Type、处理 Value、如何设计 OOP 数据结构和消息机制、如何设计 ABI 等，去了解这么一个小而美的 C 语言运行时扩展是怎么设计出来的。假如非要让我考一道 Runtime 的题，可能是**“给你 C 语言，如何实现一个 Objective-C？”**，答到哪儿算哪儿。

接下来的文章就找几个有意思的点挨个聊聊。

## [#References](#References)References

[https://zh.wikipedia.org/wiki/Objective-C](https://zh.wikipedia.org/wiki/Objective-C)  
[http://web.cecs.pdx.edu/~harry/musings/SmalltalkOverview.html](http://web.cecs.pdx.edu/~harry/musings/SmalltalkOverview.html)

## [#来罐可乐并催更](#来罐可乐并催更)来罐可乐并催更

![](http://ww2.sinaimg.cn/large/51530583jw1et2mwz8hqzj20af0camy7.jpg)
