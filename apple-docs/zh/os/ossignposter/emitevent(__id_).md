---
title: 'emitEvent(_:id:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/emitevent(_:id:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/emitevent%28_%3Aid%3A%29.json'
content_hash: 'sha256:b1e38f436c99f25c'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# emitEvent(_:id:)

<sub>实例方法</sub>

标记时间上的某个关注点。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive)
```

## 参数

- `name` — 事件的名称。

- `id` — 事件的标识符。默认值为 [exclusive](../ossignpostid/exclusive.md)。

## 讨论

你可以使用 [makeSignpostID()](<makesignpostid().md>) 和 [makeSignpostID(from:)](<makesignpostid(from_).md>) 方法为事件生成标识符，如下例所示：

```swift
// 使用默认子系统创建 signposter。
let signposter = OSSignposter()
        
// 生成要与该事件关联的 signpost ID。
let signpostID = signposter.makeSignpostID()
        
// 使用该 signpost ID 发出一个命名事件。
signposter.emitEvent("Example Event", id: signpostID)
```

## 另请参阅

### 发出单独的 signpost

- [emitEvent(_:id:_:)](<emitevent(__id___).md>) — 标记时间上的某个关注点，并附加指定的消息。
