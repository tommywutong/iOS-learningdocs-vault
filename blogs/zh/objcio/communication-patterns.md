---
title: 通信模式
source: objc.io
source_key: objcio
source_url: 'https://www.objc.io/issues/7-foundation/communication-patterns'
original_language: en
published: ''
status: frozen
license: 未声明（页面无版权声明，文章版权归各作者）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7c41eba553e0d2de'
translated: true
---

> 原文：[Communication Patterns](https://www.objc.io/issues/7-foundation/communication-patterns)　·　objc.io

每个应用都由多个耦合程度不一的对象组成，它们需要彼此通信才能完成工作。本文将梳理所有可用选项，看看它们在 Apple 框架中如何使用，并提炼出一些关于何时该用哪种机制的最佳实践建议。

尽管本期主题是 Foundation 框架，我们的视野会超出 Foundation 中的通信机制——KVO 与通知——还会讨论委托、block 以及 target-action。

当然，有些情况下并没有该用哪种模式的明确答案，选择最终取决于口味。但也有许多情况相当一目了然。

在本文中，我们常会使用「接收者」（recipient）和「发送者」（sender）这两个术语。在通信模式语境下它们的含义，用几个例子最容易说清：table view 是发送者，其 delegate 是接收者。Core Data 的 managed object context 是其所发通知的发送者，拾取这些通知的一方是接收者。slider 是 action 消息的发送者，实现该 action 的 responder 是接收者。带有符合 KVO 的属性且该属性发生变化的对象是发送者，observer 是接收者。明白了吧？

## 模式

我们先看看每种可用通信模式的具体特征。在此基础上，下一节将构建一张流程图，帮助为任务选择合适工具。最后，我们会过一遍 Apple 框架中的一些例子，并推理他们为何对某些用例选择了特定模式。

### KVO

KVO 是一种向对象通知属性变化的机制。它实现于 Foundation 中，许多构建在 Foundation 之上的框架都依赖它。关于使用 KVO 的最佳实践与示例，请阅读本期 Daniel 的 [KVO 与 KVC 文章](https://www.objc.io/issues/7-foundation/key-value-coding-and-observing/)。

若你只关心另一个对象的值变化，KVO 是可行的通信模式。不过还有一些额外要求。首先，接收者——将收到变化消息的对象——必须了解发送者——值发生变化的那个对象。此外，接收者还需要了解发送者的生命周期，因为必须在发送者对象被释放之前取消注册观察者。若所有这些要求都满足，通信甚至可以是一对多的，因为多个观察者可以为同一对象注册更新。

若计划对 Core Data 对象使用 KVO，你必须知道这里的情况略有不同。这与 Core Data 的 faulting 机制有关。一旦 managed object 变成 fault，它会对其属性触发观察者回调，尽管这些属性的值并未改变。

### 通知

通知是在代码中相对无关的部分之间广播消息的很好工具，尤其当消息偏信息性、你并不一定期望有人据此做事时。

通知可用于发送任意消息，甚至可通过 `userInfo` 字典或子类化 `NSNotification` 携带载荷。通知的独特之处在于发送者和接收者不必彼此了解。它们可用于在非常松耦合的模块之间传递信息。因此，通信是单向的——你无法回复一条通知。

### 委托

委托是贯穿 Apple 框架的广泛模式。它让我们能定制对象的行为，并获知某些事件。要使委托模式工作，消息发送者需要了解接收者（delegate），但反过来不必。耦合还因发送者只知道其 delegate 遵循某个协议而进一步放松。

由于委托协议可以定义任意方法，你可以把通信精确建模成所需形态。你可以用方法参数传递载荷，委托甚至可以通过委托方法的返回值作出响应。若你只需在两个在应用架构中位置相对接近的特定对象之间通信，委托是一种非常灵活且直截了当的通信模式。

但也存在过度使用委托模式的危险。若两个对象耦合紧密到一方离不开另一方，就没有必要定义委托协议。在这些情况下，对象可以了解对方的类型并直接对话。两个现代例子是 `UICollectionViewLayout` 和 `NSURLSessionConfiguration`。

### Blocks

Blocks 是 Objective-C 相对较新的补充，最早在 OS X 10.6 和 iOS 4 中可用。Blocks 常常能承担以前会用委托模式实现的角色。不过，两种模式各有独特的要求与优势。

何时不该使用 blocks，有一个相当清晰的判据，与造成[循环引用](https://developer.apple.com/library/mac/documentation/cocoa/conceptual/memorymgmt/Articles/mmPractical.html#//apple_ref/doc/uid/TP40004447-1000810)的危险有关。若发送者需要 retain block，且无法保证该引用会被置为 nil，那么 block 内对 `self` 的每一次引用都可能成为潜在的循环引用。

假设我们想实现一个 table view，但想用 block 回调代替委托模式来处理选择方法，像这样：

```
self.myTableView.selectionHandler = ^void(NSIndexPath *selectedIndexPath) {
    // handle selection ...
};
```

这里的问题是：`self` retain 了 table view，而 table view 必须 retain 这个 block 才能稍后使用它。table view 无法把这个引用置为 nil，因为它无法判断何时不再需要它。若我们无法保证循环引用会被打破，且我们会 retain 发送者，那么 blocks 就不是好选择。

`NSOperation` 是一个好例子，说明这何时不会成为问题，因为它会在某个时刻打破循环引用：

```
self.queue = [[NSOperationQueue alloc] init];
MyOperation *operation = [[MyOperation alloc] init];
operation.completionBlock = ^{
    [self finishedOperation];
};
[self.queue addOperation:operation];
```

乍看这像是循环引用：`self` retain 了 queue，queue retain 了 operation，operation retain 了 completion block，completion block 又 retain 了 `self`。然而，把 operation 加入 queue 最终会导致它被执行，之后从 queue 中移除。（若它根本不被执行，我们就有更大的问题了。）一旦 queue 移除了 operation，循环引用就被打破。

另一个例子：假设我们在实现一个视频编码器类，在其上调用 `encodeWithCompletionHandler:` 方法。要使这不成问题，我们必须保证编码器对象会在某个时刻把它对 block 的引用置为 nil。在内部，这大致需要如下写法：

```
@interface Encoder ()
@property (nonatomic, copy) void (^completionHandler)();
@end

@implementation Encoder

- (void)encodeWithCompletionHandler:(void (^)())handler
{
    self.completionHandler = handler;
    // do the asynchronous processing...
}

// This one will be called once the job is done
- (void)finishedEncoding
{
    self.completionHandler();
    self.completionHandler = nil; // <- Don't forget this!
}

@end
```

一旦工作完成并调用了 completion block，我们就把它置为 nil。

若我们调用的消息需要发回一次与该次方法调用相关的一次性响应，blocks 就非常合适，因为那时我们可以打破潜在的循环引用。此外，若把处理该消息的代码与消息调用放在一起有助于可读性，就很难反对使用 blocks。沿着这条线，blocks 的一个非常常见的用例是 completion handler、error handler 等。

### Target-Action

Target-Action 是响应界面事件时发送消息的典型模式。iOS 上的 `UIControl` 与 Mac 上的 `NSControl`/`NSCell` 都支持该模式。Target-Action 在消息的发送者与接收者之间建立非常松的耦合。消息的接收者不知道发送者，甚至发送者也不必事先知道接收者是谁。若 target 为 `nil`，action 会沿[响应者链](https://developer.apple.com/library/ios/documentation/general/conceptual/Devpedia-CocoaApp/Responder.html)向上传递，直到找到能响应它的对象。在 iOS 上，每个控件甚至可以关联多个 target-action 对。

基于 target-action 的通信有一个局限：所发消息无法携带任何自定义载荷。在 Mac 上，action 方法总是以发送者作为第一个参数。在 iOS 上，它们可选地接收发送者和触发该 action 的事件作为参数。但除此之外，无法让控件随 action 消息发送其他对象。

## 做出正确选择

基于上文所述各模式的特征，我们构建了一张流程图，帮助在不同情境下做出该用哪种模式的良好决策。事先警告：这张图的建议不必是最终答案；可能还有同样好用的其他替代方案。但在多数情况下，它应能引导你找到适合任务的正确模式。

![](https://www.objc.io/images/issue-7/communication-patterns-flow-chart_56d2293.png)

图中还有几处细节值得进一步解释：

其中一个框写着「发送者符合 KVO」。这不仅意味着发送者在相关值变化时发送 KVO 通知，还意味着观察者了解发送者的生命周期。若发送者存放在 weak 属性中，它可能随时被置为 nil，观察者就会泄漏。

底行另一个框写着「消息是对方法调用的直接响应」。这意味着方法调用的接收者需要作为该方法调用的直接响应，与调用者对话。这通常也意味着：把处理该消息的代码与方法调用放在同一处是合理的。

最后，右下方有一个决策问题：「发送者能否保证把对 block 的引用置为 nil？」。这指的是上文关于基于 block 的 API 与潜在循环引用的讨论。若发送者无法保证其持有的对 block 的引用会在某个时刻被置为 nil，你就是在自找循环引用的麻烦。

## 框架示例

本节我们会过一遍 Apple 框架中的一些例子，看看前面勾勒的决策流程是否真的说得通，以及 Apple 为何按现状选择了这些模式。

### KVO

`NSOperationQueue` 使用 KVO 来观察其 operations 的状态属性变化（`isFinished`、`isExecuting`、`isCancelled`）。状态变化时，queue 会收到 KVO 通知。为何 operation queue 对此使用 KVO？

消息的接收者（operation queue）显然了解发送者（operation），并通过 retain 它来控制其生命周期。此外，该用例只需要单向通信机制。至于 operation queue 是否只关心 operation 的值变化，答案没那么清晰。但至少可以说，需要传达的内容（状态变化）可以被建模为值变化。由于这些状态属性除了让 operation queue 了解 operation 状态之外本身也很有用，在此场景下使用 KVO 是合乎逻辑的选择。

![](https://www.objc.io/images/issue-7/kvo-flow-chart_6b0ac5a.png)

不过 KVO 并非唯一可行的选择。我们也可以想象让 operation queue 成为 operation 的 delegate，由 operation 调用如 `operationDidFinish:` 或 `operationDidBeginExecuting:` 这样的方法，向 queue 发出状态变化信号。但这会不太方便，因为 operation 除了调用这些方法外，还得让状态属性保持最新。此外，queue 必须自己跟踪所有 operations 的状态，因为它不能再向它们询问了。

### 通知

Core Data 使用通知来传达诸如 managed object context 内变化之类的事件（`NSManagedObjectContextObjectsDidChangeNotification`）。

变化通知由 managed object contexts 发送，因此我们不能假定该消息的接收者一定了解发送者。由于消息来源显然不是 UI 事件，可能有多个接收者感兴趣，且只需要单向通信通道，在此场景下通知是唯一可行的选择。

![](https://www.objc.io/images/issue-7/notification-flow-chart_dae4ce1.png)

### 委托

Table view 的委托承担多种职能，从管理 accessory views、编辑，到跟踪屏幕上的 cells。为便于本例，我们看 `tableView:didSelectRowAtIndexPath:` 方法。为何这被实现为委托调用？为何不是 target-action 模式？

如上文流程图所述，target-action 仅在你无需传输任何自定义载荷时才适用。在选择场景中，collection view 不仅告诉我们某个 cell 被选中了，还通过交出其 index path 告诉我们是哪一个。若我们坚持要求发送 index path，流程图会直接把我们导向委托模式。

![](https://www.objc.io/images/issue-7/delegation-flow-chart_9d9cb75.png)

那么，不随选择消息发送 index path，而是在收到消息后向 table view 询问当前选中的 cells，这种选项如何？那会相当不便，因为那样我们就得自己记账哪些 cells 当前被选中，才能在多选情况下判断哪个 cell 是新选中的。

类似地，我们可以设想仅通过观察 table view 上一个带有选中 index paths 的属性，来获知选择变化。然而我们会遇到与上面相同的问题：若不自己记账，就无法区分哪个 cell 最近被选中/取消选中。

### Blocks

作为基于 block 的 API 示例，我们看 `-[NSURLSession dataTaskWithURL:completionHandler:]`。从 URL 加载系统回传给调用者的通信是怎样的？首先，作为该 API 的调用者，我们了解消息的发送者，但并不 retain 它。此外，这是与 `dataTaskWithURL:` 方法调用直接耦合的单向通信。把这些因素都代入流程图，我们直接落到基于 block 的通信模式。

![](https://www.objc.io/images/issue-7/block-flow-chart_3b433df.png)

还有其他选项吗？当然有，Apple 自己的 `NSURLConnection` 就是最好的例子。`NSURLConnection` 在 Objective-C 尚无 blocks 时打造，因此他们需要另辟蹊径，用委托模式实现了这种通信。一旦有了 blocks，Apple 在 OS X 10.7 和 iOS 5 中为 `NSURLConnection` 添加了 `sendAsynchronousRequest:queue:completionHandler:` 方法，于是简单任务就不再需要委托了。

由于 `NSURLSession` 是在 OS X 10.9 和 iOS 7 才加入的非常现代的 API，blocks 现在是做这类通信的首选模式（`NSURLSession` 仍有委托，但用于其他目的）。

### Target-Action

Target-action 模式的一个明显用例是按钮。按钮除了「被点击（或轻触）」之外不必发送任何信息。为此，target-action 是一种非常灵活的模式，用来把这一界面事件告知应用。

![](https://www.objc.io/images/issue-7/target-action-flow-chart_8f5a051.png)

若指定了 target，action 消息会直接发给该对象。然而，若 target 为 `nil`，action 消息会沿响应者链冒泡，寻找能处理它的对象。在这种情况下，我们拥有一种完全解耦的通信机制：发送者不必了解接收者，反之亦然。

Target-action 模式非常适合界面事件。没有其他通信模式能提供相同功能。就发送者与接收者完全解耦而言，通知最为接近，但使 target-action 特别的是对响应者链的利用。只有一个对象能对该 action 作出反应，且 action 沿响应者层次结构中一条定义良好的路径传递，直到被某个东西拾取。

## 结论

可用于在对象之间传递信息的模式数量，起初可能让人应接不暇。该用哪种模式的选择常常感觉含糊。但一旦我们更仔细地研究每种模式，它们都有非常独特的要求与能力。

决策流程图是澄清特定模式选择的良好起点，但当然不是所有问题的终点。我们很乐意听你说说它是否与你使用这些模式的方式相符，或者你是否认为有遗漏或误导之处。

---
