---
title: 'Friday Q&A 2017-10-06: Type-Safe User Defaults'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-10-06-type-safe-user-defaults.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b02b28a3bceaff19'
translated: false
---

> 原文：[Friday Q&A 2017-10-06: Type-Safe User Defaults](https://www.mikeash.com/pyblog/friday-qa-2017-10-06-type-safe-user-defaults.html)　·　mikeash.com Friday Q&A

Posted at 2017-10-06 12:55 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [The Complete Friday Q&A Volumes II and III Are Out!](https://www.mikeash.com/pyblog/the-complete-friday-qa-volumes-ii-and-iii-are-out.html)  
Previous article: [Friday Q&A 2017-09-22: Swift 4 Weak References](https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-10-06: Type-Safe User Defaults

by [Mike Ash](https://www.mikeash.com/)

**User Defaults**  
`NSUserDefaults`, or just `UserDefaults` in Swift, is a typical dynamically-typed string-oriented Objective-C API. It stores string keys and property list values. This is perfectly fine, but I wanted to do better. I came up with this wishlist:

1. by declaring string constants, but it's easy to get lazy and not do it.
2. There should be no repetition in the common case. A key's string should automatically be made to match its identifier in the code.
3. No casting should be required. Keys should have a value type associated with them and the conversion handled internally.
4. .
5. .
6. Default values should be specified as part of the key rather than registered separately.
7. The value should be made available as a property so that it can be the target of mutating methods and operators.

I managed to hit all of these points, although the implementation is somewhat gnarly.

**Code**  
As usual, the code is available on GitHub if you want to play with it or see it all in one place:

[https://github.com/mikeash/TSUD](https://github.com/mikeash/TSUD)

**Example Use**  
Before we get into the implementation, let's take at what it looks like to use this API. That will inform the implementation choices and make it clearer why things work the way they do.

To declare a key, write a `struct` conforming to the `TSUD` protocol. Inside, implement a single `static` property called `defaultValue` which contains the value to be returned if `UserDefaults` doesn't contain a value:

```
    struct fontSize: TSUD {
        static let defaultValue = 12.0
    }
```

To read or write the value, use the `value` property on the `struct`:

```
    let font = NSFont.systemFont(ofSize: fontSize.value)
    fontSize.value = 14.0
```

Since `value` is just a property, you can do disturbing and unnatural things like `+=` to it.

```
    fontSize.value += 5.0
```

If you want to be able to detect the lack of a value and handle it specially rather than getting a default value, declare `defaultValue` to be optional and set it to `nil`:

```
    struct username: TSUD {
        static let defaultValue: String? = nil
    }
```

Then use it like any other optional:

```
    if let username = username.value {
        field.string = username
    } else {
        username.value = promptForUsername()
    }
```

By default, `TSUD` types correspond to a `UserDefaults` key matching their type name. These examples would be stored under `"fontSize"` and `"username"`. If you need to override this (for example, because you want to access a key that has a space in it, or you don't like the key's capitalization in your code), implement the `stringKey` property:

```
    struct hasWidgets: TSUD {
        static let defaultValue = false
        static let stringKey = "Has Widgets"
    }
```

Arbitrary `Codable` types are supported. They are encoded as property list objects:

```
    struct Person: Codable {
        var name: String
        var quest: String
        var age: Int
    }

    struct testPerson: TSUD {
        static let defaultValue: Person? = nil
    }
```

If you prefer, you can also use methods to get and set the value:

```
    if hasWidgets.get() {
        hasWidgets.set(false)
    }
```

These methods allow you to specify the `UserDefaults` object to work with, in the unlikely event that you want to work with something other than `UserDefaults.standard`:

```
    let otherDefaults = UserDefaults(suiteName: "...")!
    if hasWidgets.get(otherDefaults) {
        // That other thing has widgets!
    }
```

If you want to access the value in another `UserDefaults` instance as a mutable value, there's a subscript which takes a `UserDefaults` instance and provides the value. Unfortunately, Swift doesn't allow `static` subscripts, so you have to instantiate the key type:

```
    fontSize()[otherDefaults] += 10.0
```

**Implementation**  
We'll start with the protocol itself. It contains an `associatedtype` for the value type, an empty `init` method so the type can be instantiated, and the two properties discussed above:

```
    public protocol TSUD {
        associatedtype ValueType: Codable

        init()

        static var defaultValue: ValueType { get }

        static var stringKey: String { get }
    }
```

We'll provide a default implementation for `stringKey` that uses the type name:

```
    public extension TSUD {
        static var stringKey: String {
            let s = String(describing: Self.self)
```

In certain circumstances, Swift adds a little numeric tag at the end like `"hasWidgets #1"` If this name contains one, we strip it off. Otherwise we return the name directly:

```
            if let index = s.index(of: " ") {
                return String(s[..<index])
            } else {
                return s
            }
        }
    }
```

Later on, we'll need the ability to detect whether a value of `ValueType` is an `Optional` set to `nil`. This is not as easy as checking it with `== nil`, because it needs to work with arbitrary types wrapped in an `Optional`. The best technique I could find was to create a small protocol with an `isNil` property, and make `Optional` conform to it. Code that wants to check for `nil` can attempt to cast to the protocol, check `isNil` on success, and assume `false` on failure:

```
    private protocol OptionalP {
        var isNil: Bool { get }
    }

    extension Optional: OptionalP {
        var isNil: Bool { return self == nil }
    }
```

The main API of `TSUD` is implemented in an extension:

```
    extension TSUD {
```

Getting and setting the value is implemented with subscripting. This calls helper methods to encode and decode the value:

```
        public subscript(nsud: UserDefaults) -> ValueType {
            get {
                return decode(nsud.object(forKey: Self.stringKey)) ?? Self.defaultValue
            }
            nonmutating set {
                nsud.set(encode(newValue), forKey: Self.stringKey)
            }
        }
```

The `get` and `set` methods call through to the subscript. Because these are `static` methods and we can't have a `static` subscript, these instantiate `self` using the empty `init()` in the protocol:

```
        public static func get(_ nsud: UserDefaults = .standard) -> ValueType {
            return self.init()[nsud]
        }

        public static func set(_ value: ValueType, _ nsud: UserDefaults = .standard) {
            self.init()[nsud] = value
        }
```

`value` is a computed property that calls `get` and `set`:

```
        public static var value: ValueType {
            get {
                return get()
            }
            set {
                set(newValue)
            }
        }
```

The `encode` method takes care of transforming a value to a property list object suitable for `UserDefaults`:

```
        private func encode(_ value: ValueType) -> Any? {
```

There are some special cases to handle. First, if `ValueType` is an optional and `value` contains `nil`, we return nil:

```
            switch value {
            case let value as OptionalP where value.isNil: return nil
```

`Date` and `Data` are returned unchanged. For some reason, `Date`'s implementation of `Codable` encodes its value as a raw number, even though property lists support `Date` values natively. Likewise, `Data` encodes its value as an array of numbers even though `Data` is a valid property list type. We get past that by avoiding any encoding for these types. It's possible that more property list types need this treatment, in which case it's easy to add them here:

```
            case is Date: return value
            case is Data: return value
```

All other values get encoded. We use `PropertyListEncoder` to encode the value:

```
            default:
                let data = try? PropertyListEncoder().encode([value])
```

If this fails, we'll return `nil`:

```
                guard let dataUnwrapped = data else { return nil }
```

You'll notice that we're not encoding the value directly, but rather an array containing the value. For some reason, `PropertyListEncoder` does not support numbers or dates as top-level objects. Wrapping them in an array convinces it to work. We'll extract it back out afterwards.

Unfortunately, there's a bit of an impedence mismatch here. `PropertyListEncoder` produces binary data in property list format, but we want property list _objects_ which can be passed to `UserDefaults`. We'll turn that data back into objects by using `PropertyListSerialization`:

```
                let wrappedPlist = (try? PropertyListSerialization.propertyList(from: dataUnwrapped, options: [], format: nil)) as? [Any]
```

This is really ugly. It's unfortunate that `PropertyListEncoder` doesn't have an option to skip the serialization step and provide objects directly. We could make our own, but that's more ambitious than I was willing to get for this.

Once we have the property list object, we can index into the wrapper array to fetch the object we actually want:

```
                return wrappedPlist?[0]
            }
        }

            let data = try? PropertyListEncoder().encode([value])
            guard let dataUnwrapped = data else { return nil }
            let wrappedPlist = (try? PropertyListSerialization.propertyList(from: dataUnwrapped, options: [], format: nil)) as? [Any]
            return wrappedPlist?[0]
```

Decoding is the same thing in reverse. The `decode` method takes an optional to make it easier to handle `nil` from `UserDefaults`. It returns a `nil` value in that case:

```
        private func decode(_ plist: Any?) -> ValueType? {
            guard let plist = plist else { return nil }
```

As with encoding, decoding a `Date` or `Data` is special-cased to pass the value through:

```
            switch ValueType.self {
            case is Date.Type,
                 is Data.Type:
                return plist as? ValueType
```

For all other values, we'll use `PropertyListDecoder`. As with the encoder, there's no way to have `PropertyListDecoder` work on property list objects directly. It only works with data, so we have to encode the object as data, then decode that:

```
            default:
                let data = try? PropertyListSerialization.data(fromPropertyList: plist, format: .binary, options: 0)
                guard let dataUnwrapped = data else { return nil }
                return try? PropertyListDecoder().decode(ValueType.self, from: dataUnwrapped)
            }
        }
```

Unlike the encoder, the decoder is perfectly happy with a top-level number or date, so the array dance is not necessary on this end.

With encoding and decoding implemented, we've reached the end!

**Conclusion**  
This was a fun project for an NSCoderNight, and it's interesting to see just how far it can go. The result ends up looking pretty nice, although the problem it's solving isn't particularly pressing. This code is mostly intended as an educational experiment, but it could be used for practical purposes too.

That's it for today. Come back again for more terrifying tales of coding bravery. Friday Q&A is driven by reader ideas (some of them accidental), so as always, if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikaesh.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
