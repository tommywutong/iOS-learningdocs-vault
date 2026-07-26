---
title: 《 App 架构》阅读笔记-笔记1
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/app-architecture-first/'
original_language: zh
published: 2018-10-29
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5f85396a45b47a84'
translated: n/a
---

> 原文：[《 App 架构》阅读笔记-笔记1](https://dirtmelon.github.io/posts/app-architecture-first/)　·　dirtmelon

由 [objc.io](https://www.objc.io/) 出版的关于 App架构的书，我阅读的是[ObjC 中国](https://objccn.io/)翻译的中文版本。

## 关于此书

此书用一个 录音 app 来实现以下几种设计模式：

- Model-View-Controller (MVC)
- Model-View-ViewModel+Coordinator (MVVM-C)
- Model-View-Controller+ViewState (MVC+VS)
- ModelAdapter-ViewBinder (MAVB)
- Elm 架构 (The Elm Architecture, TEA)

没有哪种设计模式可以在所有情况下都做到最好，需要根据团队和 app 来进行调整和选择。

> App 的设计模式不仅仅只是一套技术 上的工具，它同时也是审美和社交的手段，可以让你，以及你的代码的其他读者，与你所设计 的程序产生交流。换言之，最好的模式就是对你来说最为清晰的模式。

### 关于架构的思考

一个架构并不是所选择之后就不用再去考量和讨论，随着 app 和团队的不断变化，我们需要不断思考和改进架构，诚如书本所言，这些东西事关程序员的幸福。

### 为什么选择录音 app

需要一个可以展示各个架构的不同之处而又不会湮没细节的 app 。

### 应用架构

架构关注的两个方面：

- 如何将 app 分解为不同的接口和概念层次部件
- 这些部件之间和自身的不同操作所使用的控制流和数据流路径

### Model 和 View

#### Model

- Model 层是 app 最基础的部分，不依赖其他框架
- 为我们的程序提供一个表述事实的单一来源，这会让逻辑清晰，行为正确

#### View

- View 层依赖于 app 框架的部分，使 model 层可见
- 允许用户交互

### App的本质

App 的本质是反馈回路，根据用户的操作进行 UI 界面的刷新，即使是最简单的 scrollView 滚动，也是根据用户的滑动手势来改变 scrollView 的位移，从而更新 scrollView 的显示部分。 所以每个 app 所要处理的问题其实都是如何串联 View 和 Model 之间的通讯。

### 架构技术

- Notification 支持将值从单一源广播
- KVO 将某个对象上属性的改变报告给另一个对象
- 响应式编程 让逻辑可以在部件之间传 输信息的同时得以表达 （本文采用的是 RxSwift）

### App 任务

1. 构建 — 谁负责构建 model 和 view，以及将两者连接起来？
2. 更新 model — 如何处理 view action？
3. 改变 view — 如何将 model 的数据应用到 view 上去？
4. view state — 如何处理导航和其他一些 model state 以外的状态？
5. 测试 — 为了达到一定程度的测试覆盖，要采取怎样的测试策略？

## MVC

### 实现

MVC 的核心思想是，controller 层负责将 model 层和 view 层撮合到一起工作。Controller 对 另外两层进行构建和配置，并对 model 对象和 view 对象之间的双向通讯进行协调。所以，在 一个 MVC app 中，controller 层是作为核心来参与形成 app 的反馈回路的。

文章认为对 model 改变的行为不应该和 view 层级变更的行为放在同一个函数，view 的变更只发生在观察的回调中，这样可以维持 model 和 view 的分离。

View state 可以按需要被 store 在 view 或者 controller 的属性中。相对于影响 model 的 view action，那些只影响 view 或 controller 状态的 action 则不需要通过 model 进行传递。

### 测试

Cocoa MVC 模式已经超过 20 年历史，创建的时候没有考虑过测试这件事。大部分情况下只能采取集成测试，需要构建一个自包含版本的 app，操作其中的某些部分，然后从其他部 分读取数据，确保结果在对象之间按照期望的方式传递。

### 讨论

#### 优点

- 开发阻力最低的架构模式
- Cocoa 每个类都是在 MVC 模式下进行测试的
- 代码量最少，设计开销最小

#### 缺点

- Model 和 view 的同步可能失效，无论在修改 model 或者 view 时都有可能导致两者的状态没有同步
- View Controller 过于臃肿，ViewController 需要处理 view 层，也复制观察 model 以及更新 view，同时也要对 model 的数据进行处理。这些都会使 ViewController 过于臃肿

#### 改进

- 使用观察者模式，可以使用 NotificationCenter 或者 KVO 来观察 model 的变化
- 将尽可能多的功能从 View Controller 移出来，如移到 model 层中，比如排序，数据获取和处理等方法。个人感觉判断某段代码是否适合放在 View Controller 的标准是这段代码是否在其它地方也有使用到，如果有，就可以考虑抽离
- 使用代码而不是 Storyboard ，不使用 Storyboard 可以在构建阶段有更多的控制力
- 在扩展中进行代码重用，在 Swift 中可以结合协议来实现
- 利用 Child ViewController 进行代码重用
- 区分 coordinating controller 和 mediating controller，一般来说 coordinating controller 是无法重用的，而 coordinating controller 是用来执行特定的任务，是可重用的
- 简化 View 配置代码，如果 view controller 需要构建和更新非常多的 view，那么将这部分 view 配置的代码提取出来会很有帮助

### 总结

> 在一个程序员表达对某个不同架构模式的拥护时，他们有时候会贬低 MVC。对于 MVC 的负面 评论包括：无法测试的 view controller，view controller 会增⻓得过大而且无法控制，数据依 赖难以管理等。但是，在阅读本章后，我们希望你意识到，虽然 MVC 确实有它自己的挑战，但 是写出清晰简洁，并包含完整测试以及明确对数据依赖进行管理的 view controller，是完全可能的。

## MVVM-C

### 实现

Model-View-ViewModel+协调器 (MVVM-C) 是 MVC 的变种，它拥有单独的“view-model” (视图模型) 和一个用来管理 view controller 的协调器。MVVM 使用数据 绑定 (通常会和响应式编程一起使用) 来建立 view-model 层和 view 层之间的连接。

MVVM 鼓励将 model 和 view 之间的关系构建为一系列的变形管道。（减少了 controller 所需要承担的责任），提供一套独立于 app 框架的接口，但是它在相当程度上代表了 view 应该展示的状态。

和 MVC 不同，view controller 不监听 model 。View-model 将负责观察 model，并将 model 的通知转变为 view controller 可以理解的形式。View controller 订阅 view-model 的变更，这 通常通过一个响应式编程框架来完成，但也可以使用任意其他的观察机制。当一个 view-model 事件来到时，由 view controller 去更改 view 层级。

### 测试

在 MVVM 里，我们通常只使用接口测试来测试 view-model，而 controller 和 view 则依赖于 Xcode 的 UI 测试或者人工测试。

- 配置测试：构建输入，构建用来传递输入的接口，然后从接口中读取结果
- 展示测试：对可观察量的测试也遵循通用的模式：对 view-model 上所暴露的每一个可观察量，对初始值 进行测试，然后执行操作，并测试后续的条件 (还可以进行更多的操作并测试更多的条件)
- 行为测试：测试 初始条件，执行操作，然后测试接下来的条件

#### 较低的学习成本

为了降低学习成本，可以使用较少响应式编程的 MVVM，可以通过 KVO 的形式来实现。

#### 协调器

协调器是独立于 MVVM 架构之外的一种模式，用来减少 controller 的职责，并对它们解耦。controller 调用协调器上的代码来与其他 controller 进行联动。

Cocoa MVC 中 controller 层的一个职责就是将 model 数据变形为所配置的 view 中所需要的显 示数据。通常这意味着将 model 对象上的字符串，数字或者日期转变为可以显示的形式。即使 在最简单的情况下，将这边部分代码抽离出来，也可以让 controller 更加整洁，同时易于测试。

### 总结

即使不使用 MVVM ，我们也可以从 MVVM 的架构学到一些东西。通过适当引入额外的层，可以使得代码更易维护，减少错误的发生，下面是一些在适当的情况下可以引入的层：

- App-model：获取 model 数据 (比如是否存在已经保存的用户凭证) 并将它与系统服务 的信息 (比如网络是否可用) 合并，将这个信息作为可观察量提供给其他 view-model 使 用
- Session-model：追踪当前登录会话的细节，可能需要在 view-model 和 主 model 之间，或者 view-model 和其他接口之间，进行网络请求的处理
- Flow-model：一个类似 model 版本的协调器，用来将导航状态作为数 据进行建模，并将导航状态和 model 数据合并，直接为 view-model 提供可观察的 model 数据
- Use case：使用例指的是那些用来对主 model 进行切片准备，并且用来简化所 要执行的操作的任意类型的接口或者 model。使用例和 view-model 很像，但是它并不 被绑定在一个单独的 controller 上，而是可以在 view-model 之间进行传递或者共享， 来在多个 view-model 中提供可重用的功能。当一个 app 有多个 view 显示同样的底层 数据时，我们可以使用共通的使用例对象来对从 model 获取数据和将数据写回 model 的操作进行简化

> 大多数大型程序最终都会发展到包含这些抽象。我们建议你不要过早地引入额外的抽象层。你需要精心评估某个变更是否能让你的代码变得简单 (比如更容易被理解)，是否能减少错误发生 的可能，以及是否更容易维护。如果额外的抽象不能提升你写新代码的能力的话，那么我们就 没有理由添加它们。
