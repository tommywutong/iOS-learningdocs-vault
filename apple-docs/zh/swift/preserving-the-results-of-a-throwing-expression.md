---
title: 保留可抛出错误的表达式的结果
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/preserving-the-results-of-a-throwing-expression
source_url: 'https://developer.apple.com/documentation/swift/preserving-the-results-of-a-throwing-expression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/preserving-the-results-of-a-throwing-expression.json'
content_hash: 'sha256:7a7c868a7f91db56'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Swift](../swift.md) · [Swift 标准库](swift-standard-library.md) · [数字和基本值](numbers-and-basic-values.md) · [Result](result.md)

# 保留可抛出错误的表达式的结果

<sub>文章</sub>

当你需要序列化或缓存结果时，调用能包装可抛出错误表达式的初始化方法。

## 概述

有时你需要保留一次函数调用（或其他既可能抛出错误、也可能返回值的表达式）的完整结果。例如，你可能需要序列化这个结果，或者把它作为一个值传给 App 里处理结果数据的另一部分。在这类场景下，使用 [Result](result.md) 类型来捕获一次可能失败的操作的结果。

### 确定要保留的可抛出错误的表达式

通常你会用 `do-catch` 语句立即处理可抛出错误的表达式，但有时你需要把这次操作的完整结果存起来，供之后诸如分析一批调用之类的任务处理。下面的示例引入了一个用来生成随机数的 API，它大约有一半的概率会失败。

```swift
enum EntropyError: Error {
    case entropyDepleted
}

struct UnreliableRandomGenerator {
    func random() throws -> Int {
        if Bool.random() {
            return Int.random(in: 1...100)
        } else {
            throw EntropyError.entropyDepleted
        }
    }
}
```

### 把可抛出错误的表达式转换成 Result

使用 [Result](result.md) 枚举的 `Swift/Result/init(catching:)` 初始化方法，可以保留一个可抛出错误的表达式的返回值或抛出的错误。在传给这个初始化方法的闭包内部调用这个可抛出错误的表达式：

```swift
let singleSample = Result { try UnreliableRandomGenerator().random() }
```

在大多数场景下，你会把保留下来的结果用作代码里更广泛功能的一部分。例如，你可能要运行一系列随机性测试，既要计算随机数生成器返回的一系列数字的统计平均值，也要计算调用这个 API 的失败率。在这类情况下，你需要存储整个结果，而不是只存储成功值，或者只记录 API 调用失败了这件事。

下面的示例在保存一系列调用以供之后做统计分析这个更广泛的场景下，使用了 `Swift/Result/init(catching:)` 初始化方法：

```swift
struct RandomnessMonitor {
    let randomnessSource: UnreliableRandomGenerator
    var results: [Result<Int, Error>] = []

    init(generator: UnreliableRandomGenerator) {
        randomnessSource = generator
    }

    mutating func sample() {
        let sample = Result { try randomnessSource.random() }
        results.append(sample)
    }

    func summary() -> (Double, Double) {
        let totals = results.reduce((sum: 0, count: 0)) { total, sample in
            switch sample {
            case .success(let number):
                return (total.sum + number, total.count)
            case .failure:
                return (total.sum, total.count + 1)
            }
        }

        return (
            average: Double(totals.sum) / Double(results.count - totals.count),
            failureRate: Double(totals.count) / Double(results.count)
        )
    }
}
```

在足够大的样本上运行这个分析，会得到一个接近 50 的平均数，以及一个接近 50% 的失败率：

```swift
var monitor = RandomnessMonitor(generator: UnreliableRandomGenerator())
(0..<1000).forEach { _ in monitor.sample() }
let (average, failureRate) = monitor.summary()
print("Average value: \(average), failure rate: \(failureRate * 100.0)%.")
// 会打印类似这样的值："Average value: 47.95, failure rate: 48.69%."
```
