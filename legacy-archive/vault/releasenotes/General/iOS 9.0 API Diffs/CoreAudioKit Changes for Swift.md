---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreAudioKit.html
archived_at: '2026-07-18T02:56:43.284568Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreAudioKit Changes for Swift

### CoreAudioKit

Added [AUAudioUnit.requestViewControllerWithCompletionHandler(_: (UIViewController?) -> Void)](https://developer.apple.com/documentation/audiounit/auaudiounit/1516626-requestviewcontrollerwithcomplet)Added [AUViewController](https://developer.apple.com/documentation/coreaudiokit/auviewcontroller)Modified [CAInterAppAudioTransportView](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview)

|  | Declaration |
| --- | --- |
| From | ``` class CAInterAppAudioTransportView : UIView {     var enabled: Bool     var playing: Bool { get }     var recording: Bool { get }     var connected: Bool { get }     var labelColor: UIColor!     var currentTimeLabelFont: UIFont!     var rewindButtonColor: UIColor!     var playButtonColor: UIColor!     var pauseButtonColor: UIColor!     var recordButtonColor: UIColor!     func setOutputAudioUnit(_ au: AudioUnit) } ``` |
| To | ``` class CAInterAppAudioTransportView : UIView {     var enabled: Bool     var playing: Bool { get }     var recording: Bool { get }     var connected: Bool { get }     var labelColor: UIColor     var currentTimeLabelFont: UIFont     var rewindButtonColor: UIColor     var playButtonColor: UIColor     var pauseButtonColor: UIColor     var recordButtonColor: UIColor     func setOutputAudioUnit(_ au: AudioUnit) } ``` |

Modified [CAInterAppAudioTransportView.currentTimeLabelFont](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614722-currenttimelabelfont)

|  | Declaration |
| --- | --- |
| From | ``` var currentTimeLabelFont: UIFont! ``` |
| To | ``` var currentTimeLabelFont: UIFont ``` |

Modified [CAInterAppAudioTransportView.labelColor](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614718-labelcolor)

|  | Declaration |
| --- | --- |
| From | ``` var labelColor: UIColor! ``` |
| To | ``` var labelColor: UIColor ``` |

Modified [CAInterAppAudioTransportView.pauseButtonColor](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614723-pausebuttoncolor)

|  | Declaration |
| --- | --- |
| From | ``` var pauseButtonColor: UIColor! ``` |
| To | ``` var pauseButtonColor: UIColor ``` |

Modified [CAInterAppAudioTransportView.playButtonColor](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614710-playbuttoncolor)

|  | Declaration |
| --- | --- |
| From | ``` var playButtonColor: UIColor! ``` |
| To | ``` var playButtonColor: UIColor ``` |

Modified [CAInterAppAudioTransportView.recordButtonColor](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614694-recordbuttoncolor)

|  | Declaration |
| --- | --- |
| From | ``` var recordButtonColor: UIColor! ``` |
| To | ``` var recordButtonColor: UIColor ``` |

Modified [CAInterAppAudioTransportView.rewindButtonColor](https://developer.apple.com/documentation/coreaudiokit/cainterappaudiotransportview/1614700-rewindbuttoncolor)

|  | Declaration |
| --- | --- |
| From | ``` var rewindButtonColor: UIColor! ``` |
| To | ``` var rewindButtonColor: UIColor ``` |

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
