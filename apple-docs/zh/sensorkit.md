---
title: SensorKit
framework: SensorKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/sensorkit
source_url: 'https://developer.apple.com/documentation/sensorkit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/sensorkit.json'
content_hash: 'sha256:7d8926f18f4fda26'
translated: true
---

> 导航：[Technologies](technologies.md)

# SensorKit

<sub>框架</sub>

从 iPhone 或已配对的 Apple Watch 上的传感器检索数据和派生指标。

## 概述

系统会使用设备上的各种传感器采集信息，SensorKit 让 App 能够访问部分原始数据，或者系统从传感器处理得到的指标，例如：

- 步数信息
- 加速度计或转速数据
- 用户手腕上手表的佩戴状态
- 物理环境中的环境光
- 用户日常通勤或出行路线的详情

完整列表参见 [SRSensor](sensorkit/srsensor.md)。

> [!note] 注意
> 这个框架会忽略你使用 Mac Catalyst 构建的 Mac App，以及在 visionOS 上运行的兼容 iPad 和 iPhone App 发出的调用。

## 主题

### 基础

- [SensorKit updates](updates/sensorkit.md) — 了解 SensorKit 的重要变更。

### 设置

- [Configuring your project for sensor reading](sensorkit/configuring-your-project-for-sensor-reading.md) — 为你的 App 添加元数据，以获取访问传感器数据所需的系统和用户权限。
- [SRSensorReader](sensorkit/srsensorreader.md) — 一个建立用户授权并记录特定传感器数据的对象。 _(已废弃)_

### 授权

- [com.apple.developer.sensorkit.reader.allow](bundleresources/entitlements/com.apple.developer.sensorkit.reader.allow.md) — App 预先获批的研究项目访问传感器数据所需的必要授权。

### 查询数据

- [SRFetchRequest](sensorkit/srfetchrequest.md) — 一个定义样本查询条件的对象。
- [SRFetchResult](sensorkit/srfetchresult.md) — 传感器读取器所获取的已记录数据。

### 解析数据

- [SRAmbientLightSample](sensorkit/srambientlightsample.md) — 用户所处环境中的环境光强度。
- [SRDeviceUsageReport](sensorkit/srdeviceusagereport.md) — 用户使用其设备、特定 Apple App 或网站的频率和相对时长。
- [SRKeyboardMetrics](sensorkit/srkeyboardmetrics.md) — 设备键盘的配置及其使用模式。
- [SRMediaEvent](sensorkit/srmediaevent.md) — 用户与媒体对象（如图像或视频）的一次交互。
- [SRMessagesUsageReport](sensorkit/srmessagesusagereport.md) — 一个描述用户在一段时间内 Messages App 活动情况的对象。
- [SRPhoneUsageReport](sensorkit/srphoneusagereport.md) — 一个描述用户在一段时间内电话活动情况的对象。
- [SRVisit](sensorkit/srvisit.md) — 用户在其每日出行路线中的进度。
- [SRWristDetection](sensorkit/srwristdetection.md) — 佩戴者手腕上手表的佩戴状态。

### 删除样本

- [SRDeletionRecord](sensorkit/srdeletionrecord.md) — 一个描述框架删除样本原因的对象。

### 解析语音

- [SRSpeechMetrics](sensorkit/srspeechmetrics.md) — 一个表示某段语音相关指标的对象。
- [SRSpeechExpression](sensorkit/srspeechexpression.md) — 一个表示某段语音相关指标和语音分析结果的对象。

### 解析面部

- [SRFaceMetrics](sensorkit/srfacemetrics.md) — 一个表示用户面部相关指标的对象。
- [SR_ARKIT_SUPPORTED](sensorkit/sr_arkit_supported.md) — 一个标志位，指示 ARKit 框架在 SensorKit 框架所用的 SDK 中是否可用。

### 记录手腕温度

