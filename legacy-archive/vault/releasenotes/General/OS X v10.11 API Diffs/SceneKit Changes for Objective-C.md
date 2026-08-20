---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/SceneKit.html
archived_at: '2026-07-18T02:53:12.441426Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SceneKit Changes for Objective-C

### SceneKit

#### ModelIO.h (Added)

Added [+[MDLAsset assetWithSCNScene:]](https://developer.apple.com/documentation/modelio/mdlasset/1419847-init)Added [+[MDLCamera cameraWithSCNCamera:]](https://developer.apple.com/documentation/modelio/mdlcamera/1419832-camerawithscncamera)Added [+[MDLLight lightWithSCNLight:]](https://developer.apple.com/documentation/modelio/mdllight/1419830-lightwithscnlight)Added [+[MDLMaterial materialWithSCNMaterial:]](https://developer.apple.com/documentation/modelio/mdlmaterial/1419851-init)Added [+[MDLMesh meshWithSCNGeometry:]](https://developer.apple.com/documentation/modelio/mdlmesh/1419853-init)Added [+[MDLObject objectWithSCNNode:]](https://developer.apple.com/documentation/modelio/mdlobject/1419855-objectwithscnnode)Added [+[MDLSubmesh submeshWithSCNGeometryElement:]](https://developer.apple.com/documentation/modelio/mdlsubmesh/1419837-init)Added [+[SCNCamera cameraWithMDLCamera:]](https://developer.apple.com/documentation/scenekit/scncamera/1419839-init)Added [+[SCNGeometry geometryWithMDLMesh:]](https://developer.apple.com/documentation/scenekit/scngeometry/1419845-geometrywithmdlmesh)Added [+[SCNGeometryElement geometryElementWithMDLSubmesh:]](https://developer.apple.com/documentation/scenekit/scngeometryelement/1419843-geometryelementwithmdlsubmesh)Added [+[SCNLight lightWithMDLLight:]](https://developer.apple.com/documentation/scenekit/scnlight/1419849-lightwithmdllight)Added [+[SCNMaterial materialWithMDLMaterial:]](https://developer.apple.com/documentation/scenekit/scnmaterial/1419835-materialwithmdlmaterial)Added [+[SCNNode nodeWithMDLObject:]](https://developer.apple.com/documentation/scenekit/scnnode/1419841-init)Added [+[SCNScene sceneWithMDLAsset:]](https://developer.apple.com/documentation/scenekit/scnscene/1419833-scenewithmdlasset)Added MDLAsset(SCNModelIO)Added MDLCamera(SCNModelIO)Added MDLLight(SCNModelIO)Added MDLMaterial(SCNModelIO)Added MDLMesh(SCNModelIO)Added MDLObject(SCNModelIO)Added MDLSubmesh(SCNModelIO)Added SCNCamera(SCNModelIO)Added SCNGeometry(SCNModelIO)Added SCNGeometryElement(SCNModelIO)Added SCNLight(SCNModelIO)Added SCNMaterial(SCNModelIO)Added SCNNode(SCNModelIO)Added SCNScene(SCNModelIO)

#### SceneKitTypes.h

Added #def SCN_ENABLE_METALModified [NSValue.SCNMatrix4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409684-scnmatrix4value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNMatrix4 SCNMatrix4Value ``` |
| To | ``` @property(nonatomic, readonly) SCNMatrix4 SCNMatrix4Value ``` |

Modified [NSValue.SCNVector3Value](https://developer.apple.com/documentation/foundation/nsvalue/1409669-scnvector3value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNVector3 SCNVector3Value ``` |
| To | ``` @property(nonatomic, readonly) SCNVector3 SCNVector3Value ``` |

Modified [NSValue.SCNVector4Value](https://developer.apple.com/documentation/foundation/nsvalue/1409725-scnvector4value)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNVector4 SCNVector4Value ``` |
| To | ``` @property(nonatomic, readonly) SCNVector4 SCNVector4Value ``` |

Modified [+[NSValue valueWithSCNMatrix4:]](https://developer.apple.com/documentation/foundation/nsvalue/1409680-valuewithscnmatrix4)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithSCNMatrix4:(SCNMatrix4)v ``` |
| To | ``` + (NSValue * _Nonnull)valueWithSCNMatrix4:(SCNMatrix4)v ``` |

Modified [+[NSValue valueWithSCNVector3:]](https://developer.apple.com/documentation/foundation/nsvalue/1409671-valuewithscnvector3)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithSCNVector3:(SCNVector3)v ``` |
| To | ``` + (NSValue * _Nonnull)valueWithSCNVector3:(SCNVector3)v ``` |

Modified [+[NSValue valueWithSCNVector4:]](https://developer.apple.com/documentation/foundation/nsvalue/1409688-valuewithscnvector4)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithSCNVector4:(SCNVector4)v ``` |
| To | ``` + (NSValue * _Nonnull)valueWithSCNVector4:(SCNVector4)v ``` |

#### SCNAction.h

Removed [-[SCNActionable hasActions]](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Removed SCNAction(SCNActions)Added [+[SCNAction hide]](https://developer.apple.com/documentation/scenekit/scnaction/1523487-hide)Added [+[SCNAction playAudioSource:waitForCompletion:]](https://developer.apple.com/documentation/scenekit/scnaction/1523651-playaudio)Added [+[SCNAction unhide]](https://developer.apple.com/documentation/scenekit/scnaction/1524205-unhide)Added [SCNActionable.actionKeys](https://developer.apple.com/documentation/scenekit/scnactionable/1523036-actionkeys)Added [SCNActionable.hasActions](https://developer.apple.com/documentation/scenekit/scnactionable/1523794-hasactions)Modified [+[SCNAction customActionWithDuration:actionBlock:]](https://developer.apple.com/documentation/scenekit/scnaction/1523692-customactionwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)customActionWithDuration:(NSTimeInterval)seconds actionBlock:(void (^)(SCNNode *node, CGFloat elapsedTime))block ``` |
| To | ``` + (SCNAction * _Nonnull)customActionWithDuration:(NSTimeInterval)seconds actionBlock:(void (^ _Nonnull)(SCNNode * _Nonnull node, CGFloat elapsedTime))block ``` |

Modified [+[SCNAction fadeInWithDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522777-fadein)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)fadeInWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)fadeInWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction fadeOpacityBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523595-fadeopacityby)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)fadeOpacityBy:(CGFloat)factor duration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)fadeOpacityBy:(CGFloat)factor duration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction fadeOpacityTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523875-fadeopacityto)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)fadeOpacityTo:(CGFloat)opacity duration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)fadeOpacityTo:(CGFloat)opacity duration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction fadeOutWithDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523922-fadeoutwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)fadeOutWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)fadeOutWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction group:]](https://developer.apple.com/documentation/scenekit/scnaction/1522779-group)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)group:(NSArray *)actions ``` |
| To | ``` + (SCNAction * _Nonnull)group:(NSArray<SCNAction *> * _Nonnull)actions ``` |

Modified [+[SCNAction javaScriptActionWithScript:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523984-javascriptaction)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)javaScriptActionWithScript:(NSString *)script duration:(NSTimeInterval)seconds ``` |
| To | ``` + (SCNAction * _Nonnull)javaScriptActionWithScript:(NSString * _Nonnull)script duration:(NSTimeInterval)seconds ``` |

Modified [+[SCNAction moveBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522605-move)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)moveBy:(SCNVector3)delta duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)moveBy:(SCNVector3)delta duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction moveByX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523238-moveby)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)moveByX:(CGFloat)deltaX y:(CGFloat)deltaY z:(CGFloat)deltaZ duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)moveByX:(CGFloat)deltaX y:(CGFloat)deltaY z:(CGFloat)deltaZ duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction moveTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1522826-move)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)moveTo:(SCNVector3)location duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)moveTo:(SCNVector3)location duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction removeFromParentNode]](https://developer.apple.com/documentation/scenekit/scnaction/1522966-removefromparentnode)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)removeFromParentNode ``` |
| To | ``` + (SCNAction * _Nonnull)removeFromParentNode ``` |

Modified [+[SCNAction repeatAction:count:]](https://developer.apple.com/documentation/scenekit/scnaction/1522764-repeat)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)repeatAction:(SCNAction *)action count:(NSUInteger)count ``` |
| To | ``` + (SCNAction * _Nonnull)repeatAction:(SCNAction * _Nonnull)action count:(NSUInteger)count ``` |

Modified [+[SCNAction repeatActionForever:]](https://developer.apple.com/documentation/scenekit/scnaction/1522908-repeatactionforever)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)repeatActionForever:(SCNAction *)action ``` |
| To | ``` + (SCNAction * _Nonnull)repeatActionForever:(SCNAction * _Nonnull)action ``` |

Modified [-[SCNAction reversedAction]](https://developer.apple.com/documentation/scenekit/scnaction/1522815-reversed)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNAction *)reversedAction ``` |
| To | ``` - (SCNAction * _Nonnull)reversedAction ``` |

Modified [+[SCNAction rotateByAngle:aroundAxis:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523805-rotate)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)rotateByAngle:(CGFloat)angle aroundAxis:(SCNVector3)axis duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)rotateByAngle:(CGFloat)angle aroundAxis:(SCNVector3)axis duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction rotateByX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523522-rotatebyx)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)rotateByX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)rotateByX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction rotateToAxisAngle:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1524191-rotatetoaxisangle)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)rotateToAxisAngle:(SCNVector4)axisAngle duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)rotateToAxisAngle:(SCNVector4)axisAngle duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction rotateToX:y:z:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1524044-rotateto)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)rotateToX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration ``` |
| To | ``` + (SCNAction * _Nonnull)rotateToX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration ``` |

Modified [+[SCNAction rotateToX:y:z:duration:shortestUnitArc:]](https://developer.apple.com/documentation/scenekit/scnaction/1522808-rotatetox)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)rotateToX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration shortestUnitArc:(BOOL)shortestUnitArc ``` |
| To | ``` + (SCNAction * _Nonnull)rotateToX:(CGFloat)xAngle y:(CGFloat)yAngle z:(CGFloat)zAngle duration:(NSTimeInterval)duration shortestUnitArc:(BOOL)shortestUnitArc ``` |

