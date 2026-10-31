---
title: OSAllocatedUnfairLock
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osallocatedunfairlock
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock.json'
content_hash: 'sha256:63712d5c29990d19'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSAllocatedUnfairLock

<sub>结构体</sub>

一个创建 unfair lock 的结构体。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSAllocatedUnfairLock<State>
```

## 概述

Unfair lock 是在争用时能高效阻塞的低层级锁。它们适合用来保护加载已存储资源的代码。不过，从 Swift 使用 [os_unfair_lock](os_unfair_lock.md) 并不安全，因为它是值类型，因此没有稳定的内存地址。这意味着当你调用 [os_unfair_lock_lock](os_unfair_lock_lock.md) 或 [os_unfair_lock_unlock](os_unfair_lock_unlock.md)，并用 `&` 运算符传入锁对象时，系统可能会锁定或解锁错误的对象。

应改用 [OSAllocatedUnfairLock](osallocatedunfairlock.md)，它能避免该陷阱，因为尽管它是结构体，却并不按值类型那样工作。[OSAllocatedUnfairLock](osallocatedunfairlock.md) 的所有副本都控制同一份底层锁分配。

> [!important] 重要
> 如果你已有使用 [os_unfair_lock](os_unfair_lock.md) 的 Swift 代码，请改为使用 [OSAllocatedUnfairLock](osallocatedunfairlock.md)，以确保正确的加锁行为。

要创建一个保护操作状态的锁，请创建一个包含可能状态的枚举，然后创建锁对象并传入初始状态。下面是资源加载操作的示例：

```swift
enum MyState {
    case idle
    case loading
    case complete(MyAsset)
    case error(Error)
}
let protectedState = OSAllocatedUnfairLock(initialState: MyState.idle)
```

把状态存放在锁内部有助于跟踪锁所保护的内容，并提供一种安全访问该状态的方式。要开始使用锁，请调用 `withLock(_:)` 或 `withLockIfAvailable(_:)`，并传入一个包含要由锁保护的代码的闭包，如下例所示：

```swift
func myLoadMethod() {
    protectedState.withLock { state in
        state = .loading
    }
    var (resource, error) = loadMyResources()
    if resource != nil {
        protectedState.withLock { state in
            state = .complete(resource)
        }
    } else {
        protectedState.withLock { state in
            state = .error(error!)
        }
    }
}
```

若要用外部定义的状态或不带状态来保护某项操作，请创建锁对象时不指定初始状态。非作用域加锁更灵活，但不会协助跟踪锁所保护操作的状态。要使用非作用域锁，请使用 `withLock(_:)` 或 `withLockIfAvailable(_:)`。

```swift
let myLock = OSAllocatedUnfairLock()
myLock.withLock {
    // 需要保护的代码。
}
```

你也可以采用更传统的 lock/unlock 方式使用 [OSAllocatedUnfairLock](osallocatedunfairlock.md)：在执行需要保护的代码之前调用 [lock()](<osallocatedunfairlock/lock().md>)，完成后调用 [unlock()](<osallocatedunfairlock/unlock().md>)，如下所示：

```swift
myLock.lock()
// 需要保护的代码。
myLock.unlock()
```

使用这种方式时，必须从调用 [lock()](<osallocatedunfairlock/lock().md>) 的同一线程调用 [unlock()](<osallocatedunfairlock/unlock().md>)。因此，跨 `await` 挂起点使用这种方式并不安全。在异步代码中使用锁时，请用闭包加锁，或者更好的做法是考虑使用 [Actor](../swift/actor.md)。

> [!warning] 警告
> [OSAllocatedUnfairLock](osallocatedunfairlock.md) 不是递归锁。若试图在同一线程上多次锁定同一对象而中间没有解锁，会触发运行时异常。

## 关系

- **遵循**： [Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 创建锁对象

- [init()](<osallocatedunfairlock/init().md>) — 创建一个不保护状态数据的锁对象。
- [init(initialState:)](<osallocatedunfairlock/init(initialstate_).md>) — 创建一个维护并保护状态数据的锁对象。

### 使用锁

- [lock()](<osallocatedunfairlock/lock().md>) — 获取锁。
- [lockIfAvailable()](<osallocatedunfairlock/lockifavailable().md>) — 尝试获取锁。
- [unlock()](<osallocatedunfairlock/unlock().md>) — 解锁。

### 判定锁所有权

- [Ownership](osallocatedunfairlock/ownership.md) — 表示 unfair lock 所有权状态的枚举。
- [precondition(_:)](<osallocatedunfairlock/precondition(__).md>) — 如果锁对象未能满足指定的所有权要求，则触发断言。

### 初始化方法

- [init(uncheckedState:)](<osallocatedunfairlock/init(uncheckedstate_).md>)

### 实例方法

- [lock(flags:)](<osallocatedunfairlock/lock(flags_).md>)
- [withLock(_:)](<osallocatedunfairlock/withlock(__)-1uy7m.md>)
- [withLock(_:)](<osallocatedunfairlock/withlock(__)-hple.md>)
- [withLock(flags:_:)](<osallocatedunfairlock/withlock(flags___)-1ub4c.md>)
- [withLock(flags:_:)](<osallocatedunfairlock/withlock(flags___)-u2xj.md>)
- [withLockIfAvailable(_:)](<osallocatedunfairlock/withlockifavailable(__)-1rp3w.md>)
- [withLockIfAvailable(_:)](<osallocatedunfairlock/withlockifavailable(__)-3kw0o.md>)
- [withLockIfAvailableUnchecked(_:)](<osallocatedunfairlock/withlockifavailableunchecked(__)-15q0y.md>)
- [withLockIfAvailableUnchecked(_:)](<osallocatedunfairlock/withlockifavailableunchecked(__)-6gji7.md>)
- [withLockUnchecked(_:)](<osallocatedunfairlock/withlockunchecked(__)-7qywq.md>)
- [withLockUnchecked(_:)](<osallocatedunfairlock/withlockunchecked(__)-9v03m.md>)
- [withLockUnchecked(flags:_:)](<osallocatedunfairlock/withlockunchecked(flags___)-8cv64.md>)
- [withLockUnchecked(flags:_:)](<osallocatedunfairlock/withlockunchecked(flags___)-9iq8s.md>)

## 另请参阅

### Swift 包装器

- [OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)
