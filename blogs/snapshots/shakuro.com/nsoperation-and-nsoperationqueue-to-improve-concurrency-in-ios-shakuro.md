---
title: 'NSOperation and NSOperationQueue To Improve Concurrency in iOS | Shakuro'
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
---

> 原文：[NSOperation and NSOperationQueue To Improve Concurrency in iOS | Shakuro](https://shakuro.com/blog/nsoperation-and-nsoperationqueue-to-improve-concurrency-in-ios)

Operations can render assistance in concurrency. Operation is an object-oriented method of job encapsulation, that is to [be done asynchronously](https://shakuro.com/services/python). Operations are supposed to be used in conjunction with an operation queue or independently.

Operation object is an Operation class instance that is used for the required job encapsulation. The Operation class in and of itself is an abstract class that is to be implemented by a subclass for the utility purposes.

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

The OperationQueue class regulates the execution of an operation objects set. After added to the queue, the operation stays in that queue until finished or cancelled. The operations in a queue self-organize in accordance to their priorities and dependencies between the operations. If the operations in a queue have a similar priority, they are executed by the FIFO principle.

Operations support the following basic characteristics:

- Dependencies, preventing operations start before the previous ones are finished.
- Support of the additional completion block.
- Monitoring operations changes of state by using KVO.
- [Support of operations](https://shakuro.com/services/support) priorities and influencing their execution order.
- Cancellation option, allowing to stop the operation at the time of its execution.

If the operation does not fully respond to the application’s needs, an NSOperation subclass can be created to add the missing functionality.  
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
//Asynchronous logic (eg: n/w calls) with callback {
}
}
}
```

The object operations are executed in a synchronous mode by default. However, if you are planning on executing the operations manually with the ability to execute operations asynchronously, you have to redefine the following methods and properties:

- [start()](https://developer.apple.com/reference/foundation/operation/1416837-start)
- [isAsynchronous](https://developer.apple.com/reference/foundation/operation/1408275-isasynchronous)
- [isExecuting](https://developer.apple.com/reference/foundation/operation/1415621-isexecuting)
- [isFinished](https://developer.apple.com/reference/foundation/operation/1413540-isfinished)

After the execution operation starts, it keeps on [accomplishing its task](https://shakuro.com/blog/angular-automation-for-enterprise-development) until it’s finished, or your code definitively cancells it. The cancellation can happen at any time, even before the operation starts.  
 For the support of the operation object cancellation, all you need to do is periodically check the isCancelled value in your custom code.
