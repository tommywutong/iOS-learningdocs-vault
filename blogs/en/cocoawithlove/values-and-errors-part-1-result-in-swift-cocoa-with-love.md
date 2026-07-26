---
title: 'Values and errors, part 1: ''Result'' in Swift | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/08/21/result-types-part-one.html'
original_language: en
published: 2016-08-21
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:da81543e75281fde'
translated: false
---

> 原文：[Values and errors, part 1: 'Result' in Swift | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/08/21/result-types-part-one.html)　·　Cocoa with Love (Matt Gallagher)

Swift’s error handling has a major limitation: it can only be used to pass an error to an enclosing `catch` scope or the previous function on the stack.

If you want to handle errors across asynchronous boundaries or store value/error results for later processing, then Swift error handling won’t help. The best alternative is a common pattern called a `Result` type: it stores a value/error “sum” type (either one _or_ the other) and can be used between any two arbitrary execution contexts.

It’s an incredibly simple type but since the handling of value/error results sits a critical position in many types of operation, it provides an interesting look into the capabilities and priorities of a programming language. The `Result` type is so useful that it was _almost_ included in the Swift standard library and even its _rejection_ reveals an interesting look at the philosophies underpinning Swift’s design.

In this article, I’ll discuss the `Result` type in Swift as well as common variations in implementation and approach used for this data type. I’ll also look at _why_ the type was rejected for inclusion in the standard library and what effect that rejection is likely to have.

## A tagged union of success and failure

