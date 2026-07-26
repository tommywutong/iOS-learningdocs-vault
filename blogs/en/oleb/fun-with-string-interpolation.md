---
title: Fun with String Interpolation
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/01/fun-with-string-interpolation/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d80593f8ae0720f0'
translated: false
---

> 原文：[Fun with String Interpolation](https://oleb.net/blog/2017/01/fun-with-string-interpolation/)　·　Ole Begemann

# Fun with String Interpolation

One of the first things you learn as a Swift programmer is [string interpolation](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/StringsAndCharacters.html#//apple_ref/doc/uid/TP40014097-CH7-ID292), or how to mix variables and expressions into string literals to build new strings:

```
let a = 6
let b = 12
let message = "\(a) × \(b) = \(a * b)"
// → "6 × 12 = 72"
```

What you may not know is that you can customize what string interpolation does when you initialize your own custom types with an interpolated string. This is what this article is about.

# Escaping unsafe strings

I’m going to use the task of escaping strings to sanitize (potentially) unsafe user input as an example.

## Motivation

Every program that handles data from external sources, such as text submitted by its users, must be prepared for this data to be used [as an attack vector](https://en.wikipedia.org/wiki/Cross-site_scripting) to compromise the program. For example, an attacker could enter a `<script>` tag as their username when registering an account. If the web app just renders this text verbatim, it just gave the attacker a way to execute an uncontrolled script, thus possibly allowing the attacker to steal other users’ session cookies. This is why a program must take care to sanitize all input it receives from external sources, e.g. by escaping HTML tags.

I came across [this tweet by Joel Spolsky](https://twitter.com/spolsky/status/815044634170785792) a few weeks ago where he links to a 2005 article of his titled [_Making Wrong Code Look Wrong_](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/). In the article, Spolsky argues for a particular style of naming variables that’s supposed to make it easier for the programmer to follow if a variable contains safe or unsafe (i.e. unescaped) text. It’s a good read and it includes a nice history lesson about [Hungarian notation](https://en.wikipedia.org/wiki/Hungarian_notation).

## Not all strings are equal

However, rather than try to follow a naming convention, the better (and safer) way to solve this problem in a strongly typed language like Swift would be to take advantage of the type system.

The source of the problem is that “unsafe strings” and “safe strings” are so fundamentally different that we should often treat them differently, yet we tend to use the same [`String`](https://developer.apple.com/reference/swift/string) type for both. So let’s introduce separate types for these concepts. I’m calling these `UnsafeString`^[1](#fn:1) and `SanitizedHTML`. Each uses a `String` as its internal storage:

```
/// An unescaped string from a potentially unsafe
/// source (such as user input)
struct UnsafeString {
    var value: String
}

/// A string that either comes from a safe source
/// (e.g. a string literal in the source code)
/// or has been escaped.
struct SanitizedHTML {
    fileprivate(set) var value: String

    init(unsafe input: UnsafeString) {
        value = SanitizedHTML.escaping(unsafe: input.value)
    }
}
```

We also provide an initializer to create a `SanitizedHTML` value from an `UnsafeString`, escaping the input in the process. The `escape` method replaces all angle brackets with their corresponding [HTML entities](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references). It’s very simple for this example, but it could be arbitrarily complex:

```
import Foundation // required for String.replacingOccurrences(of:with:)

extension SanitizedHTML {
    /// Escapes a string.
    fileprivate static func escaping(unsafe input: String) -> String {
        return input
            .replacingOccurrences(of: "<", with: "&lt;")
            .replacingOccurrences(of: ">", with: "&gt;")
    }
}
```

Note the differences in the declarations of the `value` property for the two types. For `UnsafeString`, `value` is a `var` because that’s often [what you want for value types](http://chris.eidhof.nl/post/structs-and-mutation-in-swift/) — you’re not giving up any of the safety (simple ownership model, values are copied on assignment) value types provide by doing that. In contrast, `SanitizedHTML`’s `value` property is modified with `fileprivate(set)` to make sure no third party can circumvent the type’s official API and inject an unescaped string value, while still permitting mutation from the type’s own implementation.^[2](#fn:2)

Let’s add a way to append new content to a sanitized string. We provide two overloads for the `append(_:)` method: one that takes an `UnsafeString` and one that takes another `SanitizedHTML`. For the latter, we can be sure the content is already sanitized so we don’t need to escape it again:

```
extension SanitizedHTML {
    mutating func append(_ other: SanitizedHTML) {
        // other is already safe
        value.append(other.value)
    }

    mutating func append(_ other: UnsafeString) {
        let sanitized = SanitizedHTML(unsafe: other)
        append(sanitized)
    }
}
```

## Allowing unescaped input from safe sources

We also need a way to add content to `SanitizedHTML` that we know is safe — you wouldn’t want the `<h1>` and `<p>` tags (or even the `<script>` tags) from your HTML template to be escaped. A convenient way to do this is via string [literals](https://en.wikipedia.org/wiki/Literal_%28computer_programming%29), i.e. constant strings in your source code. We can assume that string literals in the source code are always safe; if your source code is compromised, all bets are off in any case.^[3](#fn:3)

To add the ability for your type to be initialized with a string literal, add conformance to the [`ExpressibleByStringLiteral`](https://developer.apple.com/reference/swift/expressiblebystringliteral) protocol. The protocol is a little unwieldy because it requires three initializers, but they can generally forward to each other, so it sounds harder than it is:

```
// Initialization with a string literal should not escape the input.
extension SanitizedHTML: ExpressibleByStringLiteral {
    init(stringLiteral value: String) {
        self.value = value
    }
    init(unicodeScalarLiteral value: String) {
        self.init(stringLiteral: value)
    }
    init(extendedGraphemeClusterLiteral value: String) {
        self.init(stringLiteral: value)
    }
}
```

While we’re at it, it would be nice to have the same capability for `UnsafeString`. The implementation is identical to the one for `SanitizedHTML`:

```
extension UnsafeString: ExpressibleByStringLiteral {
    // Same implementation, see above
}
```

Now we can create `UnsafeString` and `SanitizedHTML` values from string literals. The type annotations are required because otherwise we’d get `String` values:

```
let userInput: UnsafeString = "<script>alert('P0wn3d');</script>"
var sanitized: SanitizedHTML = "<strong>Name:</strong> "
sanitized.append(userInput)
sanitized.value
// → "<strong>Name:</strong> &lt;script&gt;alert('P0wn3d');&lt;/script&gt;"
```

It works! The safe string literal has not been escaped, but the unsafe user input has.

# String Interpolation

We’re basically done now. If we make sure that all rendering APIs only accept `SanitizedHTML` as input, the new types make it impossible to accidentally render an unescaped string.

However, using the `SanitizedHTML` type would be even more convenient if we could initialize it via string interpolation, like this:

```
let sanitized2: SanitizedHTML = "<strong>Name:</strong> \(userInput)"
// error: cannot convert value of type 'String' to specified type 'SanitizedHTML'
```

Curently this results in a compile-time error. To be useful, this should also do the right thing, i.e. treat the literal portions of the interpolation string as safe and the expressions inside `\()` as unsafe.

## The odd `ExpressibleByStringInterpolation` protocol

As we shall see next, it is possible to make this work. The standard library provides another protocol we need to conform to: [`ExpressibleByStringInterpolation`](http://swiftdoc.org/v3.0/protocol/ExpressibleByStringInterpolation/). The protocol in its current form (as of Swift 3.0) [was deprecated in Swift 3](https://github.com/apple/swift-evolution/blob/master/proposals/0137-avoiding-lock-in.md) because the Swift team recognized it was [mis-designed](https://bugs.swift.org/browse/SR-1260) and [limited](https://bugs.swift.org/browse/SR-2303). This means we’ll get a warning if we use it and we need to be prepared to update our code with whatever new API [will replace it in Swift 4 or later](https://github.com/apple/swift/blob/master/docs/StringManifesto.md#string-interpolation) (which will likely be more powerful). Until then, the existing API is already surprisingly capable, albeit unintuitive.

The protocol requires adopters to provide two initializers. String interpolation is a two-step process:

1. In the first step, the compiler breaks the interpolation string into segments of string literals and variable expressions. The segments are then passed to the [`init<T>(stringInterpolationSegment:)`](http://swiftdoc.org/v3.0/protocol/ExpressibleByStringInterpolation/#comment-init-stringinterpolationsegment_) initializer.

  Note that the segments [always alternate between string literals and variable expressions](https://twitter.com/jckarter/status/815054320106283008), and the first segment is always a literal (which may be empty if the interpolation string begins with a variable). If two variable expressions are directly adjacent in the interpolation string, again an empty literal segment would be inserted in between.

  For example, the segments for this interpolation string:

  ```
  "\(name) says \(greeting1)\(greeting2)!"
  ```

  will be:

  ```
  ""
  name
  " says "
  greeting1
  ""
  greeting2
  "!"
  ```

  I don’t think this behavior is officially documented at the moment.
2. In the second interpolation step, the results of the first initializer are passed to the second initializer [`init(stringInterpolation:)`](http://swiftdoc.org/v3.0/protocol/ExpressibleByStringInterpolation/#comment-init-stringinterpolation_) in the order in which appear in the interpolation string.

  We can use the characteristic ordering of the segments to deduce that the even-numbered segments (starting at 0) are always string literals and thus safe, whereas the odd-numbered segments are unsafe and must be escaped.

## Conforming to `ExpressibleByStringInterpolation`

The odd thing about this API is that the first step in the interpolation process uses an initializer of the conforming type. This means we have to construct a valid `SanitizedHTML` value from each interpolation segment, only to then combine these segments into the finished value in step two. We need a place to store each segment inside `SanitizedHTML`, so let’s add another property to the type definition:

```
struct SanitizedHTML {
    fileprivate(set) var value: String
    // Required for string interpolation processing
    fileprivate var interpolationSegment: Any? = nil
    ...
}
```

The property’s type is `Optional<Any>`. `Any` because it should store any value that’s being passed in the interpolation string without converting it, and `Optional` because we only need it during the string interpolation process. In all other situations it will be `nil`.

Here’s the full implementation for both interpolation steps:

```
extension SanitizedHTML: ExpressibleByStringInterpolation {
    // Step 1
    public init<T>(stringInterpolationSegment expr: T) {
        // Store the segment
        interpolationSegment = expr
        // Dummy initialization, this is never used
        value = ""
    }

    // Step 2
    public init(stringInterpolation segments: SanitizedHTML...) {
        let stringSegments = segments.enumerated()
            .map { index, segment -> String in
                guard let segment = segment.interpolationSegment else {
                    fatalError("Invalid interpolation sequence")
                }
                if index % 2 == 0 {
                    // Even indices are literal segments
                    // and thus already safe.
                    if let string = segment as? String {
                        return string
                    } else {
                        return String(describing: segment)
                    }
                } else {
                    // Odd indices are variable expressions
                    switch segment {
                    case let safe as SanitizedHTML:
                        // Already safe
                        return safe.value
                    case let unsafe as UnsafeString:
                        return SanitizedHTML.escaping(unsafe: unsafe.value)
                    default:
                        // All other types are treated as unsafe too.
                        let unsafe = UnsafeString(value: String(describing: segment))
                        return SanitizedHTML(unsafe: unsafe).value
                    }
                }
        }
        value = stringSegments.joined()
    }
}
```

The initializer for step 1 stores the value it receives and leaves the actual conversion to step 2. Initializers must always initialize all properties, so we need to provide a dummy value for the `value` property, even though this instance will never outlive step 2.

In step 2, we receive the segments as an array of `SanitizedHTML` values. Our goal is to convert these values to strings, escaping the variable expression segments in the process. We can then join the strings together and assign the result to our `value` property. We map over the array and its indices and use our knowledge that even indices are safe. We also know that even indices are already strings, but just to be safe we check and convert the segment to a string if necessary.

For the odd indices, we distinguish three cases: if the segment is already a `SanitizedHTML` value, return its value directly without escaping it again; if the segment is an `UnsafeString`, escape it and return the result; if the segment has any other type (such as `String` or `Int`), construct an `UnsafeString` from it first and then escape that.

We could extend this further and add custom logic for sequences of `SanitizedHTML` values, for example, but this is already very powerful. Let’s try the example from above again:

```
let sanitized2: SanitizedHTML = "<strong>Name:</strong> \(userInput)"
sanitized2.value
// → "<strong>Name:</strong> &lt;script&gt;alert('P0wn3d');&lt;/script&gt;"
```

Just as we wanted, string literals are passed through verbatim and variable expressions are escaped. Fantastic!

That’s it. To make the new types even more convenient to use, a good next step would be to add conformance to [`CustomStringConvertible`](https://developer.apple.com/reference/swift/customstringconvertible) and/or [`CustomDebugStringConvertible`](https://developer.apple.com/reference/swift/customdebugstringconvertible), but I leave that to you.

[The full code is available in a Gist](https://gist.github.com/ole/0ced09733c91768b745119efe5b0be6c). Paste it into a playground to play around with it.

# Conclusion

Customizing how your own types interpret an interpolation string is an extremely powerful feature, especially for [DSLs](https://en.wikipedia.org/wiki/Domain-specific_language). Building SQL queries or localized strings are just two examples where you could employ the same techniques ([here’s an implementation of the latter](https://gist.github.com/beccadax/79fa038c0af0cafb52dd) by Becca Royal-Gordon). Any task that needs strings built from components can probably profit from it.

It’s really cool that Swift makes this possible, even if the API is far from perfect. When the string interpolation API gets revamped in a future Swift version, it will likely become even more expressive and hopefully easier to use.

Special thanks to Jacob Bandes-Storch for [giving me the idea](https://twitter.com/jtbandes/status/815096781872607233) for this article.

1. I’m not super happy with the name `UnsafeString` because it clashes with the `UnsafePointer` etc. types in the standard library. In Swift, [_unsafe_ generally refers](https://www.raywenderlich.com/148569/unsafe-swift) to [memory safety](https://en.wikipedia.org/wiki/Memory_safety), i.e. types or functions that allow you to access memory without the language protecting you. `UnsafeString` deals with a different kind of unsafe behavior. [↩︎](#fnref:1)
2. Alternatively, you could declare the property as `var` and add a `willSet` [observer](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Properties.html#//apple_ref/doc/uid/TP40014097-CH14-ID262) that made sure to re-escape the value on each mutation. This would likely clash with other features we’re about to add, though — not all kinds of input should be escaped. [↩︎](#fnref:2)
3. For real-world use, sourcing safe strings only from literals isn’t enough since you probably want to load your HTML templates from files. In that case, add an initializer `init(knownSafe: String)` that you can use to put known-safe text into a `SanitizedHTML` value. You have to take care not to misuse it. [↩︎](#fnref:3)
