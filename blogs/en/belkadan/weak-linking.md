---
title: Weak Linking
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/07/Weak-Linking/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca1ade5d229a1faf'
translated: false
---

> 原文：[Weak Linking](https://belkadan.com/blog/2011/07/Weak-Linking/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Using Clang from SVN in Xcode](https://belkadan.com/blog/2011/07/Using-Clang-from-SVN-in-Xcode/)

["Little Big Details"](https://belkadan.com/blog/2011/08/Little-Big-Details/) »

« [Automatic Reference Counting](https://belkadan.com/blog/2011/06/Automatic-Reference-Counting/?tag=compilers)

[“Skip the FFI”](https://belkadan.com/blog/2015/01/Skip-the-FFI/?tag=compilers) »

[Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/?tag=linking) »

## [Weak Linking](#)

When you compile a program that uses external libraries or frameworks, the last step (or a step near the end, at least) is to hook up all of the functions, etc. you use in your program to their implementations in the libraries. This is called “linking”.^[1](#fn:simplified)

A while back, Apple realized that when they added new features to their frameworks (usually with the release of each new OS version), people might want to take advantage of them, but remain backwards-compatible with old OSs. So they added a feature called [weak linking](http://developer.apple.com/library/mac/documentation/MacOSX/Conceptual/BPFrameworks/Concepts/WeakLinking.html#//apple_ref/doc/uid/20002378-106633-CJBGFCAC). Apple wasn’t the first to realize that this might be a problem, and I don’t know if they were the first to come up with weak linking. (Heck, it wasn’t even their first time; apparently there was a similar capability in Mac OS Classic’s Code Fragment Manager.) But that’s where I heard about it first.

Here’s the way you use it (taken from Apple’s guide at the link above):

> If a weakly linked symbol is not available in a framework, the linker sets the address of the symbol to `NULL`. You can check this address in your code using code similar to the following:

```
extern int MyWeakLinkedFunction() __attribute__((weak_import));
int main() {
    int result = 0;
    if (MyWeakLinkedFunction != NULL) {
        result = MyWeakLinkedFunction();
    }
    return result;
}
```

> **Note:** When checking for the existence of a symbol, you must explicitly compare it to `NULL` or `nil` in your code. You cannot use the negation operator ( `!` ) to negate the address of the symbol.

I’m not sure why that last note is in there; I’m pretty sure it would work anyway with a modern GCC or Clang. But I haven’t tested it.

Anyway, pretty cool, right? If you want to take advantage of something that only exists on 10.6 (say, [associated objects](http://developer.apple.com/library/mac/documentation/cocoa/conceptual/ObjectiveC/Chapters/ocAssociativeReferences.html#//apple_ref/doc/uid/TP30001163-CH24-SW1)) you can do that without sacrificing backwards compatibility.

Functions are all well and good, but what about other symbols, though? Webmailer uses the [`NSImageNameStatusAvailable`](http://developer.apple.com/library/mac/documentation/Cocoa/Reference/ApplicationKit/Classes/NSImage_Class/Reference/Reference.html#//apple_ref/doc/c_ref/NSImageNameStatusAvailable) constant to show the standard “online” image from iChat, using it to show which destination is active. I was trying to use it like this:

```
NSImage *activeImage;
// No need to redeclare it as weak-linked: AvailabilityMacros.h takes care of it.
if (NSImageNameStatusAvailable != NULL) {
    activeImage = [[NSImage imageNamed:NSImageNameStatusAvailable] copy];
} else {
    // Fall back to an image in our bundle.
    activeImage = [[NSImage alloc] initWithContentsOfFile:[bundle pathForImageResource:@"active"]];
}
```

And it wasn’t working. Despite my check to see if the image name was `NULL`, it still seemed to be unconditionally loading the image.

See the problem?

Let’s look at the instructions again:

> If a weakly linked symbol is not available in a framework, the linker sets the **address** of the symbol to `NULL`.

OH! Right. You need to be able to tell the difference between a variable whose _value_ is `NULL`, and a variable that doesn’t actually exist at all. For a function pointer, this doesn’t matter: when you say the name of a function like `objc_getAssociatedObject`, the compiler treats it like `&objc_getAssociatedObject`. But that’s not true for `NSImageNameStatusAvailable`, which is just a global constant, a pointer to an NSString.

Here’s what I should have written:

```
if (&NSImageNameStatusAvailable != NULL)
```

And indeed that works. Must be careful in the future!

By the way, Greg Parker has a good article on [weakly-linked _classes_](http://www.sealiesoftware.com/blog/archive/2009/09/09/objc_explain_Weak-import_classes.html), but since this only works back to the first version of the framework that was _compiled_ with weakly-linked classes, you can only use them with Mac OS X v10.7+ or iOS 3.1+. *sigh* Before that, you’ll have to use the old way of `NSClassFromString` to see if a class is available at runtime.

### Postscript: How does it work?

In regular code, you know that it’s not possible for the address of a variable to be `NULL`. Clearly, if the variable exists, it lives somewhere in memory, and that address is _guaranteed_ not to be `0` by the C standard.^[2](#fn:null) But with weakly-linked symbols, _the variable might not exist,_ and so it’s actually quite appropriate that its “address” might be `NULL`.

How does it work? It’s basically like a C++ reference: a weakly-linked symbol `X` actually has a “shadow” symbol with a name like `X$non_lazy_ptr`. Any time you refer to `X`, the compiler replaces it internally with `*X$non_lazy_ptr`.

And how does `X$non_lazy_ptr` get its value? When you load your bundle, there are two secret functions called `dyld_stub_binding_helper` and `__dyld_func_lookup`. My (weak) understanding is that the first one will go through all of your dynamically-linked symbols and use the second one to find the correct addresses to “fill in” the “shadow pointers”.

It’s basically a very small form of self-modifying code, but it makes weak linking possible. Pretty cool, huh?

1. Of course, this is greatly simplified from what a linker really does. If you’re a CS major, you’ve probably learned at least a little about linkers, and if not, well, chances are you won’t be needing to write your own any time soon. If you’re still looking for an explanation, [here’s one](http://thecoffeedesk.com/news/index.php/2009/06/01/how-linker-works/) that I found on the first page of Google results for “what is a linker”. [↩︎](#fnref:simplified)
2. Well, actually, that might not be true. What’s guaranteed is that if you cast the integer `0` to a pointer value, you get the null pointer, and that the null pointer does not point to any valid object, and that the null pointer has a conditional value of `false`. But I don’t think it says that the _representation_ of a null pointer has to be `0`, which means that doing a C++ `reinterpret_cast` on a `0` could conceivably give you a valid pointer. I think.

  In practice, pretty much everyone uses `0` as the representation of null pointers. [↩︎](#fnref:null)

This entry was posted on [July](https://belkadan.com/blog/2011/07) 29, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Compilers](https://belkadan.com/blog/tags/compilers), [Linking](https://belkadan.com/blog/tags/linking)
