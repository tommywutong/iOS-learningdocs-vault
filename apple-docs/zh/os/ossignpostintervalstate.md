---
title: OSSignpostIntervalState
framework: os
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/ossignpostintervalstate
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate.json'
content_hash: 'sha256:ed81d11d98383083'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSSignpostIntervalState

<sub>类</sub>

跟踪带 signpost 标记的时间区间状态的对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OSSignpostIntervalState
```

## 概述

[OSSignposter](ossignposter.md) 使用时间区间状态来强制执行下列运行时断言：

- 多次 end 调用不会消耗同一时间区间状态。
- begin 调用与 end 调用使用相同的名称。
- begin 调用与 end 调用向相同的底层日志发出 signpost。
- 你不会对跨越进程边界的时间区间使用 [exclusive](ossignpostid/exclusive.md) signpost ID。

在 debug 构建中，任何断言失败都会导致崩溃。在生产构建中，你的 App 会继续运行，而 signposter 会改为把错误消息附加到该时间区间的结束 signpost 上。

[OSSignpostIntervalState](ossignpostintervalstate.md) 遵循 [Codable](../swift/codable.md) 协议，这意味着你可以序列化状态并在进程间安全共享，如下例所示：

```swift
// A closure that represents a process in the context of this example.
let processA: () throws -> Data = {
    // Create a signposter that uses the default subsystem.
    let signposter = OSSignposter()
            
    // Generate a signpost ID to associate with the signposted interval.
    let signpostID = signposter.makeSignpostID()
            
    // Begin a signposted interval.
    let state = signposter.beginInterval("Example", id: signpostID)
            
    // Encode the state into JSON and return to the caller.
    return try JSONEncoder().encode(state)
}
        
// A closure that represents a different process.
let processB: (Data) throws -> Void = { data in
    // Decode the provided JSON data into an instance of 
    // OSSignpostIntervalState.
    let state = try JSONDecoder().decode(OSSignpostIntervalState.self, 
        from: data)
            
    // Create a signposter that uses the same subsystem as
    // the original, which, in this case, is the default.
    let signposter = OSSignposter()
            
    // End the signposted interval using the decoded state.
    signposter.endInterval("Example", state)
}
        
// Execute the two closures.
do {
    let data = try processA()
    try processB(data)
} catch {
    // Handle any thrown errors accordingly.
}
```

如果你无法访问开始带 signpost 标记的时间区间的调用所返回的时间区间状态，或者在进程间传递时序列化该状态的开销不可接受，请将该时间区间的 signpost ID 传给 [beginState(id:)](<ossignpostintervalstate/beginstate(id_).md>) 方法来重新创建时间区间状态。

## 关系

- **遵循**： [Decodable](../swift/decodable.md)、[Encodable](../swift/encodable.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 创建时间区间状态

- [init(from:)](<ossignpostintervalstate/init(from_).md>) — 从所提供的解码器中解码时间区间状态。

### 重新创建时间区间状态

- [beginState(id:)](<ossignpostintervalstate/beginstate(id_).md>) — 根据指定的 signpost ID 重新创建时间区间状态。

### 编码时间区间状态

- [encode(to:)](<ossignpostintervalstate/encode(to_).md>) — 将时间区间状态编码到所提供的编码器中。

## 另请参阅

### 开始带 signpost 标记的时间区间

- [beginInterval(_:id:)](<ossignposter/begininterval(__id_).md>) — 开始一个带 signpost 标记的时间区间。
- [beginInterval(_:id:_:)](<ossignposter/begininterval(__id___).md>) — 开始一个带 signpost 标记的时间区间，并附加指定的消息。
- [beginAnimationInterval(_:id:)](<ossignposter/beginanimationinterval(__id_).md>) — 开始一个用于测量动画的、带 signpost 标记的时间区间。
- [beginAnimationInterval(_:id:_:)](<ossignposter/beginanimationinterval(__id___).md>) — 开始一个用于测量动画的、带 signpost 标记的时间区间，并附加一条消息。
- [SignpostMetadata](signpostmetadata.md) — 表示你附加到 signpost 的消息的类型。
