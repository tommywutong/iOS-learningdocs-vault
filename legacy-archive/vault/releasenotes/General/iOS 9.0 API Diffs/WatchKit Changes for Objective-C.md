---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/WatchKit.html
archived_at: '2026-07-18T02:56:38.345185Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# WatchKit Changes for Objective-C

### WatchKit

#### WKAlertAction.h (Added)

Added [WKAlertActionStyle](https://developer.apple.com/documentation/watchkit/wkalertactionstyle)

#### WKAudioFilePlayer.h (Added)

Added [WKAudioFilePlayerStatus](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)

#### WKAudioFilePlayerItem.h (Added)

Added [WKAudioFilePlayerItemStatus](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus)

#### WKDefines.h

Added #def WK_AVAILABLE_IOS_ONLYAdded #def WK_AVAILABLE_WATCHOS_IOSAdded #def WK_AVAILABLE_WATCHOS_ONLY

#### WKError.h

Added [WatchKitDownloadError](https://developer.apple.com/documentation/watchkit/watchkiterrorcode/watchkitdownloaderror)Added [WatchKitInvalidArgumentError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/invalidargument)Added [WatchKitMediaPlayerError](https://developer.apple.com/documentation/watchkit/watchkiterror/code/mediaplayerfailed)

#### WKInterfaceController.h

Added [-[WKInterfaceController presentTextInputControllerWithSuggestionsForLanguage:allowedInputMode:completion:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619574-presenttextinputcontrollerwithsu)Added [WKAlertControllerStyle](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)Added WKAudioRecordingPresetAdded [WKVideoGravity](https://developer.apple.com/documentation/watchkit/wkvideogravity)Modified [-[WKInterfaceController presentControllerWithNames:contexts:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619561-presentcontrollerwithnames)

|  | Declaration |
| --- | --- |
| From | ``` - (void)presentControllerWithNames:(NSArray *)names contexts:(NSArray *)contexts ``` |
| To | ``` - (void)presentControllerWithNames:(NSArray<NSString *> * _Nonnull)names contexts:(NSArray * _Nullable)contexts ``` |

Modified [-[WKInterfaceController presentTextInputControllerWithSuggestions:allowedInputMode:completion:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619527-presenttextinputcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)presentTextInputControllerWithSuggestions:(NSArray *)suggestions allowedInputMode:(WKTextInputMode)inputMode completion:(void (^)(NSArray *results))completion ``` |
| To | ``` - (void)presentTextInputControllerWithSuggestions:(NSArray<NSString *> * _Nullable)suggestions allowedInputMode:(WKTextInputMode)inputMode completion:(void (^ _Nonnull)(NSArray * _Nullable results))completion ``` |

Modified [+[WKInterfaceController reloadRootControllersWithNames:contexts:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619563-reloadrootcontrollerswithnames)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reloadRootControllersWithNames:(NSArray *)names contexts:(NSArray *)contexts ``` |
| To | ``` + (void)reloadRootControllersWithNames:(NSArray<NSString *> * _Nonnull)names contexts:(NSArray * _Nullable)contexts ``` |

Modified [-[WKUserNotificationInterfaceController init]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619540-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

#### WKInterfaceDevice.h

Added [WKInterfaceDevice.localizedModel](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620835-localizedmodel)Added [WKInterfaceDevice.model](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620940-model)Added [WKInterfaceDevice.name](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620883-name)Added [WKInterfaceDevice.systemName](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620857-systemname)Added [WKInterfaceDevice.systemVersion](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620927-systemversion)Added [WKHapticType](https://developer.apple.com/documentation/watchkit/wkhaptictype)Modified [WKInterfaceDevice.cachedImages](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620887-cachedimages)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, strong) NSDictionary *cachedImages ``` |
| To | ``` @property(nonatomic, readonly, strong, nonnull) NSDictionary<NSString *,NSNumber *> *cachedImages ``` |

#### WKInterfaceGroup.h

Removed -[WKInterfaceGroup startAnimating]Removed -[WKInterfaceGroup startAnimatingWithImagesInRange:duration:repeatCount:]Removed -[WKInterfaceGroup stopAnimating]Modified [WKInterfaceGroup](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)

|  | Protocols |
| --- | --- |
| From | -- |
| To | WKImageAnimatable |

#### WKInterfaceImage.h

Removed -[WKInterfaceImage startAnimating]Removed -[WKInterfaceImage startAnimatingWithImagesInRange:duration:repeatCount:]Removed -[WKInterfaceImage stopAnimating]Added [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable)Added [-[WKImageAnimatable startAnimating]](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615219-startanimating)Added [-[WKImageAnimatable startAnimatingWithImagesInRange:duration:repeatCount:]](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615208-startanimatingwithimagesinrange)Added [-[WKImageAnimatable stopAnimating]](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615225-stopanimating)Modified [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)

|  | Protocols |
| --- | --- |
| From | -- |
| To | WKImageAnimatable |

#### WKInterfaceObject.h

Added [-[WKInterfaceObject setAccessibilityIdentifier:]](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/1620817-setaccessibilityidentifier)Added [WKInterfaceObjectHorizontalAlignment](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment)Added [WKInterfaceObjectVerticalAlignment](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment)Modified [-[WKInterfaceObject setAccessibilityImageRegions:]](https://developer.apple.com/documentation/watchkit/wkinterfaceobject/1620920-setaccessibilityimageregions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setAccessibilityImageRegions:(NSArray *)accessibilityImageRegions ``` |
| To | ``` - (void)setAccessibilityImageRegions:(NSArray<WKAccessibilityImageRegion *> * _Nonnull)accessibilityImageRegions ``` |

#### WKInterfaceTable.h

Modified [-[WKInterfaceTable setRowTypes:]](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615839-setrowtypes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setRowTypes:(NSArray *)rowTypes ``` |
| To | ``` - (void)setRowTypes:(NSArray<NSString *> * _Nonnull)rowTypes ``` |

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
