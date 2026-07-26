---
title: Making illegal states unrepresentable
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/03/making-illegal-states-unrepresentable/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ddc41940c6c08d85'
translated: false
---

> 原文：[Making illegal states unrepresentable](https://oleb.net/blog/2018/03/making-illegal-states-unrepresentable/)　·　Ole Begemann

# Making illegal states unrepresentable

## Did you know URLSession can return a response and an error at the same time?

[I’ve said before](https://oleb.net/blog/2015/07/swift-type-system/) that one of the main benefits of a strong type system is automatic and compiler-enforced documentation.

# Types as compiler-enforced documentation

An API with carefully chosen input and output types is easier to use because the types establish a kind of “upper bound” for the function’s behavior.

Consider the following Swift function signature as a simple example:

```
func / (dividend: Int, divisor: Int) -> Int
```

Without knowing anything about the function’s implementation, you can deduce that it must perform [integer division](http://mathworld.wolfram.com/IntegerDivision.html) because the return type is incapable of expressing fractional values. In contrast, if the function’s return type were [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber), which can express both integer and floating-point values, you’d have to trust that the behavior is adequately documented.

This technique of using types for documenting behavior becomes more and more useful as a type system’s expressiveness grows. If Swift had a `NonZeroInt` type[1](#fn:1) to express the concept of “any integer except zero”, the divide function might be declared like this:

```
func / (dividend: Int, divisor: NonZeroInt) -> Int
```

Because the type checker would no longer allow you to pass `0` as the divisor, you wouldn’t have to question how the function handles a division by zero error. Does it trap? Does it return a garbage value? This is something the first variant of the function must document separately.

# Make illegal states impossible

We can turn this insight into a general rule: **Use types to make illegal states unrepresentable in your program.**

If you want to learn more about how to do this, check out Brandon Williams and Stephen Celis’s new video series [Point-Free](https://www.pointfree.co). They talk a lot about this and related topics. The first eight episodes have been great and I highly recommend the subscription. You’ll learn a lot.

In [episode 4 on algebraic data types](https://www.pointfree.co/episodes/ep4-algebraic-data-types), Brandon and Stephen discuss how enums and structs (or tuples) can be combined to design types that can precisely represent the desired states but no more (making all invalid states unrepresentable). Towards the end of the episode, they mention Apple’s [`URLSession`](https://developer.apple.com/documentation/foundation/urlsession) API as a negative example of an API that doesn’t use types as well as it should, which brings me to this article’s subtitle.

# `URLSession`

Swift’s type system is much more expressive than Objective-C’s. However, many of Apple’s APIs don’t yet take full advantage of it, be it for lack of resources for updating old APIs or to maintain Objective-C compatibility.

Consider the commonly used [method for making a network request](https://developer.apple.com/documentation/foundation/urlsession/1410330-datatask) on iOS:

```
class URLSession {
    func dataTask(with url: URL,
        completionHandler: @escaping (Data?, URLResponse?, Error?) -> Void)
        -> URLSessionDataTask
}
```

The completion handler receives three optional values: [`Data?`](https://developer.apple.com/documentation/foundation/data), [`URLResponse?`](https://developer.apple.com/documentation/foundation/urlresponse) and [`Error?`](https://developer.apple.com/documentation/swift/error). That makes 2 × 2 × 2 = 8 possible states[2](#fn:2), but how many of those are legal?

To quote [Brandon and Stephen](https://www.pointfree.co/episodes/ep4-algebraic-data-types), there are a lot of representable states here that don’t make sense. Some are obviously nonsensical, and we can probably rely on Apple’s code to never call the completion handler with all values being `nil` or all being non-`nil`.

## Response and error can be non-`nil` at the same time

Other states are trickier, and here Brandon and Stephen made a small mistake: they assumed that the API will either return (a) a valid `Data` _and_ `URLResponse`, _or_ (b) an `Error`. After all, it shouldn’t be possible to get a non-`nil` response and an error at the same time. Makes sense, right?

It turns out that this is wrong. A `URLResponse` encapsulates the server’s [HTTP response headers](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html), and the `URLSession` API will always provide you with this value once it has received a valid response header, even if the request errors at a later stage (e.g. due to cancellation or a timeout). It’s thus expected behavior for the completion handler to contain a populated `URLResponse` _and_ a non-`nil` error value (but no `Data`).

If you’re familiar with `URLSession`’s delegate-based API this may not be surprising to you because there are separate delegate methods for [`didReceiveResponse`](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1410027-urlsession) and [`didReceiveData`](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/1411528-urlsession). And to be fair, [the documentation for `dataTask​(with:​completionHandler:)`](https://developer.apple.com/documentation/foundation/urlsession/1410330-datatask) also calls this case out:

> If a response from the server is received, **regardless of whether the request completes successfully or fails,** the response parameter contains that information.

Still, I bet this is a very popular misconception among Cocoa developers. Just in the past four weeks, I saw [two](https://davedelong.com/blog/2018/03/02/apple-networking-feedback/) blog [posts](https://ruiper.es/2018/03/03/ras-s2e1/) whose authors made the same mistake (or at least didn’t acknowledge the subtlety).

I absolutely love the irony in this: the fact that Brandon and Stephen, while pointing out a flaw in an API due to badly chosen types, made an honest mistake that _could have been prevented if the original API had used better types_, illustrates the point they were making beautifully: a more strictly-typed API can prevent accidental misuse.

## Sample code

If you want to check out `URLSession`’s behavior yourself, paste the following code into a Swift playground:

```
import Foundation
import PlaygroundSupport

// If this 404s, replace with a URL to any other large file
let bigFile = URL(string: "https://speed.hetzner.de/1GB.bin")!

let task = URLSession.shared.dataTask(with: bigFile) { (data, response, error) in
    print("data:", data as Any)
    print("response:", response as Any)
    print("error:", error as Any)
}
task.resume()

// Cancel download after a few seconds
DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
    task.cancel()
}

PlaygroundPage.current.needsIndefiniteExecution = true
```

The code starts downloading a large file and then cancels the request after a few seconds. As a result, the completion handler gets called with a non-`nil` response and error.

(This assumes that the specified timespan is long enough to receive the response headers from the server and too short for the download to complete. If you’re on a very slow or incredibly fast network, you may have to tweak the time parameter.)

## What is the correct type?

Brandon and Stephen published their own follow-up of the issue as part of [episode 9 of Point-Free](https://www.pointfree.co/episodes/ep9-algebraic-data-types-exponents). Their conclusion is that the “correct” parameter type for the completion handler is:

```
(URLResponse?, Result<Data, Error>)
```

I disagree because getting valid data but no response seems impossible. I think it should be:

```
Result<(Data, URLResponse), (Error, URLResponse?)>
```

Translation: you’ll either get data and a response (which is guaranteed to not be `nil`), _or_ an error and an optional response.

# The `Result` type

Admittedly, my suggestion conflicts with the definition of the [`Result` type](https://developer.apple.com/documentation/swift/result) in the standard library, which constrains the failure parameter to the [`Error` protocol](https://developer.apple.com/documentation/swift/error) — we can’t conform `(Error, URLResponse?)` to `Error` because tuples can’t conform to protocols. If you wanted to use represent this API using `Result`, you’d have to create a struct with two properties — underlying error and optional response — and conform that struct to `Error`.

The `URLSession` API is particularly tricky due to the unintuitive behavior of the `URLResponse` parameter, but pretty much all of Apple’s callback-based asynchronous APIs exhibit the same anti-pattern that the provided types make illegal states representable.

Now that the `Result` type is [part of the Swift standard library](https://github.com/apple/swift-evolution/blob/master/proposals/0235-add-result.md), Apple might be able to automatically import Cocoa APIs of the form `completionHandler: (A?, Error?) -> Void` as `(Result<A>) -> Void`, turning four representable states into two. Until then (if it ever happens), I encourage you to [do the conversion yourself](https://oleb.net/blog/2017/01/result-init-helper/).

On a longer timescale, Swift will get proper language support for working with asynchronous APIs someday. It’s likely that whatever solution the community and the Swift team come up with [will allow existing Cocoa APIs to be ported](https://gist.github.com/lattner/429b9070918248274f25b714dcfc7619#conversion-of-imported-objective-c-apis) to the new system, similar to how `NSError **` parameters in Objective-C are already imported into Swift as throwing functions. Don’t count on seeing this before Swift 6 at the earliest, though.

1. Nothing’s stopping you from defining a `NonZeroInt` type yourself, but there is no way to tell the compiler “raise an error if someone tries to initialize this type with zero”. You’d have to rely on runtime checks.

  Still, introducing types like this is often a good idea because _users_ of the type can rely on the stated invariants after initialization. I haven’t yet seen a `NonZeroInt` type in the wild; custom types for guaranteed-to-be-non-empty collections are somewhat more popular. [↩︎](#fnref:1)
2. I’m only counting “nil” or “non-nil” as possible states here. Obviously, a non-`nil` `Data` value can have an infinite number of possible states, and the same is true for the other two parameters. But these states aren’t interesting to us here. [↩︎](#fnref:2)
