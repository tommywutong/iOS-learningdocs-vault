---
title: 错误处理编程指南
apple_id: TP40001806
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2011-01-07'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ErrorHandlingCocoa/RevisionHistory/RevisionHistory.html
archived_at: '2026-07-15T07:15:26.588072Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [错误处理编程指南](Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Index.md) [上一页](Recovering%20From%20Errors.md)

# 文档修订历史

下表列出了《错误处理编程指南》的修订记录。

| __日期__ | __说明__ |
| --- | --- |
| 2011-01-07 | 增加建议：如果方法不是直接通过返回 `NO` 来表示错误，就不应修改错误参数（“创建并返回 NSError 对象”）。 |
| 2009-10-16 | 对代码示例中的局部变量进行了初始化。 |
| 2009-08-18 | 说明 `NSError` 对象可用于 iOS，但错误响应者/恢复 API 及其架构仅适用于 Mac；同时做了若干小幅修正，并添加了指向核心能力概念的链接。 |
| 2009-03-04 | 修正了一个错误链接。 |
| 2009-01-06 | 在《基于文档的应用程序概览》中添加了指向“文档架构中的错误处理”的链接；说明了 `presentError:` 对 `NSCocoaErrorDomain`/`NSUserCancelledError` 错误的默认行为；并提供了相关参考资料、示例代码和文档。 |
| 2006-10-03 | 修正了清单 5-2 中创建 `NSInvocation` 对象的代码。 |
| 2006-04-04 | 修正了演示错误恢复的代码清单，并讨论了 `NSUserCancelledError` 错误代码。 |
| 2005-04-29 | 新增文档，介绍在处理用户级错误时如何使用 `NSError` 对象及相关的 Application Kit 支持。 |

[下一页](Index.md) [上一页](Recovering%20From%20Errors.md)
