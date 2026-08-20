---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/AVKit.html
archived_at: '2026-07-18T02:53:16.165570Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AVKit Changes for Swift

### AVKit

Added [AVCaptureViewControlsStyle.Default](https://developer.apple.com/documentation/avkit/avcaptureviewcontrolsstyle/1519165-default)Added [AVPlayerViewControlsStyle.Default](https://developer.apple.com/documentation/avkit/avplayerviewcontrolsstyle/avplayerviewcontrolsstyledefault)Modified [AVCaptureView](https://developer.apple.com/documentation/avkit/avcaptureview)

|  | Declaration |
| --- | --- |
| From | ``` class AVCaptureView : NSView {     var session: AVCaptureSession! { get }     func setSession(_ session: AVCaptureSession!, showVideoPreview showVideoPreview: Bool, showAudioPreview showAudioPreview: Bool)     var fileOutput: AVCaptureFileOutput! { get }     weak var delegate: AVCaptureViewDelegate!     var controlsStyle: AVCaptureViewControlsStyle     var videoGravity: String! } ``` |
| To | ``` class AVCaptureView : NSView {     var session: AVCaptureSession? { get }     func setSession(_ session: AVCaptureSession?, showVideoPreview showVideoPreview: Bool, showAudioPreview showAudioPreview: Bool)     var fileOutput: AVCaptureFileOutput? { get }     weak var delegate: AVCaptureViewDelegate?     var controlsStyle: AVCaptureViewControlsStyle     var videoGravity: String } ``` |

Modified [AVCaptureView.delegate](https://developer.apple.com/documentation/avkit/avcaptureview/1519144-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: AVCaptureViewDelegate! ``` |
| To | ``` weak var delegate: AVCaptureViewDelegate? ``` |

Modified [AVCaptureView.fileOutput](https://developer.apple.com/documentation/avkit/avcaptureview/1519149-fileoutput)

|  | Declaration |
| --- | --- |
| From | ``` var fileOutput: AVCaptureFileOutput! { get } ``` |
| To | ``` var fileOutput: AVCaptureFileOutput? { get } ``` |

Modified [AVCaptureView.session](https://developer.apple.com/documentation/avkit/avcaptureview/1519186-session)

|  | Declaration |
| --- | --- |
| From | ``` var session: AVCaptureSession! { get } ``` |
| To | ``` var session: AVCaptureSession? { get } ``` |

Modified [AVCaptureView.setSession(_: AVCaptureSession?, showVideoPreview: Bool, showAudioPreview: Bool)](https://developer.apple.com/documentation/avkit/avcaptureview/1519163-setsession)

|  | Declaration |
| --- | --- |
| From | ``` func setSession(_ session: AVCaptureSession!, showVideoPreview showVideoPreview: Bool, showAudioPreview showAudioPreview: Bool) ``` |
| To | ``` func setSession(_ session: AVCaptureSession?, showVideoPreview showVideoPreview: Bool, showAudioPreview showAudioPreview: Bool) ``` |

Modified [AVCaptureView.videoGravity](https://developer.apple.com/documentation/avkit/avcaptureview/1519134-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` var videoGravity: String! ``` |
| To | ``` var videoGravity: String ``` |

Modified [AVCaptureViewControlsStyle [enum]](https://developer.apple.com/documentation/avkit/avcaptureviewcontrolsstyle)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum AVCaptureViewControlsStyle : Int {     case Inline     case Floating     case InlineDeviceSelection } ``` | -- |
| To | ``` enum AVCaptureViewControlsStyle : Int {     case Inline     case Floating     case InlineDeviceSelection     static var Default: AVCaptureViewControlsStyle { get } } ``` | Int |

Modified [AVCaptureViewDelegate](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol AVCaptureViewDelegate : NSObjectProtocol {     func captureView(_ captureView: AVCaptureView!, startRecordingToFileOutput fileOutput: AVCaptureFileOutput!) } ``` |
| To | ``` protocol AVCaptureViewDelegate : NSObjectProtocol {     func captureView(_ captureView: AVCaptureView, startRecordingToFileOutput fileOutput: AVCaptureFileOutput) } ``` |

Modified [AVCaptureViewDelegate.captureView(_: AVCaptureView, startRecordingToFileOutput: AVCaptureFileOutput)](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate/1519138-captureview)

|  | Declaration |
| --- | --- |
| From | ``` func captureView(_ captureView: AVCaptureView!, startRecordingToFileOutput fileOutput: AVCaptureFileOutput!) ``` |
| To | ``` func captureView(_ captureView: AVCaptureView, startRecordingToFileOutput fileOutput: AVCaptureFileOutput) ``` |

Modified [AVPlayerView](https://developer.apple.com/documentation/avkit/avplayerview)

|  | Declaration |
| --- | --- |
| From | ``` class AVPlayerView : NSView {     var player: AVPlayer!     var controlsStyle: AVPlayerViewControlsStyle     var videoGravity: String!     var readyForDisplay: Bool { get }     var videoBounds: NSRect { get }     var contentOverlayView: NSView! { get } } extension AVPlayerView {     var showsFrameSteppingButtons: Bool     var showsSharingServiceButton: Bool     var actionPopUpButtonMenu: NSMenu!     var showsFullScreenToggleButton: Bool } extension AVPlayerView {     var canBeginTrimming: Bool { get }     func beginTrimmingWithCompletionHandler(_ handler: ((AVPlayerViewTrimResult) -> Void)!) } extension AVPlayerView {     func flashChapterNumber(_ chapterNumber: Int, chapterTitle chapterTitle: String!) } ``` |
| To | ``` class AVPlayerView : NSView {     var player: AVPlayer?     var controlsStyle: AVPlayerViewControlsStyle     var videoGravity: String     var readyForDisplay: Bool { get }     var videoBounds: NSRect { get }     var contentOverlayView: NSView? { get } } extension AVPlayerView {     var showsFrameSteppingButtons: Bool     var showsSharingServiceButton: Bool     var actionPopUpButtonMenu: NSMenu?     var showsFullScreenToggleButton: Bool } extension AVPlayerView {     var canBeginTrimming: Bool { get }     func beginTrimmingWithCompletionHandler(_ handler: ((AVPlayerViewTrimResult) -> Void)?) } extension AVPlayerView {     func flashChapterNumber(_ chapterNumber: Int, chapterTitle chapterTitle: String) } ``` |

Modified [AVPlayerView.actionPopUpButtonMenu](https://developer.apple.com/documentation/avkit/avplayerview/1416543-actionpopupbuttonmenu)

|  | Declaration |
| --- | --- |
| From | ``` var actionPopUpButtonMenu: NSMenu! ``` |
| To | ``` var actionPopUpButtonMenu: NSMenu? ``` |

Modified [AVPlayerView.beginTrimmingWithCompletionHandler(_: ((AVPlayerViewTrimResult) -> Void)?)](https://developer.apple.com/documentation/avkit/avplayerview/1416570-begintrimmingwithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func beginTrimmingWithCompletionHandler(_ handler: ((AVPlayerViewTrimResult) -> Void)!) ``` |
| To | ``` func beginTrimmingWithCompletionHandler(_ handler: ((AVPlayerViewTrimResult) -> Void)?) ``` |

Modified [AVPlayerView.contentOverlayView](https://developer.apple.com/documentation/avkit/avplayerview/1416573-contentoverlayview)

|  | Declaration |
| --- | --- |
| From | ``` var contentOverlayView: NSView! { get } ``` |
| To | ``` var contentOverlayView: NSView? { get } ``` |

Modified [AVPlayerView.flashChapterNumber(_: Int, chapterTitle: String)](https://developer.apple.com/documentation/avkit/avplayerview/1416547-flashchapternumber)

|  | Declaration |
| --- | --- |
| From | ``` func flashChapterNumber(_ chapterNumber: Int, chapterTitle chapterTitle: String!) ``` |
| To | ``` func flashChapterNumber(_ chapterNumber: Int, chapterTitle chapterTitle: String) ``` |

Modified [AVPlayerView.player](https://developer.apple.com/documentation/avkit/avplayerview/1416539-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: AVPlayer! ``` |
| To | ``` var player: AVPlayer? ``` |

Modified [AVPlayerView.videoGravity](https://developer.apple.com/documentation/avkit/avplayerview/1416559-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` var videoGravity: String! ``` |
| To | ``` var videoGravity: String ``` |

Modified [AVPlayerViewControlsStyle [enum]](https://developer.apple.com/documentation/avkit/avplayerviewcontrolsstyle)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum AVPlayerViewControlsStyle : Int {     case None     case Inline     case Floating     case Minimal } ``` | -- |
| To | ``` enum AVPlayerViewControlsStyle : Int {     case None     case Inline     case Floating     case Minimal     static var Default: AVPlayerViewControlsStyle { get } } ``` | Int |

Modified [AVPlayerViewTrimResult [enum]](https://developer.apple.com/documentation/avkit/avplayerviewtrimresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
