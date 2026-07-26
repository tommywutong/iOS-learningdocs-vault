---
title: Sharing cross-platform code in SwiftUI apps
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/08/19/sharing-code-in-swiftui-apps/'
original_language: en
published: 2022-08-19
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2a4f09a060365472'
translated: false
---

> 原文：[Sharing cross-platform code in SwiftUI apps](https://www.jessesquires.com/blog/2022/08/19/sharing-code-in-swiftui-apps/)　·　Jesse Squires

The main appeal of building apps in [SwiftUI](https://developer.apple.com/xcode/swiftui/) is being able to share UI code across platforms, in particular iOS and macOS. It is not perfect and you often have to do some `#if os()` checks, but when it works it is truly great. Before SwiftUI was around, you could already share a lot of (non-UI) code between iOS and macOS. Many of the system frameworks are available on both platforms, for example [Foundation](https://developer.apple.com/documentation/foundation) and [Core Data](https://developer.apple.com/documentation/coredata). Occasionally there are API differences, but they rarely impose a significant burden.

The biggest issue when working on a cross-platform SwiftUI app is when you need to drop into [AppKit](https://developer.apple.com/documentation/appkit) on macOS and [UIKit](https://developer.apple.com/documentation/uikit) on iOS. Often, the APIs that you need (because they are absent from SwiftUI) are simply entirely different. However, sometimes the APIs are _nearly identical_ but _just different enough_ to require branching into platform-specific code paths. A good example of this is [`UIPasteboard`](https://developer.apple.com/documentation/uikit/uipasteboard) on iOS and [`NSPasteboard`](https://developer.apple.com/documentation/appkit/nspasteboard) on macOS.

In this cross-platform SwiftUI app that I’m working on, I wanted to allow the user to copy some text from a table view. The UI code is shared for both platforms, but not the underlying copying functionality — because we need to use AppKit on macOS and UIKit on iOS. But I wanted to keep the copy action code at the call site clean, without a bunch of `#if os()` checks. To do this, you can employ a clever use of `typealias`.

First, we define a common `typealias` on both platforms.

```
#if os(macOS)
    import AppKit
    typealias XPasteboard = NSPasteboard
#else
    import UIKit
    typealias XPasteboard = UIPasteboard
#endif
```

Then we can write an extension on `XPasteboard` to encapsulate the common functionality.

```
extension XPasteboard {
    func copyText(_ text: String) {
#if os(macOS)
        self.clearContents()
        self.setString(text, forType: .string)
#else
        self.string = text
#endif
    }
}
```

At the call site, we now have a single “cross-platform” API to use. I like how this keeps code cleaner and simpler.

```
XPasteboard.general.copyText(someText)
```

This is only a small example of how you can workaround differences in AppKit and UIKit to produce nicer code, but there are plenty of other opportunities for improvement as you come across similar-but-different APIs in the two frameworks. As your SwiftUI app becomes more complex, you’ll need AppKit and UIKit more and more. This is one strategy I like to use to encapsulate some of that complexity.
