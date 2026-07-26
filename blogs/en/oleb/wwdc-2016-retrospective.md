---
title: WWDC 2016 Retrospective
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/06/wwdc/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:10ff5ec99dfde584'
translated: false
---

> 原文：[WWDC 2016 Retrospective](https://oleb.net/blog/2016/06/wwdc/)　·　Ole Begemann

# WWDC 2016 Retrospective

Here are some random observations on the new stuff that was announced at WWDC 2016 (besides Swift 3, which [I discussed separately](https://oleb.net/blog/2016/06/swift-3/)).

# Favorite sessions

- [207 – What’s New in Foundation for Swift](https://developer.apple.com/videos/play/wwdc2016/207/).
- [403 – Swift API Design Guidelines](https://developer.apple.com/videos/play/wwdc2016/403/).
- [406 – Optimizing App Startup Time](https://developer.apple.com/videos/play/wwdc2016/406/). A very complex topic very well explained so that everybody can understand it. This is not the umpteenth variant of “don’t block the main thread in `applicationDidFinishLaunching`”, but rather a detailed overview of what the system does when it launches an app before it passes control to the app for the first time.
- [408 – Introducing Swift Playgrounds](https://developer.apple.com/videos/play/wwdc2016/408/).
- [416 – Understanding Swift Performance](https://developer.apple.com/videos/play/wwdc2016/416/). The performance implications of value vs. reference types and protocols vs. generics.

# Xcode 8

Shipping Xcode 8 with both Swift 3.0 and [Swift 2.3](https://swift.org/blog/swift-2-3/) is a nice move that I had not expected. 2.3 allows you to build your Swift 2.2 app with the new SDKs with minimal changes — the language itself has not changed from Swift 2.2 to 2.3, but linking against the new SDKs means you probably will have to make some changes because some APIs had their nullability annotations changed. Apple will [accept apps built with Swift 2.3](https://developer.apple.com/swift/blog/?id=36) when iOS 10 gets released, so that gives you more substantially more leeway when to make the move to Swift 3.

The new [thread sanitizer](https://developer.apple.com/videos/play/wwdc2016/412/) joins the address sanitizer, which was introduced last year and now also supports Swift. Both tools look extremely useful for finding bugs that would be much harder to find otherwise. I hope if and when Swift gets native support for concurrency the compiler will be able to detect most multithreading bugs and there won’t be as big a need for runtime tools like these in the future.

The new [code signing workflow](https://developer.apple.com/videos/play/wwdc2016/401/) seems a lot more transparent about error conditions than before, which should make debugging these issues easier. I guess we’ll have to wait and see how well it works in practice.

The new Interface Builder UI for switching between device and screen configurations looks like a big improvement.

[Source editor extensions](https://developer.apple.com/videos/play/wwdc2016/414/) feel a little bit like the [iWork 13 transition](http://www.theverge.com/2013/10/29/5042880/apple-iwork-2013-refresh-complaints). Because Xcode 8 also moves under the [System Integrity Protection](https://en.wikipedia.org/wiki/System_Integrity_Protection) umbrella, the unofficial plugins many of us have been using will no longer work, and the new extension point [doesn’t provide nearly as many capabilities](http://www.russbishop.net/xcode-extensions). I know this is an unfair comparison because Xcode never had an official plugin API, and who knows if the move to SIP had not come anyway this year? After all, it certainly is a good idea to protect the development toolchain against tampering (remember [XcodeGhost](https://en.wikipedia.org/wiki/XcodeGhost)?). An official extension model is better in the long run for stability and security, so let’s hope this is just the first step (it seems [the Xcode team agrees](https://twitter.com/beccadax/status/744032908705472513)).

# Swift Playgrounds for iPad

The [Playgrounds app](https://developer.apple.com/videos/play/wwdc2016/408/) is very well done. The onscreen keyboard works surprisingly well. I can totally imagine getting “real work” done with something like this. From a technical standpoint, I found it interesting how Apple runs the live view on the right side of the screen in a separate process from the code in the playground. This ensures that the live view is always visible and animating even if the playground code doesn’t compile. And a crash in the playground code won’t take down the live view.

The [playground book file format](https://developer.apple.com/library/prerelease/content/documentation/Xcode/Conceptual/swift_playgrounds_doc_format/index.html) is quite powerful and fully documented. With Swift being open-source, other companies could theoretically build their own compatible playground apps for other platforms (e.g. the web), which sounds cool until you realize that UIKit & Co. are not available on non-Apple platforms.

# Foundation

The Foundation team knocked it out of the park this year. The new [native value types and type-safe string constants](https://oleb.net/blog/2016/06/swift-3/) for Swift are probably my favorite features overall. On top of that, we got [new data types for units and measurements](https://developer.apple.com/videos/play/wwdc2016/238/) and some new date handling and formatting APIs.

# UIKit

UIKit is getting bigger and more powerful with each release. There are [many improvements](https://developer.apple.com/videos/play/wwdc2016/205/), although no single feature stood out to me. [Push and local notifications](https://developer.apple.com/videos/play/wwdc2016/708/) have become vastly more powerful, and the notifications API has been completely redone. [Apps can now respond to 3D Touch peek and pop](https://developer.apple.com/videos/play/wwdc2016/228/) gestures with their own fully custom UI while adopting the system’s response curve. This could lead to many cool new interactions (if users ever discover them).

# AppKit

[`NSGridView`](https://developer.apple.com/reference/appkit/nsgridview) is a new layout container view that, like `NSStackView` and `UIStackView`, is meant to simplify a tedious auto layout task, this time laying out views in a grid. It has a lot of nice features, like adjustable margins (per cell, row, or column) and cells spanning multiple rows or columns. Check out the demo in the [What’s New in Auto Layout](https://developer.apple.com/videos/play/wwdc2016/236/) session, it was very well done.

# Miscellaneous

## NSUserActivity

[`NSUserActivity`](https://developer.apple.com/reference/foundation/nsuseractivity), introduced for handoff in iOS 8, is more and more [becoming the iOS equivalent](https://developer.apple.com/videos/play/wwdc2016/240/) of the [semantic web](https://en.wikipedia.org/wiki/Semantic_Web), though Apple may stand a better chance of it being widely adopted. Ultimately (I think), Apple’s idea is that developers should create a user activity object for (almost) every single screen in their apps, exposing to the system what the user is currently doing, giving it a chance to offer complementary actions.

I’d love it if something like this eventually led to a feature where the OS allowed me to quickly google a word or phrase that’s currently on screen, even if the host app didn’t make it selectable. It probably won’t happen, but people can dream.

## SFSpeechRecognizer

I definitely had not expected a fully featured [speech recognition API](https://developer.apple.com/videos/play/wwdc2016/509/) this year. It basically lets you build something like Siri dictation or the new voicemail transcription. The recognition results even include timecodes. Usage is free, subject to unspecified rate limits and a limit of about one minute of audio per submitted fragment, so it’s not (yet?) suitable for podcast or video transcription.

## APFS

The new file system keeps checksums for metadata, but [not for file contents](http://dtrace.org/blogs/ahl/2016/06/19/apfs-part5/). I hope Apple changes their mind on this before the final version gets released next year.

## Privacy

Apps now must provide a [justification text in their `Info.plist`](https://developer.apple.com/library/prerelease/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW1) for all data and hardware access types that are regulated by the system. We have previously had this for location access and some other cases, and it has now been expanded to include the camera, microphone, photo library, music library, contacts, calendars, reminders, health data, HomeKit data, accelerometer, Bluetooth, Siri, speech recognition, TV provider data, and VoIP. I think this is great.

## iCloud backup encryption

After [Apple’s dispute with the FBI](https://en.wikipedia.org/wiki/FBI%E2%80%93Apple_encryption_dispute), I really expected some news regarding the encryption of iCloud backups in a way that Apple cannot decrypt them (which is [not the case today](http://9to5mac.com/2016/02/25/apple-working-on-stronger-icloud-backup-encryption-and-iphone-security-to-counter-fbi-unlock-requests/)). Something to look out for in the future.
