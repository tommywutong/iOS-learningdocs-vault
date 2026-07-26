---
title: 让软件支持Retina
source: 杨萧玉
source_key: yulingtianxia
source_url: 'http://yulingtianxia.com/blog/2014/06/19/rang-ruan-jian-zhi-chi-retina/'
original_language: zh
published: 2019-05-26
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:5e2bd03ab6d3bed6'
translated: n/a
---

> 原文：[让软件支持Retina](http://yulingtianxia.com/blog/2014/06/19/rang-ruan-jian-zhi-chi-retina/)　·　杨萧玉

# [让软件支持Retina](http://yulingtianxia.com/blog/2014/06/19/rang-ruan-jian-zhi-chi-retina/)

By [杨萧玉](https://plus.google.com/106642427004837273341?rel=author)

发表于 2014-06-19

**文章目录**

1. 右键单击程序，选择“显示包内容”
2. 找到“info.plist”文件并打开
3. 如果用Xcode打开：添加一个新的键值对，类型为Boolean，Key为“NSHighResolutionCapable”，Value选择“YES”；如果用其他软件打开，直接在plist节点中的dict中添加一个键值对就可以：NSHighResolutionCapable
4. 为了使系统更新，复制一份“软件.app”，改成别的名字如“软件1.app”，删除原来的“软件.app”，再把“软件1.app”重命名为“软件.app”
