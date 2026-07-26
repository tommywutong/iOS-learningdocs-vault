---
title: 遗留的 Signpost 符号
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/legacy-signpost-symbols
source_url: 'https://developer.apple.com/documentation/os/legacy-signpost-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/legacy-signpost-symbols.json'
content_hash: 'sha256:a8d59196fa6f5484'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 遗留的 Signpost 符号

<sub>API 集合</sub>

把你的代码从这些遗留符号迁移出来。

## 主题

### 测量事件

- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-2oz8u.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-2om9b.md>) — 把代码中的某个关注点记录为一个时间区间，或者记录为一个用于在 Instruments 中调试性能的事件，并附带一条详细消息。 _(已废弃)_
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:)](<os_signpost(__dso_log_name_signpostid_)-12m3v.md>) — 把动画的开始记录为代码中的一个关注点，不附带消息。 _(已废弃)_
- [os_signpost(_:dso:log:name:signpostID:_:_:)](<os_signpost(__dso_log_name_signpostid_____)-nez5.md>) — 把动画的开始记录为代码中的一个关注点，并在日志中包含指定的消息。 _(已废弃)_
- [OSSignpostAnimationBegin](ossignpostanimationbegin.md) — 测量动画时使用的 signpost 选项。 _(已废弃)_
- [AnimationFormatString](animationformatstring.md) — 一个命名空间，包含与动画相关的 signpost 专用工具。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。

## 另请参阅

### 测量事件

- [Recording Performance Data](recording-performance-data.md) — 添加 signpost 来记录感兴趣的、基于时间的事件。
- [OSSignposter](ossignposter.md) — 用于借助统一日志系统测量任务性能的对象。
- [OSSignpostType](ossignposttype.md) — signpost 的各种类型。 _(已废弃)_
- [os_signpost_id_t](os_signpost_id_t.md) — 用于区分名称和目标日志相同的多个 signpost 的标识符。
