---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/AVKit.html
archived_at: '2026-07-18T02:52:47.463806Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AVKit Changes for Objective-C

### AVKit

#### AVCaptureView.h

Modified [AVCaptureView.delegate](https://developer.apple.com/documentation/avkit/avcaptureview/1519144-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id<AVCaptureViewDelegate> delegate ``` |
| To | ``` @property(weak, nullable) id<AVCaptureViewDelegate> delegate ``` |

Modified [AVCaptureView.fileOutput](https://developer.apple.com/documentation/avkit/avcaptureview/1519149-fileoutput)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) AVCaptureFileOutput *fileOutput ``` |
| To | ``` @property(readonly, nullable) AVCaptureFileOutput *fileOutput ``` |

Modified [AVCaptureView.session](https://developer.apple.com/documentation/avkit/avcaptureview/1519186-session)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) AVCaptureSession *session ``` |
| To | ``` @property(readonly, nullable) AVCaptureSession *session ``` |

Modified [-[AVCaptureView setSession:showVideoPreview:showAudioPreview:]](https://developer.apple.com/documentation/avkit/avcaptureview/1519163-setsession)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSession:(AVCaptureSession *)session showVideoPreview:(BOOL)showVideoPreview showAudioPreview:(BOOL)showAudioPreview ``` |
| To | ``` - (void)setSession:(AVCaptureSession * _Nullable)session showVideoPreview:(BOOL)showVideoPreview showAudioPreview:(BOOL)showAudioPreview ``` |

Modified [AVCaptureView.videoGravity](https://developer.apple.com/documentation/avkit/avcaptureview/1519134-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *videoGravity ``` |
| To | ``` @property(copy, nonnull) NSString *videoGravity ``` |

Modified [-[AVCaptureViewDelegate captureView:startRecordingToFileOutput:]](https://developer.apple.com/documentation/avkit/avcaptureviewdelegate/1519138-captureview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)captureView:(AVCaptureView *)captureView startRecordingToFileOutput:(AVCaptureFileOutput *)fileOutput ``` |
| To | ``` - (void)captureView:(AVCaptureView * _Nonnull)captureView startRecordingToFileOutput:(AVCaptureFileOutput * _Nonnull)fileOutput ``` |

#### AVPlayerView.h

Modified [AVPlayerView.actionPopUpButtonMenu](https://developer.apple.com/documentation/avkit/avplayerview/1416543-actionpopupbuttonmenu)

|  | Declaration |
| --- | --- |
| From | ``` @property NSMenu *actionPopUpButtonMenu ``` |
| To | ``` @property(nullable) NSMenu *actionPopUpButtonMenu ``` |

Modified [-[AVPlayerView beginTrimmingWithCompletionHandler:]](https://developer.apple.com/documentation/avkit/avplayerview/1416570-begintrimming)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginTrimmingWithCompletionHandler:(void (^)(AVPlayerViewTrimResult result))handler ``` |
| To | ``` - (void)beginTrimmingWithCompletionHandler:(void (^ _Nullable)(AVPlayerViewTrimResult result))handler ``` |

Modified [AVPlayerView.contentOverlayView](https://developer.apple.com/documentation/avkit/avplayerview/1416573-contentoverlayview)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSView *contentOverlayView ``` |
| To | ``` @property(readonly, nullable) NSView *contentOverlayView ``` |

Modified [-[AVPlayerView flashChapterNumber:chapterTitle:]](https://developer.apple.com/documentation/avkit/avplayerview/1416547-flashchapternumber)

|  | Declaration |
| --- | --- |
| From | ``` - (void)flashChapterNumber:(NSUInteger)chapterNumber chapterTitle:(NSString *)chapterTitle ``` |
| To | ``` - (void)flashChapterNumber:(NSUInteger)chapterNumber chapterTitle:(NSString * _Nonnull)chapterTitle ``` |

Modified [AVPlayerView.player](https://developer.apple.com/documentation/avkit/avplayerview/1416539-player)

|  | Declaration |
| --- | --- |
| From | ``` @property AVPlayer *player ``` |
| To | ``` @property(nullable) AVPlayer *player ``` |

Modified [AVPlayerView.videoGravity](https://developer.apple.com/documentation/avkit/avplayerview/1416559-videogravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *videoGravity ``` |
| To | ``` @property(copy, nonnull) NSString *videoGravity ``` |

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
