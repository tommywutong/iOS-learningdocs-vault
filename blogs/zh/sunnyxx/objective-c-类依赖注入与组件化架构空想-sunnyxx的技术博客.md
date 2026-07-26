---
title: Objective-C 类依赖注入与组件化架构空想 · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/class-dependency-injection.html'
original_language: zh
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:13f0814e60ea1997'
translated: n/a
---

> 原文：[Objective-C 类依赖注入与组件化架构空想 · sunnyxx的技术博客](http://blog.sunnyxx.com/class-dependency-injection.html)　·　sunnyxx (孙源)

# Objective-C 类依赖注入与组件化架构空想

2016年3月29日

## [#我是前言](#我是前言)我是前言

![](http://ww1.sinaimg.cn/large/51530583jw1f2e305fh99j20gz0bjdh9.jpg)

写这篇博客的时候，正好听了半天万物发展、“递弱代偿”的讲解，借机扯一扯：

1. 从原子电子到元素和分子、再从有机物到高级生命，万物都由简单向复杂发展。
2. 各司其职的小部件组成细胞，各司其职的细胞组成器官，各司其职的器官组成一个人，各司其职的人们组成这个社会，复杂的事物都由特定功能的组件按一定架构构成。
3. 低级的细菌给点营养就能活，再看现在的人没网都能半死，越高度演化的东西结构越复杂，但存在性反而越差，只能靠更多的外部依赖才能存活。

细想这些道理，和软件设计似乎也有蛮多共通之处。  
零散的功能代码在过程封装的思想下成了 Function，Function 在面向对象思想下的成了 Class，Class 在设计模式的指导下成了 Module，各个 Module 在组件化架构的指导下构成了一个 App。最近各位老师一直在讨论的组件化架构问题，正是 App 复杂度到了一定程度后，陈旧结构的退化、拆散、重新组合成更复杂结构的过程。但随着系统的庞大、分工的细致，必将带来存在性的减弱，要引入更多外部依赖代为偿还，有时一个依赖库编译失败、人为失误、流程错误、甚至负责打包的机器出了问题，都可能造成整个部门运转的瘫痪。所以一个架构师的挑战不仅仅是想出个组件化实现，更要维持这个大规模代码、人员构成的复杂系统的稳定运转。  
乍一看是不是很高大上，但其实本身也没当过架构师，大多只是空想而已，受最近老师们讨论的启发，产生了自己的一些想法，加上一些对 Objective-C Runtime 机制和小黑魔法的了解，利用依赖注入的思路，简单怼出来了套实现，下面分享一下。

## [#Objective-C-中依赖的本质](#Objective-C-中依赖的本质)Objective-C 中依赖的本质

所谓组件化终归到底都是在处理**依赖**问题，将以往的：

```objc
#import "FDLogger/FDLogger.h"
```

## [#我心目中的组件化架构](#我心目中的组件化架构)我心目中的组件化架构

1. 自然的调用方式。
2. 低侵入的接入