I’ve [previously talked about how errors](https://www.cocoawithlove.com/blog/2016/03/17/non-pure-errors.html#impact-of-a-composite-type-on-the-caller) are inherently “composite”: they represent a combination of multiple data paths or potential data values that are brought together to produce a single result that reflects the path taken and the state encountered. Within a larger operation, the results from multiple steps are composed to produce the final output.

If you’re familiar with Swift, then you know that Swift’s inbuilt error handling deals with the different paths associated with “success” and “failure” states by decorating functions with the `throws` keyword which allows them to have two separate exit paths: a `return` path for the normal value and a `throws` path for an `Error` type.

I’m sure you already know what Swift error handling looks like but here’s an example so I can refer back to it later:

```swift
// A simple function that returns the time since boot, if it is even
// otherwise throws an error
func evenTimeValue() throws -> UInt64 {
   switch mach_absolute_time() {
   case let t where t % 2 == 0: return t
   default: throw TimeError.expectedEvenGotOdd
   }
}

enum TimeError: Error { case expectedEvenGotOdd }

// Calling the function and handling the error
do {
   print(try evenTimeValue())
} catch {
   print(error)
}
```

The `evenTimeValue` result may return a `UInt64` or it may throw a `TimeError.expectedEvenGotOdd` error. This composite result is immediately decomposed in the `do` block by splitting into two paths, the `print(try evenTimeValue())` path and the `print(error)` path.

## The Result type

Swift’s error handling works to return value/error results to callers on the stack but it won’t pass value/error results in any other way. Examples of scenarios you might want to handle where Swift’s error handling won’t help include:

- results passed between threads
- results asynchronously delivered to the current thread
- results retained for any duration
- results passed into a function rather than out of a function.

Many of these alternate scenarios fall under the banner of [“continuation passing style”](https://en.wikipedia.org/wiki/Continuation-passing_style) (a design pattern where, instead of directly returning a result, functions invoke a provided “handler” function and pass the result into it). Work with Swift for long enough and you’re likely to use a continuation passing style eventually. Depending on the nature of your work, you might even need to store errors and other results.

The obvious candidate in these other scenarios is a `Result` type. Where Swift’s error handling encapsulates the composite nature of error handling by using “value” and “error” return paths from a function, a `Result` type embeds the “value” or “error” directly into a composite data type:

```swift
enum Result<Value> {
   case success(Value)
   case failure(Error)
}
```

Most `Result` implementations also offer `map` and `flatMap` methods, conversion to an optional value/error and conversion to/from a Swift `throws` function.

That’s about it; it’s a type that is better served by a narrow implementation.

## A Result example

Imagine our `evenTime()` function was computationally intensive and we wanted to invoke it outside the main queue. We might then need a callback function to report the result:

```swift
// A version of `evenTimeValue` that returns a `Result` instead of throwing
func evenTimeValue() -> Result<UInt64> {
   switch mach_absolute_time() {
   case let t where t % 2 == 0: return .success(t)
   default: return .failure(TimeError.expectedEvenGotOdd)
   }
}

// An async wrapper around `evenTime` that invokes a callback when complete
func asyncEvenTime(callback: @escaping (Result<UInt64>) -> Void) {
   DispatchQueue.global().async { callback(evenTimeValue()) }
}

// This is equivalent to the do/catch block labelled "Calling the
// function and handling the error" in the previous example
asyncEvenTime { timeResult in
   switch timeResult {
   case .success(let value): print(value)
   case .failure(let error): print(error)
   }
}
```

As in the Swift error handling example, the `asyncEvenTime` function may generate a `UInt64` or it may generate a `TimeError.expectedEvenGotOdd` error but in this case, the value or error is wrapped in a `.success` or `.failure` case of the `Result<UInt64>` and passed into the `callback` function. This `enum` is manually unwrapped and pattern matched by the `switch` statement, splitting into two paths, the `print(value)` path and the `print(error)` path.

Without language integration, the compiler doesn’t _force_ us to handle the `timeResult`. Otherwise, the effect is very similar: `Result` handling and Swift error handling process the same data flow in very similar ways.

## Using Result as a monad

Some people view a `Result` type as a functional programming construct that should be manipulated using `flatMap` calls. The `flatMap` function looks like this:

```swift
extension Result {
   func flatMap<U>(_ transform: (Value) -> Result<U>) -> Result<U> {
      switch self {
      case .success(let val): return transform(val)
      case .failure(let e): return .failure(e)
      }
   }
}
```

The intent of `flatMap` is to _avoid_ unwrapping the `Result` in your own code. Instead, you let the `flatMap` unwrap the `Result` and _if_ it happens to contain a `.success`, the `flatMap` function will invoke your code to process the `.success` value appropriately and pass it to the next stage in the processing pipeline, otherwise the `flatMap` function will short-circuit passed your processing function and instead pass the existing `.failure` error along to the next stage in the processing pipeline.

Types manipulated exclusively with `flatMap` (or functions implemented on top of `flatMap`) are called “monads”. By never accessing the contents directly and instead interacting through the “black box” of the `flatMap` function, your program avoids being dependent on the state of the value inside the monad. Since avoiding dependency on state is a key aim of functional programming, monads end up being a key pattern in functional programming.

It’s important to note though that Swift is _not_ a functional programming language and _I didn’t use_ `flatMap` in the `asyncEvenTime` example. The `Result` type was merely used as data transport with any logic applied either before wrapping the `Result` or after unwrapping at the end.

There are certainly situations where you might choose to use `Result` as a monad (I show an example in the [Comparing Result and Swift error handling](#comparing-result-and-swift-error-handling) section, below) but any such usage is not required. I personally think it’s appropriate to consider unwrapping with a `switch` statement as a _first_ option and consider more abstract functional operators as a _second_ option, only when they constitute a clear simplification.

## Specifying an error parameter

Some implementations of `Result` use a generic parameter for the error:

```swift
enum Result<Value, E: Error> {
   case success(Value)
   case failure(E)
}
```

There are some problems though with strongly typing errors like this in Swift. On the Swift Evolution mailing list, [John McCall offers some comments on the subject](https://lists.swift.org/pipermail/swift-evolution/Week-of-Mon-20151207/001450.html).

Basically, this approach would be fine if we could define a type as:

```swift
let result: Result<Value, FileError | NetworkError>
```

where the error is a “structural sum type” (a type that is either `FileError` or `NetworkError`) but we can’t do this in Swift at the moment.

Instead, we would need to manually define an enum each time:

```swift
enum ErrorFromMyFunction: Error {
   case file(FileError)
   case network(NetworkError)
}
```

That might not seem too bad but this then requires we manually wrap and unwrap error types as they occur inside our interface to get them into the correct container `enum`, since a manually constructed `enum` can’t be constructed from an unrelated error `enum` using `flatMap` or other composing functions.

Frankly, until Swift supports structural sum types (and there is no guarantee that it ever will), this can potentially involve a lot of manual work propagating errors to communicate a small amount of additional type information that the interface user will promptly ignore by treating all errors identically (bail out on any error).

## Comparing Result and Swift error handling

I’ve shown how you can use a `Result` for asynchronous callbacks but it’s worth considering how a `Result` would compare to Swift’s error handling if they were both used in the same “function return” scenario.

Consider a function that invokes the previous `evenTimeValue` function and adds a previously obtained `UInt64` value:

```swift
// Using Swift error handling:
func addToEvenTime(_ previous: UInt64) throws -> UInt64 {
   return try previous + evenTimeValue()
}

// Using a `Result` return type:
func addToEvenTime(_ previous: UInt64) -> Result<UInt64> {
   return evenTimeValue().map { previous + $0 }
}
```

I’m using `map` in the `Result` implementation to avoid unwrapping and rewrapping (`map` is a `flatMap` where the output from `transform` is always wrapped in a `.success`). Meanwhile, Swift’s error handling doesn’t require handling of wrapped values.

Now, let’s look at how Swift error handling and `Result` handling compare when chaining three calls to `addToEvenTime` together:

```swift
// Using Swift error handling:
func sumOfThreeEvenTimes() throws -> UInt64 {
   return try addToEvenTime(addToEvenTime(addToEvenTime(0)))
}

// Using a `Result` return type:
func sumOfThreeEvenTimes() -> Result<UInt64> {
   return addToEvenTime(0).flatMap(addToEvenTime).flatMap(addToEvenTime)
}
```

The comparison between these two approaches provides a good insight into Swift’s design philosophy. The _effect_ of Swift’s error handling over successive `throws` statements is equivalent to the monadic `flatMap` over multiple `Result` generating functions but Swift avoids making abstract mathematical concepts like `map` and `flatMap` a required part of the core language and instead makes the code _look_ as though it is a simple, linear sequence of actions.

As a counterpoint, `Result` is not really much more complicated, despite lacking any language integration. If you find a situation where Swift’s error handling is not practical, then switching to `Result` instead is relatively simple. If you use asynchronous workflows and other data-flow scenarios, then you might find `Result` is pratically required.

## In the standard library

Multiple people have suggested, via the Swift Evolution mailing list, that the Swift standard library should incorporate `Result`. At one point in time, the Swift development team themselves suggested a `Result` type might be added to the standard library to handle cases that Swift’s built-in error handling couldn’t cover (see [ErrorHandling.rst](https://github.com/apple/swift/blob/master/docs/ErrorHandling.rst#manual-propagation-and-manipulation-of-errors) in the docs directory of the Swift repository).

[John McCall explains the Swift standard library team’s verdict as follows](https://lists.swift.org/pipermail/swift-evolution/Week-of-Mon-20151207/001433.html):

> We considered it, had some specifics worked out, and then decided to put it on hold. Part of our reasoning was that it seemed more like an implementation detail of the async / CPS-conversion features we’d like to provide than an independently valuable feature, given that we don’t want to encourage people to write library interfaces using functional-style error handling instead of throws.

Ultimately, while a `Result` type _is_ useful in Swift, the Swift team would rather avoid directly endorsing alternatives to `throws` approach since it is not their first preference and they ultimately hope to extend the `throws` style handling to other scenarios.

The “async / CPS-conversion features” hinted at are the potential future [Swift “Concurrency” features that I’ve mentioned previously](https://www.cocoawithlove.com/blog/2016/06/02/threads-and-mutexes.html#future-concurrency-in-swift). Sadly though, no features will be delivered in this area [until after Swift 4](https://lists.swift.org/pipermail/swift-evolution/Week-of-Mon-20160725/025676.html).

## Implications of no Result type in the standard library

What are the implications of omitting a type from a standard library?

If a commonly used type is neither part of the standard library nor sourced from a single common repository, this results in two common problems:

1. Bloated code size due to replication
2. Interoperability between multiple independent implementations

Since a `Result` type is mostly just an `enum` definition, it may add some runtime type information to the executable but it won’t add to the actual code size. Methods that operate on the `Result` type do have measurable size but the most complicated extension you’re likely to need, `flatMap`, is just five lines. Even with a broad range of helper functions, a `Result` implementation should be less than 100 lines. It certainly isn’t a big code overhead on your project.

Interoperability between multiple independent implementations is a bigger concern but again, unlikely to become a major headache. The biggest reason for this is that any two implementations will always have a path through which they can be converted: Swift’s `throws` error handling.

Provided any two implementations contain the following two functions:

```swift
extension Result {
   // Construct a `Result` from a Swift `throws` error handling function
   public init(_ capturing: () throws -> Value) {
      do {
         self = .success(try capturing())
      } catch {
         self = .failure(error)
      }
   }

   // Convert the `Result` back to typical Swift `throws` error handling
   public func unwrap() throws -> Value {
      switch self {
      case .success(let v): return v
      case .failure(let e): throw e
      }
   }
}
```

then any two different definitions of `Result` from different modules could be converted as follows:

```swift
let firstResult: Module1.Result<Int> = someModule1Function()
let secondResult = Module2.Result<Int> { firstResult.unwrap() }
```

## Conclusion and usage

> A `Result` implementation can be found in the [CwlResult.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlResult.swift?ts=3) file of the [CwlUtils repository](https://github.com/mattgallagher/CwlUtils).

The [CwlResult.swift](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlResult.swift?ts=3) file has no dependencies and you can just use the file alone, if you wish. Of course, the implementation of a `Result` type is so mind numbingly simple that you might not even need to use someone else’s code – it’s just a two case `enum`, aferall.

Swift’s error handling doesn’t cover all error passing scenarios. Disappointing but not a disaster. If you need to handle value/error results in your code outside of passing results to the caller, there’s very little friction involved in switching to `Result` handling instead – they can both end up producing a very similar outcome.

I would absolutely prefer to see Swift’s error handling extended so it covers a wider range of common scenarios but I’ve been using a `Result` type to handle error passing in Swift since Swift’s first public betas and I’m not worried about the prospect of continuing to do so.

### Looking forward

“Asynchrony” is going to be a major focus of the next half dozen (or more) articles on Cocoa with Love. Passing around `Result` is a big part of making that work.

## Aside 1: Why then does the standard library include Optional?

It’s interesting to consider that where `Result` is rejected from the standard library, in favor of special language features and syntax, Swift contains a very similar type, `Optional` which looks like this:

```swift
enum Optional<Wrapped> {
   case some(Wrapped)
   case none
}
```

Both `Optional` and `Result` can be used to encapsulte the result of a function that may produce a result or fail. Both types can be processed via `map` and `flatMap` to handle the success case while short-circuiting the failure case.

In many ways, a `Result` is a _more_ powerful `Optional`. In the “not a value” case, a `Result` allows metadata about why the state occurred.

Interestingly, despite being less powerful, an `Optional` is more _useful_ because it is simpler. An `Optional` represents a basic toggle so it is well suited to representing basic boolean state (connected/disconnected, constructed/deleted, enabled/disabled, available/unavailable). Meanwhile `Result` is really constrained – by virtue of requiring `Error` metadata in `failure` cases – to being the output of an actual data flow.

## Aside 2: Either types

Another type, similar to `Result<Value>` that [was suggested for the Swift standard library](https://lists.swift.org/pipermail/swift-evolution/Week-of-Mon-20151207/001394.html) and [ultimately rejected](https://github.com/apple/swift-evolution/pull/67) was a biased `Either<Left, Right>` type that looks a little like this:

```swift
enum Either<Left, Right> {
   case left(Left)
   case right(Right)
}
```

If you consider a fully typed `Result<Value, ErrorType>` like this:

```swift
enum Result<Value, ErrorType> {
   case success(Value)
   case failure(ErrorType)
}
```

then a left-biased `Either` type can be considered a more general form of the same type.

The discussion on this topic revealed that the proposers of an `Either` type were most interested in capturing the “shape” of different potential abstract operations. I understand the intent but attempting to capture the “shape” of operations is difficult enough in single parameter, strictly functional languages like Haskell but in multi-parameter imperative languages like Swift, the number of possible operations grows with each additional parameter and once side effects are involved, it becomes immediately unmanageable.

It’s usually just easier to unwrap the `enum` when you need to operate on its contents, rather than relying on a large library of abstract and inefficient transformations.
