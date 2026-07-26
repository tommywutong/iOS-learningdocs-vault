---
title: XCTKVOExpectation for native Swift key paths
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/02/xctkvoexpectation-swift-keypaths/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:02135d4e52f4b94b'
translated: false
---

> 原文：[XCTKVOExpectation for native Swift key paths](https://oleb.net/blog/2018/02/xctkvoexpectation-swift-keypaths/)　·　Ole Begemann

# XCTKVOExpectation for native Swift key paths

The [XCTest framework](https://developer.apple.com/documentation/xctest) comes with [`XCTKVOExpectation`](https://developer.apple.com/documentation/xctest/xctkvoexpectation), a nice convenience API for setting up an [expectation](https://developer.apple.com/documentation/xctest/asynchronous_tests_and_expectations) based on [Cocoa key-value observation (KVO)](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html).

Using `XCTKVOExpectation` in Swift is a little bit less convenient than it could be because it doesn’t support [native Swift key paths](https://github.com/apple/swift-evolution/blob/master/proposals/0161-key-paths.md) (yet?). This isn’t a huge deal since the class hides most of the ugly KVO setup code from you, but the added protection against type mismatches or typos would still be nice to have.

# `KVOExpectation`

So I wrote a new class, [`KVOExpectation`](https://gist.github.com/ole/efe13925abd8e8ea2c7926e9a3131abf), that does exactly that. It takes an object and a Swift key path to observe, and either an expected value to compare the observed property against or a handler block that allows you to customize when to fulfill the expectation.

You can use `KVOExpectation` in a test like this:

```
func testLongOperationFinishes() {
    let op = BlockOperation {
        // Perform work
        // ...
    }
    let e = KVOExpectation(object: op, keyPath: \.isFinished, expectedValue: true)
    let queue = OperationQueue()
    queue.addOperation(op)
    wait(for: [e], timeout: 5)
    XCTAssertFalse(op.isCancelled)
}
```

In this example, we set up an expectation that observes an [`Operation`’s](https://developer.apple.com/documentation/foundation/operation) [`isFinished`](https://developer.apple.com/documentation/foundation/operation/1413540-isfinished) value. The test asserts that the operation completes successfully.

Note that because Swift key paths are strongly typed, the compiler can enforce the correct type for the `expectedValue` parameter — this wouldn’t be possible with Cocoa key paths.

The implementation relies on [the type-safe observation API for Swift key paths](https://github.com/apple/swift/blob/9cc534a05a94bacb7162d361cc803aa4f9fc0f4d/stdlib/public/SDK/Foundation/NSObject.swift#L185-L200) that Apple added last year when Swift 4.0 was introduced. If you don’t use this yet, you absolutely should — it’s so much nicer to use than the old Objective-C API. I would go so far as to say that it makes KVO a viable option for data binding again, whereas I’d never use the old API voluntarily.[1](#fn:1)

# Convenience methods on `XCTestCase`

I also wanted to provide convenience methods on [`XCTestCase`](https://developer.apple.com/documentation/xctest/xctestcase) for the new expectation type. If you call a method like [`expectation(description:)`](https://developer.apple.com/documentation/xctest/xctestcase/1500899-expectation) inside a test, the expectation associates itself automatically with the current test — you don’t have to store the return value. A single call to [`waitForExpectations​(timeout:​handler:)`](https://developer.apple.com/documentation/xctest/xctestcase/1500748-waitforexpectations) will then wait for all registered expectations to fulfill.

Supporting this was more difficult than I expected because `XCTestCase` doesn’t provide an API to register custom expectations. I helped myself by registering a dummy expectation with the test case. My actual KVO expectation will fulfill the dummy expectation when its own fulfillment criteria are met.

This is the relevant code:

```
extension XCTestCase {
    @discardableResult
    func keyValueObservingExpectation<Object: NSObject, Value>(
        for objectToObserve: Object, keyPath: KeyPath<Object, Value>,
        options: NSKeyValueObservingOptions = [],
        file: StaticString = #file, line: Int = #line,
        handler: ((Object, NSKeyValueObservedChange<Value>) -> Bool)? = nil)
        -> XCTestExpectation
    {
        let wrapper = expectation(description: KVOExpectation.description(
            forObject: objectToObserve, keyPath: keyPath, file: file, line: line))
        // Following XCTest precedent, which sets `assertForOverFulfill` to true by default
        // for expectations created with `XCTestCase` convenience methods.
        wrapper.assertForOverFulfill = true
        // The KVO handler inside KVOExpectation retains its parent object while the observation is active.
        // That's why we can get away with not retaining the KVOExpectation here.
        _ = KVOExpectation(object: objectToObserve, keyPath: keyPath,
            options: options) { (object, change) in
            let isFulfilled = handler == nil || handler?(object, change) == true
            if isFulfilled {
                wrapper.fulfill()
                return true
            } else {
                return false
            }
        }
        return wrapper
    }
}
```

Since there is no way to have the subordinate expectation be retained by the dummy expectation object (short of using something like [associated objects](https://oleb.net/blog/2011/05/faking-ivars-in-objc-categories-with-associative-references/)), I rely on the fact that the innermost KVO handler strongly references the expectation object while the observation is active.

Here’s an example of the convenience API in use:

```
keyValueObservingExpectation(for: op,
    keyPath: \.isFinished, expectedValue: true)
// ...
waitForExpectations(timeout: 5)
```

The full code, including fairly comprehensive unit tests, is available [as a Gist on GitHub](https://gist.github.com/ole/efe13925abd8e8ea2c7926e9a3131abf). Paste it into a playground to run the unit tests or feel free to include it in your own projects.

1. As nice as the new KVO API is, I still can’t find this method anywhere in Apple’s documentation, almost nine months after WWDC 2017. I suspect it has something to do with the fact that it’s defined on the quasi-private `_KeyValueCodingAndObserving` protocol; Apple excludes underscored Swift identifiers from the documentation so as not to pollute it with implementation details.

  Anyway, this is the method signature:

  ```
  extension NSObject /* _KeyValueCodingAndObserving */ {
      /// When the returned NSKeyValueObservation is deinited
      /// or invalidated, it will stop observing.
      public func observe<Value>(
          _ keyPath: KeyPath<Self, Value>,
          options: NSKeyValueObservingOptions = [],
          changeHandler: @escaping (Self, NSKeyValueObservedChange<Value>) -> Void)
          -> NSKeyValueObservation
  }
  ```

  [↩︎](#fnref:1)
