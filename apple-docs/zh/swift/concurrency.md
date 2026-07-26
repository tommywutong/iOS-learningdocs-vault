---
title: 并发
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/concurrency
source_url: 'https://developer.apple.com/documentation/swift/concurrency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/concurrency.json'
content_hash: 'sha256:f7263bc70785d335'
translated: true
---

> 导航： [技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md)

# 并发

<sub>API 集合</sub>

执行异步和并行操作。

## 主题

### 基础

- [随堂编码：借助 Swift 并发提升 App](code-along-elevating-an-app-with-swift-concurrency.md) — 跟随 WWDC 讲师一起编码，借助 Swift 并发提升一个 SwiftUI App。
- [更新 App 以使用严格并发](updating-an-app-to-use-strict-concurrency.md) — 使用这段代码跟随指南，将你的代码迁移为充分利用 Swift 6 语言模式提供的完整并发保护。
- [更新 App 以使用 Swift 并发](updating_an_app_to_use_swift_concurrency.md) — 通过重构代码以利用 Swift 中的异步函数，提升你 App 的性能。

### 任务

- [Task](task.md) — 异步工作的一个单元。
- [TaskGroup](taskgroup.md) — 一个包含动态创建的子任务的组。
- [withTaskGroup(of:returning:isolation:body:)](<withtaskgroup(of_returning_isolation_body_).md>) — 开启一个可以包含动态数量子任务的新作用域。
- [ThrowingTaskGroup](throwingtaskgroup.md) — 一个包含会抛出错误、动态创建的子任务的组。
- [withThrowingTaskGroup(of:returning:isolation:body:)](<withthrowingtaskgroup(of_returning_isolation_body_).md>) — 开启一个可以包含动态数量、会抛出错误的子任务的新作用域。
- [TaskPriority](taskpriority.md) — 任务的优先级。
- [DiscardingTaskGroup](discardingtaskgroup.md) — 一个会丢弃子任务结果、包含动态创建的子任务的组。
- [withDiscardingTaskGroup(returning:isolation:body:)](<withdiscardingtaskgroup(returning_isolation_body_).md>) — 开启一个可以包含动态数量子任务的新作用域。
- [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md) — 一个会抛出错误、且会丢弃子任务结果、包含动态创建的子任务的组。
- [withThrowingDiscardingTaskGroup(returning:isolation:body:)](<withthrowingdiscardingtaskgroup(returning_isolation_body_).md>) — 开启一个可以包含动态数量、会抛出错误的子任务的新作用域。
- [UnsafeCurrentTask](unsafecurrenttask.md) — 对当前任务的一个不安全引用。

### 异步序列

- [AsyncSequence](asyncsequence.md) — 一种为其元素提供异步、顺序、可迭代访问的类型。
- [AsyncStream](asyncstream.md) — 一种由闭包生成的异步序列，该闭包通过调用 continuation 来产生新元素。
- [AsyncThrowingStream](asyncthrowingstream.md) — 一种由会抛出错误的闭包生成的异步序列，该闭包通过调用 continuation 来产生新元素。

### Continuation

- [Continuation](continuation.md) — 一种在同步代码与异步代码之间建立接口的机制，它强制要求该 continuation 只能被恢复（resume）一次。 _(beta)_
- [withContinuation(of:_:)](<withcontinuation(of___).md>) — 使用一个不可复制（non-copyable）的当前任务 continuation 调用传入的闭包。 _(beta)_
- [withContinuation(of:throwing:_:)](<withcontinuation(of_throwing___).md>) — 使用一个不可复制（non-copyable）的当前任务 continuation 调用传入的闭包。 _(beta)_
- [CheckedContinuation](checkedcontinuation.md) — 一种在同步代码与异步代码之间建立接口的机制，会记录正确性方面的违规情况。
- [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) — 使用当前任务的一个受检 continuation 调用传入的闭包。
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-13yf6.md>)
- [withCheckedThrowingContinuation(function:_:)](<withcheckedthrowingcontinuation(function___)-2k46m.md>) — 使用当前任务的一个受检 continuation 调用传入的闭包。
- [UnsafeContinuation](unsafecontinuation.md) — 一种在同步代码与异步代码之间建立接口的机制，不进行正确性检查。
- [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) — 使用当前任务的一个不安全 continuation 调用传入的闭包。

### Actor

- [Sendable](sendable.md) — 一种线程安全的类型，其值可以在任意并发上下文之间共享，而不会引入数据争用的风险。
- [Actor](actor.md) — 所有 actor 都遵循的通用协议。
- [MainActor](mainactor.md) — 一个单例 actor，其 executor 等价于主调度队列。
- [GlobalActor](globalactor.md) — 一种类型，表示程序中可用于隔离各类声明的、全局唯一的 actor。
- [SendableMetatype](sendablemetatype.md) — 一种类型，其元类型（metatype）可以在任意隔离域之间共享，而不会引入数据争用的风险。
- [isolation()](<isolation().md>) — 生成对封闭代码所隔离到的那个 actor 的引用；如果代码是非隔离的（nonisolated），则返回 `nil`。

