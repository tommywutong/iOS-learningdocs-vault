---
title: 'Errors: unexpected, composite, non-pure, external. | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/03/17/non-pure-errors.html'
original_language: en
published: 2016-03-17
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2943164f5f7c301e'
translated: false
---

> 原文：[Errors: unexpected, composite, non-pure, external. | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/03/17/non-pure-errors.html)　·　Cocoa with Love (Matt Gallagher)

The opening sentence of [“The Swift Programming Language”](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/index.html) chapter on [“Error Handling”](https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/ErrorHandling.html) briefly refers to “error conditions” but beyond that, there’s no definition of what an error is, the conditions that would give rise to one or why it would require special handling.

It’s not a problem unique to “The Swift Programming Language”; search for “error” on the web and you’ll realize it is difficult to find a clear definition of this kind of error that isn’t a discussion about error representations. Error representations are just value types so they’re not ultimately very interesting. They may be returned along separate return paths to non-errors or they may be combined with non-error types into composite entities like “sum” types – but they are still just values.

To better manage errors and test the functions that involve them, we need to look at what makes errors (not just their representations) unique. I’ll give a universal definition of an “error” and look at an increasing series of complications common to errors (“unexpected”, “composite”, “non-pure”, “external”) that make them much worse than typical values and look at the implications this has on testing and subsequent handling.

## Figure 1: a pure function

To begin, let’s look at a function that doesn’t produce an error or require any error handling.

