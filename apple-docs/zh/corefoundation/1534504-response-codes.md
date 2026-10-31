---
title: 响应码
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1534504-response-codes
source_url: 'https://developer.apple.com/documentation/corefoundation/1534504-response-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1534504-response-codes.json'
content_hash: 'sha256:d75b625716469ec8'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFUserNotification](cfusernotification.md)

# 响应码

<sub>API 集合</sub>

标识用于关闭通知对话框所按下按钮的响应码。

## 概述

要从已关闭通知的响应标志中提取该值（例如由 [CFUserNotificationReceiveResponse](<cfusernotificationreceiveresponse(______).md>) 返回的值），必须先对返回的响应标志与 `0x3` 执行按位与（bitwise-AND）运算，然后再将该值与这些常量进行比较。

## 主题

### 常量

- [kCFUserNotificationDefaultResponse](kcfusernotificationdefaultresponse.md) — 按下了默认按钮。
- [kCFUserNotificationAlternateResponse](kcfusernotificationalternateresponse.md) — 按下了备选按钮。
- [kCFUserNotificationOtherResponse](kcfusernotificationotherresponse.md) — 按下了第三个按钮。
- [kCFUserNotificationCancelResponse](kcfusernotificationcancelresponse.md) — 未按下任何按钮，且通知已超时。

## 另请参阅

### 常量

- [提醒级别](1534483-alert-levels.md) — 标识用户通知严重程度的标志。
- [按钮标志](1534481-button-flags.md) — 用于更改用户通知对话框中按钮显示方式的标志。
- [提醒级别](1534483-alert-levels.md) — 标识用户通知严重程度的标志。
- [按钮标志](1534481-button-flags.md) — 用于更改用户通知对话框中按钮显示方式的标志。
- [对话框描述键](dialog-description-keys.md) — 用户通知描述字典中使用的键，该字典描述要显示的通知对话框内容。
