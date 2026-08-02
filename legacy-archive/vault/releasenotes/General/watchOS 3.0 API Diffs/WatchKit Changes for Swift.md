---
title: watchOS 3.0 API Diffs
apple_id: TP40017328
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS30APIDiffs/Swift/WatchKit.html
archived_at: '2026-07-18T02:58:36.035025Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 3.0 API Diffs](watchOS%202.2%20to%20watchOS%203.0%20API%20Differences.md)


# WatchKit Changes for Swift

### WatchKit

Removed WKInterfaceController.reloadRootControllers(_: [(name: String, context: AnyObject)]) [class]Added [WatchKitError [struct]](https://developer.apple.com/documentation/watchkit/watchkiterror)Added [WatchKitError.applicationDelegateWatchKitRequestReplyNotCalled](https://developer.apple.com/documentation/watchkit/watchkiterror/2320710-applicationdelegatewatchkitreque)Added [WatchKitError.downloadFailed](https://developer.apple.com/documentation/watchkit/watchkiterror/2320715-downloadfailed)Added WatchKitError.init(_nsError: NSError)Added [WatchKitError.invalidArgument](https://developer.apple.com/documentation/watchkit/watchkiterror/2320711-invalidargument)Added [WatchKitError.mediaPlayerFailed](https://developer.apple.com/documentation/watchkit/watchkiterror/2320714-mediaplayerfailed)Added [WatchKitError.recordingFailed](https://developer.apple.com/documentation/watchkit/watchkiterror/2320712-recordingfailed)Added [WatchKitError.unknown](https://developer.apple.com/documentation/watchkit/watchkiterror/2320713-unknown)Added [WKApplicationRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkapplicationrefreshbackgroundtask)Added [WKApplicationState [enum]](https://developer.apple.com/documentation/watchkit/wkapplicationstate)Added [WKApplicationState.active](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active)Added [WKApplicationState.background](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background)Added [WKApplicationState.inactive](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive)Added [WKCrownDelegate](https://developer.apple.com/documentation/watchkit/wkcrowndelegate)Added [WKCrownDelegate.crownDidBecomeIdle(_: WKCrownSequencer?)](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/1650884-crowndidbecomeidle)Added [WKCrownDelegate.crownDidRotate(_: WKCrownSequencer?, rotationalDelta: Double)](https://developer.apple.com/documentation/watchkit/wkcrowndelegate/1650886-crowndidrotate)Added [WKCrownSequencer](https://developer.apple.com/documentation/watchkit/wkcrownsequencer)Added [WKCrownSequencer.delegate](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650887-delegate)Added [WKCrownSequencer.focus()](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650892-focus)Added [WKCrownSequencer.isIdle](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650890-isidle)Added [WKCrownSequencer.resignFocus()](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650889-resignfocus)Added [WKCrownSequencer.rotationsPerSecond](https://developer.apple.com/documentation/watchkit/wkcrownsequencer/1650891-rotationspersecond)Added [WKExtension.applicationState](https://developer.apple.com/documentation/watchkit/wkextension/1650873-applicationstate)Added [WKExtension.scheduleBackgroundRefresh(withPreferredDate: Date, userInfo: NSSecureCoding?, scheduledCompletion: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkextension/1650848-schedulebackgroundrefresh)Added [WKExtension.scheduleSnapshotRefresh(withPreferredDate: Date, userInfo: NSSecureCoding?, scheduledCompletion: (Error?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkextension/1650837-schedulesnapshotrefresh)Added [WKExtensionDelegate.applicationDidEnterBackground()](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650865-applicationdidenterbackground)Added [WKExtensionDelegate.applicationWillEnterForeground()](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650868-applicationwillenterforeground)Added [WKExtensionDelegate.handle(_: HKWorkoutConfiguration)](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650871-handleworkoutconfiguration)Added [WKExtensionDelegate.handle(_: Set<WKRefreshBackgroundTask>)](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1650877-handle)Added [WKGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer)Added [WKGestureRecognizer.isEnabled](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650812-enabled)Added [WKGestureRecognizer.locationInObject() -> CGPoint](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650823-locationinobject)Added [WKGestureRecognizer.objectBounds() -> CGRect](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650835-objectbounds)Added [WKGestureRecognizer.state](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer/1650821-state)Added [WKGestureRecognizerState [enum]](https://developer.apple.com/documentation/watchkit/wkgesturerecognizerstate)Added WKGestureRecognizerState.beganAdded WKGestureRecognizerState.cancelledAdded WKGestureRecognizerState.changedAdded WKGestureRecognizerState.endedAdded WKGestureRecognizerState.failedAdded WKGestureRecognizerState.possibleAdded WKGestureRecognizerState.recognizedAdded [WKInterfaceController.crownSequencer](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648288-crownsequencer)Added [WKInterfaceController.handleAction(withIdentifier: String?, for: UNNotification)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1648286-handleaction)Added [WKInterfaceController.presentController(withNamesAndContexts: [(name: String, context: AnyObject)])](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/2143143-presentcontroller)Added [WKInterfaceController.reloadRootControllers(withNamesAndContexts: [(name: String, context: AnyObject)]) [class]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/2143142-reloadrootcontrollers)Added [WKInterfaceDevice.crownOrientation](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1650805-crownorientation)Added [WKInterfaceDevice.waterResistanceRating](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/2293683-waterresistancerating)Added [WKInterfaceDevice.wristLocation](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1650810-wristlocation)Added [WKInterfaceDeviceCrownOrientation [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation)Added [WKInterfaceDeviceCrownOrientation.left](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation/left)Added [WKInterfaceDeviceCrownOrientation.right](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation/right)Added [WKInterfaceDeviceWristLocation [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation)Added [WKInterfaceDeviceWristLocation.left](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation/left)Added [WKInterfaceDeviceWristLocation.right](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation/wkinterfacedevicewristlocationright)Added [WKInterfaceHMCamera](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera)Added [WKInterfaceHMCamera.setCameraSource(_: HMCameraSource?)](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera/1833710-setcamerasource)Added [WKInterfaceInlineMovie](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie)Added [WKInterfaceInlineMovie.pause()](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650859-pause)Added [WKInterfaceInlineMovie.play()](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650853-play)Added [WKInterfaceInlineMovie.playFromBeginning()](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650854-playfrombeginning)Added [WKInterfaceInlineMovie.setAutoplays(_: Bool)](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650855-setautoplays)Added [WKInterfaceInlineMovie.setLoops(_: Bool)](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650851-setloops)Added [WKInterfaceInlineMovie.setMovieURL(_: URL)](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650858-setmovieurl)Added [WKInterfaceInlineMovie.setPosterImage(_: WKImage?)](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650857-setposterimage)Added [WKInterfaceInlineMovie.setVideoGravity(_: WKVideoGravity)](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie/1650856-setvideogravity)Added [WKInterfacePaymentButton](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton)Added [WKInterfaceSCNScene](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene)Added [WKInterfaceSCNScene.antialiasingMode](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650881-antialiasingmode)Added [WKInterfaceSCNScene.preferredFramesPerSecond](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650883-preferredframespersecond)Added [WKInterfaceSCNScene.scene](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650879-scene)Added [WKInterfaceSCNScene.snapshot() -> UIImage](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene/1650882-snapshot)Added [WKInterfaceSKScene](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene)Added [WKInterfaceSKScene.isPaused](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650797-ispaused)Added [WKInterfaceSKScene.preferredFramesPerSecond](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650796-preferredframespersecond)Added [WKInterfaceSKScene.presentScene(_: SKScene?)](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650801-presentscene)Added [WKInterfaceSKScene.presentScene(_: SKScene, transition: SKTransition)](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650799-presentscene)Added [WKInterfaceSKScene.scene](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650798-scene)Added [WKInterfaceSKScene.texture(from: SKNode) -> SKTexture?](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650800-texture)Added [WKInterfaceSKScene.texture(from: SKNode, crop: CGRect) -> SKTexture?](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene/1650802-texture)Added [WKInterfaceTable.performSegue(forRow: Int)](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1650850-performsegue)Added [WKLongPressGestureRecognizer](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer)Added [WKLongPressGestureRecognizer.allowableMovement](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650814-allowablemovement)Added [WKLongPressGestureRecognizer.minimumPressDuration](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650831-minimumpressduration)Added [WKLongPressGestureRecognizer.numberOfTapsRequired](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer/1650822-numberoftapsrequired)Added [WKPanGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer)Added [WKPanGestureRecognizer.translationInObject() -> CGPoint](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/1650832-translationinobject)Added [WKPanGestureRecognizer.velocityInObject() -> CGPoint](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer/1650817-velocityinobject)Added [WKRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask)Added [WKRefreshBackgroundTask.setTaskCompleted()](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/1833709-settaskcompleted)Added [WKRefreshBackgroundTask.userInfo](https://developer.apple.com/documentation/watchkit/wkrefreshbackgroundtask/1650839-userinfo)Added [WKSnapshotRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask)Added [WKSnapshotRefreshBackgroundTask.returnToDefaultState](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/1773208-returntodefaultstate)Added [WKSnapshotRefreshBackgroundTask.setTaskCompleted(restoredDefaultState: Bool, estimatedSnapshotExpiration: Date, userInfo: NSSecureCoding?)](https://developer.apple.com/documentation/watchkit/wksnapshotrefreshbackgroundtask/1650844-settaskcompleted)Added [WKSwipeGestureRecognizer](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer)Added [WKSwipeGestureRecognizer.direction](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer/1650828-direction)Added [WKSwipeGestureRecognizerDirection [struct]](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizerdirection)Added WKSwipeGestureRecognizerDirection.downAdded [WKSwipeGestureRecognizerDirection.init(rawValue: UInt)](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizerdirection/1650893-init)Added WKSwipeGestureRecognizerDirection.leftAdded WKSwipeGestureRecognizerDirection.rightAdded WKSwipeGestureRecognizerDirection.upAdded [WKTapGestureRecognizer](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer)Added [WKTapGestureRecognizer.numberOfTapsRequired](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer/1650834-numberoftapsrequired)Added [WKURLSessionRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask)Added [WKURLSessionRefreshBackgroundTask.sessionIdentifier](https://developer.apple.com/documentation/watchkit/wkurlsessionrefreshbackgroundtask/1650836-sessionidentifier)Added [WKUserNotificationInterfaceController.didReceive(_: UNNotification, withCompletion: (WKUserNotificationInterfaceType) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1648287-didreceive)Added [WKUserNotificationInterfaceController.suggestionsForResponseToAction(withIdentifier: String, for: UNNotification, inputLanguage: String) -> [String]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1650691-suggestionsforresponsetoactionwi)Added [WKWatchConnectivityRefreshBackgroundTask](https://developer.apple.com/documentation/watchkit/wkwatchconnectivityrefreshbackgroundtask)Added [WKWaterResistanceRating [enum]](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating)Added [WKWaterResistanceRating.ipx7](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/ipx7)Added [WKWaterResistanceRating.wr50](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating/wkwaterresistanceratingwr50)Modified [NSNotification.Name.WKAudioFilePlayerItemDidPlayToEndTime](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemdidplaytoendtimenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | WKAudioFilePlayerItemDidPlayToEndTimeNotification | ``` let WKAudioFilePlayerItemDidPlayToEndTimeNotification: String ``` |
| To | WKAudioFilePlayerItemDidPlayToEndTime | ``` static let WKAudioFilePlayerItemDidPlayToEndTime: NSNotification.Name ``` |

Modified [NSNotification.Name.WKAudioFilePlayerItemFailedToPlayToEndTime](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemfailedtoplaytoendtimenotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | WKAudioFilePlayerItemFailedToPlayToEndTimeNotification | ``` let WKAudioFilePlayerItemFailedToPlayToEndTimeNotification: String ``` |
| To | WKAudioFilePlayerItemFailedToPlayToEndTime | ``` static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name ``` |

Modified [NSNotification.Name.WKAudioFilePlayerItemTimeJumped](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemtimejumpednotification)

|  | Name | Declaration |
| --- | --- | --- |
| From | WKAudioFilePlayerItemTimeJumpedNotification | ``` let WKAudioFilePlayerItemTimeJumpedNotification: String ``` |
| To | WKAudioFilePlayerItemTimeJumped | ``` static let WKAudioFilePlayerItemTimeJumped: NSNotification.Name ``` |

Modified [WatchKitError.Code [enum]](https://developer.apple.com/documentation/watchkit/watchkiterror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum WatchKitErrorCode : Int {     case UnknownError     case ApplicationDelegateWatchKitRequestReplyNotCalledError     case InvalidArgumentError     case MediaPlayerError     case DownloadError     case RecordingFailedError } extension WatchKitErrorCode : _BridgedNSError { } extension WatchKitErrorCode : _BridgedNSError { } ``` |
| To | ``` enum Code : Int {         typealias _ErrorType = WatchKitError         case unknown         case applicationDelegateWatchKitRequestReplyNotCalled         case invalidArgument         case mediaPlayerFailed         case downloadFailed         case recordingFailed     } ``` |

Modified [WatchKitError.Code.applicationDelegateWatchKitRequestReplyNotCalled](https://developer.apple.com/documentation/watchkit/watchkiterrorcode/watchkitapplicationdelegatewatchkitrequestreplynotcallederror)

|  | Declaration |
| --- | --- |
| From | ``` case ApplicationDelegateWatchKitRequestReplyNotCalledError ``` |
| To | ``` case applicationDelegateWatchKitRequestReplyNotCalled ``` |

Modified [WatchKitError.Code.downloadFailed](https://developer.apple.com/documentation/watchkit/watchkiterrorcode/watchkitdownloaderror)

|  | Declaration |
| --- | --- |
| From | ``` case DownloadError ``` |
| To | ``` case downloadFailed ``` |

Modified [WatchKitError.Code.invalidArgument](https://developer.apple.com/documentation/watchkit/watchkiterror/code/invalidargument)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidArgumentError ``` |
| To | ``` case invalidArgument ``` |

Modified [WatchKitError.Code.mediaPlayerFailed](https://developer.apple.com/documentation/watchkit/watchkiterrorcode/watchkitmediaplayererror)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case MediaPlayerError ``` | watchOS 2.0 |
| To | ``` case mediaPlayerFailed ``` | watchOS 3.0 |

Modified [WatchKitError.Code.recordingFailed](https://developer.apple.com/documentation/watchkit/watchkiterror/code/recordingfailed)

|  | Declaration |
| --- | --- |
| From | ``` case RecordingFailedError ``` |
| To | ``` case recordingFailed ``` |

Modified [WatchKitError.Code.unknown](https://developer.apple.com/documentation/watchkit/watchkiterror/code/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case UnknownError ``` |
| To | ``` case unknown ``` |

Modified [WKAccessibilityImageRegion](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKAccessibilityImageRegion : NSObject {     var frame: CGRect     var label: String } ``` | -- |
| To | ``` class WKAccessibilityImageRegion : NSObject {     var frame: CGRect     var label: String     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKAccessibilityImageRegion : CVarArg { } extension WKAccessibilityImageRegion : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKAlertAction](https://developer.apple.com/documentation/watchkit/wkalertaction)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKAlertAction : NSObject {     convenience init(title title: String, style style: WKAlertActionStyle, handler handler: WKAlertActionHandler)     class func actionWithTitle(_ title: String, style style: WKAlertActionStyle, handler handler: WKAlertActionHandler) -> Self     init() } ``` | -- |
| To | ``` class WKAlertAction : NSObject {     convenience init(title title: String, style style: WKAlertActionStyle, handler handler: WatchKit.WKAlertActionHandler)     class func withTitle(_ title: String, style style: WKAlertActionStyle, handler handler: WatchKit.WKAlertActionHandler) -> Self     init()     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKAlertAction : CVarArg { } extension WKAlertAction : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKAlertAction.init(title: String, style: WKAlertActionStyle, handler: WatchKit.WKAlertActionHandler)](https://developer.apple.com/documentation/watchkit/wkalertaction/1628193-actionwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(title title: String, style style: WKAlertActionStyle, handler handler: WKAlertActionHandler) ``` |
| To | ``` convenience init(title title: String, style style: WKAlertActionStyle, handler handler: WatchKit.WKAlertActionHandler) ``` |

Modified [WKAlertActionStyle [enum]](https://developer.apple.com/documentation/watchkit/wkalertactionstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum WKAlertActionStyle : Int {     case Default     case Cancel     case Destructive } ``` |
| To | ``` enum WKAlertActionStyle : Int {     case `default`     case cancel     case destructive } ``` |

Modified [WKAlertActionStyle.cancel](https://developer.apple.com/documentation/watchkit/wkalertactionstyle/wkalertactionstylecancel)

|  | Declaration |
| --- | --- |
| From | ``` case Cancel ``` |
| To | ``` case cancel ``` |

Modified [WKAlertActionStyle.default](https://developer.apple.com/documentation/watchkit/wkalertactionstyle/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [WKAlertActionStyle.destructive](https://developer.apple.com/documentation/watchkit/wkalertactionstyle/destructive)

|  | Declaration |
| --- | --- |
| From | ``` case Destructive ``` |
| To | ``` case destructive ``` |

Modified [WKAlertControllerStyle [enum]](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle)

|  | Declaration |
| --- | --- |
| From | ``` enum WKAlertControllerStyle : Int {     case Alert     case SideBySideButtonsAlert     case ActionSheet } ``` |
| To | ``` enum WKAlertControllerStyle : Int {     case alert     case sideBySideButtonsAlert     case actionSheet } ``` |

Modified [WKAlertControllerStyle.actionSheet](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/wkalertcontrollerstyleactionsheet)

|  | Declaration |
| --- | --- |
| From | ``` case ActionSheet ``` |
| To | ``` case actionSheet ``` |

Modified [WKAlertControllerStyle.alert](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/alert)

|  | Declaration |
| --- | --- |
| From | ``` case Alert ``` |
| To | ``` case alert ``` |

Modified [WKAlertControllerStyle.sideBySideButtonsAlert](https://developer.apple.com/documentation/watchkit/wkalertcontrollerstyle/sidebysidebuttonsalert)

|  | Declaration |
| --- | --- |
| From | ``` case SideBySideButtonsAlert ``` |
| To | ``` case sideBySideButtonsAlert ``` |

Modified [WKAudioFileAsset](https://developer.apple.com/documentation/watchkit/wkaudiofileasset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKAudioFileAsset : NSObject {     init()     convenience init(URL URL: NSURL)     class func assetWithURL(_ URL: NSURL) -> Self     convenience init(URL URL: NSURL, title title: String?, albumTitle albumTitle: String?, artist artist: String?)     class func assetWithURL(_ URL: NSURL, title title: String?, albumTitle albumTitle: String?, artist artist: String?) -> Self     var URL: NSURL { get }     var duration: NSTimeInterval { get }     var title: String? { get }     var albumTitle: String? { get }     var artist: String? { get } } ``` | -- |
| To | ``` class WKAudioFileAsset : NSObject {     init()     convenience init(url URL: URL)     class func withURL(_ URL: URL) -> Self     convenience init(url URL: URL, title title: String?, albumTitle albumTitle: String?, artist artist: String?)     class func withURL(_ URL: URL, title title: String?, albumTitle albumTitle: String?, artist artist: String?) -> Self     var url: URL { get }     var duration: TimeInterval { get }     var title: String? { get }     var albumTitle: String? { get }     var artist: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKAudioFileAsset : CVarArg { } extension WKAudioFileAsset : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKAudioFileAsset.duration](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/1628116-duration)

|  | Declaration |
| --- | --- |
| From | ``` var duration: NSTimeInterval { get } ``` |
| To | ``` var duration: TimeInterval { get } ``` |

Modified [WKAudioFileAsset.init(url: URL)](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/1628229-assetwithurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL) ``` |
| To | ``` convenience init(url URL: URL) ``` |

Modified [WKAudioFileAsset.init(url: URL, title: String?, albumTitle: String?, artist: String?)](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/1628141-assetwithurl)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(URL URL: NSURL, title title: String?, albumTitle albumTitle: String?, artist artist: String?) ``` |
| To | ``` convenience init(url URL: URL, title title: String?, albumTitle albumTitle: String?, artist artist: String?) ``` |

Modified [WKAudioFileAsset.url](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/1628176-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL { get } ``` |
| To | ``` var url: URL { get } ``` |

Modified [WKAudioFilePlayer](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKAudioFilePlayer : NSObject {     init()     convenience init(playerItem item: WKAudioFilePlayerItem)     class func playerWithPlayerItem(_ item: WKAudioFilePlayerItem) -> Self     func play()     func pause()     func replaceCurrentItemWithPlayerItem(_ item: WKAudioFilePlayerItem?)     var currentItem: WKAudioFilePlayerItem? { get }     var status: WKAudioFilePlayerStatus { get }     var error: NSError? { get }     var rate: Float     var currentTime: NSTimeInterval { get } } ``` | -- |
| To | ``` class WKAudioFilePlayer : NSObject {     init()     convenience init(playerItem item: WKAudioFilePlayerItem)     class func withPlayerItem(_ item: WKAudioFilePlayerItem) -> Self     func play()     func pause()     func replaceCurrentItem(with item: WKAudioFilePlayerItem?)     var currentItem: WKAudioFilePlayerItem? { get }     var status: WKAudioFilePlayerStatus { get }     var error: Error? { get }     var rate: Float     var currentTime: TimeInterval { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKAudioFilePlayer : CVarArg { } extension WKAudioFilePlayer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKAudioFilePlayer.currentTime](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/1628171-currenttime)

|  | Declaration |
| --- | --- |
| From | ``` var currentTime: NSTimeInterval { get } ``` |
| To | ``` var currentTime: TimeInterval { get } ``` |

Modified [WKAudioFilePlayer.error](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/1628214-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [WKAudioFilePlayer.replaceCurrentItem(with: WKAudioFilePlayerItem?)](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer/1628121-replacecurrentitemwithplayeritem)

|  | Declaration |
| --- | --- |
| From | ``` func replaceCurrentItemWithPlayerItem(_ item: WKAudioFilePlayerItem?) ``` |
| To | ``` func replaceCurrentItem(with item: WKAudioFilePlayerItem?) ``` |

Modified [WKAudioFilePlayerItem](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKAudioFilePlayerItem : NSObject {     init()      init(asset asset: WKAudioFileAsset)     class func playerItemWithAsset(_ asset: WKAudioFileAsset) -> WKAudioFilePlayerItem     var asset: WKAudioFileAsset { get }     var status: WKAudioFilePlayerItemStatus { get }     var error: NSError? { get }     var currentTime: NSTimeInterval { get } } ``` | -- |
| To | ``` class WKAudioFilePlayerItem : NSObject {     init()      init(asset asset: WKAudioFileAsset)     class func withAsset(_ asset: WKAudioFileAsset) -> WKAudioFilePlayerItem     var asset: WKAudioFileAsset { get }     var status: WKAudioFilePlayerItemStatus { get }     var error: Error? { get }     var currentTime: TimeInterval { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKAudioFilePlayerItem : CVarArg { } extension WKAudioFilePlayerItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKAudioFilePlayerItem.currentTime](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/1628158-currenttime)

|  | Declaration |
| --- | --- |
| From | ``` var currentTime: NSTimeInterval { get } ``` |
| To | ``` var currentTime: TimeInterval { get } ``` |

Modified [WKAudioFilePlayerItem.error](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem/1628195-error)

|  | Declaration |
| --- | --- |
| From | ``` var error: NSError? { get } ``` |
| To | ``` var error: Error? { get } ``` |

Modified [WKAudioFilePlayerItemStatus [enum]](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum WKAudioFilePlayerItemStatus : Int {     case Unknown     case ReadyToPlay     case Failed } ``` |
| To | ``` enum WKAudioFilePlayerItemStatus : Int {     case unknown     case readyToPlay     case failed } ``` |

Modified [WKAudioFilePlayerItemStatus.failed](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/failed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [WKAudioFilePlayerItemStatus.readyToPlay](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/wkaudiofileplayeritemstatusreadytoplay)

|  | Declaration |
| --- | --- |
| From | ``` case ReadyToPlay ``` |
| To | ``` case readyToPlay ``` |

Modified [WKAudioFilePlayerItemStatus.unknown](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemstatus/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [WKAudioFilePlayerStatus [enum]](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus)

|  | Declaration |
| --- | --- |
| From | ``` enum WKAudioFilePlayerStatus : Int {     case Unknown     case ReadyToPlay     case Failed } ``` |
| To | ``` enum WKAudioFilePlayerStatus : Int {     case unknown     case readyToPlay     case failed } ``` |

Modified [WKAudioFilePlayerStatus.failed](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/wkaudiofileplayerstatusfailed)

|  | Declaration |
| --- | --- |
| From | ``` case Failed ``` |
| To | ``` case failed ``` |

Modified [WKAudioFilePlayerStatus.readyToPlay](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/readytoplay)

|  | Declaration |
| --- | --- |
| From | ``` case ReadyToPlay ``` |
| To | ``` case readyToPlay ``` |

Modified [WKAudioFilePlayerStatus.unknown](https://developer.apple.com/documentation/watchkit/wkaudiofileplayerstatus/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [WKAudioFileQueuePlayer](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer)

|  | Declaration |
| --- | --- |
| From | ``` class WKAudioFileQueuePlayer : WKAudioFilePlayer {     convenience init(items items: [WKAudioFilePlayerItem])     class func queuePlayerWithItems(_ items: [WKAudioFilePlayerItem]) -> Self     func advanceToNextItem()     func appendItem(_ item: WKAudioFilePlayerItem)     func removeItem(_ item: WKAudioFilePlayerItem)     func removeAllItems()     var items: [WKAudioFilePlayerItem] { get } } ``` |
| To | ``` class WKAudioFileQueuePlayer : WKAudioFilePlayer {     convenience init(items items: [WKAudioFilePlayerItem])     class func withItems(_ items: [WKAudioFilePlayerItem]) -> Self     func advanceToNextItem()     func appendItem(_ item: WKAudioFilePlayerItem)     func removeItem(_ item: WKAudioFilePlayerItem)     func removeAllItems()     var items: [WKAudioFilePlayerItem] { get } } ``` |

Modified [WKAudioRecorderPreset [enum]](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset)

|  | Declaration |
| --- | --- |
| From | ``` enum WKAudioRecorderPreset : Int {     case NarrowBandSpeech     case WideBandSpeech     case HighQualityAudio } ``` |
| To | ``` enum WKAudioRecorderPreset : Int {     case narrowBandSpeech     case wideBandSpeech     case highQualityAudio } ``` |

Modified [WKAudioRecorderPreset.highQualityAudio](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/highqualityaudio)

|  | Declaration |
| --- | --- |
| From | ``` case HighQualityAudio ``` |
| To | ``` case highQualityAudio ``` |

Modified [WKAudioRecorderPreset.narrowBandSpeech](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/wkaudiorecorderpresetnarrowbandspeech)

|  | Declaration |
| --- | --- |
| From | ``` case NarrowBandSpeech ``` |
| To | ``` case narrowBandSpeech ``` |

Modified [WKAudioRecorderPreset.wideBandSpeech](https://developer.apple.com/documentation/watchkit/wkaudiorecorderpreset/widebandspeech)

|  | Declaration |
| --- | --- |
| From | ``` case WideBandSpeech ``` |
| To | ``` case wideBandSpeech ``` |

Modified [WKExtension](https://developer.apple.com/documentation/watchkit/wkextension)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKExtension : NSObject {     class func sharedExtension() -> WKExtension     func openSystemURL(_ url: NSURL)     weak var delegate: WKExtensionDelegate?     var rootInterfaceController: WKInterfaceController? { get } } ``` | -- |
| To | ``` class WKExtension : NSObject {     class func shared() -> WKExtension     func openSystemURL(_ url: URL)     weak var delegate: WKExtensionDelegate?     var rootInterfaceController: WKInterfaceController? { get }     var applicationState: WKApplicationState { get }     func scheduleBackgroundRefresh(withPreferredDate preferredFireDate: Date, userInfo userInfo: NSSecureCoding?, scheduledCompletion scheduledCompletion: @escaping (Error?) -> Swift.Void)     func scheduleSnapshotRefresh(withPreferredDate preferredFireDate: Date, userInfo userInfo: NSSecureCoding?, scheduledCompletion scheduledCompletion: @escaping (Error?) -> Swift.Void)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKExtension {     func scheduleBackgroundRefresh(withPreferredDate preferredFireDate: Date, userInfo userInfo: NSSecureCoding?, scheduledCompletion scheduledCompletion: @escaping (Error?) -> Swift.Void)     func scheduleSnapshotRefresh(withPreferredDate preferredFireDate: Date, userInfo userInfo: NSSecureCoding?, scheduledCompletion scheduledCompletion: @escaping (Error?) -> Swift.Void) } extension WKExtension : CVarArg { } extension WKExtension : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKExtension.openSystemURL(_: URL)](https://developer.apple.com/documentation/watchkit/wkextension/1628224-opensystemurl)

|  | Declaration |
| --- | --- |
| From | ``` func openSystemURL(_ url: NSURL) ``` |
| To | ``` func openSystemURL(_ url: URL) ``` |

Modified [WKExtension.shared() -> WKExtension [class]](https://developer.apple.com/documentation/watchkit/wkextension/1628212-sharedextension)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedExtension() -> WKExtension ``` |
| To | ``` class func shared() -> WKExtension ``` |

Modified [WKExtensionDelegate](https://developer.apple.com/documentation/watchkit/wkextensiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol WKExtensionDelegate : NSObjectProtocol {     optional func applicationDidFinishLaunching()     optional func applicationDidBecomeActive()     optional func applicationWillResignActive()     optional func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     optional func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     optional func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject], withResponseInfo responseInfo: [NSObject : AnyObject])     optional func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification, withResponseInfo responseInfo: [NSObject : AnyObject])     optional func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     optional func didReceiveRemoteNotification(_ userInfo: [NSObject : AnyObject])     optional func didReceiveLocalNotification(_ notification: UILocalNotification) } ``` |
| To | ``` protocol WKExtensionDelegate : NSObjectProtocol {     optional func applicationDidFinishLaunching()     optional func applicationDidBecomeActive()     optional func applicationWillResignActive()     optional func applicationWillEnterForeground()     optional func applicationDidEnterBackground()     optional func handle(_ workoutConfiguration: HKWorkoutConfiguration)     optional func handleUserActivity(_ userInfo: [AnyHashable : Any]?)     optional func handle(_ backgroundTasks: Set<WKRefreshBackgroundTask>)     optional func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any])     optional func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification)     optional func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any], withResponseInfo responseInfo: [AnyHashable : Any])     optional func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification, withResponseInfo responseInfo: [AnyHashable : Any])     optional func didReceiveRemoteNotification(_ userInfo: [AnyHashable : Any])     optional func didReceive(_ notification: UILocalNotification) } ``` |

Modified [WKExtensionDelegate.didReceive(_: UILocalNotification)](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628200-didreceivelocalnotification)

|  | Declaration |
| --- | --- |
| From | ``` optional func didReceiveLocalNotification(_ notification: UILocalNotification) ``` |
| To | ``` optional func didReceive(_ notification: UILocalNotification) ``` |

Modified [WKExtensionDelegate.didReceiveRemoteNotification(_: [AnyHashable : Any])](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628170-didreceiveremotenotification)

|  | Declaration |
| --- | --- |
| From | ``` optional func didReceiveRemoteNotification(_ userInfo: [NSObject : AnyObject]) ``` |
| To | ``` optional func didReceiveRemoteNotification(_ userInfo: [AnyHashable : Any]) ``` |

Modified [WKExtensionDelegate.handleAction(withIdentifier: String?, for: UILocalNotification)](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628139-handleaction)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification) ``` |
| To | ``` optional func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification) ``` |

Modified [WKExtensionDelegate.handleAction(withIdentifier: String?, for: UILocalNotification, withResponseInfo: [AnyHashable : Any])](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628242-handleaction)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification, withResponseInfo responseInfo: [NSObject : AnyObject]) ``` |
| To | ``` optional func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification, withResponseInfo responseInfo: [AnyHashable : Any]) ``` |

Modified [WKExtensionDelegate.handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628138-handleactionwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject]) ``` |
| To | ``` optional func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any]) ``` |

Modified [WKExtensionDelegate.handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any], withResponseInfo: [AnyHashable : Any])](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628160-handleactionwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject], withResponseInfo responseInfo: [NSObject : AnyObject]) ``` |
| To | ``` optional func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any], withResponseInfo responseInfo: [AnyHashable : Any]) ``` |

Modified [WKExtensionDelegate.handleUserActivity(_: [AnyHashable : Any]?)](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628223-handleuseractivity)

|  | Declaration |
| --- | --- |
| From | ``` optional func handleUserActivity(_ userInfo: [NSObject : AnyObject]?) ``` |
| To | ``` optional func handleUserActivity(_ userInfo: [AnyHashable : Any]?) ``` |

Modified [WKHapticType [enum]](https://developer.apple.com/documentation/watchkit/wkhaptictype)

|  | Declaration |
| --- | --- |
| From | ``` enum WKHapticType : Int {     case Notification     case DirectionUp     case DirectionDown     case Success     case Failure     case Retry     case Start     case Stop     case Click } ``` |
| To | ``` enum WKHapticType : Int {     case notification     case directionUp     case directionDown     case success     case failure     case retry     case start     case stop     case click } ``` |

Modified [WKHapticType.click](https://developer.apple.com/documentation/watchkit/wkhaptictype/click)

|  | Declaration |
| --- | --- |
| From | ``` case Click ``` |
| To | ``` case click ``` |

Modified [WKHapticType.directionDown](https://developer.apple.com/documentation/watchkit/wkhaptictype/wkhaptictypedirectiondown)

|  | Declaration |
| --- | --- |
| From | ``` case DirectionDown ``` |
| To | ``` case directionDown ``` |

Modified [WKHapticType.directionUp](https://developer.apple.com/documentation/watchkit/wkhaptictype/directionup)

|  | Declaration |
| --- | --- |
| From | ``` case DirectionUp ``` |
| To | ``` case directionUp ``` |

Modified [WKHapticType.failure](https://developer.apple.com/documentation/watchkit/wkhaptictype/wkhaptictypefailure)

|  | Declaration |
| --- | --- |
| From | ``` case Failure ``` |
| To | ``` case failure ``` |

Modified [WKHapticType.notification](https://developer.apple.com/documentation/watchkit/wkhaptictype/wkhaptictypenotification)

|  | Declaration |
| --- | --- |
| From | ``` case Notification ``` |
| To | ``` case notification ``` |

Modified [WKHapticType.retry](https://developer.apple.com/documentation/watchkit/wkhaptictype/wkhaptictyperetry)

|  | Declaration |
| --- | --- |
| From | ``` case Retry ``` |
| To | ``` case retry ``` |

Modified [WKHapticType.start](https://developer.apple.com/documentation/watchkit/wkhaptictype/start)

|  | Declaration |
| --- | --- |
| From | ``` case Start ``` |
| To | ``` case start ``` |

Modified [WKHapticType.stop](https://developer.apple.com/documentation/watchkit/wkhaptictype/stop)

|  | Declaration |
| --- | --- |
| From | ``` case Stop ``` |
| To | ``` case stop ``` |

Modified [WKHapticType.success](https://developer.apple.com/documentation/watchkit/wkhaptictype/success)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [WKImage](https://developer.apple.com/documentation/watchkit/wkimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKImage : NSObject, NSCopying, NSSecureCoding {     convenience init(image image: UIImage)     class func imageWithImage(_ image: UIImage) -> Self     convenience init(imageData imageData: NSData)     class func imageWithImageData(_ imageData: NSData) -> Self     convenience init(imageName imageName: String)     class func imageWithImageName(_ imageName: String) -> Self     init()     var image: UIImage? { get }     var imageData: NSData? { get }     var imageName: String? { get } } ``` | NSCopying, NSSecureCoding |
| To | ``` class WKImage : NSObject, NSCopying, NSSecureCoding {     convenience init(image image: UIImage)     class func withImage(_ image: UIImage) -> Self     convenience init(imageData imageData: Data)     class func withImageData(_ imageData: Data) -> Self     convenience init(imageName imageName: String)     class func withImageName(_ imageName: String) -> Self     init()     var image: UIImage? { get }     var imageData: Data? { get }     var imageName: String? { get }     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKImage : CVarArg { } extension WKImage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSCopying, NSSecureCoding |

Modified [WKImage.imageData](https://developer.apple.com/documentation/watchkit/wkimage/1628152-imagedata)

|  | Declaration |
| --- | --- |
| From | ``` var imageData: NSData? { get } ``` |
| To | ``` var imageData: Data? { get } ``` |

Modified [WKImage.init(imageData: Data)](https://developer.apple.com/documentation/watchkit/wkimage/1628143-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(imageData imageData: NSData) ``` |
| To | ``` convenience init(imageData imageData: Data) ``` |

Modified [WKImageAnimatable](https://developer.apple.com/documentation/watchkit/wkimageanimatable)

|  | Declaration |
| --- | --- |
| From | ``` protocol WKImageAnimatable : NSObjectProtocol {     func startAnimating()     func startAnimatingWithImagesInRange(_ imageRange: NSRange, duration duration: NSTimeInterval, repeatCount repeatCount: Int)     func stopAnimating() } ``` |
| To | ``` protocol WKImageAnimatable : NSObjectProtocol {     func startAnimating()     func startAnimatingWithImages(in imageRange: NSRange, duration duration: TimeInterval, repeatCount repeatCount: Int)     func stopAnimating() } ``` |

Modified [WKImageAnimatable.startAnimatingWithImages(in: NSRange, duration: TimeInterval, repeatCount: Int)](https://developer.apple.com/documentation/watchkit/wkimageanimatable/1615208-startanimatingwithimagesinrange)

|  | Declaration |
| --- | --- |
| From | ``` func startAnimatingWithImagesInRange(_ imageRange: NSRange, duration duration: NSTimeInterval, repeatCount repeatCount: Int) ``` |
| To | ``` func startAnimatingWithImages(in imageRange: NSRange, duration duration: TimeInterval, repeatCount repeatCount: Int) ``` |

Modified [WKInterfaceActivityRing](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceActivityRing : WKInterfaceObject {     func setActivitySummary(_ activitySummary: HKActivitySummary?, animated animated: Bool) } ``` | -- |
| To | ``` class WKInterfaceActivityRing : WKInterfaceObject {     func setActivitySummary(_ activitySummary: HKActivitySummary?, animated animated: Bool)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceActivityRing : CVarArg { } extension WKInterfaceActivityRing : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceButton](https://developer.apple.com/documentation/watchkit/wkinterfacebutton)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceButton : WKInterfaceObject {     func setTitle(_ title: String?)     func setAttributedTitle(_ attributedTitle: NSAttributedString?)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: NSData?)     func setBackgroundImageNamed(_ imageName: String?)     func setEnabled(_ enabled: Bool) } ``` | -- |
| To | ``` class WKInterfaceButton : WKInterfaceObject {     func setTitle(_ title: String?)     func setAttributedTitle(_ attributedTitle: NSAttributedString?)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: Data?)     func setBackgroundImageNamed(_ imageName: String?)     func setEnabled(_ enabled: Bool)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceButton : CVarArg { } extension WKInterfaceButton : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceButton.setBackgroundImageData(_: Data?)](https://developer.apple.com/documentation/watchkit/wkinterfacebutton/1620162-setbackgroundimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func setBackgroundImageData(_ imageData: NSData?) ``` |
| To | ``` func setBackgroundImageData(_ imageData: Data?) ``` |

Modified [WKInterfaceController](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceController : NSObject {     init()     func awakeWithContext(_ context: AnyObject?)     var contentFrame: CGRect { get }     func willActivate()     func didDeactivate()     func didAppear()     func willDisappear()     func pickerDidFocus(_ picker: WKInterfacePicker)     func pickerDidResignFocus(_ picker: WKInterfacePicker)     func pickerDidSettle(_ picker: WKInterfacePicker)     func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int)     func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject])     func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification)     func handleUserActivity(_ userInfo: [NSObject : AnyObject]?)     func setTitle(_ title: String?)     func pushControllerWithName(_ name: String, context context: AnyObject?)     func popController()     func popToRootController()     class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func becomeCurrentPage()     func presentControllerWithName(_ name: String, context context: AnyObject?)     func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?)     func dismissController()     func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func presentTextInputControllerWithSuggestionsForLanguage(_ suggestionsHandler: ((String) -> [AnyObject]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void)     func dismissTextInputController()     func presentMediaPlayerControllerWithURL(_ URL: NSURL, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSTimeInterval, NSError?) -> Void)     func dismissMediaPlayerController()     func presentAudioRecorderControllerWithOutputURL(_ URL: NSURL, preset preset: WKAudioRecorderPreset, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSError?) -> Void)     func dismissAudioRecorderController()     func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]?     func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject?     func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]?     func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void)     func presentAlertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction])     func presentAddPassesControllerWithPasses(_ passes: [PKPass], completion completion: () -> Void)     func dismissAddPassesController()     func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector)     func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector)     func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [NSObject : AnyObject], reply reply: (([NSObject : AnyObject], NSError?) -> Void)?) -> Bool     func beginGlanceUpdates()     func endGlanceUpdates() } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } extension WKInterfaceController {     class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) } ``` | -- |
| To | ``` class WKInterfaceController : NSObject {     init()     func awake(withContext context: Any?)     var contentFrame: CGRect { get }     var crownSequencer: WKCrownSequencer { get }     func willActivate()     func didDeactivate()     func didAppear()     func willDisappear()     func pickerDidFocus(_ picker: WKInterfacePicker)     func pickerDidResignFocus(_ picker: WKInterfacePicker)     func pickerDidSettle(_ picker: WKInterfacePicker)     func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int)     func handleAction(withIdentifier identifier: String?, for notification: UNNotification)     func handleUserActivity(_ userInfo: [AnyHashable : Any]?)     func setTitle(_ title: String?)     func pushController(withName name: String, context context: Any?)     func pop()     func popToRootController()     class func reloadRootControllers(withNames names: [String], contexts contexts: [Any]?)     func becomeCurrentPage()     func presentController(withName name: String, context context: Any?)     func presentController(withNames names: [String], contexts contexts: [Any]?)     func dismiss()     func presentTextInputController(withSuggestions suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: @escaping ([Any]?) -> Swift.Void)     func presentTextInputControllerWithSuggestions(forLanguage suggestionsHandler: (@escaping (String) -> [Any]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: @escaping ([Any]?) -> Swift.Void)     func dismissTextInputController()     func presentMediaPlayerController(with URL: URL, options options: [AnyHashable : Any]? = nil, completion completion: @escaping (Bool, TimeInterval, Error?) -> Swift.Void)     func dismissMediaPlayerController()     func presentAudioRecorderController(withOutputURL URL: URL, preset preset: WKAudioRecorderPreset, options options: [AnyHashable : Any]? = nil, completion completion: @escaping (Bool, Error?) -> Swift.Void)     func dismissAudioRecorderController()     func contextForSegue(withIdentifier segueIdentifier: String) -> Any?     func contextsForSegue(withIdentifier segueIdentifier: String) -> [Any]?     func contextForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex rowIndex: Int) -> Any?     func contextsForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex rowIndex: Int) -> [Any]?     func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Swift.Void)     func presentAlert(withTitle title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction])     func presentAddPassesController(withPasses passes: [PKPass], completion completion: @escaping () -> Swift.Void)     func dismissAddPassesController()     func addMenuItem(with image: UIImage, title title: String, action action: Selector)     func addMenuItem(withImageNamed imageName: String, title title: String, action action: Selector)     func addMenuItem(with itemIcon: WKMenuItemIcon, title title: String, action action: Selector)     func clearAllMenuItems()     func updateUserActivity(_ type: String, userInfo userInfo: [AnyHashable : Any]? = nil, webpageURL webpageURL: URL?)     func invalidateUserActivity()     class func openParentApplication(_ userInfo: [AnyHashable : Any], reply reply: (@escaping ([AnyHashable : Any], Error?) -> Swift.Void)? = nil) -> Bool     func beginGlanceUpdates()     func endGlanceUpdates()     func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any])     func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification)     @nonobjc final class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     class func reloadRootControllers(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])     @nonobjc final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceController : CVarArg { } extension WKInterfaceController : Equatable, Hashable {     var hashValue: Int { get } } extension WKInterfaceController {     @nonobjc final class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     class func reloadRootControllers(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])     @nonobjc final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)]) } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceController.addMenuItem(with: UIImage, title: String, action: Selector)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619552-addmenuitemwithimage)

|  | Declaration |
| --- | --- |
| From | ``` func addMenuItemWithImage(_ image: UIImage, title title: String, action action: Selector) ``` |
| To | ``` func addMenuItem(with image: UIImage, title title: String, action action: Selector) ``` |

Modified [WKInterfaceController.addMenuItem(with: WKMenuItemIcon, title: String, action: Selector)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619520-addmenuitemwithitemicon)

|  | Declaration |
| --- | --- |
| From | ``` func addMenuItemWithItemIcon(_ itemIcon: WKMenuItemIcon, title title: String, action action: Selector) ``` |
| To | ``` func addMenuItem(with itemIcon: WKMenuItemIcon, title title: String, action action: Selector) ``` |

Modified [WKInterfaceController.addMenuItem(withImageNamed: String, title: String, action: Selector)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619515-addmenuitemwithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` func addMenuItemWithImageNamed(_ imageName: String, title title: String, action action: Selector) ``` |
| To | ``` func addMenuItem(withImageNamed imageName: String, title title: String, action action: Selector) ``` |

Modified [WKInterfaceController.animate(withDuration: TimeInterval, animations: () -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1628239-animate)

|  | Declaration |
| --- | --- |
| From | ``` func animateWithDuration(_ duration: NSTimeInterval, animations animations: () -> Void) ``` |
| To | ``` func animate(withDuration duration: TimeInterval, animations animations: @escaping () -> Swift.Void) ``` |

Modified [WKInterfaceController.awake(withContext: Any?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619543-awakewithcontext)

|  | Declaration |
| --- | --- |
| From | ``` func awakeWithContext(_ context: AnyObject?) ``` |
| To | ``` func awake(withContext context: Any?) ``` |

Modified [WKInterfaceController.contextForSegue(withIdentifier: String) -> Any?](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619522-contextforseguewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func contextForSegueWithIdentifier(_ segueIdentifier: String) -> AnyObject? ``` |
| To | ``` func contextForSegue(withIdentifier segueIdentifier: String) -> Any? ``` |

Modified [WKInterfaceController.contextForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> Any?](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619514-contextforseguewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func contextForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> AnyObject? ``` |
| To | ``` func contextForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex rowIndex: Int) -> Any? ``` |

Modified [WKInterfaceController.contextsForSegue(withIdentifier: String) -> [Any]?](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619533-contextsforsegue)

|  | Declaration |
| --- | --- |
| From | ``` func contextsForSegueWithIdentifier(_ segueIdentifier: String) -> [AnyObject]? ``` |
| To | ``` func contextsForSegue(withIdentifier segueIdentifier: String) -> [Any]? ``` |

Modified [WKInterfaceController.contextsForSegue(withIdentifier: String, in: WKInterfaceTable, rowIndex: Int) -> [Any]?](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619544-contextsforseguewithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func contextsForSegueWithIdentifier(_ segueIdentifier: String, inTable table: WKInterfaceTable, rowIndex rowIndex: Int) -> [AnyObject]? ``` |
| To | ``` func contextsForSegue(withIdentifier segueIdentifier: String, in table: WKInterfaceTable, rowIndex rowIndex: Int) -> [Any]? ``` |

Modified [WKInterfaceController.dismiss()](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619556-dismisscontroller)

|  | Declaration |
| --- | --- |
| From | ``` func dismissController() ``` |
| To | ``` func dismiss() ``` |

Modified [WKInterfaceController.handleAction(withIdentifier: String?, for: UILocalNotification)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619516-handleaction)

|  | Declaration |
| --- | --- |
| From | ``` func handleActionWithIdentifier(_ identifier: String?, forLocalNotification localNotification: UILocalNotification) ``` |
| To | ``` func handleAction(withIdentifier identifier: String?, for localNotification: UILocalNotification) ``` |

Modified [WKInterfaceController.handleAction(withIdentifier: String?, forRemoteNotification: [AnyHashable : Any])](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619530-handleaction)

|  | Declaration |
| --- | --- |
| From | ``` func handleActionWithIdentifier(_ identifier: String?, forRemoteNotification remoteNotification: [NSObject : AnyObject]) ``` |
| To | ``` func handleAction(withIdentifier identifier: String?, forRemoteNotification remoteNotification: [AnyHashable : Any]) ``` |

Modified [WKInterfaceController.handleUserActivity(_: [AnyHashable : Any]?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619573-handleuseractivity)

|  | Declaration |
| --- | --- |
| From | ``` func handleUserActivity(_ userInfo: [NSObject : AnyObject]?) ``` |
| To | ``` func handleUserActivity(_ userInfo: [AnyHashable : Any]?) ``` |

Modified [WKInterfaceController.pop()](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619548-popcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func popController() ``` |
| To | ``` func pop() ``` |

Modified [WKInterfaceController.presentAddPassesController(withPasses: [PKPass], completion: () -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1628236-presentaddpassescontrollerwithpa)

|  | Declaration |
| --- | --- |
| From | ``` func presentAddPassesControllerWithPasses(_ passes: [PKPass], completion completion: () -> Void) ``` |
| To | ``` func presentAddPassesController(withPasses passes: [PKPass], completion completion: @escaping () -> Swift.Void) ``` |

Modified [WKInterfaceController.presentAlert(withTitle: String?, message: String?, preferredStyle: WKAlertControllerStyle, actions: [WKAlertAction])](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1628243-presentalert)

|  | Declaration |
| --- | --- |
| From | ``` func presentAlertControllerWithTitle(_ title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction]) ``` |
| To | ``` func presentAlert(withTitle title: String?, message message: String?, preferredStyle preferredStyle: WKAlertControllerStyle, actions actions: [WKAlertAction]) ``` |

Modified [WKInterfaceController.presentAudioRecorderController(withOutputURL: URL, preset: WKAudioRecorderPreset, options: [AnyHashable : Any]?, completion: (Bool, Error?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1628147-presentaudiorecordercontrollerwi)

|  | Declaration |
| --- | --- |
| From | ``` func presentAudioRecorderControllerWithOutputURL(_ URL: NSURL, preset preset: WKAudioRecorderPreset, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSError?) -> Void) ``` |
| To | ``` func presentAudioRecorderController(withOutputURL URL: URL, preset preset: WKAudioRecorderPreset, options options: [AnyHashable : Any]? = nil, completion completion: @escaping (Bool, Error?) -> Swift.Void) ``` |

Modified [WKInterfaceController.presentController(_: [(name: String, context: AnyObject)])](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1620858-presentcontroller)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) ``` | -- |
| To | ``` @nonobjc final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)]) ``` | watchOS 3.0 |

Modified [WKInterfaceController.presentController(withName: String, context: Any?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619560-presentcontrollerwithname)

|  | Declaration |
| --- | --- |
| From | ``` func presentControllerWithName(_ name: String, context context: AnyObject?) ``` |
| To | ``` func presentController(withName name: String, context context: Any?) ``` |

Modified [WKInterfaceController.presentController(withNames: [String], contexts: [Any]?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619561-presentcontrollerwithnames)

|  | Declaration |
| --- | --- |
| From | ``` func presentControllerWithNames(_ names: [String], contexts contexts: [AnyObject]?) ``` |
| To | ``` func presentController(withNames names: [String], contexts contexts: [Any]?) ``` |

Modified [WKInterfaceController.presentMediaPlayerController(with: URL, options: [AnyHashable : Any]?, completion: (Bool, TimeInterval, Error?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1628203-presentmediaplayercontrollerwith)

|  | Declaration |
| --- | --- |
| From | ``` func presentMediaPlayerControllerWithURL(_ URL: NSURL, options options: [NSObject : AnyObject]?, completion completion: (Bool, NSTimeInterval, NSError?) -> Void) ``` |
| To | ``` func presentMediaPlayerController(with URL: URL, options options: [AnyHashable : Any]? = nil, completion completion: @escaping (Bool, TimeInterval, Error?) -> Swift.Void) ``` |

Modified [WKInterfaceController.presentTextInputController(withSuggestions: [String]?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619527-presenttextinputcontrollerwithsu)

|  | Declaration |
| --- | --- |
| From | ``` func presentTextInputControllerWithSuggestions(_ suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void) ``` |
| To | ``` func presentTextInputController(withSuggestions suggestions: [String]?, allowedInputMode inputMode: WKTextInputMode, completion completion: @escaping ([Any]?) -> Swift.Void) ``` |

Modified [WKInterfaceController.presentTextInputControllerWithSuggestions(forLanguage: ( (String) -> [Any]?)?, allowedInputMode: WKTextInputMode, completion: ([Any]?) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619574-presenttextinputcontrollerwithsu)

|  | Declaration |
| --- | --- |
| From | ``` func presentTextInputControllerWithSuggestionsForLanguage(_ suggestionsHandler: ((String) -> [AnyObject]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: ([AnyObject]?) -> Void) ``` |
| To | ``` func presentTextInputControllerWithSuggestions(forLanguage suggestionsHandler: (@escaping (String) -> [Any]?)?, allowedInputMode inputMode: WKTextInputMode, completion completion: @escaping ([Any]?) -> Swift.Void) ``` |

Modified [WKInterfaceController.pushController(withName: String, context: Any?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619532-pushcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func pushControllerWithName(_ name: String, context context: AnyObject?) ``` |
| To | ``` func pushController(withName name: String, context context: Any?) ``` |

Modified [WKInterfaceController.reloadRootControllers(withNames: [String], contexts: [Any]?) [class]](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619563-reloadrootcontrollers)

|  | Declaration |
| --- | --- |
| From | ``` class func reloadRootControllersWithNames(_ names: [String], contexts contexts: [AnyObject]?) ``` |
| To | ``` class func reloadRootControllers(withNames names: [String], contexts contexts: [Any]?) ``` |

Modified [WKInterfaceController.table(_: WKInterfaceTable, didSelectRowAt: Int)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619575-table)

|  | Declaration |
| --- | --- |
| From | ``` func table(_ table: WKInterfaceTable, didSelectRowAtIndex rowIndex: Int) ``` |
| To | ``` func table(_ table: WKInterfaceTable, didSelectRowAt rowIndex: Int) ``` |

Modified [WKInterfaceController.updateUserActivity(_: String, userInfo: [AnyHashable : Any]?, webpageURL: URL?)](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/1619553-updateuseractivity)

|  | Declaration |
| --- | --- |
| From | ``` func updateUserActivity(_ type: String, userInfo userInfo: [NSObject : AnyObject]?, webpageURL webpageURL: NSURL?) ``` |
| To | ``` func updateUserActivity(_ type: String, userInfo userInfo: [AnyHashable : Any]? = nil, webpageURL webpageURL: URL?) ``` |

Modified [WKInterfaceDate](https://developer.apple.com/documentation/watchkit/wkinterfacedate)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceDate : WKInterfaceObject {     func setTextColor(_ color: UIColor?)     func setTimeZone(_ timeZone: NSTimeZone?)     func setCalendar(_ calendar: NSCalendar?) } ``` | -- |
| To | ``` class WKInterfaceDate : WKInterfaceObject {     func setTextColor(_ color: UIColor?)     func setTimeZone(_ timeZone: TimeZone?)     func setCalendar(_ calendar: Calendar?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceDate : CVarArg { } extension WKInterfaceDate : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceDate.setCalendar(_: Calendar?)](https://developer.apple.com/documentation/watchkit/wkinterfacedate/1620871-setcalendar)

|  | Declaration |
| --- | --- |
| From | ``` func setCalendar(_ calendar: NSCalendar?) ``` |
| To | ``` func setCalendar(_ calendar: Calendar?) ``` |

Modified [WKInterfaceDate.setTimeZone(_: TimeZone?)](https://developer.apple.com/documentation/watchkit/wkinterfacedate/1620854-settimezone)

|  | Declaration |
| --- | --- |
| From | ``` func setTimeZone(_ timeZone: NSTimeZone?) ``` |
| To | ``` func setTimeZone(_ timeZone: TimeZone?) ``` |

Modified [WKInterfaceDevice](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceDevice : NSObject {     class func currentDevice() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImageWithData(_ imageData: NSData, name name: String) -> Bool     func removeCachedImageWithName(_ name: String)     func removeAllCachedImages()     var cachedImages: [String : NSNumber] { get }     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var layoutDirection: WKInterfaceLayoutDirection { get }     class func interfaceLayoutDirectionForSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     func playHaptic(_ type: WKHapticType) } ``` | -- |
| To | ``` class WKInterfaceDevice : NSObject {     class func current() -> WKInterfaceDevice     func addCachedImage(_ image: UIImage, name name: String) -> Bool     func addCachedImage(with imageData: Data, name name: String) -> Bool     func removeCachedImage(withName name: String)     func removeAllCachedImages()     var cachedImages: [String : NSNumber] { get }     var screenBounds: CGRect { get }     var screenScale: CGFloat { get }     var preferredContentSizeCategory: String { get }     var layoutDirection: WKInterfaceLayoutDirection { get }     var wristLocation: WKInterfaceDeviceWristLocation { get }     var crownOrientation: WKInterfaceDeviceCrownOrientation { get }     class func interfaceLayoutDirection(for semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection     var systemVersion: String { get }     var name: String { get }     var model: String { get }     var localizedModel: String { get }     var systemName: String { get }     var waterResistanceRating: WKWaterResistanceRating { get }     func play(_ type: WKHapticType)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceDevice : CVarArg { } extension WKInterfaceDevice : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceDevice.current() -> WKInterfaceDevice [class]](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1620961-currentdevice)

|  | Declaration |
| --- | --- |
| From | ``` class func currentDevice() -> WKInterfaceDevice ``` |
| To | ``` class func current() -> WKInterfaceDevice ``` |

Modified [WKInterfaceDevice.interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection [class]](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1628117-interfacelayoutdirection)

|  | Declaration |
| --- | --- |
| From | ``` class func interfaceLayoutDirectionForSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection ``` |
| To | ``` class func interfaceLayoutDirection(for semanticContentAttribute: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection ``` |

Modified [WKInterfaceDevice.play(_: WKHapticType)](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/1628128-playhaptic)

|  | Declaration |
| --- | --- |
| From | ``` func playHaptic(_ type: WKHapticType) ``` |
| To | ``` func play(_ type: WKHapticType) ``` |

Modified [WKInterfaceGroup](https://developer.apple.com/documentation/watchkit/wkinterfacegroup)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceGroup : WKInterfaceObject, WKImageAnimatable {     func setCornerRadius(_ cornerRadius: CGFloat)     func setContentInset(_ contentInset: UIEdgeInsets)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: NSData?)     func setBackgroundImageNamed(_ imageName: String?) } ``` | WKImageAnimatable |
| To | ``` class WKInterfaceGroup : WKInterfaceObject, WKImageAnimatable {     func setCornerRadius(_ cornerRadius: CGFloat)     func setContentInset(_ contentInset: UIEdgeInsets)     func setBackgroundColor(_ color: UIColor?)     func setBackgroundImage(_ image: UIImage?)     func setBackgroundImageData(_ imageData: Data?)     func setBackgroundImageNamed(_ imageName: String?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceGroup : CVarArg { } extension WKInterfaceGroup : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, WKImageAnimatable |

Modified [WKInterfaceGroup.setBackgroundImageData(_: Data?)](https://developer.apple.com/documentation/watchkit/wkinterfacegroup/1619662-setbackgroundimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func setBackgroundImageData(_ imageData: NSData?) ``` |
| To | ``` func setBackgroundImageData(_ imageData: Data?) ``` |

Modified [WKInterfaceImage](https://developer.apple.com/documentation/watchkit/wkinterfaceimage)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceImage : WKInterfaceObject, WKImageAnimatable {     func setImage(_ image: UIImage?)     func setImageData(_ imageData: NSData?)     func setImageNamed(_ imageName: String?)     func setTintColor(_ tintColor: UIColor?) } ``` | WKImageAnimatable |
| To | ``` class WKInterfaceImage : WKInterfaceObject, WKImageAnimatable {     func setImage(_ image: UIImage?)     func setImageData(_ imageData: Data?)     func setImageNamed(_ imageName: String?)     func setTintColor(_ tintColor: UIColor?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceImage : CVarArg { } extension WKInterfaceImage : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, WKImageAnimatable |

Modified [WKInterfaceImage.setImageData(_: Data?)](https://developer.apple.com/documentation/watchkit/wkinterfaceimage/1615217-setimagedata)

|  | Declaration |
| --- | --- |
| From | ``` func setImageData(_ imageData: NSData?) ``` |
| To | ``` func setImageData(_ imageData: Data?) ``` |

Modified [WKInterfaceLabel](https://developer.apple.com/documentation/watchkit/wkinterfacelabel)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceLabel : WKInterfaceObject {     func setText(_ text: String?)     func setTextColor(_ color: UIColor?)     func setAttributedText(_ attributedText: NSAttributedString?) } ``` | -- |
| To | ``` class WKInterfaceLabel : WKInterfaceObject {     func setText(_ text: String?)     func setTextColor(_ color: UIColor?)     func setAttributedText(_ attributedText: NSAttributedString?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceLabel : CVarArg { } extension WKInterfaceLabel : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceLayoutDirection [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection)

|  | Declaration |
| --- | --- |
| From | ``` enum WKInterfaceLayoutDirection : Int {     case LeftToRight     case RightToLeft } ``` |
| To | ``` enum WKInterfaceLayoutDirection : Int {     case leftToRight     case rightToLeft } ``` |

Modified [WKInterfaceLayoutDirection.leftToRight](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection/lefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case LeftToRight ``` |
| To | ``` case leftToRight ``` |

Modified [WKInterfaceLayoutDirection.rightToLeft](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection/righttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case RightToLeft ``` |
| To | ``` case rightToLeft ``` |

Modified [WKInterfaceMap](https://developer.apple.com/documentation/watchkit/wkinterfacemap)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceMap : WKInterfaceObject {     func setVisibleMapRect(_ mapRect: MKMapRect)     func setRegion(_ coordinateRegion: MKCoordinateRegion)     func addAnnotation(_ location: CLLocationCoordinate2D, withImage image: UIImage?, centerOffset offset: CGPoint)     func addAnnotation(_ location: CLLocationCoordinate2D, withImageNamed name: String?, centerOffset offset: CGPoint)     func addAnnotation(_ location: CLLocationCoordinate2D, withPinColor pinColor: WKInterfaceMapPinColor)     func removeAllAnnotations() } ``` | -- |
| To | ``` class WKInterfaceMap : WKInterfaceObject {     func setVisibleMapRect(_ mapRect: MKMapRect)     func setRegion(_ coordinateRegion: MKCoordinateRegion)     func addAnnotation(_ location: CLLocationCoordinate2D, with image: UIImage?, centerOffset offset: CGPoint)     func addAnnotation(_ location: CLLocationCoordinate2D, withImageNamed name: String?, centerOffset offset: CGPoint)     func addAnnotation(_ location: CLLocationCoordinate2D, with pinColor: WKInterfaceMapPinColor)     func removeAllAnnotations()     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceMap : CVarArg { } extension WKInterfaceMap : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceMap.addAnnotation(_: CLLocationCoordinate2D, with: WKInterfaceMapPinColor)](https://developer.apple.com/documentation/watchkit/wkinterfacemap/1619888-addannotation)

|  | Declaration |
| --- | --- |
| From | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withPinColor pinColor: WKInterfaceMapPinColor) ``` |
| To | ``` func addAnnotation(_ location: CLLocationCoordinate2D, with pinColor: WKInterfaceMapPinColor) ``` |

Modified [WKInterfaceMap.addAnnotation(_: CLLocationCoordinate2D, with: UIImage?, centerOffset: CGPoint)](https://developer.apple.com/documentation/watchkit/wkinterfacemap/1619883-addannotation)

|  | Declaration |
| --- | --- |
| From | ``` func addAnnotation(_ location: CLLocationCoordinate2D, withImage image: UIImage?, centerOffset offset: CGPoint) ``` |
| To | ``` func addAnnotation(_ location: CLLocationCoordinate2D, with image: UIImage?, centerOffset offset: CGPoint) ``` |

Modified [WKInterfaceMapPinColor [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor)

|  | Declaration |
| --- | --- |
| From | ``` enum WKInterfaceMapPinColor : Int {     case Red     case Green     case Purple } ``` |
| To | ``` enum WKInterfaceMapPinColor : Int {     case red     case green     case purple } ``` |

Modified [WKInterfaceMapPinColor.green](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor/wkinterfacemappincolorgreen)

|  | Declaration |
| --- | --- |
| From | ``` case Green ``` |
| To | ``` case green ``` |

Modified [WKInterfaceMapPinColor.purple](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor/wkinterfacemappincolorpurple)

|  | Declaration |
| --- | --- |
| From | ``` case Purple ``` |
| To | ``` case purple ``` |

Modified [WKInterfaceMapPinColor.red](https://developer.apple.com/documentation/watchkit/wkinterfacemappincolor/red)

|  | Declaration |
| --- | --- |
| From | ``` case Red ``` |
| To | ``` case red ``` |

Modified [WKInterfaceMovie](https://developer.apple.com/documentation/watchkit/wkinterfacemovie)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceMovie : WKInterfaceObject {     func setMovieURL(_ URL: NSURL)     func setVideoGravity(_ videoGravity: WKVideoGravity)     func setLoops(_ loops: Bool)     func setPosterImage(_ posterImage: WKImage?) } ``` | -- |
| To | ``` class WKInterfaceMovie : WKInterfaceObject {     func setMovieURL(_ URL: URL)     func setVideoGravity(_ videoGravity: WKVideoGravity)     func setLoops(_ loops: Bool)     func setPosterImage(_ posterImage: WKImage?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceMovie : CVarArg { } extension WKInterfaceMovie : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceMovie.setMovieURL(_: URL)](https://developer.apple.com/documentation/watchkit/wkinterfacemovie/1628144-setmovieurl)

|  | Declaration |
| --- | --- |
| From | ``` func setMovieURL(_ URL: NSURL) ``` |
| To | ``` func setMovieURL(_ URL: URL) ``` |

Modified [WKInterfaceObject](https://developer.apple.com/documentation/watchkit/wkinterfaceobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` | -- |
| To | ``` class WKInterfaceObject : NSObject {     init()     func setHidden(_ hidden: Bool)     func setAlpha(_ alpha: CGFloat)     func setSemanticContentAttribute(_ semanticContentAttribute: WKInterfaceSemanticContentAttribute)     func setHorizontalAlignment(_ horizontalAlignment: WKInterfaceObjectHorizontalAlignment)     func setVerticalAlignment(_ verticalAlignment: WKInterfaceObjectVerticalAlignment)     func setWidth(_ width: CGFloat)     func setHeight(_ height: CGFloat)     func setRelativeWidth(_ width: CGFloat, withAdjustment adjustment: CGFloat)     func setRelativeHeight(_ height: CGFloat, withAdjustment adjustment: CGFloat)     func sizeToFitWidth()     func sizeToFitHeight()     var interfaceProperty: String { get }     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceObject : CVarArg { } extension WKInterfaceObject : Equatable, Hashable {     var hashValue: Int { get } } extension WKInterfaceObject {     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion]) } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceObjectHorizontalAlignment [enum]](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum WKInterfaceObjectHorizontalAlignment : Int {     case Left     case Center     case Right } ``` |
| To | ``` enum WKInterfaceObjectHorizontalAlignment : Int {     case left     case center     case right } ``` |

Modified [WKInterfaceObjectHorizontalAlignment.center](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment/center)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [WKInterfaceObjectHorizontalAlignment.left](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment/wkinterfaceobjecthorizontalalignmentleft)

|  | Declaration |
| --- | --- |
| From | ``` case Left ``` |
| To | ``` case left ``` |

Modified [WKInterfaceObjectHorizontalAlignment.right](https://developer.apple.com/documentation/watchkit/wkinterfaceobjecthorizontalalignment/wkinterfaceobjecthorizontalalignmentright)

|  | Declaration |
| --- | --- |
| From | ``` case Right ``` |
| To | ``` case right ``` |

Modified [WKInterfaceObjectVerticalAlignment [enum]](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment)

|  | Declaration |
| --- | --- |
| From | ``` enum WKInterfaceObjectVerticalAlignment : Int {     case Top     case Center     case Bottom } ``` |
| To | ``` enum WKInterfaceObjectVerticalAlignment : Int {     case top     case center     case bottom } ``` |

Modified [WKInterfaceObjectVerticalAlignment.bottom](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment/wkinterfaceobjectverticalalignmentbottom)

|  | Declaration |
| --- | --- |
| From | ``` case Bottom ``` |
| To | ``` case bottom ``` |

Modified [WKInterfaceObjectVerticalAlignment.center](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment/wkinterfaceobjectverticalalignmentcenter)

|  | Declaration |
| --- | --- |
| From | ``` case Center ``` |
| To | ``` case center ``` |

Modified [WKInterfaceObjectVerticalAlignment.top](https://developer.apple.com/documentation/watchkit/wkinterfaceobjectverticalalignment/top)

|  | Declaration |
| --- | --- |
| From | ``` case Top ``` |
| To | ``` case top ``` |

Modified [WKInterfacePicker](https://developer.apple.com/documentation/watchkit/wkinterfacepicker)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfacePicker : WKInterfaceObject {     func focus()     func resignFocus()     func setSelectedItemIndex(_ itemIndex: Int)     func setItems(_ items: [WKPickerItem]?)     func setCoordinatedAnimations(_ coordinatedAnimations: [WKInterfaceObject]?)     func setEnabled(_ enabled: Bool) } ``` | -- |
| To | ``` class WKInterfacePicker : WKInterfaceObject {     func focus()     func resignFocus()     func setSelectedItemIndex(_ itemIndex: Int)     func setItems(_ items: [WKPickerItem]?)     func setCoordinatedAnimations(_ coordinatedAnimations: [WKInterfaceObject]?)     func setEnabled(_ enabled: Bool)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfacePicker : CVarArg { } extension WKInterfacePicker : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceSemanticContentAttribute [enum]](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute)

|  | Declaration |
| --- | --- |
| From | ``` enum WKInterfaceSemanticContentAttribute : Int {     case Unspecified     case Playback     case Spatial     case ForceLeftToRight     case ForceRightToLeft } ``` |
| To | ``` enum WKInterfaceSemanticContentAttribute : Int {     case unspecified     case playback     case spatial     case forceLeftToRight     case forceRightToLeft } ``` |

Modified [WKInterfaceSemanticContentAttribute.forceLeftToRight](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeforcelefttoright)

|  | Declaration |
| --- | --- |
| From | ``` case ForceLeftToRight ``` |
| To | ``` case forceLeftToRight ``` |

Modified [WKInterfaceSemanticContentAttribute.forceRightToLeft](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeforcerighttoleft)

|  | Declaration |
| --- | --- |
| From | ``` case ForceRightToLeft ``` |
| To | ``` case forceRightToLeft ``` |

Modified [WKInterfaceSemanticContentAttribute.playback](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/playback)

|  | Declaration |
| --- | --- |
| From | ``` case Playback ``` |
| To | ``` case playback ``` |

Modified [WKInterfaceSemanticContentAttribute.spatial](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributespatial)

|  | Declaration |
| --- | --- |
| From | ``` case Spatial ``` |
| To | ``` case spatial ``` |

Modified [WKInterfaceSemanticContentAttribute.unspecified](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute/wkinterfacesemanticcontentattributeunspecified)

|  | Declaration |
| --- | --- |
| From | ``` case Unspecified ``` |
| To | ``` case unspecified ``` |

Modified [WKInterfaceSeparator](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceSeparator : WKInterfaceObject {     func setColor(_ color: UIColor?) } ``` | -- |
| To | ``` class WKInterfaceSeparator : WKInterfaceObject {     func setColor(_ color: UIColor?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceSeparator : CVarArg { } extension WKInterfaceSeparator : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceSlider](https://developer.apple.com/documentation/watchkit/wkinterfaceslider)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceSlider : WKInterfaceObject {     func setEnabled(_ enabled: Bool)     func setValue(_ value: Float)     func setColor(_ color: UIColor?)     func setNumberOfSteps(_ numberOfSteps: Int) } ``` | -- |
| To | ``` class WKInterfaceSlider : WKInterfaceObject {     func setEnabled(_ enabled: Bool)     func setValue(_ value: Float)     func setColor(_ color: UIColor?)     func setNumberOfSteps(_ numberOfSteps: Int)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceSlider : CVarArg { } extension WKInterfaceSlider : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceSwitch](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceSwitch : WKInterfaceObject {     func setTitle(_ title: String?)     func setAttributedTitle(_ attributedTitle: NSAttributedString?)     func setEnabled(_ enabled: Bool)     func setOn(_ on: Bool)     func setColor(_ color: UIColor?) } ``` | -- |
| To | ``` class WKInterfaceSwitch : WKInterfaceObject {     func setTitle(_ title: String?)     func setAttributedTitle(_ attributedTitle: NSAttributedString?)     func setEnabled(_ enabled: Bool)     func setOn(_ on: Bool)     func setColor(_ color: UIColor?)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceSwitch : CVarArg { } extension WKInterfaceSwitch : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceTable](https://developer.apple.com/documentation/watchkit/wkinterfacetable)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceTable : WKInterfaceObject {     func setRowTypes(_ rowTypes: [String])     func setNumberOfRows(_ numberOfRows: Int, withRowType rowType: String)     var numberOfRows: Int { get }     func rowControllerAtIndex(_ index: Int) -> AnyObject?     func insertRowsAtIndexes(_ rows: NSIndexSet, withRowType rowType: String)     func removeRowsAtIndexes(_ rows: NSIndexSet)     func scrollToRowAtIndex(_ index: Int) } ``` | -- |
| To | ``` class WKInterfaceTable : WKInterfaceObject {     func setRowTypes(_ rowTypes: [String])     func setNumberOfRows(_ numberOfRows: Int, withRowType rowType: String)     var numberOfRows: Int { get }     func rowController(at index: Int) -> Any?     func insertRows(at rows: IndexSet, withRowType rowType: String)     func removeRows(at rows: IndexSet)     func scrollToRow(at index: Int)     func performSegue(forRow row: Int)     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceTable : CVarArg { } extension WKInterfaceTable : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceTable.insertRows(at: IndexSet, withRowType: String)](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615834-insertrows)

|  | Declaration |
| --- | --- |
| From | ``` func insertRowsAtIndexes(_ rows: NSIndexSet, withRowType rowType: String) ``` |
| To | ``` func insertRows(at rows: IndexSet, withRowType rowType: String) ``` |

Modified [WKInterfaceTable.removeRows(at: IndexSet)](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615841-removerowsatindexes)

|  | Declaration |
| --- | --- |
| From | ``` func removeRowsAtIndexes(_ rows: NSIndexSet) ``` |
| To | ``` func removeRows(at rows: IndexSet) ``` |

Modified [WKInterfaceTable.rowController(at: Int) -> Any?](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615836-rowcontrolleratindex)

|  | Declaration |
| --- | --- |
| From | ``` func rowControllerAtIndex(_ index: Int) -> AnyObject? ``` |
| To | ``` func rowController(at index: Int) -> Any? ``` |

Modified [WKInterfaceTable.scrollToRow(at: Int)](https://developer.apple.com/documentation/watchkit/wkinterfacetable/1615837-scrolltorow)

|  | Declaration |
| --- | --- |
| From | ``` func scrollToRowAtIndex(_ index: Int) ``` |
| To | ``` func scrollToRow(at index: Int) ``` |

Modified [WKInterfaceTimer](https://developer.apple.com/documentation/watchkit/wkinterfacetimer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKInterfaceTimer : WKInterfaceObject {     func setTextColor(_ color: UIColor?)     func setDate(_ date: NSDate)     func start()     func stop() } ``` | -- |
| To | ``` class WKInterfaceTimer : WKInterfaceObject {     func setTextColor(_ color: UIColor?)     func setDate(_ date: Date)     func start()     func stop()     func setAccessibilityIdentifier(_ accessibilityIdentifier: String?)     func setAccessibilityLabel(_ accessibilityLabel: String?)     func setAccessibilityHint(_ accessibilityHint: String?)     func setAccessibilityValue(_ accessibilityValue: String?)     func setIsAccessibilityElement(_ isAccessibilityElement: Bool)     func setAccessibilityTraits(_ accessibilityTraits: UIAccessibilityTraits)     func setAccessibilityImageRegions(_ accessibilityImageRegions: [WKAccessibilityImageRegion])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKInterfaceTimer : CVarArg { } extension WKInterfaceTimer : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKInterfaceTimer.setDate(_: Date)](https://developer.apple.com/documentation/watchkit/wkinterfacetimer/1620967-setdate)

|  | Declaration |
| --- | --- |
| From | ``` func setDate(_ date: NSDate) ``` |
| To | ``` func setDate(_ date: Date) ``` |

Modified [WKMenuItemIcon [enum]](https://developer.apple.com/documentation/watchkit/wkmenuitemicon)

|  | Declaration |
| --- | --- |
| From | ``` enum WKMenuItemIcon : Int {     case Accept     case Add     case Block     case Decline     case Info     case Maybe     case More     case Mute     case Pause     case Play     case Repeat     case Resume     case Share     case Shuffle     case Speaker     case Trash } ``` |
| To | ``` enum WKMenuItemIcon : Int {     case accept     case add     case block     case decline     case info     case maybe     case more     case mute     case pause     case play     case `repeat`     case resume     case share     case shuffle     case speaker     case trash } ``` |

Modified [WKMenuItemIcon.accept](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/accept)

|  | Declaration |
| --- | --- |
| From | ``` case Accept ``` |
| To | ``` case accept ``` |

Modified [WKMenuItemIcon.add](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconadd)

|  | Declaration |
| --- | --- |
| From | ``` case Add ``` |
| To | ``` case add ``` |

Modified [WKMenuItemIcon.block](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconblock)

|  | Declaration |
| --- | --- |
| From | ``` case Block ``` |
| To | ``` case block ``` |

Modified [WKMenuItemIcon.decline](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemicondecline)

|  | Declaration |
| --- | --- |
| From | ``` case Decline ``` |
| To | ``` case decline ``` |

Modified [WKMenuItemIcon.info](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconinfo)

|  | Declaration |
| --- | --- |
| From | ``` case Info ``` |
| To | ``` case info ``` |

Modified [WKMenuItemIcon.maybe](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconmaybe)

|  | Declaration |
| --- | --- |
| From | ``` case Maybe ``` |
| To | ``` case maybe ``` |

Modified [WKMenuItemIcon.more](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconmore)

|  | Declaration |
| --- | --- |
| From | ``` case More ``` |
| To | ``` case more ``` |

Modified [WKMenuItemIcon.mute](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconmute)

|  | Declaration |
| --- | --- |
| From | ``` case Mute ``` |
| To | ``` case mute ``` |

Modified [WKMenuItemIcon.pause](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconpause)

|  | Declaration |
| --- | --- |
| From | ``` case Pause ``` |
| To | ``` case pause ``` |

Modified [WKMenuItemIcon.play](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconplay)

|  | Declaration |
| --- | --- |
| From | ``` case Play ``` |
| To | ``` case play ``` |

Modified [WKMenuItemIcon.repeat](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconrepeat)

|  | Declaration |
| --- | --- |
| From | ``` case Repeat ``` |
| To | ``` case `repeat` ``` |

Modified [WKMenuItemIcon.resume](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconresume)

|  | Declaration |
| --- | --- |
| From | ``` case Resume ``` |
| To | ``` case resume ``` |

Modified [WKMenuItemIcon.share](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/share)

|  | Declaration |
| --- | --- |
| From | ``` case Share ``` |
| To | ``` case share ``` |

Modified [WKMenuItemIcon.shuffle](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/wkmenuitemiconshuffle)

|  | Declaration |
| --- | --- |
| From | ``` case Shuffle ``` |
| To | ``` case shuffle ``` |

Modified [WKMenuItemIcon.speaker](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/speaker)

|  | Declaration |
| --- | --- |
| From | ``` case Speaker ``` |
| To | ``` case speaker ``` |

Modified [WKMenuItemIcon.trash](https://developer.apple.com/documentation/watchkit/wkmenuitemicon/trash)

|  | Declaration |
| --- | --- |
| From | ``` case Trash ``` |
| To | ``` case trash ``` |

Modified [WKPickerItem](https://developer.apple.com/documentation/watchkit/wkpickeritem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKPickerItem : NSObject, NSSecureCoding {     var title: String?     var caption: String?     @NSCopying var accessoryImage: WKImage?     @NSCopying var contentImage: WKImage? } ``` | NSSecureCoding |
| To | ``` class WKPickerItem : NSObject, NSSecureCoding {     var title: String?     var caption: String?     @NSCopying var accessoryImage: WKImage?     @NSCopying var contentImage: WKImage?     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKPickerItem : CVarArg { } extension WKPickerItem : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable, NSSecureCoding |

Modified [WKTextInputMode [enum]](https://developer.apple.com/documentation/watchkit/wktextinputmode)

|  | Declaration |
| --- | --- |
| From | ``` enum WKTextInputMode : Int {     case Plain     case AllowEmoji     case AllowAnimatedEmoji } ``` |
| To | ``` enum WKTextInputMode : Int {     case plain     case allowEmoji     case allowAnimatedEmoji } ``` |

Modified [WKTextInputMode.allowAnimatedEmoji](https://developer.apple.com/documentation/watchkit/wktextinputmode/wktextinputmodeallowanimatedemoji)

|  | Declaration |
| --- | --- |
| From | ``` case AllowAnimatedEmoji ``` |
| To | ``` case allowAnimatedEmoji ``` |

Modified [WKTextInputMode.allowEmoji](https://developer.apple.com/documentation/watchkit/wktextinputmode/wktextinputmodeallowemoji)

|  | Declaration |
| --- | --- |
| From | ``` case AllowEmoji ``` |
| To | ``` case allowEmoji ``` |

Modified [WKTextInputMode.plain](https://developer.apple.com/documentation/watchkit/wktextinputmode/plain)

|  | Declaration |
| --- | --- |
| From | ``` case Plain ``` |
| To | ``` case plain ``` |

Modified [WKUserNotificationInterfaceController](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class WKUserNotificationInterfaceController : WKInterfaceController {     init()     func didReceiveRemoteNotification(_ remoteNotification: [NSObject : AnyObject], withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void)     func didReceiveLocalNotification(_ localNotification: UILocalNotification, withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void)     func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forRemoteNotification remoteNotification: [NSObject : AnyObject], inputLanguage inputLanguage: String) -> [String]     func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forLocalNotification localNotification: UILocalNotification, inputLanguage inputLanguage: String) -> [String] } ``` | -- |
| To | ``` class WKUserNotificationInterfaceController : WKInterfaceController {     init()     func didReceive(_ notification: UNNotification, withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Swift.Void)     func suggestionsForResponseToAction(withIdentifier identifier: String, for notification: UNNotification, inputLanguage inputLanguage: String) -> [String]     func didReceiveRemoteNotification(_ remoteNotification: [AnyHashable : Any], withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Swift.Void)     func didReceive(_ localNotification: UILocalNotification, withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Swift.Void)     func suggestionsForResponseToAction(withIdentifier identifier: String, forRemoteNotification remoteNotification: [AnyHashable : Any], inputLanguage inputLanguage: String) -> [String]     func suggestionsForResponseToAction(withIdentifier identifier: String, for localNotification: UILocalNotification, inputLanguage inputLanguage: String) -> [String]     @nonobjc final class func reloadRootControllers(_ namesAndContexts: [(name: String, context: AnyObject)])     class func reloadRootControllers(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])     @nonobjc final func presentController(_ namesAndContexts: [(name: String, context: AnyObject)])     func presentController(withNamesAndContexts namesAndContexts: [(name: String, context: AnyObject)])     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)     func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool)     func performSelector(inBackground aSelector: Selector, with arg: Any?)     class func classForKeyedUnarchiver() -> AnyClass     var classForKeyedArchiver: AnyClass? { get }     func replacementObject(for archiver: NSKeyedArchiver) -> Any?     class func classFallbacksForKeyedArchiver() -> [String]     class func keyPathsForValuesAffectingValue(forKey key: String) -> Set<String>     class func automaticallyNotifiesObservers(forKey key: String) -> Bool     var observationInfo: UnsafeMutableRawPointer?     func willChangeValue(forKey key: String)     func didChangeValue(forKey key: String)     func willChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func didChange(_ changeKind: NSKeyValueChange, valuesAt indexes: IndexSet, forKey key: String)     func willChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func didChangeValue(forKey key: String, withSetMutation mutationKind: NSKeyValueSetMutationKind, using objects: Set<AnyHashable>)     func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options options: NSKeyValueObservingOptions = [], context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String, context context: UnsafeMutableRawPointer?)     func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)     func observeValue(forKeyPath keyPath: String?, of object: Any?, change change: [NSKeyValueChangeKey : Any]?, context context: UnsafeMutableRawPointer?)     class var accessInstanceVariablesDirectly: Bool { get }     func value(forKey key: String) -> Any?     func setValue(_ value: Any?, forKey key: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey inKey: String) throws     func mutableArrayValue(forKey key: String) -> NSMutableArray     func mutableOrderedSetValue(forKey key: String) -> NSMutableOrderedSet     func mutableSetValue(forKey key: String) -> NSMutableSet     func value(forKeyPath keyPath: String) -> Any?     func setValue(_ value: Any?, forKeyPath keyPath: String)     func validateValue(_ ioValue: AutoreleasingUnsafeMutablePointer<AnyObject?>, forKeyPath inKeyPath: String) throws     func mutableArrayValue(forKeyPath keyPath: String) -> NSMutableArray     func mutableOrderedSetValue(forKeyPath keyPath: String) -> NSMutableOrderedSet     func mutableSetValue(forKeyPath keyPath: String) -> NSMutableSet     func value(forUndefinedKey key: String) -> Any?     func setValue(_ value: Any?, forUndefinedKey key: String)     func setNilValueForKey(_ key: String)     func dictionaryWithValues(forKeys keys: [String]) -> [String : Any]     func setValuesForKeys(_ keyedValues: [String : Any])     func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool     func fileManager(_ fm: FileManager, willProcessPath path: String)     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoopMode])     func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)     class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)     class func cancelPreviousPerformRequests(withTarget aTarget: Any)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int, delegate delegate: Any?, didRecoverSelector didRecoverSelector: Selector?, contextInfo contextInfo: UnsafeMutableRawPointer?)     func attemptRecovery(fromError error: Error, optionIndex recoveryOptionIndex: Int) -> Bool     var autoContentAccessingProxy: Any { get }     class func version() -> Int     class func setVersion(_ aVersion: Int)     var classForCoder: AnyClass { get }     func awakeAfter(using aDecoder: NSCoder) -> Any? } extension WKUserNotificationInterfaceController : CVarArg { } extension WKUserNotificationInterfaceController : Equatable, Hashable {     var hashValue: Int { get } } ``` | CVarArg, Equatable, Hashable |

Modified [WKUserNotificationInterfaceController.didReceive(_: UILocalNotification, withCompletion: (WKUserNotificationInterfaceType) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619534-didreceive)

|  | Declaration |
| --- | --- |
| From | ``` func didReceiveLocalNotification(_ localNotification: UILocalNotification, withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void) ``` |
| To | ``` func didReceive(_ localNotification: UILocalNotification, withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Swift.Void) ``` |

Modified [WKUserNotificationInterfaceController.didReceiveRemoteNotification(_: [AnyHashable : Any], withCompletion: (WKUserNotificationInterfaceType) -> Swift.Void)](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1619568-didreceiveremotenotification)

|  | Declaration |
| --- | --- |
| From | ``` func didReceiveRemoteNotification(_ remoteNotification: [NSObject : AnyObject], withCompletion completionHandler: (WKUserNotificationInterfaceType) -> Void) ``` |
| To | ``` func didReceiveRemoteNotification(_ remoteNotification: [AnyHashable : Any], withCompletion completionHandler: @escaping (WKUserNotificationInterfaceType) -> Swift.Void) ``` |

Modified [WKUserNotificationInterfaceController.suggestionsForResponseToAction(withIdentifier: String, for: UILocalNotification, inputLanguage: String) -> [String]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1628142-suggestionsforresponsetoaction)

|  | Declaration |
| --- | --- |
| From | ``` func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forLocalNotification localNotification: UILocalNotification, inputLanguage inputLanguage: String) -> [String] ``` |
| To | ``` func suggestionsForResponseToAction(withIdentifier identifier: String, for localNotification: UILocalNotification, inputLanguage inputLanguage: String) -> [String] ``` |

Modified [WKUserNotificationInterfaceController.suggestionsForResponseToAction(withIdentifier: String, forRemoteNotification: [AnyHashable : Any], inputLanguage: String) -> [String]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller/1628132-suggestionsforresponsetoactionwi)

|  | Declaration |
| --- | --- |
| From | ``` func suggestionsForResponseToActionWithIdentifier(_ identifier: String, forRemoteNotification remoteNotification: [NSObject : AnyObject], inputLanguage inputLanguage: String) -> [String] ``` |
| To | ``` func suggestionsForResponseToAction(withIdentifier identifier: String, forRemoteNotification remoteNotification: [AnyHashable : Any], inputLanguage inputLanguage: String) -> [String] ``` |

Modified [WKUserNotificationInterfaceType [enum]](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype)

|  | Declaration |
| --- | --- |
| From | ``` enum WKUserNotificationInterfaceType : Int {     case Default     case Custom } ``` |
| To | ``` enum WKUserNotificationInterfaceType : Int {     case `default`     case custom } ``` |

Modified [WKUserNotificationInterfaceType.custom](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype/custom)

|  | Declaration |
| --- | --- |
| From | ``` case Custom ``` |
| To | ``` case custom ``` |

Modified [WKUserNotificationInterfaceType.default](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacetype/wkusernotificationinterfacetypedefault)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [WKVideoGravity [enum]](https://developer.apple.com/documentation/watchkit/wkvideogravity)

|  | Declaration |
| --- | --- |
| From | ``` enum WKVideoGravity : Int {     case ResizeAspect     case ResizeAspectFill     case Resize } ``` |
| To | ``` enum WKVideoGravity : Int {     case resizeAspect     case resizeAspectFill     case resize } ``` |

Modified [WKVideoGravity.resize](https://developer.apple.com/documentation/watchkit/wkvideogravity/resize)

|  | Declaration |
| --- | --- |
| From | ``` case Resize ``` |
| To | ``` case resize ``` |

Modified [WKVideoGravity.resizeAspect](https://developer.apple.com/documentation/watchkit/wkvideogravity/wkvideogravityresizeaspect)

|  | Declaration |
| --- | --- |
| From | ``` case ResizeAspect ``` |
| To | ``` case resizeAspect ``` |

Modified [WKVideoGravity.resizeAspectFill](https://developer.apple.com/documentation/watchkit/wkvideogravity/resizeaspectfill)

|  | Declaration |
| --- | --- |
| From | ``` case ResizeAspectFill ``` |
| To | ``` case resizeAspectFill ``` |

Modified [WKAlertActionHandler](https://developer.apple.com/documentation/watchkit/wkalertactionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias WKAlertActionHandler = () -> Void ``` |
| To | ``` typealias WKAlertActionHandler = () -> Swift.Void ``` |

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
