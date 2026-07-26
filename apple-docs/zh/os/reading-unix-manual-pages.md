---
title: 阅读 UNIX 联机手册
framework: os
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/reading-unix-manual-pages
source_url: 'https://developer.apple.com/documentation/os/reading-unix-manual-pages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/reading-unix-manual-pages.json'
content_hash: 'sha256:61d679fd58ba53ac'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# 阅读 UNIX 联机手册

<sub>文章</sub>

使用「终端」App 阅读底层 UNIX 工具和 API 的文档。

## 概述

UNIX 联机手册，也就是所谓的 _man pages_，记录了底层 UNIX 命令行工具、API 和文件格式。如果你在系统最底层工作，不要错过这份丰富的信息来源。

### 在「终端」App 中显示一个 man page

输入 `man` 以及你想查阅其文档的工具或 API 的名称，然后按下 Return 键。

![两个「终端」窗口，第一个显示要输入的命令，第二个显示结果。](../../../attachments/602374384e61f1b28c8ac34c1806b57b/media-3087691@2x.png)

因为 man page 比窗口大，「终端」只会显示页面的第一部分。按 Space 键显示后续部分，或按 Q 键退出 `man` 工具。

> [!important] 重要
> 面向开发者的 man page 随 Xcode 一起分发。`man` 工具会在当前活跃的开发者目录中搜索 man page。如果你安装了多份 Xcode，可以用 `xcode-select` 命令行工具选择当前活跃的开发者目录。详情参见 `xcode-select` 的 man page。

### 搜索特定的分节

联机手册的第 1 节涵盖命令行工具，第 2 节涵盖系统调用，第 3 节涵盖用户空间库，以此类推。如果不指定分节，`man` 会显示第一个含有匹配条目的分节里的页面。例如，下面这条命令会显示 `open` 命令行工具的 man page。

```bash
$ man open
```

如果你想获取 `open` 系统调用的 man page，指定第 2 节。

```bash
$ man 2 open
```

如果不确定该用哪个分节，用 `-k` 选项做关键字搜索。例如，下面这条命令会显示所有提到 _open_ 的 man page。

```bash
$ man -k open
```

### 了解 man page 的更多信息

`man` 命令行工具自己也有 man page，是深入了解这项功能的好地方。

```bash
$ man man
```
