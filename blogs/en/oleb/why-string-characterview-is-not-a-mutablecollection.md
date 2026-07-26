---
title: Why String.CharacterView is not a MutableCollection
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/02/why-is-string-characterview-not-a-mutablecollection/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9eb25a947c1b963d'
translated: false
---

> 原文：[Why String.CharacterView is not a MutableCollection](https://oleb.net/blog/2017/02/why-is-string-characterview-not-a-mutablecollection/)　·　Ole Begemann

# Why String.CharacterView is not a MutableCollection

[In the previous article](https://oleb.net/blog/2017/02/why-is-dictionary-not-a-mutablecollection/) I discussed why `Set` and `Dictionary` don’t conform to `MutableCollection` and `RangeReplaceableCollection`. Today I’d like to do the same for [`String.CharacterView`](https://developer.apple.com/reference/swift/string.characterview).

`CharacterView` does conform to [`RangeReplaceableCollection`](https://developer.apple.com/reference/swift/rangereplaceablecollection) but not to [`MutableCollection`](https://developer.apple.com/reference/swift/mutablecollection). Why? A string is clearly mutable; it seems logical that it should adopt this protocol. Again, we need to consider the protocol’s [semantics](https://oleb.net/blog/2016/12/protocols-have-semantics/).

[The documentation for `MutableCollection`](https://developer.apple.com/reference/swift/mutablecollection) specifies these requirements:

> The `MutableCollection` protocol allows changing the values of a collection’s elements but not the length of the collection itself. …
> 
> A value stored into a subscript of a `MutableCollection` instance must subsequently be accessible at that same position. That is, for a mutable collection instance `a`, index `i`, and value `x`, the two sets of assignments in the following code sample must be equivalent:
> 
> ```
> a[i] = x
> let y = a[i]
> // Must be equivalent to:
> a[i] = x
> let y = x
> ```

# Replacing characters can invalidate indices

Let’s try this with a `CharacterView`. We’ll start with an initial string `a` and an index `i` that points to the `"_"` character, which we want to replace with an emoji (our new value `x`):

```
var a = "Grinning face: _".characters
let i = a.index(of: "_")!
// Verify a[i]
a[i] // → "_"

let x: Character = "😀"
```

We can’t say `a[i] = x` to perform the replacement because of the missing `MutableCollection` conformance, but we can replicate the behavior with [`replaceSubrange(_:with:)`](https://developer.apple.com/reference/swift/string/1778790-replacesubrange):

```
// Workaround for a[i] = x
a.replaceSubrange(i...i, with: CollectionOfOne(x))

// The replacement worked:
String(a) // → "Grinning face: 😀"
// Now a[i] should still return "_":
a[i] // → "�" WRONG!
```

`a[i]` returns � (the [Unicode replacement character U+FFFD](https://codepoints.net/U+FFFD)), which is a sign that something went wrong. The call to `replaceSubrange` worked, but the index `i` is no longer valid. We can see why if we take a look at its underlying structure using the [`dump`](https://developer.apple.com/reference/swift/1539127-dump) function:

```
dump(i)
/* →
▿ Swift.String.CharacterView.Index
  ▿ _base: Swift.String.UnicodeScalarView.Index
    - _position: 15
  - _countUTF16: 1
*/
```

The index stores two values: a position in the string’s underlying storage (measured in UTF-16 code units) _and_ the length of the [`Character`](https://developer.apple.com/reference/swift/character) in UTF-16 code units. While the original character `"_"` had length 1, its emoji replacement is two UTF-16 code units long, which we can verify by computing a new index:

```
let newIndex = a.index(of: "😀")!
dump(newIndex)
/* →
▿ Swift.String.CharacterView.Index
  ▿ _base: Swift.String.UnicodeScalarView.Index
    - _position: 15
  - _countUTF16: 2
*/
```

So we saw that mutating a single `Character` can invalidate that `Character`’s index. Therefore `String.CharacterView` can’t conform to `MutableCollection` without violating the protocol’s semantics. `RangeReplaceableCollection` has different semantics, which is why `CharacterView` conforms to it.

# Character has a variable-length encoding

Let me add one more observation regarding the second invariant of `MutableCollection`, namely that mutation must not affect the collection’s length. `CharacterView` arguably fulfills this requirement: the length of a `Character` is always 1, so replacing one with another should maintain the string’s overall length.

However, the `Character`’s _size_ in the underlying storage [is not the same](https://oleb.net/blog/2016/08/swift-3-strings/) for [all characters](https://oleb.net/blog/2016/12/emoji-4-0/), so replacing a single `Character` can potentially make it necessary to move the subsequent text forward or backward in memory by a few bytes to make room for the replacement. This would make the simple subscript assignment potentially an [O(_n_)](https://en.wikipedia.org/wiki/Big_O_notation) operation, and subscripting is supposed to be O(1). The following quote is from [the documentation for `Collection`](https://developer.apple.com/reference/swift/collection):

> Types that conform to `Collection` are expected to provide the `startIndex` and `endIndex` properties and subscript access to elements as O(1) operations. Types that are not able to guarantee that expected performance must document the departure, because many collection operations depend on O(1) subscripting performance for their own performance guarantees.

Granted, this only talks about the subscript _getter_ and `MutableCollection` doesn’t say anything about the expected _setter_ performance, but it’s probably reasonable to assume it should have the same characteristics.

# Unicode edge cases

The final potential issue for `CharacterView`’s hypothetical `MutableCollection` conformance is [Unicode](https://en.wikipedia.org/wiki/Unicode) and the complexities it brings. The existence of [combining characters](https://en.wikipedia.org/wiki/Combining_character) means that replacing a single `Character` can actually change the string’s length (measured in `Character`s) if the new character combines with its preceding character.

In the following example, we replace the underscore in `"1_"` with [U+20E3 COMBINING ENCLOSING KEYCAP](https://codepoints.net/U+20E3), which then combines with the character before it:

```
var s = "1_".characters
s.count // → 2, as expected
let idx = s.index(of: "_")!

// U+20E3 COMBINING ENCLOSING KEYCAP
let keycap: Character = "\u{20E3}"

// Replace _ with keycap
s.replaceSubrange(idx...idx, with: [keycap])

// The keycap has combined with the preceding character:
String(s) // → "1⃣"
// Length is now 1
s.count // → 1
```

The resulting string `"1⃣"` is only 1 `Character` long, again violating the `MutableCollection` semantics. And accessing `s[idx]` would now crash because the index points to a position that no longer exists.

Arguably, the main point this example makes is not so much that it would violate the `MutableCollection` semantics, but that Unicode is complex and can easily be misused — you should generally not operate with combining marks separately from their base characters. If a few obscure Unicode-related edge cases were the only situations where a string type could not uphold a protocol’s semantics, this should probably not be reason enough not to adopt that protocol. Unicode is so complicated that there’s a good chance its features will never perfectly satisfy the constraints of a generic collection protocol.

For this reason, [`String` will probably become a `Collection` again in Swift 4](https://github.com/apple/swift/blob/master/docs/StringManifesto.md#string-should-be-a-collection-of-characters-again), acknowledging that some operations may violate strict `Collection` semantics for “degenerate” cases.

As we’ve seen, Unicode is not the deciding factor in this case, however. There are other things that make `CharacterView` incompatible with `MutableCollection` semantics.
