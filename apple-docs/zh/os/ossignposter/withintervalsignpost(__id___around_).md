---
title: 'withIntervalSignpost(_:id:_:around:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/withintervalsignpost(_:id:_:around:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/withintervalsignpost%28_%3Aid%3A_%3Aaround%3A%29.json'
content_hash: 'sha256:fda9e1832fa52415'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# withIntervalSignpost(_:id:_:around:)

<sub>实例方法</sub>

测量闭包的执行，并附加指定的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withIntervalSignpost<T>(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata, around task: () throws -> T) rethrows -> T
```

## 参数

- `name` — signpost 的名称。

- `id` — signpost 的 ID。默认值为 [exclusive](../ossignpostid/exclusive.md)。

- `message` — signposter 附加到该 signpost 的插值字符串。消息中的每一处插值都可以指定各自的格式和隐私选项。更多信息参见 [Message Argument Formatters](../message-argument-formatters.md)。

- `task` — 要在其周围创建带 signpost 标记的时间区间的闭包。

## 讨论

> [!important] 重要
> 不要创建 [SignpostMetadata](../signpostmetadata.md) 的实例。请改为向 `message` 参数提供插值字符串，系统会自动完成转换。

signposter 使用 signpost ID 来配对带 signpost 标记的时间区间的开始与结束；这是必要的，因为具有相同配置和作用域的多个时间区间可以同时进行。如果在任意特定时刻只能执行一个具有特定配置的时间区间，请将 [exclusive](../ossignpostid/exclusive.md) 作为 `id` 参数传入。否则，请使用 [makeSignpostID()](<makesignpostid().md>) 和 [makeSignpostID(from:)](<makesignpostid(from_).md>) 方法生成 signpost 标识符，如下例所示：

```swift
let accountNumber = "12345678"
                
// 使用默认子系统创建 signposter。
let signposter = OSSignposter()
        
// 生成要与该 signpost 关联的 signpost ID。
let signpostID = signposter.makeSignpostID()
        
// 为封装一个或多个相关任务的闭包
// 打上时间区间的 signpost，并附加一条
// 安全插值敏感数据的消息。
signposter.withIntervalSignpost("Account Reconciliation", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))") {
    
    // 执行相关任务。
    processTransactions()
    updateBalance()
}
```

## 另请参阅

### 测量闭包

- [withIntervalSignpost(_:id:around:)](<withintervalsignpost(__id_around_).md>) — 测量指定闭包的执行。
