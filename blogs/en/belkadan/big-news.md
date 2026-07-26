---
title: Big News
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2012/05/Big-News/'
original_language: en
published: 2012-05-16
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8892bfc5e097dbcf'
translated: false
---

> 原文：[Big News](https://belkadan.com/blog/2012/05/Big-News/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

[Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/) »

« [Auspicious Continuation](https://belkadan.com/blog/2011/05/Auspicious-Continuation/?tag=meta)

[Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=meta) »

« [Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/?tag=llvm)

[How to Write a Checker in 24 Hours](https://belkadan.com/blog/2012/12/How-to-Write-a-Checker/?tag=llvm) »

« [Priorities](https://belkadan.com/blog/2011/07/Priorities/?tag=apple)

[Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=apple) »

## [Big News](#)

I’m going to Apple.

This is not as exciting for me as it would be for someone else. I actually grew up in Cupertino, and I’ve interned there a few summers ago. I have a lot of respect for Apple’s emphasis on design and quality in their products (there are always exceptions, but the general trend is very good), but I haven’t been _dying_ to work there the way some people might.

What _is_ exciting is what I’ll be doing. As I mentioned a few weeks back, I’ve shifted away from Cocoa development and gotten involved with [Clang](http://clang.llvm.org/). I’m happy to say that the group I’ll be joining at Apple is one of the Clang teams, which is primarily responsible for the [static analyzer](http://clang-analyzer.llvm.org/), among other things.

_Edit from the future: I now work on [Swift](https://developer.apple.com/swift)._

What does Clang do for you? If you develop for Mac or iOS, it’s probably your compiler these days. The Objective-C language group just brought you [_collection literals,_ _numeric literals,_ and _boxed expressions_](http://clang.llvm.org/docs/ObjectiveCLiterals.html), something that’s been wanted for a while. (I wouldn’t be surprised if NSValue wrappers came soon as well.)

```
NSViewAnimation *anim = [[NSViewAnimation alloc] initWithViewAnimations:@[
    @{
        NSViewAnimationTargetKey: updateBar,
        NSViewAnimationEndFrameKey: [NSValue valueWithRect:updateFrame]
    },
    @{
        NSViewAnimationTargetKey: mainView,
        NSViewAnimationEndFrameKey: [NSValue valueWithRect:mainFrame]
    }
]];
```

On the static analysis side of things, Clang has long detected memory leaks in your code, even if you’re using [ARC](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/). (This only really happens when you cross the Cocoa/CoreFoundation interface, though.)

```
NSImage *icon;
if ([self shouldUseApplicationIcon]) {
    icon = [[NSImage imageNamed:NSApplicationIconName] copy];
    [icon setSize:NSMakeSize(16, 16)];
} else {
    icon = [NSImage imageNamed:kWarningIconName];
}
return icon;
```

> _**warning**: Potential leak of an object stored into ‘`icon`‘_

But we’re pushing it further. Did you know the analyzer can check for returning stack-based memory?

```
dispatch_block_t getPrintBlock (const char *msg) {
    return ^{
        printf("%s", msg);
    };
}
```

> _**error**: returning block that lives on the local stack_

And even if you aren’t interested in statically finding path-sensitive bugs in your program, Clang can _still_ help you simply with its quality error messages.

```
size_t getLength (std::string *s) {
    return s.length();
}
```

> _**error**: member reference type ‘`string *`’ (aka ‘`basic_string<char> *`’) is a pointer; maybe you meant to use ‘`->`‘?_

What’s that, you don’t use a C-based language? While _I_ might not be helping you, there are a [number](http://dragonegg.llvm.org/) [of](http://www.haskell.org/ghc/) [other](http://emscripten.org/) [projects](http://www.rubymotion.com/) that use the same [LLVM](http://llvm.org/) backend as Clang. I won’t be directly working on that, but it’s shared infrastructure.

(What’s that, you’re not a programmer? Sorry to have wasted your time, then.)

---

**DOWNSIDE**: Webmailer and Keystone probably aren’t going to be able to continue. Despite being open-source, they may still present a conflict of interest with working at Apple. (Keystone in particular is kind of “sticky” given how it injects itself into Safari.) Consequently, I’m working to resolve the few outstanding feature requests now and upload the latest version of the source to both apps on Github, but there will most likely be no Mountain Lion update from Belkadan Software.

In addition, _this blog_ is probably a bit sensitive, and while I’d like to continue posting about interesting bits of programming and things Clang is (publicly) supporting, I’m not sure if I’ll be able to do that either. We’ll see.

However, you can also continue to see me on the Clang mailing lists, and hopefully I’ll be working on something that simply makes life easier for programmers. There are a lot of ways we can make the experience of software development better, easier, and _smoother._ _That’s_ what I’m doing.

I’m going to Clang, and it’s going to be great.

This entry was posted on [May](https://belkadan.com/blog/2012/05) 16, [2012](https://belkadan.com/blog/2012) and is filed under [Personal](https://belkadan.com/blog/personal). Tags: [Meta](https://belkadan.com/blog/tags/meta), [LLVM](https://belkadan.com/blog/tags/llvm), [Apple](https://belkadan.com/blog/tags/apple)
