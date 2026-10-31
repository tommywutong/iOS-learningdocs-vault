---
title: 'beginInterval(_:id:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/begininterval(_:id:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/begininterval(_:id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/begininterval%28_%3Aid%3A%29.json'
content_hash: 'sha256:ba77cf4d0c68bf20'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# beginInterval(_:id:)

<sub>实例方法</sub>

开始一个带 signpost 标记的时间区间。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginInterval(_ name: StaticString, id: OSSignpostID = .exclusive) -> OSSignpostIntervalState
```

## 参数

- `name` — signpost 的名称。

- `id` — signpost 的 ID。默认值为 [exclusive](../ossignpostid/exclusive.md)。

## 返回值

signposter 根据指定 `id` 参数派生出的时间区间状态。

## 讨论

signposter 使用 signpost ID 来配对带 signpost 标记的时间区间的开始与结束；这是必要的，因为具有相同配置和作用域的多个时间区间可以同时进行。如果在任意特定时刻只能执行一个具有特定配置的时间区间，请将 [exclusive](../ossignpostid/exclusive.md) 作为 `id` 参数传入。否则，请使用 [makeSignpostID()](<makesignpostid().md>) 和 [makeSignpostID(from:)](<makesignpostid(from_).md>) 方法生成 signpost 标识符。

要结束带 signpost 标记的时间区间，请将返回值传给 [endInterval(_:_:)](<endinterval(____).md>) 或 [endInterval(_:_:_:)](<endinterval(______).md>) 方法之一。如果在想要结束该时间区间时无法访问返回的时间区间状态，可通过将同一 signpost ID 传给 [beginState(id:)](<../ossignpostintervalstate/beginstate(id_).md>) 方法来重新创建它。

如果需要将返回的时间区间状态跨进程边界传递，必须先对其进行编码。更多信息参见 [OSSignpostIntervalState](../ossignpostintervalstate.md)。

下面的示例演示了如何使用 signpost ID 和时间区间状态，为某个时间区间的开始与结束打上 signpost：

```swift
// 使用默认子系统创建 signposter。
let signposter = OSSignposter()
        
// 生成要与带 signpost 标记的时间区间关联的 signpost ID。
let signpostID = signposter.makeSignpostID()
        
// 创建一个名称，signposter 会将其与
// signpost ID 一起使用，以消除 begin 调用与 end 调用之间的歧义。
// 类型必须是 StaticString。
let name: StaticString = "Example Signpost"
        
// 开始一个带 signpost 标记的时间区间，并保留对
// 返回的时间区间状态的引用。
let state = signposter.beginInterval(name, id: signpostID)
        
// 执行一个或多个要测量的任务。
        
// 使用 begin 调用得到的时间区间状态，结束
// 对应的带 signpost 标记的时间区间。
signposter.endInterval(name, state)
```

## 另请参阅

### 开始带 signpost 标记的时间区间

- [beginInterval(_:id:_:)](<begininterval(__id___).md>) — 开始一个带 signpost 标记的时间区间，并附加指定的消息。
- [beginAnimationInterval(_:id:)](<beginanimationinterval(__id_).md>) — 开始一个用于测量动画的、带 signpost 标记的时间区间。
- [beginAnimationInterval(_:id:_:)](<beginanimationinterval(__id___).md>) — 开始一个用于测量动画的、带 signpost 标记的时间区间，并附加一条消息。
- [OSSignpostIntervalState](../ossignpostintervalstate.md) — 追踪带 signpost 标记的时间区间状态的对象。
- [SignpostMetadata](../signpostmetadata.md) — 表示你附加到 signpost 的消息的类型。
