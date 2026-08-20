---
title: 令人费解的 bridgeOS 崩溃
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/12/22/obscure-bridgeos-crash/'
original_language: en
published: 2020-12-22
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75988db23c844446'
translated: true
---

> 原文：[Obscure bridgeOS crash](https://www.jessesquires.com/blog/2020/12/22/obscure-bridgeos-crash/)　·　Jesse Squires

这对我来说还是头一遭。我把 MacBook 搁那儿几个小时再回来，发现它居然关机了——明明我离开时是开机状态。机器当时处于空闲状态，没有运行任何特定任务。我原以为是 macOS 内核恐慌（kernel panic），但重新启动后，我发现崩溃是由 bridgeOS 引起的。

[bridgeOS](https://en.wikipedia.org/wiki/BridgeOS)（watchOS 的修改版本）在现代 MacBook 上负责一些任务。它由 [T2 芯片](https://en.wikipedia.org/wiki/Apple-designed_processors#T_series)驱动，操控着 Touch Bar 和[安全隔区（Secure Enclave）](https://en.wikipedia.org/wiki/IOS#Secure_Enclave)。

崩溃的详细信息含糊得令人失望：

```
Unexpected SoC (system) watchdog reset occurred
```

我猜测崩溃与 Touch Bar 有关——[我讨厌这东西](https://www.jessesquires.com/blog/2020/07/08/best-touch-bar-configuration-for-people-who-hate-the-touch-bar/)。不过，由于信息太少，很难准确判断到底发生了什么。我在网上搜了一圈，没有任何结果。

为什么这些笔记本电脑还在配 Touch Bar？它到底有多大用处？反正我讨厌它，我认识的每个人都讨厌它。而现在，它居然能（潜在地）让整台机器崩溃——这让我更讨厌它了。

也许到了配备新一代 [M 系列芯片](https://en.wikipedia.org/wiki/Apple_M1)的下一代机器，就不再需要 bridgeOS 和独立的 T2 芯片了——如果我们运气好的话，还能有个选项把 Touch Bar **拆掉**。

![bridgeOS 崩溃](https://www.jessesquires.com/img/blog/bridge-os-crash.jpg)
