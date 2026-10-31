---
title: 单位与测量
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/units-and-measurement
source_url: 'https://developer.apple.com/documentation/foundation/units-and-measurement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/units-and-measurement.json'
content_hash: 'sha256:5c66b4a611d8e982'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 单位与测量

<sub>API 集合</sub>

使用物理维度标记数值量，以便进行适应区域设置的格式化以及相关单位之间的转换。

## 主题

### 基础

- [Measurement](measurement.md) — 带有计量单位标记的数值量，支持单位转换和感知单位的计算。
- [NSMeasurement](nsmeasurement.md) — 带有计量单位标记的数值量，支持单位转换和感知单位的计算。
- [Unit](unit.md) — 表示计量单位的抽象类。
- [Dimension](dimension.md) — 表示有量纲计量单位的抽象类。

### 转换

- [UnitConverter](unitconverter.md) — 一个抽象类，提供如何将某一单位与其量纲的基本单位相互转换的描述。
- [UnitConverterLinear](unitconverterlinear.md) — 描述如何使用线性方程在单位之间进行转换。

### 物理维度

- [UnitArea](unitarea.md) — 面积的计量单位。
- [UnitLength](unitlength.md) — 长度的计量单位。
- [UnitVolume](unitvolume.md) — 体积的计量单位。
- [UnitAngle](unitangle.md) — 平面角和旋转的计量单位。

### 质量、重量与力

- [UnitMass](unitmass.md) — 质量的计量单位。
- [UnitPressure](unitpressure.md) — 压力的计量单位。

### 时间与运动

- [UnitAcceleration](unitacceleration.md) — 加速度的计量单位。
- [UnitDuration](unitduration.md) — 时间持续时长的计量单位。
- [UnitFrequency](unitfrequency.md) — 频率的计量单位。
- [UnitSpeed](unitspeed.md) — 速度的计量单位。

### 能量、热与光

- [UnitEnergy](unitenergy.md) — 能量的计量单位。
- [UnitPower](unitpower.md) — 功率的计量单位。
- [UnitTemperature](unittemperature.md) — 温度的计量单位。
- [UnitIlluminance](unitilluminance.md) — 照度的计量单位。

### 电

- [UnitElectricCharge](unitelectriccharge.md) — 电荷的计量单位。
- [UnitElectricCurrent](unitelectriccurrent.md) — 电流的计量单位。
- [UnitElectricPotentialDifference](unitelectricpotentialdifference.md) — 电位差的计量单位。
- [UnitElectricResistance](unitelectricresistance.md) — 电阻的计量单位。

### 浓度与分散

- [UnitConcentrationMass](unitconcentrationmass.md) — 质量浓度的计量单位。
- [UnitDispersion](unitdispersion.md) — 特定分散度数量的计量单位。

### 燃油效率

- [UnitFuelEfficiency](unitfuelefficiency.md) — 燃油效率的计量单位。

### 数据存储

- [UnitInformationStorage](unitinformationstorage.md) — 信息量的计量单位。

### 格式化测量值

- [MeasurementFormatUnitUsage](measurementformatunitusage.md) — 一种为格式化测量值提供通用用法的类型。

## 另请参阅

### 基本原理

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [Strings and Text](strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [Collections](collections.md) — 使用数组、字典、集合和专用集合来存储和迭代对象组或值组。
- [Dates and Times](dates-and-times.md) — 比较日期与时间，并执行日历和时区计算。
- [Data Formatting](data-formatting.md) — 在数值、日期、测量结果及其他值与适应区域设置的字符串表示形式之间进行转换。
- [Filters and Sorting](filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。
