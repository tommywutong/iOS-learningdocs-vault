---
title: 'Thoughts on @dynamicMemberLookup'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/06/dynamic-member-lookup/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:db4bbe8ff73e5f8a'
translated: false
---

> 原文：[Thoughts on @dynamicMemberLookup](https://oleb.net/blog/2018/06/dynamic-member-lookup/)　·　Ole Begemann

# Thoughts on @dynamicMemberLookup

Possibly the most controversial new feature in Swift 4.2 is _dynamic member lookup_, introduced by [Swift Evolution proposal SE-0195](https://github.com/apple/swift-evolution/blob/master/proposals/0195-dynamic-member-lookup.md).

`@dynamicMemberLookup` is a new attribute that can be applied to a class, struct, enum, or protocol declaration.^[1](#fn:1) Instances of a `@dynamic​Member​Lookup` type can be called with _any_ property-style accessor (using dot notation) — the compiler won’t emit an error if a property with the given name doesn’t exist.

# Runtime lookup for properties

Instead, the compiler translates such accesses into calls of a special `subscript​(dynamicMember:)` subscript that gets passed the “non-existent” member name as a string. Inside the subscript’s implementation, the author of the type can do whatever they want to look up the appropriate return value at runtime.

Let’s look at a simple, if pointless, example. This type returns any member as an uppercased string:

```
@dynamicMemberLookup
struct Uppercaser {
    subscript(dynamicMember input: String) -> String {
        return input.uppercased()
    }
}

Uppercaser().hello // → "HELLO"
// You can type anything, as long as Swift accepts it as an identifier.
Uppercaser().käsesoße // → "KÄSESOSSE"
```

# The rules

Here are some non-obvious things you can do with `@dynamicMemberLookup`:

- **Provide a setter in addition to the getter.** This allows assignments through dynamic member lookup, or passing the subscript expression [`inout`](https://docs.swift.org/swift-book/LanguageGuide/Functions.html#ID173). For an example, check out [Doug Gregor’s](https://twitter.com/dgregor79) wrapper for [reading and writing environment variables](https://gist.github.com/DougGregor/68259dd47d9711b27cbbfde3e89604e8).
- **Choose any return type.** The subscript must have a single parameter, which can be any type that conforms to [`ExpressibleByStringLiteral`](https://developer.apple.com/documentation/swift/expressiblebystringliteral) but will likely be a [`String`](https://developer.apple.com/documentation/swift/string) 99 % of the time. The return type, though, can be anything you want, including generic parameters.
- **Provide multiple overloads of the subscript with different return types.** If there are multiple dynamic member subscripts, the compiler will pick the best match according to its normal type inference rules, or emit an error if the choice is ambiguous.

Here are some things you can’t do:

- **“Hide” a declared member of a type.** Declared properties always take precedence in the type checker over dynamic member lookup.
- **Retroactively support dynamic member lookup for a type you don’t control.** The attribute only works on the original type declaration.

# Interoperability with dynamic languages

The proposal and implementation of dynamic member lookup was largely driven by the [Swift for TensorFlow](https://github.com/tensorflow/swift) team at Google. Their main motivation is to facilitate interoperability between Swift and dynamic languages, specifically (though not exclusively) [Python](https://www.python.org). Their goal is to make it possible to call Python code from Swift with a pretty and familiar syntax.

The `@dynamic​Member​Lookup` proposal covers “only” half the distance toward this goal. The other half is a feature called [`@dynamic​Callable`](https://github.com/apple/swift-evolution/blob/master/proposals/0216-dynamic-callable.md), which will allow developers to declare types as dynamically “callable”, i.e. to be able to respond at runtime to a “function call” with an arbitrary argument list (optionally with labeled arguments). `@dynamic​Callable` didn’t make it into Swift 4.2, but [the proposal SE-0216](https://github.com/apple/swift-evolution/blob/master/proposals/0216-dynamic-callable.md) was [recently accepted](https://forums.swift.org/t/accepted-se-216-user-defined-dynamically-callable-types/14110) and the feature will be included in a future Swift release.

The Swift for Tensorflow team has written [a Swift–Python bridge](https://github.com/tensorflow/swift/blob/master/docs/PythonInteroperability.md) that will take advantage of these features once they ship. You can try out the Python bridge today by installing a [Swift for TensorFlow toolchain](https://github.com/tensorflow/swift/blob/master/Installation.md).

(It’s worth noting that since [Python has a C API](https://docs.python.org/2/c-api/) and Swift can call into C, neither `@dynamic​Member​Lookup` nor `@dynamic​Callable` are required to implement the actual Swift–Python bridge, but they make the resulting Swift syntax much nicer. Without them, chances are nobody would use the bridge because the syntax would be unacceptably verbose for anything more than a few isolated lines of code.)

Although Python has been the primary focus of the team that worked on the proposal, interop layers with other dynamic languages like Ruby or JavaScript will also be able to take advantage of it.

# Other use cases

And dynamic member lookup isn’t limited to this one use case, either. Any type that currently has a string-based subscript-style API could be converted to dynamic member lookup style.

## Example: strongly typed JSON

[SE-0195 uses a strongly typed `JSON` type as an example](https://github.com/apple/swift-evolution/blob/master/proposals/0195-dynamic-member-lookup.md#example-usage) that I’d like to repeat here with minor modifications. Suppose we have an enum to represent JSON data:

```
enum JSON {
    case number(Double)
    case string(String)
    case array([JSON])
    case dictionary([String: JSON])
}
```

(We only handle a subset of [valid JSON](https://www.json.org) for the example; feel free to add support for Boolean values and null.)

To make it easier to extract the data inside a `JSON` value, we can provide some accessors and two subscripts — one that takes an [`Int`](https://developer.apple.com/documentation/swift/int#) for indexing into an array and one that takes a `String` for drilling down into a dictionary:

```
extension JSON {
    var numberValue: Double? {
        guard case .number(let n) = self else {
            return nil
        }
        return n
    }

    var stringValue: String? {
        guard case .string(let s) = self else {
            return nil
        }
        return s
    }

    subscript(index: Int) -> JSON? {
        guard case .array(let arr) = self,
            arr.indices.contains(index) else
        {
            return nil
        }
        return arr[index]
    }

    subscript(key: String) -> JSON? {
        guard case .dictionary(let dict) = self else {
            return nil
        }
        return dict[key]
    }
}
```

Notice that the subscripts again return optional `JSON` values. This allows us to drill down into nested JSON data using optional chaining:

```
// [
//   {
//     "name": {
//       "first": "…",
//       "last": "…"
//     }
//   },
//   {
//     …
//   }
// ]
json[0]?["name"]?["first"]?.stringValue
```

Now let’s apply `@dynamicMemberLookup` to our type. The implementation is exactly the same as for the string-based subscript above:

```
@dynamicMemberLookup
enum JSON {
    ...

    subscript(dynamicMember key: String) -> JSON? {
        guard case .dictionary(let dict) = self else {
            return nil
        }
        return dict[key]
    }
}
```

This cleans up the syntax for drilling into a JSON dictionary very nicely into this:

```
json[0]?.name?.first?.stringValue
```

## Choosing the correct return type

Observe again that we as authors of the `JSON` type have full flexibility over the return type(s) of our dynamic member subscript(s). This gives us complete freedom^[2](#fn:2) how to handle unsuccessful lookups. Do you want your type to behave like a [`Dictionary`](https://developer.apple.com/documentation/swift/dictionary), returning `nil` when a key can’t be found? Make your return type [optional](https://developer.apple.com/documentation/swift/optional). Do you prefer trapping on invalid input? Make the return type non-optional and call [`fatalError`](https://developer.apple.com/documentation/swift/1538698-fatalerror) in your implementation.

This is why the proposal stresses that dynamic member lookup is fully type safe despite the fact that name resolution is happening at runtime and can obviously fail — the point is that (a) the author of a type has complete control over the runtime behavior, and (b) the user of the type can infer how to handle the return value from the subscript’s return type.

As we saw, returning the same type (as an optional or not) is going to be a popular choice because it allows chaining. The Python bridge also uses this pattern: [every return type is again a `PythonObject`](https://github.com/apple/swift/blob/683ffcd161bfaff295ecf6c30d3c9f60a9039cf8/stdlib/public/Python/Python.swift).

# It’s just syntactic sugar

It’s important to understand that `@dynamic​Member​Lookup` isn’t some sort of compiler magic. It just provides syntactic sugar, removing a few square brackets and quotations marks from your code. The invocation `Uppercaser()​.hello` is equivalent to `Uppercaser()​[dynamicMember: "hello"]` in every way.

# Is it worth it?

That brings me to the central question. Is the syntactic sugar worth it? Should you replace all your existing subscripts with `@dynamic​Member​Lookup`? I don’t think so.

Yes, the syntax is cleaner and more readable, but I’d argue this comes at the expense of clarity in most cases. By hiding a fundamentally “unsafe”^[3](#fn:3) string lookup behind the seemingly “safe” construct of member access using dot notation, you may give readers of your code the wrong impression that the compiler has been able to check your code for typos etc.^[4](#fn:4)

Syntax highlighting can help some: Xcode can color declared members differently than dynamic lookups. But not everyone can use an editor with good syntax highlighting, and even Xcode can’t help you if you accidentally insert a typo into a dynamic member lookup expression. (The same is true if you put a typo in a normal string-based subscript, of course. But at least it’s clear to readers of the code that this is a somewhat risky operation.)

Does `json[0]?.name?.first` read that much better to you than `json[0]?["name"]?["first"]` to be worth this tradeoff? It doesn’t to me.

# Conclusion

Dynamic member lookup is an indispensable feature for a small but important set of use cases where a clean syntax can make or break an API – namely, interfacing with dynamic languages and possibly dynamic proxies/message forwarding.

With dynamic member lookup, it’s not certain that the Python community will embrace Swift (or the Swift commmunity, Python). Without it, Swift wouldn’t even have a chance.

For all other applications, ask yourself if the clean syntax is really that much more readable than a normal subscript to be worth the downsides. Remember, dynamic member lookup is just syntactic sugar. It doesn’t enable any new functionality. In most situations, I think the answer should be “no”.

If misused, dynamic member lookup (and the associated “dynamic callable” proposal) has the potential to fundamentally change what constitutes Swift code in the minds of developers. It also has the potential to open Swift up to other communities and allow it to grow into fields where it isn’t a player at the moment. Let’s work on making the latter a reality.

1. Protocols annotated with `dynamic​Member​​Lookup` currently only compile if you provide a default implementation for the dynamic member subscript. [I filed a bug](https://bugs.swift.org/browse/SR-8077). [↩︎](#fnref:1)
2. Okay, almost complete freedom. [Throwing subscripts aren’t supported yet](https://bugs.swift.org/browse/SR-238). [↩︎](#fnref:2)
3. I’m using quotes for “unsafe” because as we saw, dynamic member lookup isn’t unsafe in Swift’s definition of the word. But it fundamentally remains a string-based lookup and prohibits refactoring and compiler checks. [↩︎](#fnref:3)
4. This argument has also been made during the proposal review, [most compellingly by Matthew Johnson](https://forums.swift.org/t/se-0195-introduce-user-defined-dynamic-member-lookup-types/8658/54).

  Others proposed to add a sigil (e.g. `^` as in `value^.member`) to distinguish dynamic lookups from compiler-checked lookups in the code. This was ultimately rejected as too intrusive. Olivier Halligon explores [how to recreate this behavior](http://alisoftware.github.io/swift/exploration/2018/06/14/exploring-dynamicmemberlookup/) in the confines of the design that shipped with Swift 4.2, using a custom postfix operator. [↩︎](#fnref:4)
