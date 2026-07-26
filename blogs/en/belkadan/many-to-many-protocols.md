---
title: Many-to-Many Protocols
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c8fb436bafae2222'
translated: false
---

> 原文：[Many-to-Many Protocols](https://belkadan.com/blog/2018/02/Many-to-Many-Protocols/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Color Palette #8](https://belkadan.com/blog/2018/01/Color-Palette-8/)

[My Little Optimization: The Compiler Is Magic](https://belkadan.com/blog/2018/03/My-Little-Optimization/) »

« [The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/?tag=programming-languages)

[Swift Regrets](https://belkadan.com/blog/2021/09/Swift-Regrets/?tag=programming-languages) »

« [The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/?tag=swift)

["FIXME" Doesn't Always Mean "Fix Me"](https://belkadan.com/blog/2018/04/FIXME/?tag=swift) »

## [Many-to-Many Protocols](#)

My colleague [Michael Ilseman](https://twitter.com/Ilseman) shared a design problem with me today, which came down to something like this:

Today, we have a protocol [RawRepresentable](https://developer.apple.com/documentation/swift/rawrepresentable), which says that “if I have a type `X`, I can convert it to and from `X.RawValue`”. You can then make a whole host of types that use `Int` as the raw value, and indeed that’s how Swift represents enums imported from Objective-C. (Well, those with an `NSInteger` underlying type, at least.) That makes this, in some sense, a “many-to-one” relation, because many types can have the same one raw value type. But what you _can’t_ do is make a single type have _multiple_ `RawValue` types—one of them has to claim the name `X.RawValue`.more

So, what can you do about it? One option is to make a one-off protocol that hardcodes one of the types, so that there’s no associated type to worry about. And indeed we have [LosslessStringConvertible](https://developer.apple.com/documentation/swift/losslessstringconvertible), which isn’t _quite_ the same as RawRepresentable with a `RawValue` type of `String`, but it’s pretty close. Now we can have types that have a custom `RawValue` and can also be converted to String. But that doesn’t really scale—one new protocol for each new type. Is there a better answer that works in today’s Swift?

It turns out that no, there’s not. The way Swift protocols work, you _have_ to pick one type—the `Self` type—to be the “anchor”, and then all the other types get associated with that. (Very deliberate word choice there.) The problem here ends up being similar to the punchline in my previous (very long) post “[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/)” (the section about lattices).

While there may not be a _better_ answer, there does exist _another_ answer, and you can even express it in today’s Swift:

```
protocol ArbitraryConverter {
  associatedtype From
  associatedtype To
  
  // like `init?(rawValue: RawValue)`
  static func convert(_ value: From) -> To?
  // like `var rawValue: RawValue`
  static func unconvert(_ value: To) -> From
}

enum /*namespace*/ StringToInt: ArbitraryConverter {
  static func convert(_ value: String) -> Int? {
    return Int(value, radix: 10)
  }
  
  static func unconvert(_ value: Int) -> String {
    return String(value)
  }
}

extension Sequence {
  func tryConvertAll<Converter>(_ converter: Converter.Type) -> [Converter.To]
      where Converter: ArbitraryConverter, Converter.From == Self.Element {
    return self.compactMap { converter.convert($0) }
  }
}

["1", "2", "three"].tryConvertAll(StringToInt.self)
```

This lets you connect _any_ two types by using a third type, forming a “many-to-many” relation. However, you now have to name the relation explicitly. That is, I couldn’t just say `["1", "2", "three"].tryConvertAll(Int.self)`, because neither `String` nor `Int` knows about `StringToInt`. I have to actually write `StringToInt` somewhere at the call site.

(Please ignore the fact that `Int.init` can work in this particular case. This is all simplified for the purposes of this post, so if it feels contrived, rest assured that it is.)

So, with Swift’s current protocol system, this is as good as we’re going to get. We can represent many-to-one relations, like RawRepresentable, and if we’re clever we can usually use that to represent one-to-many relations, but many-to-many relations need to be explicitly named.

P.S. There is an upside to this, which is that this lets us have _multiple_ ways to convert a String to an Int. Sometimes that’s useful. (Maybe there’s one that can parse English spellings of numbers, so that `"three"` would actually convert to `3`.)

P.P.S. As mentioned in “[The New Kingdom of Nouns](https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/)”, there is a language that has first-class support for many-to-many relations: [ML](https://en.wikipedia.org/wiki/Standard_ML#Module_system) (with its “modules” and “signatures”). But my understanding is that ML’s answer to the problem is to say you _always_ need to name the relation, even when it’s many-to-one like RawRepresentable (with `RawValue`) or Sequence (with its `Element`). So it’s more consistent, but not necessarily easier to use.

This entry was posted on [February](https://belkadan.com/blog/2018/02) 26, [2018](https://belkadan.com/blog/2018) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages), [Swift](https://belkadan.com/blog/tags/swift)