### 任务本地存储

- [TaskLocal](tasklocal.md) — 定义任务本地值键的包装类型。
- [TaskLocal()](<tasklocal().md>) — 引入 [TaskLocal](tasklocal.md) 绑定的宏。

### Executor

- [Executor](executor.md) — 一种可以执行 job 的服务。
- [ExecutorJob](executorjob.md) — 一个可调度工作的单元。
- [SerialExecutor](serialexecutor.md) — 一种执行 job 的服务。
- [TaskExecutor](taskexecutor.md) — 一种可被任务用作首选 executor 的 executor。
- [UnownedJob](unownedjob.md) — 一个可调度工作的单元。
- [JobPriority](jobpriority.md) — 此 job 的优先级。
- [UnownedSerialExecutor](unownedserialexecutor.md) — 对一个串行 executor（一个 `SerialExecutor` 值）的无主引用。
- [UnownedTaskExecutor](unownedtaskexecutor.md)
- [globalConcurrentExecutor](globalconcurrentexecutor.md) — 默认用于 Swift 并发任务的全局并发 executor。
- [withTaskExecutorPreference(_:isolation:operation:)](<withtaskexecutorpreference(__isolation_operation_).md>) — 将当前任务层级结构的任务 executor 偏好设置为传入的 [TaskExecutor](taskexecutor.md)，并通过立即跳转到该 executor 来执行传入的闭包。

### 已废弃

- [extractIsolation(_:)](<extractisolation(__).md>) _(已废弃)_
- [withCheckedContinuation(isolation:function:_:)](<withcheckedcontinuation(isolation_function___).md>) — 源代码兼容性重载；已被 [withCheckedContinuation(function:_:)](<withcheckedcontinuation(function___).md>) 取代。 _(已废弃)_
- [withCheckedThrowingContinuation(isolation:function:_:)](<withcheckedthrowingcontinuation(isolation_function___).md>) — 源代码兼容性重载；已被 `withCheckedThrowingContinuation(function:_:)` 取代。 _(已废弃)_
- [withUnsafeContinuation(isolation:_:)](<withunsafecontinuation(isolation___).md>) — 源代码兼容性重载；已被 [withUnsafeContinuation(_:)](<withunsafecontinuation(__).md>) 取代。 _(已废弃)_
- [AnyActor](anyactor.md) — 通用标记协议，为（本地）`Actor` 和（可能远程的）`DistributedActor` 类型提供共享的“基础”。 _(已废弃)_
- [ConcurrentValue](concurrentvalue.md) _(已废弃)_
- [Job](job.md) — [ExecutorJob](executorjob.md) 的已废弃等价物。 _(已废弃)_
- [PartialAsyncTask](partialasynctask.md) _(已废弃)_
- [UnsafeConcurrentValue](unsafeconcurrentvalue.md) _(已废弃)_
- [UnsafeSendable](unsafesendable.md) — 一种类型，其值可以通过复制安全地跨并发域传递，但会在一致性声明处禁用部分安全检查。 _(已废弃)_
- [UnsafeThrowingContinuation](unsafethrowingcontinuation.md) _(已废弃)_
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-32nwt.md>) — 使用当前任务的一个不安全 continuation 调用传入的闭包。
- [withUnsafeThrowingContinuation(_:)](<withunsafethrowingcontinuation(__)-7zhvy.md>)
- [withUnsafeThrowingContinuation(isolation:_:)](<withunsafethrowingcontinuation(isolation___).md>) — 源代码兼容性重载；已被 `withUnsafeThrowingContinuation(_:)` 取代。 _(已废弃)_

## 另请参阅

### 编程任务

- [Input and Output](input-and-output.md) — 将值打印到控制台，从文本流中读取和写入，并使用命令行参数。
- [Debugging and Reflection](debugging-and-reflection.md) — 使用运行时检查强化你的代码，并检查你的值的运行时表示。
- [Macros](macros.md) — 生成样板代码，并执行其他编译期操作。
- [Key-Path Expressions](key-path-expressions.md) — 使用键路径表达式动态访问属性。
- [Manual Memory Management](manual-memory-management.md) — 手动分配和管理内存。
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — 在类型之间执行转换，或表示任意类型的值。
- [C Interoperability](c-interoperability.md) — 使用导入的 C 类型，或调用 C 可变参数函数。
- [Operator Declarations](operator-declarations.md) — 使用前缀、后缀和中缀运算符。
