---
title: 'NSOperation 与 NSOperationQueue：提升 iOS 并发 | Shakuro'
source_url: 'https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios'
source_domain: shakuro.com
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:b4c0bfa5d88792db'
plan_ref: 第四周：线程、GCD、Operation 与锁 / Day 4｜Operation 是“可管理的任务图”（对应 W3-05）
plan_week: 第四周：线程、GCD、Operation 与锁
plan_day: Day 4｜Operation 是“可管理的任务图”（对应 W3-05）
container: '//*[contains(@class,''post-content'')]'
container_source: guess
translated: true
---

> 原文：[NSOperation and NSOperationQueue To Improve Concurrency in iOS | Shakuro](https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios)

操作（operations）有助于实现并发。Operation 是一种面向对象的任务封装方式，用于[异步执行](https://shakuro.com/services/python)。Operation 可以与操作队列（operation queue）配合使用，也可以独立使用。

Operation 对象是 Operation 类的实例，用于封装所需的任务。Operation 类本身是一个抽象类，需要由子类继承并实现具体功能。

```
let queue = OperationQueue()
queue.maxConcurrentOperationCount = 2
 
let operation1 = BlockOperation(block: {
  ...
})
operation1.qualityOfService = .userInitiated
 
let operation2 = BlockOperation(block: {
  ...
})
 
operation1.completionBlock = {
    ...
}
operation2.completionBlock = {
    ...
}
 
operation2.addDependency(operation1)
 
queue.addOperation(operation1)
queue.addOperation(operation2)
```

OperationQueue 类负责管理一组 Operation 对象的执行。在添加到队列后，Operation 会一直留在队列中，直到执行完毕或被取消。队列中的 Operation 会根据各自的优先级和相互之间的依赖关系自行组织。如果队列中的 Operation 优先级相同，则按照 FIFO（先进先出）原则执行。

Operation 支持以下基本特性：

- 依赖关系，可以防止操作在前一个操作完成之前启动。
- 支持额外的完成（completion）`block`。
- 通过 KVO（Key-Value Observing，键值观察）监控操作的状态变化。
- [支持操作](https://shakuro.com/services/support)的优先级，并影响其执行顺序。
- 提供取消选项，允许在操作执行过程中将其停止。

如果 Operation 无法完全满足 App 的需求，可以创建 NSOperation 的子类来添加缺失的功能。
 import Foundation

```
class AsynchronousOperation: Operation {
enum State: String {
case Ready
case Executing
case Finished
private var keyPath: String {
get {
return "is" + self.rawValue
}
}
}
var state: State = .Ready {
willSet {
willChangeValue(forKey: newValue.rawValue)
willChangeValue(forKey: newValue.rawValue)
}
didSet {
didChangeValue(forKey: oldValue.rawValue)
didChangeValue(forKey: oldValue.rawValue)
}
}
override var isAsynchronous: Bool {
get {
return true
}
}
override var isExecuting: Bool {
get {
return state == .Executing
}
}
override var isFinished: Bool {
get {
return state == .Finished
}
}
override func start() {
if self.isCancelled {
state = .Finished
} else {
state = .Ready
main()
}
}
override func main() {
if self.isCancelled {
state = .Finished
} else {
state = .Executing
//异步逻辑（例如网络调用）及回调 {
}
}
}
```

Operation 对象默认以同步模式执行。但是，如果你打算手动执行 Operation，并希望使其具备异步执行能力，则需要重写以下方法和属性：

- [start()](https://developer.apple.com/reference/foundation/operation/1416837-start)
- [isAsynchronous](https://developer.apple.com/reference/foundation/operation/1408275-isasynchronous)
- [isExecuting](https://developer.apple.com/reference/foundation/operation/1415621-isexecuting)
- [isFinished](https://developer.apple.com/reference/foundation/operation/1413540-isfinished)

操作启动后，它会持续[完成其任务](https://shakuro.com/blog/angular-automation-for-enterprise-development)，直到执行完毕，或者你的代码明确将其取消。取消可以发生在任何时间，甚至可以在操作开始之前。
 为了支持 Operation 对象的取消，你需要在自定义代码中定期检查 `isCancelled` 属性的值。
