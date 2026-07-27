---
title: 为 iOS 编写 ARMv7 代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/writing-armv7-code-for-ios
source_url: 'https://developer.apple.com/documentation/xcode/writing-armv7-code-for-ios'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/writing-armv7-code-for-ios.json'
content_hash: 'sha256:06ebf4bb4636fdc0'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Application binary interfaces](application-binary-interfaces.md)

# 为 iOS 编写 ARMv7 代码

<sub>文章</sub>

创建符合 iOS 所支持的应用程序二进制接口（ABI）的 ARMv7 汇编语言指令。

## 概述

ARMv7 环境和 ARMv6 环境的调用约定几乎完全相同。因此，你为 ARMv7 环境构建的任何 App 都能够在 ARMv6 环境中运行，反之亦然。不过，ARMv7 环境的一些特性会偏离或扩展 ARMv6 环境的特性。

### 在 ARMv7 中保留特定寄存器

除下表列出的变化和新增内容外，ARMv7 架构保留的寄存器与 ARMv6 架构相同：

| 类型 | 名称 | 是否保留 | 说明 |
|---|---|---|---|
| VFP 寄存器 | D0-D7 | 否 | 在 ARMv7 上也称为 Q0-Q3。这些寄存器在 ARMv7 上可从 Thumb 模式访问。 |
|  | D8-D15 | 是 | 在 ARMv7 上也称为 Q4-Q7。这些寄存器在 ARMv7 上可从 Thumb 模式访问。 |
|  | D16-D31 | 否 | 也称为 Q8-Q15。这些寄存器仅在 ARMv7 中可用。 |

有关寄存器保留的更多指南，参见[在 ARMv6 中保留特定寄存器](writing-armv6-code-for-ios.md#Preserve-specific-registers-in-ARMv6)。

### 用同一份汇编代码生成 ARM 或 Thumb 代码

ARMv7 中的 Thumb 版本与 ARM 汇编指令兼容。具体来说，Thumb 能够保存和恢复 VFP 寄存器的内容，且 ARMv7 汇编使用一套统一的助记符。

下面的示例展示了一个保存关键寄存器（包括若干 VFP 寄存器）的序言，它还为局部存储分配了 36 字节。

```other
push add  {r4-r7, lr}     // 保存 LR、R7 和 R4-R6。
add       r7, sp, #12     // 调整 R7，使其指向保存的 R7。
push      {r8, r10, r11}  // 保存其余 GPR（R8、R10、R11）。
vstmdb    sp!, {d8-d15}   // 保存 VFP/Advanced SIMD 寄存器 D8
                          //（也称为 S16-S31、Q4-Q7）。
sub       sp, sp, #36     // 为局部存储分配空间。
```

下面的示例展示了恢复前述序言所保存的寄存器的尾声：

```other
add       sp, sp, #36     // 释放局部存储空间。
vldmia    sp!, {d8-d15}   // 恢复 VFP/Advanced SIMD 寄存器。
pop       {r8, r10, r11}  // 恢复 R8-R11。
pop       {r4-r7, pc}     // 恢复 R4-R6、保存的 R7，并
                          // 返回保存的 LR
```

## 另请参阅

### iOS 接口

- [为 iOS 编写 ARMv6 代码](writing-armv6-code-for-ios.md) — 创建符合 iOS 所支持的应用程序二进制接口（ABI）的 ARMv6 汇编语言指令。
