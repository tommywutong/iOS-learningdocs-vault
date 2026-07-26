---
title: Safeguarding Equatable implementations
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/dump-as-equatable-safeguard/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:8db2b9d60859d541'
translated: false
---

> 原文：[Safeguarding Equatable implementations](https://oleb.net/blog/2017/03/dump-as-equatable-safeguard/)　·　Ole Begemann

# Safeguarding Equatable implementations

Say you have a struct:

```
struct Person {
    var name: String
}
```

And you add conformance to [`Equatable`](https://developer.apple.com/reference/swift/equatable) like so:

```
extension Person: Equatable {
    static func ==(lhs: Person, rhs: Person) -> Bool {
        return lhs.name == rhs.name
    }
}
```

This works as you would expect:

```
Person(name: "Lisa") == Person(name: "Lisa") // → true
Person(name: "Lisa") == Person(name: "Bart") // → false
```

# `Equatable` conformance is fragile

Unfortunately, like the enum example I talked about [in the previous post](https://oleb.net/blog/2017/03/enums-equatable-exhaustiveness/), this conformance to `Equatable` is very fragile: every time you add a property to the struct, you have to remember to also update the implementation of the [`==` function](https://developer.apple.com/reference/swift/equatable/1539854). If you forget, your `Equatable` conformance will be broken, and depending on how good your tests are this bug has the potential to go undetected for a long time — the compiler won’t be able to help you here.

As an example, let’s add another field to the struct:

```
struct Person {
    var name: String
    var city: String
}
```

Since the `Equatable` implementation is unchanged, it’s enough for two persons to have the same name to compare equal — the `city` property is not taken into account at all:

```
let lisaSimpson = Person(name: "Lisa", city: "Springfield")
let lisaStansfield = Person(name: "Lisa", city: "Dublin")
lisaSimpson == lisaStansfield // → true!!!
```

Even worse, [_unlike_ the enum example](https://oleb.net/blog/2017/03/enums-equatable-exhaustiveness/), there’s no simple way to secure the `==` function against mistakes like this. The compiler has no equivalent to exhaustiveness checking for other contexts than a `switch` statement.[1](#fn:1)

# Asserting equality with `dump`

It occurred to me to use the standard library’s [`dump`](https://developer.apple.com/reference/swift/1641218-dump) function as a safeguard. `dump` is interesting because it uses [Swift’s reflection capabilities](https://developer.apple.com/reference/swift/mirror) to create a string representation of a value or object that includes all storage fields. It generally gives a more thorough picture of a value’s internals than its [`description`](https://developer.apple.com/reference/swift/customstringconvertible) or [`debugDescription`](https://developer.apple.com/reference/swift/customdebugstringconvertible). The output of `dump` looks like this:

```
dump(lisaSimpson)
// ▿ Person
//   - name: "Lisa"
//   - city: "Springfield"
```

Here’s a function that asserts that its two arguments have identical dump outputs:

```
/**
 Asserts that two expressions have the same `dump` output.

 - Note: Like the standard library's `assert`, the
   assertion is only active in playgrounds and `-Onone`
   builds. The function does nothing in optimized builds.
 - Seealso: `dump(_:to:name:indent:maxDepth:maxItems)`
 */
func assertDumpsEqual<T>(_ lhs: @autoclosure () -> T,
    _ rhs: @autoclosure () -> T,
    file: StaticString = #file, line: UInt = #line) {
    assert(String(dumping: lhs()) == String(dumping: rhs()),
           "Expected dumps to be equal.",
           file: file, line: line)
}

extension String {
    /**
     Creates a string from the `dump` output of the
     given value.
     */
    init<T>(dumping x: T) {
        self.init()
        dump(x, to: &self)
    }
}
```

**Update March 9, 2017:** Many thanks to Tim Vermeulen for [suggesting this version](https://twitter.com/tim_vermeulen/status/839651813884309505) of the function. It’s much simpler than my original version, which I [preserved in the appendix below](#zero-overhead-assertions-in-release-builds).

# Securing the `==` function

Now you can call `assertDumpsEqual` from your `==` function:

```
extension Person: Equatable {
    static func ==(lhs: Person, rhs: Person) -> Bool {
        // WRONG! Doesn't include city property!
        let areEqual = lhs.name == rhs.name
        // Safeguard: equal values should have equal dumps
        if areEqual {
            assertDumpsEqual(lhs, rhs)
        }
        return areEqual
    }
}
```

From now on the program will trap at runtime if two values that are equal according to your implementation have different `dump` outputs:

```
lisaSimpson == lisaStansfield
// Crash: assertion failed: Expected dumps to be equal.
```

![Screenshot of Xcode with the triggered assertion](https://oleb.net/media/xcode-assertion-equatable-dump-1270px.png)

<sub>The assertion caught the bug.</sub>

This gives you a much better chance to notice immediately that you forgot to include the `city` property in the `==` function. It’s not 100% safe, of course: a compile-time check would be better, and you still have to remember to actually call `assertDumpsEqual` from your `==` functions — but you only need to remember this once per type, not with every stored property you add.

**Update March 9, 2017:** The shape of the `==` functions that use this pattern will always be the same: test if the values are equal, if true perform the dump-based assertion, and finally return the result of the test. Tim Vermeulen [suggests](https://twitter.com/tim_vermeulen/status/839651813884309505) creating [a protocol that implements this pattern](https://gist.github.com/timvermeulen/afd4a6aa4eb1cfc39fa8496673dc24af) and exposes the actual equality test as a customization point. It’s an interesting alternative that saves you some boilerplate, at the cost of hiding what’s going on.

# Disadvantages

The biggest drawback of the solution might be that `dump` is not a perfectly reliable way to determine equality. It should be pretty good at avoiding [false negatives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives#False_negative_error), but you’ll probably see some [false positives](https://en.wikipedia.org/wiki/False_positives_and_false_negatives#False_positive_error), i.e. values that really _are equal_ but whose `dump` outputs are different. Prime candidates for false positives are `NSObject` subclasses for whom equality is _not_ based on object identity, but whose `description` contains their memory address (which is the default).

I checked a number of standard Swift types and Apple’s framework classes that are `Equatable`, and the ones I tested all worked well with this usage of `dump`. But you have to take care to override `description` in your own `NSObject` subclasses.

# Conclusion

If you can secure your `Equatable` implementations against regressions by using a linter, a static analysis tool, or a code-generation tool like [Sourcery](https://github.com/krzysztofzablocki/Sourcery), then by all means go for it. I don’t think there are currently any code analysis tools that would catch the problem I outlined here, however. The imperfect solution I presented here might help you catch some bugs until other, better tools become available.

**Update July 21, 2017:** The [encoding and decoding infrastructure](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md) introduced in Swift 4 provides an interesting alternative to `dump`. If a type conforms to `Encodable`, consider replacing the `dump` output with its encoded representation using an encoder of your choice, such as `JSONEncoder` or `PropertyListEncoder`.

# Appendix

## Examples of `dump` output for typical Swift and Objective-C types

```
dump([1,2,3])
// ▿ 3 elements
//   - 1
//   - 2
//   - 3
dump(1..<10)
// ▿ CountableRange(1..<10)
//   - lowerBound: 1
//   - upperBound: 10
dump(["key": "value"])
// ▿ 1 key/value pair
//   ▿ (2 elements)
//     - .0: "key"
//     - .1: "value"
dump("Lisa" as String?)
// ▿ Optional("Lisa")
//   - some: "Lisa"
dump(Date())
// ▿ 2017-03-08 14:08:27 +0000
//   - timeIntervalSinceReferenceDate: 510674907.82620001
dump([1,2,3] as NSArray)
// ▿ 3 elements #0
//   - 1 #1
//     - super: NSNumber
//       - super: NSValue
//         - super: NSObject
//   - 2 #2
//     - super: NSNumber
//       - super: NSValue
//         - super: NSObject
//   - 3 #3
//     - super: NSNumber
//       - super: NSValue
//         - super: NSObject
dump("Hello" as NSString)
// - Hello #0
//   - super: NSMutableString
//     - super: NSString
//       - super: NSObject
dump(UIColor.red)
// - UIExtendedSRGBColorSpace 1 0 0 1 #0
//   - super: UIDeviceRGBColor
//     - super: UIColor
//       - super: NSObject

// Dumps of UIFont objects _do_ include a memory address,
// but UIFont shares these objects internally, so this is
// not a problem.
let f1 = UIFont(name: "Helvetica", size: 12)!
let f2 = UIFont(name: "Helvetica", size: 12)!
f1 == f2 // → true
dump(f1)
// - <UICTFont: 0x7ff5e6102e60> font-family: "Helvetica"; font-weight: normal; font-style: normal; font-size: 12.00pt #0
//   - super: UIFont
//     - super: NSObject
dump(f2)
// - <UICTFont: 0x7ff5e6102e60> font-family: "Helvetica"; font-weight: normal; font-style: normal; font-size: 12.00pt #0
//   - super: UIFont
//     - super: NSObject

// Dumps of Swift classes _do not_ include a memory
// address:
class A {
    let value: Int
    init(value: Int) { self.value = value }
}
dump(A(value: 42))
// ▿ A #0
//   - value: 42

// NSObject subclasses _do_ include a memory address
// and hence are problematic:
class B: NSObject {
    let value: Int
    init(value: Int) {
        self.value = value
        super.init()
    }
    static func ==(lhs: B, rhs: B) -> Bool {
        return lhs.value == rhs.value
    }
}
dump(B(value: 42))
// ▿ <__lldb_expr_26.B: 0x101012160> #0
//   - super: NSObject
//   - value: 42

// Fix: override `description`:
extension B {
    override open var description: String {
        return "B: \(value)"
    }
}
dump(B(value: 42))
// ▿ B: 42 #0
//   - super: NSObject
//   - value: 42
```

## Zero-overhead assertions in release builds

In Swift, assertions should only be active in debug builds (use [`precondition`](https://developer.apple.com/reference/swift/1540960-precondition) for checks that should trap in release builds). `assertDumpsEqual` achieves this by piggybacking on the standard library’s `assert` function. For this to work well the function should not perform any work before or after calling `assert`. Passing an expensive expression to `assert` is okay, though: `assert` uses the [`@autoclosure`](https://developer.apple.com/library/prerelease/content/documentation/Swift/Conceptual/Swift_Programming_Language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-ID543) attribute for its arguments to make sure that the potentially expensive expressions are not evaluated when the function is called.

The `assertDumpsEqual` version shown above ([written by Tim Vermeulen](https://gist.github.com/timvermeulen/afd4a6aa4eb1cfc39fa8496673dc24af)) takes advantage of this by calling into a custom `String` initializer that creates the dumps (which is expensive). Here’s my original version that created the dumps inside the function:

```
/**
 Asserts that two expressions have the same `dump` output.

 - Note: The assertion is only active when the `DEBUG`
   conditional compilation flag is defined). Otherwise the
   function does nothing. Note that playgrounds and -Onone
   builds don't automatically set the `DEBUG` flag.
 */
func assertDumpsEqual<T>(_ lhs: @autoclosure () -> T,
    _ rhs: @autoclosure () -> T,
    file: StaticString = #file, line: UInt = #line) {
    #if DEBUG
        var left = "", right = ""
        dump(lhs(), to: &left)
        dump(rhs(), to: &right)
        assert(left == right,
            "Expected dumps to be equal.\nlhs: \(left)\nrhs:\(right)",
            file: file, line: line)
    #endif
}
```

The entire function body inside the [`#if DEBUG`](https://developer.apple.com/library/prerelease/content/documentation/Swift/Conceptual/Swift_Programming_Language/Statements.html#//apple_ref/doc/uid/TP40014097-CH33-ID538) block won’t be compiled unless the `DEBUG` conditional compilation flag is set. This would work if we could rely on the `DEBUG` flag always being set in unoptimized builds. Unfortunately, Xcode doesn’t set the flag automatically for playgrounds, nor is it set by default in debug builds with the Swift Package Manager.[2](#fn:2) The standard library’s [`assert`](https://developer.apple.com/reference/swift/1541112-assert) is smarter. It treats all unoptimized builds (including playgrounds) as assertion-worthy. [The way `assert` recognizes an unoptimized build](https://github.com/apple/swift/blob/master/stdlib/public/core/Assert.swift#L40-L53) is not officially available outside the stdlib, however, which is the reason why we should push the entire expensive computation into `assert`.

Before I saw Tim’s simple solution, my approach to achieve this was to put the code that generates and compares the dumps into a local closure, which we then “call” when we pass it to `assert`. The actual execution of the closure will only occur inside `assert` (and thus only in unoptimized builds) because `assert`’s argument is an `@autoclosure` too. It would look like this:

```
func assertDumpsEqual<T>(_ lhs: @autoclosure () -> T,
    _ rhs: @autoclosure () -> T,
    file: StaticString = #file, line: UInt = #line) {
    func areDumpsEqual() -> Bool {
        var left = "", right = ""
        // Error: Declaration closing over non-escaping
        // parameter may allow it to escape
        dump(lhs(), to: &left)
        // Error: Declaration closing over non-escaping
        // parameter may allow it to escape
        dump(rhs(), to: &right)
        return left == right
    }
    assert(areDumpsEqual(), "Expected dumps to be equal.",
           file: file, line: line)
}
```

This triggers a compiler error, though. The problem is that the compiler doesn’t permit us to capture the `lhs` and `rhs` arguments in a closure because they are [non-escaping](https://oleb.net/blog/2016/10/optional-non-escaping-closures/). In our case, the closure doesn’t actually escape the scope, but the compiler can’t verify this. To fix this, we can either (1) annotate `assertDumpsEqual`’s arguments with `@escaping`, or (2) use the [`withoutActuallyEscaping`](https://developer.apple.com/reference/swift/2827967-withoutactuallyescaping) function ([new in Swift 3.1](https://github.com/apple/swift/blob/master/CHANGELOG.md#swift-31)) to override the compiler. The function then looks like this:

```
/// - Note: Requires Swift 3.1 for `withoutActuallyEscaping`.
func assertDumpsEqual<T>(_ lhs: @autoclosure () -> T,
    _ rhs: @autoclosure () -> T,
    file: StaticString = #file, line: UInt = #line) {

    // Nested function is a workaround for SR-4188: `withoutActuallyEscaping`
    // doesn't accept `@autoclosure` argument. https://bugs.swift.org/browse/SR-4188
    func assertDumpsEqualImpl(lhs: () -> T, rhs: () -> T) {
        withoutActuallyEscaping(lhs) { escapableL in
            withoutActuallyEscaping(rhs) { escapableR in
                func areDumpsEqual() -> Bool {
                    var left = "", right = ""
                    dump(escapableL(), to: &left)
                    dump(escapableR(), to: &right)
                    return left == right
                }
                assert(areDumpsEqual(), "Expected dumps to be equal.",
                       file: file, line: line)
            }
        }
    }
    assertDumpsEqualImpl(lhs: lhs, rhs: rhs)
}
```

(The nested function is [a workaround for a bug](https://bugs.swift.org/browse/SR-4188): `withoutActuallyEscaping` currently doesn’t accept arguments that are autoclosures.)

1. Assuming that equality should generally be determined by looking at _all_ of a type’s _stored_ properties, it’s conceivable that the compiler could issue a warning in the future if an implementation of `==` doesn’t use all stored properties (if it turns out to be a significant source of bugs in practice). But nothing like this exists today. [↩︎](#fnref:1)
2. In SwiftPM, you can set the flag manually with `swift build -Xswiftc "-D" -Xswiftc "DEBUG"`. [↩︎](#fnref:2)
