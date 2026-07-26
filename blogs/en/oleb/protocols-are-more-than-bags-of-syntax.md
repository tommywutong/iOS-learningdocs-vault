---
title: Protocols are more than Bags of Syntax
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/12/protocols-have-semantics/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:17840e8c785de401'
translated: false
---

> 原文：[Protocols are more than Bags of Syntax](https://oleb.net/blog/2016/12/protocols-have-semantics/)　·　Ole Begemann

# Protocols are more than Bags of Syntax

There’s been an interesting (and very long) discussion on [swift-evolution](https://forums.swift.org/c/evolution/18) this week. Someone pitched the idea to [add a protocol named `DefaultConstructible`](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771) to the Swift standard library whose only requirement would be a parameter-less initializer:

```
protocol DefaultConstructible {
    init()
}
```

In other words, the protocol would formalize that you could create some sort of “default” value or instance of a conforming type without additional information.

Several people, mainly [Xiaodi Wu](https://github.com/xwu) and [Dave Abrahams](https://github.com/dabrahams), raised some very good arguments against this idea. I’d like to repeat these points here because I think they are important on a broader scale than this specific discussion.

# Semantics are an essential part of protocols

The first argument is that protocols are more than just bags of syntax. The semantics of a protocol matter just as much as its interface.

[Xiaodi Wu](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/34):

> In Swift, protocols do not merely guarantee particular spellings, but particular semantics as well.

[Dave Abrahams](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/48):

> I should add: that’s a core principle of generic programming as put forth by [Stepanov](https://en.wikipedia.org/wiki/Alexander_Stepanov).

[And](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/9):

> Protocols (a.k.a. concepts) are not just bags of syntax; unless you can attach semantics to the operations, you can’t write useful generic algorithms against them. So we shouldn’t have `DefaultConstructible` for the same reason we shouldn’t have “Plusable” to represent something that lets you write `x + x`.

## The semantics of `Equatable`

Take the [`Equatable`](http://swiftdoc.org/v3.0/protocol/Equatable/) protocol as an example. Its API is minimal — just a single function:

```
public protocol Equatable {
    /// Returns a Boolean value indicating whether two values are equal.
    ///
    /// Equality is the inverse of inequality. For any values `a` and `b`,
    /// `a == b` implies that `a != b` is `false`.
    static func == (lhs: Self, rhs: Self) -> Bool
}
```

Yet, by conforming a type to `Equatable` you also guarantee that your implementation follows the protocol’s _semantics_, which are listed [in its documentation](http://swiftdoc.org/v3.0/protocol/Equatable/). In short, these are:

- Equality implies substitutability — any two instances that compare equally can be used interchangeably in any code that depends on their values.
- To maintain substitutability, the `==` operator should take into account _all visible aspects_ of an `Equatable` type.

  This means that if you write a `Person` struct with `firstName` and `lastName` properties and in your implementation of `==` you only use `firstName` to determine equality, you’re violating the contract laid down by the protocol’s semantics.
- `a==a` is always `true` (reflexivity); `a==b` implies b==a (symmetry); `a==b` and `b==c` implies `a==c` (transitivity).
- Inequality is the inverse of equality, so if you provide an (optional) custom implementation of the `!=` operator, you must guarantee that `a!=b` implies `!(a==b)`.

For class instances, it can make sense to base equality on instance identity ([`===`](http://swiftdoc.org/v3.0/operator/eqeqeq/#comment-func-eqeqeq_-anyobject-rhs_-anyobject)). It really depends on the characteristics of the type. See [these comments by Jordan Rose](https://twitter.com/UINT_MIN/status/816691626613448708).

## Protocols should enable meaningful algorithms

[Xiaodi Wu](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/69):

> Again, protocols aren’t about just syntax but about semantics. One implication is that **it’s perfectly logical to have protocols with no syntax requirements at all**, i.e. `protocol MyProtocolWithSpecialSemantics { }`.^[1](#fn:error) Another implication, therefore, is that **Swift does not automatically conform types to a protocol simply because it implements all requirements, because there’s no way for the compiler to judge semantics.**

The requirements a protocol — particularly one that makes it into the standard library — defines should be both necessary and sufficient to implement _useful_ generic algorithms based on them.

Going back to the `DefaultConstructible` proposal, what interesting algorithm can you base on a protocol that guarantees only `T()` without semantics? None that I can think of.

# Is the idea of a generalized default value meaningful?

Alternatively, you can ask yourself what semantics you could ascribe to this protocol. Useful algorithms could emerge from the constraints set by a coherent set of semantics.

One problem with a generic `init()` requirement without additional context is that `T()` means very different things for different `T`:

- Some types have intuitive “empty” representations; these are a good match for a parameter-less initializer: `String()` creates an empty string; `Array()`, `Dictionary()`, and `Set()`, an empty collection.
- For the number and boolean types things are less clear. Why does [`Bool()`](http://swiftdoc.org/v3.0/type/Bool/#comment-init) initialize to `false` and not `true`? It seems almost arbitrary. All the number types initialize to `0`, which intuitively makes sense (`a + 0 == a`) until you realize that `1` would also be a valid choice (`a * 1 == a`).
- And then there are objects that aren’t values. For example, `UIView()` and `Thread()` create distinct objects with every invocation — although these objects are initialized with their properties set to “default” values, you can’t really speak of a “default” `UIView` or `Thread` object.

[Xiaodi Wu](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/58):

> [Afaict](https://en.wiktionary.org/wiki/AFAICT), there’s not much you can do with a default value that you couldn’t with `nil`, unless you have some guarantee as to _what_ that default is; however, I’d expect that in every case that you can rely on a guarantee about a default value which would be more useful than `nil`, it’s going to require more specific knowledge of your type than an all-encompassing `DefaultConstructible` can provide.

So some types have a meaningful default value and others don’t. You can’t assign coherent semantics to the concept of `init()` — unless you add context, that is.

## The semantics of `RangeReplaceableCollection`

There is already a protocol in the standard library that requires `init()`: [`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection). The difference to `DefaultConstructible` is that in the context of this protocol, `init()` has meaning. We know that the conforming type is a collection, and thus `T()` means “empty collection”. We can also assert that `T()` is equivalent to `someCollection.removeAll()`.

The fact that the context of `RangeReplaceableCollection` is necessary to ascribe the semantics is an indicator that the requirement should indeed be defined in this protocol and not be factored out into a separate protocol (which `RangeReplaceableCollection` would then refine).

[Dave Abrahams](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/98):

> With `DefaultConstructible`, you don’t know anything about the value of this `T`. There is nothing you can do with it, reliably. If the default constructability requirement is part of some larger protocol like `RangeReplaceableCollection`, then you can say things like, “this makes an empty collection,” and “a default-constructed instance is equivalent to an instance on which you’ve called removeAll.” That doesn’t argue for factoring the `init()` out into its own protocol. **It argues for including the `init()` requirement in every protocol where it forms an important part of the protocol’s semantic basis operations.**
> 
> […]
> 
> **There _is_ something wrong with slicing meaningful protocols up into bits that have only syntactic value, though. I suspect that’s what’s going on here.**

[And](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/101):

> Factoring out implementations is one thing, and definitely a good place for [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself). Factoring out requirements should only be done when the commonality enables some kind of generic programming. In fact, the opposite—clustering requirements together to create concepts (a.k.a. protocols)—is [an important part of the generic programming process](https://stlab.adobe.com/wiki/index.php/Runtime_Concepts#Concept).

## Conflicting protocols (same syntax, different semantics)

Another implication of this is that if there are two protocols whose requirements have (partially or fully) identical syntax _but different semantics_, one type shouldn’t conform to both protocols because there is no way to fulfill the semantics of both.

[Xiaodi Wu](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/92):

> In particular, I appreciate that there’s a huge amount of thought put into semantic meaning. The notion that protocols should carry semantics has been adhered to very strictly. This is why I think this proposal does do harm, because it explicitly rejects that very important idea, one that can only be upheld by people and not compilers.

# Without semantics, protocols reduce to reflection

> If it walks like a duck and quacks like a duck, it probably is a duck.
> 
> — The [duck typing](https://en.wikipedia.org/wiki/Duck_typing) rule of thumb.

As we’ve seen, duck typing is not the preferred way of thinking in Swift because the fact that an object has certain capabilities (as exhibited by implementing a particular API) says nothing about semantics.

[Xiaodi Wu argues](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/79) that the purpose of the proposed `DefaultConstructible` protocol would be better served by adding support for more powerful reflection capabilities to Swift:

> At base, you want a way of knowing if a type has `init()`. That sounds like reflection to me, not protocol conformance.

(The counterargument is that reflection [doesn’t give you compile-time safety](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4771/86).)

# Swift eschews default initialization of values to “zero”

The fourth argument against the `DefaultConstructible` protocol is that it clashes with Swift’s policy to not initialize values to “zero” or some other default. In contrast to many other languages, Swift doesn’t zero out memory for variables — the compiler forces the programmer to initialize every variable with an explicit value.

Following this philosophy, Swift versions of algorithms that rely on something like `DefaultConstructible` in other languages (e.g. [factories](https://en.wikipedia.org/wiki/Factory_method_pattern)) should generally pass the responsibility for constructing a default value to the caller.

[Tony Allevato argues](https://forums.swift.org/t/pitch-add-the-defaultconstructible-protocol-to-the-standard-library/4777/5) that you can do this very elegantly in Swift by passing the initializer as a function:

> There have been a couple times where I’ve written code that needed to generically serve instances of a type `T`, and in each of those cases—thanks to Swift’s support for first-class functions and initializers-as-functions—I found it to be cleaner to have my factory take a `() -> T` as a parameter and I pass `T.init` into that, rather than place constraints on `T` itself.

1. A good example of a “pure semantics” protocol is [`Error`](https://developer.apple.com/reference/swift/error). By adding `Error` conformance to a type, you communicate that you intend to use this type for error reporting. Example:

  ```
  extension String: Error { }

  // Later
  throw "File not found"
  ```

  [↩︎](#fnref:error)
