---
title: 在 Swift 中处理异步 Objective-C API
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/01/result-init-helper/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bfa3e1277cc55366'
translated: true
---

> 原文：[Working with Asynchronous Objective-C APIs in Swift](https://oleb.net/blog/2017/01/result-init-helper/)　·　Ole Begemann

# 在 Swift 中处理异步 Objective-C API

许多异步的 Objective-C API 会在它们的完成处理程序（completion handler）中传入两个可选值（optional）：一个是操作成功时的方法结果，另一个是操作失败时的错误值。

一个例子是 Core Location 框架中的 [`CLGeocoder.reverseGeocodeLocation`](https://developer.apple.com/reference/corelocation/clgeocoder/1423621-reversegeocodelocation) 方法。它接受一个 [`CLLocation`](https://developer.apple.com/reference/corelocation/cllocation) 对象，并将坐标发送到网络服务，以[将其转换为可读地址](https://en.wikipedia.org/wiki/Reverse_geocoding)。当网络请求完成时，该方法会调用它的完成 block（completion block），传入一个可选数组（包含 [`CLPlacemark`](https://developer.apple.com/reference/corelocation/clplacemark) 对象）和一个可选 [`Error`](https://developer.apple.com/reference/corelocation/clerror.code) 值：

```
class CLGeocoder {
    ...
    func reverseGeocodeLocation(_ location: CLLocation,
        completionHandler: @escaping ([CLPlacemark]?, Error?) -> Void)
    ...
}
```

这种返回一对可选成功值和可选错误的模式，是在 Objective-C API 中处理此类情况最实用的方式。不过，如果这是一个不需要从 Objective-C 调用的 Swift API，你会有不同的设计。

# 两种可能的结果，四种潜在的状态

当前 API 的问题在于，操作实际上只有_两种_可能的结果：要么请求成功并返回结果，要么请求失败并返回错误。然而，现有的代码却允许_四种_不同的状态：

1. 结果非 `nil`，错误为 `nil`。
2. 错误非 `nil`，结果为 `nil`。
3. 两者都非 `nil`。
4. 两者都为 `nil`。

API 的文档可以明确说明排除最后两种情况，但作为使用者，你永远无法真正确定文档是正确的。

# 使用 `Result`（Result 类型）的更好设计

在 Swift 中，你可能会这样设计同样的 API：

```
class CLGeocoder {
    ...
    func reverseGeocode(location: CLLocation,
        completion: @escaping (Result<[CLPlacemark]>) -> Void)
    ...
}
```

现在，完成 block 只接收一个（非可选）参数，其类型为 `Result<…>`。`Result` 是一个枚举（enum），与 Swift 的 [`Optional`](https://developer.apple.com/reference/swift/optional) 类型非常相似。唯一的区别是，它还可以在 `failure` case 中存储一个错误值，而 `Optional` 只在其 `success` case 中有一个关联值：

```
enum Result<T> {
    case success(T)
    case failure(Error)
}
```

`Result` 目前还不是 Swift 标准库的一部分，但将来很可能会被加入。在那之前，你可以自己轻松定义它，或者使用流行的 [antitypical/Result](https://github.com/antitypical/Result) 库。^[1](#fn:1)

借助这个虚构的新 API，编译器可以保证传递给完成 block 的参数只能有两种状态：成功或失败。你无需担心两个值都存在或都不存在的情况。

# 将 `(T?, Error?)` 转换为 `Result<T>` 的初始化方法

然而，我们无法改变 Apple 的 API，所以对完成 block 参数固有的歧义性也无能为力。我们_能_做的是，将可选成功值和可选错误转换为单个 `Result` 值的逻辑集中在一个地方。我在代码中通过为 `Result` 添加一个便捷初始化方法（convenience initializer）来实现这一点：

```
import Foundation // needed for NSError

extension Result {
    /// Initializes a Result from an optional success value
    /// and an optional error. Useful for converting return
    /// values from many asynchronous Apple APIs to Result.
    init(value: T?, error: Error?) {
        switch (value, error) {
        case (let v?, _):
            // Ignore error if value is non-nil
            self = .success(v)
        case (nil, let e?):
            self = .failure(e)
        case (nil, nil):
            let error = NSError(domain: "ResultErrorDomain", code: 1,
                userInfo: [NSLocalizedDescriptionKey:
                    "Invalid input: value and error were both nil."])
            self = .failure(error)
        }
    }
}
```

在两个输入都为 `nil`（正常情况下不应发生）的情况下，此代码会创建一个自定义错误放入结果中。我为此使用了 [`NSError`](https://developer.apple.com/reference/foundation/nserror)，但你可以使用任何遵循 `Error` 协议的类型。

定义了这个初始化方法后，我像这样使用地理编码 API：

```
let location = ...
let geocoder = CLGeocoder()
geocoder.reverseGeocodeLocation(location) { placemarks, error in
    // Turn arguments into Result
    let result = Result(value: placemarks, error: error)
    // Only work with result from here
    switch result {
    case .success(let p): ...
    case .failure(let e): ...
    }
}
```

只需增加一行代码，将参数转换为 `Result` 值，从那时起我就不必再担心未处理的情况了。

**2017 年 1 月 20 日更新：** [Shawn Throop 建议](https://twitter.com/shawnthroop/status/822414872285679616)将我上面概述的更好 API 添加到 `CLGeocoder` 的扩展（extension）中。你的代码随后只调用基于 `Result` 的方法，该方法再调用原始 API 并负责转换：

```
extension CLGeocoder {
    func reverseGeocode(location: CLLocation,
        completion: @escaping (Result<[CLPlacemark]>) -> Void) {
        reverseGeocodeLocation(location) { placemarks, error in
            completion(Result(value: placemarks, error: error))
        }
    }
}
```

1. 那个 `Result` 类型与我这里使用的略有不同：它使用了强类型错误，即有一个用于错误类型的第二个泛型参数。 [↩︎](#fnref:1)
