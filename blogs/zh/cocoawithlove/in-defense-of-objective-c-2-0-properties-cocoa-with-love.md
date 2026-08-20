---
title: '为 Objective-C 2.0 属性辩护 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/in-defense-of-objective-c-20-properties.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:90f495d07d4fc709'
translated: true
---

> 原文：[In defense of Objective-C 2.0 Properties | Cocoa with Love](https://www.cocoawithlove.com/2008/08/in-defense-of-objective-c-20-properties.html)　·　Cocoa with Love (Matt Gallagher)

在 Objective-C 2.0 的所有新特性中，没有哪个能像声明属性（declared properties）那样引发如此大的争议。从各种抨击来看，争议很大程度上源于人们误解了属性在类中所承担的角色。在本文中，我将解释为什么属性在 Objective-C 中是有用的——要说的并不是自动生成 getter 和 setter，也不是点语法。

## 困惑、争议与憎恶

我在 Objective-C 博客圈的诸位可敬同行并不是普遍偏爱 Objective-C 2.0 的属性的。如果你错过了那些尖刻言论，让我提醒你留意：

- [Cocoa Is My Girlfriend — A case against dot syntax](http://www.cimgf.com/2008/07/08/a-case-against-dot-syntax/)  
  _“这纯属语法糖，对语言毫无增益。然而，它的弊端太多了，我无法建议任何人在任何场合使用它。”_
- [Stuff on fire — Does Objective-C Really Need Properties?](http://www.stuffonfire.com/2006/12/08/does-objective-c-really-need-properties/)  
  _“不，合成存取方法和 setter 是酷的，但属性不是。属性的语法烂得掉渣，其概念本身也烂得掉渣。它是什么？是一个 ivar 吗？是另一个对象的 ivar 的代理（因为它可能是）？是一个方法的返回值吗？因为如果是，为什么我们要用 object.property 而不是 [object property]？”_
- [Cocoadev — Are Objective-C 2.0 Properties Ugly?](http://www.cocoadev.com/index.pl?AreObjectiveCTwoPropertiesUgly)  
  _“我确实认为 Objective-C 2 中新引入的 @property 实现既丑陋又令人困惑。我认为它把一门优美、简洁而优雅的语言搅得一团糟。”_
- [Bitquabit — Objective-C 2.0: the Bad, the Horrible, and the Ugly](http://bitquabit.com/2006/08/objective-c-20-the-bad-the-horrible-and-the-ugly/)  
  _“Objective-C 2.0 还加入了属性（properties）。这让我从根本上感到恼火。”  
   “这是 Objective-C 开始修改 C 语法的又一个例子，只不过这回改动不单是不一致；而是致命的。”_

我喜欢一场好戏。而且我还听说，到了下一季，编剧们真的会把剧情再往上推一个档次。

## 并非其目的

用来访问属性的语法，是大多数仇恨的直接靶子。批评者声称，这一语法是毫无意义的外来添加，大可以用现有的方法语法取而代之。我认为，这类抱怨的发出者误解了属性的目的，进而也误解了点语法的目的。

那就让我们先来厘清属性的目的。请允许我非常明确地阐述：

1. 属性的目的**不是**提供自动生成的 getter 与 setter 方法。
2. 属性的目的**不是**用点语法取代方法语法。
3. 属性的目的**不是**换一种方式将特性（attributes）公之于众。

诚然，这些事情可以通过属性来实现，但如果出现了这些结果，它们也只是在朝向真正目的努力的过程中，由实现所附带提供的一种副产物或便利罢了。

为支持以上观点，请允许我指出：

1. 自动生成方法是容许提供的一种便利，因为属性清楚地声明了其被访问的方式。但这是一种便利，而非理由。很多属性并不使用 `@synthesize` 功能。
2. 属性和方法是截然不同的概念，绝不应使用对方的语法。语法上的可互换，只是 Objective-C 实现属性的一种副产物，而非邀人去利用这种混淆。
3. 属性并不需要一个同名的 ivar。它们可以使用另一个不同的 ivar，或者以全然相异的形式来存储数据。属性（properties）与特性（attributes）并没有直接关联。

## 真正的目的

> **属性（Properties）**  
> 一种干净、抽象的途径，用来暴露对象的状态值。  
>   
> 属性是对象所暴露的两种隐喻之一，另一种是方法（方法的含义是“一种干净、抽象的途径，用来执行某个动作”）。

特性（attributes，即 ivar）并不承担与属性（properties）相同的角色，即使特性是公开的，原因就在于它们未被抽象。你无法覆写（override）一个特性。你无法在改变一个特性的存储方式的同时，还维持接口的兼容性。

方法能够完成与属性相同的工作（获取状态，或是设置状态），但它们这样做的基础是约定而不是设计。

在属性被引入之前，必须依靠方法来承担属性的工作。为了让这种做法可行，文档就必须去说明：这个方法的存在是为了访问状态，而非执行某个动作。同样的文档还会塞满 getter 方法提及对应 setter 方法的内容。setter 方法又会指明对应的 getter 方法。

在属性出现之前，对“类似状态的值”的 get 和 set 访问确实存在，但这靠的不过是散落在多处、彼此松耦合的代码，勉强撑起了一个底层语言并不支持的概念。属性则清晰地声明了状态值的存在，消除了 getter 与 setter 方法之间的割裂。

## 新语法虽是外来，但它必须是新的

对点语法的一条核心抱怨在于，较之 Objective-C 的消息发送语法，这一语法看上去是外来的。究竟为什么要用新语法？为什么不直接去调用底层的 getter 或 setter 方法呢？

因为属性是一种不同的隐喻，也暗示了与方法调用所不同的行为与期望。

并且，点语法让 get 与 set 能使用同一种语法，将这两个概念恰当地拴在一起。它还进一步把状态访问与执行动作隔离开来。

getter 与 setter 方法被用来实现一个属性，这应当被看作一个实现细节，而并非接口的真正组成部分。为保持抽象，你永远不应直接调用某个属性所对应的方法。

## 抽象超载

属性的确代表了 Objective-C 中一种新的抽象概念，而有些人视更多的抽象为坏事，因为它们会导致[渗漏的抽象（leaky abstractions）](http://en.wikipedia.org/wiki/Leaky_abstraction)。这条抱怨是有道理的：除非你对其感到自如，并且觉得你的代码需要它，否则就不要使用一种新的抽象。不要仅仅因为属性摆在那里，就去用它。

如果你想把状态与动作分开，以收获“意图被隐形传达”这一优势，那就用属性。

相较传统的存取方法，属性暗示着“随时可访问”（无需特殊的准备工作）。属性暗示着“短小而简单”（不涉及复杂的计算）。读一个属性暗示着“什么也不会改变”。在多数情况下，各属性之间是彼此独立的。

而就存取方法来说，与属性相反，它暗示着“调用者当心”——功能更强，但也需要更深入的理解，才能确保方法会成功。
