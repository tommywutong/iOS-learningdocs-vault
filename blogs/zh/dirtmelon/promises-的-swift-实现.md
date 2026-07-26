---
title: Promises 的 Swift 实现
source: dirtmelon
source_key: dirtmelon
source_url: 'https://dirtmelon.github.io/posts/promise-third/'
original_language: zh
published: 2021-12-13
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:85e6d626b95a0f0c'
translated: n/a
---

> 原文：[Promises 的 Swift 实现](https://dirtmelon.github.io/posts/promise-third/)　·　dirtmelon

Promises 的 Swift 层是基于 Objective-C 层实现的，借由 Swift 的特性，提供了更加安全和便捷的接口。

## 基础属性

`Promise` 为 Swift 层提供的类，由于 Swift 有命名空间，所以不需要添加前缀。 `Promise` 内部定义了一个 `alias` ，使得调用更加清晰：

```swift
public typealias ObjCPromise<Value: AnyObject> = FBLPromise<Value>
```

`Promise` 的相关属性：

- `let objCPromise: ObjCPromise<AnyObject>` ，每个 Promise 内部都会有个对应的 `objCPromise` ；
- `var isPending: Bool { return objCPromise.__isPending }` ，获取 `objCPromise` 对应的状态，每个属性前都多了两个下划线，原因是在 Objective-C 层这个属性使用 `NS_REFINED_FOR_SWIFT` 进行声明，表示这个方法在 Swift 层会进行重定义，所以 Swift 调用这个方法时不会自动补全，而且需要加多两个下划线 https://developer.apple.com/documentation/swift/objective-c_and_c_code_customization/improving_objective-c_api_declarations_for_swift ；
- `__value` 在 Objective-C 层也使用了 `NS_REFINED_FOR_SWIFT` ，所以这里也要加一下下划线：

  ```swift
  var value: Value? {
  	let objCValue = objCPromise.__value
    if Promise<AnyObject>.isBridgedNil(objCValue) { return nil }
    guard let value = objCValue as? Value else {
      preconditionFailure("Cannot cast \\(type(of: objCValue)) to \\(Value.self)")
    }
    return value
  }
  ```

  `isBridgedNil` 的实现：

  ```swift
  private static func isBridgedNil(_ value: Value?) -> Bool {
  	// Swift nil becomes NSNull during bridging.
    return !(value is NSNull) && (value as AnyObject is NSNull)
  }
  ```

  这里处理分为两种情况：一个是 `nil` ，一个是 `Optional` 的 `none` 。
- 由于 Swift 是强类语言，所以 `error` 内部会先尝试转换为 `PromiseError` ：

  ```swift
  var error: Error? {
    guard let objCPromiseError = objCPromise.__error else { return nil }
    // Convert `NSError` to `PromiseError`, if applicable.
    return PromiseError(objCPromiseError) ?? objCPromiseError
  }
  ```

## 初始化

`Promise` 提供了将 `FBLPromise` 作为参数的初始化方法：

```swift
public init<Value>(_ objCPromise: ObjCPromise<Value>) {
  guard let objCPromise = objCPromise as? ObjCPromise<AnyObject> else {
    preconditionFailure("Cannot cast \\(Value.self) to \\(AnyObject.self)")
  }
  self.objCPromise = objCPromise
}
```

而通过 `asObjCPromise()` 方法可以获取到对应的 `FBLPromise` ：

```swift
public func asObjCPromise<Value>() -> ObjCPromise<Value> {
  guard let objCPromise = objCPromise as? ObjCPromise<Value> else {
    preconditionFailure("Cannot cast \\(AnyObject.self) to \\(Value.self)")
  }
  return objCPromise
}
```

通过这两个方法可以便捷地在 Swift 和 Objective-C 的 `class` 之间进行转换：

```objectivec
@interface ObjCTest : NSObject

- (FBLPromise<NSString *> *)getString;
- (FBLPromise<NSNumber *> *)getNumber:(NSString *)string;
- (void)asyncWith:(NSString *)string and:(NSInteger)integer completion:(void(^)())handler;
- (void)needsAPromise:(FBLPromise<NSString *> *)promise;

@end
```

Swift 也可以直接使用 `ObjCTest` 进行测试：

```swift
let objc = ObjCTest()

// 通过 FBLPromise 进行初始化
Promise<String>(objc.getString()).then { string in
  return Promise<Int>(objc.getNumber(string))
}.then { number in
  print(number)
}

wrap { handler in
  objc.async(with: "hello", and: 42, completion: handler)
}.then { _ in
  print("Success.")
}.catch { error in
  print(error)
}

let stringPromise = Promise<String> {
  return "Hello world!"
}

// 通过 asObjCPromise 获取 FBLPromise
objc.needsAPromise(stringPromise.asObjCPromise())

@objc(providesAPromiseFromNumber:)
func providesAPromise(from number: Int) -> Promise<String>.ObjCPromise<NSString> {
  return Promise<String> {
    "The number is \\(number)"
  }.asObjCPromise()
}

objc.needsAPromise(providesAPromise(42))
```

## 其它部分

`Promise` 其它的用法和 `FBLPromise` 区别不大，最大的区别是 `all` 操作符部分，为了在 Swift 上使用更加安全， `all` 操作符通过范型提供了强类型操作，但是最多支持 4 个 `Promise` 合并：

```swift
public func all<A, B, C, D>(
  on queue: DispatchQueue = .promises,
  _ promiseA: Promise<A>,
  _ promiseB: Promise<B>,
  _ promiseC: Promise<C>,
  _ promiseD: Promise<D>
) -> Promise<(A, B, C, D)> {
  let promises = [
    promiseA.objCPromise,
    promiseB.objCPromise,
    promiseC.objCPromise,
    promiseD.objCPromise
  ]
  let promise = Promise<(A, B, C, D)>(
    Promise<(A, B, C, D)>.ObjCPromise<AnyObject>.__onQueue(
      queue,
      all: promises
    ).__onQueue(queue, then: { objCValues in
      guard let values = objCValues as [AnyObject]?,
            let valueA = Promise<A>.asValue(values[0]),
            let valueB = Promise<B>.asValue(values[1]),
            let valueC = Promise<C>.asValue(values[2]),
            let valueD = Promise<D>.asValue(values[3])
      else {
        preconditionFailure("Cannot convert \\(type(of: objCValues)) to \\((A, B, C, D).self)")
      }
      return (valueA, valueB, valueC, valueD)
    })
  )
  // 让 Promises 持有 promise ，避免提早释放。
  promises.forEach {
    $0.__addPendingObject(promise)
  }
  return promise
}
```

总的来说 Swift 相当于在 Objective-C 的实现上套了一层壳，提供了更加 Swifty 和安全的 API 。
