---
title: nil / Nil / NULL / NSNull
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/nil/'
original_language: en
published: 2013-01-07
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:d1e77eb5ee0e6602'
translated: false
---

> 原文：[nil / Nil / NULL / NSNull](https://nshipster.com/nil/)　·　NSHipster (Mattt)

# [nil / Nil / NULL / NSNull](https://nshipster.com/nil/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  January 7^th, 2013

Understanding the concept of nothingness is as much a philosophical issue as it is a pragmatic one. We are inhabitants of a universe of _somethings_, yet reason in a logical universe of ontological uncertainties. As a physical manifestation of a logical system, computers are faced with the intractable problem of how to represent _nothing_ with _something_.

In Objective-C, there are a few different varieties of nothing: `NULL`, `nil`, `Nil`, and `NSNull`.

| Symbol | Value | Meaning |
|---|---|---|
| `NULL` | `(void *)0` | literal null value for C pointers |
| `nil` | `(id)0` | literal null value for Objective-C objects |
| `Nil` | `(Class)0` | literal null value for Objective-C classes |
| `NSNull` | `[NSNull null]` | singleton object used to represent null |

## NULL

C represents _nothing_ as `0` for primitive values and `NULL` for pointers _([which is equivalent to `0` in a pointer context](http://c-faq.com/null/nullor0.html))_.

The only time you see `NULL` in Objective-C code is when interacting with low-level C APIs like Core Foundation or Core Graphics.

## nil

Objective-C builds on C’s representation of _nothing_ by adding `nil`. `nil` is an _object_ pointer to nothing. Although semantically distinct from `NULL`, they are technically equivalent.

Perhaps the most notable behavior of `nil`, however, is that it can have messages sent to it without a problem. In other languages, like Java, this kind of behavior would crash your program. But in Objective-C, invoking a method on `nil` returns a zero value — which is to say, _“`nil` begets `nil`“_. This fact alone significantly simplifies things for Objective-C developers, as it obviates the need to check for `nil` before doing anything:

```
// For example, this expression...
if (name != nil && [name isEqualToString:@"Steve"]) { ... }

// ...can be simplified to:
if ([name isEqualToString:@"Steve"]) { ... }
```

With vigilance, this quirk of Objective-C can be a convenient feature rather than a lurking source of bugs in your application.

## Nil

In addition to `nil`, [the Objective-C runtime defines `Nil`](https://gist.github.com/4469665) as a _class_ pointer to nothing. This lesser-known title-case cousin of `nil` doesn’t show up much very often, but it’s at least worth noting.

## NSNull

On the framework level, Foundation defines `NSNull`. `NSNull` defines a class method (`+null`) that returns the singleton `NSNull` object. `NSNull` represents nothing with an actual object rather than a zero value like `nil` or `NULL`.

`NSNull` is used throughout Foundation and other frameworks to skirt around the limitations of collections like `NSArray` and `NSDictionary` not being able to contain `nil` values. You can think of `NSNull` as effectively [boxing](https://en.wikipedia.org/wiki/Object_type_(object-oriented_programming)#Boxing) the `NULL` or `nil` value so that it can be used in collections:

```
NSMutableDictionary *mutableDictionary = [NSMutableDictionary dictionary];
mutableDictionary[@"someKey"] = [NSNull null];
NSLog(@"%@", [mutableDictionary allKeys]);
// @[@"someKey"]
```

---

Why does Objective-C have four values for nothing when one might suffice? It all goes back to [a common refrain](https://nshipster.com/ns_enum-ns_options/), about how Objective-C bridges the procedural paradigm of C with Smalltalk-inspired object-oriented paradigm.

In the procedural world of C, values are indistinguishable from their numeric value. The same zero value might represent the first index of an array, the terminating byte of a string, or the simply result of “2 - 2”. Objective-C constructs an object-oriented layer on top of these primitives, and in so doing establishes a distinct logical universe. This abstraction allows for a sentinel value, the `NSNull` singleton, to be defined independently of numbers. `nil` (and `Nil`) therefore serve as intermediaries between these worlds at their convergence point: zero.
