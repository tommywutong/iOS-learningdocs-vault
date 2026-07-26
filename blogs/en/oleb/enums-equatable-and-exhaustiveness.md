---
title: Enums, Equatable, and exhaustiveness
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/enums-equatable-exhaustiveness/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b579bc5440de7220'
translated: false
---

> 原文：[Enums, Equatable, and exhaustiveness](https://oleb.net/blog/2017/03/enums-equatable-exhaustiveness/)　·　Ole Begemann

# Enums, Equatable, and exhaustiveness

Say you have this Swift enum:

```
enum Expression {
    case number(Double)
    case string(String)
}
```

And you want it to conform to [`Equatable`](https://developer.apple.com/reference/swift/equatable). Since the enum has associated values, `Equatable` conformance must be added manually. So you implement the [`==` function](https://developer.apple.com/reference/swift/equatable/1539854):

```
extension Expression: Equatable {
    static func ==(lhs: Expression, rhs: Expression)
        -> Bool {
        switch (lhs, rhs) {
        case let (.number(l), .number(r)): return l == r
        case let (.string(l), .string(r)): return l == r
        default: return false
        }
    }
}
```

You handle the two cases where the two arguments are the same case and add a `default` pattern to return `false` otherwise. This is straightforward, short, and correct:

```
Expression.number(1) == .number(1) // → true
Expression.number(1) == .string("a") // → false
```

# Default case makes exhaustiveness check uneffective

However, your implementation has a serious flaw: if you ever add another case to your enum, the compiler won’t alert you that your `==` implementation is now incomplete. Let’s add a third case to the enum:

```
enum Expression {
    case number(Double)
    case string(String)
    case bool(Bool)
}
```

This is totally fine as far as the compiler is concerned. Your code will now return wrong results, though:

```
Expression.bool(true) == .bool(true) // → false!
```

The `default` clause in the `switch` statement make the compiler’s exhaustiveness checks uneffective. For this reason, it’s generally a good idea to not use `default` in `switch` statements if you can avoid it.

**Don’t use `default` in `switch` statements if you can avoid it.**

# Quadratic explosion of patterns

The downside of not having a default case is, of course, more boilerplate to write. Here’s a version of `==` that switches over the three-case enum exhaustively:

```
extension Expression: Equatable {
    static func ==(lhs: Expression, rhs: Expression)
        -> Bool {
        switch (lhs, rhs) {
        case let (.number(l), .number(r)): return l == r
        case let (.string(l), .string(r)): return l == r
        case let (.bool(l), .bool(r)): return l == r
        case (.number, .string),
             (.number, .bool),
             (.string, .number),
             (.string, .bool),
             (.bool, .number),
             (.bool, .string): return false
        }
    }
}
```

Phew! This isn’t fun to write, and it would get even worse with more cases. The number of states the `switch` statement must distinguish grows quadratically with the number of cases in the enum.

# From quadratic to linear growth

You can make this considerably more manageable with some intelligent application of the `_` placeholder pattern. While we saw above that a single default clause is not enough, _one pattern per case_ is. The last six patterns in the `switch` statement become three:

```
extension Expression: Equatable {
    static func ==(lhs: Expression, rhs: Expression)
        -> Bool {
        switch (lhs, rhs) {
        case let (.number(l), .number(r)): return l == r
        case let (.string(l), .string(r)): return l == r
        case let (.bool(l), .bool(r)): return l == r
        case (.number, _),
             (.string, _),
             (.bool, _): return false
        }
    }
}
```

Even better, each additional case in the enum only adds two more lines to the `switch` statement — it doesn’t grow quadratically anymore. And you retain the benefit from the compiler’s exhaustiveness checks: adding a new case will raise an error in `==`.

# Sourcery

If this is still too much boilerplate for you, take a look at [Krzysztof Zabłocki’s](http://merowing.info) code generation tool [Sourcery](https://github.com/krzysztofzablocki/Sourcery). Among many other things, it can auto-generate `Equatable` conformances for enums and other types (and keep them up to date).
