---
title: AppKit in Swift Playgrounds
source: Saagar Jha
source_key: saagarjha
source_url: 'https://saagarjha.com/blog/2020/02/11/appkit-in-swift-playgrounds/'
original_language: en
published: 2020-02-11
status: active
license: CC BY-SA 4.0 → 可再分发，但译文必须同样 BY-SA 并署名
archived_at: 2026-07-27
content_hash: 'sha256:011c3a7151508da0'
translated: false
---

> 原文：[AppKit in Swift Playgrounds](https://saagarjha.com/blog/2020/02/11/appkit-in-swift-playgrounds/)　·　Saagar Jha

# AppKit in Swift Playgrounds

Tuesday, February 11, 2020

A [Catalyst version](https://apps.apple.com/us/app/swift-playgrounds/id1496833156?mt=12) of [the Swift Playgrounds app](https://www.apple.com/swift/playgrounds/) launched for macOS earlier today, with support for the [Mac Catalyst platform SDK](https://developer.apple.com/documentation/uikit/mac_catalyst). While it’s usually impractical to import AppKit in a Catalyst application, this is apparently now possible in Swift Playgrounds. Most Cocoa APIs have been marked as unavailable, but `import AppKit` does cause the image to actually end up being loaded so it only takes a little bit of work to be able to use them:

![A native AppKit window presented from Swift Playgrounds on macOS. It's titled "Hello from Swift Playgrounds!".](https://saagarjha.com/blog/2020/02/11/appkit-in-swift-playgrounds/AppKitWindow.png)

Catalyst sets up an application for us already, so all we need to do to show a native window is to find the class for `NSWindow` dynamically and mock its interface so the Objective-C runtime will let us call the right methods on it set it up. The code used to make the demo above is quite simple:

```
import AppKit
import PlaygroundSupport
import SwiftUI

@objc protocol _NSWindow {
    var title: String? { get set }
    var styleMask: UInt { get set }
    func setFrame(_ frameRect: NSRect, display flag: Bool)
    func center()
    func makeKeyAndOrderFront(_ sender: Any?)
}

let _NSWindowStyleMaskClosable: UInt = 1 << 1

// A bit more roundabout than it needs to be: see https://bugs.swift.org/browse/SR-4243
let window = unsafeBitCast((NSClassFromString("NSWindow")! as! NSObject.Type).init(), to: _NSWindow.self)
window.styleMask |= _NSWindowStyleMaskClosable
window.title = "Hello from Swift Playgrounds!"
window.setFrame(CGRect(x: 0, y: 0, width: 300, height: 300), display: true)
window.center()
window.makeKeyAndOrderFront(nil)

PlaygroundPage.current.needsIndefiniteExecution = true
```

Perhaps Apple is simply testing this internally and we’ll be able to do this officially in a future release of Playgrounds.
