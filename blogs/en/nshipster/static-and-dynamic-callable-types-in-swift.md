---
title: Static and Dynamic Callable Types in Swift
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/callable/'
original_language: en
published: 2020-02-12
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:f8706d1c8e310ec4'
translated: false
---

> 原文：[Static and Dynamic Callable Types in Swift](https://nshipster.com/callable/)　·　NSHipster (Mattt)

# [Static and Dynamic Callable Types in Swift](https://nshipster.com/callable/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  February 12^th, 2020

Last week, Apple released the [first beta of Xcode 11.4](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_4_beta_release_notes), and it’s proving to be one of the most substantial updates in recent memory. `XCTest` got [a huge boost](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_4_beta_release_notes#3530390), with numerous quality of life improvements, and [Simulator](https://developer.apple.com/documentation/xcode_release_notes/xcode_11_4_beta_release_notes#3530393), likewise, got a solid dose of TLC. But it’s the changes to Swift that are getting the lion’s share of attention.

In Xcode 11.4, Swift compile times are down across the board, with many developers reporting improvements of 10 – 20% in their projects. And thanks to a [new diagnostics architecture](https://swift.org/blog/new-diagnostic-arch-overview/), error messages from the compiler are consistently more helpful. This is also the first version of Xcode to ship with the new [`sourcekit-lsp` server](https://nshipster.com/language-server-protocol/), which serves to empower editors like [VSCode](https://nshipster.com/vscode/) to work with Swift in a more meaningful way.

Yet, despite all of these improvements (which are truly an incredible achievement by Apple’s Developer Tools team), much of the early feedback has focused on the most visible additions to Swift 5.2. And the response from the peanut galleries of Twitter, Hacker News, and Reddit has been — to put it charitably — _“mixed”_.

---

If like most of us, you aren’t tuned into the comings-and-goings of [Swift Evolution](https://apple.github.io/swift-evolution/), Xcode 11.4 was your first exposure to two new additions to the language: [key path expressions as functions](https://github.com/apple/swift-evolution/blob/master/proposals/0249-key-path-literal-function-expressions.md) and [callable values of user-defined nominal types](https://github.com/apple/swift-evolution/blob/master/proposals/0253-callable.md).

The first of these allows key paths to replace one-off closures used by functions like `map`:

```
// Swift >= 5.2
"🧁🍭🍦".unicodeScalars.map(\.properties.name)
// ["CUPCAKE", "LOLLIPOP", "SOFT ICE CREAM"]

// Swift <5.2 equivalent
"🧁🍭🍦".unicodeScalars.map { $0.properties.name }
```

The second allows instances of types with a method named `callAsFunction` to be called as if they were a function:

```
struct Sweetener {
    let additives: Set<Character>

    init<S>(_ sequence: S) where S: Sequence, S.Element == Character {
        self.additives = Set(sequence)
    }

    func callAsFunction(_ message: String) -> String {
        message.split(separator: " ")
               .flatMap { [$0, "\(additives.randomElement()!)"] }
               .joined(separator: " ") + "😋"
    }
}

let dessertify = Sweetener("🧁🍭🍦")
dessertify("Hello, world!")
// "Hello, 🍭 world! 🍦😋"
```

---

Granted, both of those examples are terrible. And that’s kinda the problem.

---

Too often, coverage of _“What’s New In Swift”_ amounts to little more than a regurgitation of Swift Evolution proposals, interspersed with poorly motivated (and often emoji-laden) examples. Such treatments provide a poor characterization of Swift language features, and — in the case of Swift 5.2 — serves to feed into the popular critique that these are frivolous additions — mere [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar).

This week, we hope to reach the ooey gooey center of the issue by providing some historical and theoretical context for understanding these new features.

## Syntactic Sugar in Swift

If you’re salty about “key path as function” being too sugary, recall that the status quo isn’t without a sweet tooth. Consider our saccharine example from before:

```
"🧁🍭🍦".unicodeScalars.map { $0.properties.name }
```

That expression relies on at least four different syntactic concessions:

1. **Trailing closure syntax**, which allows a final closure argument label of a function to be omitted
2. **Anonymous closure arguments**, which allow arguments in closures to be used positionally (`$0`, `$1`, …) without binding to a named variable.
3. **Inferred parameter and return value types**
4. **Implicit return from single-expression closures**

If you wanted to cut sugar out of your diet completely, you’d best get [Mavis Beacon](https://en.wikipedia.org/wiki/Mavis_Beacon_Teaches_Typing) on the line, because you’ll be doing a lot more [typing](https://nshipster.com/rawrepresentable/).

```
"🧁🍭🍦".unicodeScalars.map(transform: { (unicodeScalar: Unicode.Scalar) -> String in
    return unicodeScalar.properties.name
})
```

In fact, as we’ll see in the examples to come, Swift is a marshmallow world in the winter, _syntactically speaking_. From initializers and method calls to optionals and method chaining, nearly everything about Swift could be described as a cotton candy melody — it really just depends on where you draw the line between “language feature” and “syntactic sugar”.

---

To understand why, you have to understand how we got here in the first place, which requires a bit of history, math, and computer science. Get ready to eat your vegetables 🥦.

## The λ-Calculus and Speculative Computer Science Fiction

All programming languages can be seen as various attempts to represent [the λ-calculus](https://en.wikipedia.org/wiki/Lambda_calculus). Everything you need to write code — variables, binding, application — it’s all in there, buried under a mass of Greek letters and mathematical notation.

Setting aside syntactic differences, each programming language can be understood by its combination of affordances for making programs easier to write and easier to read. Language features like objects, classes, modules, optionals, literals, and generics are all just abstractions built on top of the λ-calculus.

Any other deviation from pure mathematical formalism can be ascribed to real-world constraints, such as [a typewriter from the 1870s](https://en.wikipedia.org/wiki/QWERTY), [a punch card from the 1920s](https://en.wikipedia.org/wiki/Punched_card#IBM_80-column_punched_card_format_and_character_codes), [a computer architecture from the 1940s](https://en.wikipedia.org/wiki/Von_Neumann_architecture), or [a character encoding from the 1960s](https://en.wikipedia.org/wiki/ASCII).

Among the earliest programming languages were Lisp, ALGOL*, and COBOL, from which nearly every other language derives.

```
(defun square (x)
    (* x x))

(print (square 4)) 
;; 16
```

```
pure function square(x)
  integer, intent(in) :: x
  integer :: square
  square = x * x
end function

program main
  integer :: square
  print *, square(4)
end program main
! 16
```

```
IDENTIFICATION DIVISION.
       PROGRAM-ID. example.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  x   PIC 9(3) VALUE 4.
       01  y   PIC 9(9).
       PROCEDURE DIVISION.
           CALL "square" USING
               BY CONTENT x
               BY REFERENCE y.
           DISPLAY y.
           STOP RUN.
       END PROGRAM example.

IDENTIFICATION DIVISION.
       PROGRAM-ID. square.
       DATA DIVISION.
       LINKAGE SECTION.
       01  x   PIC 9(3).
       01  y   PIC 9(3).
       PROCEDURE DIVISION USING x, y.
           MULTIPLY x BY x GIVING y.
           EXIT PROGRAM.
       END PROGRAM square.
* 016000000
```

Here you get a glimpse into three very different timelines; ours is the reality in which ALGOL’s syntax (option #2) “won out” over the alternatives. From ALGOL 60, you can draw a straight line from [CPL](https://en.wikipedia.org/wiki/CPL_(programming_language)) in 1963, to [BCPL](https://en.wikipedia.org/wiki/BCPL) in 1967 and [C](https://en.wikipedia.org/wiki/C_(programming_language)) in 1972, followed by [Objective-C in 1984](https://nshipster.com/direct/#object-oriented-programming) and Swift in 2014. That’s the lineage that informs what types are callable and how we call them.

---

_Now, back to Swift…_

## Function Types in Swift

Functions are first-class objects in Swift, meaning that they can be assigned to variables, stored in properties, and passed as arguments or returned as values from other functions.

What distinguishes function types from other values is that they’re callable, meaning that you can invoke them to produce new values.

### Closures

Swift’s fundamental function type is the closure, a self-contained unit of functionality.

```
let square: (Int) -> Int = { x in x * x }
```

As a function type, you can call a closure by passing the requisite number of arguments between opening and closing parentheses `()` — _a la_ ALGOL.

```
square(4) // 16
```

Closures are so called because they close over and capture references to any variables from the context in which they’re defined. However, capturing semantics aren’t always desirable, which is why Swift provides dedicated syntax to a special kind of closure known as a function.

### Functions

Functions defined at a top-level / global scope are named closures that don’t capture any values. In Swift, you declare them with the `func` keyword:

```
func square(_ x: Int) -> Int { x * x }
square(4) // 16
```

Compared to closures, functions have greater flexibility in how arguments are passed.

Function arguments can have named labels instead of a closure’s unlabeled, positional arguments — which goes a long way to clarify the effect of code at its call site:

```
func deposit(amount: Decimal,
             from source: Account,
             to destination: Account) throws { … }
try deposit(amount: 1000.00, from: checking, to: savings)
```

Functions can be [generic](https://docs.swift.org/swift-book/LanguageGuide/Generics.html), allowing them to be used for multiple types of arguments:

```
func square<T: Numeric>(_ x: T) -> T { x * x }
func increment<T: Numeric>(_ x: T) -> T { x + 1 }
func compose<T>(_ f: @escaping (T) -> T, _ g: @escaping (T) -> T) -> (T) -> T {
    { x in g(f(x)) }
}

compose(increment, square)(4 as Int) // 25 ((4 + 1)²)
compose(increment, square)(4.2 as Double) // 27.04 ((4.2 + 1)²)
```

Functions can also take variadic arguments, implicit closures, and default argument values (allowing for magic expression literals like `#file` and `#line`):

```
func print(items: Any...) { … }

func assert(_ condition: @autoclosure () -> Bool,
            _ message: @autoclosure () -> String = String(),
            file: StaticString = #file,
            line: UInt = #line) { … }
```

And yet, despite all of this flexibility for accepting arguments, most functions you’ll encounter operate on an _implicit_ `self` argument. These functions are called methods.

### Methods

A method is a function contained by a type. Methods automatically provide access to `self`, allowing them to effectively capture the instance on which they’re called as an implicit argument.

```
struct Queue<Element> {
    private var elements: [Element] = []

    mutating func push(_ newElement: Element) {
        self.elements.append(newElement)
    }

    mutating func pop() -> Element? {
        guard !self.elements.isEmpty else { return nil }
        return self.elements.removeFirst()
    }
}
```

---

Putting everything together, these syntactic affordances allow Swift code to be expressive, clear, and concise:

```
var queue = Queue<Int>()
queue.push(1)
queue.push(2)
queue.pop() // 1
```

Compared to more verbose languages like Objective-C, the experience of writing Swift is, well, pretty _sweet_. It’s hard to imagine any Swift developers objecting to what we have here as being “sugar-coated”.

But like a 16oz can of [Surge](https://en.wikipedia.org/wiki/Surge_(drink)), the sugar content of something is often surprising. Turns out, that example from before is far from innocent:

```
var queue = Queue<Int>() // desugars to `Queue<Int>.init()`
queue.push(1) // desugars to `Queue.push(&queue)(1)`
```

All this time, our so-called “direct” calls to methods and initializers were actually shorthand for ~~[function currying](https://en.wikipedia.org/wiki/Currying)~~ [partially-applied functions](https://en.wikipedia.org/wiki/Partial_application).

With this in mind, let’s now take another look at callable types in Swift more generally.

## {Type, Instance, Member} ⨯ {Static, Dynamic}

Since their introduction in Swift 4.2 and Swift 5, respectively, many developers have had a hard time keeping `@dynamicMemberLookup` and `@dynamicCallable` straight in their minds — made even more difficult by the introduction of `callAsFunction` in Swift 5.2.

If you’re also confused, we think the following table can help clear things up:

|  | Static | Dynamic |
|---|---|---|
| Type | `init` | _N/A_ |
| Instance | **`callAsFunction`** | **`@dynamicCallable`** |
| Member | `func` | **`@dynamicMemberLookup`** |

Swift has always had static callable types and type members. What’s changed in new versions of Swift is that instances are now callable, and both instances and members can now be called dynamically.

Let’s see what that means in practice, starting with static callables.

### Static Callable

```
struct Static {
    init() {}

    func callAsFunction() {}

    static func function() {}
    func function() {}
}
```

This type can be called statically in the following ways:

```
let instance = Static() // ❶ desugars to `Static.init()`

Static.function() // ❷ (no syntactic sugar!)
instance.function() // ❸ desugars to Static.function(instance)()

instance() // ❹ desugars to `Static.callAsFunction(instance)()`
```

❶ Calling the `Static` type invokes an initializer ❷ Calling `function` on the `Static` type invokes the corresponding static function member, passing `Static` as an implicit `self` argument. ❸ Calling `function` on an instance of `Static` invokes the corresponding function member, passing the instance as an implicit `self` argument. ❹ Calling an instance of `Static` invokes the `callAsFunction()` function member, passing the instance as an implicit `self` argument.

### Dynamic Callable

```
@dynamicCallable
@dynamicMemberLookup
struct Dynamic {
    func dynamicallyCall(withArguments args: [Int]) -> Void { () }
    func dynamicallyCall(withKeywordArguments args: KeyValuePairs<String, Int>) -> Void { () }

    static subscript(dynamicMember member: String) -> (Int) -> Void { { _ in } }
    subscript(dynamicMember member: String) -> (Int) -> Void { { _ in } }
}
```

This type can be called dynamically in a few different ways:

```
let instance = Dynamic() // desugars to `Dynamic.init()`

instance(1) // ❶ desugars to `Dynamic.dynamicallyCall(instance)(withArguments: [1])`
instance(a: 1) // ❷ desugars to `Dynamic.dynamicallyCall(instance)(withKeywordArguments: ["a": 1])`

Dynamic.function(1) // ❸ desugars to `Dynamic[dynamicMember: "function"](1)`
instance.function(1) // ❹ desugars to `instance[dynamicMember: "function"](1)`
```

❶ Calling an instance of `Dynamic` invokes the `dynamicallyCall(withArguments:)` method, passing an array of arguments and `Dynamic` as an implicit `self` argument. ❷ Calling an instance of `Dynamic` with at least one labeled argument invokes the `dynamicallyCall(withKeywordArguments:)` method, passing the arguments in a [`KeyValuePairs` object](https://nshipster.com/keyvaluepairs/) and `Dynamic` as an implicit `self` argument. ❸ Calling `function` on the `Dynamic` type invokes the static `dynamicMember` subscript, passing `"function"` as the key; here, we call the returned anonymous closure. ❹ Calling `function` on an instance of `Dynamic` invokes the `dynamicMember` subscript, passing `"function"` as the key; here, we call the returned anonymous closure.

#### Dynamism by Declaration Attributes

`@dynamicCallable` and `@dynamicMemberLookup` are declaration attributes, which means that they can’t be applied to existing declarations through an extension.

So you can’t, for example, _spice up_ `Int` with [Ruby-ish](https://github.com/rails/rails/blob/master/activesupport/lib/active_support/core_ext/array/access.r) natural language accessors:

```
@dynamicMemberLookup // ⚠︎ Error: '@dynamicMemberLookup' attribute cannot be applied to this declaration
extension Int {
    static subscript(dynamicMember member: String) -> Int? {
        let string = member.replacingOccurrences(of: "_", with: "-")

        let formatter = NumberFormatter()
        formatter.numberStyle = .spellOut
        return formatter.number(from: string)?.intValue
    }
}

// ⚠︎ Error: Just to be super clear, this doesn't work
Int.forty_two // 42 (hypothetically, if we could apply `@dynamicMemberLookup` in an extension)
```

Contrast this with `callAsFunction`, which can be added to any type in an extension.

---

There’s much more to talk about with `@dynamicMemberLookup`, `@dynamicCallable`, and `callAsFunction`, and we look forward to covering them all in more detail in future articles.

---

_But speaking of ~~Ruby~~Python…_

## Swift ⨯ **__****__****__**_

Adding to [our list of _“What code is like”_](https://nshipster.com/numericcast/):

> Code is like fan fiction.

Sometimes to ship software, you need to pair up and “ship” different technologies.

In building these features, the “powers that be” have ordained that [Swift replace Python for Machine Learning](https://github.com/tensorflow/swift/blob/master/docs/WhySwiftForTensorFlow.md). Taking for granted that an incremental approach is best, the way to make that happen is to allow Swift to interoperate with Python as seamlessly as it does with Objective-C. And since Swift 4.2, we’ve been [getting pretty close](https://www.tensorflow.org/swift/tutorials/python_interoperability).

```
import Python

let numpy = Python.import("numpy")
let zeros = numpy.ones([2, 4])
/* [[1, 1, 1, 1]
    [1, 1, 1, 1]] */
```

## The Externalities of Dynamism

The promise of additive changes is that they don’t change anything if you don’t want them to. You can continue to write Swift code remaining totally ignorant of the features described in this article (most of us have so far). But let’s be clear: there are no cost-free abstractions.

Economics uses the term [negative externalities](https://en.wikipedia.org/wiki/Externality) to describe indirect costs incurred by a decision. Although you don’t pay for these features unless you use them, we all shoulder the burden of a more complex language that’s more difficult to teach, learn, document, and reason about.

---

A lot of us who have been with Swift from the beginning have grown weary of Swift Evolution. And for those on the outside looking in, it’s unfathomable that we’re wasting time on inconsequential “sugar” like this instead of features that will _really_ move the needle, like [`async` / `await`](https://gist.github.com/lattner/429b9070918248274f25b714dcfc7619).

In isolation, each of these proposals is thoughtful and useful — _genuinely_. We’ve already [had occasion](https://github.com/NSHipster/DBSCAN) to use a few of them. But it can be really hard to judge things on their own technical merits when they’re steeped in emotional baggage.

Everyone has their own sugar tolerance, and it’s often informed by what they’re accustomed to. Being cognizant of the [drawbridge effect](https://en.wikipedia.org/wiki/Drawbridge_mentality), I honestly can’t tell if I’m out of touch, or if it’s [the children who are wrong](https://knowyourmeme.com/memes/am-i-out-of-touch)…
