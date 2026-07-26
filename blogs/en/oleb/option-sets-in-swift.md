---
title: Option Sets in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/09/swift-option-sets/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:b0710699564cf8e4'
translated: false
---

> 原文：[Option Sets in Swift](https://oleb.net/blog/2016/09/swift-option-sets/)　·　Ole Begemann

# Option Sets in Swift

Option sets are Swift’s answer to bit masks. In C and Objective-C, it’s common to represent a set of boolean options as a number of enum cases whose integer values are powers of two. You then use bit masking to select the desired options. For example, [`NSString`](https://developer.apple.com/reference/foundation/nsstring?language=objc) defines an [`NSStringCompareOptions`](https://developer.apple.com/reference/foundation/nsstringcompareoptions?language=objc) enum that is used to configure string comparisons:

```
typedef enum {
	NSCaseInsensitiveSearch = 1,
	NSLiteralSearch = 2,
	NSBackwardsSearch = 4,
	NSAnchoredSearch = 8,
	NSNumericSearch = 64,
	NSDiacriticInsensitiveSearch = 128,
	NSWidthInsensitiveSearch = 256,
	NSForcedOrderingSearch = 512,
	NSRegularExpressionSearch = 1024
} NSStringCompareOptions;
```

To perform a case-insensitive, backward search, you’d then combine the corresponding options, using a bitwise or:

```
NSStringCompareOptions options = NSCaseInsensitiveSearch | NSBackwardsSearch;
// → 5 (= 1 + 4)
```

# Using option sets

Swift imports this definition not as an [enum](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Enumerations.html#//apple_ref/doc/uid/TP40014097-CH12-ID145), but as a [struct](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/ClassesAndStructures.html#//apple_ref/doc/uid/TP40014097-CH13-ID82) that conforms to the [`OptionSet`](https://developer.apple.com/reference/swift/optionset) protocol. Why a struct and not an enum? Enums are great when the cases are _mutually exclusive_, i.e. only one option can be set at a time. But you can’t combine multiple enum cases into a single value in Swift — unlike in C, where an enum is treated like an integer by the compiler and can assume any value.

An option set struct uses the same efficient representation as a bit field in C, but it presents itself externally _as a set_ whose members are the selected options. This allows you to manipulate the bit field with standard [set operations](https://en.wikipedia.org/wiki/Set_(mathematics)#Basic_operations), such as testing for membership with [`contains`](https://developer.apple.com/reference/swift/optionset/1641006-contains) or combining two bit fields with [`union`](https://developer.apple.com/reference/swift/optionset/1641498-union). And because `OptionSet` inherits from [`ExpressibleByArrayLiteral`](https://developer.apple.com/reference/swift/expressiblebyarrayliteral), you can populate an option set with an array literal:

```
let options: NSString.CompareOptions = [.caseInsensitive, .backwards]
options.contains(.backwards)          // → true
options.contains(.regularExpression)  // → false
options.union([.diacriticInsensitive]).rawValue  :// → 133 (= 1 + 4 + 128)
```

# Conforming to `OptionSet`

How do you create your own option set type? The only requirements are a `rawValue` property of integer type and an initializer. For structs Swift will usually provide an automatic memberwise initializer for you, so you don’t have to write it yourself. The `rawValue` is the underlying storage for the bit field. The constants for the individual options should be static type properties that initialize the bit field with the appropriate value:

```
struct Sports: OptionSet {
    let rawValue: Int

    static let running = Sports(rawValue: 1)
    static let cycling = Sports(rawValue: 2)
    static let swimming = Sports(rawValue: 4)
    static let fencing = Sports(rawValue: 8)
    static let shooting = Sports(rawValue: 32)
    static let horseJumping = Sports(rawValue: 512)
}
```

Now you can create option sets like this:

```
let triathlon: Sports = [.swimming, .cycling, .running]
triathlon.contains(.swimming)  // → true
triathlon.contains(.fencing)   // → false
```

Note that the compiler doesn’t automatically assign ascending powers of two to the options you provide; it is your responsibility to do this correctly so that each option represents a single bit of the `rawValue`. If you assigned consecutive integers (1, 2, 3, …) to the options, it’d be impossible to distinguish between `.swimming` (which would have the value `3`) and `[.running, .cycling]` (which would be `1 + 2`).

The benefits of having to assign the values manually are (a) less magic, and (b) full control over the value for each option. It also allows you to provide additional properties for common combinations of options:

```
extension Sports {
    static let modernPentathlon: Sports =
        [.swimming, .fencing, .horseJumping, .shooting, .running]
}

let commonEvents = triathlon.intersection(.modernPentathlon)
commonEvents.contains(.swimming)    // → true
commonEvents.contains(.cycling)     // → false
```

# Option sets aren’t collections

`OptionSet` conformance doesn’t imply conformance to the [`Sequence`](https://developer.apple.com/reference/swift/sequence) or [`Collection`](https://developer.apple.com/reference/swift/collection) protocols, so you can’t use `count` to determine how many bits are set or iterate over the selected options in a `for` loop. Fundamentally, an option set remains a plain integer value.
