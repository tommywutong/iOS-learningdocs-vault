---
title: 'Breaking Swift with reference counted structs | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/03/27/on-delete.html'
original_language: en
published: 2016-03-27
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:315e6b092b8fcc25'
translated: false
---

> 原文：[Breaking Swift with reference counted structs | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/03/27/on-delete.html)　·　Cocoa with Love (Matt Gallagher)

In Swift, a `class` type is allocated on the heap, uses reference counting to track its lifetime and can perform cleanup behaviors when it is deleted. By contrast, a `struct` is not separately allocated on the heap, does not use reference counting and cannot perform cleanup behaviors.

Right?

In reality all of these traits “heap”, “reference counting” and “cleanup behaviors” can be true of `struct` types too. Be careful though: out-of-character behaviors are a good way to cause problems. I’m going to show how a `struct` can end up with some of the traits you might associate with a `class` and show how this can be a source of memory leaks, errant behavior and compiler crashes.

> **THIS ARTICLE IS OUT OF DATE AS OF SWIFT 3**: While it is still possible to have a heap allocated, reference counted struct with cleanup behaviors in Swift 3, it is no longer possible to capture a reference to `self` in a struct method as described in this article. The problems detailed in section 2 in this article have been fixed in Swift 3 and the remainder of this article is merely a historical artefact. Don’t worry: you’re better off as a result.

## Class fields in a struct

While a `struct` doesn’t usually have any `deinit` behavior, values of `struct` type are required (like all other values in Swift) to correctly maintain reference counts for their contents. Any reference counted field within the `struct` must have its reference counts correctly incremented and decremented as they are added to the `struct` and when they are removed, or when the `struct` is deleted.

We can exploit the fact that reference counted fields are decremented when a `struct` falls out of scope to attach behaviors to the `struct` as though it had a `deinit` method.

To do this, all we need to do is add a class field to a struct:

```swift
struct OrdinaryStruct {
   let classField: SomeClass
}
```

An example of using this effect productively is to attach an `OnDelete` field to your struct. An `OnDelete` class runs a customized closure at cleanup:

```swift
public final class OnDelete {
   var block: () -> Void
   public init(_ @escaping c: () -> Void) {
      block = c
   }
   deinit {
      block()
   }
}
```

Here’s an example struct named `DeletionLogger` that uses an `OnDelete` class to write to standard output when it is deleted:

```swift
struct DeletionLogger {
   let od = OnDelete { print("DeletionLogger deleted") }
}

do {
   let dl = DeletionLogger()
   print("Not deleted, yet")
   withExtendedLifetime(dl) {}
}
```

which will output:

```
Not deleted, yet
DeletionLogger deleted
```

## Trying to access a struct from a closure

So far, there’s nothing too strange. An `OnDelete` object can perform a function at cleanup time for a `struct`, a little like a `deinit` method. But while it might appear to mimic the `deinit` behavior of a `class`, an `OnDelete` closure is unable to do the most important thing a `deinit` method can do: operate on the fields of the `struct`.

Despite some obvious reasons why it’s a bad idea, let’s try to access the `struct` anyway and see what goes wrong. We’ll use a simple `struct` that contains an `Int` value and we’ll try to output the value of the `Int` when the `OnDelete` closure runs.

```swift
struct Counter {
   let count = 0
   let od = OnDelete { print("Counter value is \(count)") }
}
```

We can’t do this (error: `Instance member 'count' cannot be used on type 'SomeStruct'`). That’s not so strange though: we wouldn’t be allowed to do that, even on a `class` since you’re not allowed to access other fields from an initializer like that.

Let’s initialize the `struct` properly and then try to capture one of its fields.

```swift
struct Counter {
   let count = 0
   var od: OnDelete? = nil
   init() {
      od = OnDelete { print("Counter value is \(self.count)") }
   }
}
```

> This is no longer possible in Swift 3. It prevents us doing anything this profoundly silly with the error message: “Closure cannot implicitly capture a mutating self parameter”.

The compiler throws a segmentation fault in Swift 2.2 and a fatal error in Swift Development Snapshot 2016-03-24.

Excellent! I’m having fun already.

Of course, I could avoid all compiler problems by doing this:

```swift
struct Counter {
   var count: Int
   let od: OnDelete
   init() {
      let c = 0
      count = c
      od = OnDelete { print("Counter value is \(c)") }
   }
}
```

or the seldom-seen capture list which, in this case, is equivalent:

```swift
struct Counter {
   var count = 0
   let od: OnDelete?
   init() {
      od = OnDelete { [count] in print("Counter value is \(count)") }
   }
}
```

but neither of these options actually let us access the `struct` itself; both these options capture an immutable copy of the `count` field but we want access to the up-to-date mutable `count`.

```swift
struct Counter {
   var count = 0
   var od: OnDelete?
   init() {
      od = OnDelete { print("Counter value is \(self.count)") }
   }
}
```

> As before, this is no longer possible in Swift 3.

Hooray! That’s better. Everything is mutable and shared. We’ve captured the `count` variable and there are no compiler crashes.

We should ship this code since it clearly works, doesn’t it?

## Completely loopy

