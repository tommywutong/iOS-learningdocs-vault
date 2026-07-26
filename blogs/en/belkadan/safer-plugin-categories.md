---
title: Safer Plugin Categories
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a5add5adab941d24'
translated: false
---

> 原文：[Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Hacking Safari 4...for Great Convenience](https://belkadan.com/blog/2009/04/Hacking-Safari-4-for-Great-Convenience/)

[[Meme] How Many HTML Elements Can You Name in 5 Minutes?](https://belkadan.com/blog/2009/04/Meme--How-Many-HTML-Elements-Can-You-Name/) »

« [Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=objective-c)

[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=objective-c) »

« [Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=cocoa)

[Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/?tag=cocoa) »

## [Safer Plugin Categories](#)

Why did I miss last week’s post? To test this!

A few posts back I [suggested](http://belkadan.com/blog/2009/03/Categories-and-load/) the use of a category’s `+load` method as a way to safely swizzle methods in a plugin. What do you do, though, if the _same_ category is going to be loaded twice?

The established behavior of categories, of course is that the last one loaded “wins”.

The behavior of _classes_, however, is that the _first_ one loaded wins.

That is, if a bundle defines a class with the same name as an existing class, it is not loaded. `[bundle principalClass]` returns the existing class (if the principal class is the conflicted one) and `[bundle classNamed:@"MyClass"]` simply returns `nil`.

That’s good news for plugin writers who might want to use some common Cocoa-enhancing class, like [RBSplitView](http://www.brockerhoff.net/src/rbs.html). But how does this figure into categories?

For that, you have to remember what a category does. It adds methods to a class, replacing any that are already there. The new Leopard runtime API, however, makes it very easy to imitate this behavior dynamically:

```
Method _m = class_getInstanceMethod(FROM_CLASS, @selector(SEL));
class_addMethod(TO_CLASS, @selector(SEL), method_getImplementation(_m), method_getTypeEncoding(_m));
```

The general idea is to put the methods in a custom holding class for the time being, then copy them into the target class when then plugin is loaded. (In the Safari completion project, this code is in a macro, hence the placeholders and awkward names.) It’s easy enough to test (using, say, `+instancesRespondToSelector:`) if another plugin has already done this, and not overwrite existing methods.

Couple this with the usual plugin name-mangling-then-swizzle strategy to wrap an existing method with new behavior, and I’m pretty sure we’ve got a safe way to use category behavior in plugins.

Thoughts?

This entry was posted on [April](https://belkadan.com/blog/2009/04) 16, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Objective-C](https://belkadan.com/blog/tags/objective-c), [Cocoa](https://belkadan.com/blog/tags/cocoa)
