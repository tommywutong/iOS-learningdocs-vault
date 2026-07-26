---
title: 'Values and errors, part 2: eight languages compared | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/08/23/result-types-part-two.html'
original_language: en
published: 2016-08-23
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:c6d8ae1d2cb251b6'
translated: false
---

> 原文：[Values and errors, part 2: eight languages compared | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/08/23/result-types-part-two.html)　·　Cocoa with Love (Matt Gallagher)

I’m going to look at an error handling example implemented across a range of different languages studied by the Swift developers when designing Swift’s approach to error handling. By comparing these languages to Swift, I’ll try to better understand the balance of feature complexity, syntactic efficiency, abstraction, information signalling and safety that typical Swift code is expected to offer.

## Learning about languages via error handling

The [“Survey” section of the ErrorHandlingRationale](https://github.com/apple/swift/blob/master/docs/ErrorHandlingRationale.rst#survey) briefly discusses error propagation in C, C++, Objective-C, Java, C#, Haskell, Rust, Go and common scripting languages. Since I personally maintain professional projects in 5 of those languages (and I’ve written projects in most of the rest) the topic makes me reflect on the approaches I use for error handling in each language; whether I’m writing the best code I can, given the constraints and expected idioms of each language.

So I wanted to take a concrete look at error handling in the languages mentioned and see if I could learn more about those languages or more about Swift itself by directly comparing error handling approaches. Following the discussion from the [previous article](https://www.cocoawithlove.com/blog/2016/08/21/result-types-part-one.html), I want to ensure consideration of approaches beyond simple synchronous errors, so I will use an example that includes two different kinds of error routing:

1. Passing a value or recoverable error result from a function to its caller
2. Invoking a callback function, passing a value or error as an argument

Unlike the [ErrorHandlingRationale](https://github.com/apple/swift/blob/master/docs/ErrorHandlingRationale.rst) document:

- I will consider only common use recoverable errors
- I won’t be considering scope cleanup issues
- I’m not going to look at Go or any scripting languages since I don’t use them often enough to be insightful

## Swift

I’m going to start with a reference implementation in Swift. Assuming a `Result` type that includes a constructor from a Swift error handling `throws` function, as described in the [previous article](https://www.cocoawithlove.com/blog/2016/08/21/result-types-part-one.html#implications-of-no-result-type-in-the-standard-library), the example looks like this:

```swift
// A function with a synchronous error result (Swift error handling)
func evenTimeValue() throws -> UInt64 {
   switch mach_absolute_time() {
   case let t where t % 2 == 0: return t
   default: throw TimeError.expectedEvenGotOdd
   }
}

enum TimeError: Error { case expectedEvenGotOdd }

// A continuation passing style wrapper (Swift error handling to Result handling)
func cpsEvenTime(callback: (Result<UInt64>) -> Void) {
   callback(Result { try evenTimeValue() })
}

// This is the top level that invokes the continuation passing style wrapper
// around `evenTimeValue` and passes it a closure that ultimately processes the result 
cpsEvenTime { timeResult in
   switch timeResult {
   case .success(let value): print(value)
   case .failure(let error): print(error)
   }
}
```

> **Scorecard**: 16 lines (excluding blank lines and comments), 2 `switch` statements, 2 closures, 7 function calls. **Safety concerns**: No language support for `Result` means it is possible to accidentally ignore `timeResult`.

## C

Typical implementations use an `int` return to indicate “success” (often zero) or “failure” (often a non-zero error code) and return their results through an out-pointer:

```c
// Synchronous error result (int error code, result by out-pointer)
int evenTimeValue(unsigned long long *result) {
   unsigned long long t = mach_absolute_time();
   if (t % 2 == 0) {
      *result = t;
      return 0;
   } else {
      return 1;
   }
}

// Continuation passing style wrapper (code and value passed into function pointer)
void cpsEvenTime(void (*callback)(int, unsigned long long)) {
   unsigned long long t;
   int code = evenTimeValue(&t);
   callback(code, t);
}

// C has no anonymous functions (lambdas/closures) so the handler is a declared function
void handleResult(int code, unsigned long long t) {
   if (code == 0) {
      printf("%lld\n", t);
   } else {
      printf("failed\n");
   }
}

// Program entry point that invokes the continuation passing style wrapper
// around `evenTimeValue` and passes it a pointer to a function that ultimately processes
// the result 
int main(int argc, char **argv) {
   cpsEvenTime(handleResult);
   return 0;
}
```

> **Scorecard**: 25 lines (excluding blank lines and comments), 2 `if`/`else` statements, 1 function pointer, 1 out-pointer, 6 function calls. **Safety concerns**: No language support means it is possible to omit any check of the `code` and get an uninitialized `t` value.

### What does this tell us about C?

C aims to be simple by offering a minimal set of language features and relying on the programmer to understand problems like undefined behavior and avoid them. Good programming in C requires a simple and methodical approach. It’s possible to write abstractions in C but generally, programmers work in C because they want a raw pointer and the freedom to process things themselves, one byte at a time if necessary.

The reality is that C could get a little closer to the _spirit_ of the Swift implementation through its `union` type – which could encapsulate a value or error disjunction in a single data type but a manually tagged union is clumsy and adds layers of complexity with no additional safety. Ultimately, layers of abstraction like this conflict with a typical C design philosophy and are typically avoided. There’s a whole world of preprocessor hacks that attempt to make different design patterns like this manageable in C but that’s really just one leaky abstraction on top of another.

### What does this tell us about Swift?

Like C, Swift aspires to be simple, but Swift and C disagree on what simple is. Swift aims for simplicity by offering clear tools to solve common problems and minimizing the possibility of mistakes.

## Objective-C

In principal, Objective-C inherits C’s error handling, which is to say that it doesn’t have any language supported error handling. By convention though, Objective-C uses a slightly different style, returning an object pointer on success and `nil` on failure, plus an optional `NSError **` out parameter with details.

```objc
// It wouldn't be Objective-C without some boilerplate
@interface TimeSource: NSObject
@end

// And some file-scoped definitions
NSString * const TimeSourceErrorDomain = @"TimeSourceError";
NSInteger TimeSourceExpectedEvenGotOdd = 0;

@implementation TimeSource

// Synchronous error result (nil value means error, errorOut may be NULL)
+ (NSNumber *)evenTimeValueWithError:(NSError **)errorOut {
   uint64_t t = mach_absolute_time();
   if (t % 2 == 0) {
      return @(t);
   } else {
      if (errorOut) {
         *errorOut = [NSError
            errorWithDomain:TimeSourceErrorDomain
            code:TimeSourceExpectedEvenGotOdd
            userInfo:nil];
      }
      return nil;
   }
}

// Continuation passing style wrapper (code and value passed into block parameter)
+ (void)cpsEvenTime:(void (^)(NSNumber *, NSError *))callback {
   NSError *e;
   NSNumber *t = [self evenTimeValueWithError:&e];
   callback(t, e);
}

@end

// Program entry point that invokes the continuation passing style wrapper
// around `evenTimeValue` and passes it a closure that ultimately processes the
// result 
int main(int argc, char **argv) {
   [TimeSource cpsEvenTime: ^(NSNumber *t, NSError *e) {
      if (t) {
         printf("%s\n", [[t description] UTF8String]);
      } else {
         printf("%s\n", [[e localizedDescription] UTF8String]);
      }
   }];
   return 0;
}
```

> **Scorecard**: 32 lines (excluding blank lines and comments and unwrapping ), 2 `if`/`else` statements and an `if` statement, 1 closure, 1 out-pointer, 4 function calls, 7 method invocations. **Safety concerns**: It is possible to omit any check of the `t` value and get Objective-C’s no-op when messaging `nil` or worse, use the `nil` pointer where non-`nil` is required.

I’m fond of Objective-C but this example emphasizes a lot of its worst aspects. It’s verbose, full of structural boilerplate, over-reliant on heap allocations and while the “`nil` messaging is no-op” pattern (inherent in the `NSNumber *` result) reduce crashes in Objective-C versus C, it doesn’t guarantee correct behavior and may make problems harder to track down.

### What does this tell us about Objective-C?

Objective-C tries to handle most problems as object-oriented design problems but when that doesn’t work, it falls back to plain C. Composite value/error result handling falls outside basic object-oriented design so Objective-C offers little over C except some slightly more consistent standard patterns. However, some of those standard patterns in Objective-C involve some running around – this is a prime example.

### What does this tell us about Swift?

Objective-C’s standard approach for error handling was objectively mediocre. It was never obviously a focus of the langauge. While Swift inherits many ideas from Objective-C, error handling is _not_ among them.

When interoperating with Objective-C, all of this work may still occur but it’s such straightforward boilerplate that Swift can do it automatically.

## C++

This is tricky because there’s no universally used approach for error handling in C++.

Many of C++’s features are controversial. [I’ve previously discussed why many C++ programmers disable exceptions](https://www.cocoawithlove.com/blog/2016/05/01/swift-name-demangling.html#c-exceptions-versus-swift-error-handling). Some C++ programmers use compilers that don’t support lamdas. Others avoid templates for compile-time performance reasons or historical bugs in the template implementations of some compilers. Even where templates are used, some C++ programmers avoid large common libraries like “boost” due to poor compilation performance and lack of modularity.

The result is that there are hundreds of little sub-domains within C++ built around a specific subset of features, written as though all the other features of the language don’t exist – because they might not.

For handling disjunctions over value or error results, the following are used to varying degrees:

- Variations on C-style error handling (result code plus out-pointer).
- C++ exceptions
- Tagged unions using `boost::variant` (or `std::variant` in C++17)

I’m going to use the latter two, even though the first might be the most universal (I’ve already written a section in C for this article).

```cpp
#include <boost/variant.hpp>

// Synchronous error result (throws exception on error)
unsigned long long evenTimeValue() {
   uint64_t mach_absolute_time(void);
   unsigned long long t = mach_absolute_time();
   if (t % 2 == 0) {
      return t;
   } else {
      throw std::runtime_error("Expected even time, got odd");
   }
}

// Continuation passing style wrapper (error string or value in a tagged union)
void cpsEvenTime(const std::function<void(boost::variant<std::string, unsigned long long>)>
   &callback) {
   try {
      callback(evenTimeValue());
   } catch (std::exception &e) {
      callback(e.what());
   }
}

// Program entry point that invokes the continuation passing style wrapper
// around `evenTimeValue` and passes it a lambda that ultimately processes the
// result 
int main(int argc, char **argv) {
   cpsEvenTime([](boost::variant<std::string, unsigned long long> result){
      if (boost::get<unsigned long long>(&result)) {
         printf("%lld\n", boost::get<unsigned long long>(result));
      } else {
         printf("%s\n", boost::get<std::string>(result).c_str());
      }
   });
   return 0;
}
```

> **Scorecard**: 27 lines (ignoring blank lines and comments), 2 `if`/`else` statements, a `try`/`catch`, 1 potential `throw`, 1 lambda, 4 function calls, 13 function calls. **Safety concerns**: It is possible to omit the `try`/`catch` and have the exception propagate to a surrounding scope. You could also accidentally ignore the `result` or misapply the `boost::get` and trigger a runtime abort.

### What does this tell us about C++?

C++ incorporates many distinct philosophies. C-style programming is a common denominator for most – but not all. There’s usually a few tools to solve any problem but there’s no guarantee any of them will play well with your own style of C++.

C++ is typesafe and usually avoids pointers of any kind but that doesn’t mean it’s completely _robust_, since you can forget to catch an exception or use the wrong `boost::get` and trigger another exception or unwanted `abort` – there are lots of potential ways to accidentally trigger runtime errors (it’s difficult to avoid partial functions).

Additionally, despite a reputation for being a kitchen sink of every language feature, I needed to use `boost::variant` in the example, rather than a standard library feature or an actual inbuilt language feature to get a basic tagged union. C++17 will finally add this to the standard library but it’s still not as good as adding it to the language itself (it will still be prone to runtime, rather than compile-time type checking).

### What does this tell us about Swift?

Given that all of the Swift compiler developers are themselves C++ developers, it is interesting that Swift has turned out almost, but not quite, entirely unlike C++. While Swift’s error handling offers potentially similar control flow to C++ exceptions, C++ exceptions provided the clearest example of what the Swift developers wanted to avoid with Swift.

Swift would also rather solve problems with clear syntax rather than the numerous safe implementation rules required in C++. The `defer` syntax used to manage cleanup at scope exit, including around thrown errors, is an example of language syntax avoiding the need for safe implementation rules like [RAII](https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization).

## Haskell

Errors in Haskell are typically represented as an `Either`, `Maybe` or an `IO` monad type. In Haskell, the `flatMap` operation from Swift is called `bind` and it is typically invoked using the `>>=` operator (or implicitly handled using `do` notation).

Since Haskell is less likely to be well understood by readers of Cocoa with Love, I’ve thoroughly commented this code so if you can’t read the Haskell, you can at least read about what is happening here.

```haskell
import Data.Time.Clock.POSIX
import Control.Exception

-- ** A function with an IO monad wrapped Integer result **
-- Please excuse everything to the left of `getPOSIXTime` here; it's just to
-- generate a time value as an integer.
-- The actual test for even/odd occurs in the `evenOrFail` helper function
evenTimeValue = round . (* 1000000) <$> getPOSIXTime >>= evenOrFail

-- ** Pattern matching helper function with an IO monad wrapped Integer result **
-- Tests t for odd or even, triggering an error if it is odd
-- This function is intended to be used with a `>>=` operator since it
-- takes a bare value and returns an `IO` monad wrapped value
evenOrFail t
   | mod t 2 == 0 = return t
   | otherwise = fail "Expected even"

-- ** Continuation passing style wrapper around `evenTimeValue` (empty IO monad result) **
-- Passing the result from `evenTimeValue` into the callback `c` is effortless
-- since errors from functions and errors as parameters have the same monad
-- representation in Haskell
cpsEvenTime c = c evenTimeValue

-- ** Callback function (empty IO monad result) **
-- Processing the value occurs with another `>>=` operator. Processing
-- the error requires a `catch` and redirect to the `onError` handler
callback t = (t >>= print) `catch` onError

-- ** Error handling helper function (empty IO monad result) **
-- Separate error handling function
onError :: IOError -> IO ()
onError e = print ("Error: " ++ show (e))

-- ** Invoke everything at the top level (has an implicit empty IO monad result) **
main = cpsEvenTime callback
```

> **Scorecard**: 11 lines (ignoring blank lines and comments), 1 pattern match, 2 bind operators, 1 `catch`, 6 different symbolic operators. **Safety concerns**: It is possible to accidentally omit the `catch` and have the error bubble, like a fatal exception, all the way to the top level.

### What does this tell us about Haskell?

Ignoring the bulk added by the comments, this code is quite compact. It’s not exactly simpler or doing less than the Swift example, rather, Haskell avoids braces and makes heavy use of symbolic operators so it crams a lot of work into a small space.

Haskell’s error handling is fundamentally anchored in monads. Often these are “one-way” monads (where you can never pattern match and unwrap, you can only bind or catch to process the possible cases).

Haskell has many good aspects when it comes to code correctness and error handling:

- memory safe programming language
- fewer [partial functions](https://www.cocoawithlove.com/blog/2016/01/25/partial-functions-part-one-avoidance.html) than common imperative languages so you’re less unlikely to see exceptions/aborts
- no force unwrapping or other cheating

However, Haskell’s approach to error handling does have some limitations. Specifically, monadic handling makes it very easy to “bind” (`>>=`) to get the “success” result and totally ignore what happens in an error case. Monadic handling encourages the ignoring of errors. If this code had omitted the `catch` handling, the `IO` monad would have propagated all the way to the output of the `main` function.

There’s also an almost total lack of signalling. Unless you look for the bind operator, `do` notation or the `catch`, `return` or `fail` functions, it’s difficult to know where `IO` or other monads are involved. Haskell’s pervasive type inferencing is often a hindrance here: only one of these functions is required to actually specify a type signature.

### What does this tell us about Swift?

Swift’s `do` and `Result` handling have a lot in common with Haskell’s `do` and monads. The difference is that Swift avoids wrapping your data types and therefore allows you to manage the data flow without any wrappers or abstractions.

While downplaying abstractions, Swift plays _up_ control flow and signalling of potential actions with keywords like `try` for signalling the existince of error handling in a statement where equivalent handling in Haskell may be subtler to detect.

## Java

Java includes the closest parallel to Swift’s inbuilt error handling with its “checked exceptions”. Like Swift’s `throws`, the possibility of throwing is part of a function’s signature and may not be ignored by the caller.

```java
import java.io.IOException;
import java.util.function.BiConsumer;

public class TimeSource {
   // A function with declared "checked" exception
   public static long evenTimeValue() throws IOException {
      long t = System.currentTimeMillis();
      if (t % 2 == 0) {
         return t;
      } else {
         throw new IOException("Expected even, got odd");
      }
   }
   
   // A continuation passing style wrapper (passing value and error arguments)
   public static void cpsEvenTime(BiConsumer<IOException, Long> callback) {
      try {
         callback.accept(null, new Long(evenTimeValue()));
      } catch (IOException e) {
         callback.accept(e, null);
      }
   }

   // Program entry point that invokes the continuation passing style wrapper
   // around `evenTimeValue` and passes it a lambda that ultimately processes the
   // result 
   public static void main(String[] args) {
      TimeSource.cpsEvenTime((error, time) -> {
         if (error != null) {
            System.out.println(error.getMessage());
         } else {
            System.out.println(time);
         }
      });
   }
}
```

> **Scorecard**: 28 lines (ignoring blank lines and comments), 2 `if`/`else` statements, a `try`/`catch`, 1 potential `throw`, 1 lambda, 10 methods. **Safety concerns**: It is possible to forget to check the `error` for `null` and use an invalid value.

### What does this tell us about Java?

In this example, Java’s use of `throws`, `throw` and `catch` closely resemble Swift’s matching keywords. However, while methods that throw “checked exceptions” are always marked, sites that _use_ these functions are not marked – if the `IOException` had been generated inside a function, there would not need to be any mention of that in this source code.

Negatives of the approach for common error handling include:

1. In Java, the exception types thrown must be fully enumerated – a difference that is sometimes an advantage and sometimes a burden. I’ll look at the problems this causes [in the C# section, below](#c-2).
2. Java’s `Exception` class captures a full stack trace and other information, which, along with allocation overhead and exception hander overhead, [makes it 60 times slower than returning an error code](http://stackoverflow.com/questions/299068/how-slow-are-java-exceptions)
3. The name “exception” leads to reasonable questions about whether it should be regularly used or used only in exceptional circumstances.

Ignoring poor performance, the biggest problem affecting Java’s checked exceptions is the existence of “unchecked exceptions”. While checked exceptions are usable for common errors, unchecked exceptions are absolutely for exceptional circumstances (programmer errors which should lead to an abort). Despite the fact that they should be a rarer choice, unchecked exceptions are actually easier to use, since they don’t need to be declared.

Ultimately, declaration issues, performance issues and confusion with programmer errors lead to a signficantly compromised language feature.

### What does this tell us about Swift?

While Swift has copied some of the syntactic elements of checked exceptions, Swift is very careful to avoid calling its errors “exceptions” since they are different in important ways. Most significantly, Swift’s errors are as performant as returning an error code and have no overlap with technology intended for fatal errors.

Good performance and clear separation of concerns are important goals of Swift.

## C#

I doubt it would be new information to anyone here but C#’s syntax is very similar to Java to the point where you can’t always immediately tell one from the other.

```csharp
using System;

namespace TimeSourceApplication {
   class TimeSource {
       // A function that might throw an exception
       public static long evenTimeValue() {
          long t = System.DateTime.Now.Millisecond;
          if (t % 2 == 0) {
             return t;
          } else {
             throw new System.Exception("Expected even, got odd.");
          }
       }
   
       // A continuation passing style wrapper (passing value and error arguments)
       public static void cpsEvenTime(Action<System.Exception, long> callback) {
          try {
             callback(null, evenTimeValue());
          } catch (System.Exception e) {
             callback(e, 0);
          }
       }

      // Program entry point that invokes the continuation passing style wrapper
      // around `evenTimeValue` and passes it a lambda that ultimately processes the
      // result 
      public static void Main(string[] args) {
          TimeSource.cpsEvenTime((error, time) => {
             if (error != null) {
                System.Console.WriteLine(error.Message);
             } else {
                System.Console.WriteLine(time);
             }
          });
       }
   }
}
```

> **Scorecard**: 29 lines (ignoring blank lines and comments), 2 `if`/`else` statements, a `try`/`catch`, 1 potential `throw`, 1 lambda, 9 methods (including a getter). **Safety concerns**: You could accidentally omit the `try`/`catch` and have the exception propagate to the surrounding scope. It is also possible to forget to check the `error` for `null` and use an invalid value.

### What does this tell us about C#?

On the topic of error handling, C# explicitly rejected Java’s checked exceptions in favor of unchecked exceptions.

[Anders Hejlsberg, creator of C#, spoke about why checked exceptions were not included in C# in an interview in 2003](http://www.artima.com/intv/handcuffs.html):

> Adding a new exception to a throws clause in a new version breaks client code. It’s like adding a method to an interface. After you publish an interface, it is for all practical purposes immutable, because any implementation of it might have the methods that you want to add in the next version. So you’ve got to create a new interface instead. Similarly with exceptions, you would either have to create a whole new method called foo2 that throws more exceptions, or you would have to catch exception D in the new foo, and transform the D into an A, B, or C.

and he further states:

> The trouble begins when you start building big systems where you’re talking to four or five different subsystems. Each subsystem throws four to ten exceptions. Now, each time you walk up the ladder of aggregation, you have this exponential hierarchy below you of exceptions you have to deal with. You end up having to declare 40 exceptions that you might throw. And once you aggregate that with another subsystem you’ve got 80 exceptions in your throws clause. It just balloons out of control.

The problem, as he sees it, is Java requires you explicitly enumerate every kind of exception that can be thrown. This is in contrast to Swift which simply says: “an error may be thrown” and makes matching error types a runtime concern.

### What does this tell us about Swift?

The interesting point here then is that Swift has taken an approach closer to _checked_ exceptions than C#’s _unchecked_ exceptions. Swift addresses Anders Hejlsberg’s concerns about checked exceptions by removing the need to declare exception types but keeping the explicit use of the `throws` keyword.

Swift wants code that is easy to reason about accurately. Unmarked exceptions (i.e. no visible `try` or `throws` keyword in every function traversed) does not fit this desire.

## Rust

Rust and Swift are both products of modern programming language design and include similar aims (no null pointers, no undefined behavior and no memory unsafety outside of clearly identified “unsafe”). Each has borrowed ideas from the same sources and each has borrowed from the other. The two are very different when it comes to level of programmer involvement in managing ideas like reference ownership but even on this level, there’s evidence that [Swift may move a little closer to Rust](https://lists.swift.org/pipermail/swift-evolution/Week-of-Mon-20160725/025676.html) in the future.

```rust
// A function with a synchronous error (Result return type)
fn even_time_value() -> Result<u64, TimeSourceError> {
    match try!(std::time::UNIX_EPOCH.elapsed()).as_secs() {
       t if t % 2 == 0 => Ok(t),
       _ => Err(TimeSourceError::ExpectedEvenGotOdd),
   }
}

// An error type that includes cases for our generated error and a possible underlying
// system error
#[derive(Debug)]
enum TimeSourceError {
   ExpectedEvenGotOdd,
   SystemTimeError(std::time::SystemTimeError)
}

// Helper function that re-wraps SystemTimeError as TimeSourceError (used in try!, above)
impl From<std::time::SystemTimeError> for TimeSourceError {
    fn from(err: std::time::SystemTimeError) -> Self {
        TimeSourceError::SystemTimeError(err)
    }
}

// A continuation passing style wrapper (Result passed as argument)
fn cps_even_time_value<F>(callback: F) where F: Fn(Result<u64, TimeSourceError>) {
   callback(even_time_value());
}

// Program entry point that invokes the continuation passing style wrapper
// around `evenTimeValue` and passes it a lambda that ultimately processes the
// result 
fn main() {
   cps_even_time_value(|r|
      match r {
         Ok(v) => println!("{:?}", v),
         Err(e) => println!("{:?}", e)
      }
   );
}
```

> **Scorecard**: 27 lines (excluding blank lines and comments), 2 `match` statements, 1 closure, 3 macros, 4 function calls. **Safety concerns**: None.

### What does this tell us about Rust?

Rust prides itself on being precise and opinionated. Precise reference ownership semantics, precise error typing, even debug printing is unavailable unless specifically requested (in this case, with the `derive(Debug)` attribute). This is also the only example where I’ve altered the naming scheme to match the language since `evenTimeValue` gave a compiler warning: “function `evenTimeValue` should have a snake case name such as `even_time_value`”.

In accordance with the focus on being precise, Rust includes no automatic error propagation. Instead, you are merely forbidden (via the compiler attribute `#[must_use]`) from completely ignoring the `Result`. Beyond that, the behavior or propagation is completely manual.

However, Rust’s macro system offers some tricks that smooth over the handling to the point where it almost looks like Swift’s error handling. Specifically, the `try!` macro (the exclamation mark indicates a macro, not a force unwrap like Swift) expands to checking for an error, exiting early from the function if an error occurs and only proceeding if it gets a success. Since the `Err` case of the `Result` is handled by this macro, the output of the `try!` macro has the type of the `Ok` case, `u64`, rather than a `Result` wrapped type.

The effect is very similar to how Swift’s error handling works inside a `throws` function but there’s a complication: the fully typed errors used by Rust’s `Result` type don’t automatically compose like Swift’s `Error` protocol does. Instead, [composing custom error types in Rust](https://doc.rust-lang.org/book/error-handling.html#composing-custom-error-types) requires that we convert the underlying error to the appropriate type – which we do in this case with an implementation of the `From` trait (which is called from inside the `try!` macro to allow conversion).

### What does this tell us about Swift?

Swift is less focussed on precision and control than Rust. Swift is happy to have errors fall under a single broad protocol (rather than precisely enumerating all possible sub-error types) to allow a smoother experience.

Swift is also happy to include compiler automated behaviors like propagation, provided there is clear signalling of possible behaviors. With the Rust `try!` macro in this example, the effect was very similar but Swift’s approach will also work over successive `try` statements in a `do` scope within a single function (the Rust `try!` macro works only when it can exit from the current function).

## Conclusion

Swift’s error handling is probably my favorite feature in the language because of the improvements it offers over alternatives while remaining familiar, simple to use and easy to reason about.

However, I’m not exclusively a Swift programmer. I continue to program in other languages so I feel like there are also lessons from this investigation that I could apply back to some of the other languages I use.

In particular, I feel like I should experiment with `Result` types in C++, Java and C# to avoid problems with exceptions or the problems with using separate error codes and values. The generics/templates and lambdas in these languages are certainly capable of cleanly expressing this pattern. I do already use `boost::variant` in my C++ code but it’s prone to accidental `boost::get` misuse and lacks transformations for composing errors – a dedicated `Result` type would be better.

For the other languages in this post, while I prefer Swift’s error handling, the error handling approaches match the philosophy of the respective languages. Rust’s `Result` type is safe, precise and avoids compiler inserted sugar while offering similar syntax in many cases to Swift’s error handling. Haskell’s error handling – and the possibilites afforded by monads and higher kinded types – is practically a religion for its adherents. Even C’s approach (language does nothing, language user coordinates everything) could be considered appropriate for the language.

### Looking forward

Writing code in multiple languages is mostly playing around. However, there’s lots of ideas to borrow from all of the languages here. A number of design patterns that I hope to present in future articles have come to me via implementations in the languages here.
