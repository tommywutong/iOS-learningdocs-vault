---
title: 'Performance Optimization: Why We Can''t Use valueForKeyPath:'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:eb05736a08bf8335'
translated: false
---

> 原文：[Performance Optimization: Why We Can't Use valueForKeyPath:](https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Short Xcode Tip: Plugins](https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/)

[GenericToolbar and IB3](https://belkadan.com/blog/2007/12/GenericToolbar-and-IB3/) »

[NSNumber, CFNumber, and CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/?tag=cocoa) »

## [Performance Optimization: Why We Can't Use valueForKeyPath:](#)

Recently I was coding away and found myself needing to access something three levels down in a dictionary. I immediately cringed at the thought of the following:

```
[[[info objectForKey:@"tile-data"] objectForKey:@"file-data"] objectForKey:@"_CFURLStringType"];
```

Why? Because it’s ugly. I mean, the code to get an object out of a dictionary completely buries which object I’m getting. It would be much nicer just to do this:

```
[info valueForKeyPath:@"tile-data.file-data._CFURLStringType"]
```

But I was wary enough to run some speed tests, using the harness written by Mike Ash for [_his_ performance tests](http://mikeash.com/blog/pivot/entry.php?id=29). The results:

| Name | Iterations | Total time (sec) | Time per (ns) |
|---|---|---|---|
| objectForKey x3 | 10000000 | 5.0 | 497.1 |
| valueForKey x3 | 10000000 | 5.6 | 561.9 |
| valueForKeyPath | 10000000 | 71.9 | 7186.2 |

Looks like `valueForKeyPath:` is over _ten times_ slower than the repeated `objectForKey:`. That kind of difference is pretty significant, even if you have to run the code 10 million times to see it. (For the curious, the `objectForKey:` and `valueForKey:` calls are on the same order as creating and releasing an NSAutoreleasePool; the `valueForKeyPath:` call a bit slower than creating an NSButtonCell. So it’s not _that_ slow either way.)

This is pretty damning evidence. Looks like the prettier syntax is going to be sacrificed before I make it a habit.

_Note: I did not make any special effort to remove all other factors in this test, such as length of the individual keys, number of keys in the path, or even what else was running on my computer at the time. (That last, I know, is quite serious, although I did avoid being active.) I simply tested the same dictionary (loaded once for each test, not included in the timing) with the key path given above. If the performance results were closer, I might have done a more precise test, but they weren’t, so I won’t._

This entry was posted on [October](https://belkadan.com/blog/2007/10) 27, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa)
