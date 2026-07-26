---
title: KeyValuePairs
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/keyvaluepairs/'
original_language: en
published: 2019-11-19
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:dd05803780e04eb9'
translated: false
---

> 原文：[KeyValuePairs](https://nshipster.com/keyvaluepairs/)　·　NSHipster (Mattt)

# [Key​Value​Pairs](https://nshipster.com/keyvaluepairs/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  November 19^th, 2019

Cosmologies seek to create order by dividing existence into discrete, interdependent parts. Thinkers in every society throughout history have posited various arrangements — though [Natural numbers](https://en.wikipedia.org/wiki/Natural_number) being what they are, there are only so many ways to slice the ontological pie.

There are dichotomies like  [陰陽](https://en.wikipedia.org/wiki/Yin_and_yang) ( yīnyáng )  ( ☯ )  : incontrovertible and self-evident (albeit reductive). There are trinities, which position man in relation to heaven and earth. One might divide everything into four, [like the ancient Greeks](https://en.wikipedia.org/wiki/Classical_element) with the elements of earth, water, air, and fire. Or you could carve things into five, [like the Chinese](https://en.wikipedia.org/wiki/Wuxing_%28Chinese_philosophy%29) with  Wood ( 木 mù ) ,  Fire ( 火 huǒ ) ,  Earth ( 土 tǔ ) ,  Metal ( 金 jīn ) , and  Water ( 水 shuǐ ) . Still not satisfied? Perhaps the eight-part  [八卦](https://en.wikipedia.org/wiki/Bagua) (bāguà)  will provide the answers that you seek:

| Trigram | ☰ | ☱ | ☲ | ☳ | ☴ | ☵ | ☶ | ☷ |
|---|---|---|---|---|---|---|---|---|
| Nature | 天 ( Heaven ) | 澤 ( Lake / Marsh ) | 火 ( Fire ) | 雷 ( Thunder ) | 風 ( Wind ) | 水 ( Water ) | 山 ( Mountain ) | 地 ( Ground ) |

Despite whatever [galaxy brain](https://nshipster.com/secrets/) opinion we may have about computer science, the pragmatic philosophy of day-to-day programming more closely aligns with a mundane cosmology; less _imago universi_, more  [じゃんけん](https://en.wikipedia.org/wiki/Rock_paper_scissors) _jan-ken_  ( Rock-Paper-Scissors ✊🤚✌️ )  .

For a moment, ponder the mystical truths of fundamental Swift collection types:

> Arrays are ordered collections of values.   
>  Sets are unordered collections of unique values.   
>  Dictionaries are unordered collections of key-value associations. [The Book of Swift](https://docs.swift.org/swift-book/LanguageGuide/CollectionTypes.html)

Thus compared to the pantheon of [`java.util` collections](https://docs.oracle.com/javase/7/docs/api/java/util/package-summary.html) or [`std` containers](http://www.cplusplus.com/reference/stl/), Swift offers a coherent coalition of three. Yet, just as we no longer explain everyday phenomena strictly in terms of [humors](https://en.wikipedia.org/wiki/Humorism#Four_humors) or [æther](https://en.wikipedia.org/wiki/Aether_%28classical_element%29), we must reject this formulation. Such a model is incomplete.

We could stretch our understanding of sets to incorporate `OptionSet` (as explained in a [previous article](https://nshipster.com/optionset/)), but we’d be remiss to try and shoehorn `Range` and `ClosedRange` into the same bucket as `Array` — and that’s to say nothing of the panoply of [Swift Collection Protocols](https://nshipster.com/swift-collection-protocols) _(an article in dire need of revision)_.

This week on NSHipster, we’ll take a look at `KeyValuePairs`, a small collection type that challenges our fundamental distinctions between `Array`, `Set`, and `Dictionary`. In the process, we’ll gain a new appreciation and a deeper understanding of the way things work in Swift.

---

`KeyValuePairs` is a structure in the Swift standard library that — _surprise, surprise_ — represents a collection of key-value pairs.

```
struct KeyValuePairs<Key, Value>: ExpressibleByDictionaryLiteral,
                                  RandomAccessCollection
{
  typealias Element = (key: Key, value: Value)
  typealias Index = Int
  typealias Indices = Range<Int>
  typealias SubSequence = Slice<KeyValuePairs>

  …
}
```

This truncated declaration highlights the defining features of `KeyValuePairs`:

- Its ability to be expressed by a dictionary literal
- Its capabilities as a random-access collection

## KeyValuePairs as Expressible by Dictionary Literal

[Literals](https://nshipster.com/swift-literals/) allow us to represent values directly in source code, and Swift is rather unique among other languages by extending this functionality to our own custom types through protocols.

A dictionary literal represents a value as mapping of keys and values like so:

```
["key": "value"]
```

However, the term _“dictionary literal”_ is a slight misnomer, since a sequence of key-value pairs — not a `Dictionary` — are passed to the `ExpressibleByDictionaryLiteral` protocol’s required initializer:

```
protocol ExpressibleByDictionaryLiteral {
    associatedtype Key
    associatedtype Value

    init(dictionaryLiteral elements: (Key, Value)...)
}
```

This confusion was amplified by the existence of a `DictionaryLiteral` type, which was only recently renamed to `KeyValuePairs` in Swift 5. The name change served to both clarify its true nature and bolster use as a public API (and not some internal language construct).

You can create a `KeyValuePairs` object with a dictionary literal (in fact, this is the only way to create one):

```
let pairs: KeyValuePairs<String, String> = [
    "木": "wood",
    "火": "fire",
    "土": "ground",
    "金": "metal",
    "水": "water"
]
```

## KeyValuePairs as Random-Access Collection

`KeyValuePairs` conforms to `RandomAccessCollection`, which allows its contents to be retrieved by _(in this case, `Int`)_ indices. In contrast to `Array`, `KeyValuePairs` doesn’t conform to `RangeReplaceableCollection`, so you can’t append elements or remove individual elements at indices or ranges. This narrowly constrains `KeyValuePairs`, such that it’s effectively immutable once initialized from a dictionary literal.

These functional limitations are the key to understanding its narrow application in the standard library.

## KeyValuePairs in the Wild

Across the Swift standard library and Apple SDK, `KeyValuePairs` are found in just two places:

- A [`Mirror` initializer](https://developer.apple.com/documentation/swift/mirror/3128579-init) ([as discussed previously](https://nshipster.com/mirror/)):

```
struct Mirror {
    init<Subject>(_ subject: Subject,
                  children: KeyValuePairs<String, Any>,
                  displayStyle: DisplayStyle? = nil,
                  ancestorRepresentation: AncestorRepresentation = .generated)
}

typealias RGBA = UInt32
typealias RGBAComponents = (UInt8, UInt8, UInt8, UInt8)

let color: RGBA = 0xFFEFD5FF
let mirror = Mirror(color,
                    children: ["name": "Papaya Whip",
                               "components": (0xFF, 0xEF, 0xD5, 0xFF) as RGBAComponents],
                    displayStyle: .struct)

mirror.children.first(where: { (label, _) in label == "name" })?.value
// "Papaya Whip"
```

- The [`@dynamicCallable` method](https://github.com/apple/swift-evolution/blob/master/proposals/0216-dynamic-callable.md):

```
@dynamicCallable
struct KeywordCallable {
  func dynamicallyCall(withKeywordArguments args: KeyValuePairs<String, Int>) -> Int {
    return args.count
  }
}

let object = KeywordCallable()
object(a: 1, 2) // desugars to `object.dynamicallyCall(withKeywordArguments: ["a": 1, "": 2])`
```

On both occasions, `KeyValuePairs` is employed as an alternative to `[(Key, Value)]` to enforce restraint by the caller. Without any other public initializers, `KeyValuePairs` can only be constructed from dictionary literals, and can’t be constructed dynamically.

## Working with KeyValuePairs Values

If you want to do any kind of work with a `KeyValuePairs`, you’ll first want to convert it into a conventional `Collection` type — either `Array` or `Dictionary`.

### Converting to Arrays

`KeyValuePairs` is a `Sequence`, by virtue of its conformance to `RandomAccessCollection` (and therefore `Collection`). When we pass it to the corresponding `Array` initializer, it becomes an array of its associated `Element` type (`(Key, Value)`).

```
let arrayOfPairs: [(Key, Value)] = Array(pairs)
```

Though, if you just want to iterate over each key-value pair, its conformance to `Sequence` means that you can pass it directly to a `for-in` loop:

```
for (key, value) in pairs {
    …
}
```

You can always create an `Array` from a `KeyValuePairs` object, but creating a `Dictionary` is more complicated.

## Converting to Dictionaries

There are four built-in types that conform to `ExpressibleByDictionaryLiteral`:

- `Dictionary`
- `NSDictionary`
- `NSMutableDictionary`
- `KeyValuePairs`

Each of the three dictionary types constitutes a [surjective mapping](https://en.wikipedia.org/wiki/Surjective_function), such that every value element has one or more corresponding keys. `KeyValuePairs` is the odd one out: it instead maintains an ordered list of tuples that allows for duplicate key associations.

`Dictionary` got a number of convenient initializers in Swift 4 thanks to [SE-0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md) _(thanks, [Nate](https://nshipster.com/authors/nate-cook/)!)_, including `init(uniqueKeysWithValues:)`, `init(_:uniquingKeysWith:)`, and `init(grouping:by)`

Consider the following example that constructs a `KeyValuePairs` object with a duplicate key:

```
let pairsWithDuplicateKey: KeyValuePairs<String, String> = [
    "天": "Heaven",
    "澤": "Lake",
    "澤": "Marsh",
    …
]
```

Attempting to pass this to `init(uniqueKeysWithValues:)` results in a fatal error:

```
Dictionary<String, Int>(uniqueKeysWithValues: Array(pairsWithDuplicateKey))
// Fatal error: Duplicate values for key: '澤'
```

Instead, you must either specify which value to map or map each key to an array of values:

```
Dictionary(Array(pairsWithDuplicateKey),
                 uniquingKeysWith: { (first, _) in first })
// ["澤": "Lake", …]

Dictionary(Array(pairsWithDuplicateKey),
                 uniquingKeysWith: { (_, last) in last })
// ["澤": "Marsh", …]

Dictionary(grouping: Array(pairsWithDuplicateKey),
           by: { (pair) in pair.value })
// ["澤": ["Lake", "Marsh"], …]
```

---

Outside of its narrow application in the standard library, `KeyValuePairs` are unlikely to make an appearance in your own codebase. You’re almost always better off going with a simple `[(Key, Value)]` tuple array.

Much as today’s [Standard Model](https://en.wikipedia.org/wiki/Standard_Model) more closely resembles the cacophony of a [zoo](https://en.wikipedia.org/wiki/Particle_zoo) than the _musica universalis_ of [celestial spheres](https://en.wikipedia.org/wiki/Celestial_spheres), `KeyValuePairs` challenges our tripartite view of Swift collection types. But like all cosmological exceptions — though uncomfortable or even unwelcome at times — it serves to expand our understanding.

That’s indeed its key value.
