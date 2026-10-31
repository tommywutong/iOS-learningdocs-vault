---
title: 'os_signpost(_:dso:log:name:signpostID:_:_:)'
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/os_signpost(_:dso:log:name:signpostid:_:_:)-nez5'
source_url: 'https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:_:_:)-nez5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost%28_%3Adso%3Alog%3Aname%3Asignpostid%3A_%3A_%3A%29-nez5.json'
content_hash: 'sha256:9e4aecfd3817d096'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost(_:dso:log:name:signpostID:_:_:)

<sub>函数</sub>

把动画的开始记录为代码中的一个关注点，并在日志中包含指定的消息。

> [!warning] 已废弃
> 请改用 [beginAnimationInterval(_:id:_:)](<ossignposter/beginanimationinterval(__id___).md>)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_signpost(_ animationBegin: OSSignpostAnimationBegin, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive, _ format: AnimationFormatString.OSLogMessage, _ arguments: any CVarArg...)
```

## 参数

- `animationBegin` — 要创建的动画 signpost 类型。

- `log` — 用于写入该 signpost 的日志对象。

- `name` — signpost 的名称。

- `signpostID` — 用于区分名称相同的多个 signpost 的标识符。如果为此参数指定 [invalid](ossignpostid/invalid.md) 或 [null](ossignpostid/null.md)，此方法不执行任何操作。

- `format` — 生成人类可读日志消息的常量字符串或格式字符串。

- `arguments` — 代入 `format` 字符串参数的附加参数。按它们在字符串中出现的顺序传入预期数量的参数。如果 `format` 是常量字符串，不要包含任何附加参数。

## 另请参阅

### 测量事件

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件，并附带一条详细消息。 _(已废弃)_
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — 把动画的开始记录为代码中的一个关注点，不附带消息。 _(已废弃)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — 测量动画时使用的 signpost 选项。 _(已废弃)_
- [AnimationFormatString](animationformatstring.md) — 一个命名空间，包含与动画相关的 signpost 专用工具。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。
