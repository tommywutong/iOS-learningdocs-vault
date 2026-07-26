---
title: Xcode plugins memo · sunnyxx的技术博客
source: sunnyxx (孙源)
source_key: sunnyxx
source_url: 'http://blog.sunnyxx.com/2014/03/14/xcode_plugins/'
original_language: zh
published: 2014-03-14
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2b44e151f4d61ed7'
translated: n/a
---

> 原文：[Xcode plugins memo · sunnyxx的技术博客](http://blog.sunnyxx.com/2014/03/14/xcode_plugins/)　·　sunnyxx (孙源)

# Xcode plugins memo

2014年3月14日

## FuzzyAutocomplete

github：[https://github.com/chendo/FuzzyAutocompletePlugin](https://github.com/chendo/FuzzyAutocompletePlugin)  
![FuzzyAutocomplete](https://raw.github.com/chendo/FuzzyAutocompletePlugin/master/demo.gif)

一个支持**模糊匹配**的代码提示优化插件，支持了xcode5.1  
注意：使用的时候有个输入字母字数小于3就输入不了的bug。  
效率必备。

## KSImageNamed

github: [https://github.com/ksuther/KSImageNamed-Xcode](https://github.com/ksuther/KSImageNamed-Xcode)  
![KSImageNamed](https://raw.github.com/ksuther/KSImageNamed-Xcode/master/screenshot.gif)  
输入`imageNamed:`之后快速预览选择图片  
注意：项目中图片文件数量很多的时候，安装这个插件导致xcode运行明显缓慢，不知道现在版本是否已经修改了这个bug  
手写UI的尤其适用，我等sb党用的少点。

## HOStringSense

github: [https://github.com/holtwick/HOStringSense-for-Xcode](https://github.com/holtwick/HOStringSense-for-Xcode)  
![HOStringSense](https://github.com/holtwick/HOStringSense-for-Xcode/raw/master/StringDemoAnimation.gif)  
帮助快速输入字符串，尤其是长段复杂的字符串。