It clearly doesn’t work. If we run the code the same way as before:

```swift
do {
   let c = Counter()
   print("Not deleted, yet")
   withExtendedLifetime(c) {}
}
```

the only output we get is:

```
Not deleted, yet
```

The `OnDelete` closure is not getting invoked. Why?

Looking at the SIL (Swift Intermediate Language, as returned by `swiftc -emit-sil`), it’s clear that capturing `self` in the `OnDelete` closure prevents `self` from being optimized to the stack. This means that instead of using `alloc_stack`, the `self` variable is allocated using `alloc_box`:

```
%1 = alloc_box $Counter, var, name "self", argno 1 // users: %2, %20, %22, %29
```

and the `OnDelete` closure retains this `alloc_box`.

Why is this a problem? It’s a reference counted loop:

- closure retains the boxed version of `Counter` → the boxed version of `Counter` retains `OnDelete` → `OnDelete` retains closure

With this loop created, our `OnDelete` object is never deallocated and never invokes its closure.

## Can we break the loop?

If `Counter` was a `class`, we would capture it using a `[weak self]` closure and avoid the reference counted loop that way. However, since `Counter` is a `struct`, attempting to do that is an error. No luck there.

Can we break the loop manually, after construction, by setting the `od` field to `nil`?

```swift
var c = Counter()
c.od = nil
```

Nope. Still doesn’t work. Why not?

When the `Counter.init` function returns, the `alloc_box` it creates is copied to the stack. This means that the version `OnDelete` has retained is different from this version we can accces. The version `OnDelete` has is now inaccessible.

We’ve created an _unbreakable_ loop.

As [Joe Groff highlights in this thread on Twitter](https://twitter.com/jckarter/status/715171466283646977), Swift evolution change [SE-0035](https://github.com/apple/swift-evolution/blob/master/proposals/0035-limit-inout-capture.md) should prevent this problem by limiting `inout` capture (the kind of capture used in the `Counter.init` method) to `@noescape` closures (which would prevent capture by `OnDelete`’s escaping closure).

So the problem is that a different copy of `self` is returned by the `Counter.init` method than the version we capture during the method. What we need is to make the returned and retained versions the same.

Let’s avoid doing anything in an `init` method and instead set things up in `static` function instead.

```swift
struct Counter {
   var count = 0
   var od: OnDelete? = nil
   static func construct() -> Counter {
      var c = Counter()
      c.od = OnDelete{
         print("Value loop break is \(c.count)")
      }
      return c
   }
}

do {
   var c = Counter.construct()
   c.count += 1
   c.od = nil
}
```

Nope: we still have the same problem. We’ve got a captured version of `Counter`, permanently embedded in `OnDelete`, that’s different to the returned version.

Let’s change that `static` method…

```swift
struct Counter {
   var count = 0
   var od: OnDelete? = nil
   static func construct() -> () -> () {
      var c = Counter()
      c.od = OnDelete{
         print("Value loop break is \(c.count)")
      }
      return {
         c.count += 1
         c.od = nil
      }
   }
}

do {
   var loopBreaker = Counter.construct()
   loopBreaker()
}
```

The output is now:

```
Counter value is 1
```

This finally works, and we can see the state change from the `loopBreaker` closure is correctly affecting the result printed in the `OnDelete` closure.

Now that we’re no longer returning the `Counter` instance, we’ve stopped making a separate copy of it. There is only one copy of the `Counter` instance and that’s the `alloc_box` version shared by the two closures. We have a referenced counted `struct` on the heap and an `OnDelete` method that can access the fields of the `struct` at cleanup time.

## Some perspective

The code technically “works” but the result is a mess. We have a reference counted loop that we need to manually break, we can only access the `Counter` type through closures set up in the `construct` function and for a single underlying instance we now have four heap allocations (the closure in `OnDelete`, the `OnDelete` object itself, the boxed allocation of the `c` variable and the `loopBreaker` closure).

If you haven’t realized by now… this has all been a big waste of time.

We could just have made the `Counter` a `class` in the first place, keeping the number of heap allocations to 1.

```swift
class Counter {
   var count = 0
   deinit {
      print("Counter value is \(count)")
   }
}
```

Long story short: if you need access to the same mutable data from different scopes, a `struct` probably isn’t a great choice.

## Conclusion

Closure capture is something we just write and assume the compiler will do what is required. However, capturing mutable values has a few, subtly different semantics, that may need to be understood to avoid problems. This is complicated by a couple minor design issues that we’re still waiting on Swift 3 to fix.

Remember to consider the possibility of reference counted loops when capturing `struct` values with `class` fields. You can’t weakly capture a `struct` so if a reference counted loop occurs, you’ll need to break the loop another way.

In any case, most of this article has looked at a completely stupid idea: trying to make a `struct` capture itself. Don’t do that. Capturing, like other reference counting structures, should be an _acyclic_ graph. If you find yourself trying to make loops, it’s probably because you should be using `class` types with `weak` links from child to parent.

Finally, there are some _good_ reasons to use an `OnDelete` class but don’t start thinking it works like a `deinit` method – it’s predominantly for side effects (state outside the scope to which it’s attached).
