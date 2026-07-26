---
title: 'Partial functions in Swift, Part 1: Avoidance | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html'
original_language: en
published: 2016-01-25
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2b04cdff78258110'
translated: false
---

> 原文：[Partial functions in Swift, Part 1: Avoidance | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html)　·　Cocoa with Love (Matt Gallagher)

For my first proper article since returning to Cocoa with Love, I want to talk about “partial functions” (functions with preconditions).

It’s an unusual topic for an app programming blog since, outside of API design or Design by Contract, preconditions are not widely discussed. This isn’t because our functions are precondition-free. Instead, it’s because we tend to test applications in such a narrow way that we never consider the entire range of values that can be passed to our functions. Our functions may have lots of implicit preconditions (including dependencies on broader program state) that we’ve never considered or that we never document (so are easy to violate during subsequent changes).

Ultimately, consideration of preconditions and how to avoid partial functions is the consideration of whether our programs work reliably across the whole range of possible scenarios.

## Background: type requirements versus runtime expectations

Every function has two categories of requirements:

1. **Type requirements**: a function must accept arguments and return a result as specified by its type signature. The compiler enforces the type requirements, ensuring both caller and function meet the requirements.
2. **Runtime expectations**: a description of what the function will achieve by its conclusion. Ensuring runtime expectations are met is the role of the function’s programmer (and testing).

What happens when these two categories of requirements conflict?

Let’s consider a function that converts an `Int` to a `Bool` (those are the type requirements). Rather than use the C rule of `0` is `false` and anything else is `true`, this function will be strict: `0` is `false` and only `1` may be converted to `true` (that’s the runtime expectation).

```swift
func toBool(_ x: Int) -> Bool {
   if x == 0 {
      return false
   } else if x == 1 {
      return true
   }
}
```

This function satisfies the runtime expectations: `0` becomes `false` and `1` becomes `true` but the compiler will highlight the closing `}` character with the error message:

> Missing return in a function expected to return ‘Bool’

The compiler knows that we haven’t handled every possible value of `x` and the function can skip over the two `if` conditions and reach the end without returning a value (a violation of type requirements).

We could change the function to handle every possible value of `x`:

```swift
func toBool(_ x: Int) -> Bool {
   if x == 0 {
      return false
   }
   return true
}
```

but now we’re converting values like `-1` to `true` in violation of the runtime expectations.

This is a conflict between type requirements and runtime expectations.

## Background: preconditions

The conflict occurs because the runtime expectations imply an additional requirement that is not part of the type requirements. We call this additional requirement a **precondition**. In our simple `toBool` example, the precondition is that the value of `x` must be `0` or `1`.

This article mostly discusses preconditions on parameters (since it is easier in simple examples). However many preconditions depend on broader program state. For example, if you need to initialize a module before invoking its methods, that's a precondition. If you need to start a server before making requests, that's a precondition. If you're only allowed to set a value once on an object, that's a precondition.

That’s simple enough to say but there’s a problem: the precondition isn’t known to the compiler so it is possible to accidentally violate the precondition at runtime. What should a function do if the precondition is not met?

The only safe option is to trigger a fatal error (abort the program).

This might not sound “safe” but it’s the only approach that prevents something potentially worse. If a function fails to meet runtime expectations and actually returns, this means anything dependent on the function is now in an indeterminate state. Once the program is in an indeterminate state, any branch could go the wrong way, any action could be wrong. Maybe `toBool` was trying to answer the question “Do you want to delete everything on your hard disk?” Maybe `toBool` was trying to determine if the program should exit a loop but now it’s stuck in the loop, allocating more memory until the whole computer grinds to a halt.

We also want to abort the program because it draws attention to the exact location where the programming error occurred – rather than forcing us to look at subsequent symptoms and try to trace the symptoms back to where the program went awry. A fatal error simplifies debugging and ensures that when an error occurs, it’s likely to be caught and reported.

## Background: preconditions in Swift

So we need to enforce the precondition by triggering a fatal error if it is not satisfied. Swift has a function named `precondition` which, unsurprisingly, does exactly that: tests a condition and triggers a fatal error if the condition is `false`. Our function then becomes:

```swift
func toBool(_ x: Int) -> Bool {
   precondition(x == 0 || x == 1, "This function can only convert 0 or 1 to Bool")
   if x == 0 {
      return false
   }
   /* x == 1 */
   return true
}
```

