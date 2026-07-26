---
title: ProximityReader
framework: ProximityReader
symbol_kind: module
role: collection
role_heading: Framework
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/proximityreader
source_url: 'https://developer.apple.com/documentation/proximityreader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/proximityreader.json'
content_hash: 'sha256:f5d928643aba4cdd'
translated: true
---

> 导航：[Technologies](technologies.md)

# ProximityReader

<sub>框架</sub>

使用 iPhone 读取非接触式实体卡和数字钱包卡。

## 概述

ProximityReader 框架支持 _iPhone 上的插卡、感应和刷卡付款_，该功能让某人的 iPhone 无需额外硬件即可充当销售点设备。ProximityReader 还支持从「钱包」App 读取会员卡。使用此框架可以从你的 App 发起付款流程。

使用此框架要求你与经过 Level 3 认证、参与该计划的付款服务提供商进行协调。请联系你的付款提供商，与其合作建立处理付款的工作流程。准备就绪后，请联系 Apple 并申请将 iPhone 上的插卡、感应和刷卡付款支持集成到你的 App 中所需的授权。有关申请此授权的信息，请参阅 [Setting up Tap to Pay on iPhone](proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone.md)。

> [!note] 注意
> iPhone 上的插卡、感应和刷卡付款遵循 PCI CPoC 标准，该标准使用经过 Level 2 认证的付款内核和用户界面来读取非接触式付款卡。

## 主题

### 付款卡读卡器

- [Setting up Tap to Pay on iPhone](proximityreader/setting-up-the-entitlement-for-tap-to-pay-on-iphone.md) — 申请并配置支持 iPhone 上插卡、感应和刷卡付款所需的授权。
- [Adding support for Tap to Pay on iPhone to your app](proximityreader/adding-support-for-tap-to-pay-on-iphone-to-your-app.md) — 配置你的 App，以便使用 iPhone 上的插卡、感应和刷卡付款来读取非接触式付款卡。
- [PaymentCardReader](proximityreader/paymentcardreader.md) — 用于在当前设备上配置 iPhone 上插卡、感应和刷卡付款的对象。
- [PaymentCardReaderSession](proximityreader/paymentcardreadersession.md) — 用于开始读取非接触式付款卡或会员卡的对象。

### 付款请求

- [PaymentCardTransactionRequest](proximityreader/paymentcardtransactionrequest.md) — 非接触式购买或退款请求，包含购买金额和货币信息。
- [PaymentCardVerificationRequest](proximityreader/paymentcardverificationrequest.md) — 用于验证非接触式付款卡详细信息的请求。
- [PaymentCardReadResult](proximityreader/paymentcardreadresult.md) — 付款卡读取操作的结果。

### Store and Forward 模式

- [StoreAndForwardBatch](proximityreader/storeandforwardbatch.md) — 存储要发送给付款服务提供商以供处理的数据的结构体。
- [StoreAndForwardBatchDeletionToken](proximityreader/storeandforwardbatchdeletiontoken.md) — 用于删除 Store and Forward 批次的安全令牌。
- [StoreAndForwardPaymentCardReaderSession](proximityreader/storeandforwardpaymentcardreadersession.md) — 用于在 Store and Forward 模式下开始读取非接触式付款卡或会员卡的对象。
- [StoreAndForwardStatus](proximityreader/storeandforwardstatus.md) — 描述 Store and Forward 会话状态的结构体。
- [PaymentCardReaderStore](proximityreader/paymentcardreaderstore.md) — 管理包含所有 Store and Forward 读取记录的存储的结构体。

### 会员卡请求

- [Accepting loyalty passes from Wallet](proximityreader/accepting-loyalty-passes-from-wallet.md) — 设置必要的组件，以便你的 App 可以开始使用 iPhone 上的插卡、感应和刷卡付款来读取和发放会员通行证。
- [VASRequest](proximityreader/vasrequest.md) — 读取非接触式会员卡并检索该用户会员计划标识符的请求。
- [VASReadResult](proximityreader/vasreadresult.md) — 请求读取会员卡信息的结果。

### 商户发现

- [ProximityReaderDiscovery](proximityreader/proximityreaderdiscovery.md) — 呈现 UI 以展示如何使用 iPhone 上的插卡、感应和刷卡付款的相关信息的对象。

### 移动证件读取器

