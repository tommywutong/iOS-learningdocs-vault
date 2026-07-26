---
title: BOOL / bool / Boolean / NSCFBoolean
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/bool/'
original_language: en
published: 2013-04-08
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:60c298a344a11100'
translated: false
---

> 原文：[BOOL / bool / Boolean / NSCFBoolean](https://nshipster.com/bool/)　·　NSHipster (Mattt)

# [BOOL / bool / Boolean / NSCFBoolean](https://nshipster.com/bool/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  April 8^th, 2013

Truth. _Vēritās_. The entire charter of Philosophy is founded upon the pursuit of it, and yet its exact meaning and implications still elude us. Does truth exist independently or is it defined contingently against falsity? Can a proposition be at once both true _and_ false? Is there absolute truth in anything, or is everything relative?

Encoding our logical universe into the cold, calculating bytecode of computers forces us to deal with these questions one way or another. And, as we’ll soon discuss, truth is indeed stranger than fiction.

We’ve talked before about the [philosophical and technical concerns of nothingness in programming](https://nshipster.com/nil/). This week, our attention turns to another fundamental matter: _Boolean types in Objective-C_.

---

In `C`, statements like `if` and `while` evaluate a conditional expression to determine which code to execute next. A value of `0` is considered “false” while any other value is considered “true”.

Objective-C defines the `BOOL` type to encode truth values. Altogether, `BOOL` comprises a type definition (`typedef signed char BOOL`) and the macros `YES` and `NO`, which represent true and false, respectively. By convention, we use the `BOOL` type for Boolean parameters, properties, and instance variables and use `YES` and `NO` when representing literal Boolean values.

## The Wrong Answer to the Wrong Question

Novice programmers often include an equality operator in conditional expressions:

```
if ([a isEqual:b] == YES) {
  ...
}
```

Not only is this unnecessary, but depending on the left-hand value can cause unexpected results, as demonstrated by Mark Dalrymple in [this blog post](https://www.bignerdranch.com/blog/bools-sharp-corners/) with the following example:

```
static BOOL different (int a, int b) {
    return a - b;
}
```

A clever programmer might take some satisfaction in this approach. Indeed, two integers are equal if and only if their difference is `0`. However, because `BOOL` is `typedef`‘d as a `signed char`, this implementation doesn’t behave as expected:

```
if (different(11, 10) == YES) {
  printf ("11 != 10\n");
} else {
  printf ("11 == 10\n");
}
// Prints "11 != 10"

if (different(10, 11) == YES) {
  printf ("10 != 11\n");
} else {
  printf ("10 == 11\n");
}
// Prints "10 == 11"

if (different(512, 256) == YES) {
  printf ("512 != 256\n");
} else {
  printf ("512 == 256\n");
}
// Prints "512 == 256"
```

[This might be acceptable for JavaScript](https://www.destroyallsoftware.com/talks/wat), but Objective-C doesn’t suffer fools gladly.

Deriving truth value directly from an arithmetic operation is never a good idea. Like the sentence [“Colorless green ideas sleep furiously”](https://en.wikipedia.org/wiki/Colorless_green_ideas_sleep_furiously), it may be grammatical but it doesn’t make any sense. Instead, use the result of the `==` operator or cast values into booleans with the `!` (or `!!`) operator.

## The Truth About `NSNumber` and `BOOL`

**Pop Quiz**: What is the output of the following expression?

```
NSLog(@"%@", [@(YES) class]);
```

**Answer**: `__NSCFBoolean`

_Wait, what?_

All this time, we’ve been led to believe that `NSNumber` [boxes](https://nshipster.com/nsvalue/) primitives into an object representation. Any other integer- or floating-point-derived `NSNumber` object shows its class to be `__NSCFNumber`. _So what gives?_

`NSCFBoolean` is a private class in the `NSNumber` [class cluster](https://nshipster.com/nsorderedset/). It’s a bridge to the [`CFBooleanRef` type](https://developer.apple.com/library/mac/#documentation/CoreFoundation/Reference/CFBooleanRef/Reference/reference.html), which is used to wrap boolean values for Core Foundation property lists and collections. `CFBoolean` defines the constants `kCFBooleanTrue` and `kCFBooleanFalse`. Because `CFNumberRef` and `CFBooleanRef` are different types in Core Foundation, it makes sense that they are represented by different bridging classes in `NSNumber`.

| Name | Typedef | Header | True Value | False Value |
|---|---|---|---|---|
| `BOOL` | `signed char` | objc.h | `YES` | `NO` |
| `bool` | `_Bool` (`int`) | stdbool.h | `true` | `false` |
| `Boolean` | `unsigned char` | MacTypes.h | `TRUE` | `FALSE` |
| `NSNumber` | `__NSCFBoolean` | Foundation.h | `@(YES)` | `@(NO)` |
| `CFBooleanRef` | `struct` | CoreFoundation.h | `kCFBooleanTrue` | `kCFBooleanFalse` |

---

For most people, Boolean values and boxed objects “just work”. They don’t really care what goes into making the sausage. But here at NSHipster, we’re all about sausages. That’s the honest truth.