Modified [+[SCNAction runBlock:]](https://developer.apple.com/documentation/scenekit/scnaction/1523637-runblock)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)runBlock:(void (^)(SCNNode *node))block ``` |
| To | ``` + (SCNAction * _Nonnull)runBlock:(void (^ _Nonnull)(SCNNode * _Nonnull node))block ``` |

Modified [+[SCNAction runBlock:queue:]](https://developer.apple.com/documentation/scenekit/scnaction/1522875-run)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)runBlock:(void (^)(SCNNode *node))block queue:(dispatch_queue_t)queue ``` |
| To | ``` + (SCNAction * _Nonnull)runBlock:(void (^ _Nonnull)(SCNNode * _Nonnull node))block queue:(dispatch_queue_t _Nonnull)queue ``` |

Modified [+[SCNAction scaleBy:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523129-scaleby)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)scaleBy:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)scaleBy:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction scaleTo:duration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523322-scale)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)scaleTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)scaleTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction sequence:]](https://developer.apple.com/documentation/scenekit/scnaction/1522793-sequence)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)sequence:(NSArray *)actions ``` |
| To | ``` + (SCNAction * _Nonnull)sequence:(NSArray<SCNAction *> * _Nonnull)actions ``` |

Modified [SCNAction.timingFunction](https://developer.apple.com/documentation/scenekit/scnaction/1524130-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) SCNActionTimingFunction timingFunction ``` |
| To | ``` @property(nonatomic, nullable) SCNActionTimingFunction timingFunction ``` |

Modified [+[SCNAction waitForDuration:]](https://developer.apple.com/documentation/scenekit/scnaction/1523915-wait)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)waitForDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SCNAction * _Nonnull)waitForDuration:(NSTimeInterval)sec ``` |

Modified [+[SCNAction waitForDuration:withRange:]](https://developer.apple.com/documentation/scenekit/scnaction/1523086-wait)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNAction *)waitForDuration:(NSTimeInterval)sec withRange:(NSTimeInterval)durationRange ``` |
| To | ``` + (SCNAction * _Nonnull)waitForDuration:(NSTimeInterval)sec withRange:(NSTimeInterval)durationRange ``` |

Modified [-[SCNActionable actionForKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523287-action)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNAction *)actionForKey:(NSString *)key ``` |
| To | ``` - (SCNAction * _Nullable)actionForKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNActionable removeActionForKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523617-removeactionforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeActionForKey:(NSString *)key ``` |
| To | ``` - (void)removeActionForKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNActionable runAction:]](https://developer.apple.com/documentation/scenekit/scnactionable/1523164-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SCNAction *)action ``` |
| To | ``` - (void)runAction:(SCNAction * _Nonnull)action ``` |

Modified [-[SCNActionable runAction:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnactionable/1524219-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SCNAction *)action completionHandler:(void (^)(void))block ``` |
| To | ``` - (void)runAction:(SCNAction * _Nonnull)action completionHandler:(void (^ _Nullable)(void))block ``` |

Modified [-[SCNActionable runAction:forKey:]](https://developer.apple.com/documentation/scenekit/scnactionable/1524222-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SCNAction *)action forKey:(NSString *)key ``` |
| To | ``` - (void)runAction:(SCNAction * _Nonnull)action forKey:(NSString * _Nullable)key ``` |

Modified [-[SCNActionable runAction:forKey:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnactionable/1522791-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SCNAction *)action forKey:(NSString *)key completionHandler:(void (^)(void))block ``` |
| To | ``` - (void)runAction:(SCNAction * _Nonnull)action forKey:(NSString * _Nullable)key completionHandler:(void (^ _Nullable)(void))block ``` |

#### SCNAnimation.h

Removed [-[SCNAnimatable animationKeys]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523610-animationkeys)Added [SCNAnimatable.animationKeys](https://developer.apple.com/documentation/scenekit/scnanimatable/1523610-animationkeys)Modified [CAAnimation.animationEvents](https://developer.apple.com/documentation/quartzcore/caanimation/1523940-animationevents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSArray *animationEvents ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNAnimationEvent *> *animationEvents ``` |

Modified [-[SCNAnimatable addAnimation:forKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523386-addanimation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAnimation:(CAAnimation *)animation forKey:(NSString *)key ``` |
| To | ``` - (void)addAnimation:(CAAnimation * _Nonnull)animation forKey:(NSString * _Nullable)key ``` |

Modified [-[SCNAnimatable animationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1524020-animation)

|  | Declaration |
| --- | --- |
| From | ``` - (CAAnimation *)animationForKey:(NSString *)key ``` |
| To | ``` - (CAAnimation * _Nullable)animationForKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNAnimatable isAnimationForKeyPaused:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523703-isanimationforkeypaused)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isAnimationForKeyPaused:(NSString *)key ``` |
| To | ``` - (BOOL)isAnimationForKeyPaused:(NSString * _Nonnull)key ``` |

Modified [-[SCNAnimatable pauseAnimationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523592-pauseanimation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pauseAnimationForKey:(NSString *)key ``` |
| To | ``` - (void)pauseAnimationForKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNAnimatable removeAnimationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1522880-removeanimationforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnimationForKey:(NSString *)key ``` |
| To | ``` - (void)removeAnimationForKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNAnimatable removeAnimationForKey:fadeOutDuration:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1522841-removeanimation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnimationForKey:(NSString *)key fadeOutDuration:(CGFloat)duration ``` |
| To | ``` - (void)removeAnimationForKey:(NSString * _Nonnull)key fadeOutDuration:(CGFloat)duration ``` |

Modified [-[SCNAnimatable resumeAnimationForKey:]](https://developer.apple.com/documentation/scenekit/scnanimatable/1523332-resumeanimationforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resumeAnimationForKey:(NSString *)key ``` |
| To | ``` - (void)resumeAnimationForKey:(NSString * _Nonnull)key ``` |

Modified [+[SCNAnimationEvent animationEventWithKeyTime:block:]](https://developer.apple.com/documentation/scenekit/scnanimationevent/1524004-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)animationEventWithKeyTime:(CGFloat)time block:(SCNAnimationEventBlock)eventBlock ``` |
| To | ``` + (instancetype _Nonnull)animationEventWithKeyTime:(CGFloat)time block:(SCNAnimationEventBlock _Nonnull)eventBlock ``` |

#### SCNAudioSource.h (Added)

Added [SCNAudioPlayer](https://developer.apple.com/documentation/scenekit/scnaudioplayer)Added [SCNAudioPlayer.audioNode](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522747-audionode)Added [+[SCNAudioPlayer audioPlayerWithAVAudioNode:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1533927-audioplayerwithavaudionode)Added [+[SCNAudioPlayer audioPlayerWithSource:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1533919-audioplayerwithsource)Added [SCNAudioPlayer.audioSource](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523059-audiosource)Added [SCNAudioPlayer.didFinishPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522818-didfinishplayback)Added [-[SCNAudioPlayer initWithAVAudioNode:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1523010-init)Added [-[SCNAudioPlayer initWithSource:]](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1522736-init)Added [SCNAudioPlayer.willStartPlayback](https://developer.apple.com/documentation/scenekit/scnaudioplayer/1524115-willstartplayback)Added [SCNAudioSource](https://developer.apple.com/documentation/scenekit/scnaudiosource)Added [+[SCNAudioSource audioSourceNamed:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524138-audiosourcenamed)Added [-[SCNAudioSource initWithFileNamed:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524225-init)Added [-[SCNAudioSource initWithURL:]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523264-initwithurl)Added [-[SCNAudioSource load]](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523399-load)Added [SCNAudioSource.loops](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524183-loops)Added [SCNAudioSource.positional](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524185-positional)Added [SCNAudioSource.rate](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524189-rate)Added [SCNAudioSource.reverbBlend](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523450-reverbblend)Added [SCNAudioSource.shouldStream](https://developer.apple.com/documentation/scenekit/scnaudiosource/1523475-shouldstream)Added [SCNAudioSource.volume](https://developer.apple.com/documentation/scenekit/scnaudiosource/1524106-volume)Added [-[SCNNode addAudioPlayer:]](https://developer.apple.com/documentation/scenekit/scnnode/1523464-addaudioplayer)Added [SCNNode.audioPlayers](https://developer.apple.com/documentation/scenekit/scnnode/1523244-audioplayers)Added [-[SCNNode removeAllAudioPlayers]](https://developer.apple.com/documentation/scenekit/scnnode/1523570-removeallaudioplayers)Added [-[SCNNode removeAudioPlayer:]](https://developer.apple.com/documentation/scenekit/scnnode/1522767-removeaudioplayer)Added SCNNode(SCNAudioSupport)

#### SCNBoundingVolume.h

Modified [-[SCNBoundingVolume getBoundingBoxMin:max:]](https://developer.apple.com/documentation/scenekit/scnboundingvolume/1522872-getboundingboxmin)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getBoundingBoxMin:(SCNVector3 *)min max:(SCNVector3 *)max ``` |
| To | ``` - (BOOL)getBoundingBoxMin:(SCNVector3 * _Nullable)min max:(SCNVector3 * _Nullable)max ``` |

Modified [-[SCNBoundingVolume getBoundingSphereCenter:radius:]](https://developer.apple.com/documentation/scenekit/scnboundingvolume/1523886-getboundingspherecenter)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)getBoundingSphereCenter:(SCNVector3 *)center radius:(CGFloat *)radius ``` |
| To | ``` - (BOOL)getBoundingSphereCenter:(SCNVector3 * _Nullable)center radius:(CGFloat * _Nullable)radius ``` |

Modified [-[SCNBoundingVolume setBoundingBoxMin:max:]](https://developer.apple.com/documentation/scenekit/scnboundingvolume/1522866-setboundingboxmin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setBoundingBoxMin:(SCNVector3 *)min max:(SCNVector3 *)max ``` |
| To | ``` - (void)setBoundingBoxMin:(SCNVector3 * _Nullable)min max:(SCNVector3 * _Nullable)max ``` |

#### SCNCamera.h

Modified [+[SCNCamera camera]](https://developer.apple.com/documentation/scenekit/scncamera/1436602-camera)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)camera ``` |
| To | ``` + (instancetype _Nonnull)camera ``` |

Modified [SCNCamera.name](https://developer.apple.com/documentation/scenekit/scncamera/1436623-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

#### SCNConstraint.h

Added [SCNBillboardConstraint](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint)Added [+[SCNBillboardConstraint billboardConstraint]](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/1468673-billboardconstraint)Added [SCNBillboardConstraint.freeAxes](https://developer.apple.com/documentation/scenekit/scnbillboardconstraint/1468685-freeaxes)Added [-[SCNIKConstraint initWithChainRootNode:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468694-init)Added [SCNBillboardAxis](https://developer.apple.com/documentation/scenekit/scnbillboardaxis)Added [SCNBillboardAxisAll](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/1468666-all)Added [SCNBillboardAxisX](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisx)Added [SCNBillboardAxisY](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisy)Added [SCNBillboardAxisZ](https://developer.apple.com/documentation/scenekit/scnbillboardaxis/scnbillboardaxisz)Modified [SCNIKConstraint.chainRootNode](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468690-chainrootnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *chainRootNode ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *chainRootNode ``` |

Modified [+[SCNIKConstraint inverseKinematicsConstraintWithChainRootNode:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468653-inversekinematicsconstraintwithc)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)inverseKinematicsConstraintWithChainRootNode:(SCNNode *)chainRootNode ``` |
| To | ``` + (instancetype _Nonnull)inverseKinematicsConstraintWithChainRootNode:(SCNNode * _Nonnull)chainRootNode ``` |

Modified [-[SCNIKConstraint maxAllowedRotationAngleForJoint:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468681-maxallowedrotationangle)

|  | Declaration |
| --- | --- |
| From | ``` - (CGFloat)maxAllowedRotationAngleForJoint:(SCNNode *)node ``` |
| To | ``` - (CGFloat)maxAllowedRotationAngleForJoint:(SCNNode * _Nonnull)node ``` |

Modified [-[SCNIKConstraint setMaxAllowedRotationAngle:forJoint:]](https://developer.apple.com/documentation/scenekit/scnikconstraint/1468649-setmaxallowedrotationangle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMaxAllowedRotationAngle:(CGFloat)angle forJoint:(SCNNode *)node ``` |
| To | ``` - (void)setMaxAllowedRotationAngle:(CGFloat)angle forJoint:(SCNNode * _Nonnull)node ``` |

Modified [+[SCNLookAtConstraint lookAtConstraintWithTarget:]](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468683-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)lookAtConstraintWithTarget:(SCNNode *)target ``` |
| To | ``` + (instancetype _Nonnull)lookAtConstraintWithTarget:(SCNNode * _Nonnull)target ``` |

Modified [SCNLookAtConstraint.target](https://developer.apple.com/documentation/scenekit/scnlookatconstraint/1468677-target)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *target ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *target ``` |

Modified [+[SCNTransformConstraint transformConstraintInWorldSpace:withBlock:]](https://developer.apple.com/documentation/scenekit/scntransformconstraint/1468679-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)transformConstraintInWorldSpace:(BOOL)world withBlock:(SCNMatrix4 (^)(SCNNode *node, SCNMatrix4 transform))block ``` |
| To | ``` + (instancetype _Nonnull)transformConstraintInWorldSpace:(BOOL)world withBlock:(SCNMatrix4 (^ _Nonnull)(SCNNode * _Nonnull node, SCNMatrix4 transform))block ``` |

#### SCNGeometry.h

Added [SCNGeometry.geometryElements](https://developer.apple.com/documentation/scenekit/scngeometry/1523046-geometryelements)Added [SCNGeometry.geometrySources](https://developer.apple.com/documentation/scenekit/scngeometry/1523662-sources)Added [+[SCNGeometrySource geometrySourceWithBuffer:vertexFormat:semantic:vertexCount:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522873-init)Modified [SCNGeometry.edgeCreasesElement](https://developer.apple.com/documentation/scenekit/scngeometry/1523246-edgecreaseselement)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNGeometryElement *edgeCreasesElement ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNGeometryElement *edgeCreasesElement ``` |

Modified [SCNGeometry.edgeCreasesSource](https://developer.apple.com/documentation/scenekit/scngeometry/1523479-edgecreasessource)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNGeometrySource *edgeCreasesSource ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNGeometrySource *edgeCreasesSource ``` |

Modified [SCNGeometry.firstMaterial](https://developer.apple.com/documentation/scenekit/scngeometry/1523485-firstmaterial)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNMaterial *firstMaterial ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNMaterial *firstMaterial ``` |

Modified [+[SCNGeometry geometry]](https://developer.apple.com/documentation/scenekit/scngeometry/1585530-geometry)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometry ``` |
| To | ``` + (instancetype _Nonnull)geometry ``` |

Modified [-[SCNGeometry geometryElementAtIndex:]](https://developer.apple.com/documentation/scenekit/scngeometry/1523266-element)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNGeometryElement *)geometryElementAtIndex:(NSInteger)elementIndex ``` |
| To | ``` - (SCNGeometryElement * _Nonnull)geometryElementAtIndex:(NSInteger)elementIndex ``` |

Modified [-[SCNGeometry geometrySourcesForSemantic:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522926-geometrysourcesforsemantic)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)geometrySourcesForSemantic:(NSString *)semantic ``` |
| To | ``` - (NSArray<SCNGeometrySource *> * _Nonnull)geometrySourcesForSemantic:(NSString * _Nonnull)semantic ``` |

Modified [+[SCNGeometry geometryWithSources:elements:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522803-geometrywithsources)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometryWithSources:(NSArray *)sources elements:(NSArray *)elements ``` |
| To | ``` + (instancetype _Nonnull)geometryWithSources:(NSArray<SCNGeometrySource *> * _Nonnull)sources elements:(NSArray<SCNGeometryElement *> * _Nonnull)elements ``` |

Modified [-[SCNGeometry insertMaterial:atIndex:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522876-insertmaterial)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertMaterial:(SCNMaterial *)material atIndex:(NSUInteger)index ``` |
| To | ``` - (void)insertMaterial:(SCNMaterial * _Nonnull)material atIndex:(NSUInteger)index ``` |

Modified [SCNGeometry.levelsOfDetail](https://developer.apple.com/documentation/scenekit/scngeometry/1523745-levelsofdetail)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *levelsOfDetail ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNLevelOfDetail *> *levelsOfDetail ``` |

Modified [SCNGeometry.materials](https://developer.apple.com/documentation/scenekit/scngeometry/1523472-materials)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *materials ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<SCNMaterial *> *materials ``` |

Modified [-[SCNGeometry materialWithName:]](https://developer.apple.com/documentation/scenekit/scngeometry/1523789-material)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNMaterial *)materialWithName:(NSString *)name ``` |
| To | ``` - (SCNMaterial * _Nullable)materialWithName:(NSString * _Nonnull)name ``` |

Modified [SCNGeometry.name](https://developer.apple.com/documentation/scenekit/scngeometry/1522953-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [-[SCNGeometry replaceMaterialAtIndex:withMaterial:]](https://developer.apple.com/documentation/scenekit/scngeometry/1522714-replacematerialatindex)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceMaterialAtIndex:(NSUInteger)index withMaterial:(SCNMaterial *)material ``` |
| To | ``` - (void)replaceMaterialAtIndex:(NSUInteger)index withMaterial:(SCNMaterial * _Nonnull)material ``` |

Modified [SCNGeometryElement.data](https://developer.apple.com/documentation/scenekit/scngeometryelement/1523367-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *data ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSData *data ``` |

Modified [+[SCNGeometryElement geometryElementWithData:primitiveType:primitiveCount:bytesPerIndex:]](https://developer.apple.com/documentation/scenekit/scngeometryelement/1522615-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometryElementWithData:(NSData *)data primitiveType:(SCNGeometryPrimitiveType)primitiveType primitiveCount:(NSInteger)primitiveCount bytesPerIndex:(NSInteger)bytesPerIndex ``` |
| To | ``` + (instancetype _Nonnull)geometryElementWithData:(NSData * _Nullable)data primitiveType:(SCNGeometryPrimitiveType)primitiveType primitiveCount:(NSInteger)primitiveCount bytesPerIndex:(NSInteger)bytesPerIndex ``` |

Modified [SCNGeometrySource.data](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522881-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSData *data ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSData *data ``` |

Modified [+[SCNGeometrySource geometrySourceWithData:semantic:vectorCount:floatComponents:componentsPerVector:bytesPerComponent:dataOffset:dataStride:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523320-geometrysourcewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithData:(NSData *)data semantic:(NSString *)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |
| To | ``` + (instancetype _Nonnull)geometrySourceWithData:(NSData * _Nonnull)data semantic:(NSString * _Nonnull)semantic vectorCount:(NSInteger)vectorCount floatComponents:(BOOL)floatComponents componentsPerVector:(NSInteger)componentsPerVector bytesPerComponent:(NSInteger)bytesPerComponent dataOffset:(NSInteger)offset dataStride:(NSInteger)stride ``` |

Modified [+[SCNGeometrySource geometrySourceWithNormals:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522882-geometrysourcewithnormals)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithNormals:(const SCNVector3 *)normals count:(NSInteger)count ``` |
| To | ``` + (instancetype _Nonnull)geometrySourceWithNormals:(const SCNVector3 * _Nonnull)normals count:(NSInteger)count ``` |

Modified [+[SCNGeometrySource geometrySourceWithTextureCoordinates:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1522718-geometrysourcewithtexturecoordin)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithTextureCoordinates:(const CGPoint *)texcoord count:(NSInteger)count ``` |
| To | ``` + (instancetype _Nonnull)geometrySourceWithTextureCoordinates:(const CGPoint * _Nonnull)texcoord count:(NSInteger)count ``` |

Modified [+[SCNGeometrySource geometrySourceWithVertices:count:]](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523882-geometrysourcewithvertices)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)geometrySourceWithVertices:(const SCNVector3 *)vertices count:(NSInteger)count ``` |
| To | ``` + (instancetype _Nonnull)geometrySourceWithVertices:(const SCNVector3 * _Nonnull)vertices count:(NSInteger)count ``` |

Modified [SCNGeometrySource.semantic](https://developer.apple.com/documentation/scenekit/scngeometrysource/1523071-semantic)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSString *semantic ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *semantic ``` |

#### SCNJavascript.h

Modified [SCNExportJavaScriptModule()](https://developer.apple.com/documentation/scenekit/1524164-scnexportjavascriptmodule)

|  | Declaration |
| --- | --- |
| From | ``` void SCNExportJavaScriptModule (     JSContext *context ); ``` |
| To | ``` void SCNExportJavaScriptModule (     JSContext * _Nonnull context ); ``` |

#### SCNLayer.h

Modified [SCNLayer.scene](https://developer.apple.com/documentation/scenekit/scnlayer/1393188-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNScene *scene ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNScene *scene ``` |

#### SCNLevelOfDetail.h

Modified [SCNLevelOfDetail.geometry](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1522819-geometry)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNGeometry *geometry ``` |
| To | ``` @property(readonly, nullable) SCNGeometry *geometry ``` |

Modified [+[SCNLevelOfDetail levelOfDetailWithGeometry:screenSpaceRadius:]](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1523557-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)levelOfDetailWithGeometry:(SCNGeometry *)geometry screenSpaceRadius:(CGFloat)radius ``` |
| To | ``` + (instancetype _Nonnull)levelOfDetailWithGeometry:(SCNGeometry * _Nullable)geometry screenSpaceRadius:(CGFloat)radius ``` |

Modified [+[SCNLevelOfDetail levelOfDetailWithGeometry:worldSpaceDistance:]](https://developer.apple.com/documentation/scenekit/scnlevelofdetail/1522802-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)levelOfDetailWithGeometry:(SCNGeometry *)geometry worldSpaceDistance:(CGFloat)distance ``` |
| To | ``` + (instancetype _Nonnull)levelOfDetailWithGeometry:(SCNGeometry * _Nullable)geometry worldSpaceDistance:(CGFloat)distance ``` |

#### SCNLight.h

Modified [-[SCNLight attributeForKey:]](https://developer.apple.com/documentation/scenekit/scnlight/1523345-attribute)

|  | Declaration |
| --- | --- |
| From | ``` - (id)attributeForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)attributeForKey:(NSString * _Nonnull)key ``` |

Modified [SCNLight.color](https://developer.apple.com/documentation/scenekit/scnlight/1523627-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id color ``` |
| To | ``` @property(nonatomic, retain, nonnull) id color ``` |

Modified [SCNLight.gobo](https://developer.apple.com/documentation/scenekit/scnlight/1523524-gobo)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *gobo ``` |
| To | ``` @property(nonatomic, readonly, nullable) SCNMaterialProperty *gobo ``` |

Modified [+[SCNLight light]](https://developer.apple.com/documentation/scenekit/scnlight/1542979-light)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)light ``` |
| To | ``` + (instancetype _Nonnull)light ``` |

Modified [SCNLight.name](https://developer.apple.com/documentation/scenekit/scnlight/1522839-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [-[SCNLight setAttribute:forKey:]](https://developer.apple.com/documentation/scenekit/scnlight/1523148-setattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setAttribute:(id)attribute forKey:(NSString *)key ``` |
| To | ``` - (void)setAttribute:(id _Nullable)attribute forKey:(NSString * _Nonnull)key ``` |

Modified [SCNLight.shadowColor](https://developer.apple.com/documentation/scenekit/scnlight/1522864-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id shadowColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) id shadowColor ``` |

Modified [SCNLight.type](https://developer.apple.com/documentation/scenekit/scnlight/1522919-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *type ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *type ``` |

#### SCNMaterial.h

Added [SCNMaterial.ambientOcclusion](https://developer.apple.com/documentation/scenekit/scnmaterial/1462579-ambientocclusion)Added [SCNMaterial.blendMode](https://developer.apple.com/documentation/scenekit/scnmaterial/1462585-blendmode)Added [SCNMaterial.selfIllumination](https://developer.apple.com/documentation/scenekit/scnmaterial/1462524-selfillumination)Added [SCNBlendMode](https://developer.apple.com/documentation/scenekit/scnblendmode)Added [SCNBlendModeAdd](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodeadd)Added [SCNBlendModeAlpha](https://developer.apple.com/documentation/scenekit/scnblendmode/alpha)Added [SCNBlendModeMultiply](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodemultiply)Added [SCNBlendModeReplace](https://developer.apple.com/documentation/scenekit/scnblendmode/replace)Added [SCNBlendModeScreen](https://developer.apple.com/documentation/scenekit/scnblendmode/screen)Added [SCNBlendModeSubtract](https://developer.apple.com/documentation/scenekit/scnblendmode/scnblendmodesubtract)Modified [SCNMaterial.ambient](https://developer.apple.com/documentation/scenekit/scnmaterial/1462558-ambient)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *ambient ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *ambient ``` |

Modified [SCNMaterial.diffuse](https://developer.apple.com/documentation/scenekit/scnmaterial/1462589-diffuse)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *diffuse ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *diffuse ``` |

Modified [SCNMaterial.emission](https://developer.apple.com/documentation/scenekit/scnmaterial/1462527-emission)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *emission ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *emission ``` |

Modified [SCNMaterial.lightingModelName](https://developer.apple.com/documentation/scenekit/scnmaterial/1462518-lightingmodelname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *lightingModelName ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *lightingModelName ``` |

Modified [+[SCNMaterial material]](https://developer.apple.com/documentation/scenekit/scnmaterial/1462552-material)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)material ``` |
| To | ``` + (instancetype _Nonnull)material ``` |

Modified [SCNMaterial.multiply](https://developer.apple.com/documentation/scenekit/scnmaterial/1462575-multiply)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *multiply ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *multiply ``` |

Modified [SCNMaterial.name](https://developer.apple.com/documentation/scenekit/scnmaterial/1462525-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [SCNMaterial.normal](https://developer.apple.com/documentation/scenekit/scnmaterial/1462542-normal)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *normal ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *normal ``` |

Modified [SCNMaterial.reflective](https://developer.apple.com/documentation/scenekit/scnmaterial/1462520-reflective)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *reflective ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *reflective ``` |

Modified [SCNMaterial.specular](https://developer.apple.com/documentation/scenekit/scnmaterial/1462516-specular)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *specular ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *specular ``` |

Modified [SCNMaterial.transparent](https://developer.apple.com/documentation/scenekit/scnmaterial/1462583-transparent)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *transparent ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *transparent ``` |

#### SCNMaterialProperty.h

Removed [SCNClamp](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnclamp)Removed [SCNClampToBorder](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnclamptoborder)Removed [SCNLinearFiltering](https://developer.apple.com/documentation/scenekit/scnfiltermode/scnlinearfiltering)Removed [SCNMirror](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnmirror)Removed [SCNNearestFiltering](https://developer.apple.com/documentation/scenekit/scnfiltermode/scnnearestfiltering)Removed [SCNNoFiltering](https://developer.apple.com/documentation/scenekit/scnfiltermode/scnnofiltering)Removed [SCNRepeat](https://developer.apple.com/documentation/scenekit/scnwrapmode/scnrepeat)Modified [SCNMaterialProperty.borderColor](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395376-bordercolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id borderColor ``` |
| To | ``` @property(nonatomic, retain, nullable) id borderColor ``` |

Modified [SCNMaterialProperty.contents](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395372-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id contents ``` |
| To | ``` @property(nonatomic, retain, nullable) id contents ``` |

Modified [+[SCNMaterialProperty materialPropertyWithContents:]](https://developer.apple.com/documentation/scenekit/scnmaterialproperty/1395386-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)materialPropertyWithContents:(id)contents ``` |
| To | ``` + (instancetype _Nonnull)materialPropertyWithContents:(id _Nonnull)contents ``` |

#### SCNMorpher.h

Modified [SCNMorpher.targets](https://developer.apple.com/documentation/scenekit/scnmorpher/1523572-targets)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *targets ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSArray<SCNGeometry *> *targets ``` |

#### SCNNode.h

Modified [-[SCNNode addChildNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407974-addchildnode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addChildNode:(SCNNode *)child ``` |
| To | ``` - (void)addChildNode:(SCNNode * _Nonnull)child ``` |

Modified [SCNNode.camera](https://developer.apple.com/documentation/scenekit/scnnode/1407976-camera)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNCamera *camera ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNCamera *camera ``` |

Modified [SCNNode.childNodes](https://developer.apple.com/documentation/scenekit/scnnode/1407984-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *childNodes ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNNode *> *childNodes ``` |

Modified [-[SCNNode childNodesPassingTest:]](https://developer.apple.com/documentation/scenekit/scnnode/1407982-childnodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)childNodesPassingTest:(BOOL (^)(SCNNode *child, BOOL *stop))predicate ``` |
| To | ``` - (NSArray<SCNNode *> * _Nonnull)childNodesPassingTest:(BOOL (^ _Nonnull)(SCNNode * _Nonnull child, BOOL * _Nonnull stop))predicate ``` |

Modified [-[SCNNode childNodeWithName:recursively:]](https://developer.apple.com/documentation/scenekit/scnnode/1407951-childnodewithname)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNNode *)childNodeWithName:(NSString *)name recursively:(BOOL)recursively ``` |
| To | ``` - (SCNNode * _Nullable)childNodeWithName:(NSString * _Nonnull)name recursively:(BOOL)recursively ``` |

Modified [-[SCNNode clone]](https://developer.apple.com/documentation/scenekit/scnnode/1408046-clone)

|  | Declaration |
| --- | --- |
| From | ``` - (id)clone ``` |
| To | ``` - (instancetype _Nonnull)clone ``` |

Modified [SCNNode.constraints](https://developer.apple.com/documentation/scenekit/scnnode/1408016-constraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *constraints ``` |
| To | ``` @property(copy, nullable) NSArray<SCNConstraint *> *constraints ``` |

Modified [-[SCNNode convertPosition:fromNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1408018-convertposition)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNVector3)convertPosition:(SCNVector3)position fromNode:(SCNNode *)node ``` |
| To | ``` - (SCNVector3)convertPosition:(SCNVector3)position fromNode:(SCNNode * _Nullable)node ``` |

Modified [-[SCNNode convertPosition:toNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407990-convertposition)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNVector3)convertPosition:(SCNVector3)position toNode:(SCNNode *)node ``` |
| To | ``` - (SCNVector3)convertPosition:(SCNVector3)position toNode:(SCNNode * _Nullable)node ``` |

Modified [-[SCNNode convertTransform:fromNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407996-converttransform)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform fromNode:(SCNNode *)node ``` |
| To | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform fromNode:(SCNNode * _Nullable)node ``` |

Modified [-[SCNNode convertTransform:toNode:]](https://developer.apple.com/documentation/scenekit/scnnode/1407986-converttransform)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform toNode:(SCNNode *)node ``` |
| To | ``` - (SCNMatrix4)convertTransform:(SCNMatrix4)transform toNode:(SCNNode * _Nullable)node ``` |

Modified [-[SCNNode enumerateChildNodesUsingBlock:]](https://developer.apple.com/documentation/scenekit/scnnode/1408032-enumeratechildnodesusingblock)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateChildNodesUsingBlock:(void (^)(SCNNode *child, BOOL *stop))block ``` |
| To | ``` - (void)enumerateChildNodesUsingBlock:(void (^ _Nonnull)(SCNNode * _Nonnull child, BOOL * _Nonnull stop))block ``` |

Modified [SCNNode.filters](https://developer.apple.com/documentation/scenekit/scnnode/1407949-filters)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *filters ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<CIFilter *> *filters ``` |

Modified [-[SCNNode flattenedClone]](https://developer.apple.com/documentation/scenekit/scnnode/1407960-flattenedclone)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNNode *)flattenedClone ``` |
| To | ``` - (instancetype _Nonnull)flattenedClone ``` |

Modified [SCNNode.geometry](https://developer.apple.com/documentation/scenekit/scnnode/1407966-geometry)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNGeometry *geometry ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNGeometry *geometry ``` |

Modified [-[SCNNode hitTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnnode/1407998-hittestwithsegment)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTestWithSegmentFromPoint:(SCNVector3)pointA toPoint:(SCNVector3)pointB options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTestWithSegmentFromPoint:(SCNVector3)pointA toPoint:(SCNVector3)pointB options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNNode insertChildNode:atIndex:]](https://developer.apple.com/documentation/scenekit/scnnode/1407958-insertchildnode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertChildNode:(SCNNode *)child atIndex:(NSUInteger)index ``` |
| To | ``` - (void)insertChildNode:(SCNNode * _Nonnull)child atIndex:(NSUInteger)index ``` |

Modified [SCNNode.light](https://developer.apple.com/documentation/scenekit/scnnode/1408004-light)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNLight *light ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNLight *light ``` |

Modified [SCNNode.morpher](https://developer.apple.com/documentation/scenekit/scnnode/1408022-morpher)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNMorpher *morpher ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNMorpher *morpher ``` |

Modified [SCNNode.name](https://developer.apple.com/documentation/scenekit/scnnode/1408014-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [+[SCNNode node]](https://developer.apple.com/documentation/scenekit/scnnode/1407972-node)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)node ``` |
| To | ``` + (instancetype _Nonnull)node ``` |

Modified [+[SCNNode nodeWithGeometry:]](https://developer.apple.com/documentation/scenekit/scnnode/1408020-nodewithgeometry)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNNode *)nodeWithGeometry:(SCNGeometry *)geometry ``` |
| To | ``` + (SCNNode * _Nonnull)nodeWithGeometry:(SCNGeometry * _Nullable)geometry ``` |

Modified [SCNNode.parentNode](https://developer.apple.com/documentation/scenekit/scnnode/1407968-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *parentNode ``` |
| To | ``` @property(nonatomic, readonly, nullable) SCNNode *parentNode ``` |

Modified [SCNNode.physicsBody](https://developer.apple.com/documentation/scenekit/scnnode/1407988-physicsbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNPhysicsBody *physicsBody ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNPhysicsBody *physicsBody ``` |

Modified [SCNNode.physicsField](https://developer.apple.com/documentation/scenekit/scnnode/1408006-physicsfield)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNPhysicsField *physicsField ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNPhysicsField *physicsField ``` |

Modified [SCNNode.presentationNode](https://developer.apple.com/documentation/scenekit/scnnode/1408030-presentation)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNNode *)presentationNode ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *presentationNode ``` |

Modified [SCNNode.rendererDelegate](https://developer.apple.com/documentation/scenekit/scnnode/1408012-rendererdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SCNNodeRendererDelegate> rendererDelegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<SCNNodeRendererDelegate> rendererDelegate ``` |

Modified [-[SCNNode replaceChildNode:with:]](https://developer.apple.com/documentation/scenekit/scnnode/1408002-replacechildnode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceChildNode:(SCNNode *)oldChild with:(SCNNode *)newChild ``` |
| To | ``` - (void)replaceChildNode:(SCNNode * _Nonnull)oldChild with:(SCNNode * _Nonnull)newChild ``` |

Modified [SCNNode.skinner](https://developer.apple.com/documentation/scenekit/scnnode/1407953-skinner)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNSkinner *skinner ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNSkinner *skinner ``` |

Modified [-[SCNNodeRendererDelegate renderNode:renderer:arguments:]](https://developer.apple.com/documentation/scenekit/scnnoderendererdelegate/1407993-rendernode)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderNode:(SCNNode *)node renderer:(SCNRenderer *)renderer arguments:(NSDictionary *)arguments ``` |
| To | ``` - (void)renderNode:(SCNNode * _Nonnull)node renderer:(SCNRenderer * _Nonnull)renderer arguments:(NSDictionary<NSString *,NSValue *> * _Nonnull)arguments ``` |

#### SCNParametricGeometry.h

Modified [+[SCNBox boxWithWidth:height:length:chamferRadius:]](https://developer.apple.com/documentation/scenekit/scnbox/1522620-boxwithwidth)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)boxWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length chamferRadius:(CGFloat)chamferRadius ``` |
| To | ``` + (instancetype _Nonnull)boxWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length chamferRadius:(CGFloat)chamferRadius ``` |

Modified [+[SCNCapsule capsuleWithCapRadius:height:]](https://developer.apple.com/documentation/scenekit/scncapsule/1523790-capsulewithcapradius)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)capsuleWithCapRadius:(CGFloat)capRadius height:(CGFloat)height ``` |
| To | ``` + (instancetype _Nonnull)capsuleWithCapRadius:(CGFloat)capRadius height:(CGFloat)height ``` |

Modified [+[SCNCone coneWithTopRadius:bottomRadius:height:]](https://developer.apple.com/documentation/scenekit/scncone/1522863-conewithtopradius)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)coneWithTopRadius:(CGFloat)topRadius bottomRadius:(CGFloat)bottomRadius height:(CGFloat)height ``` |
| To | ``` + (instancetype _Nonnull)coneWithTopRadius:(CGFloat)topRadius bottomRadius:(CGFloat)bottomRadius height:(CGFloat)height ``` |

Modified [+[SCNCylinder cylinderWithRadius:height:]](https://developer.apple.com/documentation/scenekit/scncylinder/1523685-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)cylinderWithRadius:(CGFloat)radius height:(CGFloat)height ``` |
| To | ``` + (instancetype _Nonnull)cylinderWithRadius:(CGFloat)radius height:(CGFloat)height ``` |

Modified [+[SCNFloor floor]](https://developer.apple.com/documentation/scenekit/scnfloor/1572698-floor)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)floor ``` |
| To | ``` + (instancetype _Nonnull)floor ``` |

Modified [+[SCNPlane planeWithWidth:height:]](https://developer.apple.com/documentation/scenekit/scnplane/1523631-planewithwidth)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)planeWithWidth:(CGFloat)width height:(CGFloat)height ``` |
| To | ``` + (instancetype _Nonnull)planeWithWidth:(CGFloat)width height:(CGFloat)height ``` |

Modified [+[SCNPyramid pyramidWithWidth:height:length:]](https://developer.apple.com/documentation/scenekit/scnpyramid/1523254-pyramidwithwidth)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)pyramidWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length ``` |
| To | ``` + (instancetype _Nonnull)pyramidWithWidth:(CGFloat)width height:(CGFloat)height length:(CGFloat)length ``` |

Modified [SCNShape.chamferProfile](https://developer.apple.com/documentation/scenekit/scnshape/1522865-chamferprofile)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSBezierPath *chamferProfile ``` |
| To | ``` @property(nonatomic, copy, nullable) NSBezierPath *chamferProfile ``` |

Modified [SCNShape.path](https://developer.apple.com/documentation/scenekit/scnshape/1523434-path)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSBezierPath *path ``` |
| To | ``` @property(nonatomic, copy, nullable) NSBezierPath *path ``` |

Modified [+[SCNShape shapeWithPath:extrusionDepth:]](https://developer.apple.com/documentation/scenekit/scnshape/1523432-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithPath:(NSBezierPath *)path extrusionDepth:(CGFloat)extrusionDepth ``` |
| To | ``` + (instancetype _Nonnull)shapeWithPath:(NSBezierPath * _Nullable)path extrusionDepth:(CGFloat)extrusionDepth ``` |

Modified [+[SCNSphere sphereWithRadius:]](https://developer.apple.com/documentation/scenekit/scnsphere/1522601-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sphereWithRadius:(CGFloat)radius ``` |
| To | ``` + (instancetype _Nonnull)sphereWithRadius:(CGFloat)radius ``` |

Modified [SCNText.alignmentMode](https://developer.apple.com/documentation/scenekit/scntext/1523158-alignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *alignmentMode ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *alignmentMode ``` |

Modified [SCNText.chamferProfile](https://developer.apple.com/documentation/scenekit/scntext/1523334-chamferprofile)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSBezierPath *chamferProfile ``` |
| To | ``` @property(nonatomic, copy, nullable) NSBezierPath *chamferProfile ``` |

Modified [SCNText.font](https://developer.apple.com/documentation/scenekit/scntext/1523273-font)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSFont *font ``` |
| To | ``` @property(nonatomic, retain) NSFont * _Null_unspecified font ``` |

Modified [SCNText.string](https://developer.apple.com/documentation/scenekit/scntext/1523439-string)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) id string ``` |
| To | ``` @property(nonatomic, copy, nullable) id string ``` |

Modified [+[SCNText textWithString:extrusionDepth:]](https://developer.apple.com/documentation/scenekit/scntext/1522734-textwithstring)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textWithString:(id)string extrusionDepth:(CGFloat)extrusionDepth ``` |
| To | ``` + (instancetype _Nonnull)textWithString:(id _Nullable)string extrusionDepth:(CGFloat)extrusionDepth ``` |

Modified [SCNText.truncationMode](https://developer.apple.com/documentation/scenekit/scntext/1523414-truncationmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *truncationMode ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSString *truncationMode ``` |

Modified [+[SCNTorus torusWithRingRadius:pipeRadius:]](https://developer.apple.com/documentation/scenekit/scntorus/1523833-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)torusWithRingRadius:(CGFloat)ringRadius pipeRadius:(CGFloat)pipeRadius ``` |
| To | ``` + (instancetype _Nonnull)torusWithRingRadius:(CGFloat)ringRadius pipeRadius:(CGFloat)pipeRadius ``` |

Modified [+[SCNTube tubeWithInnerRadius:outerRadius:height:]](https://developer.apple.com/documentation/scenekit/scntube/1522843-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)tubeWithInnerRadius:(CGFloat)innerRadius outerRadius:(CGFloat)outerRadius height:(CGFloat)height ``` |
| To | ``` + (instancetype _Nonnull)tubeWithInnerRadius:(CGFloat)innerRadius outerRadius:(CGFloat)outerRadius height:(CGFloat)height ``` |

#### SCNParticleSystem.h

Modified [-[SCNNode addParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnnode/1523123-addparticlesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addParticleSystem:(SCNParticleSystem *)system ``` |
| To | ``` - (void)addParticleSystem:(SCNParticleSystem * _Nonnull)system ``` |

Modified [SCNNode.particleSystems](https://developer.apple.com/documentation/scenekit/scnnode/1522705-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *particleSystems ``` |
| To | ``` @property(readonly, nullable) NSArray<SCNParticleSystem *> *particleSystems ``` |

Modified [-[SCNNode removeParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnnode/1524014-removeparticlesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeParticleSystem:(SCNParticleSystem *)system ``` |
| To | ``` - (void)removeParticleSystem:(SCNParticleSystem * _Nonnull)system ``` |

Modified [SCNParticlePropertyController.animation](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523707-animation)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CAAnimation *animation ``` |
| To | ``` @property(nonatomic, retain, nonnull) CAAnimation *animation ``` |

Modified [+[SCNParticlePropertyController controllerWithAnimation:]](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1523579-controllerwithanimation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)controllerWithAnimation:(CAAnimation *)animation ``` |
| To | ``` + (instancetype _Nonnull)controllerWithAnimation:(CAAnimation * _Nonnull)animation ``` |

Modified [SCNParticlePropertyController.inputOrigin](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522895-inputorigin)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) SCNNode *inputOrigin ``` |
| To | ``` @property(nonatomic, weak, nullable) SCNNode *inputOrigin ``` |

Modified [SCNParticlePropertyController.inputProperty](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/1522973-inputproperty)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *inputProperty ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *inputProperty ``` |

Modified [-[SCNParticleSystem addModifierForProperties:atStage:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522635-addmodifierforproperties)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addModifierForProperties:(NSArray *)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock)block ``` |
| To | ``` - (void)addModifierForProperties:(NSArray<NSString *> * _Nonnull)properties atStage:(SCNParticleModifierStage)stage withBlock:(SCNParticleModifierBlock _Nonnull)block ``` |

Modified [SCNParticleSystem.colliderNodes](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523516-collidernodes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *colliderNodes ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SCNNode *> *colliderNodes ``` |

Modified [SCNParticleSystem.emitterShape](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522737-emittershape)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNGeometry *emitterShape ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNGeometry *emitterShape ``` |

Modified [-[SCNParticleSystem handleEvent:forProperties:withBlock:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523251-handleevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray *)properties withBlock:(SCNParticleEventBlock)block ``` |
| To | ``` - (void)handleEvent:(SCNParticleEvent)event forProperties:(NSArray<NSString *> * _Nonnull)properties withBlock:(SCNParticleEventBlock _Nonnull)block ``` |

Modified [SCNParticleSystem.particleColor](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1523248-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *particleColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *particleColor ``` |

Modified [SCNParticleSystem.particleImage](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524153-particleimage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id particleImage ``` |
| To | ``` @property(nonatomic, retain, nullable) id particleImage ``` |

Modified [+[SCNParticleSystem particleSystem]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1564486-particlesystem)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)particleSystem ``` |
| To | ``` + (instancetype _Nonnull)particleSystem ``` |

Modified [+[SCNParticleSystem particleSystemNamed:inDirectory:]](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522772-particlesystemnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)particleSystemNamed:(NSString *)name inDirectory:(NSString *)directory ``` |
| To | ``` + (instancetype _Nullable)particleSystemNamed:(NSString * _Nonnull)name inDirectory:(NSString * _Nullable)directory ``` |

Modified [SCNParticleSystem.propertyControllers](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522775-propertycontrollers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *propertyControllers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,SCNParticlePropertyController *> *propertyControllers ``` |

Modified [SCNParticleSystem.systemSpawnedOnCollision](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524068-systemspawnedoncollision)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNParticleSystem *systemSpawnedOnCollision ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNParticleSystem *systemSpawnedOnCollision ``` |

Modified [SCNParticleSystem.systemSpawnedOnDying](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1524091-systemspawnedondying)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNParticleSystem *systemSpawnedOnDying ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNParticleSystem *systemSpawnedOnDying ``` |

Modified [SCNParticleSystem.systemSpawnedOnLiving](https://developer.apple.com/documentation/scenekit/scnparticlesystem/1522751-systemspawnedonliving)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNParticleSystem *systemSpawnedOnLiving ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNParticleSystem *systemSpawnedOnLiving ``` |

Modified [-[SCNScene addParticleSystem:withTransform:]](https://developer.apple.com/documentation/scenekit/scnscene/1523359-addparticlesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addParticleSystem:(SCNParticleSystem *)system withTransform:(SCNMatrix4)transform ``` |
| To | ``` - (void)addParticleSystem:(SCNParticleSystem * _Nonnull)system withTransform:(SCNMatrix4)transform ``` |

Modified [SCNScene.particleSystems](https://developer.apple.com/documentation/scenekit/scnscene/1522787-particlesystems)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSArray *particleSystems ``` |
| To | ``` @property(readonly, nullable) NSArray<SCNParticleSystem *> *particleSystems ``` |

Modified [-[SCNScene removeParticleSystem:]](https://developer.apple.com/documentation/scenekit/scnscene/1523498-removeparticlesystem)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeParticleSystem:(SCNParticleSystem *)system ``` |
| To | ``` - (void)removeParticleSystem:(SCNParticleSystem * _Nonnull)system ``` |

#### SCNPhysicsBehavior.h

Modified [SCNPhysicsBallSocketJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387981-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNPhysicsBody *bodyA ``` |

Modified [SCNPhysicsBallSocketJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387902-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly, nullable) SCNPhysicsBody *bodyB ``` |

Modified [+[SCNPhysicsBallSocketJoint jointWithBody:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387975-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBody:(SCNPhysicsBody *)body anchor:(SCNVector3)anchor ``` |
| To | ``` + (instancetype _Nonnull)jointWithBody:(SCNPhysicsBody * _Nonnull)body anchor:(SCNVector3)anchor ``` |

Modified [+[SCNPhysicsBallSocketJoint jointWithBodyA:anchorA:bodyB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicsballsocketjoint/1387926-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBodyA:(SCNPhysicsBody *)bodyA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody *)bodyB anchorB:(SCNVector3)anchorB ``` |
| To | ``` + (instancetype _Nonnull)jointWithBodyA:(SCNPhysicsBody * _Nonnull)bodyA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody * _Nonnull)bodyB anchorB:(SCNVector3)anchorB ``` |

Modified [SCNPhysicsHingeJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387973-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNPhysicsBody *bodyA ``` |

Modified [SCNPhysicsHingeJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387918-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly, nullable) SCNPhysicsBody *bodyB ``` |

Modified [+[SCNPhysicsHingeJoint jointWithBody:axis:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387977-jointwithbody)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBody:(SCNPhysicsBody *)body axis:(SCNVector3)axis anchor:(SCNVector3)anchor ``` |
| To | ``` + (instancetype _Nonnull)jointWithBody:(SCNPhysicsBody * _Nonnull)body axis:(SCNVector3)axis anchor:(SCNVector3)anchor ``` |

Modified [+[SCNPhysicsHingeJoint jointWithBodyA:axisA:anchorA:bodyB:axisB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicshingejoint/1387898-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBodyA:(SCNPhysicsBody *)bodyA axisA:(SCNVector3)axisA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody *)bodyB axisB:(SCNVector3)axisB anchorB:(SCNVector3)anchorB ``` |
| To | ``` + (instancetype _Nonnull)jointWithBodyA:(SCNPhysicsBody * _Nonnull)bodyA axisA:(SCNVector3)axisA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody * _Nonnull)bodyB axisB:(SCNVector3)axisB anchorB:(SCNVector3)anchorB ``` |

Modified [SCNPhysicsSliderJoint.bodyA](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387987-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNPhysicsBody *bodyA ``` |

Modified [SCNPhysicsSliderJoint.bodyB](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387896-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly, nullable) SCNPhysicsBody *bodyB ``` |

Modified [+[SCNPhysicsSliderJoint jointWithBody:axis:anchor:]](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387932-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBody:(SCNPhysicsBody *)body axis:(SCNVector3)axis anchor:(SCNVector3)anchor ``` |
| To | ``` + (instancetype _Nonnull)jointWithBody:(SCNPhysicsBody * _Nonnull)body axis:(SCNVector3)axis anchor:(SCNVector3)anchor ``` |

Modified [+[SCNPhysicsSliderJoint jointWithBodyA:axisA:anchorA:bodyB:axisB:anchorB:]](https://developer.apple.com/documentation/scenekit/scnphysicssliderjoint/1387922-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)jointWithBodyA:(SCNPhysicsBody *)bodyA axisA:(SCNVector3)axisA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody *)bodyB axisB:(SCNVector3)axisB anchorB:(SCNVector3)anchorB ``` |
| To | ``` + (instancetype _Nonnull)jointWithBodyA:(SCNPhysicsBody * _Nonnull)bodyA axisA:(SCNVector3)axisA anchorA:(SCNVector3)anchorA bodyB:(SCNPhysicsBody * _Nonnull)bodyB axisB:(SCNVector3)axisB anchorB:(SCNVector3)anchorB ``` |

Modified [SCNPhysicsVehicle.chassisBody](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387985-chassisbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsBody *chassisBody ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNPhysicsBody *chassisBody ``` |

Modified [+[SCNPhysicsVehicle vehicleWithChassisBody:wheels:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387943-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)vehicleWithChassisBody:(SCNPhysicsBody *)chassisBody wheels:(NSArray *)wheels ``` |
| To | ``` + (instancetype _Nonnull)vehicleWithChassisBody:(SCNPhysicsBody * _Nonnull)chassisBody wheels:(NSArray<SCNPhysicsVehicleWheel *> * _Nonnull)wheels ``` |

Modified [SCNPhysicsVehicle.wheels](https://developer.apple.com/documentation/scenekit/scnphysicsvehicle/1387906-wheels)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *wheels ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNPhysicsVehicleWheel *> *wheels ``` |

Modified [SCNPhysicsVehicleWheel.node](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387892-node)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SCNNode *node ``` |
| To | ``` @property(readonly, nonnull) SCNNode *node ``` |

Modified [+[SCNPhysicsVehicleWheel wheelWithNode:]](https://developer.apple.com/documentation/scenekit/scnphysicsvehiclewheel/1387989-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)wheelWithNode:(SCNNode *)node ``` |
| To | ``` + (instancetype _Nonnull)wheelWithNode:(SCNNode * _Nonnull)node ``` |

#### SCNPhysicsBody.h

Added [SCNPhysicsBody.affectedByGravity](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514738-affectedbygravity)Added [SCNPhysicsBody.contactTestBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514746-contacttestbitmask)Added [SCNPhysicsBody.momentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514777-momentofinertia)Added [SCNPhysicsBody.usesDefaultMomentOfInertia](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514761-usesdefaultmomentofinertia)Modified [+[SCNPhysicsBody bodyWithType:shape:]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514797-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)bodyWithType:(SCNPhysicsBodyType)type shape:(SCNPhysicsShape *)shape ``` |
| To | ``` + (instancetype _Nonnull)bodyWithType:(SCNPhysicsBodyType)type shape:(SCNPhysicsShape * _Nullable)shape ``` |

Modified [SCNPhysicsBody.categoryBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514768-categorybitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger categoryBitMask ``` |
| To | ``` @property(nonatomic) NSUInteger categoryBitMask ``` |

Modified [SCNPhysicsBody.collisionBitMask](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514772-collisionbitmask)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger collisionBitMask ``` |
| To | ``` @property(nonatomic) NSUInteger collisionBitMask ``` |

Modified [+[SCNPhysicsBody dynamicBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514766-dynamicbody)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)dynamicBody ``` |
| To | ``` + (instancetype _Nonnull)dynamicBody ``` |

Modified [+[SCNPhysicsBody kinematicBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514776-kinematicbody)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)kinematicBody ``` |
| To | ``` + (instancetype _Nonnull)kinematicBody ``` |

Modified [SCNPhysicsBody.physicsShape](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514789-physicsshape)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNPhysicsShape *physicsShape ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNPhysicsShape *physicsShape ``` |

Modified [+[SCNPhysicsBody staticBody]](https://developer.apple.com/documentation/scenekit/scnphysicsbody/1514791-staticbody)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)staticBody ``` |
| To | ``` + (instancetype _Nonnull)staticBody ``` |

#### SCNPhysicsContact.h

Modified [SCNPhysicsContact.nodeA](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1523445-nodea)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *nodeA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *nodeA ``` |

Modified [SCNPhysicsContact.nodeB](https://developer.apple.com/documentation/scenekit/scnphysicscontact/1524232-nodeb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *nodeB ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *nodeB ``` |

#### SCNPhysicsField.h

Modified [+[SCNPhysicsField customFieldWithEvaluationBlock:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388140-customfieldwithevaluationblock)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)customFieldWithEvaluationBlock:(SCNFieldForceEvaluator)block ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)customFieldWithEvaluationBlock:(SCNFieldForceEvaluator _Nonnull)block ``` |

Modified [+[SCNPhysicsField dragField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388164-drag)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)dragField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)dragField ``` |

Modified [+[SCNPhysicsField electricField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388152-electricfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)electricField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)electricField ``` |

Modified [+[SCNPhysicsField linearGravityField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388130-lineargravity)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)linearGravityField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)linearGravityField ``` |

Modified [+[SCNPhysicsField magneticField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388168-magneticfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)magneticField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)magneticField ``` |

Modified [+[SCNPhysicsField noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388150-noisefieldwithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)noiseFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)noiseFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |

Modified [+[SCNPhysicsField radialGravityField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388115-radialgravity)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)radialGravityField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)radialGravityField ``` |

Modified [+[SCNPhysicsField springField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388134-spring)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)springField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)springField ``` |

Modified [+[SCNPhysicsField turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388162-turbulencefield)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)turbulenceFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)turbulenceFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |

Modified [+[SCNPhysicsField vortexField]](https://developer.apple.com/documentation/scenekit/scnphysicsfield/1388160-vortex)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNPhysicsField *)vortexField ``` |
| To | ``` + (SCNPhysicsField * _Nonnull)vortexField ``` |

#### SCNPhysicsShape.h

Added [SCNPhysicsShape.options](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508904-options)Added [SCNPhysicsShape.sourceObject](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508888-sourceobject)Added [SCNPhysicsShape.transforms](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508898-transforms)Modified [+[SCNPhysicsShape shapeWithGeometry:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508897-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithGeometry:(SCNGeometry *)geometry options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)shapeWithGeometry:(SCNGeometry * _Nonnull)geometry options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNPhysicsShape shapeWithNode:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508889-shapewithnode)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithNode:(SCNNode *)node options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)shapeWithNode:(SCNNode * _Nonnull)node options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNPhysicsShape shapeWithShapes:transforms:]](https://developer.apple.com/documentation/scenekit/scnphysicsshape/1508886-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeWithShapes:(NSArray *)shapes transforms:(NSArray *)transforms ``` |
| To | ``` + (instancetype _Nonnull)shapeWithShapes:(NSArray<SCNPhysicsShape *> * _Nonnull)shapes transforms:(NSArray<NSValue *> * _Nullable)transforms ``` |

#### SCNPhysicsWorld.h

Modified [-[SCNPhysicsContactDelegate physicsWorld:didBeginContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512835-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` - (void)physicsWorld:(SCNPhysicsWorld *)world didBeginContact:(SCNPhysicsContact *)contact ``` |
| To | ``` - (void)physicsWorld:(SCNPhysicsWorld * _Nonnull)world didBeginContact:(SCNPhysicsContact * _Nonnull)contact ``` |

Modified [-[SCNPhysicsContactDelegate physicsWorld:didEndContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512883-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` - (void)physicsWorld:(SCNPhysicsWorld *)world didEndContact:(SCNPhysicsContact *)contact ``` |
| To | ``` - (void)physicsWorld:(SCNPhysicsWorld * _Nonnull)world didEndContact:(SCNPhysicsContact * _Nonnull)contact ``` |

Modified [-[SCNPhysicsContactDelegate physicsWorld:didUpdateContact:]](https://developer.apple.com/documentation/scenekit/scnphysicscontactdelegate/1512865-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` - (void)physicsWorld:(SCNPhysicsWorld *)world didUpdateContact:(SCNPhysicsContact *)contact ``` |
| To | ``` - (void)physicsWorld:(SCNPhysicsWorld * _Nonnull)world didUpdateContact:(SCNPhysicsContact * _Nonnull)contact ``` |

Modified [-[SCNPhysicsWorld addBehavior:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512839-addbehavior)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addBehavior:(SCNPhysicsBehavior *)behavior ``` |
| To | ``` - (void)addBehavior:(SCNPhysicsBehavior * _Nonnull)behavior ``` |

Modified [SCNPhysicsWorld.allBehaviors](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512853-allbehaviors)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allBehaviors ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SCNPhysicsBehavior *> *allBehaviors ``` |

Modified [SCNPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512843-contactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, assign) id<SCNPhysicsContactDelegate> contactDelegate ``` |
| To | ``` @property(atomic, assign, nullable) id<SCNPhysicsContactDelegate> contactDelegate ``` |

Modified [-[SCNPhysicsWorld contactTestBetweenBody:andBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512875-contacttestbetween)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contactTestBetweenBody:(SCNPhysicsBody *)bodyA andBody:(SCNPhysicsBody *)bodyB options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)contactTestBetweenBody:(SCNPhysicsBody * _Nonnull)bodyA andBody:(SCNPhysicsBody * _Nonnull)bodyB options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld contactTestWithBody:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512841-contacttestwithbody)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)contactTestWithBody:(SCNPhysicsBody *)body options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)contactTestWithBody:(SCNPhysicsBody * _Nonnull)body options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld convexSweepTestWithShape:fromTransform:toTransform:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512859-convexsweeptest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)convexSweepTestWithShape:(SCNPhysicsShape *)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNPhysicsContact *> * _Nonnull)convexSweepTestWithShape:(SCNPhysicsShape * _Nonnull)shape fromTransform:(SCNMatrix4)from toTransform:(SCNMatrix4)to options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld rayTestWithSegmentFromPoint:toPoint:options:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512857-raytestwithsegmentfrompoint)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)rayTestWithSegmentFromPoint:(SCNVector3)origin toPoint:(SCNVector3)dest options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNPhysicsWorld removeBehavior:]](https://developer.apple.com/documentation/scenekit/scnphysicsworld/1512870-removebehavior)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeBehavior:(SCNPhysicsBehavior *)behavior ``` |
| To | ``` - (void)removeBehavior:(SCNPhysicsBehavior * _Nonnull)behavior ``` |

#### SCNReferenceNode.h (Added)

Added [SCNReferenceNode](https://developer.apple.com/documentation/scenekit/scnreferencenode)Added [-[SCNReferenceNode initWithCoder:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1524061-init)Added [-[SCNReferenceNode initWithURL:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523967-init)Added [-[SCNReferenceNode load]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523204-load)Added [SCNReferenceNode.loaded](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523906-loaded)Added [SCNReferenceNode.loadingPolicy](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522996-loadingpolicy)Added [+[SCNReferenceNode referenceNodeWithURL:]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1551036-referencenodewithurl)Added [SCNReferenceNode.referenceURL](https://developer.apple.com/documentation/scenekit/scnreferencenode/1522733-referenceurl)Added [-[SCNReferenceNode unload]](https://developer.apple.com/documentation/scenekit/scnreferencenode/1523566-unload)Added [SCNReferenceLoadingPolicy](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy)Added [SCNReferenceLoadingPolicyImmediate](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyimmediate)Added [SCNReferenceLoadingPolicyOnDemand](https://developer.apple.com/documentation/scenekit/scnreferenceloadingpolicy/scnreferenceloadingpolicyondemand)

#### SCNRenderer.h

Added [-[SCNRenderer renderAtTime:viewport:commandBuffer:passDescriptor:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518401-renderattime)Added [+[SCNRenderer rendererWithDevice:options:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518404-rendererwithdevice)Modified [-[SCNRenderer render]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518403-render)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [+[SCNRenderer rendererWithContext:options:]](https://developer.apple.com/documentation/scenekit/scnrenderer/1518408-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rendererWithContext:(void *)context options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nonnull)rendererWithContext:(CGLContextObj _Nonnull)context options:(NSDictionary * _Nullable)options ``` |

Modified [SCNRenderer.scene](https://developer.apple.com/documentation/scenekit/scnrenderer/1518400-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNScene *scene ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNScene *scene ``` |

#### SCNScene.h

Modified [-[SCNScene attributeForKey:]](https://developer.apple.com/documentation/scenekit/scnscene/1522858-attributeforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)attributeForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)attributeForKey:(NSString * _Nonnull)key ``` |

Modified [SCNScene.background](https://developer.apple.com/documentation/scenekit/scnscene/1523665-background)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNMaterialProperty *background ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNMaterialProperty *background ``` |

Modified [SCNScene.fogColor](https://developer.apple.com/documentation/scenekit/scnscene/1522774-fogcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) id fogColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) id fogColor ``` |

Modified [SCNScene.physicsWorld](https://developer.apple.com/documentation/scenekit/scnscene/1522643-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNPhysicsWorld *physicsWorld ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNPhysicsWorld *physicsWorld ``` |

Modified [SCNScene.rootNode](https://developer.apple.com/documentation/scenekit/scnscene/1524029-rootnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *rootNode ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *rootNode ``` |

Modified [+[SCNScene scene]](https://developer.apple.com/documentation/scenekit/scnscene/1574179-scene)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)scene ``` |
| To | ``` + (instancetype _Nonnull)scene ``` |

Modified [+[SCNScene sceneNamed:]](https://developer.apple.com/documentation/scenekit/scnscene/1523355-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneNamed:(NSString *)name ``` |
| To | ``` + (instancetype _Nullable)sceneNamed:(NSString * _Nonnull)name ``` |

Modified [+[SCNScene sceneNamed:inDirectory:options:]](https://developer.apple.com/documentation/scenekit/scnscene/1522851-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneNamed:(NSString *)name inDirectory:(NSString *)directory options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneNamed:(NSString * _Nonnull)name inDirectory:(NSString * _Nullable)directory options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNScene sceneWithURL:options:error:]](https://developer.apple.com/documentation/scenekit/scnscene/1522660-scenewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneWithURL:(NSURL *)url options:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` + (instancetype _Nullable)sceneWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[SCNScene setAttribute:forKey:]](https://developer.apple.com/documentation/scenekit/scnscene/1524229-setattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setAttribute:(id)attribute forKey:(NSString *)key ``` |
| To | ``` - (void)setAttribute:(id _Nullable)attribute forKey:(NSString * _Nonnull)key ``` |

Modified [-[SCNScene writeToURL:options:delegate:progressHandler:]](https://developer.apple.com/documentation/scenekit/scnscene/1523577-write)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)writeToURL:(NSURL *)url options:(NSDictionary *)options delegate:(id<SCNSceneExportDelegate>)delegate progressHandler:(SCNSceneExportProgressHandler)progressHandler ``` |
| To | ``` - (BOOL)writeToURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options delegate:(id<SCNSceneExportDelegate> _Nullable)delegate progressHandler:(SCNSceneExportProgressHandler _Nullable)progressHandler ``` |

Modified [-[SCNSceneExportDelegate writeImage:withSceneDocumentURL:originalImageURL:]](https://developer.apple.com/documentation/scenekit/scnsceneexportdelegate/1524221-write)

|  | Declaration |
| --- | --- |
| From | ``` - (NSURL *)writeImage:(NSImage *)image withSceneDocumentURL:(NSURL *)documentURL originalImageURL:(NSURL *)originalImageURL ``` |
| To | ``` - (NSURL * _Nullable)writeImage:(NSImage * _Nonnull)image withSceneDocumentURL:(NSURL * _Nonnull)documentURL originalImageURL:(NSURL * _Nullable)originalImageURL ``` |

#### SCNSceneRenderer.h

Added [SCNSceneRenderer.audioEngine](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522686-audioengine)Added [SCNSceneRenderer.audioEnvironmentNode](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523582-audioenvironmentnode)Added [SCNSceneRenderer.audioListener](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523747-audiolistener)Added [SCNSceneRenderer.colorPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523701-colorpixelformat)Added [SCNSceneRenderer.commandQueue](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523974-commandqueue)Added [SCNSceneRenderer.currentRenderCommandEncoder](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522609-currentrendercommandencoder)Added [SCNSceneRenderer.debugOptions](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523281-debugoptions)Added [SCNSceneRenderer.depthPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523780-depthpixelformat)Added [SCNSceneRenderer.device](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523935-device)Added [-[SCNSceneRenderer nodesInsideFrustumWithPointOfView:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522942-nodesinsidefrustum)Added [-[SCNSceneRenderer presentScene:withTransition:incomingPointOfView:completionHandler:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523028-presentscene)Added [SCNSceneRenderer.renderingAPI](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522616-renderingapi)Added [SCNSceneRenderer.stencilPixelFormat](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523315-stencilpixelformat)Added [SCNDebugOptionNone](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionnone)Added [SCNDebugOptions](https://developer.apple.com/documentation/scenekit/scndebugoptions)Added [SCNDebugOptionShowBoundingBoxes](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowboundingboxes)Added [SCNDebugOptionShowLightExtents](https://developer.apple.com/documentation/scenekit/scndebugoptions/scndebugoptionshowlightextents)Added [SCNDebugOptionShowLightInfluences](https://developer.apple.com/documentation/scenekit/scndebugoptions/1522606-showlightinfluences)Added [SCNDebugOptionShowPhysicsFields](https://developer.apple.com/documentation/scenekit/scndebugoptions/1523589-showphysicsfields)Added [SCNDebugOptionShowPhysicsShapes](https://developer.apple.com/documentation/scenekit/scndebugoptions/1522896-showphysicsshapes)Added [SCNDebugOptionShowWireframe](https://developer.apple.com/documentation/scenekit/scndebugoptions/1523384-showwireframe)Added [SCNRenderingAPI](https://developer.apple.com/documentation/scenekit/scnrenderingapi)Added [SCNRenderingAPIMetal](https://developer.apple.com/documentation/scenekit/scnrenderingapi/metal)Added [SCNRenderingAPIOpenGLCore32](https://developer.apple.com/documentation/scenekit/scnrenderingapi/scnrenderingapiopenglcore32)Added [SCNRenderingAPIOpenGLCore41](https://developer.apple.com/documentation/scenekit/scnrenderingapi/scnrenderingapiopenglcore41)Added [SCNRenderingAPIOpenGLLegacy](https://developer.apple.com/documentation/scenekit/scnrenderingapi/opengllegacy)Modified [SCNHitTestResult.node](https://developer.apple.com/documentation/scenekit/scnhittestresult/1523256-node)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SCNNode *node ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SCNNode *node ``` |

Modified [SCNSceneRenderer.context](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522840-context)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) void *context ``` |
| To | ``` @property(nonatomic, readonly, nullable) void *context ``` |

Modified [SCNSceneRenderer.delegate](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522671-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SCNSceneRendererDelegate> delegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<SCNSceneRendererDelegate> delegate ``` |

Modified [-[SCNSceneRenderer hitTest:options:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522929-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTest:(CGPoint)thePoint options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTest:(CGPoint)point options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneRenderer isNodeInsideFrustum:withPointOfView:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522647-isnode)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isNodeInsideFrustum:(SCNNode *)node withPointOfView:(SCNNode *)pointOfView ``` |
| To | ``` - (BOOL)isNodeInsideFrustum:(SCNNode * _Nonnull)node withPointOfView:(SCNNode * _Nonnull)pointOfView ``` |

Modified [SCNSceneRenderer.overlaySKScene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1524051-overlayskscene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKScene *overlaySKScene ``` |
| To | ``` @property(nonatomic, retain, nullable) SKScene *overlaySKScene ``` |

Modified [SCNSceneRenderer.pointOfView](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523982-pointofview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNNode *pointOfView ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNNode *pointOfView ``` |

Modified [-[SCNSceneRenderer prepareObject:shouldAbortBlock:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1522798-prepareobject)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)prepareObject:(id)object shouldAbortBlock:(BOOL (^)(void))block ``` |
| To | ``` - (BOOL)prepareObject:(id _Nonnull)object shouldAbortBlock:(BOOL (^ _Nullable)(void))block ``` |

Modified [-[SCNSceneRenderer prepareObjects:withCompletionHandler:]](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523375-prepareobjects)

|  | Declaration |
| --- | --- |
| From | ``` - (void)prepareObjects:(NSArray *)objects withCompletionHandler:(void (^)(BOOL success))completionHandler ``` |
| To | ``` - (void)prepareObjects:(NSArray * _Nonnull)objects withCompletionHandler:(void (^ _Nullable)(BOOL success))completionHandler ``` |

Modified [SCNSceneRenderer.scene](https://developer.apple.com/documentation/scenekit/scnscenerenderer/1523956-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNScene *scene ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNScene *scene ``` |

Modified [-[SCNSceneRendererDelegate renderer:didApplyAnimationsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523038-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didApplyAnimationsAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didApplyAnimationsAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:didRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1524233-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didRenderScene:(SCNScene *)scene atTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didRenderScene:(SCNScene * _Nonnull)scene atTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:didSimulatePhysicsAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522738-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer didSimulatePhysicsAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer didSimulatePhysicsAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:updateAtTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1522937-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer updateAtTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer updateAtTime:(NSTimeInterval)time ``` |

Modified [-[SCNSceneRendererDelegate renderer:willRenderScene:atTime:]](https://developer.apple.com/documentation/scenekit/scnscenerendererdelegate/1523483-renderer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderer:(id<SCNSceneRenderer>)aRenderer willRenderScene:(SCNScene *)scene atTime:(NSTimeInterval)time ``` |
| To | ``` - (void)renderer:(id<SCNSceneRenderer> _Nonnull)renderer willRenderScene:(SCNScene * _Nonnull)scene atTime:(NSTimeInterval)time ``` |

#### SCNSceneSource.h

Modified [SCNSceneSource.data](https://developer.apple.com/documentation/scenekit/scnscenesource/1523061-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSData *data ``` |
| To | ``` @property(readonly, nullable) NSData *data ``` |

Modified [-[SCNSceneSource entriesPassingTest:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523055-entries)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)entriesPassingTest:(BOOL (^)(id entry, NSString *identifier, BOOL *stop))predicate ``` |
| To | ``` - (NSArray<id> * _Nonnull)entriesPassingTest:(BOOL (^ _Nonnull)(id _Nonnull entry, NSString * _Nonnull identifier, BOOL * _Nonnull stop))predicate ``` |

Modified [-[SCNSceneSource entryWithIdentifier:withClass:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573762-entrywithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)entryWithIdentifier:(NSString *)uid withClass:(Class)entryClass ``` |
| To | ``` - (id _Nullable)entryWithIdentifier:(NSString * _Nonnull)uid withClass:(Class _Nonnull)entryClass ``` |

Modified [-[SCNSceneSource identifiersOfEntriesWithClass:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523656-identifiersofentrieswithclass)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)identifiersOfEntriesWithClass:(Class)entryClass ``` |
| To | ``` - (NSArray<NSString *> * _Nonnull)identifiersOfEntriesWithClass:(Class _Nonnull)entryClass ``` |

Modified [-[SCNSceneSource initWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523500-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneSource initWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522629-initwithurl)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithURL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nullable)initWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneSource propertyForKey:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523277-propertyforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (id)propertyForKey:(NSString *)key ``` |
| To | ``` - (id _Nullable)propertyForKey:(NSString * _Nonnull)key ``` |

Modified [+[SCNSceneSource sceneSourceWithData:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573764-scenesourcewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithData:(NSData *)data options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneSourceWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [+[SCNSceneSource sceneSourceWithURL:options:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1573763-scenesourcewithurl)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneSourceWithURL:(NSURL *)url options:(NSDictionary *)options ``` |
| To | ``` + (instancetype _Nullable)sceneSourceWithURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SCNSceneSource sceneWithOptions:error:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1523962-scenewithoptions)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary *)options error:(NSError **)error ``` |
| To | ``` - (SCNScene * _Nullable)sceneWithOptions:(NSDictionary<NSString *,id> * _Nullable)options error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[SCNSceneSource sceneWithOptions:statusHandler:]](https://developer.apple.com/documentation/scenekit/scnscenesource/1522887-scene)

|  | Declaration |
| --- | --- |
| From | ``` - (SCNScene *)sceneWithOptions:(NSDictionary *)options statusHandler:(SCNSceneSourceStatusHandler)statusHandler ``` |
| To | ``` - (SCNScene * _Nullable)sceneWithOptions:(NSDictionary<NSString *,id> * _Nullable)options statusHandler:(SCNSceneSourceStatusHandler _Nullable)statusHandler ``` |

Modified [SCNSceneSource.url](https://developer.apple.com/documentation/scenekit/scnscenesource/1524038-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSURL *url ``` |
| To | ``` @property(readonly, nullable) NSURL *url ``` |

#### SCNShadable.h

Added [SCNBufferStream](https://developer.apple.com/documentation/scenekit/scnbufferstream)Added [-[SCNBufferStream writeBytes:length:]](https://developer.apple.com/documentation/scenekit/scnbufferstream/1523175-writebytes)Added [SCNProgram.fragmentFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1524012-fragmentfunctionname)Added [-[SCNProgram handleBindingOfBufferNamed:frequency:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnprogram/1524047-handlebindingofbuffernamed)Added [SCNProgram.library](https://developer.apple.com/documentation/scenekit/scnprogram/1522934-library)Added [SCNProgram.vertexFunctionName](https://developer.apple.com/documentation/scenekit/scnprogram/1522799-vertexfunctionname)Added [SCNBufferBindingBlock](https://developer.apple.com/documentation/scenekit/scnbufferbindingblock)Added [SCNBufferFrequency](https://developer.apple.com/documentation/scenekit/scnbufferfrequency)Added [SCNBufferFrequencyPerFrame](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencyperframe)Added [SCNBufferFrequencyPerNode](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencypernode)Added [SCNBufferFrequencyPerShadable](https://developer.apple.com/documentation/scenekit/scnbufferfrequency/scnbufferfrequencypershadable)Modified [SCNProgram.delegate](https://developer.apple.com/documentation/scenekit/scnprogram/1522611-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SCNProgramDelegate> delegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<SCNProgramDelegate> delegate ``` |

Modified [SCNProgram.fragmentShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523135-fragmentshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *fragmentShader ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *fragmentShader ``` |

Modified [SCNProgram.geometryShader](https://developer.apple.com/documentation/scenekit/scnprogram/1524049-geometryshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *geometryShader ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *geometryShader ``` |

Modified [+[SCNProgram program]](https://developer.apple.com/documentation/scenekit/scnprogram/1565076-program)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)program ``` |
| To | ``` + (instancetype _Nonnull)program ``` |

Modified [-[SCNProgram semanticForSymbol:]](https://developer.apple.com/documentation/scenekit/scnprogram/1523350-semantic)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)semanticForSymbol:(NSString *)symbol ``` |
| To | ``` - (NSString * _Nullable)semanticForSymbol:(NSString * _Nonnull)symbol ``` |

Modified [-[SCNProgram setSemantic:forSymbol:options:]](https://developer.apple.com/documentation/scenekit/scnprogram/1522730-setsemantic)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setSemantic:(NSString *)semantic forSymbol:(NSString *)symbol options:(NSDictionary *)options ``` |
| To | ``` - (void)setSemantic:(NSString * _Nullable)semantic forSymbol:(NSString * _Nonnull)symbol options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [SCNProgram.tessellationControlShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523852-tessellationcontrolshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *tessellationControlShader ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *tessellationControlShader ``` |

Modified [SCNProgram.tessellationEvaluationShader](https://developer.apple.com/documentation/scenekit/scnprogram/1523760-tessellationevaluationshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *tessellationEvaluationShader ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *tessellationEvaluationShader ``` |

Modified [SCNProgram.vertexShader](https://developer.apple.com/documentation/scenekit/scnprogram/1522891-vertexshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *vertexShader ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *vertexShader ``` |

Modified [-[SCNProgramDelegate program:bindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1524155-program)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)program:(SCNProgram *)program bindValueForSymbol:(NSString *)symbol atLocation:(unsigned int)location programID:(unsigned int)programID renderer:(SCNRenderer *)renderer ``` |
| To | ``` - (BOOL)program:(SCNProgram * _Nonnull)program bindValueForSymbol:(NSString * _Nonnull)symbol atLocation:(unsigned int)location programID:(unsigned int)programID renderer:(SCNRenderer * _Nonnull)renderer ``` |

Modified [-[SCNProgramDelegate program:handleError:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523007-program)

|  | Declaration |
| --- | --- |
| From | ``` - (void)program:(SCNProgram *)program handleError:(NSError *)error ``` |
| To | ``` - (void)program:(SCNProgram * _Nonnull)program handleError:(NSError * _Nonnull)error ``` |

Modified [-[SCNProgramDelegate program:unbindValueForSymbol:atLocation:programID:renderer:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523857-program)

|  | Declaration |
| --- | --- |
| From | ``` - (void)program:(SCNProgram *)program unbindValueForSymbol:(NSString *)symbol atLocation:(unsigned int)location programID:(unsigned int)programID renderer:(SCNRenderer *)renderer ``` |
| To | ``` - (void)program:(SCNProgram * _Nonnull)program unbindValueForSymbol:(NSString * _Nonnull)symbol atLocation:(unsigned int)location programID:(unsigned int)programID renderer:(SCNRenderer * _Nonnull)renderer ``` |

Modified [-[SCNProgramDelegate programIsOpaque:]](https://developer.apple.com/documentation/scenekit/scnprogramdelegate/1523068-programisopaque)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)programIsOpaque:(SCNProgram *)program ``` |
| To | ``` - (BOOL)programIsOpaque:(SCNProgram * _Nonnull)program ``` |

Modified [-[SCNShadable handleBindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1523063-handlebindingofsymbol)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleBindingOfSymbol:(NSString *)symbol usingBlock:(SCNBindingBlock)block ``` |
| To | ``` - (void)handleBindingOfSymbol:(NSString * _Nonnull)symbol usingBlock:(SCNBindingBlock _Nullable)block ``` |

Modified [-[SCNShadable handleUnbindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scnshadable/1522783-handleunbinding)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleUnbindingOfSymbol:(NSString *)symbol usingBlock:(SCNBindingBlock)block ``` |
| To | ``` - (void)handleUnbindingOfSymbol:(NSString * _Nonnull)symbol usingBlock:(SCNBindingBlock _Nullable)block ``` |

Modified [SCNShadable.program](https://developer.apple.com/documentation/scenekit/scnshadable/1523689-program)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNProgram *program ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNProgram *program ``` |

Modified [SCNShadable.shaderModifiers](https://developer.apple.com/documentation/scenekit/scnshadable/1523348-shadermodifiers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSDictionary *shaderModifiers ``` |
| To | ``` @property(nonatomic, copy, nullable) NSDictionary<NSString *,NSString *> *shaderModifiers ``` |

#### SCNSkinner.h

Modified [SCNSkinner.baseGeometry](https://developer.apple.com/documentation/scenekit/scnskinner/1522823-basegeometry)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, nonatomic) SCNGeometry *baseGeometry ``` |
| To | ``` @property(retain, nonatomic, nullable) SCNGeometry *baseGeometry ``` |

Modified [SCNSkinner.boneIndices](https://developer.apple.com/documentation/scenekit/scnskinner/1524117-boneindices)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SCNGeometrySource *boneIndices ``` |
| To | ``` @property(readonly, nonatomic, nonnull) SCNGeometrySource *boneIndices ``` |

Modified [SCNSkinner.boneInverseBindTransforms](https://developer.apple.com/documentation/scenekit/scnskinner/1523802-boneinversebindtransforms)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *boneInverseBindTransforms ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSArray<NSValue *> *boneInverseBindTransforms ``` |

Modified [SCNSkinner.bones](https://developer.apple.com/documentation/scenekit/scnskinner/1522732-bones)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *bones ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<SCNNode *> *bones ``` |

Modified [SCNSkinner.boneWeights](https://developer.apple.com/documentation/scenekit/scnskinner/1522986-boneweights)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) SCNGeometrySource *boneWeights ``` |
| To | ``` @property(readonly, nonatomic, nonnull) SCNGeometrySource *boneWeights ``` |

Modified [SCNSkinner.skeleton](https://developer.apple.com/documentation/scenekit/scnskinner/1523048-skeleton)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNNode *skeleton ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNNode *skeleton ``` |

Modified [+[SCNSkinner skinnerWithBaseGeometry:bones:boneInverseBindTransforms:boneWeights:boneIndices:]](https://developer.apple.com/documentation/scenekit/scnskinner/1523964-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)skinnerWithBaseGeometry:(SCNGeometry *)baseGeometry bones:(NSArray *)bones boneInverseBindTransforms:(NSArray *)boneInverseBindTransforms boneWeights:(SCNGeometrySource *)boneWeights boneIndices:(SCNGeometrySource *)boneIndices ``` |
| To | ``` + (instancetype _Nonnull)skinnerWithBaseGeometry:(SCNGeometry * _Nullable)baseGeometry bones:(NSArray<SCNNode *> * _Nonnull)bones boneInverseBindTransforms:(NSArray<NSValue *> * _Nullable)boneInverseBindTransforms boneWeights:(SCNGeometrySource * _Nonnull)boneWeights boneIndices:(SCNGeometrySource * _Nonnull)boneIndices ``` |

#### SCNTechnique.h

Added [-[SCNTechnique objectForKeyedSubscript:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520493-objectforkeyedsubscript)Added [-[SCNTechnique setObject:forKeyedSubscript:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520495-setobject)Modified [SCNTechnique.dictionaryRepresentation](https://developer.apple.com/documentation/scenekit/scntechnique/1520492-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSDictionary *dictionaryRepresentation ``` |
| To | ``` @property(readonly, nonnull) NSDictionary<NSString *,id> *dictionaryRepresentation ``` |

Modified [-[SCNTechnique handleBindingOfSymbol:usingBlock:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520490-handlebindingofsymbol)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleBindingOfSymbol:(NSString *)symbol usingBlock:(SCNBindingBlock)block ``` |
| To | ``` - (void)handleBindingOfSymbol:(NSString * _Nonnull)symbol usingBlock:(SCNBindingBlock _Nullable)block ``` |

Modified [+[SCNTechnique techniqueBySequencingTechniques:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520497-techniquebysequencingtechniques)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNTechnique *)techniqueBySequencingTechniques:(NSArray *)techniques ``` |
| To | ``` + (SCNTechnique * _Nullable)techniqueBySequencingTechniques:(NSArray<SCNTechnique *> * _Nonnull)techniques ``` |

Modified [+[SCNTechnique techniqueWithDictionary:]](https://developer.apple.com/documentation/scenekit/scntechnique/1520494-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SCNTechnique *)techniqueWithDictionary:(NSDictionary *)dictionary ``` |
| To | ``` + (SCNTechnique * _Nullable)techniqueWithDictionary:(NSDictionary<NSString *,id> * _Nonnull)dictionary ``` |

Modified [SCNTechniqueSupport.technique](https://developer.apple.com/documentation/scenekit/scntechniquesupport/1520496-technique)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) SCNTechnique *technique ``` |
| To | ``` @property(nonatomic, copy, nullable) SCNTechnique *technique ``` |

#### SCNTransaction.h

Modified [+[SCNTransaction animationTimingFunction]](https://developer.apple.com/documentation/scenekit/scntransaction/1522614-animationtimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` + (CAMediaTimingFunction *)animationTimingFunction ``` |
| To | ``` + (CAMediaTimingFunction * _Nullable)animationTimingFunction ``` |

Modified [+[SCNTransaction completionBlock]](https://developer.apple.com/documentation/scenekit/scntransaction/1523660-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void (^)(void))completionBlock ``` |
| To | ``` + (void (^ _Nullable)(void))completionBlock ``` |

Modified +[SCNTransaction setAnimationTimingFunction:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction *)function ``` |
| To | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction * _Nullable)animationTimingFunction ``` |

Modified +[SCNTransaction setCompletionBlock:]

|  | Declaration |
| --- | --- |
| From | ``` + (void)setCompletionBlock:(void (^)(void))block ``` |
| To | ``` + (void)setCompletionBlock:(void (^ _Nullable)(void))block ``` |

Modified [+[SCNTransaction setValue:forKey:]](https://developer.apple.com/documentation/scenekit/scntransaction/1524124-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setValue:(id)anObject forKey:(NSString *)key ``` |
| To | ``` + (void)setValue:(id _Nullable)value forKey:(NSString * _Nonnull)key ``` |

Modified [+[SCNTransaction valueForKey:]](https://developer.apple.com/documentation/scenekit/scntransaction/1523919-valueforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)valueForKey:(NSString *)key ``` |
| To | ``` + (id _Nullable)valueForKey:(NSString * _Nonnull)key ``` |

#### SCNView.h

Added [SCNPreferLowPowerDeviceKey](https://developer.apple.com/documentation/scenekit/scnview/option/1522859-preferlowpowerdevice)Added [SCNPreferredDeviceKey](https://developer.apple.com/documentation/scenekit/scnview/option/1523209-preferreddevice)Added [SCNPreferredRenderingAPIKey](https://developer.apple.com/documentation/scenekit/scnpreferredrenderingapikey)Modified [SCNView.backgroundColor](https://developer.apple.com/documentation/scenekit/scnview/1523088-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSColor *backgroundColor ``` |
| To | ``` @property(nonatomic, copy, nonnull) NSColor *backgroundColor ``` |

Modified [-[SCNView initWithFrame:options:]](https://developer.apple.com/documentation/scenekit/scnview/1524215-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithFrame:(NSRect)frame options:(NSDictionary *)options ``` |
| To | ``` - (instancetype _Nonnull)initWithFrame:(NSRect)frame options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [SCNView.openGLContext](https://developer.apple.com/documentation/scenekit/scnview/1522850-openglcontext)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSOpenGLContext *openGLContext ``` |
| To | ``` @property(nonatomic, retain, nullable) NSOpenGLContext *openGLContext ``` |

Modified [-[SCNView pause:]](https://developer.apple.com/documentation/scenekit/scnview/1522825-pause)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)pause:(id)sender ``` |
| To | ``` - (IBAction)pause:(id _Nullable)sender ``` |

Modified [SCNView.pixelFormat](https://developer.apple.com/documentation/scenekit/scnview/1523612-pixelformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSOpenGLPixelFormat *pixelFormat ``` |
| To | ``` @property(nonatomic, retain, nullable) NSOpenGLPixelFormat *pixelFormat ``` |

Modified [-[SCNView play:]](https://developer.apple.com/documentation/scenekit/scnview/1523699-play)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)play:(id)sender ``` |
| To | ``` - (IBAction)play:(id _Nullable)sender ``` |

Modified [SCNView.scene](https://developer.apple.com/documentation/scenekit/scnview/1523904-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNScene *scene ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNScene *scene ``` |

Modified [-[SCNView snapshot]](https://developer.apple.com/documentation/scenekit/scnview/1524031-snapshot)

|  | Declaration |
| --- | --- |
| From | ``` - (NSImage *)snapshot ``` |
| To | ``` - (NSImage * _Nonnull)snapshot ``` |

Modified [-[SCNView stop:]](https://developer.apple.com/documentation/scenekit/scnview/1524132-stop)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)stop:(id)sender ``` |
| To | ``` - (IBAction)stop:(id _Nullable)sender ``` |

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
