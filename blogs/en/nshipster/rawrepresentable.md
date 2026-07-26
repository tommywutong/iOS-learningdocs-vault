---
title: RawRepresentable
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/rawrepresentable/'
original_language: en
published: 2020-01-29
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:65e97d6a9aae9764'
translated: false
---

> 原文：[RawRepresentable](https://nshipster.com/rawrepresentable/)　·　NSHipster (Mattt)

# [Raw​Representable](https://nshipster.com/rawrepresentable/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  January 29^th, 2020

Programming is about typing. And programming languages are typically judged by how much they make you type — in both senses of the word.

Swift is beloved for being able to save us a few keystrokes without compromising safety or performance, whether it’s through implicit typing or automatic synthesis of protocols like [`Equatable`](https://nshipster.com/equatable-and-comparable/) and [`Hashable`](https://nshipster.com/hashable/). But the OG ergonomic feature of Swift is undoubtedly automatic synthesis of `RawRepresentable` conformance for enumerations with raw types. You know… the language feature that lets you do this:

```
enum Greeting: String {
    case hello = "hello"
    case goodbye // implicit raw value of "goodbye"
}

enum SortOrder: Int {
    case ascending = -1
    case same // implicit raw value of 0
    case descending  // implicit raw value of 1
}
```

Though _“enum + RawValue”_ has been carved into the oak tree of our hearts since first we laid eyes on that language with a fast bird, few of us have had occasion to consider what `RawRepresentable` means outside of autosynthesis. This week, we invite you to do a little extra typing and explore some untypical use cases for the `RawRepresentable` protocol.

---

In Swift, an enumeration can be declared with raw value syntax.

According to [the documentation](https://developer.apple.com/documentation/swift/rawrepresentable):

> For any enumeration with a string, integer, or floating-point raw type, the Swift compiler automatically adds `RawRepresentable` conformance.

When developers first start working with Swift, they inevitably run into situations where raw value syntax doesn’t work:

- Enumerations with raw values other than `Int` or `String`
- Enumerations with associated values

Upon seeing those bright, red error sigils, many of us fall back to a more conventional enumeration, failing to realize that what we wanted to do wasn’t impossible, but rather just slightly beyond what the compiler can do for us.

---

## RawRepresentable with C Raw Value Types

The primary motivation for raw value enumerations is to improve interoperability. Quoting again from the docs:

> Using the raw value of a conforming type streamlines interoperation with Objective-C and legacy APIs.

This is true of Objective-C frameworks in the Apple SDK, which declare enumerations with [`NS_ENUM`](https://nshipster.com/ns_enum-ns_options/). But interoperability with other C libraries is often less seamless.

Consider the task of interfacing with [libcmark](https://github.com/commonmark/cmark), a library for working with Markdown according to the [CommonMark spec](http://spec.commonmark.org/). Among the imported data types is `cmark_node_type`, which has the following C declaration:

```
typedef enum {
  /* Error status */
  CMARK_NODE_NONE,

  /* Block */
  CMARK_NODE_DOCUMENT,
  CMARK_NODE_BLOCK_QUOTE,
  …
  CMARK_NODE_HEADING,
  CMARK_NODE_THEMATIC_BREAK,

  CMARK_NODE_FIRST_BLOCK = CMARK_NODE_DOCUMENT,
  CMARK_NODE_LAST_BLOCK = CMARK_NODE_THEMATIC_BREAK,

  …
} cmark_node_type;
```

We can immediately see a few details that would need to be ironed out along the path of Swiftification — notably, 1) the sentinel `NONE` value, which would instead be represented by `nil`, and 2) the aliases for the first and last block values, which wouldn’t be encoded by distinct enumeration cases.

Attempting to declare a Swift enumeration with a raw value type of `cmark_node_type` results in a compiler error.

```
enum NodeType: cmark_node_type {} // Error
```

However, that doesn’t totally rule out `cmark_node_type` from being a `RawValue` type. Here’s what we need to make that happen:

```
enum NodeType: RawRepresentable {
    case document
    case blockQuote
    …

    init?(rawValue: cmark_node_type) {
        switch rawValue {
        case CMARK_NODE_DOCUMENT: self = .document
        case CMARK_NODE_BLOCK_QUOTE: self = .blockQuote
        …
        default:
            return nil
        }
    }

    var rawValue: cmark_node_type {
        switch self {
        case .document: return CMARK_NODE_DOCUMENT
        case .blockQuote: return CMARK_NODE_BLOCK_QUOTE
        …
        }
    }
}
```

It’s a far cry from being able to say `case document = CMARK_NODE_DOCUMENT`, but this approach offers a reasonable solution that falls within the existing semantics of the Swift standard library.

That debunks the myth about `Int` and `String` being the only types that can be a raw value. What about that one about associated values?

## RawRepresentable and Associated Values

In Swift, an enumeration case can have one or more associated values. Associated values are a convenient way to introduce some flexibility into the closed semantics of enumerations and all the benefits they confer.

[As the old adage goes](https://github.com/apple/swift/blob/master/docs/Driver.md#output-file-maps):

> There are three numbers in computer science: 0, 1, and N.

```
enum Number {
    case zero
    case one
    case n(Int)
}
```

Because of the associated value on `n`, the compiler can’t automatically synthesize an `Int` raw value type. But that doesn’t mean we can’t roll up our sleeves and pick up the slack.

```
extension Number: RawRepresentable {
    init?(rawValue: Int) {
        switch rawValue {
        case 0: self = .zero
        case 1: self = .one
        case let n: self = .n(n)
        }
    }

    var rawValue: Int {
        switch self {
        case .zero: return 0
        case .one: return 1
        case let .n(n): return n
        }
    }
}

Number(rawValue: 1) // .one
```

Another myth busted!

Let’s continue this example to clear up a misconception we found in the documentation.

## RawRepresentable as Raw Values for Another Enumeration

Consider the following from the `RawRepresentable` docs:

> For any enumeration with a string, integer, or floating-point raw type, the Swift compiler automatically adds `RawRepresentable` conformance.

This is, strictly speaking, true. But it actually under-sells what the compiler can do. The actual requirements for raw values are as follows:

- The raw value type must be `Equatable`
- The raw value type must be `ExpressibleByIntegerLiteral`, `ExpressibleByFloatLiteral`, or `ExpressibleByStringLiteral`
- The raw value for each enumeration case must be a literal (or unspecified, in which case the value is inferred)

Let’s see what happens if we satisfy that for our `Number` type from before.

```
extension Number: Equatable {} // conformance is automatically synthesized

extension Number: ExpressibleByIntegerLiteral {
    init(integerLiteral value: Int) {
        self.init(rawValue: value)!
    }
}

-1 as Number // .n(-1)
0 as Number // .zero
1 as Number // .one
2 as Number // .n(2)
```

If we declare a new enumeration, `数` (literally “Number”) with a `Number` raw value…

```
enum 数: Number {
    case 一 = 1
    case 二 = 2
    case 三 = 3
}

数.二 // 二
数.二.rawValue // .n(2)
数.二.rawValue.rawValue // 2
```

_Wait, that actually works? Neat!_

What’s really interesting is that our contrived little enumeration type benefits from the same, small memory footprint that you get from using enumerations in more typical capacities:

```
MemoryLayout.size(ofValue: 数.三) // 1 (bytes)
MemoryLayout.size(ofValue: 数.三.rawValue) // 9 (bytes)
MemoryLayout.size(ofValue: 数.三.rawValue.rawValue) // 8 (bytes)
```

If raw values aren’t limited to `String` or `Int`, as once believed, you may start to wonder: _How far can we take this?_

## RawRepresentable with Metatype Raw Values

Probably the biggest selling point of enumerations in Swift is how they encode a closed set of values.

```
enum Element {
    case earth, water, air, fire
}
```

Unfortunately, there’s no equivalent way to “close off” which types conform to a protocol.

```
public protocol Elemental {}
public struct Earth: Elemental {}
public struct Water: Elemental {}
public struct Air: Elemental {}
public struct Fire: Elemental {}
```

Without built-in support for type unions or an analog to the `open` access modifier for classes, there’s nothing that an API provider can do, for example, to prevent a consumer from doing the following:

```
struct Aether: Elemental {}
```

Any switch statement over a type-erased `Elemental` value using `is` checks will necessarily have a `default` case.

Until we have a first-class language feature for providing such guarantees, we can recruit enumerations and raw values for a reasonable approximation:

```
extension Element: RawRepresentable {
    init?(rawValue: Elemental.Type) {
        switch rawValue {
        case is Earth.Type:
            self = .earth
        case is Water.Type:
            self = .water
        case is Air.Type:
            self = .air
        case is Fire.Type:
            self = .fire
        default:
            return nil
        }
    }

    var rawValue: Elemental.Type {
        switch self {
        case .earth: return Earth.self
        case .water: return Water.self
        case .air: return Air.self
        case .fire: return Fire.self
        }
    }
}
```

---

Returning one last time to the docs, we’re reminded that:

> With a `RawRepresentable` type, you can switch back and forth between a custom type and an associated `RawValue` type without losing the value of the original `RawRepresentable` type.

From the earliest days of the language, `RawRepresentable` has been relegated to the thankless task of C interoperability. But looking now with a fresh set of eyes, we can now see it for in all its [injective](https://en.wikipedia.org/wiki/Injective_function) glory.

So the next time you find yourself with an enumeration whose cases broker in discrete, defined counterparts, consider adopting `RawRepresentable` to formalize the connection.
