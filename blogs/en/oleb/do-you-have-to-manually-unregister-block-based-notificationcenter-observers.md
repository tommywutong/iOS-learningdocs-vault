---
title: Do you have to manually unregister block-based NotificationCenter observers?
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/01/notificationcenter-removeobserver/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9a620defe3b33920'
translated: false
---

> 原文：[Do you have to manually unregister block-based NotificationCenter observers?](https://oleb.net/blog/2018/01/notificationcenter-removeobserver/)　·　Ole Begemann

# Do you have to manually unregister block-based NotificationCenter observers?

**tl;dr:** yes. (Tested on iOS 11.2.)

A few weeks ago, I asked this question on Twitter:

> In iOS 11, is it still necessary to unregister _block-based_ notification center observers? Apple docs are ambiguous: docs for [`addObserver(forName:object:queue:using:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver) say yes; [`removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1413994-removeobserver) docs say it’s no longer necessary for iOS 9+.

I received a lot of conflicting replies. The yes/no split was pretty close to 50/50.

So let’s test what happens.

# The problem

The block-based API I’m talking about is [`NotificationCenter.​addObserver​(forName:​object:​queue:​using:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver). We register a function with the notification center that gets called when a matching notification comes in. The return value is an opaque token that represents the observation:

```
class MyObserver {
    var observation: Any? = nil

    init() {
        observation = NotificationCenter.default.addObserver(
            forName: myNotification, object: nil, queue: nil) { notification in
                print("Received \(notification.name.rawValue)")
            }
    }
}
```

And the question is: will the notification center discard the block and stop notifying us when the `observation` token is destroyed (i.e. when the `MyObserver` instance is deallocated)? The new [`KeyPath`](https://developer.apple.com/documentation/swift/key-path-expressions)-based [KVO API](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observe(_:options:changehandler:)) works like this, so it would be somewhat understandable to expect notifications to work the same way.

Or do we have to manually call [`NotificationCenter.​removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv) (e.g. in `MyObserver`’s [`deinit`](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/deinitialization/))?

# What the documentation says

The selector-based observation API [`addObserver(_:​selector:​name:​object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/1415360-addobserver) made manual unregistering optional in iOS 9/OS X 10.11. When that change was made, [the Foundation release notes stated explicitly](https://developer.apple.com/library/content/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#10_11NotificationCenter) that the block-based observers still required manual work:

> Block based observers via the `-[NSNotificationCenter addObserver​ForName:​object:​queue:​usingBlock:]` method still need to be un-registered when no longer in use since the system still holds a strong reference to these observers.

Has anything changed since then?

The [`addObserver(forName:​object:​queue:​using:)` documentation](https://developer.apple.com/documentation/foundation/notificationcenter/1411723-addobserver) is also very clear that unregistering is required:

> You must invoke [`removeObserver(_:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv) or [`removeObserver(_:​name:​object:)`](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:name:object:)) before any object specified by `addObserver(forName:​object:​queue:​using:)` is deallocated.

However, the [`removeObserver(_:)` docs](https://developer.apple.com/documentation/foundation/notificationcenter/removeobserver(_:)-2yciv) seem to contradict this:

> If your app targets iOS 9.0 and later or macOS 10.11 and later, you don’t need to unregister an observer in its `dealloc` method.

This doesn’t make any distinction between the block-based and the selector-based API.

# The test app

I wrote a test app that allows you to inspect the behavior (via Xcode’s console) for various scenarios. [The code is available on GitHub](https://github.com/ole/NotificationUnregistering).

Here’s what I found:

- **Yes, you still have to unregister block-based observations manually (as of iOS 11.2).** The documentation for `removeObserver(_:)` is at least misleading if not wrong.
- If you don’t unregister, the notification center will retain the observer block forever and keep invoking it for every incoming notification. Whether this will wreak havoc with your app depends on what you do in the block (and what objects the block has captured).
- If you do the unregistering in `deinit`, **you must make sure not to capture `self` in your observer block.** If you do, your `deinit` will never get called because the block retains `self` (preventing its destruction) and the notification center holds a strong reference to the block. Your object will live forever.

# Automating unregistering

What’s the best way to deal with this inconvenience? I suggest you write a small wrapper class for the observation token the notification center returns to you. The wrapper object stores the token and waits to be deallocated. Its only task is to call `removeObserver(_:)` in its own deinitializer:

```
/// Wraps the observer token received from 
/// NotificationCenter.addObserver(forName:object:queue:using:)
/// and unregisters it in deinit.
final class NotificationToken: NSObject {
    let notificationCenter: NotificationCenter
    let token: Any

    init(notificationCenter: NotificationCenter = .default, token: Any) {
        self.notificationCenter = notificationCenter
        self.token = token
    }

    deinit {
        notificationCenter.removeObserver(token)
    }
}
```

This binds the lifetime of the notification observation to the lifetime of the wrapper object. All we have to do is store the wrapper in a private property so that it gets destroyed when its owner gets deallocated. So this is equivalent to manual unregistering in `deinit`, but has the benefit that you can’t forget it anymore. And by making the property an `Optional​<Notification​Token>`, you can unregister anytime simply by assigning `nil`. This pattern is known as [_Resource acquisition is initialization_ (RAII)](https://en.wikipedia.org/wiki/Resource_acquisition_is_initialization).

Let’s also write a convenience method for `NotificationCenter` that assumes the task of wrapping the observation token for us:

```
extension NotificationCenter {
    /// Convenience wrapper for addObserver(forName:object:queue:using:)
    /// that returns our custom NotificationToken.
    func observe(name: NSNotification.Name?, object obj: Any?, 
        queue: OperationQueue?, using block: @escaping (Notification) -> ())
        -> NotificationToken
    {
        let token = addObserver(forName: name, object: obj, queue: queue, using: block)
        return NotificationToken(notificationCenter: self, token: token)
    }
}
```

Now replace all calls to `addObserver(forName:​object:​queue:​using:)` with the new API, store the token in a property, and you get automatic unregistering for free.

Chris and Florian also show this technique (among other cool notification stuff) in [Swift Talk episode 27: Typed Notifications](https://talk.objc.io/episodes/S01E27-typed-notifications-part-1). I highly recommend it.
