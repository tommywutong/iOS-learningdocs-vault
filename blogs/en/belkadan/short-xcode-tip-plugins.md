---
title: 'Short Xcode Tip: Plugins'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e37fcff708c38642'
translated: false
---

> 原文：[Short Xcode Tip: Plugins](https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Port 25 Blocked?](https://belkadan.com/blog/2007/07/Port-25-Blocked/)

[Performance Optimization: Why We Can't Use valueForKeyPath:](https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/) »

[Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/?tag=xcode) »

## [Short Xcode Tip: Plugins](#)

When writing GenericToolbar 1.0 there were plenty of times I wanted to print something to the run log using `NSLog`, or even just observe the error messages IB prints. So I’d go call up the old Console utility and watch as my autorefreshing webmail window prints line after line, while IB is completely silent and error-less. Or did I just miss it with all the Safari AJAX calls?

It wasn’t too bad, but it’s not a very pleasant way to debug a plugin. And as for true debugging and breakpoints, forget it.

By the time I was starting work on GenericToolbar 1.1, I had definitely realized that this was an awkward way to develop, and didn’t want to use it again. So what’s the answer?

_Custom executables._

That’s right. Thanks to Xcode’s Custom Executables function, you can start Interface Builder (or TextEdit, or even another Xcode) inside the run environment! Run logs work just like your own executables, and breakpoints _usually_ function quite well. (I say “usually” because a few times they seem not to, but that could be the nature of what I was trying to do at the time.) So next time you’re debugging a plugin, just create a custom executable for the target application and you’re good to go.

Side note: there are a few caveats with this method, notably that some applications don’t lke to have multiple instances running. Interface Builder will actually freeze (which then freezes the Xcode you’re running it in) if a normal IB is already open. And as for menu extras like Dockyard, I’m not sure how you’d get your own SystemUIServer (the app that runs menu extras, among other things) into place when there’s already one running since you logged in. Maybe a quick kill/launch would do it, but I haven’t tried messing with that so far.

I’ve got another plugin “ready” besides GenericToolbar, called PHP/CC. It adds PHP code completion and source scanning to Xcode using Xcode’s own (undocumented) plugin system and private frameworks. I’m not releasing it publicly until I’ve used it myself for a month or so and convinced myself that there are no serious bugs.

This entry was posted on [September](https://belkadan.com/blog/2007/09) 01, [2007](https://belkadan.com/blog/2007) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Xcode](https://belkadan.com/blog/tags/xcode)
