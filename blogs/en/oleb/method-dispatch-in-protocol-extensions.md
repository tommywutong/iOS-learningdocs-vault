---
title: Method Dispatch in Protocol Extensions
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/06/lily-ballard-swift-dispatch/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b319a9cf16551aa7'
translated: false
---

> 原文：[Method Dispatch in Protocol Extensions](https://oleb.net/blog/2016/06/lily-ballard-swift-dispatch/)　·　Ole Begemann

# Method Dispatch in Protocol Extensions

We learned in the [Protocol-Oriented Programming session at WWDC 2015](https://developer.apple.com/videos/play/wwdc2015-408/?time=1767) that Swift uses two different dispatch mechanisms for methods in protocol extensions.^[1](#fn:1) Methods that are _protocol requirements_ — that is, they are declared in the protocol itself — are dispatched dynamically, whereas methods that are not backed by a requirement use static dispatch.

I remember wondering last year why Swift made that distinction. It didn’t make sense to me and, [like others](https://nomothetis.svbtle.com/the-ghost-of-swift-bugs-future), I was concerned it had the potential for lots of hard-to-find bugs. (Turns out it hasn’t been a problem in practice for me so far.) I recently came across [this post by Lily Ballard](https://forums.swift.org/t/proposal-universal-dynamic-dispatch-for-method-calls/237/57) on [Swift Evolution](https://forums.swift.org/c/evolution/discuss) that includes the best explanation I have seen for why method dispatch in protocols works the way it does:

> [Protocol extensions] are strictly static typing, all the way. Which makes sense, because there’s no virtual function table (or in Swift terms, protocol witness table) to put the methods into. Extensions can provide default implementations of protocol methods because the type that conforms to the protocol puts the extension method implementation into its own protocol witness table (and they only do this if the type doesn’t already implement the method itself). Since the protocol witness table only contains things defined in the protocol itself, protocol extension methods that aren’t part of the protocol don’t get put anywhere. So invoking one of those methods has no possible virtual function table to check, the only thing it can do is statically invoke the method from the extension. And this is why you can’t override them (or rather, why your override isn’t called if the method resolution is done via the protocol).
> 
> The only way to make protocol extension methods work via virtual dispatch is to define a new protocol witness table for the extension itself, but types that were defined without being able to see the extension won’t know to create and populate this protocol witness table. […]
> 
> The only other solution that comes to mind is turning all protocol dispatch into dynamic dispatch, which I hope you’ll agree is not a good idea.

So essentially, while protocols have a virtual function table, protocol extensions do not, and cannot easily have one because a type adopting the protocol won’t necessarily know about all extensions at compile time and therefore cannot add the extension methods to its own vtable. Opinions may vary whether dispatching protocols dynamically all the time would be a viable alternative, but it’s clearly not what the Swift team has in mind for the language.

If you want to learn more about how Swift types are laid out internally in memory and what information they contain, take a look at [the Swift ABI document](https://github.com/apple/swift/blob/master/docs/ABI.rst). It’s very interesting.

1. [Watch the video](https://developer.apple.com/videos/play/wwdc2015-408/?time=1767) from minute 29:27. [↩︎](#fnref:1)
