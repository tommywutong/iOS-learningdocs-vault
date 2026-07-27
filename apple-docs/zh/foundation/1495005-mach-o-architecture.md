---
title: Mach-O 架构
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1495005-mach-o-architecture
source_url: 'https://developer.apple.com/documentation/foundation/1495005-mach-o-architecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1495005-mach-o-architecture.json'
content_hash: 'sha256:48ac94e26c66da77'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [资源](resources.md) · [Bundle](bundle.md)

# Mach-O 架构

<sub>API 集合</sub>

描述套装可执行代码所支持 CPU 类型的常量。

## 主题

### 常量

- [NSBundleExecutableArchitectureARM64](nsbundleexecutablearchitecturearm64.md) — 64 位 ARM 架构。
- [NSBundleExecutableArchitectureI386](nsbundleexecutablearchitecturei386.md) — 32 位 Intel 架构。
- [NSBundleExecutableArchitectureX86_64](nsbundleexecutablearchitecturex86_64.md) — 64 位 Intel 架构。
- [NSBundleExecutableArchitecturePPC](nsbundleexecutablearchitectureppc.md) — 32 位 PowerPC 架构。
- [NSBundleExecutableArchitecturePPC64](nsbundleexecutablearchitectureppc64.md) — 64 位 PowerPC 架构。

## 另请参阅

### 从套装加载代码

- [executableArchitectures](bundle/executablearchitectures.md) — 一个数值数组，指示套装可执行文件支持的架构类型。
- [- preflightAndReturnError:](<bundle/preflight().md>) — 返回一个布尔值，指示是否能够成功加载套装的可执行代码。
- [- load](<bundle/load().md>) — 如果套装的可执行代码尚未加载，则将其动态加载到正在运行的程序中。
- [- loadAndReturnError:](<bundle/loadandreturnerror().md>) — 加载套装的可执行代码并返回所有错误。
- [- unload](<bundle/unload().md>) — 卸载与接收者关联的代码。
- [loaded](bundle/isloaded.md) — 套装的加载状态。
