---
title: 防止内存使用衰退
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/preventing-memory-use-regressions
source_url: 'https://developer.apple.com/documentation/xcode/preventing-memory-use-regressions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/preventing-memory-use-regressions.json'
content_hash: 'sha256:a0760ac4723d0516'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [性能与指标](performance-and-metrics.md) · [减少 App 的内存使用](reducing-your-app-s-memory-use.md)

# 防止内存使用衰退

<sub>文章</sub>

测量 App 功能所使用的内存，并使用 XCTest 性能测试检测内存使用量的增加。

## 概述

[XCTest](../xctest.md) 可以测量 App 执行测试用例时分配的内存量。若要测量内存使用情况，请在 App 的单元测试目标中创建性能测试，并向 `measure(metrics:)` 传入 [XCTMemoryMetric](../xctest/xctmemorymetric.md) 的实例（instance）。在 block 内，调用 App 中表现出内存使用问题的代码。

```swift
class MemoryTests: XCTestCase {
    func testMemoryUse() {
        self.measure(metrics: [XCTMemoryMetric()]) {
          // 在此处使用相关的 App 功能
        }
    }
}
```

运行此测试时，Xcode 会测量 block 运行期间观察到的内存使用峰值，以及 block 开始与结束之间已分配内存的增长量。你可以单击测试结果旁的图标查看这些值。单击「Set Baseline」来建立用于未来比较的值。如果内存使用量明显超过基线测量值，测试就会失败。

## 另请参阅

### 任务

- [收集内存使用信息](gathering-information-about-memory-use.md) — 通过测量和分析你的 App，识别内存使用效率低下的问题。
- [进行更改以减少内存使用](making-changes-to-reduce-memory-use.md) — 处理内存使用过量的常见原因，以减少 App 的内存使用。
- [响应低内存警告](responding-to-low-memory-warnings.md) — 检测 App 何时使用了过多内存，并使内存使用恢复到可控范围。
