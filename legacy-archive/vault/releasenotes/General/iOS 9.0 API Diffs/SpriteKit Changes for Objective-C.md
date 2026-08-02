---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/SpriteKit.html
archived_at: '2026-07-18T02:56:36.695867Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# SpriteKit Changes for Objective-C

### SpriteKit

#### SK3DNode.h

Modified [-[SK3DNode hitTest:options:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTest:(CGPoint)thePoint options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTest:(CGPoint)point options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

#### SKAction.h

Added [+[SKAction actionNamed:]](https://developer.apple.com/documentation/spritekit/skaction/1417814-init)Added [+[SKAction actionNamed:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417697-actionnamed)Added [+[SKAction actionNamed:fromURL:]](https://developer.apple.com/documentation/spritekit/skaction/1417680-init)Added [+[SKAction actionNamed:fromURL:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417754-init)Added [+[SKAction animateWithNormalTextures:timePerFrame:]](https://developer.apple.com/documentation/spritekit/skaction/1417746-animatewithnormaltextures)Added [+[SKAction animateWithNormalTextures:timePerFrame:resize:restore:]](https://developer.apple.com/documentation/spritekit/skaction/1417810-animate)Added [+[SKAction applyAngularImpulse:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417775-applyangularimpulse)Added [+[SKAction applyForce:atPoint:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417823-applyforce)Added [+[SKAction applyForce:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417782-applyforce)Added [+[SKAction applyImpulse:atPoint:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417732-applyimpulse)Added [+[SKAction applyImpulse:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417770-applyimpulse)Added [+[SKAction applyTorque:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417756-applytorque)Added [+[SKAction changeChargeBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417714-changechargeby)Added [+[SKAction changeChargeTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417752-changecharge)Added [+[SKAction changeMassBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417710-changemassby)Added [+[SKAction changeMassTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417780-changemass)Added [+[SKAction changePlaybackRateBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417670-changeplaybackrateby)Added [+[SKAction changePlaybackRateTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417808-changeplaybackrateto)Added [+[SKAction changeVolumeBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417726-changevolumeby)Added [+[SKAction changeVolumeTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417682-changevolumeto)Added [+[SKAction pause]](https://developer.apple.com/documentation/spritekit/skaction/1417820-pause)Added [+[SKAction play]](https://developer.apple.com/documentation/spritekit/skaction/1417730-play)Added [+[SKAction setNormalTexture:]](https://developer.apple.com/documentation/spritekit/skaction/1417706-setnormaltexture)Added [+[SKAction setNormalTexture:resize:]](https://developer.apple.com/documentation/spritekit/skaction/1417654-setnormaltexture)Added [+[SKAction stop]](https://developer.apple.com/documentation/spritekit/skaction/1417794-stop)Added SKAction(MixerControl)Added SKAction(NodeWithPhysicsBody)Added SKAction(PlaybackControl)Modified [+[SKAction animateWithTextures:timePerFrame:]](https://developer.apple.com/documentation/spritekit/skaction/1417828-animate)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)animateWithTextures:(NSArray *)textures timePerFrame:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)animateWithTextures:(NSArray<SKTexture *> * _Nonnull)textures timePerFrame:(NSTimeInterval)sec ``` |

Modified [+[SKAction animateWithTextures:timePerFrame:resize:restore:]](https://developer.apple.com/documentation/spritekit/skaction/1417656-animate)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)animateWithTextures:(NSArray *)textures timePerFrame:(NSTimeInterval)sec resize:(BOOL)resize restore:(BOOL)restore ``` |
| To | ``` + (SKAction * _Nonnull)animateWithTextures:(NSArray<SKTexture *> * _Nonnull)textures timePerFrame:(NSTimeInterval)sec resize:(BOOL)resize restore:(BOOL)restore ``` |

Modified [+[SKAction group:]](https://developer.apple.com/documentation/spritekit/skaction/1417688-group)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)group:(NSArray *)actions ``` |
| To | ``` + (SKAction * _Nonnull)group:(NSArray<SKAction *> * _Nonnull)actions ``` |

Modified [+[SKAction sequence:]](https://developer.apple.com/documentation/spritekit/skaction/1417817-sequence)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)sequence:(NSArray *)actions ``` |
| To | ``` + (SKAction * _Nonnull)sequence:(NSArray<SKAction *> * _Nonnull)actions ``` |

Modified [+[SKAction setTexture:]](https://developer.apple.com/documentation/spritekit/skaction/1417784-settexture)

|  | Introduction |
| --- | --- |
| From | iOS 7.0 |
| To | iOS 7.1 |

#### SKAudioNode.h (Added)

Added [+[SKAction changeObstructionBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520346-changeobstructionby)Added [+[SKAction changeObstructionTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519718-changeobstruction)Added [+[SKAction changeOcclusionBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520117-changeocclusion)Added [+[SKAction changeOcclusionTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520433-changeocclusion)Added [+[SKAction changeReverbBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519568-changereverb)Added [+[SKAction changeReverbTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520320-changereverbto)Added [+[SKAction stereoPanBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519713-stereopan)Added [+[SKAction stereoPanTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519976-stereopan)Added [SKAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode)Added [SKAudioNode.autoplayLooped](https://developer.apple.com/documentation/spritekit/skaudionode/1520336-autoplaylooped)Added [SKAudioNode.avAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode/1519633-avaudionode)Added [-[SKAudioNode initWithAVAudioNode:]](https://developer.apple.com/documentation/spritekit/skaudionode/1520232-init)Added [-[SKAudioNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skaudionode/1520341-initwithcoder)Added [-[SKAudioNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skaudionode/1519678-init)Added [-[SKAudioNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skaudionode/1519661-initwithurl)Added [SKAudioNode.positional](https://developer.apple.com/documentation/spritekit/skaudionode/1520418-ispositional)Added SKAction(SKAudioNode)

#### SKCameraNode.h (Added)

Added [SKCameraNode](https://developer.apple.com/documentation/spritekit/skcameranode)Added [-[SKCameraNode containedNodeSet]](https://developer.apple.com/documentation/spritekit/skcameranode/1434222-containednodeset)Added [-[SKCameraNode containsNode:]](https://developer.apple.com/documentation/spritekit/skcameranode/1434224-contains)

#### SKConstraint.h

Modified [SKConstraint.referenceNode](https://developer.apple.com/documentation/spritekit/skconstraint/1520369-referencenode)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) SKNode *referenceNode ``` |
| To | ``` @property(retain, nonatomic, nullable) SKNode *referenceNode ``` |

#### SKEmitterNode.h

Added [SKEmitterNode.particleRenderOrder](https://developer.apple.com/documentation/spritekit/skemitternode/1397986-particlerenderorder)Added [SKParticleRenderOrder](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)Added [SKParticleRenderOrderDontCare](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderdontcare)Added [SKParticleRenderOrderOldestFirst](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderoldestfirst)Added [SKParticleRenderOrderOldestLast](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderoldestlast)Modified [SKEmitterNode.particleZPositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397974-particlezpositionrange)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [SKEmitterNode.particleZPositionSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398008-particlezpositionspeed)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

#### SKKeyframeSequence.h

Modified [-[SKKeyframeSequence initWithKeyframeValues:times:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKeyframeValues:(NSArray *)values times:(NSArray *)times ``` |
| To | ``` - (instancetype _Nonnull)initWithKeyframeValues:(NSArray * _Nonnull)values times:(NSArray<NSNumber *> * _Nonnull)times ``` |

#### SKNode.h

Added [-[SKNode moveToParent:]](https://developer.apple.com/documentation/spritekit/sknode/1483021-movetoparent)Added [+[SKNode obstaclesFromNodeBounds:]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)Added [+[SKNode obstaclesFromNodePhysicsBodies:]](https://developer.apple.com/documentation/spritekit/sknode/1483085-obstaclesfromnodephysicsbodies)Added [+[SKNode obstaclesFromSpriteTextures:accuracy:]](https://developer.apple.com/documentation/spritekit/sknode/1483134-obstaclesfromspritetextures)Modified [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *children ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKNode *> *children ``` |

Modified [SKNode.constraints](https://developer.apple.com/documentation/spritekit/sknode/1483124-constraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *constraints ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SKConstraint *> *constraints ``` |

Modified [-[SKNode nodesAtPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483072-nodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)nodesAtPoint:(CGPoint)p ``` |
| To | ``` - (NSArray<SKNode *> * _Nonnull)nodesAtPoint:(CGPoint)p ``` |

Modified [-[SKNode objectForKeyedSubscript:]](https://developer.apple.com/documentation/spritekit/sknode/1483070-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectForKeyedSubscript:(NSString *)name ``` |
| To | ``` - (NSArray<SKNode *> * _Nonnull)objectForKeyedSubscript:(NSString * _Nonnull)name ``` |

Modified [-[SKNode removeChildrenInArray:]](https://developer.apple.com/documentation/spritekit/sknode/1483091-removechildreninarray)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeChildrenInArray:(NSArray *)nodes ``` |
| To | ``` - (void)removeChildrenInArray:(NSArray<SKNode *> * _Nonnull)nodes ``` |

#### SKPhysicsBody.h

Modified [-[SKPhysicsBody allContactedBodies]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520397-allcontactedbodies)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)allContactedBodies ``` |
| To | ``` - (NSArray<SKPhysicsBody *> * _Nonnull)allContactedBodies ``` |

Modified [+[SKPhysicsBody bodyWithBodies:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519736-bodywithbodies)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithBodies:(NSArray *)bodies ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithBodies:(NSArray<SKPhysicsBody *> * _Nonnull)bodies ``` |

Modified [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *joints ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKPhysicsJoint *> *joints ``` |

#### SKReferenceNode.h (Added)

Added [SKReferenceNode](https://developer.apple.com/documentation/spritekit/skreferencenode)Added [-[SKReferenceNode didLoadReferenceNode:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508364-didload)Added [-[SKReferenceNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508363-init)Added [-[SKReferenceNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508369-init)Added [-[SKReferenceNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508366-initwithurl)Added [+[SKReferenceNode referenceNodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508368-init)Added [+[SKReferenceNode referenceNodeWithURL:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508365-init)Added [-[SKReferenceNode resolveReferenceNode]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508371-resolvereferencenode)

#### SKScene.h

Added [SKScene.audioEngine](https://developer.apple.com/documentation/spritekit/skscene/1519644-audioengine)Added [SKScene.camera](https://developer.apple.com/documentation/spritekit/skscene/1519696-camera)Added [SKScene.listener](https://developer.apple.com/documentation/spritekit/skscene/1520363-listener)

#### SKShader.h

Modified [-[SKShader initWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477555-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source uniforms:(NSArray *)uniforms ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source uniforms:(NSArray<SKUniform *> * _Nonnull)uniforms ``` |

Modified [+[SKShader shaderWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477569-shaderwithsource)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shaderWithSource:(NSString *)source uniforms:(NSArray *)uniforms ``` |
| To | ``` + (instancetype _Nonnull)shaderWithSource:(NSString * _Nonnull)source uniforms:(NSArray<SKUniform *> * _Nonnull)uniforms ``` |

Modified [SKShader.uniforms](https://developer.apple.com/documentation/spritekit/skshader/1477565-uniforms)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *uniforms ``` |
| To | ``` @property(copy, nonnull) NSArray<SKUniform *> *uniforms ``` |

#### SKTexture.h

Added [SKTexture.CGImage](https://developer.apple.com/documentation/spritekit/sktexture/1519755-cgimage)Modified [+[SKTexture preloadTextures:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktexture/1519817-preloadtextures)

|  | Declaration |
| --- | --- |
| From | ``` + (void)preloadTextures:(NSArray *)textures withCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)preloadTextures:(NSArray<SKTexture *> * _Nonnull)textures withCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

#### SKTextureAtlas.h

Added [+[SKTextureAtlas preloadTextureAtlasesNamed:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427377-preloadtextureatlasesnamed)Modified [+[SKTextureAtlas atlasWithDictionary:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)atlasWithDictionary:(NSDictionary *)properties ``` |
| To | ``` + (instancetype _Nonnull)atlasWithDictionary:(NSDictionary<NSString *,id> * _Nonnull)properties ``` |

Modified [+[SKTextureAtlas preloadTextureAtlases:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427379-preloadtextureatlases)

|  | Declaration |
| --- | --- |
| From | ``` + (void)preloadTextureAtlases:(NSArray *)textureAtlases withCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)preloadTextureAtlases:(NSArray<SKTextureAtlas *> * _Nonnull)textureAtlases withCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [SKTextureAtlas.textureNames](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427373-texturenames)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *textureNames ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *textureNames ``` |

#### SKTransition.h

Modified [SKTransition](https://developer.apple.com/documentation/spritekit/sktransition)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCopying |

#### SKUniform.h

Modified [SKUniform.name](https://developer.apple.com/documentation/spritekit/skuniform/1455442-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *name ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSString *name ``` |

Modified [SKUniform.textureValue](https://developer.apple.com/documentation/spritekit/skuniform/1455449-texturevalue)

|  | Declaration |
| --- | --- |
| From | ``` @property SKTexture *textureValue ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *textureValue ``` |

Modified [SKUniform.uniformType](https://developer.apple.com/documentation/spritekit/skuniform/1455440-uniformtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) SKUniformType uniformType ``` |
| To | ``` @property(nonatomic, readonly) SKUniformType uniformType ``` |

#### SKVersion.h (Added)

Added #def SK_VERSION

#### SKVideoNode.h

Added [-[SKVideoNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407922-init)Added [-[SKVideoNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407898-init)Added [+[SKVideoNode videoNodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407924-videonodewithfilenamed)Added [+[SKVideoNode videoNodeWithURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407902-videonodewithurl)Modified [-[SKVideoNode initWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407918-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[SKVideoNode initWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-initwithvideourl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [+[SKVideoNode videoNodeWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407914-videonodewithvideofilenamed)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [+[SKVideoNode videoNodeWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407906-videonodewithvideourl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

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
