---
title: 工作组
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/workgroups
source_url: 'https://developer.apple.com/documentation/os/workgroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/workgroups.json'
content_hash: 'sha256:2f12672612364b79'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# 工作组

<sub>API 集合</sub>

调度一个或多个线程，使其按固定间隔运行，并在特定截止时间前完成。

## 概述

一个工作组管理一个或多个协作完成共同目标的线程。使用工作组来协调处理实时音频工作的线程。把线程注册到工作组，有助于系统把工作导向合适的系统资源，也有助于系统在低功耗与最大渲染输出这两种相互竞争的需求之间进行权衡。

## 主题

### 基础

- [Tuning your code’s performance for Apple silicon](../apple-silicon/tuning-your-code-s-performance-for-apple-silicon.md) — 改进你的代码，以便在 Apple 芯片和基于 Intel 的 Mac 电脑上都获得最佳性能。

### 间隔任务

- [Porting your audio code to Apple silicon](../apple-silicon/porting-your-audio-code-to-apple-silicon.md) — 消除音频专属代码在 Apple 芯片上运行时出现的问题。
