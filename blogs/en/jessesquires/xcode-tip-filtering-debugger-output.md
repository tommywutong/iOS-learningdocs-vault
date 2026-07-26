---
title: 'Xcode Tip: filtering debugger output'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/03/02/xcode-tip-filter-console/'
original_language: en
published: 2023-03-02
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:be8ab5fbe84fa9ac'
translated: false
---

> 原文：[Xcode Tip: filtering debugger output](https://www.jessesquires.com/blog/2023/03/02/xcode-tip-filter-console/)　·　Jesse Squires

When debugging a large project in Xcode that a large team works on, the console can get quite busy. Logs are everywhere! It can be difficult to sift through the noise, particularly when you have a number of breakpoints configured to log messages, execute debugger commands, and continue after evaluating rather than pause.

You can find a good example of this from [my previous post](https://www.jessesquires.com/blog/2023/02/20/ios-view-controller-loading/), where I showed how to debug view controller loading with symbolic breakpoints. Wouldn’t it be nice if you could hide all the other logs happening in the console to focus solely on debugging? You can! In Xcode’s debug console, you can select the “Debugger Output” option in the menu on the bottom left. When selected, the only thing you will see in the console are the logs and output from your breakpoints and any debugger commands that you execute manually.

![Filtering debugger output in Xcode](https://www.jessesquires.com/img/blog/xcode-debug-filter.jpg)

<sub>Filtering debugger output in Xcode</sub>
