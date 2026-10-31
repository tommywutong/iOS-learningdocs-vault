---
title: 编写可失败的异步 API
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/writing-failable-asynchronous-apis
source_url: 'https://developer.apple.com/documentation/swift/writing-failable-asynchronous-apis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/writing-failable-asynchronous-apis.json'
content_hash: 'sha256:a89ff98a31736902'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [数字与基本值](numbers-and-basic-values.md) · [Result](result.md)

# 编写可失败的异步 API

<sub>文章</sub>

当你无法同步返回错误时，把结果作为 API 的一部分提供。

## 概述

在编写可能失败的函数、方法或其他 API 时，你会在声明上使用 `throws` 关键字来表明该 API 调用可以抛出错误。但是，你不能用 `throws` 关键字来为异步返回的 API 建模。此时应使用 [Result](result.md) 枚举来捕捉异步调用成功或失败的信息，并使用 [Result.success(_:)](<result/success(__).md>) 和 [Result.failure(_:)](<result/failure(__).md>) 这两个 case 的关联值来携带调用结果的信息。

### 异步返回 Result 实例

下面的示例为一个异步的随机数来源建模。`fetchRemoteRandomNumber(completion:)` 方法同步返回 `Void`，并异步调用一个完成处理程序，传入一个 `Result<Int, EntropyError>` 实例，其中要么包含随机的结果，要么包含失败的信息。

```swift
let queue = DispatchQueue(label: "com.example.queue")

enum EntropyError: Error {
    case entropyDepleted
}

struct AsyncRandomGenerator {
    static let entropyLimit = 5
    var count = 0

    mutating func fetchRemoteRandomNumber(
        completion: @escaping (Result<Int, EntropyError>) -> Void
    ) {
        let result: Result<Int, EntropyError>
        if count < AsyncRandomGenerator.entropyLimit {
            // 持续产生数字，直到达到熵限制。
            result = .success(Int.random(in: 1...100))
        } else {
            // 当调用者达到限制时，提供失败原因。
            result = .failure(.entropyDepleted)
        }

        count += 1

        // 延迟以模拟异步的熵来源。
        queue.asyncAfter(deadline: .now() + 2) {
            completion(result)
        }
    }
}
```

你的远程随机数生成器的使用者可以自行决定如何处理成功和失败两种情况：

```swift
var generator = AsyncRandomGenerator()

// 请求比限制多一个的数字，以触发失败。
(0..<AsyncRandomGenerator.entropyLimit + 1).forEach { _ in
    generator.fetchRemoteRandomNumber { result in
        switch result {
        case .success(let number):
            print(number)
        case .failure(let error):
            print("Source of randomness failed: \(error)")
        }
    }
}

print("Waiting on some numbers.")

dispatchMain()
/* Prints:
success(29)
success(46)
success(85)
success(39)
success(84)
Source of randomness failed: entropyDepleted
*/
```

## 另请参阅

### 表示结果

- [Result.success(_:)](<result/success(__).md>) — 一种成功，存储一个 `Success` 值。
- [Result.failure(_:)](<result/failure(__).md>) — 一种失败，存储一个 `Failure` 值。