- [Adopting the Verifier API in your iPhone app](proximityreader/adopting-the-verifier-api-in-your-iphone-app.md) — 在你的 App 中配置并测试 ID Verifier 支持，以读取移动证件。
- [Generating reader tokens for the Verifier API](proximityreader/generating-reader-tokens-for-the-verifier-api.md) — 配置你的服务器以生成读卡器令牌，为设备读取移动证件做好准备。
- [Checking IDs with the Verifier API](proximityreader/checking-ids-with-the-verifier-api.md) — 无需任何额外硬件即可读取并验证移动驾驶证、照片证件和国家身份证信息。
- [MobileDocumentReader](proximityreader/mobiledocumentreader.md) — 用于在当前设备上配置移动证件读取的对象。
- [MobileDocumentReaderSession](proximityreader/mobiledocumentreadersession.md) — 用于开始读取移动证件的对象。

### 移动证件请求

- [MobileDriversLicenseDisplayRequest](proximityreader/mobiledriverslicensedisplayrequest.md) — 从持有者处检索元素并在屏幕上显示结果以供目视检查的移动驾驶证请求。
- [MobileDriversLicenseDataRequest](proximityreader/mobiledriverslicensedatarequest.md) — 从持有者处检索元素并返回已验证证件元素的移动驾驶证请求。
- [MobileDriversLicenseRawDataRequest](proximityreader/mobiledriverslicenserawdatarequest.md) — 从持有者处检索元素并返回用于处理的原始响应数据的移动驾驶证请求。
- [MobileNationalIDCardDisplayRequest](proximityreader/mobilenationalidcarddisplayrequest.md) — 从持有者处检索元素并在屏幕上显示结果以供目视检查的移动国家身份证请求。
- [MobileNationalIDCardDataRequest](proximityreader/mobilenationalidcarddatarequest.md) — 从持有者处检索元素并返回已验证证件元素的移动国家身份证请求。
- [MobileNationalIDCardRawDataRequest](proximityreader/mobilenationalidcardrawdatarequest.md) — 从持有者处检索元素并返回用于处理的原始响应数据的移动国家身份证请求。
- [MobileDocumentDisplayRequest](proximityreader/mobiledocumentdisplayrequest.md) — 从持有者处检索元素并在屏幕上显示结果以供目视检查的移动证件请求。
- [MobileDocumentRequest](proximityreader/mobiledocumentrequest.md) — 表示移动证件请求的类型。
- [MobileDocumentDataRequest](proximityreader/mobiledocumentdatarequest.md) — 表示移动证件数据请求的类型。
- [MobileDocumentRawDataRequest](proximityreader/mobiledocumentrawdatarequest.md) — 表示移动证件原始数据请求的类型。
- [MobilePhotoIDDataRequest](proximityreader/mobilephotoiddatarequest.md) — 从持有者处检索元素并返回已验证证件元素的照片证件请求。
- [MobilePhotoIDRawDataRequest](proximityreader/mobilephotoidrawdatarequest.md) — 从持有者处检索元素并返回用于处理的原始响应数据的照片证件请求。
- [MobileDocumentAnyOfDataRequest](proximityreader/mobiledocumentanyofdatarequest.md) — 描述一组请求中任意一份移动证件的数据请求的类型。
- [MobileDocumentAnyOfRawDataRequest](proximityreader/mobiledocumentanyofrawdatarequest.md) — 描述一组请求中任意一份移动证件的原始数据请求的类型。

### Tap to Share

- [Adding support for Tap to Share to your app](proximityreader/adding-support-for-tap-to-share-to-your-app.md) — 在设备上请求并共享客户信息。
- [CustomerEngagement](proximityreader/customerengagement.md) — 商户与客户之间共享数据的枚举。 _(beta)_
- [CustomerEngagementSession](proximityreader/customerengagementsession.md) — 用于共享和请求客户信息的对象。 _(beta)_

### 错误

- [PaymentCardReaderError](proximityreader/paymentcardreadererror.md) — 指示读卡器配置问题的错误类型。
- [MobileDocumentReaderError](proximityreader/mobiledocumentreadererror.md) — 指示准备移动证件读取器会话及执行证件请求时出现问题的错误类型。

### Structures

- [MobileDocumentHolderName](proximityreader/mobiledocumentholdername.md) — 表示移动身份证件持有者姓名的类型。 _(beta)_
