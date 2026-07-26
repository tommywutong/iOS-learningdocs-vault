---
title: CFBag
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/cfbag/'
original_language: en
published: 2012-08-27
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:fd218c59baaba022'
translated: false
---

> 原文：[CFBag](https://nshipster.com/cfbag/)　·　NSHipster (Mattt)

# [CFBag](https://nshipster.com/cfbag/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  August 27^th, 2012

Objective-C is a language caught between two worlds.

On one side, it follows the thoughtful, object-oriented philosophy of [Smalltalk](https://en.wikipedia.org/wiki/Smalltalk), which brings ideas like message sending and named parameters. On the other, are the inescapable vestiges of [C](https://en.wikipedia.org/wiki/C_(programming_language)), which brings it power and a dash of chaos.

It’s an identity crisis borne out through an ever-increasing prevalence of the `@` symbol.

This is also seen in the relationship between the Foundation and Core Foundation, particularly with the toll-free bridged collection class clusters: `NSArray` / `CFArray`, `NSDictionary` / `CFDictionary`, `NSSet` / `CFSet`. These collections can be passed back and forth between C functions and Objective-C methods without conversion. A leak in the abstraction, but a useful way to optimize the most critical parts of an application nonetheless.

However, toll-free bridging is the exception when it comes to collection classes in Foundation and Core Foundation:

| Foundation | Core Foundation | Toll-Free Bridged |
|---|---|---|
| `NSArray`^* | `CFArray`^* | ✓ |
| `NSCountedSet` | `CFBag`^* |  |
| _N/A_ | `CFBinaryHeap` |  |
| _N/A_ | `CFBitVector`^* |  |
| `NSDictionary`^* | `CFDictionary`^* | ✓ |
| `NSIndexSet`^* | _N/A_ |  |
| `NSMapTable` | _N/A_ |  |
| `NSOrderedSet` | _N/A_ |  |
| `NSPointerArray` | _N/A_ |  |
| `NSPointerFunctions` | _N/A_ |  |
| `NSSet`^* | `CFSet`^* | ✓ |
| ^* Indicates Mutable Counterpart |  |  |

Take a look at the second row, with `NSCountedSet` and `CFBag`. Notice that unlike the other Foundation / Core Foundation correspondence, these two are not toll-free bridged. No real explanation for this is provided in the documentation, aside from it being acknowledged in the `NSCountedSet` documentation. My guess is that it has something to do with `NSCountedSet` not having a mutable counterpart, and thus breaking the class cluster pattern seen in `NSArray`, et al.

## Bags, in the Abstract

In the [pantheon of collection data types](https://en.wikipedia.org/wiki/Collection_(abstract_data_type)) in computer science, bag doesn’t really have the same clout as lists, sets, associative arrays, trees, graphs, or priority queues.

In fact, it’s pretty obscure. You’ve probably never heard of it.

A bag, or [multiset](https://en.wikipedia.org/wiki/Multiset) is a variant of a set, where members can appear more than once. A count is associated with each unique member of the collection, representing the number of times it has been added. Like with sets, order does not matter.

Its practical applications are… limited, but you’ll know one when it comes up. Tallying votes in a general election? Simulating homework problems an intro probability class? Implementing a game of Yahtzee? Bag is your new bicycle!

## Working with `CFMutableBag`

As an implementation of the bag data type, `CFBag` and its mutable counterpart, `CFMutableBag`, are pretty slick.

Although it lacks the object-oriented convenience of `NSCountedSet`, it makes up for it with a number of ways to customize its behavior. When `CFBag` is created, it can be initialized with a number of callbacks, defined by the `CFBagCallBacks` struct, which specify the way values are inserted, removed, and compared:

```
struct CFBagCallBacks {
   CFIndex version;
   CFBagRetainCallBack retain;
   CFBagReleaseCallBack release;
   CFBagCopyDescriptionCallBack copyDescription;
   CFBagEqualCallBack equal;
   CFBagHashCallBack hash;
};
typedef struct CFBagCallBacks CFBagCallBacks;
```

- `retain`: callback used to retain values as they’re added to the collection
- `release`: callback used to release values as they’re removed from the collection
- `copyDescription`: callback used to create a string description of each value in the collection
- `equal`: callback used to compare values in the collection for equality
- `hash`: callback used to compute hash codes for values in the collection

For example, if you were implementing a vote tallying application, you could specify a normalizing function for `retain` to ensure that votes for mixed-case or misspelled names went to the right candidate, or ensure that the “correct” candidate is shown to be the winner when all the votes are in, with `equal` callback.

`CFMutableBag` also has `CFBagApplyFunction`, which has the ability to transform values over the collection, like if you wanted to smooth out vote counts, or something like that.

So in closing, if you need to rig an election, `CFBag` is your best bet.

---

But seriously, `CFBag`, useful in its own right, serves as a reminder of the hidden gems to be found within the standard frameworks and libraries–indeed what is at the very heart of being an NSHipster.

Also, `CFBinaryHeap`? `NSPointerFunctions`? `NSMapTable`? Surely, you’ll be seeing more of these in future editions.
