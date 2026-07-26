---
title: Objective-J and Objective-C
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fe25d93028c7fc8d'
translated: false
---

> 原文：[Objective-J and Objective-C](https://belkadan.com/blog/2008/09/Objective-J-and-Objective-C/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [HTTPS and Name-based Virtual Hosting](https://belkadan.com/blog/2008/08/HTTPS-and-Name-based-Virtual-Hosting/)

[JavaScript Tetris](https://belkadan.com/blog/2009/03/JavaScript-Tetris/) »

[Const Correctness](https://belkadan.com/blog/2009/03/Const-Correctness/?tag=programming-languages) »

[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/?tag=objective-c) »

## [Objective-J and Objective-C](#)

Just a little over a week ago, Chris Lattner [announced to the Clang mailing list](http://lists.cs.uiuc.edu/pipermail/cfe-dev/2008-August/002670.html) that Apple was adding something called “blocks” to C. These blocks are basically closures in the same sense that any computer science student would use them in Lisp, except with a few extra twists of memory management thrown in. (Specifically, if you want to mutate variables declared outside the block, you have to use a new storage qualifier, `__block`.)

Today, the anticipated “Objective-J” framework used to build the impressive [280 Slides web application](http://280slides.com/) was [released](http://cappuccino.org/discuss/2008/09/04/announcing-cappuccino/), along with a Cocoa-inspired (almost Cocoa-cloned) framework known as Cappuccino. In some cases it seems almost _too_ close, with methods like `-[CPWindowController initWithWindowCibName:]`, where “cib”, of course, stands for Cappuccino Interface Builder. (I’m not sure this exists yet; I can’t find any mention of it on the site.) But given that GNUStep is still around and OpenStep, I think, is still open, I suppose there’s not technically any copyright infringement going on. I’d like to play with Cappuccino too but I have enough on my plate right now.

Anyway, so I think blocks are cool, and would like to start using them except I try to maintain backwards compatibility. (Think about alert sheet callbacks, though!) Objective-J is _pretty_ cool but I want to see some performance specs (though I’m sure it’s faster than an overly-AJAXed site).

What I find interesting, though, is this snippet from the [Objective-J Tutorial](http://cappuccino.org/learn/tutorials/objective-j-tutorial.php)’s Methods section:

> You may be wondering why it matters what the actual name of the method is. One pattern you’ll find in Objective-J and Cappuccino going forward is the idea of passing a method as an argument to another method. This is used commonly in delegation and in the event system. Since methods aren’t first class objects in the same way as JavaScript, we use a special notation to refer to them, `@selector`. If I wanted to pass the previous method as an argument to another method, I would use the following code:
> 
> ```
> [fooObject setCallbackSelector: @selector(setJobTitle:company:)];
> ```
> 
> As you can see, the method name is passed to `@selector` complete with its colons and parameter labels.

At the same time, Objective-C, and indeed pure C as well, gets the use of blocks:

```
// something like this
[fooObject setCallback:^(NSString *title, NSString *company) {
    // do stuff
}];
```

…and while this is no good for bindings, and maybe even not target-action replacement, it’s great for callbacks.

Ironic that the two languages seem to pass each other in the mist. Personally, I’ve been finally won over to Blocks since they don’t seem to mess up C at all (unlike some other closure syntaxes I’ve seen which only work in a high-level environment). Whereas although using JavaScript functions as first class entities isn’t always needed, it seems like it wouldn’t be hard to implement. Maybe it was just a problem of copying the syntax a little too closely. *grin*

This entry was posted on [September](https://belkadan.com/blog/2008/09) 04, [2008](https://belkadan.com/blog/2008) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages), [Objective-C](https://belkadan.com/blog/tags/objective-c)
