---
title: Objective-C交叉引用解决方法
source: 杨萧玉
source_key: yulingtianxia
source_url: 'http://yulingtianxia.com/blog/2014/04/24/objective-cjiao-cha-yin-yong-jie-jue-fang-fa/'
original_language: zh
published: 2019-05-26
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a340bb6c6b743d83'
translated: n/a
---

> 原文：[Objective-C交叉引用解决方法](http://yulingtianxia.com/blog/2014/04/24/objective-cjiao-cha-yin-yong-jie-jue-fang-fa/)　·　杨萧玉

# [Objective-C交叉引用解决方法](http://yulingtianxia.com/blog/2014/04/24/objective-cjiao-cha-yin-yong-jie-jue-fang-fa/)

By [杨萧玉](https://plus.google.com/106642427004837273341?rel=author)

发表于 2014-04-24

**文章目录**

如果类A的头文件import了B，类B的头文件import了A，这样在编译时有可能产生一种错误：“can not find interface declaration”，这是因为Objective-C不允许交叉引用

#import是GCC编译器提供的，XCode在编译Objective－C、C和C++程序时都会使用它。#import可保证头文件只被包含一次，而不论此命令实际上在那个文件中出现了多少次。  
在C语言中，程序员通常使用基于#ifdef命令的方案来避免一个文件包含另一个文件，而后者又包含第一个文件的情况。  
@class创建了一个向前引用。就是在告诉编译器：“相信我，以后你会知道这个类到底是什么。但是现在，你只需要知道这些。”  
如果有循环依赖关系，@class也很有用。即A类使用B类，B类也使用A类。如果试图通过#import语句让这两个类互相引用，那么最后就会出现编译错误。但是如果在A.h中使用@class B，在B.h中使用@class A，那么这两个类就可以互相引用了。  
**所以最佳的解决方案是在头文件中使用@class，在.m文件中使用#import**
