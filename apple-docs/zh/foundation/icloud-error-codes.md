---
title: iCloud 错误码
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/icloud-error-codes
source_url: 'https://developer.apple.com/documentation/foundation/icloud-error-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/icloud-error-codes.json'
content_hash: 'sha256:9bd0ff1255826e42'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md)

# iCloud 错误码

<sub>API 集合</sub>

iCloud 相关错误发生时可能出现的错误码。

## 概述

当 iCloud 相关错误发生时，这些错误码与 [NSURL](nsurl.md) 对象上的 [NSURLUbiquitousItemDownloadingErrorKey](urlresourcekey/ubiquitousitemdownloadingerrorkey.md) 关联。

## 主题

### 常规 iCloud 文件错误

- [NSUbiquitousFileErrorMinimum](nsubiquitousfileerrorminimum-swift.var.md) — 表示 iCloud 错误的最小错误码值。
- [NSUbiquitousFileUnavailableError](nsubiquitousfileunavailableerror-swift.var.md) — 另一个设备尚未将该项目上传到 iCloud。
- [NSUbiquitousFileNotUploadedDueToQuotaError](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md) — 无法将该项目上传到 iCloud，因为这会导致账户超出配额。
- [NSUbiquitousFileUbiquityServerNotAvailable](nsubiquitousfileubiquityservernotavailable-swift.var.md) — 连接 iCloud 服务器失败。
- [NSUbiquitousFileErrorMaximum](nsubiquitousfileerrormaximum-swift.var.md) — 表示 iCloud 错误的最大错误码值。

### iCloud 共享错误

- [NSCloudSharingConflictError](nscloudsharingconflicterror-swift.var.md) — 尝试保存更改时发生冲突。
- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-swift.var.md) — 为云共享错误保留的错误码范围的终点。
- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-swift.var.md) — 为云共享错误保留的错误码范围的起点。
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-swift.var.md) — 由于网络故障而共享失败。
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-swift.var.md) — 当前用户没有执行所请求操作的权限。
- [NSCloudSharingOtherError](nscloudsharingothererror-swift.var.md) — 发生其他未具体说明的云共享错误。
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-swift.var.md) — 用户没有足够的可用存储空间来共享所请求的项目。
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-swift.var.md) — 由于已达到限制，无法再向共享中添加参与者。
