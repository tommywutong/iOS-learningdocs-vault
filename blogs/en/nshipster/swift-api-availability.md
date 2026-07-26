---
title: Swift API Availability
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/available/'
original_language: en
published: 2019-12-10
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:f26d3d2e2443eafb'
translated: false
---

> 原文：[Swift API Availability](https://nshipster.com/available/)　·　NSHipster (Mattt)

# [Swift API Availability](https://nshipster.com/available/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  December 10^th, 2019

Code exists in a world of infinite abundance. Whatever you can imagine is willed into being — so long as you know how to express your desires.

As developers, we know that code will eventually be compiled into software, and forced to compete in the real-world for allocation of scarce hardware resources. Though up until that point, we can luxuriate in the feeling of unbounded idealism… _well, mostly_. For software is not a pure science, and our job — in reality — is little more than shuttling data through broken pipes between leaky abstractions.

This week on NSHipster, we’re exploring a quintessential aspect of our unglamorous job: API availability. The good news is that Swift provides first-class constructs for dealing with these real-world constraints by way of `@available` and `#available`. However, there are a few nuances to these language features, of which many Swift developers are unaware. So be sure to read on to make sure that you’re clear on all the options available to you.

---

## @available

In Swift, you use the `@available` attribute to annotate APIs with availability information, such as “this API is deprecated in macOS 10.15” or “this API requires Swift 5.1 or higher”. With this information, the compiler can ensure that any such APIs used by your app are available to all platforms supported by the current target.

The `@available` attribute can be applied to declarations, including top-level functions, constants, and variables, types like structures, classes, enumerations, and protocols, and type members — initializers, class deinitializers, methods, properties, and subscripts.

### Platform Availability

When used to designate platform availability for an API, the `@available` attribute can take one or two forms:

- A “shorthand specification” that lists minimum version requirements for multiple platforms
- An extended specification that can communicate additional details about availability for a single platform

#### Shorthand Specification

```
@available(platform version , platform version ..., *)
```

- A platform; `iOS`, `macCatalyst`, `macOS` / `OSX`, `tvOS`, or `watchOS`, or any of those with `ApplicationExtension` appended _(e.g. `macOSApplicationExtension`)_.
- A version number consisting of one, two, or three positive integers, separated by a period (`.`), to denote the [major, minor, and patch version](https://semver.org).
- Zero or more versioned platforms in a comma-delimited (`,`) list.
- An asterisk (`*`), denoting that the API is available for all other platforms. An asterisk is always required for platform availability annotations to handle potential future platforms (_such as the [long-rumored `iDishwasherOS`](https://github.com/apple/swift/commit/0d7996f4ee1ce9b7f9f1ea1d2e3ad71394d91eb1#diff-f142ec4252ddcbeea5be368189f43481R25)_).

For example, new, cross-platform APIs introduced at [WWDC 2019](https://nshipster.com/wwdc-2019/) might be annotated as:

```
@available(macOS 10.15, iOS 13, watchOS 6, tvOS 13, *)
```

Shorthand specifications are a convenient way to annotate platform availability. But if you need to communicate more information, such as when or why an API was deprecated or what should be used as a replacement, you’ll want to opt for an extended specification instead.

### Introduced, Deprecated, Obsoleted, and Unavailable

```
// With introduced, deprecated, and/or obsoleted
@available(platform | *
          , introduced: version , deprecated: version , obsoleted: version
          , renamed: "..."
          , message: "...")

// With unavailable
@available(platform | *, unavailable , renamed: "..." , message: "...")
```

- A platform, same as before, or an asterisk (*) for all platforms.
- Either `introduced`, `deprecated`, and/or `obsoleted`…

    - An `introduced`version, denoting the first version in which the API is available
    - A `deprecated`version, denoting the first version when using the API generates a compiler warning
    - An `obsoleted`version, denoting the first version when using the API generates a compiler error
- …or `unavailable`, which causes the API to generate a compiler error when used
- `renamed` with a keypath to another API; when provided, Xcode provides an automatic “fix-it”
- A `message` string to be included in the compiler warning or error

Unlike shorthand specifications, this form allows for only one platform to be specified. So if you want to annotate availability for multiple platforms, you’ll need stack `@available` attributes. For example, here’s how the previous shorthand example can be expressed in multiple attributes:

```
@available(macOS, introduced: 10.15)
@available(iOS, introduced: 13)
@available(watchOS, introduced: 6)
@available(tvOS, introduced: 13)
```

---

Apple SDK frameworks make extensive use of availability annotations to designate new and deprecated APIs with each release of iOS, macOS, and other platforms.

For example, iOS 13 introduces a new [`UICollectionViewCompositionalLayout`](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout) class. If you jump to its declaration by holding command (⌘) and clicking on that symbol in Xcode, you’ll see that it’s annotated with `@available`:

```
@available(iOS 13.0, *)
open class UICollectionViewCompositionalLayout : UICollectionViewLayout { … }
```

This `@available` attribute tells the compiler that `UICollectionViewCompositionalLayout` can only be called on devices running iOS, version 13.0 or later _(with caveats; see note below)_.

If your app targets iOS 13 only, then you can use `UICollectionViewCompositionalLayout` without any special consideration. If, however, your deployment target is set below iOS 13 in order to support previous versions of iOS (as is the case for many existing apps), then any use of `UICollectionViewCompositionalLayout` must be conditionalized.

More on that in a moment.

### Swift Language Availability

Your code may depend on a new language feature of Swift, such as [property wrappers](https://nshipster.com/propertywrapper/) or [default enumeration case associated values](https://github.com/apple/swift-evolution/blob/master/proposals/0155-normalize-enum-case-representation.md#default-parameter-values-for-enum-constructors) — both new in Swift 5.1. If you want to support development of your app with previous versions of Xcode or for your Swift package to work for multiple Swift compiler toolchains, you can use the `@available` attribute to annotate declarations containing new language features.

When used to designate Swift language availability for an API, the `@available` attribute takes the following form:

```
@available(swift version)
```

Unlike platform availability, Swift language version annotations don’t require an asterisk (`*`); to the compiler, there’s one Swift language, with multiple versions.

## #available

In Swift, you can predicate `if`, `guard`, and `while` statements with an availability condition, `#available`, to determine the availability of APIs at runtime. Unlike the `@available` attribute, an `#available` condition can’t be used for Swift language version checks.

The syntax of an `#available` expression resembles that of an `@available` attribute:

```
if | guard | while #available(platform version , platform version ..., *) …
```

---

Now that we know how APIs are annotated for availability, let’s look at how to annotate and conditionalize code based on our platform and/or Swift language version.

---

## Working with Unavailable APIs

Similar to how, in Swift, [thrown errors must be handled or propagated](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html#ID512), use of potentially unavailable APIs must be either annotated or conditionalized code.

When you attempt to call an API that is unavailable for at least one of your supported targets, Xcode will recommend the following options:

- “Add `if #available` version check”
- “Add `@available` attribute to enclosing declaration” _(suggested at each enclosing scope; for example, the current method as well as that method’s containing class)_

Following our analogy to error handling, the first option is similar to prepending `try` to a function call, and the second option is akin to wrapping a statement within `do/catch`.

For example, within an app supporting iOS 12 and iOS 13, a class that subclasses `UICollectionViewCompositionalLayout` must have its declaration annotated with `@available`, and any references to that subclass would need to be conditionalized with `#available`:

```
@available(iOS 13.0, *)
final class CustomCompositionalLayout: UICollectionViewCompositionalLayout { … }

func createLayout() -> UICollectionViewLayout {
    if #available(iOS 13, *) {
        return CustomCompositionalLayout()
    } else {
        return UICollectionViewFlowLayout()
    }
}
```

Swift comprises many inter-dependent concepts, and crosscutting concerns like availability often result in significant complexity as various parts of the language interact. For instance, what happens if you create a subclass that overrides a property marked as unavailable by its superclass? Or what if you try to call a function that’s renamed on one platform, but replaced by an operator on another?

While it’d be tedious to enumerate every specific behavior here, these questions can and often do arise in the messy business of developing apps in the real world. If you find yourself wondering “what if” and tire of trial-and-error experimentation, you might instead try consulting the [Swift language test suite](https://github.com/apple/swift/blob/6663800cdc5e4d0d4d10c767a0f2f7fc426cfa1f/test/attr/attr_availability.swift) to determine what’s expected behavior.

Alternatively, you can surmise how things work generally from [Clang’s diagnostic text](https://clang.llvm.org/docs/DiagnosticsReference.html#wavailability):

`-Wavailability` Diagnostic Text

<sub>`-Wavailability` Diagnostic Text</sub>

warning:

‘unavailable’ availability overrides all other availability information

warning:

unknown platform A in availability macro

warning:

feature cannot be

| introduced |
|---|
| deprecated |
| obsoleted |

in B version C before it was

| introduced |
|---|
| deprecated |
| obsoleted |

in version E ; attribute ignored

warning:

use same version number separators ‘_’ or ‘.’; as in ‘major[.minor[.subminor]]’

warning:

availability does not match previous declaration

warning:

|  |
|---|
| overriding |

method

| introduced after |
|---|
| deprecated before |
| obsoleted before |

| the protocol method it implements |
|---|
| overridden method |

on B  
 ( C vs. D )

warning:

|  |
|---|
| overriding |

method cannot be unavailable on A when

| the protocol method it implements |
|---|
| its overridden method |

is available

## Annotating Availability in Your Own APIs

Although you’ll frequently interact with `@available` as a consumer of Apple APIs, you’re much less likely to use them as an API producer.

### Availability in Apps

Within the context of an app, it may be convenient to use `@available` deprecation warnings to communicate across a team that use of a view controller, convenience method, or what have you is no longer advisable.

```
@available(iOS, deprecated: 13, renamed: "NewAndImprovedViewController")
class OldViewController: UIViewController { … }

class NewAndImprovedViewController: UIViewController { … }
```

Use of `unavailable` or `deprecated`, however, are much less useful for apps; without any expectation to vend an API outside that context, you can simply remove an API outright.

### Availability in Third-Party Frameworks

If you maintain a framework that depends on the Apple SDK in some way, you may need to annotate your APIs according to the availability of the underlying system calls. For example, a convenience wrapper around [Keychain APIs](https://developer.apple.com/documentation/security/keychain_services) would likely annotate the availability of platform-specific biometric features like Touch ID and Face ID.

However, if your framework wraps SDK functionality in a way that doesn’t expose such implementation details, you might be able to opt-in to new features without affecting the availability for your own APIs. For example, an NLP library that delegates functionality to [`NSLinguisticTagger`](https://nshipster.com/nslinguistictagger/) could instead use [Natural Language framework](https://developer.apple.com/documentation/naturallanguage/) when available (as determined by `#available`), without any user-visible API changes.

### Availability in Swift Packages

If you’re writing Swift _qua_ Swift in a platform-agnostic way and distributing that code as a Swift package, you may want to use `@available` to give a heads-up to consumers about APIs that are on the way out.

Unfortunately, there’s currently no way to designate deprecation in terms of the library version (the list of platforms are hard-coded by the compiler). While it’s a bit of a hack, you could communicate deprecation by specifying an obsolete / non-existent Swift language version like so:

```
@available(swift, deprecated: 0.0.1, message: "Deprecated in 1.2.0")
func going(going: Gone...) {}
```

## Working Around Deprecation Warnings

As some of us are keenly aware, [it’s not currently possible to silence deprecation warnings in Swift](https://forums.swift.org/t/swift-should-allow-for-suppression-of-warnings-especially-those-that-come-from-objective-c/19216). Whereas in Objective-C, you could suppress warnings with `#pragma clang diagnostic push / ignored / pop`, no such convenience is afforded to Swift.

If you’re among the l33t coders who have “hard mode” turned on (“Treat Warnings as Errors” a.k.a. `SWIFT_TREAT_WARNINGS_AS_ERRORS`), but find yourself stymied by deprecation warnings, here’s a cheat code you can use:

```
class CustomView {
    @available(iOS, introduced: 10, deprecated: 13, message: "😪")
    func method() {}
}

CustomView().method() // "'method()' was deprecated in iOS 13: 😪"

protocol IgnoringMethodDeprecation {
    func method()
}

extension CustomView: IgnoringMethodDeprecation {}

(CustomView() as IgnoringMethodDeprecation).method() // No warning! 😁
```

---

As an occupation, programming epitomizes the post-scarcity ideal of a post-industrial world economy in the information age. But even so far removed from physical limitations, we remain inherently constrained by forces beyond our control. However, with careful and deliberate practice, we can learn to make use of everything available to us.
