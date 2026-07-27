---
title: '用Pike''s VM實現的非回溯正則表達式引擎'
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2012-11-05-regex-engine'
original_language: en
published: 2012-11-05
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fceb3e472f7b3c30'
translated: false
---

> 原文：[用Pike's VM實現的非回溯正則表達式引擎](https://maskray.me/blog/2012-11-05-regex-engine)　·　MaskRay (宋方睿)

[2012-11-05](https://maskray.me/blog/2012-11-05-regex-engine)

# 用Pike's VM實現的非回溯正則表達式引擎

Parser之外的部分參考http://swtch.com/~rsc/regexp/regexp2.html ，代碼都模仿自http://code.google.com/p/re1/source/browse 。注意到正則表達式是operator-precedence grammar，可以用一個擴展的Shunting-Yard算法來解析，其中用了一些特殊構造處理後綴操作符和括號。

## 實現

[github上](https://github.com/MaskRay/Regex)

## 推薦閱讀

[Parsing Expressions by Recursive Descent](http://www.engr.mun.ca/~theo/Misc/exp_parsing.htm)
