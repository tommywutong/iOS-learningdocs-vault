---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Objective-C/WatchKit.html
archived_at: '2026-07-18T02:58:16.237267Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# WatchKit Changes for Objective-C

### WatchKit

#### WKBackgroundTask.h (Added)

Added [WKApplicationRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask)Added [-[WKExtension scheduleBackgroundRefreshWithPreferredDate:userInfo:scheduledCompletion:]](https://developer.apple.com/documentation/watchkit/wkextension/1650848-schedulebackgroundrefresh)Added [-[WKExtension scheduleSnapshotRefreshWithPreferredDate:userInfo:scheduledCompletion:]](https://developer.apple.com/documentation/watchkit/wkextension/1650837-schedulesnapshotrefresh)Added [WKRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask)Added [-[WKRefreshBackgroundTask setTaskCompleted]](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/1833709-settaskcompleted)Added [WKRefreshBackgroundTask.userInfo](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/1650839-userinfo)Added [WKSnapshotRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask)Added [WKSnapshotRefreshBackgroundTask.returnToDefaultState](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/1773208-returntodefaultstate)Added [-[WKSnapshotRefreshBackgroundTask setTaskCompletedWithDefaultStateRestored:estimatedSnapshotExpiration:userInfo:]](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/1650844-settaskcompleted)Added [WKURLSessionRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask)Added [WKURLSessionRefreshBackgroundTask.sessionIdentifier](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask/1650836-sessionidentifier)Added [WKWatchConnectivityRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask)Added WKExtension(WKBackgroundTasks)

#### WKCrownSequencer.h (Added)

Added [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate)Added [-[WKCrownDelegate crownDidBecomeIdle:]](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/1650884-crowndidbecomeidle)Added [-[WKCrownDelegate crownDidRotate:rotationalDelta:]](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/1650886-crowndidrotate)Added [WKCrownSequencer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer)Added [WKCrownSequencer.delegate](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650887-delegate)Added [-[WKCrownSequencer focus]](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650892-focus)Added [WKCrownSequencer.idle](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650890-idle)Added [-[WKCrownSequencer resignFocus]](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650889-resignfocus)Added [WKCrownSequencer.rotationsPerSecond](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650891-rotationspersecond)

#### WKDefines.h

Added #def WK_DEPRECATED_WATCHOSAdded #def WK_DEPRECATED_WATCHOS_IOS

#### WKExtension.h

Added [WKExtension.applicationState](https://developer.apple.com/documentation/watchkit/wkextension/1650873-applicationstate)Added [-[WKExtensionDelegate applicationDidEnterBackground]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650865-applicationdidenterbackground)Added [-[WKExtensionDelegate applicationWillEnterForeground]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650868-applicationwillenterforeground)Added [-[WKExtensionDelegate handleBackgroundTasks:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650877-handlebackgroundtasks)Added [-[WKExtensionDelegate handleWorkoutConfiguration:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650871-handleworkoutconfiguration)Added [WKApplicationState](https://developer.apple.com/documentation/watchkit/wkapplicationstate)Added [WKApplicationStateActive](https://developer.apple.com/documentation/watchkit/wkapplicationstate/wkapplicationstateactive)Added [WKApplicationStateBackground](https://developer.apple.com/documentation/watchkit/wkapplicationstate/wkapplicationstatebackground)Added [WKApplicationStateInactive](https://developer.apple.com/documentation/watchkit/wkapplicationstate/wkapplicationstateinactive)Modified [-[WKExtensionDelegate didReceiveLocalNotification:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628200-didreceive)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKExtensionDelegate didReceiveRemoteNotification:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628170-didreceiveremotenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKExtensionDelegate handleActionWithIdentifier:forLocalNotification:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628139-handleaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKExtensionDelegate handleActionWithIdentifier:forLocalNotification:withResponseInfo:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628242-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKExtensionDelegate handleActionWithIdentifier:forRemoteNotification:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628138-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKExtensionDelegate handleActionWithIdentifier:forRemoteNotification:withResponseInfo:]](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628160-handleaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

#### WKGestureRecognizer.h (Added)

Added [WKGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer)Added [WKGestureRecognizer.enabled](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650812-enabled)Added [-[WKGestureRecognizer locationInObject]](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650823-locationinobject)Added [-[WKGestureRecognizer objectBounds]](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650835-objectbounds)Added [WKGestureRecognizer.state](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650821-state)Added [WKLongPressGestureRecognizer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer)Added [WKLongPressGestureRecognizer.allowableMovement](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650814-allowablemovement)Added [WKLongPressGestureRecognizer.minimumPressDuration](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650831-minimumpressduration)Added [WKLongPressGestureRecognizer.numberOfTapsRequired](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650822-numberoftapsrequired)Added [WKPanGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer)Added [-[WKPanGestureRecognizer translationInObject]](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/1650832-translationinobject)Added [-[WKPanGestureRecognizer velocityInObject]](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/1650817-velocityinobject)Added [WKSwipeGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer)Added [WKSwipeGestureRecognizer.direction](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer/1650828-direction)Added [WKTapGestureRecognizer](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer)Added [WKTapGestureRecognizer.numberOfTapsRequired](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer/1650834-numberoftapsrequired)Added [WKGestureRecognizerState](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate)Added WKGestureRecognizerStateBeganAdded WKGestureRecognizerStateCancelledAdded WKGestureRecognizerStateChangedAdded WKGestureRecognizerStateEndedAdded WKGestureRecognizerStateFailedAdded WKGestureRecognizerStatePossibleAdded WKGestureRecognizerStateRecognizedAdded [WKSwipeGestureRecognizerDirection](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizerdirection)Added WKSwipeGestureRecognizerDirectionDownAdded WKSwipeGestureRecognizerDirectionLeftAdded WKSwipeGestureRecognizerDirectionRightAdded WKSwipeGestureRecognizerDirectionUp

#### WKInterfaceController.h

Added [WKInterfaceController.crownSequencer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648288-crownsequencer)Added [-[WKInterfaceController handleActionWithIdentifier:forNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648286-handleactionwithidentifier)Added [-[WKUserNotificationInterfaceController didReceiveNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1648287-didreceive)Added [-[WKUserNotificationInterfaceController suggestionsForResponseToActionWithIdentifier:forNotification:inputLanguage:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1650691-suggestionsforresponsetoaction)Modified [-[WKInterfaceController handleActionWithIdentifier:forLocalNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619516-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKInterfaceController handleActionWithIdentifier:forRemoteNotification:]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619530-handleactionwithidentifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKUserNotificationInterfaceController didReceiveLocalNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619534-didreceivelocalnotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKUserNotificationInterfaceController didReceiveRemoteNotification:withCompletion:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619568-didreceiveremotenotification)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKUserNotificationInterfaceController suggestionsForResponseToActionWithIdentifier:forLocalNotification:inputLanguage:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1628142-suggestionsforresponsetoaction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

Modified [-[WKUserNotificationInterfaceController suggestionsForResponseToActionWithIdentifier:forRemoteNotification:inputLanguage:]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1628132-suggestionsforresponsetoactionwi)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | watchOS 3.0 |

#### WKInterfaceDevice.h

Added [WKInterfaceDevice.crownOrientation](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1650805-crownorientation)Added [WKInterfaceDevice.waterResistanceRating](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/2293683-waterresistancerating)Added [WKInterfaceDevice.wristLocation](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1650810-wristlocation)Added [WKInterfaceDeviceCrownOrientation](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation)Added [WKInterfaceDeviceCrownOrientationLeft](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation/wkinterfacedevicecrownorientationleft)Added [WKInterfaceDeviceCrownOrientationRight](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation/wkinterfacedevicecrownorientationright)Added [WKInterfaceDeviceWristLocation](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation)Added [WKInterfaceDeviceWristLocationLeft](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation/left)Added [WKInterfaceDeviceWristLocationRight](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation/right)Added [WKWaterResistanceRating](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating)Added [WKWaterResistanceRatingIPX7](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/wkwaterresistanceratingipx7)Added [WKWaterResistanceRatingWR50](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/wkwaterresistanceratingwr50)

#### WKInterfaceHMCamera.h (Added)

Added [WKInterfaceHMCamera](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera)Added [-[WKInterfaceHMCamera setCameraSource:]](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera/1833710-setcamerasource)

#### WKInterfaceInlineMovie.h (Added)

Added [WKInterfaceInlineMovie](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie)Added [-[WKInterfaceInlineMovie pause]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650859-pause)Added [-[WKInterfaceInlineMovie play]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650853-play)Added [-[WKInterfaceInlineMovie playFromBeginning]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650854-playfrombeginning)Added [-[WKInterfaceInlineMovie setAutoplays:]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650855-setautoplays)Added [-[WKInterfaceInlineMovie setLoops:]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650851-setloops)Added [-[WKInterfaceInlineMovie setMovieURL:]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650858-setmovieurl)Added [-[WKInterfaceInlineMovie setPosterImage:]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650857-setposterimage)Added [-[WKInterfaceInlineMovie setVideoGravity:]](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650856-setvideogravity)

#### WKInterfacePaymentButton.h (Added)

Added [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton)

#### WKInterfaceSCNScene.h (Added)

Added [WKInterfaceSCNScene](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene)Added [WKInterfaceSCNScene.antialiasingMode](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650881-antialiasingmode)Added [WKInterfaceSCNScene.preferredFramesPerSecond](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650883-preferredframespersecond)Added [WKInterfaceSCNScene.scene](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650879-scene)Added [-[WKInterfaceSCNScene snapshot]](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650882-snapshot)

#### WKInterfaceSKScene.h (Added)

Added [WKInterfaceSKScene](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene)Added [WKInterfaceSKScene.paused](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650797-paused)Added [WKInterfaceSKScene.preferredFramesPerSecond](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650796-preferredframespersecond)Added [-[WKInterfaceSKScene presentScene:]](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650801-presentscene)Added [-[WKInterfaceSKScene presentScene:transition:]](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650799-presentscene)Added [WKInterfaceSKScene.scene](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650798-scene)Added [-[WKInterfaceSKScene textureFromNode:]](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650800-texturefromnode)Added [-[WKInterfaceSKScene textureFromNode:crop:]](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650802-texturefromnode)

#### WKInterfaceTable.h

Added [-[WKInterfaceTable performSegueForRow:]](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1650850-performsegue)

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
