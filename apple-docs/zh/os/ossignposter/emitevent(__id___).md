---
title: 'emitEvent(_:id:_:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignposter/emitevent(_:id:_:)'
source_url: 'https://developer.apple.com/documentation/os/ossignposter/emitevent(_:id:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignposter/emitevent%28_%3Aid%3A_%3A%29.json'
content_hash: 'sha256:4988a8b15b923727'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignposter](../ossignposter.md)

# emitEvent(_:id:_:)

<sub>实例方法</sub>

标记时间上的某个关注点，并附加指定的消息。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func emitEvent(_ name: StaticString, id: OSSignpostID = .exclusive, _ message: SignpostMetadata)
```

## 参数

- `name` — 事件的名称。

- `id` — 事件的标识符。默认值为 [exclusive](../ossignpostid/exclusive.md)。

- `message` — signposter 附加到该事件的插值字符串。消息中的每一处插值都可以指定各自的格式和隐私选项。更多信息参见 [Message Argument Formatters](../message-argument-formatters.md)。

## 讨论

> [!important] 重要
> 不要创建 [SignpostMetadata](../signpostmetadata.md) 的实例。请改为向 `message` 参数提供插值字符串，系统会自动完成转换。

你可以使用 [makeSignpostID()](<makesignpostid().md>) 和 [makeSignpostID(from:)](<makesignpostid(from_).md>) 方法为事件生成标识符，如下例所示：

```swift
let accountNumber = "12345678"

// 使用默认子系统创建 signposter。
let signposter = OSSignposter()
        
// 生成要与该事件关联的 signpost ID。
let signpostID = signposter.makeSignpostID()
        
// 使用该 signpost ID 发出一个命名事件，并附加一条
// 安全插值敏感数据的消息。
signposter.emitEvent("New Account Created", id: signpostID,
    "Account: \(accountNumber, privacy: .sensitive(mask: .hash))")
```

## 另请参阅

### 发出单独的 signpost

- [emitEvent(_:id:)](<emitevent(__id_).md>) — 标记时间上的某个关注点。
