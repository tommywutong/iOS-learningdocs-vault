---
title: NSValue and Boxed Expressions - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/nsvalue-and-boxed-expressions/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:65c9c66f72d821aa'
translated: false
---

> 原文：[NSValue and Boxed Expressions - Low Level Bits 🇺🇦](https://lowlevelbits.org/nsvalue-and-boxed-expressions/)　·　Low Level Bits (Alex Denisov)

# NSValue and Boxed Expressions

_Published on Jun 26, 2015_

Few hours ago I finally finished with my patch to Clang. It took a lot of time, but for me it is the most interesting and challenging OSS contribution so far.

I’m not going to dive deep into the details, but will give an overview of the new feature it brings to Objective-C.

For those of you who want to see the code and documentation: [code](https://github.com/llvm-mirror/clang/commit/3849076ca69f4277bfac55479c2fc0929f5bbd9d) [docs](http://clang.llvm.org/docs/ObjectiveCLiterals.html#boxed-c-structures)

### Boxed Expressions and Structures

Boxed expressions got limited support of NSValue:

```objective
NSValue *center = @(view.center);    // Point p = view.center;
                                     // [NSValue valueWithBytes:&p objCType:@encode(Point)];
NSValue *frame = @(view.frame);      // Rect r = view.frame;
                                     // [NSValue valueWithBytes:&r objCType:@encode(Rect)];
```

To use boxed expressions on a C struct or union you’ve defined, mark it as `objc_boxable` first:

```objective
struct __attribute__((objc_boxable)) Point {
    int x, y;
};

typedef struct __attribute__((objc_boxable)) _Size {
    int width, height;
} Size;
```

For C structs or unions defined in a different part of your code (legacy, third-party), simply ‘enable’ this feature before using it:

```objective
typedef struct _Rect {
	Point origin;
  Size size;
} Rect;

Rect r;
NSValue *bad_rect = @(r);       // error

typedef struct __attribute__((objc_boxable)) _Rect Rect;

NSValue *good_rect = @(r);      // ok
```

### Availability

To write backward compatible code you need to check for attribute and feature availability:

```objective
#if __has_attribute(objc_boxable)
    typedef struct __attribute__((objc_boxable)) _Rect Rect;
#endif

CABasicAnimation animation = [CABasicAnimation animationWithKeyPath:@"position"];
#if __has_feature(objc_boxed_nsvalue_expressions)
    animation.fromValue = @(layer.position);
    animation.toValue = @(newPosition);
#else
    animation.fromValue = [NSValue valueWithCGPoint:layer.position];
    animation.toValue = [NSValue valueWithCGPoint:newPosition];
#endif
[layer addAnimation:animation forKey:@"move"];
```

### Boring Numbers

- 222 days since first version of patch
- 85 commits in an own fork of clang
- 50 emails in the mail thread
- 8 versions of the patch
- 3 different implementations
- 1 retired reviewer

### That’s it

It took about 7 months to deliver this feature. While I didn’t work on it every week, it was quite the effort. Nonetheless, the result was worth it. So next time you feel like there is no end in sight with a patch you’re trying to get merged, don’t despair - that sweet LGTM will come!