> **Terminology note**: I’ll refer to the `precondition` function for most of this article (since its role is unambiguous) but numerous other functions may be similarly used to directly (or indirectly, though a child funcion) trigger a fatal error including `assert`, `assertionFailure`, `precondition`, `preconditionFailure`, `fatalError` or other standard library functions that use “trap” intrinsics like `Builtin.int_trap` or `Builtin.condfail`.

Now, all of this might seem a little obstinate. I’ve deliberately chosen type requirements and runtime expectations that conflict and I’ve refused to change either, forcing the use of `precondition`. You might think no one would ever design a function this way of that you’d never use a function like this.

The reality is that nearly every Swift program uses this type of function indirectly through Swift standard library functions that contain similar `precondition` checks. Most common in Swift are the `Array` subcript operator (which has a precondition that the index be in-bounds), the force-unwrap operator `!` on the Swift `Optional` type (which has a precondition that `self` be non-`nil`), any use of the `ImplicitlyUnwrappedOptional` type (which similarly has a precondition that `self` be non-`nil`) and the default integer operators and conversions (which trigger fatal errors on overflow).

There’s another kind of precondition you may have in your code: functions that may misbehave, non-fatally, when certain implicit, unchecked requirements are not met. This is an extremely difficult point to keep under control but you need to consider whether any of your functions have implicit, unchecked requirements and add `precondition` checks to document the requirements and ensure that you don’t accidentally violate them in the future.

## Partial functions

A `precondition` is used to enforce the requirement that a function may be invoked only for a _partial_ subset of the total set of values that would be valid according to the function’s type signature. That leads us to the mathematical term “_partial_ function”.

_The next paragraph is going to be math jargon. It’s important to use the correct terminology. It’s not so bad; hold your breath if you’d like._