- [SRWristTemperatureSession](sensorkit/srwristtemperaturesession.md) — 一个表示设备在一段时间内记录的手腕温度的对象。
- [SRWristTemperature](sensorkit/srwristtemperature.md) — 用户睡眠时手腕的温度。

### 记录心电图数据

- [SRElectrocardiogramSample](sensorkit/srelectrocardiogramsample.md) — 心电图传感器的样本数据。

### 记录光电容积描记数据

- [SRPhotoplethysmogramSample](sensorkit/srphotoplethysmogramsample.md) — 光电容积描记（PPG）传感器的样本数据。

### 类

- [SRAcousticSettings](sensorkit/sracousticsettings.md)
- [SRHeadphoneSettings](sensorkit/srheadphonesettings.md) _(beta)_
- [SRReader](sensorkit/srreader.md) — `SRReader` 是访问各类设备传感器数据的主要接口。 _(beta)_
- [SRSleepSession](sensorkit/srsleepsession.md)
- [SRSourceDevice](sensorkit/srsourcedevice.md) _(beta)_

### 协议

- [SRDataSensor](sensorkit/srdatasensor.md) — `SRDataSensor` 是所有传感器类型的基础协议，为 SensorKit 生态系统提供类型安全性和一致性。每个遵循该协议的传感器类型都会指定其生成的数据种类，从而支持编译期校验和类型安全的数据访问方式。 _(beta)_

### 结构体

- [SRAccelerometerSensor](sensorkit/sraccelerometersensor.md) _(beta)_
- [SRAcousticSettingsSensor](sensorkit/sracousticsettingssensor.md) _(beta)_
- [SRAmbientLightSensor](sensorkit/srambientlightsensor.md) _(beta)_
- [SRAmbientPressureSensor](sensorkit/srambientpressuresensor.md) _(beta)_
- [SRDeviceUsageSensor](sensorkit/srdeviceusagesensor.md) _(beta)_
- [SRElectrocardiogramSensor](sensorkit/srelectrocardiogramsensor.md) _(beta)_
- [SRFaceMetricsSensor](sensorkit/srfacemetricssensor.md) _(beta)_
- [SRFetchResponse](sensorkit/srfetchresponse.md) — 一个容纳从 SensorKit 数据流中获取的传感器数据样本的泛型容器。 _(beta)_
- [SRHeadphoneMotionSensor](sensorkit/srheadphonemotionsensor.md) _(beta)_
- [SRHeadphoneSettingsSensor](sensorkit/srheadphonesettingssensor.md) _(beta)_
- [SRHeartRateSensor](sensorkit/srheartratesensor.md) _(beta)_
- [SRKeyboardMetricsSensor](sensorkit/srkeyboardmetricssensor.md) _(beta)_
- [SRMediaEventsSensor](sensorkit/srmediaeventssensor.md) _(beta)_
- [SRMessagesUsageSensor](sensorkit/srmessagesusagesensor.md) _(beta)_
- [SROdometerSensor](sensorkit/srodometersensor.md) _(beta)_
- [SROnWristStateSensor](sensorkit/sronwriststatesensor.md) _(beta)_
- [SRPedometerDataSensor](sensorkit/srpedometerdatasensor.md) _(beta)_
- [SRPhoneUsageSensor](sensorkit/srphoneusagesensor.md) _(beta)_
- [SRPhotoplethysmogramSensor](sensorkit/srphotoplethysmogramsensor.md) _(beta)_
- [SRRotationRateSensor](sensorkit/srrotationratesensor.md) _(beta)_
- [SRSiriSpeechMetricsSensor](sensorkit/srsirispeechmetricssensor.md) _(beta)_
- [SRSleepSessionsSensor](sensorkit/srsleepsessionssensor.md) _(beta)_
- [SRTelephonySpeechMetricsSensor](sensorkit/srtelephonyspeechmetricssensor.md) _(beta)_
- [SRVisitsSensor](sensorkit/srvisitssensor.md) _(beta)_
- [SRWristTemperatureSensor](sensorkit/srwristtemperaturesensor.md) _(beta)_
