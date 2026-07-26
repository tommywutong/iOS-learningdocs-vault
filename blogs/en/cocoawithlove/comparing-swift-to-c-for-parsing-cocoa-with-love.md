---
title: 'Comparing Swift to C++ for parsing | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/2016/05/01/swift-name-demangling.html'
original_language: en
published: 2016-05-01
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:b376ff625b66ad8b'
translated: false
---

> 原文：[Comparing Swift to C++ for parsing | Cocoa with Love](https://www.cocoawithlove.com/blog/2016/05/01/swift-name-demangling.html)　·　Cocoa with Love (Matt Gallagher)

I rewrote the C++ implementation of Swift’s [Demangle.cpp](https://github.com/apple/swift/blob/master/lib/Demangling/OldDemangler.cpp) in Swift. [My reimplementation](https://github.com/mattgallagher/CwlDemangle) is completely standalone and can be dropped directly into any Swift project.

On its own though, that isn’t necessarily very interesting. Demangling Swift names isn’t a very common task – most Swift/Cocoa reflection functions will return an already demangled name. You usually have to go through C functions to get a mangled name in the first place.

To make it interesting, I turned the exercise into an opportunity to compare C++ and Swift – to see if Swift could be used as a C++ replacement for relatively low level tasks like a [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser). Would C++ do things with preprocessor macros or templates and metaprogramming that can’t be recreated in Swift, leading to cumbersome workarounds? Would Swift turn out to have critical performance problems?

And if I could clear all the technical hurdles, could I improve on the C++ implementation by making it more “Swifty”? What would idiomatic Swift look like for this type of work?

As an aside to the whole language comparison, the `ScalarScanner` that I implemented as part of the parser [is available separately](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlScalarScanner.swift?ts=3) and might be useful if you’re looking for an alternative to using `NSScanner`, `NSRegularExpression` or other tools poorly suited to character-by-character parsing.

> NOTE: as of October 2018, CwlDemangle is up-to-date with the Swift 4.2 [Demangler.cpp](https://github.com/apple/swift/blob/master/lib/Demangling/Demangler.cpp). This article compares the older Swift 3 parsing which is still present – functions starting with `demangleSwift3` in CwlDemangle – and the corresponding [OldDemangle.cpp](https://github.com/apple/swift/blob/master/lib/Demangling/OldDemangler.cpp) in the Swift repository.

## A particular style of C++

I’m going to compare my opinion of what idiomatic Swift is to the style of C++ found in [Demangle.cpp](https://github.com/apple/swift/blob/master/lib/Demangling/OldDemangler.cpp) from the Swift project.

I’m going to refer to traits of C++ throughout this article but I will usually mean: traits of C++ as used in Demangle.cpp. Of course, there are lots of different ways of writing C++ and the C++ on display in Demangle.cpp is a very narrow subset. Demangle.cpp uses a particular, minimalist, conservative style. I will discuss some possible pragmatic reasons _why_ Demangle.cpp is so minimalist but for now, please keep in mind: I’m not saying C++ _can’t_ do things differently but that a mainstream C++ compiler project from experienced, professional developers _chooses_ to do things a certain way.

## A Swift UnicodeScalar scanner

Starting at the beginning, the most important tool for writing a [recursive descent parser](https://en.wikipedia.org/wiki/Recursive_descent_parser) is a scanner (character, string and other token reader) for traversing the input data.

Demangle.cpp defines its own scanner class named `NameSource` for traversing data provided by an LLVM `StringRef`.

```cpp
class NameSource {
  StringRef Text;
public:
  NameSource(StringRef text);

  bool hasAtLeast(size_t len);
  bool isEmpty();
  explicit operator bool();
  char peek();
  char next();
  bool nextIf(char c);
  bool nextIf(StringRef str);
  StringRef slice(size_t len);
  StringRef str();
  void advanceOffset(size_t len);
  StringRef getString();
  bool readUntil(char c, std::string &result);
};
```

We need something with similar functionality. The obvious choice for this in Cocoa is usually `NSScanner` (or a subclass) but for a number of reasons, `NSScanner` isn’t really the right tool for this type of job. In particular: it doesn’t read single characters, it doesn’t peek, you can’t inline Objective-C method invocations and it doesn’t use Swift error handling.

So I wrote `ScalarScanner`to behave like a Swift version of `NameSource`:

```swift
struct ScalarScanner<C: Collection> where C.Iterator.Element == UnicodeScalar,
   C.Index: Comparable {
   let scalars: C
   var index: C.Index
   var consumed: Int
   
   init(scalars: C)
   mutating func match(string: String) throws
   mutating func match(scalar: UnicodeScalar) throws
   mutating func readUntil(scalar: UnicodeScalar) throws -> String
   mutating func readUntil(string: String) throws -> String
   mutating func readWhile(testTrue: (UnicodeScalar) -> Bool) -> String
   mutating func skipWhile(testTrue: (UnicodeScalar) -> Bool)
   mutating func skipUntil(scalar: UnicodeScalar) throws
   mutating func skipUntil(string: String) throws
   mutating func skip(count: Int = 1) throws
   mutating func backtrack(count: Int = 1) throws
   mutating func remainder() -> String
   mutating func conditional(string: String) -> Bool
   mutating func conditional(scalar: UnicodeScalar) -> Bool
   func requirePeek() throws -> UnicodeScalar
   func peek(skipCount: Int = 0) -> UnicodeScalar?
   mutating func readScalar() throws -> UnicodeScalar
   mutating func readInt() throws -> Int
   mutating func readScalars(count: Int) throws -> String
   func unexpectedError() -> Error
   var isAtEnd: Bool
}
```

From the first line, we can see a difference between the Swift and C++ versions. Swift has a standard set of protocols and constraints for defining data providers, so it makes sense to use them. C++ _could_ use a template parameter to define the data provider but since C++ lacks an equivalent to Swift’s protocol constraints and lacks a corresponding set of standard behaviors, the mulitple constraints for the data provider would be a confusing black box thrust upon any user of `NameSource` – likely manifesting in weird errors in internal headers if any requirements were not met.

Unless there’s a strong need for abstraction in C++, it’s not worth the effort. Meanwhile, in Swift, there’s no reason to make collections, sequences and other common providers concrete.

This has immediate reuse benefits for Swift. This `ScalarScanner` can read equally from `Array<UnicodeScalar>` or from a `String.UnicodeScalarView` and is completely reusable in any Swift project. Meanwhile `NameSource` is completely dependent on LLVM’s `StringRef` and would need to be rewritten to be used with a different data provider.

## Translation is boring

I translated about 4200 lines of C++ into about 2800 lines of Swift in roughly 5 hours. All that typing, copying, regex replacing and glancing between code files is as mind numbing as you’d expect.

The answer to my question about whether there would be any difficulties is: there were no major hurdles at all. Demangle.cpp is a very clear, simple, easy to translate file.

Later, because I’m a glutton for punishment, I spent another few hours refactoring to make things a little more “Swifty” and get the line count down under 2100.

## Biggest difference between Swift and C++: error handling

The initial implementation – even before any refactoring to make the code more “Swifty” – included Swift error handling as a replacement for the C++ approach of returning a `nullptr` on error. Swift error handling is such an obvious inclusion that it doesn’t require a second pass or a rethink, even during a relatively mindless translation task.

You can see how simple it is to switch from `nullptr` results to Swift error handling from the first line of the parser:

C++:

```cpp
if (!Mangled.nextIf("_T"))
   return nullptr;
```

Swift:

```swift
try scanner.match(string: "_T")
```

The difference between these two approaches is profound.

Most importantly, there are significant benefits for reliability. When Tony Hoare called null his [“billion dollar mistake”](https://en.wikipedia.org/wiki/Null_pointer), he was referring to the likelihood of bugs when a potentially null result is not checked for null. Looking at the Git history for Demangle.cpp reveals this happening on more than one occasion – and this doesn’t include bugs that may have been fixed prior to committing. Using `nullptr` to indicate failure has a real-world maintenance cost.

Also of potential benefit for maintenance: the Swift approach includes contextual information. All errors thrown by the parser include the index where the parsed failed and brief information about the type of token that couldn’t be read. If something goes wrong, there’s at least some information about _why_ the failure occurred.

But the most visible difference in adopting Swift error handling is a significant reduction in code size. Switching to Swift error handling immediately eliminated 149 `return nullptr` early exit lines from the C++ version. Furthermore, Swift can happily exit from a function in the middle of an expression when a parse attempt fails instead of needing to break expressions into multiple pieces either side of early exits.

For example, the following C++:

```cpp
#define DEMANGLE_CHILD_OR_RETURN(PARENT, CHILD_KIND) do { \
   auto _node = demangle##CHILD_KIND();                  \
   if (!_node) return nullptr;                           \
   (PARENT)->addChild(std::move(_node));                 \
} while (false)

auto metaclass = NodeFactory::create(Node::Kind::Metaclass);
DEMANGLE_CHILD_OR_RETURN(metaclass, Type);
return metaclass;
```

Is reduced down to:

```swift
return SwiftName(kind: .metaclass, children: [try demangleType(&scanner)])
```

Swift is happy to run `demangleType` and exit before proceeding with construction of the `Array` or `SwiftName`.

## C++ exceptions versus Swift error handling

C++ could have used exceptions to improve syntactic efficiency and achieve some of the same effects as Swift error handling. Why rely on error prone `nullptr` to communicate results in Demangle.cpp?

Many large C++ projects – Swift included – are compiled with C++ exceptions entirely disabled. Why deliberately remove a potentially useful feature from the language? The Swift developers answer this question when [considering error handling options for Swift](https://github.com/apple/swift/blob/master/docs/ErrorHandlingRationale.rst#id1):

> C++ aspires to making out-of-memory a recoverable condition, and so allocation can throw […] Since constructors are called pervasively and implicitly, it makes sense for the default rule to be that all functions can throw […] Different error sites occur with a different set of cleanups active, and there are a large number of such sites. In fact, prior to C++11, compilers were forced to assume by default that destructor calls could throw, so cleanups actually created more error sites. This all adds up to a significant code-size penalty for exceptions, even in projects which don’t directly use them and which have no interest in recovering from out-of-memory conditions.

C++ exceptions bloat the entire project – even if you only use them sparingly. The code size increase alone can start to slow your program. Then, if you actually throw an exception, the stack unwinding is between 4 and 100 times slower than simply returning a value from a the function (depending on compiler and host details). And you have to maintain rigorous RAII discipline or risk leaking memory. And you have to be careful to avoid exceptions in destructors.

Exceptions are not well-loved.

## Conditionals and switch statements

The majority of any recursive descent parser is conditional logic based on the token encountered. Accordingly, the C++ parser is filled with functions that look like this:

```cpp
if (Mangled.nextIf('M')) {
 if (Mangled.nextIf('P')) {
    auto pattern =
        NodeFactory::create(Node::Kind::GenericTypeMetadataPattern);
    DEMANGLE_CHILD_OR_RETURN(pattern, Type);
    return pattern;
  }
  if (Mangled.nextIf('a')) {
    auto accessor =
      NodeFactory::create(Node::Kind::TypeMetadataAccessFunction);
    DEMANGLE_CHILD_OR_RETURN(accessor, Type);
    return accessor;
  }
  // ... and so on
}
```

The control flow here shows two tiers of conditionals, checking for `'M'` at the top level and `'P'` and `'a'` at the second.

With Swift `switch` statements, we can check both tiers of conditionals simultaneously:

```swift
switch (try scanner.readScalar(), try scanner.readScalar()) {
case ("M", "P"): return SwiftName(kind: .genericTypeMetadataPattern, children: [try demangleType(&scanner)])
case ("M", "a"): return SwiftName(kind: .typeMetadataAccessFunction, children: [try demangleType(&scanner)])
// ... and so on
}
```

Technically, C++ could pack two `char`s into a `uint16_t` and switch on that, just like I have done in Swift. With macros, you could probably make the case label vaguely readable. The point is really that this wouldn’t be idiomatic C++ so you’d need to weigh the syntactic benefit against the familiarity shock.

Let’s look at some non-idiomatic C++ and see how that usually goes. The following exerpt from Demangle.cpp is an implementation of a two tier conditional construct in C++:

```cpp
enum class ImplConventionContext { Callee, Parameter, Result };

StringRef demangleImplConvention(ImplConventionContext ctxt) {
#define CASE(CHAR, FOR_CALLEE, FOR_PARAMETER, FOR_RESULT)            \
  if (Mangled.nextIf(CHAR)) {                                      \
    switch (ctxt) {                                                \
    case ImplConventionContext::Callee: return (FOR_CALLEE);       \
    case ImplConventionContext::Parameter: return (FOR_PARAMETER); \
    case ImplConventionContext::Result: return (FOR_RESULT);       \
    }                                                              \
    unreachable("bad context");                               \
  }
  auto Nothing = StringRef();
  CASE('a',   Nothing,                Nothing,         "@autoreleased")
  CASE('d',   "@callee_unowned",      "@unowned",      "@unowned")
  CASE('D',   Nothing,                Nothing,         "@unowned_inner_pointer")
  CASE('g',   "@callee_guaranteed",   "@guaranteed",   Nothing)
  CASE('e',   Nothing,                "@deallocating", Nothing)
  CASE('i',   Nothing,                "@in",           "@out")
  CASE('l',   Nothing,                "@inout",        Nothing)
  CASE('o',   "@callee_owned",        "@owned",        "@owned")
  return Nothing;
#undef CASE
}
```

This was the trickiest construct from Demangle.cpp to translate into Swift because it’s so unconventional. It was an effort to work out, given possible values of `ctxt` on input, what were the possible results from the function.

That’s the result of doing something non-idiomatic in any language: it can take a little time to get your head around what it’s trying to do. Basically, it tries to consume the `char` in the left column of each `CASE` and if it succeeds, it will return the result from the second, third or fourth column, as determined by the `ctxt` parameter passed into the function.

Now, the `demangleImplConvention` function is used from two locations: `demangleImplCalleeConvention` and `demangleImplParameterOrResult`. The former always invokes `demangleImplConvention` with `ctxt` equal to `ImplConventionContext::Callee` and the latter goes through the following logic to determine the `ctxt` parameter:

```cpp
auto getContext = [](Node::Kind kind) -> ImplConventionContext {
  if (kind == Node::Kind::ImplParameter)
    return ImplConventionContext::Parameter;
  else if (kind == Node::Kind::ImplResult
           || kind == Node::Kind::ImplErrorResult)
    return ImplConventionContext::Result;
  else
    unreachable("unexpected node kind");
};

auto convention = demangleImplConvention(getContext(kind));
if (convention.empty()) return nullptr;
```

The relevant point is that the `ImplConventionContext` enum used as input to `demangleImplConvention` is largely pointless. The `getContext` closure maps `Node::Kind::ImplParameter` onto `ImplConventionContext::Parameter` and `Node::Kind::ImplResult`/`Node::Kind::ImplErrorResult` onto `ImplConventionContext::Result`. We might as well eliminating the existence of the `ImplConventionContext` type, using `Node::Kind` instead and then _both_ of the previous two C++ code blocks reduce to the following Swift `switch` statment:

```swift
func demangleImplConvention(inout scanner: ScalarScanner<[SwiftName]>, kind: SwiftName.Kind) throws -> String {
    switch (try scanner.readScalar(), (kind == .implErrorResult ? .implResult : kind)) {
    case ("a", .implResult): return "@autoreleased"
    case ("d", .implConvention): return "@callee_unowned"
    case ("d", .implParameter): fallthrough
    case ("d", .implResult): return "@unowned"
    case ("D", .implResult): return "@unowned_inner_pointer"
    case ("g", .implConvention): return "@callee_guaranteed"
    case ("g", .implParameter): return "@guaranteed"
    case ("e", .implParameter): return "@deallocating"
    case ("i", .implParameter): return "@in"
    case ("i", .implResult): return "@out"
    case ("l", .implParameter): return "@inout"
    case ("o", .implConvention): return "@callee_owned"
    case ("o", .implParameter): fallthrough
    case ("o", .implResult): return "@owned"
    case ("t", _): return "@convention(thin)"
    default: throw scanner.unexpectedError()
    }
}
```

This shows the advantage of a two value `switch` being idiomatic in Swift: compared to the strange series of `#define`, `if` and `switch` constructions in C++, this is clear, simple and readable. If you have a look, you’ll notice that the different columns from the C++ statement have become different rows in this example – it’s a two dimensional `switch` but the elements are still presented in a single column. (The appearance of a “t” case is not an accident; it’s an additional case rolled in from the `demangleImplCalleeConvention` call site.)

When we use a simple `switch` like this, it’s not just clearer to the programmer. It’s also clearer to the compiler. In the Swift case, you’d get warned by the compiler if you accidentally had two duplicate cases. You’re not going to get a warning about this in the C++ code… which is how the “D” case was accidentally labelled “d” for 2 years in the Swift compiler until I [created a pull request to fix the problem](https://github.com/apple/swift/pull/2328) while writing this article.

## Processing collections

Thus far, I’ve been looking at code changes in the parser but Demangle.cpp actually includes two different parts:

- the parser (which reads a mangled string into a tree of nodes) and
- the printer (that serializes the node tree back to an unmangled string).

Swift error handling and switch statements were a big help in the parser but they don’t offer much to the printer. The `print` function is already a single massive switch statement and it doesn’t need to return any error results.

Let’s look at a typical `case` from the `NodePrinter::print` function in C++:

```cpp
case Node::Kind::TupleElement:
  if (pointer->getNumChildren() == 1) {
    NodePointer type = pointer->getChild(0);
    print(type);
  } else if (pointer->getNumChildren() == 2) {
    NodePointer id = pointer->getChild(0);
    NodePointer type = pointer->getChild(1);
    print(id);
    print(type);
  }
  return;
```

On my first pass, I wasn’t able to think of anything helpful and the `SwiftName.print` I wrote ended up looking very similar to the C++.

```swift
case .TupleElement:
   if children.count == 1 {
      children[0].print(&output)
   } else if children.count == 2 {
      children[0].print(&output)
      children[1].print(&output)
   }
```

In my code, the `SwiftName` prints itself, rather than requiring a separate `NodePrinter` class, so the actual output stream is passed as the first parameter (named `output` here and it’s a `Swift.OutputStreamType`). Other than that difference, the code is structurally identical.

How do you make this more “Swifty”?

Finally, I concluded that idiomatic Swift implies processing collections – in this case, the `children` array – in a different way. Idiomatic Swift collection processing implies:

- Avoid accessing elements by index.
- Act on the collection unconditionally (conditionals should be inside your operators, not around them).
- Don’t loop over or manually enumerate collection contents (act declaratively on the whole collection).

That lead me to this:

```swift
case .tupleElement:
   output.write(sequence: children.prefix(2)) { $1.print(&$0) }
```

The `prefix` function on `SequenceType` ensures that we don’t overstep the bounds, eliminating the need for conditionals.

Obviously, this isn’t the typical `write` function on `OutputStreamType` but is instead a new overload which iterates over a sequence and runs a `render` closure to actually write to the `OutputStreamType` – in this case, that means recursing into the next level of the `SwiftName.print`

Now, it might not be clear why I’ve chosen to implement this as a function on `OutputStreamType` instead of simply running a `forEach` over the `children`. The answer is that this approach allows the `OutputStreamType` to insert prefixes, separators, suffixes or other labels into the stream between iterations of the loop making comma separated lists a simple task.

For example, the following C++:

```cpp
case Node::Kind::ProtocolConformance: {
  NodePointer child0 = pointer->getChild(0);
  NodePointer child1 = pointer->getChild(1);
  NodePointer child2 = pointer->getChild(2);
  print(child0);
  Printer << " : ";
  print(child1);
  Printer << " in ";
  print(child2);
  return;
}
```

becomes:

```swift
case .protocolConformance:
   output.write(sequence: children.prefix(3), labels: [nil, " : ", " in "]) { $1.print(&$0) }
```

Not all cases in the `print` function are this simple. In Demangle.cpp, many involve iteration over part of the `children`, terminated by different conditions, where rendering isn’t a simple recursive call to printing the child within.

An example of one of the tricker cases is `DependentGenericSignature`:

```cpp
case Node::Kind::DependentGenericSignature: {
  Printer << '<';
  
  unsigned depth = 0;
  unsigned numChildren = pointer->getNumChildren();
  for (;
       depth < numChildren
         && pointer->getChild(depth)->getKind()
             == Node::Kind::DependentGenericParamCount;
       ++depth) {
    if (depth != 0)
      Printer << "><";
    
    unsigned count = pointer->getChild(depth)->getIndex();
    for (unsigned index = 0; index < count; ++index) {
      if (index != 0)
        Printer << ", ";
      Printer << archetypeName(index, depth);
    }
  }
    
  if (depth != numChildren) {
    Printer << " where ";
    for (unsigned i = depth; i < numChildren; ++i) {
      if (i > depth)
        Printer << ", ";
      print(pointer->getChild(i));
    }
  }
  Printer << '>';
  return;
}
```

The logic here is difficult to dramatically simplify but if the operators you use to act on your collections aren’t composable (in particular, able to wrap recursively around each other), then you probably haven’t designed them correctly.

The nested loops over children from the C++ example are expressed as nested calls to `OutputStreamType.write` and the loop condition on the outer loop is expressed as a filter on the input sequence.

```swift
case .dependentGenericSignature:
   let filteredChildren = children.filter { $0.kind == .dependentGenericParamCount }.enumerated()
   var lastDepth = 0
   output.write(sequence: filteredChildren, prefix: "<", separator: "><") { o, t in
      lastDepth = t.offset
      o.write(sequence: 0..<t.element.indexFromContents(), separator: ", ") {
         $0.write(archetypeName($1, UInt32(t.offset)))
      }
   }
   let prefix: String? = (lastDepth + 1 < children.endIndex) ? " where " : nil
   let s = children.slice(lastDepth + 1, children.endIndex)
   output.write(sequence: s, prefix: prefix, separator: ", ", suffix: ">") { $1.print(&$0) }
```

This implementation of `slice` that I’m using, unlike the typical slice subscript in Swift (e.g. `children[(lastDepth + 1)..<children.endIndex]`), limits the slice range to the valid indices of the collection and won’t raise a fatal error if the start is greater than the end (it simply returns an empty collection).

No loops, no conditionals (except for a ternary operator), no direct accesses by index and the collection is processed by aggregrate statements (in two parts but that’s fine).

## Why does pragmatic C++ avoid abstraction?

The abstractions I used to improve the printing could easily be implemented in C++. But despite the standard library including a `<functional>` header (its included in Demangle.cpp although I’m not exactly sure where it’s used), C++ is not typically used in a functional fashion.

Part of the problem, as I’ve already discussed, is that a lack of protocols and contraints in C++ makes actions on different kinds of collection difficult. Accidentally providing a type that doesn’t meet the requirements of a template parameter and getting an esoteric error buried deep inside a header you didn’t write is frustrating and slow to resolve.

But there’s more to it than that. If you look though large codebases like llvm and Swift, you’ll see that they are very spartan. While Demangle.cpp contains a few minor C++11 niceities, in general, most of the code could have been written in the late 1990s. Most types have no template parameters. Most iteration is done using manual indexes. There’s no “map”, “reduce”, “filter” or other aggregate processing. And there’s no significant library of reusable functionality either – Demangle.cpp is part of a large compiler project but it has to implement its own token scanner.

Why does “best practice” in C++ often involve writing C++ like it’s C?

I’m often reminded of one of C++’s founding principles: you should only pay for those features that you use. The unfortunate corollary is that you’re forced to pay for everything you use.

C++’s compilation model requires substantial header includes and the more features you use, the slower and more painful compilation becomes. Templates must appear in the include path, rather than a separate compilation unit, adding significant complexity for every feature.

The end result is that large C++ projects work better when each file keeps to itself and minimizes includes.

I hope these problems don’t end up affecting Swift. In general, it feels like there’s less resistance in Swift towards using language features and abstractions because less baggage is brought along. No need for headers or declaring before usage. Swift uses easier-to-reason about generics rather than templates, Swift protocols rather than templates again and Swift thankfully uses nothing rather than metaprogramming. Additionally, the fact that reference counting, algebraic types and optionals are all part of the language, rather than bolted on using library features makes abstractions cleaner, less leaky and simpler.

## A quick comparison of performance

I don’t want to over emphasise the importance of performance here, since I’m fairly sure Demangle.cpp wasn’t written with performance as a primary consideration and neither was my Swift implementation. But I was curious anyway and I’m sure other people would be, also.

I extracted the full set of mangled strings from [Swift’s manglings.txt test file](https://github.com/apple/swift/blob/master/test/Demangle/Inputs/manglings.txt) and ran both a parse and print to string 10,000 times in a loop. For Apple’s Demangle.cpp version (C++), the loop was:

```cpp
for (llvm::StringRef name: names) {
   for (int i = 0; i < 10000; ++i) {
      swift::Demangle::NodePointer pointer = swift::demangle_wrappers::demangleSymbolAsNode(name);
      std::string string = swift::Demangle::nodeToString(pointer, options);
   }
}
```

For my own CwlDemangle.cpp, the loop was:

```swift
// NOTE: `input` here is `Array<UnicodeScalar>`, not `String`, to avoid conversion costs inside the loop.
for input in inputs {
   for _ in 0..<10_000 {
      _ = (try? demangleSwiftName(input).description) ?? input.reduce("") { return $0 + String($1) }
   }
}
```

I built the C++ code with the Swift project’s build script with the “ReleaseAssert” settings (which is `-O2`, I think) and Swift at `-O`.

The C++ version took 21.202s and the Swift version took 17.110s (Swift was about 20% faster).

Please don’t take this to mean that Swift is 20% faster than C++. That’s not what these numbers mean at all. In fact, at a glance it appears that all these numbers show is that the C++ version used a separately allocated pointer for each `NodePointer` but the corresponding `SwiftName` in the Swift version is just a plain `struct`. Yes, the C++ _needs_ the separate allocation to avoid a copy-constructor on `Node` when used with `std::vector` but an optimized copy constructor (or an alternative to `std::vector`) could be easily used if performance was a serious issue.

Let’s take a quick look at the top 10 “Time Profiler” results with “Invert call tree” selected:

C++

```
    Running Time    Self (ms)  Symbol Name
3766.0ms   17.2%    3766.0     szone_free_definite_size
1830.0ms    8.4%    1830.0     szone_malloc_should_clear
1741.0ms    7.9%    1741.0     tiny_malloc_from_free_list
1607.0ms    7.3%    1607.0     std::__1::__shared_weak_count::__release_shared()
1422.0ms    6.5%    1422.0     _os_lock_spin_lock
1232.0ms    5.6%    1232.0     tiny_free_list_add_ptr
1147.0ms    5.2%    1147.0     szone_size
1079.0ms    4.9%    1079.0     tiny_free_list_remove_ptr
876.0ms     4.0%     876.0     std::__1::__shared_weak_count::__add_shared()
679.0ms     3.1%     679.0     get_tiny_free_size
```

Swift

```
    Running Time    Self (ms)  Symbol Name
2115.0ms   12.3%    2115.0     _swift_release_(swift::HeapObject*)
1557.0ms    9.0%    1557.0     _swift_retain_(swift::HeapObject*)
1159.0ms    6.7%    1159.0     szone_free_definite_size
771.0ms     4.5%     771.0     szone_malloc_should_clear
770.0ms     4.5%     770.0     tiny_free_list_add_ptr
769.0ms     4.4%     769.0     _StringCore._claimCapacity(Int, minElementWidth : Int) -> (Int, COpaquePointer)
716.0ms     4.1%     716.0     tiny_malloc_from_free_list
645.0ms     3.7%     645.0     szone_size
569.0ms     3.3%     569.0     _os_lock_spin_lock
568.0ms     3.3%     568.0     _os_lock_handoff_lock
```

Bluntly: neither case is particularly optimized. These numbers represent roughly 100,000 names parsed and printed per second but optimized versions of these parsers would be an order of magnitude faster and these memory allocation, deallocation and reference counting calls would barely feature.

Despite C++ coming in slower, I would expect it to be easier to eliminate reference counting and dynamic string and array storage from C++. The reason is that these features are largely opt-in in C++ but opt-out in Swift. A couple days optimizing both codebases would probably see the performance lead swing the other way as the time spent in `_swift_release_` and `_swift_retain_` would be much harder to eliminate (not impossible, just harder) than the other calls in these lists.

In any case, I think it’s obvious that for parsers of this nature, C++ and Swift are “similar enough” in performance.

## Some minor points against Swift

The reason retains and releases are difficult to eliminate in Swift is that there’s no “unique pointer” (all reference types are shared pointers). But retains and releases are usually triggered implicitly depending on the `@owned` or `@guaranteed` nature of function parameters (attributes you might not know about unless you’ve read [Swift’s Calling Convention](https://github.com/apple/swift/blob/master/docs/CallingConvention.rst) carefully). Dancing around implicit rules like this can vary from difficult to impossible. It would be good to get some help in Instruments for locating lines of code that trigger retains and release and report why they are occurring (the variables and the rules involved) since reading the assembly and trying to connect it back to the Swift code is slow and error prone.

Changing topic from performance to safety, my implementation includes the methods: `Array.at` and `Array.slice`. These extensions to `Array` include non-fatal bounds checks on `Array` accesses (and no possibility of crashing because the start and end indexes of the slice have crossed over). With Swift’s emphasis on safety in other cases, I’m surprised that similar “crash proof” functionality is not part of the standard library. I feel like I need to include these in every project.

Another place where the Swift standard library could add a little more functionality is with `UnicodeScalar`. Converting between ASCII numerals stored in `UnicodeScalar` and `UInt32` is a real pain. Being explicit is fine but since `UnicodeScalar` _is_ a `UInt32` under the hood, it would be nice if the two could be used more naturally together for integer arithmetic so I don’t feel like need to unwrap and rewrap the `UnicodeScalar` twice in every expression.

It would also be nice to have an `ASCIILiteralType` in Swift (or something else for constructing `UInt8` from a string literal). The absence of such a type is the biggest reason I opted to use `UnicodeScalar` as my underlying element type, even though the code only ever processes UTF8 code units and is therefore wasting 25 bits of storage out of every 32. It doesn’t obviously impact performance here but if the source data was multiple kilobytes instead of a few dozen bytes, it might cause a bigger problem.

Finally, despite having an `OptionSetType` for managing bitfields, defining their values is still a nuisance in Swift. It would be nice to have an `enum` that could constrain values to powers of two by default (while allowing certain cases to have non-power-of-two values for multi-value masks) and could work together with `OptionSetType` to provide values/names for bits in the set.

## Usage

> The `ScalarScanner` presented in this article is contained in the [CwlScalarScanner.swift file](https://github.com/mattgallagher/CwlUtils/blob/master/Sources/CwlUtils/CwlScalarScanner.swift?ts=3) in my [CwlUtils project on Github](https://github.com/mattgallagher/CwlUtils).

The implementation is fully self-contained, so you can just copy the file if you wish.

Otherwise, the [ReadMe.md file for the project](https://github.com/mattgallagher/CwlUtils/blob/master/README.md) contains detailed information on cloning the whole repository and adding the framework it produces to your own projects but the file is fully self-contained so you can just download the “CwlScalarScanner.swift” file on its own and add it to an existing project, if you wish.

> The `CwlDemangle` implementation presented in this article is contained in the [CwlDemangle.swift file](https://github.com/mattgallagher/CwlDemangle/blob/master/CwlDemangle/CwlDemangle.swift?ts=3) in my [CwlDemangle project on Github](https://github.com/mattgallagher/CwlDemangle).

**LICENSE NOTE**: I usually release my code under an [ISC-style license](https://en.wikipedia.org/wiki/ISC_license) (an Expat/MIT-style license equivalent which I prefer for its simple, readable phrasing) but since the CwlDemangle.swift code is derived from the Apple/Swift project’s Demangle.cpp, I have released it under the same Apache-License 2.0 with runtime exception.

The implementation is fully self-contained, so you can just copy the file if you wish. The whole repository contains full tests for the demangle implementation (tests for `ScalarScanner` are in the `CwlUtils` repository, above).

Consult the [README](https://github.com/mattgallagher/CwlDemangle/blob/master/README.md) file for further details including a usage example or read the comments on the four functions at the top of the [CwlDemangle.swift file](https://github.com/mattgallagher/CwlDemangle/blob/master/CwlDemangle/CwlDemangle.swift?ts=3).

## Conclusion

Swift worked pretty well for writing a recursive descent parser. I expected performance gotchas in Swift compared to C++ but it worked out better than expected. I expected some C++ constructs, abstractions or library features that wouldn’t translate easily to Swift but it turns out such things are generally avoided in C++.

By adding Swift error handling, some multi-dimensional `switch` statements and some more functional abstractions over collections, I was able to produce code in Swift that passes all the same tests as the C++ version, has less possibility of unchecked `nullptr` crashes and array index issues, produces significantly better errors on parse failures, is less than half the number of lines and is nearly 20% faster.

None of this should be seen an attack on the Swift developers or their code quality. Quite the opposite: Demangle.cpp’s conservative, simple style is very easy to read, was very easy to adapt and has a universality to it that would make it legible to developers familiar with any C-influenced language. The code sometimes looks more like C than C++ but there are pragmatic reasons why that might result in a better experience in large codebases. I also suspect my more densely packed, hastily written Swift code would be a little harder for outsiders to follow.

And, of course, it’s the Swift developers who developed the tools in Swift that I’m using to iteratively improve upon the tools that are used to develop Swift.

## Appendix: why reimplement Demangle.cpp?

In general, no Swift API will give you a mangled name but if you interrogate your process through C APIs (or anything that isn’t Swift or Cocoa), you’ll see names that look like this:

```
_TFC19CwlUtils_OSXHarness11AppDelegate15someUserAction2fPs9AnyObject_T_   
```

This particular name is taken from the stack trace shown in the [previous article](https://www.cocoawithlove.com/blog/2016/04/14/error-recovery-attempter.html). This name ultimately comes from the C `dl_info` function (called as part of the `symbolsForCallStackAddresses` function I introduced in [Tracking tasks with stack traces in Swift](https://www.cocoawithlove.com/blog/2016/02/28/stack-traces-in-swift.html#implementation-of-callstackreturnaddresses)) which is not Swift name aware.

The demangled form of the name is:

```
CwlUtils_OSXHarness.AppDelegate.someUserAction2 (Swift.AnyObject) -> ()
```

The demangled name is far more readable. Where possible, I’d prefer to read the demangled name.

It’s easily possible to demangle this on the command-line. Assuming Xcode is installed, then the following will do it:

```
MacPro:~ matt$ xcrun swift-demangle _TFC19CwlUtils_OSXHarness11AppDelegate15someUserAction2fPs9AnyObject_T_
_TFC19CwlUtils_OSXHarness11AppDelegate15someUserAction2fPs9AnyObject_T_ ---> CwlUtils_OSXHarness.AppDelegate.someUserAction2 (Swift.AnyObject) -> ()
```

but this requires that a recent version of Xcode is installed on the target machine and you want to launch a whole process just to demangle a single name – neither are necessarily true on an end-user device.

Now, the Swift standard library kinda sorta contains a function to perform name demangling. The non-public function `stdlib_demangleName` exists in the standard library. Search your compiled programs and this identifier likely appears in all of them. Unfortunately, this function is non-public. Why? My guess is that you’re not supposed to encounter a mangled name if you’re acting in an idiomatically Swift way and the Swift developers are worried about backwards/forwards compatibility issues as the Swift mangled name grammar changes from version to version.

In any case, if we want name demangling, we need to do it ourselves. How complicated could it be?

The full grammar for mangled Swift names appears at the bottom of [The Swift ABI](https://github.com/apple/swift/blob/master/docs/ABI.rst) document. It’s roughly 10 screens in my browser just for the BNF grammar – it’s not exactly complex but it’s sizeable.

Faced with the prospect of implementing a 2000 line parser and serializer from scratch, I balked and instead decided to translate the Swift Demangle.cpp from C++ into Swift. This required a lot of typing but much less thinking than coding from scratch.

Why not simply use the Swift C++ version with a C wrapper, just like `stdlib_demangleName` does in the Swift standard library? For a few reasons, but mostly: I wanted to see what it was like to write a parser in Swift.
