---
title: 'Labyrinth 1.1：让端到端加密备份更加可靠'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2026/05/11/security/labyrinth-1-1-end-to-end-encrypted-e2ee-backups-more-reliable/'
original_language: en
published: 2026-05-11
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:7af382bf2e8ed5da'
translated: true
---

> 原文：[Labyrinth 1.1: Making End-to-End Encrypted Backups Even More Reliable](https://engineering.fb.com/2026/05/11/security/labyrinth-1-1-end-to-end-encrypted-e2ee-backups-more-reliable/)　·　Meta Engineering — iOS

- 我们正在推出 Labyrinth 1.1 版本，这是一套加密存储系统与协议，用于保护 Messenger 上的消息与历史记录。
- Labyrinth 1.1 通过一个新的子协议增强了端到端加密备份的可靠性，帮助消息在设备丢失、更换设备以及登录间隔过长的情况下依然完整保留。
- 更多详情，请阅读我们更新的白皮书《[Labyrinth 加密消息存储协议](https://engineering.fb.com/wp-content/uploads/2026/05/Minos-Updates-2026-Encrypted-Backups-White-Paper.pdf)》。

良好的安全性始终应当隐于无形。当 Meta 在 [2023 年为 Messenger 推出加密备份](https://engineering.fb.com/2023/12/06/security/building-end-to-end-security-for-messenger/)时，我们为大规模端到端加密（E2EE）消息服务设立了新标杆。借助 E2EE 消息备份，你的消息历史可以随你跨设备使用，而任何其他方（包括 Meta）都无法读取。

今天，我们正在推进此前与 Labyrinth 一起开始的工作——Labyrinth 是我们用于在 Messenger 账户的设备之间对存储的消息历史进行端到端加密的协议。[Labyrinth 1.1](https://engineering.fb.com/wp-content/uploads/2026/05/Minos-Updates-2026-Encrypted-Backups-White-Paper.pdf) 通过一个新的子协议改善了备份可靠性，该协议能让消息在发送时就直接存入加密备份，而无需等待设备重新上线——后者是当前 Messenger 加密备份的工作方式。

这意味着即使你丢失手机、更换设备或两次登录之间间隔很长时间，你的消息也是安全的。每条消息都被一个消息加密密钥包裹，发送方直接将该密钥放入收件人的加密备份中——就像将一个密封的信封投进只有收件人才能打开的锁箱。除了你和与你交谈的人之外，没有人能读取你的消息——就连我们也不能。

我们正在向 Messenger 广泛推出 Labyrinth 1.1，并且已经看到了显著的成效：更多消息成功备份，更多人在更换设备时恢复了完整的消息历史。

## 阅读白皮书

更多信息，请阅读我们更新的白皮书《[Labyrinth 加密消息存储协议](https://engineering.fb.com/wp-content/uploads/2026/05/Minos-Updates-2026-Encrypted-Backups-White-Paper.pdf)》。
