---
title: Automatic Reference Counting
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f0a17dee8c28f205'
translated: false
---

> 原文：[Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/)

[git add](https://belkadan.com/blog/2011/06/git-add/) »

« [Scripting Bridge](https://belkadan.com/blog/2009/07/Scripting-Bridge/?tag=cocoa)

« [Safer Plugin Categories](https://belkadan.com/blog/2009/04/Safer-Plugin-Categories/?tag=objective-c)

[Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c) »

[Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/?tag=llvm) »

[Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/?tag=compilers) »

## [Automatic Reference Counting](#)

In the Cocoa world, the big news from WWDC is the advent of Automatic Reference Counting, or ARC. The only real documentation for the system is an [unlinked reference page](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) on the Clang website, but as Clang is open source and the implementation’s in the latest builds now, that counts as public information.

The Cocoa frameworks have long used a reference-count-based system, but as of Mac OS X v10.5, Apple added optional garbage collection. As with most GC systems, you can mark certain references as `__weak` (which automatically become `nil` when their target is collected), and the actual collection of objects is non-deterministic, meaning you shouldn’t put cleanup code in your `finalize` method. (There’s very little that’s safe to do in a `finalize` method, actually.) But you can pretty much remove all `retain`, `release`, and `autorelease` messages from your code and stop worrying about memory leaks.

The catch? No garbage collection on iOS, presumably because one extra background thread per app and delayed freeing of memory was considered too high a cost on the resource-limited platforms iOS apps run on. What’s negligible on a modern computer becomes noticeable on a mobile device.

We all thought Apple would keep optimizing the garbage collector, or that the iOS hardware would eventually get powerful enough that the performance hit wouldn’t matter. Instead, though, Apple’s come up with ARC, which you can basically think of as inserting `retain`, `release`, and `autorelease` whenever necessary. All the benefits of garbage collection, without the runtime costs. Magic!

Okay, I’ve never had a problem with reference counting, so maybe the question isn’t “why use ARC?” but “what took so long?”. The closest analogue I know of is Boost’s `shared_ptr`, now adopted into C++11. (`shared_ptr` also uses reference counting, via [RAII](https://belkadan.com/blog/2011/06/Sandwich-Code).) But of course, the problem with automatic reference counting is [cycles](http://www.catb.org/jargon/html/koans.html#id3141202): if two objects refer to each other, they’ll never be deallocated.

So, why aren’t cycles a problem with _manual_ reference counting? Well, you just have to distinguish two kinds of references: ones that imply ownership (sub-views, value objects like strings and dates), and ones that don’t (delegates, action targets). This is a mild annoyance, but after a few weeks programming in a framework you usually pick it up pretty quickly.

Now, think about what Apple has done (and NeXT) over the past ten years of Cocoa:

- Simple [ownership rules](http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html), based on a naming convention.
- [Attributes](http://clang-analyzer.llvm.org/annotations.html#cocoa_mem) for when you really need to violate that convention.
- [Static analysis](http://clang-analyzer.llvm.org/xcode.html) to enforce the ownership rules.
- A way to specify the [ownership semantics of accessors](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmAccessorMethods.html#//apple_ref/doc/uid/TP40003539-SW1), along with a way to automatically generate those accessors.
- A convention for [weak references](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmObjectOwnership.html#//apple_ref/doc/uid/20000043-1044135-BCICCFAE), which (until now) has been rather loose.
- [Autorelease](http://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmObjectOwnership.html#//apple_ref/doc/uid/20000043-SW5).

Seen in retrospect, it almost looks as if Apple’s been working towards this all along. We’ve now been trained to follow naming conventions and to annotate our code to declare the semantics we want. We hardly ever get it wrong because the rules are generally clear. And if we want RAII-type semantics for Cocoa types, [we can do that](http://kickingbear.com/blog/archives/13).

```
// See http://kickingbear.com/blog/archives/13 to see how it works
{
    NSObject *myObject KBScopeReleased = [[NSObject alloc] init];
    NSLog( @"%@", myObject );
} // myObject is sent a release message here.
```

But if the rules are clear, then a program with a good understanding of the source code can put in the `retain`s for us.^[1](#fn:automatic)

That’s what ARC is.

And it can do a better job of knowing when to `retain` and `release` than you can. (The existence of functions like [`objc_autoreleaseReturnValue`](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#runtime.objc_autoreleaseReturnValue) implies that it may even be able to optimize the `autorelease` out of relinquishing ownership at the end of a method call.)

I don’t entirely grok ARC yet; I’m not in the iOS Developer Program, so all I have access to is Clang and its [test](http://llvm.org/svn/llvm-project/cfe/trunk/test/ARCMT) [cases](http://llvm.org/svn/llvm-project/cfe/trunk/test/SemaObjC). In particular, converting between managed object pointers and unmanaged C pointers (including CoreFoundation objects) seems to have gotten a lot messier. I hope Apple makes some nice docs available when they release this for real.

But you know what? I tried GC on one of my recent apps, and guess what? It’s nice not to have to worry about `retain` and `release`! So, I’m in favor of ARC, and I’m ready to have it integrated into my Cocoa development.

Interestingly, this leaves Apple with _two_ managed-memory models on the Mac: ARC and GC. GC is still a little more powerful, since you don’t have to worry about retain cycles at all. (`__weak` in GC is only for when you expect an object to go away before you do.) But ARC requires almost zero runtime support, and it’s the only option on iOS besides manual refcounting. My guess is Apple’s going to throw their support behind ARC and let GC languish.

On the flip side, the discussion about Apple’s switch from GCC to LLVM/Clang finally has a piece of solid evidence. AFAIK, GCC does not have an ARC implementation, and I doubt it will get one. Apple now has a compiler chain that’s not only not GPL, but that they essentially control. (A number of the leaders in the LLVM community, including the project founder Chris Lattner, work at Apple. The next biggest contributer is Google.) Which is what everyone’s been suspecting they’ve been after all along.

P.S. [Autorelease pools look funny now](http://clang.llvm.org/docs/AutomaticReferenceCounting.html#autoreleasepool).

```
@autoreleasepool {
    NSString *fileName = [input lastPathComponent];
    NSString *baseName = [fileName stringByDeletingPathExtension];
    NSString *extension = [fileName pathExtension];
    return [NSString stringWithFormat:@"Base: %@\nExtension: %@",
                                      baseName, extension];
}
```

1. If you’re a person who doesn’t like the compiler mucking with things behind your back, think of it this way: almost always, you want to retain your objects while you’re using them and release them when you’re done. So instead of marking ownership with `retain`/`release`, you should only have to annotate the special case of a `__weak` reference. [↩︎](#fnref:automatic)

This entry was posted on [June](https://belkadan.com/blog/2011/06) 20, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Cocoa](https://belkadan.com/blog/tags/cocoa), [Objective-C](https://belkadan.com/blog/tags/objective-c), [LLVM](https://belkadan.com/blog/tags/llvm), [Compilers](https://belkadan.com/blog/tags/compilers)
