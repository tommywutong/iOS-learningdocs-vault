---
title: 关于 NSURL 的解析和编码
source: onevcat (王巍/喵神)
source_key: onevcat
source_url: 'https://onevcat.com/2011/11/nsurl/'
original_language: zh
published: 2011-11-30
status: active
license: CC BY 4.0（页脚明示）→ 可公开，须署名并保留原文链接
archived_at: 2026-07-27
content_hash: 'sha256:bad3e0e16f30e6e1'
translated: n/a
---

> 原文：[关于 NSURL 的解析和编码](https://onevcat.com/2011/11/nsurl/)　·　onevcat (王巍/喵神)

NSURL毫无疑问是常用类，有时候我们需要对一个url进行分析整理，当然是可以按照RFC 1808的定义去自己分析，但是万能的Apple大大已经在SDK里扔了不少方法来帮助解析一个url了…方便又快捷呐～比如下面的输入：

```objc
NSURL *url = [NSURL URLWithString:
 @"http://www.onevcat.com/2011/11/debug/;param?p=307#more-307"];
NSLog(@“Scheme: %@”, [url scheme]);
NSLog(@“Host: %@”, [url host]);
NSLog(@“Port: %@”, [url port]);
NSLog(@“Path: %@”, [url path]);
NSLog(@“Relative path: %@”, [url relativePath]);
NSLog(@“Path components as array: %@”, [url pathComponents]);
NSLog(@“Parameter string: %@”, [url parameterString]);
NSLog(@“Query: %@”, [url query]);
NSLog(@“Fragment: %@”, [url fragment]);
```

将得到以下输出：

![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7 )

没什么值得多说的～相当方便就能得到所要结果的方法～ 另外，在由`NSString`生成`NSURL`对象时，有可能会出现`NSString`中包含百分号各类括号冒号等对于url来说的非法字符如果直接进行转换的话将得到nil。在对于复杂url进行转换前，可以先试试对待转换的NSString发送 `stringByAddingPercentEscapesUsingEncoding:` 将其转换为合法的url字符串（其实目的就是保证非法字符用UTF8编码..） 比如这样：

```objc
NSString *fixedStr = [reqStr stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
```
