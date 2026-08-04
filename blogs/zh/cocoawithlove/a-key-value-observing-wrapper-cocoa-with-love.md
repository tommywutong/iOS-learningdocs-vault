---
title: '键值观察包装器 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/key-value-observing-wrapper.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:9ef2c0a58b85fe47'
translated: true
---

> 原文：[A key-value observing wrapper | Cocoa with Love](https://www.cocoawithlove.com/blog/key-value-observing-wrapper.html)　·　Cocoa with Love (Matt Gallagher)

本文将介绍一个名为 `KeyValueObserver` 的辅助类型，它能改善语法，并解决键值观察中的一些核心问题。[CwlSignal 项目](https://github.com/mattgallagher/CwlSignal)使用这个类将键值观察适配为响应式编程模式，但该类只依赖 [CwlUtils](https://github.com/mattgallagher/CwlUtils) 中的 `OnDelete` 类，因此你可以只复制这两个文件，在不使用响应式编程的情况下改善键值观察的使用体验。

还有其他键值观察包装器，它们会围绕键值观察提供类型安全、通知同步或类似的抽象。但本文介绍的包装器并非如此；它基本保留底层键值观察所输出的“变更字典”及其线程安全含义，假定你的应用会自行处理变更字典或确保线程安全。我会展示 CwlSignal 如何在 `KeyValueObserver` 之上完成这两件事。

`KeyValueObserver` 类的目的，除了大幅改善语法之外，还在于解决键值观察机制中更深层的问题，例如无法报告键路径上的具体变更位置、无法正确观察弱属性，以及在观察对象释放而观察者仍注册时消除令人头疼的 `NSInternalInconsistencyException`。

> **Swift 4 更新**：自从我发布这段代码以来，Swift 增加了类型安全的键路径以及关联的 `observe(_:, options:, changeHandler:)`。虽然它没有提供本文代码的全部能力，但类型安全本身已经足以成为使用该 observe 函数而不是这种字符串方式的理由。

## 简短历史

键值观察首次出现在 Mac OS X 10.3 中。当时我对它的“魔法”感到惊叹。许多类似乎会自动支持对简单属性进行键值观察。这开启了我对 Objective-C 消息系统中其他技巧的探索兴趣。不过，早在 Swift 出现前很多年，这种兴趣就因动态消息可能带来的各种维护难题而逐渐消退。

如果你曾依赖隐式支持的键值观察（观察一个文档没有明确声明支持键值观察的值），无疑见过依赖这类技巧的后果：它并不可靠。这并不是因为键值观察机制本身存在缺陷，而是因为除非某个类谨慎地选择为特定属性支持键值观察，否则它很可能偶尔以不同方式更新该属性，而这些方式恰好不会触发键值观察通知。

所以，尽管键值观察表面上很“神奇”，在发送端它仍然需要和其他通知系统一样进行有条理的设计。

单独来看，这其实不算问题；它削弱了一些“魔法”，却没有削弱整个键值观察 API 的价值。然而，当我们开始观察接收端时，情况就会变糟。

在 `addObserver`、`observeValue` 和 `removeObserver` 之间实现正确的逻辑，代码量很大、复杂，而且隐藏着许多风险，初看时并不总是显而易见：在 `observeValue` 方法中忘记调用 super、未能保持观察唯一、未能正确处理 `change` 字典，以及完成后忘记移除观察。

即使你已经实现了所有逻辑，代码看起来也基本正常，如果由于某条没有充分测试的代码路径，观察对象在移除观察之前被释放，整个程序仍会崩溃：

```
2016-12-31 09:16:14.476134 MyApp[63688:8417160] *** Terminating app due to uncaught
exception 'NSInternalInconsistencyException', reason: 'An instance 0x100a072c0 of class
SomeModule.SomeClass was deallocated while key value observers were still registered
with it. Current observation info: <NSKeyValueObservationInfo 0x100a09e30> (
```

根据我的经验，这类生命周期顺序问题确实会偶尔发生；虽然不频繁，但发生得足够多，值得强烈期待一种不会直接崩溃的更好方案。

## Swift 中的键值观察

新编写的程序应该使用响应式编程或其他更现代的变更管理方式，而不是键值观察；但在处理现有 API 时，我们常常别无选择。

那么，让我们看看在 Swift 中使用键值观察需要做些什么。实现观察接收端有几十种方式，每种方式都有不同的缺点和代价。这套系统并不像在“轨道上”运行；相反，每次都需要你自行设计整个系统。下面我会给出一种我认为“良好”的键值观察处理方式，但请记住，相比其他方案，它仍有自己的成本和缺点。你也可以把这种方式与我在[上一篇文章](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html#a-button-dependent-on-two-state-values)中展示的另一种方式进行比较。

请记住，下面的全部代码只是为了处理_单个_键值观察属性的观察。

```swift
class MyClass: NSObject {
   var observations = Dictionary<UnsafeMutableRawPointer, (NSObject, String)>()

   // 在某个函数中设置观察（构造器/viewDidLoad/awakeFromNib）
   func startObserving(observedObject: TargetType) {
      // 正确实现 addObserver 需要一个上下文对象来保持观察唯一。
      // 我们可以使用包装器或专门的处理类，但最简单的情况是分配一个空对象；
      // 它几乎只是一个唯一键。
      let context = UnsafeMutableRawPointer.allocate(bytes: 1, alignedTo: 0)

      // 我们需要保存上下文对象，使它持续存在，并在稍后进行验证。
      // 通常保留 observedObject 也是个好主意，以避免
      // 异常。
      self.observations[context] = (observedObject, #keyPath(TargetType.targetProperty))

      // 最后，我们可以添加观察者
      observedObject.addObserver(self, forKeyPath: #keyPath(TargetType.targetProperty),
         options: NSKeyValueObservingOptions.new.union(NSKeyValueObservingOptions.initial),
            context: context)
   }

   // 实现 observeValue 函数
   override func observeValue(forKeyPath keyPath: String?, of object: Any?,
      change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?) {
      // 我们需要进行多项检查之后才能继续
      if let c = context, let (target, _) = self.observations[c] as? TargetType, let
         newValue = change?[.newKey] as? TargetPropertyType {
         // 如果 context 对象是一个专门的处理类，那么它很可能知道
         // 这次观察对应的 keyPath。但我们没有使用定制的处理类，
         // 仍然需要在这里根据 keyPath 进行切换，因为我们的
         // 类可能需要处理多种不同类型的属性。
         switch keyPath {
         case .some(#keyPath(TargetType.targetProperty)):
            // 根据 newValue 对 `self` 执行某些操作
         default: break
         }
      } else {
         // 需要调用 super
         super.observeValue(forKeyPath: keyPath, of: object, change: change,
            context: context)
      }
   }

   deinit {
      // 记得移除持有的所有观察，并释放上下文
      for (context, (target, keyPath)) in observations {
         target.removeObserver(self, forKeyPath: keyPath, context: context)
         context.deallocate(bytes: 1, alignedTo: 0)
      }
   }
}
```

大量注释让这段代码看起来比实际更长，但事实仍然是：代码很多。

注意，代码注释反复提到一个充当观察“上下文”的“专门处理类”。显然，这正是我们接下来要做的事情。

## 包装器类

本文介绍的 `KeyValueObserver` 包装器类将上面的代码精简为以下形式：

```swift
class MyClass: NSObject {
   var observers = [KeyValueObserver]()

   func startObserving(observedObject: TargetType) {
      // 构造观察
      let observer = KeyValueObserver(source: observedObject, keyPath:
         #keyPath(TargetType.targetProperty)) { [weak self] change, reason in

         // 从变更字典中安全地获取 self 的强引用和新值
         guard let s = self, let newValue = change[.newKey] as?
            TargetPropertyType else { return }

         // 根据 newValue 对 `s`（即 `self`）执行某些操作
      }

      // 保留观察
      observers.append(observer)
   }
}
```

这并不是追求最大限度的语法效率。由于 `KeyValueObserver` 并不试图重新发明轮子，仍然需要做一些工作，主要是少量样板代码。

剩下的一些冗长之处来自以下三点：

- `KeyValueObserver` 不针对被观察类型使用泛型（你需要动态向下转型观察到的值）
- `change` 字典与键值观察使用的字典相同（但它保证不会为 nil）
- `NSKeyValueObservingOptions` 的完整集合都可以与 `KeyValueObserver` 一起使用（不过这里隐式使用了 `new` + `initial` 的默认值）

保留这些小复杂性的好处是，这个 `KeyValueObserver` 应该能够替代 Cocoa 键值观察的_任何_用法。不过，如果你想要最高的语法效率，仍然需要再加一层来进一步适配输出（例如 CwlSignal，或者简单地继承 `KeyValueObserver`，对传给 `init` 方法的 `callback` 应用变换）。

例如，[CwlSignal](https://github.com/mattgallagher/CwlSignal) 包含一个围绕 `KeyValueObserver` 的包装器，内置处理前两点（并将第三点限制为 `new` 或 `new` + `initial`），于是代码变成这样：

```swift
class MyClass: NSObject {
   var endpoints = [Cancellable]()

   func startObserving(observedObject: TargetType) {
      endpoints += Signal<TargetPropertyType>.keyValueObserving(observedObject, keyPath:
         #keyPath(TargetType.targetProperty)).subscribeValues { [weak self] newValue in
         // 根据 newValue 对 `self` 执行某些操作
      }
   }
}
```

`Signal<T>.keyValueObserving` 函数只是围绕 `signalKeyValueObserving` 的一个静态函数，它会将键值观察通常发出的 `Any` 结果动态向下转型为值类型 `T`，并丢弃类型不符的值。你可以在 CwlSignal 项目的 [CwlSignalCocoa.swift 文件](https://github.com/mattgallagher/CwlSignal/blob/master/CwlSignal/CwlSignalCocoa.swift?ts=3)中查看这些函数的实现方式。

## `KeyValueObserver` 的优势

使用 `KeyValueObserver` 节省的代码，大多来自它自动提供了一个“专门处理类”上下文对象，也就是我在[Swift 中的键值观察](#key-value-observing-in-swift)一节示例代码注释中提到的对象。使用尾随闭包而不是依赖方法重载，也能节省一些代码。

不过，它的优势不止是语法上的。如果仔细观察，你还会注意到，`observeValue` 示例把 `observedObject` 连同 `context` 和 `keyPath` 一起保存在字典中，而在 `KeyValueObserver` 示例中，`observedObject` 完全没有被保留（假定其他地方会使它保持存活）。

由于观察对象在移除观察之前被释放并触发异常的风险，`observeValue` 示例_必须_保留 `observedObject`。而使用 `KeyValueObserver` 时，即使我们正在观察，被观察对象释放也是定义明确的：被观察对象释放时，观察闭包会被调用，`reason` 值设为 `.sourceDeleted`（`change` 字典为空）。

`reason` 参数还可以提供变更发生位置的更多信息，包括 `.valueChanged`（末端值发生变化时）和 `.pathChanged`（被观察对象与键路径末端之间发生变化时）。

## `KeyValueObserver` 如何工作？

整个类都是相当直接的 Swift 代码；与其他一些键值包装器不同，它不需要深入 Objective-C，也不需要进行 swizzling 之类的运行时操作。这个类确实使用了 Objective-C 运行时函数来判断被观察属性是否为 `weak`，并设置关联对象（用于检测被观察对象何时释放），但复杂性基本也就到此为止。

`KeyValueObserver` 类中最大的一部分代码，是处理实际的_路径_观察本身。通常使用 Cocoa 键值观察时，你可以传入一个“键路径”，路径上的中间观察会被自动处理。而使用 `KeyValueObserver` 时，键路径会被解析，路径中的每一步都单独进行观察。这提供了更大的灵活性，也能更详细地说明变更发生的_位置_，但由于路径变化时需要删除并重新创建这些步骤，它也占了类中大约一半的代码。如果你查看这个类时遇到看不懂的 `tailPath` 相关内容，那可能只是在跟踪和更新键路径的中间步骤。

`tailPath` 还有一种出乎意料的用法：弱属性。弱属性并不总是会为自身发送键值变更通知。为避免这个问题，`KeyValueObserver` 也可能在 `self` 上包含一个 `tailPath` 观察者。这是因为即使弱属性本身没有触发变更通知，改变弱属性也会从 `self` 触发变更通知。`KeyValueObserver` 利用这个虚拟键路径正确地通知弱属性本身。

最后还有一个有趣的点：我提过这个类实际上不会改变键值观察的线程安全性（通知仍可能在不同线程上并发发生）。这确实如此，但类中确实包含一个互斥锁。这个互斥锁用于保护类的两个可变状态值；它不会刻意改变回调的串行化。如果需要串行化，应在 `KeyValueObserver` 之上添加一层来实现（例如 CwlSignal 对 `KeyValueObserver` 的使用，会通过 `Signal` 类将所有内容串行化）。

如果你确实想了解它的工作方式，我建议你[直接查看代码](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlKeyValueObserver.swift?ts=3)。我为大多数函数和变量写了文档，并在注释中讨论了代码的许多其他方面，包括为什么 `source` 必须跟踪为 `Unmanaged<NSObject>`，而不能使用 `weak` 或 `unowned`。

## 使用

> 包含 `KeyValueObserver` 的项目可在 github 上获取：[mattgallagher/CwlUtils](https://github.com/mattgallagher/CwlUtils)。

[CwlKeyValueObserver.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlKeyValueObserver.swift?ts=3) 文件只依赖同一项目中的 [CwlOnDelete.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlOnDelete.swift?ts=3) 文件，所以如果这就是你的全部需求，可以只复制这两个文件。

否则，项目的 [ReadMe.md 文件](https://github.com/mattgallagher/CwlUtils/blob/master/README.md)包含克隆整个仓库并将它生成的框架添加到自己项目中的详细信息。

这个文件也是 [CwlSignal 框架](https://www.cocoawithlove.com/blog/cwlsignal.html)的一部分。如果你已经在使用 CwlSignal，它已经可以直接使用。作为一个[响应式编程框架](https://www.cocoawithlove.com/blog/reactive-programming-what-and-why.html)，CwlSignal 为处理、变换和管理观察提供了更多选项。

## 结论

代码更少、信息更多、潜在问题更少；`KeyValueObserver` 让键值观察关系的接收端明显变得更好。处理键值观察时，它并没有完全消除_所有_棘手之处，但提供了一个基础，你可以在上面添加应用特定的进一步过滤。

### 展望……

我写下这些文字时是 2016 年的除夕。2017 年再见！
