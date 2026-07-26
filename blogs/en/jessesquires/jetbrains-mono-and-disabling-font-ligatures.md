---
title: JetBrains Mono and disabling font ligatures
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/02/25/jetbrains-mono-and-disabling-font-ligatures/'
original_language: en
published: 2020-02-25
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0ffce2a2c2b2c130'
translated: false
---

> 原文：[JetBrains Mono and disabling font ligatures](https://www.jessesquires.com/blog/2020/02/25/jetbrains-mono-and-disabling-font-ligatures/)　·　Jesse Squires

JetBrains recently released [a new typeface for developers](https://www.jetbrains.com/lp/mono/) and I wanted to give it a try. I switched to JetBrains Mono in my two primary editors, Xcode and [Sublime Text](https://www.sublimetext.com). Much to my surprise, I really enjoyed it. I think it is a great typeface. But I quickly discovered that I hate ligatures.

There was no way (that I could find) to select JetBrains Mono in Xcode and disable ligatures. If anyone knows how to do that, please let me know. For now, I will stick with SF Mono in Xcode.

In Sublime Text, you can add the following options to your preferences file to disable ligatures.

```
"font_face": "JetBrains Mono",
"font_options": ["no_liga", "no_clig", "no_calt"],
```

And now your eyes can rest. If you prefer ligatures, don’t @ me.

##### [Update](#updated-26-february-2020)  _26 February 2020_

There is [an open issue](https://github.com/JetBrains/JetBrainsMono/issues/19) on GitHub discussing providing a version without ligatures.

##### [Update](#updated-23-march-2020)  _23 March 2020_

Good news! JetBrains has [released a no ligature version (1.0.4)](https://github.com/JetBrains/JetBrainsMono/releases/tag/v1.0.4). It is called _JetBrains Mono NL_.
