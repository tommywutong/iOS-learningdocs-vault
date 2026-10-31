---
title: 'os_signpost(_:dso:log:name:signpostID:)'
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/os/os_signpost(_:dso:log:name:signpostid:)-12m3v'
source_url: 'https://developer.apple.com/documentation/os/os_signpost(_:dso:log:name:signpostid:)-12m3v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost%28_%3Adso%3Alog%3Aname%3Asignpostid%3A%29-12m3v.json'
content_hash: 'sha256:fe69742ce8127180'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost(_:dso:log:name:signpostID:)

<sub>函数</sub>

把动画的开始记录为代码中的一个关注点，不附带消息。

> [!warning] 已废弃
> 请改用 [beginAnimationInterval(_:id:)](<ossignposter/beginanimationinterval(__id_).md>)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func os_signpost(_ animationBegin: OSSignpostAnimationBegin, dso: UnsafeRawPointer = #dsohandle, log: OSLog, name: StaticString, signpostID: OSSignpostID = .exclusive)
```

## 参数

- `animationBegin` — 要创建的动画 signpost 类型。

- `log` — 用于写入该 signpost 的日志对象。

- `name` — signpost 的名称。

- `signpostID` — 用于区分名称相同的多个 signpost 的标识符。如果为此参数指定 [invalid](ossignpostid/invalid.md) 或 [null](ossignpostid/null.md)，此方法不执行任何操作。

## 另请参阅

### 测量事件

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件，并附带一条详细消息。 _(已废弃)_
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — 把动画的开始记录为代码中的一个关注点，并在日志中包含指定的消息。 _(已废弃)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — 测量动画时使用的 signpost 选项。 _(已废弃)_
- [AnimationFormatString](animationformatstring.md) — 一个命名空间，包含与动画相关的 signpost 专用工具。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。
