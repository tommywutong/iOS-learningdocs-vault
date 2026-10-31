---
title: 使用测光 Instruments 评估 App 的视频色彩
framework: AVFoundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/evaluating-an-app-s-video-color-using-light-measurement-instruments
source_url: 'https://developer.apple.com/documentation/avfoundation/evaluating-an-app-s-video-color-using-light-measurement-instruments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/evaluating-an-app-s-video-color-using-light-measurement-instruments.json'
content_hash: 'sha256:6eb75030acbe0a16'
translated: true
---

> 导航：[技术](../technologies.md) · [AVFoundation](../avfoundation.md) · [媒体读取与写入](media-reading-and-writing.md) · [评估 App 的视频色彩](evaluating-an-app-s-video-color.md)

# 使用测光 Instruments 评估 App 的视频色彩

<sub>文章</sub>

配合测试图案文件使用光谱辐射仪或色度计来测量屏前亮度。

## 概述

使用测试图案文件评估基于 AVFoundation 的 App 或工作流程的色彩特性。将这些文件输出到光谱辐射仪或色度计，以测量屏前（FoS）亮度，并将你的测量结果与预期值进行比较。

### 测量 FoS 亮度

使用 `SDR_BT709_HDTV` 文件夹中的测试文件（参见 [AVFoundation 开发者页面](https://developer.apple.com/av-foundation/)上的「Color Test Patterns」），配合光谱辐射仪或色度计等测量仪器来测量 FoS 亮度。测量时应在暗室中将仪器对准显示器中心，以防止杂散光或眩光影响测量结果。根据仪器的公差及其校准情况，读数可能会出现一些变化。

使用 `SDR_BT709_HDTV` 文件夹中的亮度斜坡测试图案文件来测量 FoS 亮度。在你的 App 或 QuickTime Player App 中打开测试图案影片文件，然后进行测量并与下面显示的结果进行比较。如果遇到相互矛盾的结果，请参阅[确保 App 的视频准确应用颜色](evaluating-an-app-s-video-color.md#Ensure-accurate-color-application-of-your-apps-video)，以确保你的 App 充分利用 macOS 的色彩管理能力。

以下列表总结了在 macOS 平台上针对标记为 BT.709（NCLC = 1-1-1）的视频文件的 FoS 亮度预期值（以尼特为单位输出）。

- **macOS 内置显示器** — 
- **** — _屏前亮度（FoS Nits）= Reference White Nits * linearBrightnessAttenuation * (Normalized Codeword)^(1.961)_

系统采用 1.961 的 gamma 值，这是基于明亮环境环绕的假设。线性亮度衰减在 0 到 1 之间变化，取决于显示器亮度滑块的位置。参考白亮度是指 Mac 显示器的峰值亮度能力。

- **通过 HDMI 接口连接的外部电视或显示器** — 
- **** — _屏前亮度（FoS Nits）= Reference White Nits * (Normalized Codeword)^(display’s EOTF gamma)_

参考白亮度是指外部电视或显示器的峰值亮度能力。显示器的 EOTF（电光传递函数）gamma 是电视或显示器用于将输入信号解码为线性光所用的 gamma 值。

- **Pro Display XDR Apple 参考模式** — Pro Display XDR（P3-1600 尼特）和 Apple Display（P3-500 尼特）：
- **** — _屏前亮度（FoS Nits）= Reference White Nits * linearBrightnessAttenuation * (Normalized Codeword)^(1.961)_

系统采用 1.961 的 gamma 值（基于明亮环境环绕的假设），与 macOS 内置显示器相同。线性亮度衰减在 0 到 1 之间变化，取决于显示器亮度滑块的位置。参考白亮度是指 Pro Display XDR 显示器在该模式下的峰值 SDR（标准动态范围）亮度能力，两种 Apple 参考模式均设置为 500 尼特。

- **Pro Display XDR HDR 视频（P3-ST 2084）参考模式** — 
- **** — _屏前亮度（FoS Nits）= Reference White Nits * (Normalized Codeword)^(1.961)_

参考白亮度是指 HDR 视频（P3 - ST 2084）模式的峰值 SDR 亮度能力，设置为 100 尼特。

- **Pro Display XDR BT.1886 参考模式** — HDTV Video（BT.709 – BT.1886）、NTSC Video（BT.601 SMPTE-C）以及 PAL 和 SECAM Video（BT.601 – EBU）：
- **** — _屏前亮度（FoS Nits）= a*(max(Normalized Codeword + b, 0))^(gamma)_

（其中 a 和 b 的推导依据 [Recommendation ITU-R BT.1886](https://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1886-0-201103-I!!PDF-E.pdf)）

a = (Lw ^ (1/gamma) - Lb ^ (1/gamma))^(gamma)

b = Lb ^ (1/gamma) / ((Lw ^ (1/gamma) - Lb ^ (1/gamma))

Lw = 100.0 尼特

Lb = 0.0005 尼特

gamma = 2.4

- **带系统 gamma 提升的 Pro Display XDR 自定参考模式** — 
- **** — _屏前亮度（FoS Nits）= Reference White Nits * (Normalized Codeword)^(1.961 * system-gamma-boost)_

参考白亮度（SDR 最大亮度）和系统 gamma 提升（≥ 1.0）在创建自定参考模式时设置。

## 另请参阅

### 视频评估

- [使用 QuickTime 测试图案文件评估视频](evaluating-video-using-quicktime-test-pattern-files.md) — 使用测试图案文件检查你的 App 或工作流程的颜色再现。
- [使用视频测试设备评估 App 的视频色彩](evaluating-an-app-s-video-color-using-video-test-equipment.md) — 将测试图案文件输出到矢量示波器或波形分析仪以审查视频信号。
