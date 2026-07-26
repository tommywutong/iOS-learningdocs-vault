---
title: Improving multiplatform SwiftUI code
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2023/03/23/improve-multiplatform-swiftui-code/'
original_language: en
published: 2023-03-23
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:56e9360e970c3625'
translated: false
---

> 原文：[Improving multiplatform SwiftUI code](https://www.jessesquires.com/blog/2023/03/23/improve-multiplatform-swiftui-code/)　·　Jesse Squires

For multiplatform projects where I’m using [SwiftUI](https://developer.apple.com/xcode/swiftui/), it certainly makes developing for multiple platforms at once significantly faster. However, each of Apple’s platforms are different enough that eventually your codebase will be littered with `#if os()` checks.

I previously [wrote about](https://www.jessesquires.com/blog/2022/08/19/sharing-code-in-swiftui-apps/) sharing cross-platform code in SwiftUI apps where you need to bridge the differences between UIKit and AppKit for an app that runs on both iOS and macOS. I used the minor differences between `UIPasteboard` and `NSPasteboard` as an example. But API differences between platforms do not address all scenarios when you might need to make platform-specific changes. For example, UIKit is (partially) available on both watchOS and tvOS. And, SwiftUI is (obviously) available on all platforms.

One of the best examples of platform-specific differences is padding values for UI layout code. David Smith wrote last week [about “pixel perfect” design](https://www.david-smith.org/blog/2023/03/16/design-notes-32/) for one of his watch apps. While he was adjusting a UI layout for each watch device size rather than different platforms, the core issues are the same: UI layout code, even when adaptive, cannot always be universally applied.

What you end up with is _a lot_ of code that looks like this:

```
var body: some View {
    MyCustomView()
    #if os(iOS)
        .padding(10)
    #elseif os(watchOS)
        .padding(4)
    #else // macOS
        .padding(24)
    #endif
}
```

It is difficult to read, increases cognitive load, and Xcode’s default formatting for `#if os()` is terribly ugly. We can avoid having to write `#if os()` everywhere and make this code much easier to read at the same time with a simple extension.

```
extension Double {
    init(iOS: Self, watchOS: Self, macOS: Self) {
        #if os(iOS)
        self = iOS
        #elseif os(watchOS)
        self = watchOS
        #else // macOS
        self = macOS
        #endif
    }
}
```

Then our layout code simplifies to the following:

```
var body: some View {
    MyCustomView()
        .padding(Double(iOS: 10, watchOS: 4, macOS: 24))
}
```

It immediately becomes clear that we _always_ want some padding on this view and that the values are platform-specific. If you prefer, you could also extend this pattern directly to view modifiers. If we did this for `.padding()`, the resulting code would simplify further to:

```
var body: some View {
    MyCustomView()
        .padding(iOS: 10, watchOS: 4, macOS: 24)
}
```

We obviously can’t use this pattern in _every scenario_ where there are platform differences, but it does improve many situations. I’ve found this to be a great way to reduce using `#if os()` when platforms share the majority of UI code for a particular view. However, you should never hesitate to build entirely unique views for a specific platform when that’s necessary. In those situations, you can extract the `#if os()` check and platform differences into a new `View`.

```
struct MyPlatformSpecificView: View {

    var body: some View {
    #if os(iOS)
        self.body_iOS
    #else // macOS
        self.body_macOS
    #endif
    }

    private var body_iOS: some View {
        // the body for iOS only
    }

    private var body_macOS: some View {
        // the body for macOS only
    }
}

struct ContentView: View {

    var body: some View {
        MyPlatformSpecificView()
    }
}
```

If you are writing a lot of multiplatform SwiftUI code, I hope these small improvements can make a difference in your codebase too.
