---
title: 'Reference counted releases in Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/resources-releases-reentrancy.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:e80586f586112409'
translated: false
---

> 原文：[Reference counted releases in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/resources-releases-reentrancy.html)　·　Cocoa with Love (Matt Gallagher)

I [released](https://www.cocoawithlove.com/blog/cwlsignal.html) my [CwlSignal project](https://github.com/mattgallagher/CwlSignal) a few weeks ago and since then, I’ve received several questions about my unconventional use of Swift’s `withExtendedLifetime` in that code.

To explain the topic properly, I wanted to briefly look at _when_ the Swift compiler chooses to release reference counted objects in Swift. It’s a tricky topic since The Swift Programming Language is too high level to offer details and other documentation in the Swift repository is sometimes incomplete.

Instead of documentation, I’ve resorted to looking at the Swift compiler to try and understand exactly what optimizations the compiler applies to re-order release instructions. Based on the observed behavior, I’ll talk about when you can expect your objects to be released, what you might need to do to keep them alive and how you can structure your code differently to help the compiler do its job.

I’ll eventually circle back to `withExtendedLifetime` and discuss its _intended_ purpose before talking about why I use it in my code for an unconventional reason.

## Scope lifetimes

In C++ and some other languages, it is guaranteed that all “l-values” (values assigned to a variable) will live as long as the scope that declares the variable. This behavior is the principle behind constructs like scoped locks in C++:

```cpp
std::unique_lock<std::mutex> lock(this->mutex);
doSomeInternalWork();
```

Since `lock` is guaranteed to live to the end of the scope, its destructor (which automatically unlocks the mutex) will not run until after the work function, protecting it under the mutex.

If we were to write the same code in Swift, if might look like this:

```swift
let lock = ScopedLock(self.mutex)
self.doSomeInternalWork()
```

the code would work but you probably shouldn’t use this code structure in Swift.

The reason you shouldn’t use this approach is because Swift’s automatic reference counting (ARC) doesn’t guarantee that scope variables – like `lock` in this example – will stay alive for the whole scope. ARC guarantees that scope variables will stay alive until their last usage – but `lock` isn’t actually used at _all_, it is merely assigned, so according to the loosest interpretation of ARC, `lock` could be released _immediately_.

However, like I said, the Swift equivalent works in the current version of the Swift compiler. Is this just a coincidence? Will this change in future? What can we expect.

Let’s try to find out through exploring code examples.

## Lifetimes shorter than the whole scope

To demonstrate a variable with a lifetime shorter than the whole scope due to Automatic Reference Counting, let’s look at an Objective-C example:

```objc
First *f = [[First alloc] init];
consumesAnyObject(f)

Second *s = [[Second alloc] init];
consumesAnyObject(s)
```

The `consumesAnyObject` declares its parameter `ns_consumed` (equivalent to Swift’s default behavior of passing parameters by ownership).

The end result is that the lifetime of `f` ends at the first `consumesAnyObject` and it is deallocated immediately after this call – in the middle of the scope. This is what automatic reference counting can do – and why you shouldn’t rely on its for something as scope lifetime dependent as the C++ style scoped lock.

Does Swift behave this way? No, at least, not in the current 3.0.2 version. The equivalent code sees both `f` and `s` released in after the _second_ `consumesAnyObject` call:

```swift
let f = First();
consumesAnyObject(f)

let s = Second();
consumesAnyObject(s)
```

## Extending an ARC lifetime

Let’s imagine though that we had found a situation where the lifetime shorted. We can combat this with the Swift function call `withExtendedLifetime`. This lets us clearly state that we want the lifetime of an object to extend over a series of subsequent calls:

```swift
let lock = ScopedLock(self.mutex)
withExtendedLifetime(lock) {
   self.doSomeInternalWork();
}
```

But given that I was unable to find an example in Swift where this was necessary, is `withExtendedLifetime` largely useless?

Thus far, the information we have looked at appears contradictory.

On the one hand:

- ARC guarantees lifetimes only to the last _usage_
- Objective-C’s ARC rules will let a lifetime end immediately after any “consuming” usage
- , apparently because there’s a need to “extend” lifetimes

On the other hand:

- there’s no obvious situation where we need to extend lifetimes in Swift; all lifetimes appear to run until the end of the scope, both in Debug and Release builds.

How does any of this make sense and what are the hard facts?

Sadly, the documentation is of limited help. The [Swift Programming Language](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html) is far too high level on the topic to fully explain the rules underlying Swift’s automatic reference counting. The [ARCOptimization.rst document](https://github.com/apple/swift/blob/master/docs/ARCOptimization.rst) is filled with prominent, useful sounding section headers followed by “TODO: Fill this in” and does not discuss when a lifetime might be shortened. The Clang [Automatic Reference Counting](http://clang.llvm.org/docs/AutomaticReferenceCounting.html) document is much bigger but as I’ve already demonstrated, Swift appears to play by a slightly different set of rules.

## Looking at releases in the Swift compiler

Let’s try to work out what’s happening by looking at the Swift compiler.

Releases in Swift are created by the “SILGen” (Swift intermediate language generator) code in Swift. SIL generation of any statement can emit releases for “r-values” (values used without being assigned to a variable) but releases for “l-values” that we’ve been looking at for most of this article occur in `emitCleanups` invoked from `SILGenFunction::emitEpilogBB` for the containing “basic block” in the [SILGenEpilog.cpp](https://github.com/apple/swift/blob/master/lib/SILGen/SILGenEpilog.cpp) file.

So “l-values” are left to the block’s epilogue and cleaned up in LIFO order. This would indicate Swift _does_ behave like C++ and other scope lifetime languages.

But that’s not the whole story.

If you’re compiling with optimizations enabled ("-O", e.g. Release builds) then eventually, the SIL Optimizer will apply the `SILTransform` from `createLateReleaseHoisting` over the code, as defined in [ARCCodeMotion.cpp](https://github.com/apple/swift/blob/master/lib/SILOptimizer/Transforms/ARCCodeMotion.cpp). This looks through releases – including those in the epilog – and moves them to the earliest possible point in the function.

So “l-values” are released as soon as possible, conceiveably moving to an earlier point in the function.

Once again though, that’s not the whole story. We need to define “as soon as possible”. It turns out that releases are only moved ahead of instructions that do not “block” them. What blocks the move of a release? Almost everything.

Looking at `mayHaveSymmetricInterference` in [ARCAnalysis.cpp](https://github.com/apple/swift/blob/master/lib/SILOptimizer/Analysis/ARCAnalysis.cpp), a release cannot be moved forward over:

1. memory accesses to the object’s address
2. memory accesses to anything in a memory graph connected to object
3. function
4. function
5. function cannot be absolutely determined

That last point is the biggest; outside of basic instructions there is usually some aspect of a function that can’t be absolutely determined.

These requirements significantly limit the ability of `ARCCodeMotion` to do _anything_. In an overwhelming number of cases, epilog releases won’t move at all. However, you can see why these restrictions are in-place: the optimizer should not be changing the order of “release” instructions if that change has any observable effect.

## Uh-oh, a ~~bug~~ (correction: surprising behavior) in Swift 3.0.x

> **Update**: according to responses from some Swift developers, the behavior in this section, surprising though it may be, is not considered a bug. See the next section for a discussion.

Thus far, I’ve been looking at the code in the Swift repository’s _master_ branch. The current version of Xcode, 8.2.1, bundles Swift 3.0.2. Unfortunately, the release optimization code used in this release is considerably older than the code on _master_ and contains a few ~~serious bugs~~ (correction: seriously surprising behaviors).

Let’s look at the following example:

```swift
func test1() {
   let f = First()
   let s = Second()
}
```

in this function, Swift will release `s` first, then `f` (following LIFO order, i.e. stack order). This is the _expected_ behavior.

However, if `First`, `Second` and a function named `something` that takes an `Any` parameter (it needs to be an existential to trigger this bug) exist but cannot be inlined (perhaps because they’re outside the current compilation unit), then the following code:

```swift
func test2() {
   let f = First()
   something(f)
   let s = Second()
}
```

will observably release `f` first, then `s` (breaking LIFO order). Note that `f` is still released in the epilog, after the `let s = Second()` line; the only change is that the compiler re-orders the two releases.

How bad could changing the order of releases be? Deadlock bad; this reordering can cause some dramatic reorderings that can seriously interfere with execution order.

Let’s look at one of the worst cases I’ve encountered:

```swift
func perform(data: UserData) {
   something(data)
   do {
      let resource = MutexLockedResource()
      resource.doSomethingElse()
   }
}
```

In this arrangement, the `data` parameter is released _during_ the lifetime for `resource` (i.e. inside the mutex). This could potentially cause a deadlock if `data` is not retained elsewhere and the `deinit` on `UserData` tries to re-acquire the `MutexLockedResource`.

This might seem like a contrived example but I’ve encountered multiple deadlocks and other sequencing problems that I’ve needed to work around, each caused by an unexpected re-ordering of `deinit` calls where variables in parent scopes were released during the lifetime of variables from child scopes. It’s a difficult problem to work around since it is so unexpected and Swift provides no ability to force ordering on `deinit`s.

Fortunately, the new ARC optimizer, `ARCCodeMotion`, appears to fix this and other problems. It is currently part of the Swift 3.1 branch so it will likely be a part of that release. In my testing, none of the release re-ordering problems described in this section occur with the new `ARCCodeMotion` transform.

## Update: details from some Swift developers

Joe Groff, a developer on the Swift team [writes](https://twitter.com/jckarter/status/814522857325608960):

> **jckarter**: @cocoawithlove Swift’s semantics are like ObjC’s. That the compiler doesn’t shorten lifetimes now is no guarantee it won’t later.

We should expect lifetimes to shorten, like the Objective-C example given above, in future. Good to know; `withExtendedLifetime` will be useful!

Another developer on the Swift team, Michael Gottesman, [writes](https://twitter.com/gottesmang/status/814561037865271296):

> **gottesmang**: @s_tolksdorf @jckarter @cocoawithlove We do discuss this in the swift docs. See here: [github.com/apple/swift/bl…](https://github.com/apple/swift/blob/master/docs/ARCOptimization.rst#deinit-model)

I linked this document above and I did read it. Clearly though, I failed to absorb that section. It does state that “interference” in a `deinit` method will not be considered when reordering releases, so `deinit` invocations can be arbitrarily reordered with respect to each other.

I guess I expected this might be the case. Example 1 in the “Uh-oh, a bug” section is not considered a bug.

> **jckarter**: @cocoawithlove Reordering of deinits isn’t a bug. You shouldn’t rely on LIFO order of local variable releases.

This is implied by the same documentation Michael Gottesman linked, however, [I responded](https://twitter.com/cocoawithlove/status/814733718568898560) with a comment that I think Example 2 in the “Uh-oh, a bug” section _should_ be considered a bug, despite the fact that its cause is the same as Example 1.

> **cocoawithlove**: @jckarter I’m okay with lack of LIFO deinit, but: an obj not used in child scope should deinit before or after child scope, never during.

Twitter’s a difficult medium to make a clear point so I’ll clarify here. My reason for considering that second example more serious than the first is that I feel that an object from a parent scope, that is not used a child scope, should not interleave effects with effects from the child scope – even when these effects are release effects and the scope is just an otherwise pointless `do` scope.

Let’s move the `do` scope into a child function and see how that goes:

```swift
func perform(data: UserData) {
   something(data)
   completelySeparateChildFunction()
}
```

In this code, compiled under the current Swift 3.0.2, if the `completelySeparateChildFunction` is inlined, the `data` parameter will be released during a mutex which exists purely in the `completelySeparateChildFunction`. It’s a potential deadlock triggered by interleaving our code with code we can’t even see. And even if we know what `completelySeparateChildFunction` does, Swift offers no way that our `perform` function can prevent this interference (the only certain approach to prevent this interference is to mark `completelySeparateChildFunction` as `@inline(never)`).

Interleaving of effects between parent and child scopes is simply too big a violation of the principle of least surprise. These things are _clearly_ distinct in the structure of our code, they should not intersect unless we _explicitly_ cause them to intersect.

## The conventional use-case for `withExtendedLifetime`

I gave the following example and claimed that `withExtendedLifetime` is largely useless.

```swift
let lock = ScopedLock(self.mutex)
withExtendedLifetime(lock) {
   self.doSomeInternalWork();
}
```

Until such time as Swift starts ending lifetimes earlier (see the previous section) Swift simply isn’t forcing our hands to keep `lock` alive (although a safety conscious programmer should probably use `withExtendedLifetime` anyway).

There is a situation where Swift does force our hands and that’s with r-values. The following code strictly _does_ required `withExtendedLifetime`:

```swift
withExtendedLifetime(ScopedLock(self.mutex)) {
   self.doSomeInternalWork();
}
```

I rarely actually use `withExtendedLifetime` in this way though. You need to have an r-value object with side-effects that affect the scoped code for this to be useful – and the `deinit` should not have strict ordering requirements or it will hit the surprising behaviors discussed in the previous two sections. That’s a combination of requirements that doesn’t come up very often.

However, there is a usable tip here: the difference between l-values and r-values is usually not optimized away by the compiler for reference counted objects. Reference counted r-values are usually more precise and more efficient than reference counted l-values since their release will occur before the next non-release statement. If there are statements between the `withExtendedLifetime` call and the end of the surrounding scope, an r-value will be released _before_ those statements whereas an l-value will usually be released after.

Keep this point in mind: if you don’t _need_ to assign an object to a parameter, it’s better to avoid it.

## Unconventional uses of `withExtendedLifetime`

So the conventional use cases for `withExtendedLifetime` are pretty rare. I still use it but my usage tends to be a little unconventional.

A common requirement in the CwlSignal project is deferring the release of user-supplied data to outside a mutex (so any `deinit` on the user-supplied data can’t trigger a deadlock by re-entering the mutex). This is done in CwlSignal with code that looks like:

```swift
deferredWork.append { withExtendedLifetime(data) {} }
```

The `deferredWork` variable is just a list of closures that will be run once the mutex is exited. However, the closure we’re appending doesn’t need to _do_ anything, except capture the `data` value. I don’t do _literally_ nothing though, instead I call `withExtendedLifetime`.

We could try literally doing nothing. We’d still need to tell Swift that we want to capture the `data` variable which we can do through a capture list:

```swift
deferredWork.append { [data] in }
```

but the compiler will complain:

```
warning: Capture "data" was never used
```

So I use `withExtendedLifetime` to tell the compiler “Calm down, I’m using it.”

There are similar examples with “dead stores”. The CwlSignal project includes a function that looks a little like this:

```swift
public static func never() -> Signal<T> {
   var input: SignalInput<T>? = nil
   return Signal<T>.generate { i in
      input = i
   }
}
```

The purpose of the code inside the closure is simply to hold onto any `i` value it receives so that `i` lives as long as the closure itself. This is done by storing `i` in the mutable captured variable `input`.

All of that is fine except that the compiler sees `input = i` as a dead store.

```
warning: variable 'input' was written to, but never read
```

Of course, keeping the object alive _is_ the usage so we _want_ a dead store. To make this clear to the compiler, I use the `withExtendedLifetime(input) {}` so the compiler has something that it interprets as “using” the value.

```swift
public static func never() -> Signal<T> {
   var input: SignalInput<T>? = nil
   return Signal<T>.generate { i in
      input = i
      withExtendedLifetime(input) {}
   }
}
```

The reason to use `withExtendedLifetime` for this purpose is that it is effectively a no-op but its message to the compiler “I am using this variable here” will prevent complaints that variables aren’t being used. Since I’m performing the dead store for the purpose of lifetime manipulation, `withExtendedLifetime` is also vaguely appropriate, even though this isn’t its conventional use-case.

## Conclusion

Swift’s current behavior is quite conservative about release reordering. The Swift developers have pointed out that just because this is the case now, doesn’t mean it will continue to be the case in future – they clearly _intend_ for mid-scope releases to occur more frequently than currently happens. This will eventually bring Swift’s release ordering a little closer to those of Objective-C.

I performed a cursory code analysis to determine under what circumstances a release instruction might be re-ordered in the current versions of Swift (up to and including the Swift 3.1 prerelease branch). The truth is that at the moment, releases are rarely reordered much at all. Lack of knowledge about memory graphs and reachability usually keeps epilog releases trapped in the epilog. When these releases are reordered, the effect is usually _completely_ undetectable.

The `withExtendedLifetime` function has its intended uses – to extend the lifetime of an object over a relatively narrow closure scope. Given Swift’s current, highly conservative behavior, it is most clearly useful for r-values and when using `withUnsafePointer` into an object that is not retained elsewhere. Safety conscious users should probably use it in broader contexts since Swift may force your hand in future.

However, I usually use `withExtendedLifetime` as a compiler warning silencer when I’m performing ownership transfer operations without any other semantic purpose. The function has no effect other than a private call to `_fixLifetime` (which merely forces the SIL layer to keep the object alive) so I find it well suited to the task.

### Looking forward…

There’s more code from the CwlSignal project that I want to talk about. The next article will talk about a handy utility that you can use independently of CwlSignal to manage a fiddly legacy from Objective-C.