![Figure 1: a pure function](https://www.cocoawithlove.com/assets/blog/errors1.svg)

This is the structure of a basic “pure” function. If you’re unfamiliar with functional programming technology:

> A [**pure function**](https://en.wikipedia.org/wiki/Pure_function) is one whose behavior depends only on its input arguments (the only data it reads must be read from its arguments) and doesn’t change program state (only temporary local variables and the “return” value may be written)

The function pre-processes arguments (the “prepare” step in the diagram), maps the input values onto output values in accordance with expected behavior (the “evaluate” step) and then packages and sends the output to the caller (the “return” step).

An example in Swift:

```swift
func multiplyU32toU64(a: UInt32, b: UInt32) -> UInt64 {
   let (x, y) = (UInt64(a), UInt64(b))
   let result = x * y
   return result
}
```

In this function, the first line is the “prepare” step (processing the arguments into the desired format), the second line is the “evaluate” step (performs the logic of the function) and the third line is the “return” step (sending the results of the “evaluate” step to the caller).

By design, this function has the same semantics (logical behavior) for all possible inputs. Due to the increase from 32 to 64 bits, there is no possibility of overflow and there is no other way to trigger a special valued output in this function; any two `Int32` values will produce an `Int64` that is the multiplicative product of the two.

## Figure 2: a piecewise function

![Figure 2: a piecewise function](https://www.cocoawithlove.com/assets/blog/errors2.svg)

This diagram represents another “pure” function. In some respects, it is simply a “zoom in” on the previous diagram – the “prepare” step has expanded into “check” and “partition” steps. The “evaluate” step has expanded into two possible “evaluate” steps (“A” and “B”) but otherwise, it’s the same overall structure.

The difference is that now, we have two different control-flow paths for the function, based on an analysis of the input.

An example in Swift:

```swift
func multiplyU32toU32(a: UInt32, b: UInt32) -> UInt32? {
   let result: UInt32?
   if log2(Double(a)) + log2(Double(b)) < 32 {
      result = a * b
   } else {
      result = nil
   }
   return result
}
```

This version of the multiply function guards against overflow by pre-checking the inputs and returning `nil` if it multiplication would overflow and only performing the multiplication if it would be safe.

The two different control-flow paths are reflected in the result which is a “sum” type – an `Optional` which may be either `nil` or a `UInt32`.

> A [**sum type**](https://en.wikipedia.org/wiki/Tagged_union) is a [composite](https://en.wikipedia.org/wiki/Composite_data_type) or [algebraic type](https://en.wikipedia.org/wiki/Algebraic_data_type) where instances must conform to one type from a set of possible types. In Swift, this is usually implemented as an `enum`, like `Optional`.

## Errors are expectation failures

The `multiplyU32toU32` function’s behavioral expectation is that it will apply a multiplication and return the result. However, the function has a code path and a return type that bypass that functionality entirely.

Depending on the value of input arguments, this function may fail to meet behavioral expectations. This leads us to the missing definition of an error:

> An **error** represents a failure to meet expectations (of arguments, state or other input) where those expectations are a predicate to meeting behavioral expectations (of the statement, function or program).

There are different kinds of error. I’ve previously discussed [_fatal_ errors](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html) which are failures of the programmer to meet expectations where the program chooses to abort rather than allow the behavioral expectations to fail.

In this article, we’re looking at _non-fatal_ errors. They still represent an expectation failure that prevents the typical behavioral expectations of the function being met however, instead of an abort, the function avoids returning its expected result and instead, a different value (which doesn’t depend on the failed expectation) is returned.

## Implications of errors

It’s a seemingly minor note but we don’t generally expect we will fail to meet our expectations.

While the `multiplyU32toU32` function has similar structure to the following function:

```swift
func absoluteValue(a: Int) -> Int {
   let result: Int
   if a < 0 {
      result = -a
   } else {
      result = a
   }
   return result
}
```

The difference is that with `absoluteValue`, we _expect_ we’ll need to test both paths equally.

When we call something an “error”, we’re expecting to _avoid_ the error wherever possible. For this reason, there’s an instinct to leave the error path relatively untested – we don’t expect it to occur as often. Even if this asymmetry of usage is true, it creates a higher risk for the less tested path.

It should be clear that testing the internals of both `multiplyU32toU32` and `absoluteValue` should follow the same pattern: both branches should be equally exercised by tests. The only reason you should apply less rigorous testing to a path is if its _implementation_ is much simpler.

Usage frequency should not be used to dictate testing thoroughness (unless the expected frequency is “never”, in which case: maybe the path shouldn’t exist at all).

## Impact of a composite type on the caller

Any composite type – like a sum type or an ad hoc equivalent that uses mutually exclusive separate values or even single scalars where different ranges reserved for communicating different behaviors – requires that the caller separate the different components and handle each appropriately. This requires either control flow constructs or functions that are aware of the nature of the composite.

Returning a sum type increases the complexity for the caller. Efficient language constructs and functions that are aware-by-design of the sum type will mitigate some of this complexity increase but a sum type will never be as simple as a continuous scalar type.

Swift has numerous language and library features for handling “sum” types (e.g. `switch` and `if let`) but this handling has a syntactic and mental overhead compared to non-sum type handling. There are other approaches that further reduce syntactic overhead by enclosing the actual handling inside the function (e.g. conditional unwrapping and `flatMap`) but even when the syntax is efficient, we must still consider the multiple behaviors that may be involves.

## Figure 3: a non-pure function

We’ve looked at “pure errors” but the majority of errors in imperative programming results from “non-pure” inputs.

To see what that means, let’s start with an error-free, non-pure function:

![Figure 1: a non-pure function](https://www.cocoawithlove.com/assets/blog/errors3.svg)

Structurally, it’s not much different to a pure function. The “prepare” is now a “fetch” stage – implying an action to bring data in from outside – but the purpose is the same: get the required arguments for the function. The difference is in the details:

```swift
func secondsSince(previous: Date) -> Double {
   let current = Date()
   let result = current.timeIntervalSince(date: previous)
   return result
}
```

Like the `multiply32to64` function under [“Figure 1”](#figure-1-a-pure-function), this function is an operation on two values. In this case however, while one of the operands (`previous`) is a function parameter, the other (`current`) pulls its value from the system clock inside the `Date` constructor. Since the clock is not a parameter to the function, this function is “non-pure”.

## Non-pure statements

Technically a function is only non-pure by extension. Non-pure is really the property of a single statement. Most of the `secondsSince` function is pure and it is only the fetching of the current date:

```swift
let current = Date()
```

that is non-pure. The diagram for “non-pure” could have been just the “fetch” step and nothing more. However, “non-pure” as a concept is not particularly interesting, it is the effect that non-pure dependencies have on our program that we want to consider – which is why it’s important to always look at what follows any “fetch” or “send”.

## Impact of non-pure functions on testing

Non-pure statements have implications for thread-safety, repeatability and determinism but in many cases, the biggest difficulty with non-pure functions is that they’re difficult to test.

In typical testing, we invoke a function with known arguments and test the result to ensure the function worked. With non-pure functions, controlling the arguments doesn’t control the function.

In the “non-pure” function diagram, how do we test the “evaluate” step is working correctly if we don’t know the exact value constructed during the “fetch” step?

We either need access to the other dependencies (sometimes singletons or other global state within our program can be pre-configured) or we need to be loose enough with our testing that guesses about the result will be true. In both cases, it adds complexity and reduces the robustness of testing.

Alternately, we can move dependencies to the other side of the function interface (a process called “dependency injection”) which can stop the function being non-pure but adds interface complexity and (since it adds an additional layer of indirection) can impede performance.

## Figure 4: a non-pure error

I’ve looked at “pure errors” and “non-pure functions”; no surprises that the next step is a non-pure error:

![Figure 1: a non-pure error](https://www.cocoawithlove.com/assets/blog/errors4.svg)

In most respects, it is a combination of a “pure error” and a “non-pure function”. There’s a “sum” return type, two paths through the function and a dependency that isn’t part of the invocation arguments.

Here’s a simple example:

```swift
var settings = Dictionary<String, String>()
func formattedName() -> String? {
   let result: String?
   if let firstName = settings["firstName"], secondName = settings["secondName"] {
      result = "\(secondName), \(firstName)"
   } else {
      result = nil
   }
   return result
}
```

Like the `multiplyU32toU32` function, above, which checked an expectation and returned an error value of `nil` when the expectation was not met, this function checks that the “firstName” and “secondName” keys are present in the `settings` and returns `nil` when they’re not.

This example isn’t very intimidating. The dependency is local (just a global variable in the same file) so its access can be viewed and controlled easily. It’s unlikely to return `nil` in surprising ways.

## External state

The most difficult to manage errors are those that depend on “external” state.

> **External state**, in this case, is state that doesn’t reside within your own process. It may mutate independently of your program, it may have behavior that is not fully declared and even when the behavior is broadly understood, the full complexity may be far beyond what a simple app wants to manage.

Consider the following function:

```swift
func sizeOfFile(path: String) throws -> Int {
   let attributes = try FileManager.default.attributesOfItem(atPath: path)
   let result = (attributes[FileAttributeKey.size] as? Int) ?? 0
   return result
}
```

This function attempts to get the size of a file at the specified path. It’s not a complicated idea. Looking at this function, consider the following questions:

- How many ways can an attempt to get the attributes of a file fail?
- The `attributesOfItem(atPath:)` documentation simply states that attributes will be present – does it mean _all_ attributes?
- Is it possible that `FileAttributeKey.size` will be missing from the attributes?
- Is returning `0` a sensible result (correct interpretation when `FileAttributeKey.size` is missing) or would a missing `FileAttributeKey.size` convey a different meaning?

Unless you have access to the Foundation source code and the source code of the filesystem, you might not be able to answer _any_ of these questions. Errors due to external state are a nightmare because there _aren’t_ clear answers. You can guess about likely errors and scenarios but it’s almost impossible to know.

## Conclusion

It shouldn’t be as difficult to find a definition for “error” as it is. It’s not a complicated concept: an error is a failed expectation, of an input or another dependency, that leads to a failure to deliver on behavioral expectations.

It’s the common traits of an error that make them so difficult to manage:

- composite (requiring handling of multiple possibilities)
- unexpected (skewing testing and design considerations)
- non-pure (dramatically increasing difficulty of testing)
- external (preventing control or clear definition)

I’ve attempted to keep the contents of this article as simple as possible, focussing on definitions and the implicit difficulties but avoiding significant discussion about error handling or how to manage difficulties.

I hope to refer back to this article in the future as I go through the different approaches used to manage errors, test error-prone functions, handle non-pure functions, handle externalities, reduce and hide complexity in error handling and use higher level abstractions to work with composite types in the same way as normal types.
