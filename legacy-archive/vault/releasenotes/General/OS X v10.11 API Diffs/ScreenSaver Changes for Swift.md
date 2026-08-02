---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/ScreenSaver.html
archived_at: '2026-07-18T02:53:42.080049Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ScreenSaver Changes for Swift

### ScreenSaver

Removed ScreenSaverView.animationTimeInterval() -> NSTimeIntervalRemoved ScreenSaverView.isAnimating() -> BoolRemoved ScreenSaverView.isPreview() -> BoolRemoved ScreenSaverView.setAnimationTimeInterval(_: NSTimeInterval)Added [ScreenSaverView.animating](https://developer.apple.com/documentation/screensaver/screensaverview/1512467-animating)Added [ScreenSaverView.animationTimeInterval](https://developer.apple.com/documentation/screensaver/screensaverview/1512484-animationtimeinterval)Added [ScreenSaverView.preview](https://developer.apple.com/documentation/screensaver/screensaverview/1512504-ispreview)Modified [ScreenSaverDefaults](https://developer.apple.com/documentation/screensaver/screensaverdefaults)

|  | Declaration |
| --- | --- |
| From | ``` class ScreenSaverDefaults : NSUserDefaults {     class func defaultsForModuleWithName(_ inModuleName: String!) -> AnyObject! } ``` |
| To | ``` class ScreenSaverDefaults : NSUserDefaults {     convenience init?(forModuleWithName inModuleName: String)     class func defaultsForModuleWithName(_ inModuleName: String) -> Self? } ``` |

Modified [ScreenSaverDefaults.init(forModuleWithName: String)](https://developer.apple.com/documentation/screensaver/screensaverdefaults/1512473-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | defaultsForModuleWithName(_:) | ``` class func defaultsForModuleWithName(_ inModuleName: String!) -> AnyObject! ``` | OS X 10.10 |
| To | init(forModuleWithName:) | ``` convenience init?(forModuleWithName inModuleName: String) ``` | OS X 10.11 |

Modified [ScreenSaverView](https://developer.apple.com/documentation/screensaver/screensaverview)

|  | Declaration |
| --- | --- |
| From | ``` class ScreenSaverView : NSView {     class func backingStoreType() -> NSBackingStoreType     class func performGammaFade() -> Bool     init!(frame frame: NSRect)     init!(frame frame: NSRect, isPreview isPreview: Bool)     func animationTimeInterval() -> NSTimeInterval     func setAnimationTimeInterval(_ timeInterval: NSTimeInterval)     func startAnimation()     func stopAnimation()     func isAnimating() -> Bool     func drawRect(_ rect: NSRect)     func animateOneFrame()     func hasConfigureSheet() -> Bool     func configureSheet() -> NSWindow!     func isPreview() -> Bool } ``` |
| To | ``` class ScreenSaverView : NSView {     class func backingStoreType() -> NSBackingStoreType     class func performGammaFade() -> Bool     convenience init?(frame frame: NSRect)     init?(frame frame: NSRect, isPreview isPreview: Bool)     var animationTimeInterval: NSTimeInterval     func startAnimation()     func stopAnimation()     var animating: Bool { get }     func drawRect(_ rect: NSRect)     func animateOneFrame()     func hasConfigureSheet() -> Bool     func configureSheet() -> NSWindow?     var preview: Bool { get } } ``` |

Modified [ScreenSaverView.configureSheet() -> NSWindow?](https://developer.apple.com/documentation/screensaver/screensaverview/1512486-configuresheet)

|  | Declaration |
| --- | --- |
| From | ``` func configureSheet() -> NSWindow! ``` |
| To | ``` func configureSheet() -> NSWindow? ``` |

Modified ScreenSaverView.init(frame: NSRect)

|  | Declaration |
| --- | --- |
| From | ``` init!(frame frame: NSRect) ``` |
| To | ``` convenience init?(frame frame: NSRect) ``` |

Modified [ScreenSaverView.init(frame: NSRect, isPreview: Bool)](https://developer.apple.com/documentation/screensaver/screensaverview/1512475-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(frame frame: NSRect, isPreview isPreview: Bool) ``` |
| To | ``` init?(frame frame: NSRect, isPreview isPreview: Bool) ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
