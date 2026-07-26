---
title: 'About flatMap, compactMap and monads | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/an-aside-about-flatmap-and-monads.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:08005e127d3f2833'
translated: false
---

> 原文：[About flatMap, compactMap and monads | Cocoa with Love](https://www.cocoawithlove.com/blog/an-aside-about-flatmap-and-monads.html)　·　Cocoa with Love (Matt Gallagher)

The [previous article](https://www.cocoawithlove.com/blog/statements-messages-reducers.html) used a Swift function named `compactMap` but when I originally wrote that article, it was named `flatMap`. The reasons why the name are subtle; on a literal level, `compactMap` is a “flatten” and a “map”, just like `flatMap` is. The arguments for the rename ended up centering on the fact that `flatMap` is often assumed to be a monadic transformation, so `compactMap` – which is not monadic – therefore needs a different name.

It’s an esoteric argument since you must know what a monad is and be aware of the assumption, in some circles, that `flatMap` is a monad (despite the fact that in Swift, it never makes any such claims).

Swift doesn’t use the word “monad” anywhere in its documentation. Monads are far from fundamental to Swift. Yet monads _are_ essential in some programming languages, particularly Haskell. Reprising the previous article’s topic of “units of computation”, monads are a fundamental unit of computation in Haskell.

In this article, I’ll look at monads. How can something be so fundamental in one language but completely optional in others? Should we try to use monads more often in Swift? What are the alternatives?

## What is a monad?

Monads are a compound concept that build upon simpler ideas. Monads are not particularly complicated but if you don’t have a clear mental picture of the ideas they build upon, they can be very abstract.

So I’m going to start as simple as possible and build up to monads.

### Function

Let’s consider an example of a function that takes a word and returns the first letter:

```swift
func firstLetter(_ word: String) -> Character {
   return word.first!
}
```

This function assumes that the `word` is a non-empty `String` (the `!` will abort the program if `word` is an empty string) but it’s otherwise straightforward.

Here’s a diagram of this function:

![Figure 1: a function](https://www.cocoawithlove.com/assets/blog/function_to_monad1.svg)

The input value is a `String` and the output value is a `Character`.

### Unwrap and apply

Let’s add a tiny bit of complexity.

Imagine for our `firstLetter` function that we have a whole list of words whose first letters we wish to extract. The traditional imperative approach is to unwrap (extract) each element in the list and perform the calculation for the element on its own.

```swift
func processWordList(_ wordList: [String]) {
   for word in wordList {
      let letter = firstLetter(word)
      // do something with letter
   }
}
```

Our input is an array containing `String` input values. The `for` loop unwraps each `String` in `wordlist`, the body of the loop applies the `firstLetter` function we wrote and then we can use the result. We can diagram this as follows:

![Figure 2: unwrapping from an array and applying a function](https://www.cocoawithlove.com/assets/blog/function_to_monad2.svg)

In this diagram, the “container” wrapping “input value” is the `wordList` array of strings. Each `word` extracted by the `for` loop is represented by the “input value” in the “Unwrap” box. The `firstLetter` function is contained inside the “Apply function” box and the `letter` is the “output value” at the right.

### Map

Using a `for` loop to extract values from an array works but the unwrapped value is limited in lifetime to the scope of the `for` loop. If we want to continue using the extracted first letters, we would need to store them in a location outside the loop.

```swift
func firstLetters(from wordList: [String]) -> [Character] {
   var result = [Character]()
   for word in wordList {
      let letter = firstLetter(word)
      result.append(letter)
   }
   return result
}
```

By appending the results to an array declared outside the loop, we can continue to work with the results outside the loop.

We can model this in a diagram as follows:

![Figure 3: mapping from one array to another](https://www.cocoawithlove.com/assets/blog/function_to_monad3.svg)

The “unwrap” and “append” steps are still required but I’ve omitted them from the diagram so we can focus on the fact that the inputs and outputs are now both the _same container_ but have _different contained types_.

The `firstLetters(from:)` function is only 8 lines but Swift provides a common abstraction for doing it in one line: `map`. The `map` function on `Array` takes a function – like our `firstLetter` function – applies it to each of its elements and returns the result as an `Array`. This is exactly the same work we’ve performed in our `firstLetters(from:)` function, so we can replace all eight lines with:

```swift
let letters = wordList.map(firstLetter)
```

This is unlikely to be new information to most developers – it is a very common concept in modern programming – however just 6 or 7 years ago, `map` was uncommon outside of functional programming. Even though I now use `map` and other similar transformations multiple times per day, I rarely used this type of construct in Objective-C.

It’s important to understand _why_ `map` works well:

> By wrapping the outputs of a function in the same abstraction that was used to wrap the inputs, we can continue to work with the outputs in many of the same ways that we worked with the inputs

When all your data is wrapped in the same abstractions (perhaps you’re working with arrays, optionals, results, observables, etc), then you can start to build an entire library that can flexibly handle that abstraction, without needing to worry about the specifics of the content. This helps make your code composable and lets you easily build processing pipelines or reuse code between projects and modules.

### Map returning an abstraction

Let’s change our original function. Instead of returning just the first character, lets assume the input is not a single word but some arbitrary text and we want to get the first letters of all words the text contains:

```swift
func firstLettersOfWords(_ text: String) -> [Character] {
   let tokenizer = NLTokenizer(unit: .word)
   tokenizer.string = text
   return tokenizer.tokens(for: text.startIndex..<text.endIndex).map { range in text[range].first! }
}
```

Cocoa’s natural language tokenizer performs all the dirty work of finding word ranges within the text and all we need to do is get the first letter of each word range. Let’s ignore the body of the function though and focus on its inputs and outputs:

![Figure 4: a function returning a wrapped result](https://www.cocoawithlove.com/assets/blog/function_to_monad4.svg)

The input value is a `String`, as it was in the first diagram but now the result isn’t a simple `Character` but `[Character]` (array of characters).

What happens if, as before, we’re passed an array of discrete text `String` inputs and we need to `map` over all of these?

![Figure 1: mapping to a double wrapped result](https://www.cocoawithlove.com/assets/blog/function_to_monad5.svg)

```swift
let result = textList.map(firstLettersOfWords)
```

What we get is a `result` that is `[[Character]]` (an array of arrays of characters). All this nesting is starting to get cumbersome.

### Monads

Sometimes we need to preserve multiple tiers of container but in many cases, when we’re dealing with aggregate types like `Array`, instead of multiple tiers of the same abstraction, we’re interested only in the aggregate of all objects in all layers.

Aggregating an `Array` of `Array` can be done by concatenating all the inner values into a single array:

```swift
var allFirstLetters = [Character]()
for result in textList.map(firstLettersOfWords) {
   allFirstLetters.append(result)
}
```

Swift provides a simpler way of writing this:

```swift
let allFirstLetters = textList.flatMap(firstLettersOfWords)
```

A diagram of what is happening here might look like this:

![Figure 1: a monad](https://www.cocoawithlove.com/assets/blog/function_to_monad6.svg)

This diagram of `flatMap` is a diagram of the key monadic transformation called “bind”. A **bind transformation**:

1. starts with a container that can contain zero or more values
2. applies a supplied function to each of its contained values, where the function returns results that are wrapped in the same kind of container
3. concatenates/flattens/merges all containers produced by (2) into a single container of the same kind

A rough definition of a **monad** is any container that offers a bind transformation.

In category theory, monads have a few additional requirements around construction from unwrapped values, structure preservation, identity transformations and operator associativity but these requirements are not really relevant to using `flatMap` in Swift.

## Why are monads not used more often?

If you have array, optionals or other container types, it’s probably because you’ve performed some work in the past that returned the container and it’s likely that future work you’ll perform will _also_ produce instances of the same container type. If we care about the end-results, not the structure in-between, then the flattening step of a monad helps us repeatedly apply container-returning functions without needing increasingly deeper layers of wrapping around our results.

> Monads let us scalably compose successive operations whose outputs each apply an additional layer of the same abstraction.

Monads have a purpose but their usage remains uncommon in Swift. It is certainly possible to incorporate them in all your programming but you might instinctively process things another way – including a number of approaches that are highly monad-like without really being monadic:

- loop and concatenating as you go can achieve the same result as using

  on
- statements or Swift’s optional chaining can similarly unwrap an

  , similar to using

  on

  .
- syntax lets us apply a “bind”-like transformation (flattening out successive throwing functions) without ever really exposing a monad-like type
- , letting the layers of nesting build up and then apply a post-processing

  step that does its own container unwrapping and concatenation

In Swift, since you can have side-effects (unwrapped values that escape their unwrapping scope) monads are not mandatory.

## Why do Haskell programmers care so much?

Unlike Swift, you cannot avoid monads in Haskell. Why are they optional in one language but mandatory in another?

The answer is that it’s not _general_ monads that are useful in Haskell as much as _one-way_ monads – the IO monad in particular – and how they interact with the Haskell runtime system.

A **one-way monad** is a type that you can _never_ unwrap. You can perform `map` or `flatMap` operations (called bind in Haskell) on a one-way monad but you can never perform a direct unwrap or any other kind of “get” operation to look at the contents. This one-way nature allows total hiding of the contents.

Why would you ever want to totally hide contents?

Strict functional programming languages like Haskell are not allowed to mutate state or have side effects. This complicates any interaction with the user, the file system, networking, the operating system or other services since _all_ of these interactions are stateful and have side effects.

The way Haskell deals with these problems is that you can interact with these services freely but you never get access to the result. Instead, you get a container (an IO monad) that you can never unwrap. If you never unwrap a container containing side effects, then you remain free from the impact of those side effects – your actions remain the same regardless of whether the container holds a fully parsed data structure or a file-not-found error.

If you ever pass the IO monad back to the Haskell runtime, it will get correctly unwrapped – so effects like reading or writing of files will be correctly resolved at runtime – but your Haskell code remains isolated from this unwrapping and remains side-effect free.

In short video on Microsoft’s Channel 9 titled [Towards a Programming Language Nirvana](https://channel9.msdn.com/Blogs/Charles/Simon-Peyton-Jones-Towards-a-Programming-Language-Nirvana) (from 2007), [Simon Peyton Jones](https://en.wikipedia.org/wiki/Simon_Peyton_Jones), [Erik Meijer](https://en.wikipedia.org/wiki/Erik_Meijer_(computer_scientist)) and [Butler Lampson](https://en.wikipedia.org/wiki/Butler_Lampson) talk about how programming is fundamentally about having effects but – as the video explains – pure functional programming languages like Haskell are about _not_ having effects, so functional programming is completely useless.

Peyton Jones is being facetious, of course, since Haskell has what Peyton Jones calls “controlled” effects, achieved largely through the IO monad. Each IO monad “bind” operation in Haskell can be considered a single effect. Building a series of effects (i.e. a program) requires multiple IO monadic bind steps and in this way, the IO monad is literally the building block used to build Haskell programs.

## flatMap versus compactMap

Let’s bring the discussion back to Swift and look at the `firstLetter` function again. Since an empty `String` doesn’t necessarily have a first letter, we used a force-unwrap (the `!` operator). This will fail if the word is an empty string and requires the caller be aware of this limitation (a precondition).

Preconditions can easily become a source of unexpected fatal errors since they are not enforced by the compiler. Imagine we wanted to avoid this precondition and instead return an optional `Character`:

```swift
func firstLetterIfAvailable(_ word: String) -> Character? {
   return word.first
}
```

Now, if we processed an array of words using this function:

```swift
let optionalLetters = wordList.map(firstLetterIfAvailable)
```

the result would be `[Character?]` (an array of optional characters) instead of `[Character]` (an array of characters).

### flatMap

In many ways, this `[Character?]` (array of optional characters) is similar to the previous `[[Character]]` (array of arrays of characters) in that we again have two container wrappings around the underlying `Character` (instead of two array wrappings, we now have one array and one optional). There’s also a fairly intuitive concatenate rule if you want to eliminate the optional layer (concatenate all non-nil optionals into an array and omit all nil-optionals).

But we can’t replace the word `map` in the previous example with `flatMap` to flatten this structure, like we did previously. At least, we can’t do this, _anymore_. Prior to Swift 4.1, there existed an overload of `flatMap` that could have helped us here but it was renamed.

Why?

1. the mathematical definition of monad requires the flatten operation be across two nested containers of the same kind
2. with monads (even though the verb “flat” doesn’t literally imply such a narrow interpretation)

### compactMap

It all seemed a little pedantic to me but there’s not real sense in complaining: the relevant overload of `flatMap` wasn’t removed, it was merely renamed to `compactMap`.

```swift
let letters = wordList.compactMap(firstLetterIfAvailable)
```

The `letters` value here is a simple `[Character]` (array of characters), instead of `[Character?]` (array of optional character). The “compacting” is achieved by discarding nil values and concatenating only those non-nil characters.

Outside the Swift standard library, `compactMap` is used for any `flatMap`-like scenario where the nested container would be `Optional` but the outer container would be something else. For example, I’ve used it in my own [CwlSignal library](https://github.com/mattgallagher/CwlSignal) as a name for a map-like operator that transforms values that pass through the signal pipeline into optional values, then discards `nil` values, emitting only those non-nil outputs of the transformation.

There’s a valid question about what you should name similar operations where the inner container has other types. What’s the name for compacting an array of `Result`? Is this also a `compactMap` or are we expected to leave `Optional` in its own isolated space? I don’t know.

## Conclusion

Even though monads are essential in languages like Haskell, they’re just one of many processing tools in Swift.

I don’t think there’s any real need to _try_ to be monadic in Swift. There are plenty of cases where layers of Error handling or `Optional` or `Array` will naturally encourage you to concatenate results or filter out empty results but whether you choose to do this with `flatMap` or `guard let` or `for` loops or Swift’s error handling is a matter of personal syntactic preference – you’ll get the same result in each case.
