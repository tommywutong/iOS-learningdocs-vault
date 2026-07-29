---
title: 2021 年 9 月 10 日 WhatsApp 如何实现端到端加密备份
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/'
original_language: en
published: 2021-09-10
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:51e13e504def54b8'
translated: true
---

> 原文：[Sep 10, 2021 How WhatsApp is enabling end-to-end encrypted backups](https://engineering.fb.com/2021/09/10/security/whatsapp-e2ee-backups/)　·　Meta Engineering — iOS

多年来，为了保护用户消息的隐私，WhatsApp 默认提供[端到端加密](https://engineering.fb.com/2021/04/16/security/dit/)，确保消息只有发送者和接收者能够看到，中间的任何人都无法查看。现在，我们计划让用户也可以选择使用端到端加密来保护他们的 WhatsApp 备份。

用户已经可以通过 Google Drive 和 iCloud 等云服务备份 WhatsApp 消息历史。WhatsApp 本身无法访问这些备份，它们由各个云存储服务负责保护。

但如果用户选择启用端到端加密（E2EE）备份（该功能即将推出），那么无论是 WhatsApp 还是备份服务提供商，都将无法访问用户的备份或备份加密密钥。

## 端到端加密备份的工作原理

### 生成加密密钥与密码

为了实现端到端加密备份，我们开发了一套全新的加密密钥存储系统，同时支持 iOS 和 Android。启用端到端加密备份后，备份将使用一个唯一的、随机生成的加密密钥进行加密。用户可以选择手动保管密钥，或使用用户密码来保护密钥。当用户选择密码方式时，密钥会被存储在一个基于硬件安全模块（HSM）构建的备份密钥保管库（Backup Key Vault）中——这是一种专用的安全硬件，可用于安全地存储加密密钥。当帐户所有者需要访问其备份时，他们可以使用自己的加密密钥，或者使用个人密码从基于 HSM 的备份密钥保管库中检索加密密钥，进而解密备份。

基于 HSM 的备份密钥保管库将负责执行密码验证尝试策略，并在一定次数的不成功尝试后，使密钥永久不可访问。这些安全措施可防范对密钥的暴力破解尝试。WhatsApp 仅知道保管库中存在一个密钥，但无法获知密钥本身。

### 在备份密钥保管库中存储密钥

WhatsApp 的前端服务 ChatD 负责处理客户端连接和客户端-服务器身份验证，并将实现一个协议，用于在备份与 WhatsApp 服务器之间传输密钥。客户端与基于 HSM 的备份密钥保管库之间将交换加密消息，ChatD 本身无法访问这些消息的内容。

基于 HSM 的备份密钥保管库位于 ChatD 后端，为备份加密密钥提供高可用且安全的存储。备份本身将以持续的数据流形式生成，并使用生成的密钥通过对称加密进行加密。启用端到端加密备份后，备份经过加密即可存储在设备之外（例如 iCloud 或 Google Drive）。

WhatsApp 服务超过 20 亿用户，该产品的核心挑战之一是确保基于 HSM 的备份密钥保管库能够可靠运行。为了确保系统始终可用，基于 HSM 的备份密钥保管库服务将在地理上分布于多个数据中心，以便在某个数据中心[故障](https://engineering.fb.com/2021/06/02/data-center-engineering/how-facebook-deals-with-pcie-faults-to-keep-our-data-centers-running-reliably/)时仍能保持运行。

![WhatsApp 端到端加密备份](https://engineering.fb.com/wp-content/uploads/2021/09/WhatsApp_E2EE-Backups_64-digit-encryption.jpeg?w=1024)

<sub>备份可以使用由 64 位数字组成的加密密钥进行端到端加密。</sub>

![WhatsApp 端到端加密备份](https://engineering.fb.com/wp-content/uploads/2021/09/WhatsApp_E2EE-Backups_user-password.jpeg?w=1024)

<sub>备份也可以使用密码保护，此时加密密钥会保存到基于 HSM 的备份密钥保管库中。</sub>

### 基于 HSM 的备份密钥保管库及加密与解密流程

当帐户所有者使用个人密码保护其端到端加密备份时，基于 HSM 的备份密钥保管库将负责存储和保护该密钥。

当用户想要检索其备份时：

1. 他们输入密码，密码会被加密，然后由备份密钥保管库进行验证。
2. 密码验证通过后，备份密钥保管库会将加密密钥发送回 WhatsApp 客户端。
3. 客户端拿到密钥后，即可解密备份。

或者，如果帐户所有者选择仅使用由 64 位数字组成的密钥，则他们需要手动输入该密钥来解密和访问备份。

端到端加密备份将在未来几周内于 iOS 和 Android 上推出。请查看[端到端加密备份白皮书](https://www.whatsapp.com/security/WhatsApp_Security_Encrypted_Backups_Whitepaper.pdf)，了解更多技术细节。
