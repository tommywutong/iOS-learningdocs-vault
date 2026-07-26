---
title: 'Type punning isn''t funny: Using pointers to recast in C is bad. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/04/using-pointers-to-recast-in-c-is-bad.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:c1e4fb1b20dfa4bc'
translated: false
---

> 原文：[Type punning isn't funny: Using pointers to recast in C is bad. | Cocoa with Love](https://www.cocoawithlove.com/2008/04/using-pointers-to-recast-in-c-is-bad.html)　·　Cocoa with Love (Matt Gallagher)

A very common C technique for reinterpreting data types has the potential to cause nasty bugs. Apple knows this, which is why the implementation of NSRectToCGRect (correctly) doesn't do what the documention claims. I show you a technique to perform reinterpret casts safely in your own code.

Apple's [documentation for the function NSRectToCGRect](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Functions/index.html) claim that it is implemented as follows:

```objc
CGRect NSRectToCGRect(NSRect nsrect) {
   return (*(CGRect *)&(nsrect));
}
```

If you have seen a lot of C code, chances are that you've seen this approach before. You can't cast one struct to another to reinterpret — even if they have the same fields — so it is common to see reinterpreting by making a pointer and casting the pointer.

The implication is that NSRectToCGRect reinterprets an NSRect as a CGRect without altering the contained data.

While the implied functionality is accurate, the displayed implementation is not. In actuality, the function looks like this:

```objc
NS_INLINE CGRect NSRectToCGRect(NSRect nsrect) {
    union _ {NSRect ns; CGRect cg;};
    return ((union _ *)&nsrect)->cg;
}
```

Why the difference? Why bother creating a union? Why shouldn't you simply cast through a pointer?

## Type punning

As common as casting through a pointer is, it is actually bad practice and potentially risky code. Casting through a pointer has the potential to create bugs because of type punning.

> A form of
> 
> pointer aliasing
> 
> where two pointers and refer to the same location in memory but represent that location as different types. The compiler will treat both "puns" as unrelated pointers. Type punning has the potential to cause dependency problems for any data accessed through both pointers.

Most of the time, type punning won't cause any problems. It is considered undefined behavior by the C standard but will usually do the work you expect.

That is unless you're trying to squeeze more performance out of your code through optimizations. Specifically, if you ever turn on "_Enforce Strict Aliasing_" in XCode (a.k.a -fstrict_aliasing in GCC) you run the risk of unpredictable and errant behavior. With strict aliasing, the compiler may start doing things in the wrong order or leaving instructions out entirely.

To be clear, these bugs can only occur if you _dereference_ both pointers (or otherwise access their shared data) within a single scope or function. Just creating a pointer should be safe.

## An example of a punning bug

Before the NSRectToCGRect function existed, I had some code which did the following:

```objc
NSRect ellipseBounds;
ellipseBounds.origin.x = 0;
ellipseBounds.origin.y = 0;
ellipseBounds.size.width = WIDGET_SIZE - 1.0;
ellipseBounds.size.height = WIDGET_SIZE - 1.0;
ellipseBounds = NSInsetRect(ellipseBounds, 4, 4);

CGContextAddEllipseInRect(context, *(CGRect *)&ellipseBounds);
CGContextFillPath(context);
```

This code creates and sets up an NSRect and then reinterprets it as a CGRect before using it.

In this case, with -fstrict_aliasing enabled, GCC chose to order the NSInsetRect _after_ the call to  CGContextAddEllipseInRect because the dependency between the two was broken by type punning when the pointer to ellipseBounds was dereferenced as a different type.

## Union solves the problem

The traditional solution to this problem, to allow the code to be correct with -fstrict_aliasing enabled, is to use a union. As shown in the NSRectToCGRect code, the union should contain the source and destination types and you simply set or cast to the source type before reading from the destination type.

According to the C standard, anything involving type punning is implementation specific. So in a "standard" sense, using a union doesn't necessarily solve the problem. According to the standard, if you set data in a union on one field, you are required to read back from the same field.

Fortunately, GCC explicitly gives permission to do different. From the GCC documentation:

Excellent.

## A macro to reinterpret your own data safely

Really simple:

```objc
#define UNION_CAST(x, destType) \
   (((union {__typeof__(x) a; destType b;})x).b)
```

So you could cast a float variable named myFloat to an int as follows:

```objc
int myInt = UNION_CAST(myFloat, int);
```

You might notice that I don't bother with an inline function, I don't give the union a name, and I don't make a pointer to the value before casting. The Apple NSRectToCGRect function did these things but they are unnecessary. Although, since the compiler should optimize away the extra work, the function, the extra pointer and the dereference in Apple's code shouldn't matter.

## Conclusion

Creating a pointer to a value and recasting the pointer to a new type is the most common way to reinterpret data in C that I've seen. Despite its prevalence, you shouldn't do it. Always do your reinterpret casts through a union. It could save you a lot of trouble if you're ever trying to squeeze performance through compiler options.
