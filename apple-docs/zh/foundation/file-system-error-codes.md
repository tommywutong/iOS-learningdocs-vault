---
title: 文件系统错误码
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/file-system-error-codes
source_url: 'https://developer.apple.com/documentation/foundation/file-system-error-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/file-system-error-codes.json'
content_hash: 'sha256:f2ef82f7b128e31a'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [文件系统](file-system.md)

# 文件系统错误码

<sub>API 集合</sub>

识别文件系统操作生成的常见错误码。

## 主题

### 错误码

- [NSFileNoSuchFileError](nsfilenosuchfileerror-swift.var.md) — 尝试对不存在的文件执行文件系统操作。
- [NSFileLockingError](nsfilelockingerror-swift.var.md) — 无法锁定文件。
- [NSFileReadUnknownError](nsfilereadunknownerror-swift.var.md) — 由于未知原因而无法读取。
- [NSFileReadNoPermissionError](nsfilereadnopermissionerror-swift.var.md) — 由于权限问题而无法读取。
- [NSFileReadInvalidFileNameError](nsfilereadinvalidfilenameerror-swift.var.md) — 由于文件名无效而无法读取。
- [NSFileReadCorruptFileError](nsfilereadcorruptfileerror-swift.var.md) — 由于文件损坏、格式错误或类似原因而无法读取。
- [NSFileReadNoSuchFileError](nsfilereadnosuchfileerror-swift.var.md) — 由于找不到相应文件而无法读取。
- [NSFileReadInapplicableStringEncodingError](nsfilereadinapplicablestringencodingerror-swift.var.md) — 由于字符串编码不适用而无法读取。
- [NSFileReadUnsupportedSchemeError](nsfilereadunsupportedschemeerror-swift.var.md) — 由于不支持指定的 URL 方案而无法读取。
- [NSFileReadTooLargeError](nsfilereadtoolargeerror-swift.var.md) — 由于指定文件过大而无法读取。
- [NSFileReadUnknownStringEncodingError](nsfilereadunknownstringencodingerror-swift.var.md) — 由于无法确定文件的字符串编码而无法读取。
- [NSFileWriteUnknownError](nsfilewriteunknownerror-swift.var.md) — 由于未知原因而无法写入。
- [NSFileWriteNoPermissionError](nsfilewritenopermissionerror-swift.var.md) — 由于权限问题而无法写入。
- [NSFileWriteInvalidFileNameError](nsfilewriteinvalidfilenameerror-swift.var.md) — 由于文件名无效而无法写入。
- [NSFileWriteFileExistsError](nsfilewritefileexistserror-swift.var.md) — 由于目标文件已存在而无法执行操作。
- [NSFileWriteInapplicableStringEncodingError](nsfilewriteinapplicablestringencodingerror-swift.var.md) — 由于字符串编码不适用而无法写入。
- [NSFileWriteUnsupportedSchemeError](nsfilewriteunsupportedschemeerror-swift.var.md) — 由于不支持指定的 URL 方案而无法写入。
- [NSFileWriteOutOfSpaceError](nsfilewriteoutofspaceerror-swift.var.md) — 由于磁盘空间不足而无法写入。
- [NSFileWriteVolumeReadOnlyError](nsfilewritevolumereadonlyerror-swift.var.md) — 由于宗卷为只读而无法写入。
- [NSFileManagerUnmountBusyError](nsfilemanagerunmountbusyerror-swift.var.md) — 由于宗卷正在使用中而无法卸载。
- [NSFileManagerUnmountUnknownError](nsfilemanagerunmountunknownerror-swift.var.md) — 由于未知原因而无法卸载宗卷。
- [NSFileErrorMinimum](nsfileerrorminimum-swift.var.md) — 为文件错误保留的错误码范围的起点。
- [NSFileErrorMaximum](nsfileerrormaximum-swift.var.md) — 为文件错误保留的错误码范围的终点。
