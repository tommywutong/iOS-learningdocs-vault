---
title: iOS知识小集之为什么objc_msgSend()是用汇编实现的
source_url: 'https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/'
source_domain: zhongwuzw.github.io
source_group: single-site
original_language: zh
published: 2018-04-21
archived_at: 2026-07-27
content_hash: 'sha256:bf5a8e473094453a'
plan_ref: 第三周：Runtime 行为与 Cocoa 对象通信 / Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
plan_week: 第三周：Runtime 行为与 Cocoa 对象通信
plan_day: Day 1｜把方法调用还原为“查找行为”（对应 W1-03）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
---

> 原文：[iOS知识小集之为什么objc_msgSend()是用汇编实现的](https://zhongwuzw.github.io/2018/04/21/iOS%E7%9F%A5%E8%AF%86%E5%B0%8F%E9%9B%86%E4%B9%8B%E4%B8%BA%E4%BB%80%E4%B9%88objc-msgSend-%E6%98%AF%E7%94%A8%E6%B1%87%E7%BC%96%E5%AE%9E%E7%8E%B0%E7%9A%84/)

# iOS知识小集之为什么objc_msgSend()是用汇编实现的

发表于 2018-04-21      更新于 2018-05-22      分类于  [iOS开发-其它](https://zhongwuzw.github.io/categories/iOS%E5%BC%80%E5%8F%91-%E5%85%B6%E5%AE%83/)

## 消息发送

---

在使用`Objective-C`调用方法时，我们将其称之为消息发送，这与我们用的`C`、`C++`等调用函数的说法不一样，原因就是`Objective-C`调用方法时，并不是简单的会在编译时得到函数指针，调用时直接使用该函数指针调用就行（`C++`有虚函数，包含一个`v-table`，可以实现简单的多态），而是会在调用的时候，运行时的去查找函数实现，比如，当我们发送`[objc foo]`时，编译器会将其转化为`objc_msgSend(objc, @selector(foo))`(注意，不一定都是转化为`objc_msgSend`，根据发送对象和返回类型，可转化为`objc_msgSendSuper`,`objc_msgSendSuper_stret`等)，`objc_msgSend`方法负责查找函数实现并调用返回结果，我们知道，`Objc Runtime`是[开源](https://github.com/zhongwuzw/objc4-cn)的，所以我们可以看一下源代码`objc_msgSend`的实现逻辑。

## objc_msgSend()使用汇编实现

---

源码可参见[objc_msgSend源码](https://github.com/zhongwuzw/objc4-cn/blob/087a6fd60e3cad2934163b26aa484640d6ff9467/runtime/Messengers.subproj/objc-msg-arm64.s#L286)，我们发现，竟然不是用`C`实现的，而是使用的汇编语言，总结来说，原因有二：

1. 我们无法定义一个`C`函数，可以有可变的参数(可变参数是可以实现的，参考`printf`函数)并且可以调用任意的`C`函数指针，因为函数指针类型是在是无穷无尽的，根本就无法预先全部定义出来。
2. 使用汇编另一个很重要的原因就是速度，首先，汇编就比`C`快，其次，通过使用汇编，可以免去大量局部变量拷贝的操作，参数会直接被存放在寄存器中，当找到`IMP`时，参数已经保存在了寄存器中，可以直接使用。

## objc_msgSend()步骤总结

---

`objc_msgSend`步骤：

1. 获取传递进来的类对象
2. 获取类用来缓存方法的cache
3. 使用`selector`在cache中查找
4. 如果cache中查找不到，则跳转到C代码(`_class_lookupMethodAndLoadCache3`)，进行slow search
5. 调用方法的IMP

## 参考

---

1. [https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)
2. [https://github.com/zhongwuzw/objc4-cn/blob/087a6fd60e3cad2934163b26aa484640d6ff9467/runtime/Messengers.subproj/objc-msg-arm64.s](https://github.com/zhongwuzw/objc4-cn/blob/087a6fd60e3cad2934163b26aa484640d6ff9467/runtime/Messengers.subproj/objc-msg-arm64.s)
3. [https://github.com/zhongwuzw/objc4-cn](https://github.com/zhongwuzw/objc4-cn)
