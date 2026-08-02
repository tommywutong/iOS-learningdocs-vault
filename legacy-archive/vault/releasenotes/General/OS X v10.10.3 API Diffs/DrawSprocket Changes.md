---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/DrawSprocket.html
archived_at: '2026-07-18T02:52:24.161405Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# DrawSprocket Changes

## DrawSprocket

Added DSpAltBufferAttributes.init()Added DSpAltBufferAttributes.init(width: UInt32, height: UInt32, options: DSpAltBufferOption, reserved:(UInt32, UInt32, UInt32, UInt32))Added DSpBlitInfo.init()Added DSpBlitInfo.init(completionFlag: Boolean, filler:(Int8, Int8, Int8), completionProc: DSpBlitDoneProc, srcContext: DSpContextReference, srcBuffer: CGrafPtr, srcRect: Rect, srcKey: UInt32, dstContext: DSpContextReference, dstBuffer: CGrafPtr, dstRect: Rect, dstKey: UInt32, mode: DSpBlitMode, reserved:(UInt32, UInt32, UInt32, UInt32))Added DSpContextAttributes.init()Added DSpContextAttributes.init(frequency: Fixed, displayWidth: UInt32, displayHeight: UInt32, reserved1: UInt32, reserved2: UInt32, colorNeeds: UInt32, colorTable: CTabHandle, contextOptions: OptionBits, backBufferDepthMask: OptionBits, displayDepthMask: OptionBits, backBufferBestDepth: UInt32, displayBestDepth: UInt32, pageCount: UInt32, filler:(Int8, Int8, Int8), gameMustConfirmSwitch: Boolean, reserved3:(UInt32, UInt32, UInt32, UInt32))Modified DSpAltBufferAttributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSpAltBufferAttributes {     var width: UInt32     var height: UInt32     var options: DSpAltBufferOption     var reserved: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct DSpAltBufferAttributes {     var width: UInt32     var height: UInt32     var options: DSpAltBufferOption     var reserved: (UInt32, UInt32, UInt32, UInt32)     init()     init(width width: UInt32, height height: UInt32, options options: DSpAltBufferOption, reserved reserved: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified DSpBlitInfo [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSpBlitInfo {     var completionFlag: Boolean     var filler: (Int8, Int8, Int8)     var completionProc: DSpBlitDoneProc     var srcContext: DSpContextReference     var srcBuffer: CGrafPtr     var srcRect: Rect     var srcKey: UInt32     var dstContext: DSpContextReference     var dstBuffer: CGrafPtr     var dstRect: Rect     var dstKey: UInt32     var mode: DSpBlitMode     var reserved: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct DSpBlitInfo {     var completionFlag: Boolean     var filler: (Int8, Int8, Int8)     var completionProc: DSpBlitDoneProc     var srcContext: DSpContextReference     var srcBuffer: CGrafPtr     var srcRect: Rect     var srcKey: UInt32     var dstContext: DSpContextReference     var dstBuffer: CGrafPtr     var dstRect: Rect     var dstKey: UInt32     var mode: DSpBlitMode     var reserved: (UInt32, UInt32, UInt32, UInt32)     init()     init(completionFlag completionFlag: Boolean, filler filler: (Int8, Int8, Int8), completionProc completionProc: DSpBlitDoneProc, srcContext srcContext: DSpContextReference, srcBuffer srcBuffer: CGrafPtr, srcRect srcRect: Rect, srcKey srcKey: UInt32, dstContext dstContext: DSpContextReference, dstBuffer dstBuffer: CGrafPtr, dstRect dstRect: Rect, dstKey dstKey: UInt32, mode mode: DSpBlitMode, reserved reserved: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified DSpContextAttributes [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSpContextAttributes {     var frequency: Fixed     var displayWidth: UInt32     var displayHeight: UInt32     var reserved1: UInt32     var reserved2: UInt32     var colorNeeds: UInt32     var colorTable: CTabHandle     var contextOptions: OptionBits     var backBufferDepthMask: OptionBits     var displayDepthMask: OptionBits     var backBufferBestDepth: UInt32     var displayBestDepth: UInt32     var pageCount: UInt32     var filler: (Int8, Int8, Int8)     var gameMustConfirmSwitch: Boolean     var reserved3: (UInt32, UInt32, UInt32, UInt32) } ``` |
| To | ``` struct DSpContextAttributes {     var frequency: Fixed     var displayWidth: UInt32     var displayHeight: UInt32     var reserved1: UInt32     var reserved2: UInt32     var colorNeeds: UInt32     var colorTable: CTabHandle     var contextOptions: OptionBits     var backBufferDepthMask: OptionBits     var displayDepthMask: OptionBits     var backBufferBestDepth: UInt32     var displayBestDepth: UInt32     var pageCount: UInt32     var filler: (Int8, Int8, Int8)     var gameMustConfirmSwitch: Boolean     var reserved3: (UInt32, UInt32, UInt32, UInt32)     init()     init(frequency frequency: Fixed, displayWidth displayWidth: UInt32, displayHeight displayHeight: UInt32, reserved1 reserved1: UInt32, reserved2 reserved2: UInt32, colorNeeds colorNeeds: UInt32, colorTable colorTable: CTabHandle, contextOptions contextOptions: OptionBits, backBufferDepthMask backBufferDepthMask: OptionBits, displayDepthMask displayDepthMask: OptionBits, backBufferBestDepth backBufferBestDepth: UInt32, displayBestDepth displayBestDepth: UInt32, pageCount pageCount: UInt32, filler filler: (Int8, Int8, Int8), gameMustConfirmSwitch gameMustConfirmSwitch: Boolean, reserved3 reserved3: (UInt32, UInt32, UInt32, UInt32)) } ``` |

Modified DSpBlitDoneProc

|  | Declaration |
| --- | --- |
| From | ``` typealias DSpBlitDoneProc = CFunctionPointer<((UnsafePointer<DSpBlitInfo>) -> Void)> ``` |
| To | ``` typealias DSpBlitDoneProc = CFunctionPointer<((UnsafeMutablePointer<DSpBlitInfo>) -> Void)> ``` |

Modified DSpBlitInfoPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DSpBlitInfoPtr = UnsafePointer<DSpBlitInfo> ``` |
| To | ``` typealias DSpBlitInfoPtr = UnsafeMutablePointer<DSpBlitInfo> ``` |

Modified DSpCallbackProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DSpCallbackProcPtr = CFunctionPointer<((DSpContextReference, UnsafePointer<()>) -> Boolean)> ``` |
| To | ``` typealias DSpCallbackProcPtr = CFunctionPointer<((DSpContextReference, UnsafeMutablePointer<Void>) -> Boolean)> ``` |

Modified DSpContextAttributesPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DSpContextAttributesPtr = UnsafePointer<DSpContextAttributes> ``` |
| To | ``` typealias DSpContextAttributesPtr = UnsafeMutablePointer<DSpContextAttributes> ``` |

Modified DSpEventProcPtr

|  | Declaration |
| --- | --- |
| From | ``` typealias DSpEventProcPtr = CFunctionPointer<((UnsafePointer<EventRecord>) -> Boolean)> ``` |
| To | ``` typealias DSpEventProcPtr = CFunctionPointer<((UnsafeMutablePointer<EventRecord>) -> Boolean)> ``` |

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
