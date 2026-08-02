---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreAudioKit.html
archived_at: '2026-07-18T02:52:57.566665Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreAudioKit Changes for Objective-C

### CoreAudioKit

#### AUCustomViewPersistentData.h

Removed [-[AUCustomViewPersistentData customViewPersistentData]](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata/1516602-customviewpersistentdata)Removed -[AUCustomViewPersistentData setCustomViewPersistentData:]Added [AUCustomViewPersistentData.customViewPersistentData](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata/1516602-customviewpersistentdata)

#### AUGenericView.h

Added [AUGenericViewDisplayFlags](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags)Modified [AUGenericView.audioUnit](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516592-audiounit)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) AudioUnit audioUnit ``` |
| To | ``` @property(readonly, nonnull) AudioUnit audioUnit ``` |

Modified [-[AUGenericView initWithAudioUnit:]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516586-init)

|  | Declaration |
| --- | --- |
| From | ``` - (AUGenericView *)initWithAudioUnit:(AudioUnit)au ``` |
| To | ``` - (AUGenericView * _Nonnull)initWithAudioUnit:(AudioUnit _Nonnull)au ``` |

Modified [-[AUGenericView initWithAudioUnit:displayFlags:]](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516569-init)

|  | Declaration |
| --- | --- |
| From | ``` - (AUGenericView *)initWithAudioUnit:(AudioUnit)inAudioUnit displayFlags:(UInt32)inFlags ``` |
| To | ``` - (AUGenericView * _Nonnull)initWithAudioUnit:(AudioUnit _Nonnull)inAudioUnit displayFlags:(AUGenericViewDisplayFlags)inFlags ``` |

#### AUPannerView.h

Modified [AUPannerView.audioUnit](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516584-audiounit)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) AudioUnit audioUnit ``` |
| To | ``` @property(readonly, nonnull) AudioUnit audioUnit ``` |

Modified [+[AUPannerView AUPannerViewWithAudioUnit:]](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516567-init)

|  | Declaration |
| --- | --- |
| From | ``` + (AUPannerView *)AUPannerViewWithAudioUnit:(AudioUnit)au ``` |
| To | ``` + (AUPannerView * _Nonnull)AUPannerViewWithAudioUnit:(AudioUnit _Nonnull)au ``` |

#### AUViewController.h (Added)

Added [-[AUAudioUnit requestViewControllerWithCompletionHandler:]](https://developer.apple.com/documentation/audiounit/auaudiounit/1516626-requestviewcontroller)Added [AUViewController](https://developer.apple.com/documentation/coreaudiokit/auviewcontroller)Added AUAudioUnit(AUAudioUnit_ViewController)Added [AUViewControllerBase](https://developer.apple.com/documentation/coreaudiokit/auviewcontrollerbase)

#### CABTLEMIDIWindowController.h (Added)

Added [CABTLEMIDIWindowController](https://developer.apple.com/documentation/coreaudiokit/cabtlemidiwindowcontroller)

#### CAInterDeviceAudioViewController.h (Added)

Added [CAInterDeviceAudioViewController](https://developer.apple.com/documentation/coreaudiokit/cainterdeviceaudioviewcontroller)

#### CANetworkBrowserWindowController.h (Added)

Added [CANetworkBrowserWindowController](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller)Added [-[CANetworkBrowserWindowController init]](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller/1516580-init)Added [+[CANetworkBrowserWindowController isAVBSupported]](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller/1516571-isavbsupported)

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
