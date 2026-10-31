---
title: 'endInterval(_:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/endinterval(_:_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/endinterval(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/endinterval%28_%3A_%3A%29.json'
content_hash: 'sha256:89e50032cb13e4fb'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# endInterval(_:_:)

<sub>实例方法</sub>

结束与指定名称和状态相对应的、带 signpost 标记的时间区间。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endInterval(_ name: StaticString, _ state: OSSignpostIntervalState)
```


## 参数

- `name` — signpost 的名称。

- `state` — 匹配的 begin 调用所返回的时间区间状态。

## 讨论

signposter 使用时间区间状态来强制执行以下运行时断言：

- 多次 end 调用不会消耗同一时间区间状态。
- begin 调用与 end 调用使用相同的名称。
- begin 调用与 end 调用向同一底层日志发出 signpost。
- 对于跨越进程边界的时间区间，你不会使用 [exclusive](../ossignpostid/exclusive.md) signpost ID。

在调试构建中，任何断言失败都会导致崩溃。在生产构建中，你的 App 会继续运行，而 signposter 会改为将一条错误消息附加到该时间区间的收尾 signpost 上。

如果无法访问对应 begin 调用返回的时间区间状态，或者在进程间传递时序列化该状态的成本不可接受，可通过将该时间区间的 signpost ID 传给 [beginState(id:)](<../ossignpostintervalstate/beginstate(id_).md>) 来重新创建时间区间状态。有关序列化时间区间状态的更多信息，参见 [OSSignpostIntervalState](../ossignpostintervalstate.md)。

> [!important] 重要
> 使用 [beginState(id:)](<../ossignpostintervalstate/beginstate(id_).md>) 方法重新创建时间区间状态会绕过用于检查带 signpost 标记的时间区间开始与结束之间一致性的运行时断言。

下面的示例演示了如何在不包含 begin 调用的作用域中重新创建时间区间状态：

```swift
// 在本示例语境中代表某个进程的闭包。
let processA: () -> OSSignpostID = {
    // 使用默认子系统创建 signposter。
    let signposter = OSSignposter()
            
    // 生成要与带 signpost 标记的时间区间关联的 signpost ID。
    let signpostID = signposter.makeSignpostID()
            
    // 开始一个带 signpost 标记的时间区间，并将 signpost ID 返回给调用方。
    let _ = signposter.beginInterval("Example", id: signpostID)
    return signpostID
}
        
// 代表另一个进程的闭包。
let processB: (OSSignpostID) -> Void = { signpostID in
    // 创建一个使用与原先相同子系统的 signposter，
    // 在本例中即为默认子系统。
    let signposter = OSSignposter()
            
    // 使用提供的 signpost ID 重新创建时间区间状态。
    let state = OSSignpostIntervalState.beginState(id: signpostID)
            
    // 使用重新创建的状态结束带 signpost 标记的时间区间。
    signposter.endInterval("Example", state)
}
        
// 执行这两个闭包。
let signpostID = processA()
processB(signpostID)
```


## 另请参阅

### 结束带 signpost 标记的时间区间

- [endInterval(_:_:_:)](<endinterval(______).md>) — 结束一个带 signpost 标记的时间区间，并附加指定的消息。
