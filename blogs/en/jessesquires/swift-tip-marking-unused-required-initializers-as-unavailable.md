---
title: 'Swift tip: marking unused required initializers as unavailable'
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/05/20/marking-unused-required-initializers-as-unavailable/'
original_language: en
published: 2020-05-20
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d4b789df75b4aa4e'
translated: false
---

> 原文：[Swift tip: marking unused required initializers as unavailable](https://www.jessesquires.com/blog/2020/05/20/marking-unused-required-initializers-as-unavailable/)　·　Jesse Squires

Swift’s [strict initialization rules](https://docs.swift.org/swift-book/LanguageGuide/Initialization.html) are great. They help prevent an entire category of bugs that were especially common in Objective-C. However, when working with Objective-C frameworks, particularly `UIKit`, these rules can be frustrating.

When you subclass `UIViewController` and `UIView` and provide your own initializer, the compiler will prompt you to add the following `required` initializer:

```
required init?(coder: NSCoder) {
    fatalError("init(coder:) has not been implemented")
}
```

For view controllers, [`init(nibName:bundle:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621359-init) is the designated initializer, but [`init(coder:)`](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621403-init) is required by the [`NSCoding`](https://developer.apple.com/documentation/foundation/nscoding) protocol. It must be implemented not only because of the protocol, but because this is the initializer that Interface Builder calls when automatically instantiating `UIViewController` subclasses from storyboards or xibs. The same applies to `UIView` subclasses.

However, if you do not use Interface Builder, then `init(coder:)` is irrelevant and will never be called. It is annoying boilerplate. But the real problem is that Xcode (and presumably other editors) will offer `init(coder:)` as an auto-complete option when initializing your view or view controller. That is not ideal, because it is not a valid way to initialize your custom view or view controller. Luckily, you can use Swift’s [`@available` attribute](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html) to prevent this, which also has the benefit of more clearly communicating that you should not use this initializer.

```
@available(*, unavailable)
required init?(coder: NSCoder) {
    fatalError("\(#function) has not been implemented")
}
```

Now, at compile-time, this initializer is inaccessible. Or technically, at “auto-complete while you type time”.

You might have the idea of putting this in an extension or a protocol, so that you can avoid typing the boilerplate for every `UIView` and `UIViewController` subclass. Unfortunately, that is not possible because `required` initializers must be provided in subclass declarations. So, using `@available` is the best we can do.

**UPDATE:** Thanks to [JP for pointing out](https://twitter.com/simjp/status/1263202678663872513) that there’s a [SwiftLint rule](https://realm.github.io/SwiftLint/unavailable_function.html) for exactly this. Unfortunately, it does not currently support autocorrect.
