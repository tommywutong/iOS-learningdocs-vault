---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/CoreAudioKit.html
archived_at: '2026-07-18T02:53:24.742335Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreAudioKit Changes for Swift

### CoreAudioKit

Removed AUCustomViewPersistentData.customViewPersistentData() -> [NSObject : AnyObject]!Removed AUCustomViewPersistentData.setCustomViewPersistentData(_: [NSObject : AnyObject]!)Removed AUViewParametersDisplayFlagRemoved AUViewPropertiesDisplayFlagRemoved AUViewTitleDisplayFlagAdded [AUAudioUnit.requestViewControllerWithCompletionHandler(_: (NSViewController?) -> Void)](https://developer.apple.com/documentation/audiounit/auaudiounit/1516626-requestviewcontrollerwithcomplet)Added [AUCustomViewPersistentData.customViewPersistentData](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata/1516602-customviewpersistentdata)Added [AUGenericViewDisplayFlags [struct]](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags)Added AUGenericViewDisplayFlags.init(rawValue: UInt32)Added [AUGenericViewDisplayFlags.ViewParametersDisplayFlag](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags/1516624-viewparametersdisplayflag)Added [AUGenericViewDisplayFlags.ViewPropertiesDisplayFlag](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags/auviewpropertiesdisplayflag)Added [AUGenericViewDisplayFlags.ViewTitleDisplayFlag](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags/auviewtitledisplayflag)Added [AUViewController](https://developer.apple.com/documentation/coreaudiokit/auviewcontroller)Added [CABTLEMIDIWindowController](https://developer.apple.com/documentation/coreaudiokit/cabtlemidiwindowcontroller)Added [CAInterDeviceAudioViewController](https://developer.apple.com/documentation/coreaudiokit/cainterdeviceaudioviewcontroller)Added [CANetworkBrowserWindowController](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller)Added [CANetworkBrowserWindowController.init()](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller/1516580-init)Added [CANetworkBrowserWindowController.isAVBSupported() -> Bool [class]](https://developer.apple.com/documentation/coreaudiokit/canetworkbrowserwindowcontroller/1516571-isavbsupported)Modified [AUCustomViewPersistentData](https://developer.apple.com/documentation/coreaudiokit/aucustomviewpersistentdata)

|  | Declaration |
| --- | --- |
| From | ``` protocol AUCustomViewPersistentData {     func customViewPersistentData() -> [NSObject : AnyObject]!     func setCustomViewPersistentData(_ data: [NSObject : AnyObject]!) } ``` |
| To | ``` protocol AUCustomViewPersistentData {     var customViewPersistentData: [String : AnyObject]? { get set } } ``` |

Modified [AUGenericView](https://developer.apple.com/documentation/coreaudiokit/augenericview)

|  | Declaration |
| --- | --- |
| From | ``` class AUGenericView : NSView, AUCustomViewPersistentData {     var audioUnit: AudioUnit { get }     var showsExpertParameters: Bool     init!(audioUnit au: AudioUnit)     init!(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: UInt32) } ``` |
| To | ``` class AUGenericView : NSView, AUCustomViewPersistentData {     var audioUnit: AudioUnit { get }     var showsExpertParameters: Bool     init(audioUnit au: AudioUnit)     init(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: AUGenericViewDisplayFlags) } ``` |

Modified [AUGenericView.init(audioUnit: AudioUnit)](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516586-initwithaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioUnit au: AudioUnit) ``` |
| To | ``` init(audioUnit au: AudioUnit) ``` |

Modified [AUGenericView.init(audioUnit: AudioUnit, displayFlags: AUGenericViewDisplayFlags)](https://developer.apple.com/documentation/coreaudiokit/augenericview/1516569-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: UInt32) ``` |
| To | ``` init(audioUnit inAudioUnit: AudioUnit, displayFlags inFlags: AUGenericViewDisplayFlags) ``` |

Modified [AUPannerView](https://developer.apple.com/documentation/coreaudiokit/aupannerview)

|  | Declaration |
| --- | --- |
| From | ``` class AUPannerView : NSView {     var audioUnit: AudioUnit { get }     init!(audioUnit au: AudioUnit) -> AUPannerView     class func AUPannerViewWithAudioUnit(_ au: AudioUnit) -> AUPannerView! } ``` |
| To | ``` class AUPannerView : NSView {     var audioUnit: AudioUnit { get }      init(audioUnit au: AudioUnit)     class func AUPannerViewWithAudioUnit(_ au: AudioUnit) -> AUPannerView } ``` |

Modified [AUPannerView.init(audioUnit: AudioUnit)](https://developer.apple.com/documentation/coreaudiokit/aupannerview/1516567-aupannerviewwithaudiounit)

|  | Declaration |
| --- | --- |
| From | ``` init!(audioUnit au: AudioUnit) -> AUPannerView ``` |
| To | ``` init(audioUnit au: AudioUnit) ``` |

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