In mathematics, a **[partial function](https://en.wikipedia.org/wiki/Partial_function)** is a function constructed to map values from a **domain** (set of possible input values) to a **codomain** (set of possible output values) where the function is **undefined** (no appropriate mapping exists) for one or more values in the input domain. The subset of inputs values where the partial function is actually defined is called the **domain of definition**. Functions that are defined for all possible inputs are called **total functions**.

A simple example of a partial function in mathematics is _division_. A mathematical function that divides 5 by any real number:

f:ℝ→ℝ  where  f:x↦5x

is undefined for x = 0 because there is no sensible way to divide by zero in typical mathematics.

If implemented in Swift, due to the “undefined” case, we use `precondition` to enforce the requirement that the function may be invoked only within the “domain of definition”:

```swift
func divideFive(by x: Real) -> Real {
   precondition(x != 0)
   return 5 / x
}
```

## Hidden partial functions

Now there isn’t a `Real` type in the Swift standard library. We do have `Double` but Swift’s `Double` doesn’t actually work this way (see “[Change the behavior](#change-the-behavior)” below). However, Swift does work this way if we swap `Int` for `Real`:

```swift
func divideFive(by x: Int) -> Int {
   return 5 / x
}
```

Where did the `precondition` go? It’s still there. We don’t need to write `precondition` because it’s part of the `/` operator. The infix `/` operator for `Int` uses “checked” division in Swift (implemented in the standard library as `_overflowChecked`) so it will trigger a fatal error if it is invoked with `0` as its second argument. This occurs because the `Int` type in Swift, as with ℝ (reals) in the math example above, has no sensible way to handle division by zero.

The following is another example of a partial function because it may trigger a fatal error based on the value of parameter `someArrayIndex`:

```swift
func someArrayFunction(_ at: Int) -> Element {
   return myArray[at]
}
```

And so is this, since it may trigger a fatal error based on the state of `self`:

```swift
struct someStructWithAnOptionalMember {
   var optionalSomeType: SomeType?
   func accessor() -> SomeType {
      return optionalSomeType!
   }
}
```

## The problem with partial functions

How did I know that the infix `/` operator for `Int` uses “checked” division in Swift and will cause a fatal error if it is invoked with `0` as its second argument?

The only way to know is to check the documentation. [The Swift Programming Language](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/AdvancedOperators.html) describes the requirements of division as:

> arithmetic operators in Swift do not overflow by default. Overflow behavior is trapped and reported as an error.

It’s up to the reader to either know (or experiment and find out) that this means that the division operator will write a failure message to standard out and abort the program if you ever pass `0` as the second argument to integer division.

This makes partial functions terrifyingly dependent on documentation and testing (two areas worryingly prone to lapses):

1. A partial function’s requirements must be clearly documented
2. Users of the function must read and understand the documentation
3. Tests must exercise a wide range to confirm usage remains correctly inside required bounds in all cases

The biggest risk with partial functions is misbehavior in a deployed build. A corollary is that they don't cause as many problems for testing code. In tests we want to fail early and often. Use of `Array` subscript operators, `Optional` force-unwrap `!` and other convenient-but-severe partial functions in testing code is okay.

Let’s assume points 1 and 2 are satisfied (or at least noticed during debugging). We still need to satisfy point 3.

Unfortunately: debugging and testing are unlikely to check all scenarios in a non-trivial program. Debugging and testing excel at validating specific scenarios but unless your tests are extremely thorough, it’s likely your users will be able to get one of your functions into a state you never tested. If your program uses partial functions, this leaves you expsed to potential runtime failure.

## Avoid partial functions and use total functions instead

Partial functions should be avoided because:

- they have requirements that the compiler cannot verify
- they can pass your testing but still cause fatal errors after deployment if different data is encountered

Let me be clear: it is not the _checking_ of preconditions that should be avoided. Absolutely, if your function has preconditions, you should check them immediately or face rendering your program “indeterminate”.

The problem is the _existence_ of preconditions.

A function is partial if it has preconditions. We want to design our functions as “total functions” that have no preconditions. This means that we need a sensible result for every possible input value.

Let’s revisting the mathematical function that divides 5 by any real number. Previously we defined it as a partial function that was undefined for `x = 0`. Let’s write it as a total function:

f:X→ℝ  where  X=x∈ℝx≠0 ,  f:x↦5x

To explain this in a more programmer-friendly way: we’ve changed the type signature of the function. Instead of accepting any “Real” as an input, I’ve defined a new type `X` that can be any value in the Reals except zero. Now, the function is defined for every possible value in `X` and the function is a total function.

A rough equivalent in Swift would be:

```swift
struct NonZeroInt {
   let value: Int
   init?(fromInt: Int) {
      guard fromInt != 0 else { return nil }
      value = fromInt
   }
}

func divideFive(by x: NonZeroInt) -> Int {
   return 5 / x.value
}
```

The runtime requirement in `divideFiveBy` is gone and instead we have a new type, `NonZeroInt` that satisfies the requirement at compile-time.

You might be able to see why [I mentioned, above](#partial-functions), that it’s important to think about `precondition` as subtracting values from the total set of valid values according to the type signature. We can avoid a `precondition` by defining a new type where those `precondition`-excluded-values are avoided by design in the new type.

## Failable construction, non-failable usage

It's uncommon to see the term "partial function" used in imperative languages like Swift but it's a common term [in functional languages like Haskell](https://wiki.haskell.org/Partial_functions), Unsurprisingly, Haskell has pages on [avoiding partial functions](https://wiki.haskell.org/Avoiding_partial_functions), too.

In the previous example, we created a new type, `NonZeroInt`, but the constructor for this new type can fail (return a `nil` instead of a value). In some sense, we’ve simply taken the burden of ensuring correctness from the call location of `divideFiveBy` and put it somewhere else. However, this change has helped for two reasons:

1. the compiler will ensure that we check the `NonZeroInt?(fromInt:)` return result
2. we’re validating the value at its construction, not when it is used

The first point stops the function being a partial function but the second point is just as interesting.

Ideally, we shouldn’t construct `NonZeroInt` from an `Int` immediately before passing into `divideFiveBy`, instead we should never have the `Int` at all; the `NonZeroInt` should be constructed at the source. Maybe the source is a settings file, maybe the source is user-input, maybe the source is a network connection; in any case, as soon as the value comes into existence, we immediately know if it’s valid or invalid. In the invalid case, we can report the input as the source of the problem. This is a huge improvement over carrying an invalid `0` value `Int` for an unknown time until it is finally passed to the function `divideFiveBy` which has no idea about the origin of its parameters.

Think about the path of data through your program as a pipeline: if your data won’t fit through the whole pipeline, reject it at the _start_ rather than letting it cause problems in the middle. Ideally, construction should be the only scenario that can fail and every use case should be a “total function”.

## Other approaches for avoiding partial functions

Avoiding a partial function involves making the type requirements and the runtime expectations agree.

Defining a new, more specific type that encapsulates the runtime expectations’ complete requirements for the data is the conceptually best approach to addressing the problem. As I explained, it pushes any checks on data back to the construction point which is the best place to handle error conditions.

However, there are plenty of cases where it’s not the most practical option:

- it may be algorithmically difficult to determine the constraints for the data ahead-of-time
- you might not have access at construction-time to state information required to check validity
- maybe you don’t have control over the design of earlier stages in the data pipeline
- maybe you construct data in a lot of places but only use it in one place so it’s simpler to change the usage location instead of the construction location

Fortunately, there are plenty of other options.

### Change the return type

The simplest solution to making any partial function into a total function is to change the type signature to include room in the return type to communicate a failure condition. Instead of needing to trigger a fatal error, we can communicate the condition back to the caller and the caller can choose how to handle the result.

Swift’s `Optional` is ideal for this as we can show with our `toBool` function:

```swift
func toBool(_ x: Int) -> Bool? {
   switch x {
   case 0: return false
   case 1: return true
   default: nil
   }
}
```

An example of this in the Swift standard library is the subscript operator on `Dictionary`. Unlike the subscript on `Array`, the `Dictionary` version returns an `Element?`. This means that you _are_ allowed to look up a key that doesn’t exist.

I personally like to use the following extension on `CollectionType` to allow this type of `Optional` returning access for `Array` or other `CollectionType`s:

```swift
extension CollectionType {
   /// Returns the element at the specified index iff it is within bounds, otherwise nil.
   public func at(_ index: Index) -> Generator.Element? {
      return indices.contains(index) ? self[index] : nil
   }
}
```

The name `at` in this case is borrowed from a function in C++ that accesses the value if it exists or throws an exception if it does not. A Swift `throws` function would be closer to the C++ implementation but returning an `Optional` is more in line with the pattern established by `Dictionary` and is syntactically tighter for this use-case.

However, using Swift’s error handling mechanism is also a valid way of making a function total, if you’d prefer it:

```swift
enum ArtithmeticError { case DivideByZero }
func divideFive(by x: Int) throws -> Int {
   switch x {
   case 0: throw ArtithmeticError.DivideByZero
   default: return 5 / x
   }
}
```

In Objective-C, exceptions were (usually) used to indicate unrecoverable situations (i.e. partial functions). However, Swift `throws` are meant to be caught; in fact they _must_ be caught. Therefore throwing an `Error` in Swift is really just offering a different return type – semantically similar to returning an `Optional` despite the syntactic differences.

### Change the behavior

Depending on context, it might make sense to change the runtime expectations so that every input is mapped to a valid output. In the first example, if we had used the C language’s definition of a `Bool` (anything that isn’t zero is `true`) then our `toBool` function would never have needed a precondition.

We can also change the behavior of the `divideFiveBy` function to do something not-entirely-accurate but which may be valid, depending on expected usage:

```swift
func divideFive(by x: Int) -> Int {
   switch x {
   case 0: return Int.max
   default: return 5 / x
   }
}
```

This mirrors the Swift standard library’s division operator for `Double`:

```swift
func divideFive(by x: Double) -> Double {
   return 5 / x
}
```

Unlike the version from `Int` to `Int`, this function is a total function, not a partial function.

The `/` operator for `Double` will return `Double.infinity` (IEEE 754 “positive infinity”) if invoked with `x == 0` which isn’t really true in a mathematical sense but is sufficient that you can work out what happened. Of course, the problem with this type of behavior change is that it might obscure the “basically an error” status of the result (for example: you should be handling the zero denominator rather than attempting to scale a drawing by “+infinity”).

### Keep dependent components together

A common reason for partial functions is that you’re using two pieces of data that need to agree with each other (like an `Array` and a subscript index) but you create and store them separately so they are not naturally kept in agreement – they might even be created separately and could be out of agreement from their construction.

We can avoid preconditions on separate data being in sync by holding the required data in a single data structure that ensures the requirement.

The following alternative approach to indexes into an `Array` ensures the index remains valid at all times by keeping a reference to the `Array` and preventing transformations to the `index` that would make it invalid.

```swift
enum AlwaysValidArrayIndexError: Error { case NoAcceptableIndex }
struct AlwaysValidArrayIndex<T> {
   // Store the array and the index (preventing them falling out-of-sync
   let array: Array<T>
   let index: Int

   // Construct from an array (note: this captures a copy
   init(firstIndexInArray a: Array<T>) throws {
      guard !a.isEmpty else { throw AlwaysValidArrayIndexError.NoAcceptableIndex }
      array = a
      index = array.startIndex
   }
   
   // Internally construct a new version from its components
   private init(array: Array<T>, index: Int) {
      self.array = array
      self.index = index
   }

   // Safely advance the index or throw an error
   func validIndex(after: AlwaysValidArrayIndex<T>) throws -> AlwaysValidArrayIndex<T> {
      let next = array.index(after: after.index)
      guard next != array.endIndex else { throw AlwaysValidArrayIndexError.NoAcceptableIndex }
      return AlwaysValidArrayIndex(array: array, index: next)
   }

   // Access the guaranteed to be safe index
   func elementAtIndex() -> T {
      return array[index]
   }
}
```

#### Minor aside/complaint about how Swift String indexes work

Sadly, despite storing the `_StringCore` internally and therefore being able to ensure validity at all times, `String` indexes let you hit fatal errors by advancing past the end (rather than a more graceful `nil`) and even worse: don’t themselves access characters but instead need to be passed back into the subscript on a `String`. This second problem lets the `String.CharacterView.Index` and `String` be out-of-sync again (since you can use an index from one `String` on a different `String`), leading to potential fatal errors (for out-of-range accesses) or invalid Unicode as produced by this example where an index from “Unrelated string” is used to access an invalid offset in an Emoji string:

```swift
let characterView1 = "👿👿".characters
let invalidIndex = "Unrelated string".characters.index(after: characterView1.startIndex)
print(characterView1[invalidIndex])

// Output will not be the 'n' in "Unrelated" or the second "Imp" Emoji.
// Instead we get the Unicode invalid character marker '�'.
```

I hope these problems are addressed in future changes to the Swift standard library (even a basic `precondition` failure when using indexes with the wrong string would be preferrable).

### Change the design

A final way to avoid partial functions is to avoid design patterns where they are common. This means: use the library functions and features that are total functions. If we restrict our programming to total functions then our functions are more likely to be total functions too.

Easy examples include using `for x in`, `map` and `filter` to perform most of the needed work on an `Array` without using the subscript. Similarly as an alternative to `Optional`’s force unwrap, you can always use `if let`, `switch` and `flatMap` and avoid any potential fatal errors.

## What are the reasons for writing partial functions?

I’ve used a lot of words to say “partial functions are bad”. I also shown multiple ways to avoid them.

Why do partial functions exist at all? There’s a few reasons. I don’t agree with them all.

### Aesthetics

The biggest reason for partial functions is aesthetics: the interface designer didn’t really want to define a new type, return an `Optional` or declare a function as `throws`.

To illustrate this claim, there’s a number of partial functions in the Swift standard library that are designed to look like traditional operators from C while transparently adding safety checks where memory unsafe behavior could have occurred in C. This includes `Array` subscripts, `ImplicitlyUnwrappedOptional` and overflowable arithmetic; these are designed to _look_ like their C equivalents while applying runtime checks internally. There’s a historical/social expectation: people expect an array index to return a non-`Optional`. People expect that they can forcibly unwrap `Optional` if they want. People don’t want the syntactic overhead of dealing with overflows for most arithmetic.

The choice to use `precondition` rather than return an `Optional` (or another alternative) is risky and crash prone but that’s how humans work sometimes.

### Internal functions with simple conditions

Preconditions involving multiple values being in-sync or methods on an object being invoked in a given order take additional work to avoid. For our internal functions – where we are the only people who need to learn and obey any preconditions – the amount of work to avoid the precondition might not be worth the effort, particularly if the precondition is simple and obvious and we’re sure we won’t accidentally violate it.

Just make certain to use `precondition` to explicitly check, rather than run the risk of accidentally violating the precondition later.

### Method overrides

If an overrideable method is required by the superclass to do something (e.g. invoke `super`), we often need to rely on `precondition` or other similar tests to ensure the requirement occurs.

This is really a limitation of how object-oriented programming composes interfaces: subclasses are fully in control and the superclass only receives control when the subclass yields it. If the superclass wants to place requirements on the subclass, it can only do that checking the requirement after-the-fact (a “postcondition” but technically still implemented using `precondition`).

### Effectively unreachable code paths

The actual conditions required to reach some code paths are so convoluted that they’re basically unreachable. This sometimes occurs when checking the results of functions: we feel obliged to check all error results but we might not be able to design a test case to actually reach the failure path. Rather than write a recovery attempter that we can’t test, we may place a `preconditionFailure` or a `fatalError` in the path to confirm out belief that the branch is unreachable.

Examples where this is appropriate include handling memory allocation failure return paths from certain C functions. On a modern system, a memory allocation failure is usually impossible (the OS will kill the process before `malloc` fails) so writing code to test and handle this situation is a poor use of our time.

### Forced correctness

In some cases interface designers _want_ haphazard users of their functions to see failures. There’s an argument that programming defensively against careless users of your function encourages poor programming and prevents users understanding what they’re doing wrong; instead, we should force bad programmers to confront their mistakes.

I think this argument is more valid in languages like C where returning an `int` error condition is frequently ignored by the user so a fatal error is more attention grabbing. In Swift, I think this approach is inappropriate. Users can’t ignore `Optional` or `throws` in Swift and will learn their mistakes from a returned “invalid argument” `Error` just as well as they’d learn from a `precondition` failure – in fact, better, since users might not be aware of the existence of possible `precondition` failures but the syntactic overhead for `throws` is unavoidable so it’s possible that a never-before-seen failure will still be handled correctly at runtime.

Truly haphazard programmers are likely to handle `Optional` and `throws` results by using force-unwrap or `try!` in Swift so they’re going to see fatal errors anyway.

### Logic tests

The `assert` function is commonly used to test “soft” postconditions (where a `false` result is not a critical failure) and other program logic.

If you’re unaware, `assert` works like `precondition` in Debug builds (compiled with ‘-Onone’) but does nothing in Release builds (compiled with ‘-O’). This split behavior complicates the practical implications but ultimately `assert` is still used to fatally test conditions in Debug builds so its usage in a function is still equivalent to a partial function.

Ultimately, `assert` treads a weird line between a `precondition` that isn’t properly tested in Release builds (leaving you open to indeterminate behavior) and a logic test that should be in your testing code and not in your regular code.

I personally think `assert` is a good idea only when a `precondition` is too computationally onorous to run at Release. In all other cases, you should be using `precondition` (because you really do want the condition to be `true`) or you should move the testing into your test code (because it’s not truly a precondition and you’re just validating behavior in a specific case).

## Conclusion

A function with one or more preconditions is a partial function (valid for only a subset of the values implied by the type signature). Each precondition represents a potential programmer error you can make when using the partial function. Unlike type requirements (where programmer errors get caught at compile time) precondition programmer errors manifest as a fatal errors at runtime.

Fatal errors are obviously bad and you can avoid them by avoiding partial functions.

**Do _not_ avoid a partial function by failing to check preconditions**. Boldface for a reason: that’s worse than a crash. Failing to check preconditions results in indeterminate behavior that can let misbehavior propagate, potentially leading to “worst case” scenarios. It also impedes debugging and allows misbehaviors to persist rather than being quickly caught. If your function has requirements, check them!

Instead, we can avoid partial functions by fixing our design to eliminate preconditions.

Preconditions are required only because there are values permitted by the type requirements that cannot meet the runtime expectations. If you fix the type requirements (choose input types where every value can meet the runtime expectations) or change the runtime expectations (to handle every value in the type requirements) there’s no need for preconditions.

This can be as simple as returning an `Optional` instead of a simple value. Or defining an input type that validates requirements on construction (returning `nil` if the requirements can’t be met). Given Swift’s syntactically efficient conditional unwrapping operators and error handling capabilities, the cost of handling lots of these types of conditionals is quite low so partial functions should be a very rare thing.

Despite all this, partial functions do exist. There are some narrow cases where they are necessary and some other situations where they’re commonly used. And due to their use in the Swift standard library, almost all Swift programs use partial functions in some form so you need to be aware of them.

For these reasons, you might even decide to create partial functions of your own. In the next post, I’ll look at testing partial functions by catching `precondition` failures so you can ensure any partial functions you create will trigger fatal errors correctly as expected.
