---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/SpriteKit.html
archived_at: '2026-07-18T02:53:13.751098Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# SpriteKit Changes for Objective-C

### SpriteKit

#### SK3DNode.h

Modified [-[SK3DNode hitTest:options:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519782-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)hitTest:(CGPoint)thePoint options:(NSDictionary *)options ``` |
| To | ``` - (NSArray<SCNHitTestResult *> * _Nonnull)hitTest:(CGPoint)point options:(NSDictionary<NSString *,id> * _Nullable)options ``` |

Modified [-[SK3DNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519722-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[SK3DNode initWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1519708-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithViewportSize:(CGSize)viewportSize ``` |
| To | ``` - (instancetype _Nonnull)initWithViewportSize:(CGSize)viewportSize ``` |

Modified [+[SK3DNode nodeWithViewportSize:]](https://developer.apple.com/documentation/spritekit/sk3dnode/1537481-nodewithviewportsize)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)nodeWithViewportSize:(CGSize)viewportSize ``` |
| To | ``` + (instancetype _Nonnull)nodeWithViewportSize:(CGSize)viewportSize ``` |

Modified [SK3DNode.pointOfView](https://developer.apple.com/documentation/spritekit/sk3dnode/1519786-pointofview)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNNode *pointOfView ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNNode *pointOfView ``` |

Modified [SK3DNode.scnScene](https://developer.apple.com/documentation/spritekit/sk3dnode/1519834-scnscene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SCNScene *scnScene ``` |
| To | ``` @property(nonatomic, retain, nullable) SCNScene *scnScene ``` |

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

Modified [+[SKAction colorizeWithColor:colorBlendFactor:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417678-colorizewithcolor)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)colorizeWithColor:(NSColor *)color colorBlendFactor:(CGFloat)colorBlendFactor duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)colorizeWithColor:(NSColor * _Nonnull)color colorBlendFactor:(CGFloat)colorBlendFactor duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction colorizeWithColorBlendFactor:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417736-colorize)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)colorizeWithColorBlendFactor:(CGFloat)colorBlendFactor duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)colorizeWithColorBlendFactor:(CGFloat)colorBlendFactor duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction customActionWithDuration:actionBlock:]](https://developer.apple.com/documentation/spritekit/skaction/1417745-customactionwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)customActionWithDuration:(NSTimeInterval)seconds actionBlock:(void (^)(SKNode *node, CGFloat elapsedTime))block ``` |
| To | ``` + (SKAction * _Nonnull)customActionWithDuration:(NSTimeInterval)seconds actionBlock:(void (^ _Nonnull)(SKNode * _Nonnull node, CGFloat elapsedTime))block ``` |

Modified [+[SKAction fadeAlphaBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417716-fadealphaby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)fadeAlphaBy:(CGFloat)factor duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)fadeAlphaBy:(CGFloat)factor duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction fadeAlphaTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417673-fadealphato)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)fadeAlphaTo:(CGFloat)alpha duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)fadeAlphaTo:(CGFloat)alpha duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction fadeInWithDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417818-fadein)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)fadeInWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)fadeInWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKAction fadeOutWithDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417738-fadeoutwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)fadeOutWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)fadeOutWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKAction falloffBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417766-falloffby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)falloffBy:(float)falloff duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)falloffBy:(float)falloff duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction falloffTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417758-falloff)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)falloffTo:(float)falloff duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)falloffTo:(float)falloff duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction followPath:asOffset:orientToPath:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417662-followpath)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)followPath:(CGPathRef)path asOffset:(BOOL)offset orientToPath:(BOOL)orient duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)followPath:(CGPathRef _Nonnull)path asOffset:(BOOL)offset orientToPath:(BOOL)orient duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction followPath:asOffset:orientToPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417798-followpath)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)followPath:(CGPathRef)path asOffset:(BOOL)offset orientToPath:(BOOL)orient speed:(CGFloat)speed ``` |
| To | ``` + (SKAction * _Nonnull)followPath:(CGPathRef _Nonnull)path asOffset:(BOOL)offset orientToPath:(BOOL)orient speed:(CGFloat)speed ``` |

Modified [+[SKAction followPath:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417822-follow)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)followPath:(CGPathRef)path duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)followPath:(CGPathRef _Nonnull)path duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction followPath:speed:]](https://developer.apple.com/documentation/spritekit/skaction/1417786-follow)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)followPath:(CGPathRef)path speed:(CGFloat)speed ``` |
| To | ``` + (SKAction * _Nonnull)followPath:(CGPathRef _Nonnull)path speed:(CGFloat)speed ``` |

Modified [+[SKAction group:]](https://developer.apple.com/documentation/spritekit/skaction/1417688-group)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)group:(NSArray *)actions ``` |
| To | ``` + (SKAction * _Nonnull)group:(NSArray<SKAction *> * _Nonnull)actions ``` |

Modified [+[SKAction hide]](https://developer.apple.com/documentation/spritekit/skaction/1417704-hide)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)hide ``` |
| To | ``` + (SKAction * _Nonnull)hide ``` |

Modified [+[SKAction moveBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417739-moveby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)moveBy:(CGVector)delta duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)moveBy:(CGVector)delta duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction moveByX:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417722-movebyx)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)moveByX:(CGFloat)deltaX y:(CGFloat)deltaY duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)moveByX:(CGFloat)deltaX y:(CGFloat)deltaY duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction moveTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417768-moveto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)moveTo:(CGPoint)location duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)moveTo:(CGPoint)location duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction moveToX:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417779-moveto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)moveToX:(CGFloat)x duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)moveToX:(CGFloat)x duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction moveToY:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417781-movetoy)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)moveToY:(CGFloat)y duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)moveToY:(CGFloat)y duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction performSelector:onTarget:]](https://developer.apple.com/documentation/spritekit/skaction/1417764-perform)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)performSelector:(SEL)selector onTarget:(id)target ``` |
| To | ``` + (SKAction * _Nonnull)performSelector:(SEL _Nonnull)selector onTarget:(id _Nonnull)target ``` |

Modified [+[SKAction playSoundFileNamed:waitForCompletion:]](https://developer.apple.com/documentation/spritekit/skaction/1417664-playsoundfilenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)playSoundFileNamed:(NSString *)soundFile waitForCompletion:(BOOL)wait ``` |
| To | ``` + (SKAction * _Nonnull)playSoundFileNamed:(NSString * _Nonnull)soundFile waitForCompletion:(BOOL)wait ``` |

Modified [+[SKAction reachTo:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417773-reachto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)reachTo:(CGPoint)position rootNode:(SKNode *)root duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)reachTo:(CGPoint)position rootNode:(SKNode * _Nonnull)root duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction reachTo:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417720-reachto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)reachTo:(CGPoint)position rootNode:(SKNode *)root velocity:(CGFloat)velocity ``` |
| To | ``` + (SKAction * _Nonnull)reachTo:(CGPoint)position rootNode:(SKNode * _Nonnull)root velocity:(CGFloat)velocity ``` |

Modified [+[SKAction reachToNode:rootNode:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417827-reachtonode)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)reachToNode:(SKNode *)node rootNode:(SKNode *)root duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)reachToNode:(SKNode * _Nonnull)node rootNode:(SKNode * _Nonnull)root duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction reachToNode:rootNode:velocity:]](https://developer.apple.com/documentation/spritekit/skaction/1417801-reach)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)reachToNode:(SKNode *)node rootNode:(SKNode *)root velocity:(CGFloat)velocity ``` |
| To | ``` + (SKAction * _Nonnull)reachToNode:(SKNode * _Nonnull)node rootNode:(SKNode * _Nonnull)root velocity:(CGFloat)velocity ``` |

Modified [+[SKAction removeFromParent]](https://developer.apple.com/documentation/spritekit/skaction/1417748-removefromparent)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)removeFromParent ``` |
| To | ``` + (SKAction * _Nonnull)removeFromParent ``` |

Modified [+[SKAction repeatAction:count:]](https://developer.apple.com/documentation/spritekit/skaction/1417750-repeat)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)repeatAction:(SKAction *)action count:(NSUInteger)count ``` |
| To | ``` + (SKAction * _Nonnull)repeatAction:(SKAction * _Nonnull)action count:(NSUInteger)count ``` |

Modified [+[SKAction repeatActionForever:]](https://developer.apple.com/documentation/spritekit/skaction/1417676-repeatforever)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)repeatActionForever:(SKAction *)action ``` |
| To | ``` + (SKAction * _Nonnull)repeatActionForever:(SKAction * _Nonnull)action ``` |

Modified [+[SKAction resizeByWidth:height:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417812-resize)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)resizeByWidth:(CGFloat)width height:(CGFloat)height duration:(NSTimeInterval)duration ``` |
| To | ``` + (SKAction * _Nonnull)resizeByWidth:(CGFloat)width height:(CGFloat)height duration:(NSTimeInterval)duration ``` |

Modified [+[SKAction resizeToHeight:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417825-resizetoheight)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)resizeToHeight:(CGFloat)height duration:(NSTimeInterval)duration ``` |
| To | ``` + (SKAction * _Nonnull)resizeToHeight:(CGFloat)height duration:(NSTimeInterval)duration ``` |

Modified [+[SKAction resizeToWidth:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417686-resizetowidth)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)resizeToWidth:(CGFloat)width duration:(NSTimeInterval)duration ``` |
| To | ``` + (SKAction * _Nonnull)resizeToWidth:(CGFloat)width duration:(NSTimeInterval)duration ``` |

Modified [+[SKAction resizeToWidth:height:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417724-resizetowidth)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)resizeToWidth:(CGFloat)width height:(CGFloat)height duration:(NSTimeInterval)duration ``` |
| To | ``` + (SKAction * _Nonnull)resizeToWidth:(CGFloat)width height:(CGFloat)height duration:(NSTimeInterval)duration ``` |

Modified [-[SKAction reversedAction]](https://developer.apple.com/documentation/spritekit/skaction/1417803-reversedaction)

|  | Declaration |
| --- | --- |
| From | ``` - (SKAction *)reversedAction ``` |
| To | ``` - (SKAction * _Nonnull)reversedAction ``` |

Modified [+[SKAction rotateByAngle:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417805-rotate)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)rotateByAngle:(CGFloat)radians duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)rotateByAngle:(CGFloat)radians duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction rotateToAngle:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417668-rotatetoangle)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)rotateToAngle:(CGFloat)radians duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)rotateToAngle:(CGFloat)radians duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction rotateToAngle:duration:shortestUnitArc:]](https://developer.apple.com/documentation/spritekit/skaction/1417700-rotatetoangle)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)rotateToAngle:(CGFloat)radians duration:(NSTimeInterval)sec shortestUnitArc:(BOOL)shortestUnitArc ``` |
| To | ``` + (SKAction * _Nonnull)rotateToAngle:(CGFloat)radians duration:(NSTimeInterval)sec shortestUnitArc:(BOOL)shortestUnitArc ``` |

Modified [+[SKAction runAction:onChildWithName:]](https://developer.apple.com/documentation/spritekit/skaction/1417671-run)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)runAction:(SKAction *)action onChildWithName:(NSString *)name ``` |
| To | ``` + (SKAction * _Nonnull)runAction:(SKAction * _Nonnull)action onChildWithName:(NSString * _Nonnull)name ``` |

Modified [+[SKAction runBlock:]](https://developer.apple.com/documentation/spritekit/skaction/1417692-run)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)runBlock:(dispatch_block_t)block ``` |
| To | ``` + (SKAction * _Nonnull)runBlock:(dispatch_block_t _Nonnull)block ``` |

Modified [+[SKAction runBlock:queue:]](https://developer.apple.com/documentation/spritekit/skaction/1417799-runblock)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)runBlock:(dispatch_block_t)block queue:(dispatch_queue_t)queue ``` |
| To | ``` + (SKAction * _Nonnull)runBlock:(dispatch_block_t _Nonnull)block queue:(dispatch_queue_t _Nonnull)queue ``` |

Modified [+[SKAction scaleBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417741-scaleby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleBy:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleBy:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction scaleTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417712-scale)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction scaleXBy:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417796-scalexby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleXBy:(CGFloat)xScale y:(CGFloat)yScale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleXBy:(CGFloat)xScale y:(CGFloat)yScale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction scaleXTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417699-scalex)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleXTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleXTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction scaleXTo:y:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417728-scalexto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleXTo:(CGFloat)xScale y:(CGFloat)yScale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleXTo:(CGFloat)xScale y:(CGFloat)yScale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction scaleYTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417708-scaley)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)scaleYTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)scaleYTo:(CGFloat)scale duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction sequence:]](https://developer.apple.com/documentation/spritekit/skaction/1417817-sequence)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)sequence:(NSArray *)actions ``` |
| To | ``` + (SKAction * _Nonnull)sequence:(NSArray<SKAction *> * _Nonnull)actions ``` |

Modified [+[SKAction setTexture:]](https://developer.apple.com/documentation/spritekit/skaction/1417784-settexture)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` + (SKAction *)setTexture:(SKTexture *)texture ``` | OS X 10.9 |
| To | ``` + (SKAction * _Nonnull)setTexture:(SKTexture * _Nonnull)texture ``` | OS X 10.10 |

Modified [+[SKAction setTexture:resize:]](https://developer.apple.com/documentation/spritekit/skaction/1417743-settexture)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)setTexture:(SKTexture *)texture resize:(BOOL)resize ``` |
| To | ``` + (SKAction * _Nonnull)setTexture:(SKTexture * _Nonnull)texture resize:(BOOL)resize ``` |

Modified [+[SKAction speedBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417690-speedby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)speedBy:(CGFloat)speed duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)speedBy:(CGFloat)speed duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction speedTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417684-speedto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)speedTo:(CGFloat)speed duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)speedTo:(CGFloat)speed duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction strengthBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417762-strengthby)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)strengthBy:(float)strength duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)strengthBy:(float)strength duration:(NSTimeInterval)sec ``` |

Modified [+[SKAction strengthTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1417815-strengthto)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)strengthTo:(float)strength duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)strengthTo:(float)strength duration:(NSTimeInterval)sec ``` |

Modified [SKAction.timingFunction](https://developer.apple.com/documentation/spritekit/skaction/1417666-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) SKActionTimingFunction timingFunction ``` |
| To | ``` @property(nonatomic, nonnull) SKActionTimingFunction timingFunction ``` |

Modified [+[SKAction unhide]](https://developer.apple.com/documentation/spritekit/skaction/1417660-unhide)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)unhide ``` |
| To | ``` + (SKAction * _Nonnull)unhide ``` |

Modified [+[SKAction waitForDuration:]](https://developer.apple.com/documentation/spritekit/skaction/1417788-wait)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)waitForDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKAction * _Nonnull)waitForDuration:(NSTimeInterval)sec ``` |

Modified [+[SKAction waitForDuration:withRange:]](https://developer.apple.com/documentation/spritekit/skaction/1417760-waitforduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKAction *)waitForDuration:(NSTimeInterval)sec withRange:(NSTimeInterval)durationRange ``` |
| To | ``` + (SKAction * _Nonnull)waitForDuration:(NSTimeInterval)sec withRange:(NSTimeInterval)durationRange ``` |

#### SKAudioNode.h (Added)

Added [+[SKAction changeObstructionBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520346-changeobstructionby)Added [+[SKAction changeObstructionTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519718-changeobstruction)Added [+[SKAction changeOcclusionBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520117-changeocclusion)Added [+[SKAction changeOcclusionTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520433-changeocclusion)Added [+[SKAction changeReverbBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519568-changereverb)Added [+[SKAction changeReverbTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1520320-changereverbto)Added [+[SKAction stereoPanBy:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519713-stereopan)Added [+[SKAction stereoPanTo:duration:]](https://developer.apple.com/documentation/spritekit/skaction/1519976-stereopan)Added [SKAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode)Added [SKAudioNode.autoplayLooped](https://developer.apple.com/documentation/spritekit/skaudionode/1520336-autoplaylooped)Added [SKAudioNode.avAudioNode](https://developer.apple.com/documentation/spritekit/skaudionode/1519633-avaudionode)Added [-[SKAudioNode initWithAVAudioNode:]](https://developer.apple.com/documentation/spritekit/skaudionode/1520232-init)Added [-[SKAudioNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skaudionode/1520341-initwithcoder)Added [-[SKAudioNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skaudionode/1519678-init)Added [-[SKAudioNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skaudionode/1519661-initwithurl)Added [SKAudioNode.positional](https://developer.apple.com/documentation/spritekit/skaudionode/1520418-ispositional)Added SKAction(SKAudioNode)

#### SKCameraNode.h (Added)

Added [SKCameraNode](https://developer.apple.com/documentation/spritekit/skcameranode)Added [-[SKCameraNode containedNodeSet]](https://developer.apple.com/documentation/spritekit/skcameranode/1434222-containednodeset)Added [-[SKCameraNode containsNode:]](https://developer.apple.com/documentation/spritekit/skcameranode/1434224-contains)

#### SKConstraint.h

Modified [+[SKConstraint distance:toNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519750-distance)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)distance:(SKRange *)range toNode:(SKNode *)node ``` |
| To | ``` + (instancetype _Nonnull)distance:(SKRange * _Nonnull)range toNode:(SKNode * _Nonnull)node ``` |

Modified [+[SKConstraint distance:toPoint:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519688-distance)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)distance:(SKRange *)range toPoint:(CGPoint)point ``` |
| To | ``` + (instancetype _Nonnull)distance:(SKRange * _Nonnull)range toPoint:(CGPoint)point ``` |

Modified [+[SKConstraint distance:toPoint:inNode:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519746-distance)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)distance:(SKRange *)range toPoint:(CGPoint)point inNode:(SKNode *)node ``` |
| To | ``` + (instancetype _Nonnull)distance:(SKRange * _Nonnull)range toPoint:(CGPoint)point inNode:(SKNode * _Nonnull)node ``` |

Modified [+[SKConstraint orientToNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519744-orienttonode)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orientToNode:(SKNode *)node offset:(SKRange *)radians ``` |
| To | ``` + (instancetype _Nonnull)orientToNode:(SKNode * _Nonnull)node offset:(SKRange * _Nonnull)radians ``` |

Modified [+[SKConstraint orientToPoint:inNode:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519627-orienttopoint)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orientToPoint:(CGPoint)point inNode:(SKNode *)node offset:(SKRange *)radians ``` |
| To | ``` + (instancetype _Nonnull)orientToPoint:(CGPoint)point inNode:(SKNode * _Nonnull)node offset:(SKRange * _Nonnull)radians ``` |

Modified [+[SKConstraint orientToPoint:offset:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519686-orienttopoint)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)orientToPoint:(CGPoint)point offset:(SKRange *)radians ``` |
| To | ``` + (instancetype _Nonnull)orientToPoint:(CGPoint)point offset:(SKRange * _Nonnull)radians ``` |

Modified [+[SKConstraint positionX:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519716-positionx)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)positionX:(SKRange *)range ``` |
| To | ``` + (instancetype _Nonnull)positionX:(SKRange * _Nonnull)range ``` |

Modified [+[SKConstraint positionX:Y:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519760-positionx)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)positionX:(SKRange *)xRange Y:(SKRange *)yRange ``` |
| To | ``` + (instancetype _Nonnull)positionX:(SKRange * _Nonnull)xRange Y:(SKRange * _Nonnull)yRange ``` |

Modified [+[SKConstraint positionY:]](https://developer.apple.com/documentation/spritekit/skconstraint/1520356-positiony)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)positionY:(SKRange *)range ``` |
| To | ``` + (instancetype _Nonnull)positionY:(SKRange * _Nonnull)range ``` |

Modified [SKConstraint.referenceNode](https://developer.apple.com/documentation/spritekit/skconstraint/1520369-referencenode)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) SKNode *referenceNode ``` |
| To | ``` @property(retain, nonatomic, nullable) SKNode *referenceNode ``` |

Modified [+[SKConstraint zRotation:]](https://developer.apple.com/documentation/spritekit/skconstraint/1519706-zrotation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)zRotation:(SKRange *)zRange ``` |
| To | ``` + (instancetype _Nonnull)zRotation:(SKRange * _Nonnull)zRange ``` |

Modified [-[SKRange initWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520307-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLowerLimit:(CGFloat)lower upperLimit:(CGFloat)upper ``` |
| To | ``` - (instancetype _Nonnull)initWithLowerLimit:(CGFloat)lower upperLimit:(CGFloat)upper ``` |

Modified [+[SKRange rangeWithConstantValue:]](https://developer.apple.com/documentation/spritekit/skrange/1520276-rangewithconstantvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithConstantValue:(CGFloat)value ``` |
| To | ``` + (instancetype _Nonnull)rangeWithConstantValue:(CGFloat)value ``` |

Modified [+[SKRange rangeWithLowerLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1520137-rangewithlowerlimit)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithLowerLimit:(CGFloat)lower ``` |
| To | ``` + (instancetype _Nonnull)rangeWithLowerLimit:(CGFloat)lower ``` |

Modified [+[SKRange rangeWithLowerLimit:upperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1534324-rangewithlowerlimit)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithLowerLimit:(CGFloat)lower upperLimit:(CGFloat)upper ``` |
| To | ``` + (instancetype _Nonnull)rangeWithLowerLimit:(CGFloat)lower upperLimit:(CGFloat)upper ``` |

Modified [+[SKRange rangeWithNoLimits]](https://developer.apple.com/documentation/spritekit/skrange/1519920-withnolimits)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithNoLimits ``` |
| To | ``` + (instancetype _Nonnull)rangeWithNoLimits ``` |

Modified [+[SKRange rangeWithUpperLimit:]](https://developer.apple.com/documentation/spritekit/skrange/1519559-rangewithupperlimit)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithUpperLimit:(CGFloat)upper ``` |
| To | ``` + (instancetype _Nonnull)rangeWithUpperLimit:(CGFloat)upper ``` |

Modified [+[SKRange rangeWithValue:variance:]](https://developer.apple.com/documentation/spritekit/skrange/1519842-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)rangeWithValue:(CGFloat)value variance:(CGFloat)variance ``` |
| To | ``` + (instancetype _Nonnull)rangeWithValue:(CGFloat)value variance:(CGFloat)variance ``` |

#### SKCropNode.h

Modified [SKCropNode.maskNode](https://developer.apple.com/documentation/spritekit/skcropnode/1520449-masknode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKNode *maskNode ``` |
| To | ``` @property(nonatomic, retain, nullable) SKNode *maskNode ``` |

#### SKEffectNode.h

Modified [SKEffectNode.filter](https://developer.apple.com/documentation/spritekit/skeffectnode/1459392-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) CIFilter *filter ``` |
| To | ``` @property(nonatomic, retain, nullable) CIFilter *filter ``` |

Modified [SKEffectNode.shader](https://developer.apple.com/documentation/spritekit/skeffectnode/1459388-shader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKShader *shader ``` |
| To | ``` @property(nonatomic, retain, nullable) SKShader *shader ``` |

#### SKEmitterNode.h

Added [SKEmitterNode.particleRenderOrder](https://developer.apple.com/documentation/spritekit/skemitternode/1397986-particlerenderorder)Added [SKParticleRenderOrder](https://developer.apple.com/documentation/spritekit/skparticlerenderorder)Added [SKParticleRenderOrderDontCare](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderdontcare)Added [SKParticleRenderOrderOldestFirst](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderoldestfirst)Added [SKParticleRenderOrderOldestLast](https://developer.apple.com/documentation/spritekit/skparticlerenderorder/skparticlerenderorderoldestlast)Modified [SKEmitterNode.particleAction](https://developer.apple.com/documentation/spritekit/skemitternode/1397970-particleaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) SKAction *particleAction ``` |
| To | ``` @property(nonatomic, copy, nullable) SKAction *particleAction ``` |

Modified [SKEmitterNode.particleAlphaSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398057-particlealphasequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKKeyframeSequence *particleAlphaSequence ``` |
| To | ``` @property(nonatomic, retain, nullable) SKKeyframeSequence *particleAlphaSequence ``` |

Modified [SKEmitterNode.particleColor](https://developer.apple.com/documentation/spritekit/skemitternode/1398049-particlecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *particleColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *particleColor ``` |

Modified [SKEmitterNode.particleColorBlendFactorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397980-particlecolorblendfactorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorBlendFactorSequence ``` |
| To | ``` @property(nonatomic, retain, nullable) SKKeyframeSequence *particleColorBlendFactorSequence ``` |

Modified [SKEmitterNode.particleColorSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1397992-particlecolorsequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKKeyframeSequence *particleColorSequence ``` |
| To | ``` @property(nonatomic, retain, nullable) SKKeyframeSequence *particleColorSequence ``` |

Modified [SKEmitterNode.particleScaleSequence](https://developer.apple.com/documentation/spritekit/skemitternode/1398029-particlescalesequence)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKKeyframeSequence *particleScaleSequence ``` |
| To | ``` @property(nonatomic, retain, nullable) SKKeyframeSequence *particleScaleSequence ``` |

Modified [SKEmitterNode.particleTexture](https://developer.apple.com/documentation/spritekit/skemitternode/1398004-particletexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *particleTexture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *particleTexture ``` |

Modified [SKEmitterNode.particleZPositionRange](https://developer.apple.com/documentation/spritekit/skemitternode/1397974-particlezpositionrange)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [SKEmitterNode.particleZPositionSpeed](https://developer.apple.com/documentation/spritekit/skemitternode/1398008-particlezpositionspeed)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [SKEmitterNode.shader](https://developer.apple.com/documentation/spritekit/skemitternode/1398069-shader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKShader *shader ``` |
| To | ``` @property(nonatomic, retain, nullable) SKShader *shader ``` |

Modified [SKEmitterNode.targetNode](https://developer.apple.com/documentation/spritekit/skemitternode/1398012-targetnode)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak) SKNode *targetNode ``` |
| To | ``` @property(nonatomic, weak, nullable) SKNode *targetNode ``` |

#### SKFieldNode.h

Modified [+[SKFieldNode customFieldWithEvaluationBlock:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519710-customfieldwithevaluationblock)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)customFieldWithEvaluationBlock:(SKFieldForceEvaluator)block ``` |
| To | ``` + (SKFieldNode * _Nonnull)customFieldWithEvaluationBlock:(SKFieldForceEvaluator _Nonnull)block ``` |

Modified [+[SKFieldNode dragField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520225-dragfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)dragField ``` |
| To | ``` + (SKFieldNode * _Nonnull)dragField ``` |

Modified [+[SKFieldNode electricField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520396-electricfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)electricField ``` |
| To | ``` + (SKFieldNode * _Nonnull)electricField ``` |

Modified [+[SKFieldNode linearGravityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520145-lineargravityfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)linearGravityFieldWithVector:(vector_float3)direction ``` |
| To | ``` + (SKFieldNode * _Nonnull)linearGravityFieldWithVector:(vector_float3)direction ``` |

Modified [+[SKFieldNode magneticField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520134-magneticfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)magneticField ``` |
| To | ``` + (SKFieldNode * _Nonnull)magneticField ``` |

Modified [+[SKFieldNode noiseFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519947-noisefieldwithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)noiseFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |
| To | ``` + (SKFieldNode * _Nonnull)noiseFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |

Modified [+[SKFieldNode radialGravityField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520382-radialgravityfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)radialGravityField ``` |
| To | ``` + (SKFieldNode * _Nonnull)radialGravityField ``` |

Modified [SKFieldNode.region](https://developer.apple.com/documentation/spritekit/skfieldnode/1519551-region)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKRegion *region ``` |
| To | ``` @property(nonatomic, retain, nullable) SKRegion *region ``` |

Modified [+[SKFieldNode springField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519694-springfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)springField ``` |
| To | ``` + (SKFieldNode * _Nonnull)springField ``` |

Modified [SKFieldNode.texture](https://developer.apple.com/documentation/spritekit/skfieldnode/1519928-texture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *texture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *texture ``` |

Modified [+[SKFieldNode turbulenceFieldWithSmoothness:animationSpeed:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520018-turbulencefieldwithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)turbulenceFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |
| To | ``` + (SKFieldNode * _Nonnull)turbulenceFieldWithSmoothness:(CGFloat)smoothness animationSpeed:(CGFloat)speed ``` |

Modified [+[SKFieldNode velocityFieldWithTexture:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1519778-velocityfieldwithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)velocityFieldWithTexture:(SKTexture *)velocityTexture ``` |
| To | ``` + (SKFieldNode * _Nonnull)velocityFieldWithTexture:(SKTexture * _Nonnull)velocityTexture ``` |

Modified [+[SKFieldNode velocityFieldWithVector:]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520271-velocityfieldwithvector)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)velocityFieldWithVector:(vector_float3)direction ``` |
| To | ``` + (SKFieldNode * _Nonnull)velocityFieldWithVector:(vector_float3)direction ``` |

Modified [+[SKFieldNode vortexField]](https://developer.apple.com/documentation/spritekit/skfieldnode/1520157-vortexfield)

|  | Declaration |
| --- | --- |
| From | ``` + (SKFieldNode *)vortexField ``` |
| To | ``` + (SKFieldNode * _Nonnull)vortexField ``` |

#### SKKeyframeSequence.h

Modified [-[SKKeyframeSequence addKeyframeValue:time:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390894-addkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addKeyframeValue:(id)value time:(CGFloat)time ``` |
| To | ``` - (void)addKeyframeValue:(id _Nonnull)value time:(CGFloat)time ``` |

Modified [-[SKKeyframeSequence getKeyframeValueForIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390898-getkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (id)getKeyframeValueForIndex:(NSUInteger)index ``` |
| To | ``` - (id _Nonnull)getKeyframeValueForIndex:(NSUInteger)index ``` |

Modified [-[SKKeyframeSequence initWithCapacity:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390910-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCapacity:(NSUInteger)numItems ``` |
| To | ``` - (instancetype _Nonnull)initWithCapacity:(NSUInteger)numItems ``` |

Modified [-[SKKeyframeSequence initWithCoder:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390892-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[SKKeyframeSequence initWithKeyframeValues:times:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390896-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithKeyframeValues:(NSArray *)values times:(NSArray *)times ``` |
| To | ``` - (instancetype _Nonnull)initWithKeyframeValues:(NSArray * _Nonnull)values times:(NSArray<NSNumber *> * _Nonnull)times ``` |

Modified [-[SKKeyframeSequence sampleAtTime:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390904-sample)

|  | Declaration |
| --- | --- |
| From | ``` - (id)sampleAtTime:(CGFloat)time ``` |
| To | ``` - (id _Nullable)sampleAtTime:(CGFloat)time ``` |

Modified [-[SKKeyframeSequence setKeyframeValue:forIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390883-setkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setKeyframeValue:(id)value forIndex:(NSUInteger)index ``` |
| To | ``` - (void)setKeyframeValue:(id _Nonnull)value forIndex:(NSUInteger)index ``` |

Modified [-[SKKeyframeSequence setKeyframeValue:time:forIndex:]](https://developer.apple.com/documentation/spritekit/skkeyframesequence/1390890-setkeyframevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setKeyframeValue:(id)value time:(CGFloat)time forIndex:(NSUInteger)index ``` |
| To | ``` - (void)setKeyframeValue:(id _Nonnull)value time:(CGFloat)time forIndex:(NSUInteger)index ``` |

#### SKLabelNode.h

Modified [SKLabelNode.color](https://developer.apple.com/documentation/spritekit/sklabelnode/1519938-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *color ``` |
| To | ``` @property(nonatomic, retain, nullable) NSColor *color ``` |

Modified [SKLabelNode.fontColor](https://developer.apple.com/documentation/spritekit/sklabelnode/1520057-fontcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *fontColor ``` |
| To | ``` @property(nonatomic, retain, nullable) NSColor *fontColor ``` |

Modified [SKLabelNode.fontName](https://developer.apple.com/documentation/spritekit/sklabelnode/1520129-fontname)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *fontName ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *fontName ``` |

Modified [-[SKLabelNode initWithFontNamed:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1519917-initwithfontnamed)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithFontNamed:(NSString *)fontName ``` |
| To | ``` - (instancetype _Nonnull)initWithFontNamed:(NSString * _Nullable)fontName ``` |

Modified [+[SKLabelNode labelNodeWithFontNamed:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1576448-labelnodewithfontnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)labelNodeWithFontNamed:(NSString *)fontName ``` |
| To | ``` + (instancetype _Nonnull)labelNodeWithFontNamed:(NSString * _Nullable)fontName ``` |

Modified [+[SKLabelNode labelNodeWithText:]](https://developer.apple.com/documentation/spritekit/sklabelnode/1519612-labelnodewithtext)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)labelNodeWithText:(NSString *)text ``` |
| To | ``` + (instancetype _Nonnull)labelNodeWithText:(NSString * _Nullable)text ``` |

Modified [SKLabelNode.text](https://developer.apple.com/documentation/spritekit/sklabelnode/1519788-text)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *text ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *text ``` |

#### SKLightNode.h

Modified [SKLightNode.ambientColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520139-ambientcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSColor *ambientColor ``` |
| To | ``` @property(nonatomic, nonnull) NSColor *ambientColor ``` |

Modified [SKLightNode.lightColor](https://developer.apple.com/documentation/spritekit/sklightnode/1520244-lightcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSColor *lightColor ``` |
| To | ``` @property(nonatomic, nonnull) NSColor *lightColor ``` |

Modified [SKLightNode.shadowColor](https://developer.apple.com/documentation/spritekit/sklightnode/1519844-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) NSColor *shadowColor ``` |
| To | ``` @property(nonatomic, nonnull) NSColor *shadowColor ``` |

#### SKNode.h

Added [-[SKNode isEqualToNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483078-isequaltonode)Added [-[SKNode moveToParent:]](https://developer.apple.com/documentation/spritekit/sknode/1483021-movetoparent)Added [+[SKNode obstaclesFromNodeBounds:]](https://developer.apple.com/documentation/spritekit/sknode/1483132-obstacles)Added [+[SKNode obstaclesFromNodePhysicsBodies:]](https://developer.apple.com/documentation/spritekit/sknode/1483085-obstaclesfromnodephysicsbodies)Added [+[SKNode obstaclesFromSpriteTextures:accuracy:]](https://developer.apple.com/documentation/spritekit/sknode/1483134-obstaclesfromspritetextures)Modified [-[NSEvent locationInNode:]](https://developer.apple.com/documentation/appkit/nsevent/1483105-location)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)locationInNode:(SKNode *)node ``` |
| To | ``` - (CGPoint)locationInNode:(SKNode * _Nonnull)node ``` |

Modified [-[SKNode actionForKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483138-action)

|  | Declaration |
| --- | --- |
| From | ``` - (SKAction *)actionForKey:(NSString *)key ``` |
| To | ``` - (SKAction * _Nullable)actionForKey:(NSString * _Nonnull)key ``` |

Modified [-[SKNode addChild:]](https://developer.apple.com/documentation/spritekit/sknode/1483054-addchild)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addChild:(SKNode *)node ``` |
| To | ``` - (void)addChild:(SKNode * _Nonnull)node ``` |

Modified [-[SKNode childNodeWithName:]](https://developer.apple.com/documentation/spritekit/sknode/1483060-childnode)

|  | Declaration |
| --- | --- |
| From | ``` - (SKNode *)childNodeWithName:(NSString *)name ``` |
| To | ``` - (SKNode * _Nullable)childNodeWithName:(NSString * _Nonnull)name ``` |

Modified [SKNode.children](https://developer.apple.com/documentation/spritekit/sknode/1483028-children)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *children ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKNode *> *children ``` |

Modified [SKNode.constraints](https://developer.apple.com/documentation/spritekit/sknode/1483124-constraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *constraints ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<SKConstraint *> *constraints ``` |

Modified [-[SKNode convertPoint:fromNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483058-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)point fromNode:(SKNode *)node ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)point fromNode:(SKNode * _Nonnull)node ``` |

Modified [-[SKNode convertPoint:toNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483056-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)point toNode:(SKNode *)node ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)point toNode:(SKNode * _Nonnull)node ``` |

Modified [-[SKNode enumerateChildNodesWithName:usingBlock:]](https://developer.apple.com/documentation/spritekit/sknode/1483024-enumeratechildnodeswithname)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateChildNodesWithName:(NSString *)name usingBlock:(void (^)(SKNode *node, BOOL *stop))block ``` |
| To | ``` - (void)enumerateChildNodesWithName:(NSString * _Nonnull)name usingBlock:(void (^ _Nonnull)(SKNode * _Nonnull node, BOOL * _Nonnull stop))block ``` |

Modified [-[SKNode init]](https://developer.apple.com/documentation/spritekit/sknode/1483097-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[SKNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/sknode/1483142-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[SKNode inParentHierarchy:]](https://developer.apple.com/documentation/spritekit/sknode/1483111-inparenthierarchy)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)inParentHierarchy:(SKNode *)parent ``` |
| To | ``` - (BOOL)inParentHierarchy:(SKNode * _Nonnull)parent ``` |

Modified [-[SKNode insertChild:atIndex:]](https://developer.apple.com/documentation/spritekit/sknode/1483062-insertchild)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertChild:(SKNode *)node atIndex:(NSInteger)index ``` |
| To | ``` - (void)insertChild:(SKNode * _Nonnull)node atIndex:(NSInteger)index ``` |

Modified [-[SKNode intersectsNode:]](https://developer.apple.com/documentation/spritekit/sknode/1483140-intersects)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)intersectsNode:(SKNode *)node ``` |
| To | ``` - (BOOL)intersectsNode:(SKNode * _Nonnull)node ``` |

Modified [SKNode.name](https://developer.apple.com/documentation/spritekit/sknode/1483136-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *name ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *name ``` |

Modified [+[SKNode node]](https://developer.apple.com/documentation/spritekit/sknode/1483038-node)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)node ``` |
| To | ``` + (instancetype _Nonnull)node ``` |

Modified [-[SKNode nodeAtPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483099-nodeatpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (SKNode *)nodeAtPoint:(CGPoint)p ``` |
| To | ``` - (SKNode * _Nonnull)nodeAtPoint:(CGPoint)p ``` |

Modified [-[SKNode nodesAtPoint:]](https://developer.apple.com/documentation/spritekit/sknode/1483072-nodes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)nodesAtPoint:(CGPoint)p ``` |
| To | ``` - (NSArray<SKNode *> * _Nonnull)nodesAtPoint:(CGPoint)p ``` |

Modified [+[SKNode nodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/sknode/1483083-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)nodeWithFileNamed:(NSString *)filename ``` |
| To | ``` + (instancetype _Nullable)nodeWithFileNamed:(NSString * _Nonnull)filename ``` |

Modified [-[SKNode objectForKeyedSubscript:]](https://developer.apple.com/documentation/spritekit/sknode/1483070-subscript)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)objectForKeyedSubscript:(NSString *)name ``` |
| To | ``` - (NSArray<SKNode *> * _Nonnull)objectForKeyedSubscript:(NSString * _Nonnull)name ``` |

Modified [SKNode.parent](https://developer.apple.com/documentation/spritekit/sknode/1483080-parent)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKNode *parent ``` |
| To | ``` @property(nonatomic, readonly, nullable) SKNode *parent ``` |

Modified [SKNode.physicsBody](https://developer.apple.com/documentation/spritekit/sknode/1483117-physicsbody)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKPhysicsBody *physicsBody ``` |
| To | ``` @property(nonatomic, retain, nullable) SKPhysicsBody *physicsBody ``` |

Modified [SKNode.reachConstraints](https://developer.apple.com/documentation/spritekit/sknode/1483019-reachconstraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) SKReachConstraints *reachConstraints ``` |
| To | ``` @property(nonatomic, copy, nullable) SKReachConstraints *reachConstraints ``` |

Modified [-[SKNode removeActionForKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483076-removeactionforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeActionForKey:(NSString *)key ``` |
| To | ``` - (void)removeActionForKey:(NSString * _Nonnull)key ``` |

Modified [-[SKNode removeChildrenInArray:]](https://developer.apple.com/documentation/spritekit/sknode/1483091-removechildreninarray)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeChildrenInArray:(NSArray *)nodes ``` |
| To | ``` - (void)removeChildrenInArray:(NSArray<SKNode *> * _Nonnull)nodes ``` |

Modified [-[SKNode runAction:]](https://developer.apple.com/documentation/spritekit/sknode/1483093-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SKAction *)action ``` |
| To | ``` - (void)runAction:(SKAction * _Nonnull)action ``` |

Modified [-[SKNode runAction:completion:]](https://developer.apple.com/documentation/spritekit/sknode/1483103-runaction)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SKAction *)action completion:(void (^)(void))block ``` |
| To | ``` - (void)runAction:(SKAction * _Nonnull)action completion:(void (^ _Nonnull)(void))block ``` |

Modified [-[SKNode runAction:withKey:]](https://developer.apple.com/documentation/spritekit/sknode/1483042-run)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runAction:(SKAction *)action withKey:(NSString *)key ``` |
| To | ``` - (void)runAction:(SKAction * _Nonnull)action withKey:(NSString * _Nonnull)key ``` |

Modified [SKNode.scene](https://developer.apple.com/documentation/spritekit/sknode/1483064-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly, nullable) SKScene *scene ``` |

Modified [SKNode.userData](https://developer.apple.com/documentation/spritekit/sknode/1483121-userdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSMutableDictionary *userData ``` |
| To | ``` @property(nonatomic, retain, nullable) NSMutableDictionary *userData ``` |

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

Modified [+[SKPhysicsBody bodyWithCircleOfRadius:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520261-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithCircleOfRadius:(CGFloat)r ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithCircleOfRadius:(CGFloat)r ``` |

Modified [+[SKPhysicsBody bodyWithCircleOfRadius:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519692-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithCircleOfRadius:(CGFloat)r center:(CGPoint)center ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithCircleOfRadius:(CGFloat)r center:(CGPoint)center ``` |

Modified [+[SKPhysicsBody bodyWithEdgeChainFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519871-bodywithedgechainfrompath)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithEdgeChainFromPath:(CGPathRef)path ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithEdgeChainFromPath:(CGPathRef _Nonnull)path ``` |

Modified [+[SKPhysicsBody bodyWithEdgeFromPoint:toPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520401-bodywithedgefrompoint)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithEdgeFromPoint:(CGPoint)p1 toPoint:(CGPoint)p2 ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithEdgeFromPoint:(CGPoint)p1 toPoint:(CGPoint)p2 ``` |

Modified [+[SKPhysicsBody bodyWithEdgeLoopFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519732-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithEdgeLoopFromPath:(CGPathRef)path ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithEdgeLoopFromPath:(CGPathRef _Nonnull)path ``` |

Modified [+[SKPhysicsBody bodyWithEdgeLoopFromRect:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520055-bodywithedgeloopfromrect)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithEdgeLoopFromRect:(CGRect)rect ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithEdgeLoopFromRect:(CGRect)rect ``` |

Modified [+[SKPhysicsBody bodyWithPolygonFromPath:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520379-bodywithpolygonfrompath)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithPolygonFromPath:(CGPathRef)path ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithPolygonFromPath:(CGPathRef _Nonnull)path ``` |

Modified [+[SKPhysicsBody bodyWithRectangleOfSize:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520295-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithRectangleOfSize:(CGSize)s ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithRectangleOfSize:(CGSize)s ``` |

Modified [+[SKPhysicsBody bodyWithRectangleOfSize:center:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519936-bodywithrectangleofsize)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithRectangleOfSize:(CGSize)s center:(CGPoint)center ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithRectangleOfSize:(CGSize)s center:(CGPoint)center ``` |

Modified [+[SKPhysicsBody bodyWithTexture:alphaThreshold:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519689-bodywithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithTexture:(SKTexture *)texture alphaThreshold:(float)alphaThreshold size:(CGSize)size ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithTexture:(SKTexture * _Nonnull)texture alphaThreshold:(float)alphaThreshold size:(CGSize)size ``` |

Modified [+[SKPhysicsBody bodyWithTexture:size:]](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519690-bodywithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsBody *)bodyWithTexture:(SKTexture *)texture size:(CGSize)size ``` |
| To | ``` + (SKPhysicsBody * _Nonnull)bodyWithTexture:(SKTexture * _Nonnull)texture size:(CGSize)size ``` |

Modified [SKPhysicsBody.joints](https://developer.apple.com/documentation/spritekit/skphysicsbody/1519849-joints)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *joints ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<SKPhysicsJoint *> *joints ``` |

Modified [SKPhysicsBody.node](https://developer.apple.com/documentation/spritekit/skphysicsbody/1520049-node)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, weak) SKNode *node ``` |
| To | ``` @property(nonatomic, readonly, weak, nullable) SKNode *node ``` |

#### SKPhysicsContact.h

Modified [SKPhysicsContact.bodyA](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478533-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsContact.bodyB](https://developer.apple.com/documentation/spritekit/skphysicscontact/1478526-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SKPhysicsBody *bodyB ``` |

#### SKPhysicsJoint.h

Modified [SKPhysicsJoint.bodyA](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1520403-bodya)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKPhysicsBody *bodyA ``` |
| To | ``` @property(nonatomic, retain, nonnull) SKPhysicsBody *bodyA ``` |

Modified [SKPhysicsJoint.bodyB](https://developer.apple.com/documentation/spritekit/skphysicsjoint/1519693-bodyb)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKPhysicsBody *bodyB ``` |
| To | ``` @property(nonatomic, retain, nonnull) SKPhysicsBody *bodyB ``` |

Modified [+[SKPhysicsJointFixed jointWithBodyA:bodyB:anchor:]](https://developer.apple.com/documentation/spritekit/skphysicsjointfixed/1520076-joint)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsJointFixed *)jointWithBodyA:(SKPhysicsBody *)bodyA bodyB:(SKPhysicsBody *)bodyB anchor:(CGPoint)anchor ``` |
| To | ``` + (SKPhysicsJointFixed * _Nonnull)jointWithBodyA:(SKPhysicsBody * _Nonnull)bodyA bodyB:(SKPhysicsBody * _Nonnull)bodyB anchor:(CGPoint)anchor ``` |

Modified [+[SKPhysicsJointLimit jointWithBodyA:bodyB:anchorA:anchorB:]](https://developer.apple.com/documentation/spritekit/skphysicsjointlimit/1520402-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsJointLimit *)jointWithBodyA:(SKPhysicsBody *)bodyA bodyB:(SKPhysicsBody *)bodyB anchorA:(CGPoint)anchorA anchorB:(CGPoint)anchorB ``` |
| To | ``` + (SKPhysicsJointLimit * _Nonnull)jointWithBodyA:(SKPhysicsBody * _Nonnull)bodyA bodyB:(SKPhysicsBody * _Nonnull)bodyB anchorA:(CGPoint)anchorA anchorB:(CGPoint)anchorB ``` |

Modified [+[SKPhysicsJointPin jointWithBodyA:bodyB:anchor:]](https://developer.apple.com/documentation/spritekit/skphysicsjointpin/1519698-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsJointPin *)jointWithBodyA:(SKPhysicsBody *)bodyA bodyB:(SKPhysicsBody *)bodyB anchor:(CGPoint)anchor ``` |
| To | ``` + (SKPhysicsJointPin * _Nonnull)jointWithBodyA:(SKPhysicsBody * _Nonnull)bodyA bodyB:(SKPhysicsBody * _Nonnull)bodyB anchor:(CGPoint)anchor ``` |

Modified [+[SKPhysicsJointSliding jointWithBodyA:bodyB:anchor:axis:]](https://developer.apple.com/documentation/spritekit/skphysicsjointsliding/1520333-jointwithbodya)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsJointSliding *)jointWithBodyA:(SKPhysicsBody *)bodyA bodyB:(SKPhysicsBody *)bodyB anchor:(CGPoint)anchor axis:(CGVector)axis ``` |
| To | ``` + (SKPhysicsJointSliding * _Nonnull)jointWithBodyA:(SKPhysicsBody * _Nonnull)bodyA bodyB:(SKPhysicsBody * _Nonnull)bodyB anchor:(CGPoint)anchor axis:(CGVector)axis ``` |

Modified [+[SKPhysicsJointSpring jointWithBodyA:bodyB:anchorA:anchorB:]](https://developer.apple.com/documentation/spritekit/skphysicsjointspring/1519665-joint)

|  | Declaration |
| --- | --- |
| From | ``` + (SKPhysicsJointSpring *)jointWithBodyA:(SKPhysicsBody *)bodyA bodyB:(SKPhysicsBody *)bodyB anchorA:(CGPoint)anchorA anchorB:(CGPoint)anchorB ``` |
| To | ``` + (SKPhysicsJointSpring * _Nonnull)jointWithBodyA:(SKPhysicsBody * _Nonnull)bodyA bodyB:(SKPhysicsBody * _Nonnull)bodyB anchorA:(CGPoint)anchorA anchorB:(CGPoint)anchorB ``` |

#### SKPhysicsWorld.h

Modified [-[SKPhysicsContactDelegate didBeginContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449595-didbegin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didBeginContact:(SKPhysicsContact *)contact ``` |
| To | ``` - (void)didBeginContact:(SKPhysicsContact * _Nonnull)contact ``` |

Modified [-[SKPhysicsContactDelegate didEndContact:]](https://developer.apple.com/documentation/spritekit/skphysicscontactdelegate/1449599-didendcontact)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didEndContact:(SKPhysicsContact *)contact ``` |
| To | ``` - (void)didEndContact:(SKPhysicsContact * _Nonnull)contact ``` |

Modified [-[SKPhysicsWorld addJoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449617-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addJoint:(SKPhysicsJoint *)joint ``` |
| To | ``` - (void)addJoint:(SKPhysicsJoint * _Nonnull)joint ``` |

Modified [-[SKPhysicsWorld bodyAlongRayStart:end:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449613-bodyalongraystart)

|  | Declaration |
| --- | --- |
| From | ``` - (SKPhysicsBody *)bodyAlongRayStart:(CGPoint)start end:(CGPoint)end ``` |
| To | ``` - (SKPhysicsBody * _Nullable)bodyAlongRayStart:(CGPoint)start end:(CGPoint)end ``` |

Modified [-[SKPhysicsWorld bodyAtPoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449625-bodyatpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (SKPhysicsBody *)bodyAtPoint:(CGPoint)point ``` |
| To | ``` - (SKPhysicsBody * _Nullable)bodyAtPoint:(CGPoint)point ``` |

Modified [-[SKPhysicsWorld bodyInRect:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449604-body)

|  | Declaration |
| --- | --- |
| From | ``` - (SKPhysicsBody *)bodyInRect:(CGRect)rect ``` |
| To | ``` - (SKPhysicsBody * _Nullable)bodyInRect:(CGRect)rect ``` |

Modified [SKPhysicsWorld.contactDelegate](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449602-contactdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SKPhysicsContactDelegate> contactDelegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<SKPhysicsContactDelegate> contactDelegate ``` |

Modified [-[SKPhysicsWorld enumerateBodiesAlongRayStart:end:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449615-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateBodiesAlongRayStart:(CGPoint)start end:(CGPoint)end usingBlock:(void (^)(SKPhysicsBody *body, CGPoint point, CGVector normal, BOOL *stop))block ``` |
| To | ``` - (void)enumerateBodiesAlongRayStart:(CGPoint)start end:(CGPoint)end usingBlock:(void (^ _Nonnull)(SKPhysicsBody * _Nonnull body, CGPoint point, CGVector normal, BOOL * _Nonnull stop))block ``` |

Modified [-[SKPhysicsWorld enumerateBodiesAtPoint:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449597-enumeratebodiesatpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateBodiesAtPoint:(CGPoint)point usingBlock:(void (^)(SKPhysicsBody *body, BOOL *stop))block ``` |
| To | ``` - (void)enumerateBodiesAtPoint:(CGPoint)point usingBlock:(void (^ _Nonnull)(SKPhysicsBody * _Nonnull body, BOOL * _Nonnull stop))block ``` |

Modified [-[SKPhysicsWorld enumerateBodiesInRect:usingBlock:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449619-enumeratebodies)

|  | Declaration |
| --- | --- |
| From | ``` - (void)enumerateBodiesInRect:(CGRect)rect usingBlock:(void (^)(SKPhysicsBody *body, BOOL *stop))block ``` |
| To | ``` - (void)enumerateBodiesInRect:(CGRect)rect usingBlock:(void (^ _Nonnull)(SKPhysicsBody * _Nonnull body, BOOL * _Nonnull stop))block ``` |

Modified [-[SKPhysicsWorld removeJoint:]](https://developer.apple.com/documentation/spritekit/skphysicsworld/1449609-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeJoint:(SKPhysicsJoint *)joint ``` |
| To | ``` - (void)removeJoint:(SKPhysicsJoint * _Nonnull)joint ``` |

#### SKReferenceNode.h (Added)

Added [SKReferenceNode](https://developer.apple.com/documentation/spritekit/skreferencenode)Added [-[SKReferenceNode didLoadReferenceNode:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508364-didload)Added [-[SKReferenceNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508363-init)Added [-[SKReferenceNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508369-init)Added [-[SKReferenceNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508366-initwithurl)Added [+[SKReferenceNode referenceNodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508368-init)Added [+[SKReferenceNode referenceNodeWithURL:]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508365-init)Added [-[SKReferenceNode resolveReferenceNode]](https://developer.apple.com/documentation/spritekit/skreferencenode/1508371-resolvereferencenode)

#### SKRegion.h

Modified [+[SKRegion infiniteRegion]](https://developer.apple.com/documentation/spritekit/skregion/1520061-infinite)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)infiniteRegion ``` |
| To | ``` + (instancetype _Nonnull)infiniteRegion ``` |

Modified [-[SKRegion initWithPath:]](https://developer.apple.com/documentation/spritekit/skregion/1519857-initwithpath)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPath:(CGPathRef)path ``` |
| To | ``` - (instancetype _Nonnull)initWithPath:(CGPathRef _Nonnull)path ``` |

Modified [-[SKRegion initWithRadius:]](https://developer.apple.com/documentation/spritekit/skregion/1520219-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithRadius:(float)radius ``` |
| To | ``` - (instancetype _Nonnull)initWithRadius:(float)radius ``` |

Modified [-[SKRegion initWithSize:]](https://developer.apple.com/documentation/spritekit/skregion/1520385-initwithsize)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSize:(CGSize)size ``` |
| To | ``` - (instancetype _Nonnull)initWithSize:(CGSize)size ``` |

Modified [-[SKRegion inverseRegion]](https://developer.apple.com/documentation/spritekit/skregion/1519700-inverse)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)inverseRegion ``` |
| To | ``` - (instancetype _Nonnull)inverseRegion ``` |

Modified [SKRegion.path](https://developer.apple.com/documentation/spritekit/skregion/1520042-path)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) CGPathRef path ``` |
| To | ``` @property(nonatomic, readonly, nullable) CGPathRef path ``` |

Modified [-[SKRegion regionByDifferenceFromRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519879-bydifference)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)regionByDifferenceFromRegion:(SKRegion *)region ``` |
| To | ``` - (instancetype _Nonnull)regionByDifferenceFromRegion:(SKRegion * _Nonnull)region ``` |

Modified [-[SKRegion regionByIntersectionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519646-regionbyintersectionwithregion)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)regionByIntersectionWithRegion:(SKRegion *)region ``` |
| To | ``` - (instancetype _Nonnull)regionByIntersectionWithRegion:(SKRegion * _Nonnull)region ``` |

Modified [-[SKRegion regionByUnionWithRegion:]](https://developer.apple.com/documentation/spritekit/skregion/1519702-regionbyunionwithregion)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)regionByUnionWithRegion:(SKRegion *)region ``` |
| To | ``` - (instancetype _Nonnull)regionByUnionWithRegion:(SKRegion * _Nonnull)region ``` |

#### SKScene.h

Added [SKScene.audioEngine](https://developer.apple.com/documentation/spritekit/skscene/1519644-audioengine)Added [SKScene.camera](https://developer.apple.com/documentation/spritekit/skscene/1519696-camera)Added [SKScene.listener](https://developer.apple.com/documentation/spritekit/skscene/1520363-listener)Modified [SKScene.backgroundColor](https://developer.apple.com/documentation/spritekit/skscene/1520278-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *backgroundColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *backgroundColor ``` |

Modified [SKScene.delegate](https://developer.apple.com/documentation/spritekit/skscene/1520213-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<SKSceneDelegate> delegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<SKSceneDelegate> delegate ``` |

Modified [-[SKScene didMoveToView:]](https://developer.apple.com/documentation/spritekit/skscene/1519607-didmove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didMoveToView:(SKView *)view ``` |
| To | ``` - (void)didMoveToView:(SKView * _Nonnull)view ``` |

Modified [-[SKScene initWithSize:]](https://developer.apple.com/documentation/spritekit/skscene/1520435-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSize:(CGSize)size ``` |
| To | ``` - (instancetype _Nonnull)initWithSize:(CGSize)size ``` |

Modified [SKScene.physicsWorld](https://developer.apple.com/documentation/spritekit/skscene/1519584-physicsworld)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKPhysicsWorld *physicsWorld ``` |
| To | ``` @property(nonatomic, readonly, nonnull) SKPhysicsWorld *physicsWorld ``` |

Modified [+[SKScene sceneWithSize:]](https://developer.apple.com/documentation/spritekit/skscene/1536393-scenewithsize)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)sceneWithSize:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)sceneWithSize:(CGSize)size ``` |

Modified [SKScene.view](https://developer.apple.com/documentation/spritekit/skscene/1519726-view)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, weak, readonly) SKView *view ``` |
| To | ``` @property(nonatomic, weak, readonly, nullable) SKView *view ``` |

Modified [-[SKScene willMoveFromView:]](https://developer.apple.com/documentation/spritekit/skscene/1519703-willmovefromview)

|  | Declaration |
| --- | --- |
| From | ``` - (void)willMoveFromView:(SKView *)view ``` |
| To | ``` - (void)willMoveFromView:(SKView * _Nonnull)view ``` |

Modified [-[SKSceneDelegate didApplyConstraintsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520375-didapplyconstraintsforscene)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didApplyConstraintsForScene:(SKScene *)scene ``` |
| To | ``` - (void)didApplyConstraintsForScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKSceneDelegate didEvaluateActionsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520071-didevaluateactions)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didEvaluateActionsForScene:(SKScene *)scene ``` |
| To | ``` - (void)didEvaluateActionsForScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKSceneDelegate didFinishUpdateForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519814-didfinishupdate)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didFinishUpdateForScene:(SKScene *)scene ``` |
| To | ``` - (void)didFinishUpdateForScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKSceneDelegate didSimulatePhysicsForScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1520392-didsimulatephysicsforscene)

|  | Declaration |
| --- | --- |
| From | ``` - (void)didSimulatePhysicsForScene:(SKScene *)scene ``` |
| To | ``` - (void)didSimulatePhysicsForScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKSceneDelegate update:forScene:]](https://developer.apple.com/documentation/spritekit/skscenedelegate/1519757-update)

|  | Declaration |
| --- | --- |
| From | ``` - (void)update:(NSTimeInterval)currentTime forScene:(SKScene *)scene ``` |
| To | ``` - (void)update:(NSTimeInterval)currentTime forScene:(SKScene * _Nonnull)scene ``` |

#### SKShader.h

Modified [-[SKShader addUniform:]](https://developer.apple.com/documentation/spritekit/skshader/1477561-adduniform)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addUniform:(SKUniform *)uniform ``` |
| To | ``` - (void)addUniform:(SKUniform * _Nonnull)uniform ``` |

Modified [-[SKShader initWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477571-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source ``` |

Modified [-[SKShader initWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477555-initwithsource)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSource:(NSString *)source uniforms:(NSArray *)uniforms ``` |
| To | ``` - (instancetype _Nonnull)initWithSource:(NSString * _Nonnull)source uniforms:(NSArray<SKUniform *> * _Nonnull)uniforms ``` |

Modified [-[SKShader removeUniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477553-removeuniformnamed)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeUniformNamed:(NSString *)name ``` |
| To | ``` - (void)removeUniformNamed:(NSString * _Nonnull)name ``` |

Modified [+[SKShader shader]](https://developer.apple.com/documentation/spritekit/skshader/1477559-shader)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shader ``` |
| To | ``` + (instancetype _Nonnull)shader ``` |

Modified [+[SKShader shaderWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477557-shaderwithfilenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shaderWithFileNamed:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)shaderWithFileNamed:(NSString * _Nonnull)name ``` |

Modified [+[SKShader shaderWithSource:]](https://developer.apple.com/documentation/spritekit/skshader/1477563-shaderwithsource)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shaderWithSource:(NSString *)source ``` |
| To | ``` + (instancetype _Nonnull)shaderWithSource:(NSString * _Nonnull)source ``` |

Modified [+[SKShader shaderWithSource:uniforms:]](https://developer.apple.com/documentation/spritekit/skshader/1477569-shaderwithsource)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shaderWithSource:(NSString *)source uniforms:(NSArray *)uniforms ``` |
| To | ``` + (instancetype _Nonnull)shaderWithSource:(NSString * _Nonnull)source uniforms:(NSArray<SKUniform *> * _Nonnull)uniforms ``` |

Modified [SKShader.source](https://developer.apple.com/documentation/spritekit/skshader/1477544-source)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *source ``` |
| To | ``` @property(copy, nullable) NSString *source ``` |

Modified [-[SKShader uniformNamed:]](https://developer.apple.com/documentation/spritekit/skshader/1477567-uniformnamed)

|  | Declaration |
| --- | --- |
| From | ``` - (SKUniform *)uniformNamed:(NSString *)name ``` |
| To | ``` - (SKUniform * _Nullable)uniformNamed:(NSString * _Nonnull)name ``` |

Modified [SKShader.uniforms](https://developer.apple.com/documentation/spritekit/skshader/1477565-uniforms)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *uniforms ``` |
| To | ``` @property(copy, nonnull) NSArray<SKUniform *> *uniforms ``` |

#### SKShapeNode.h

Modified [SKShapeNode.fillColor](https://developer.apple.com/documentation/spritekit/skshapenode/1520154-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *fillColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *fillColor ``` |

Modified [SKShapeNode.fillShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519629-fillshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKShader *fillShader ``` |
| To | ``` @property(nonatomic, retain, nullable) SKShader *fillShader ``` |

Modified [SKShapeNode.fillTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519956-filltexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *fillTexture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *fillTexture ``` |

Modified [SKShapeNode.path](https://developer.apple.com/documentation/spritekit/skshapenode/1519741-path)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic) CGPathRef path ``` |
| To | ``` @property(nonatomic, nullable) CGPathRef path ``` |

Modified [+[SKShapeNode shapeNodeWithCircleOfRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519570-shapenodewithcircleofradius)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithCircleOfRadius:(CGFloat)radius ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithCircleOfRadius:(CGFloat)radius ``` |

Modified [+[SKShapeNode shapeNodeWithEllipseInRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520412-shapenodewithellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithEllipseInRect:(CGRect)rect ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithEllipseInRect:(CGRect)rect ``` |

Modified [+[SKShapeNode shapeNodeWithEllipseOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519980-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithEllipseOfSize:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithEllipseOfSize:(CGSize)size ``` |

Modified [+[SKShapeNode shapeNodeWithPath:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520022-shapenodewithpath)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithPath:(CGPathRef)path ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithPath:(CGPathRef _Nonnull)path ``` |

Modified [+[SKShapeNode shapeNodeWithPath:centered:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519649-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithPath:(CGPathRef)path centered:(BOOL)centered ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithPath:(CGPathRef _Nonnull)path centered:(BOOL)centered ``` |

Modified [+[SKShapeNode shapeNodeWithPoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520120-shapenodewithpoints)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithPoints:(CGPoint *)points count:(size_t)numPoints ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithPoints:(CGPoint * _Nonnull)points count:(size_t)numPoints ``` |

Modified [+[SKShapeNode shapeNodeWithRect:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520047-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithRect:(CGRect)rect ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithRect:(CGRect)rect ``` |

Modified [+[SKShapeNode shapeNodeWithRect:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519769-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithRect:(CGRect)rect cornerRadius:(CGFloat)cornerRadius ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithRect:(CGRect)rect cornerRadius:(CGFloat)cornerRadius ``` |

Modified [+[SKShapeNode shapeNodeWithRectOfSize:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520147-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithRectOfSize:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithRectOfSize:(CGSize)size ``` |

Modified [+[SKShapeNode shapeNodeWithRectOfSize:cornerRadius:]](https://developer.apple.com/documentation/spritekit/skshapenode/1519712-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithRectOfSize:(CGSize)size cornerRadius:(CGFloat)cornerRadius ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithRectOfSize:(CGSize)size cornerRadius:(CGFloat)cornerRadius ``` |

Modified [+[SKShapeNode shapeNodeWithSplinePoints:count:]](https://developer.apple.com/documentation/spritekit/skshapenode/1520140-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)shapeNodeWithSplinePoints:(CGPoint *)points count:(size_t)numPoints ``` |
| To | ``` + (instancetype _Nonnull)shapeNodeWithSplinePoints:(CGPoint * _Nonnull)points count:(size_t)numPoints ``` |

Modified [SKShapeNode.strokeColor](https://developer.apple.com/documentation/spritekit/skshapenode/1519748-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *strokeColor ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *strokeColor ``` |

Modified [SKShapeNode.strokeShader](https://developer.apple.com/documentation/spritekit/skshapenode/1519784-strokeshader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKShader *strokeShader ``` |
| To | ``` @property(nonatomic, retain, nullable) SKShader *strokeShader ``` |

Modified [SKShapeNode.strokeTexture](https://developer.apple.com/documentation/spritekit/skshapenode/1519824-stroketexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *strokeTexture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *strokeTexture ``` |

#### SKSpriteNode.h

Modified [SKSpriteNode.color](https://developer.apple.com/documentation/spritekit/skspritenode/1519639-color)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSColor *color ``` |
| To | ``` @property(nonatomic, retain, nonnull) NSColor *color ``` |

Modified [-[SKSpriteNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520399-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[SKSpriteNode initWithColor:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519762-initwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithColor:(NSColor *)color size:(CGSize)size ``` |
| To | ``` - (instancetype _Nonnull)initWithColor:(NSColor * _Nonnull)color size:(CGSize)size ``` |

Modified [-[SKSpriteNode initWithImageNamed:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520391-initwithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithImageNamed:(NSString *)name ``` |
| To | ``` - (instancetype _Nonnull)initWithImageNamed:(NSString * _Nonnull)name ``` |

Modified [-[SKSpriteNode initWithTexture:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519942-initwithtexture)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithTexture:(SKTexture *)texture ``` |
| To | ``` - (instancetype _Nonnull)initWithTexture:(SKTexture * _Nullable)texture ``` |

Modified [-[SKSpriteNode initWithTexture:color:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520029-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithTexture:(SKTexture *)texture color:(NSColor *)color size:(CGSize)size ``` |
| To | ``` - (instancetype _Nonnull)initWithTexture:(SKTexture * _Nullable)texture color:(NSColor * _Nonnull)color size:(CGSize)size ``` |

Modified [SKSpriteNode.normalTexture](https://developer.apple.com/documentation/spritekit/skspritenode/1519657-normaltexture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *normalTexture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *normalTexture ``` |

Modified [SKSpriteNode.shader](https://developer.apple.com/documentation/spritekit/skspritenode/1519714-shader)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKShader *shader ``` |
| To | ``` @property(nonatomic, retain, nullable) SKShader *shader ``` |

Modified [+[SKSpriteNode spriteNodeWithColor:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579717-spritenodewithcolor)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithColor:(NSColor *)color size:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithColor:(NSColor * _Nonnull)color size:(CGSize)size ``` |

Modified [+[SKSpriteNode spriteNodeWithImageNamed:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579718-spritenodewithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithImageNamed:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithImageNamed:(NSString * _Nonnull)name ``` |

Modified [+[SKSpriteNode spriteNodeWithImageNamed:normalMapped:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519721-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithImageNamed:(NSString *)name normalMapped:(BOOL)generateNormalMap ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithImageNamed:(NSString * _Nonnull)name normalMapped:(BOOL)generateNormalMap ``` |

Modified [+[SKSpriteNode spriteNodeWithTexture:]](https://developer.apple.com/documentation/spritekit/skspritenode/1579716-spritenodewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithTexture:(SKTexture *)texture ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithTexture:(SKTexture * _Nullable)texture ``` |

Modified [+[SKSpriteNode spriteNodeWithTexture:normalMap:]](https://developer.apple.com/documentation/spritekit/skspritenode/1520153-spritenodewithtexture)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithTexture:(SKTexture *)texture normalMap:(SKTexture *)normalMap ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithTexture:(SKTexture * _Nullable)texture normalMap:(SKTexture * _Nullable)normalMap ``` |

Modified [+[SKSpriteNode spriteNodeWithTexture:size:]](https://developer.apple.com/documentation/spritekit/skspritenode/1519812-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)spriteNodeWithTexture:(SKTexture *)texture size:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)spriteNodeWithTexture:(SKTexture * _Nullable)texture size:(CGSize)size ``` |

Modified [SKSpriteNode.texture](https://developer.apple.com/documentation/spritekit/skspritenode/1520011-texture)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) SKTexture *texture ``` |
| To | ``` @property(nonatomic, retain, nullable) SKTexture *texture ``` |

#### SKTexture.h

Added [SKTexture.CGImage](https://developer.apple.com/documentation/spritekit/sktexture/1519755-cgimage)Modified [+[SKTexture preloadTextures:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktexture/1519817-preloadtextures)

|  | Declaration |
| --- | --- |
| From | ``` + (void)preloadTextures:(NSArray *)textures withCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)preloadTextures:(NSArray<SKTexture *> * _Nonnull)textures withCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [-[SKTexture preloadWithCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktexture/1520172-preload)

|  | Declaration |
| --- | --- |
| From | ``` - (void)preloadWithCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` - (void)preloadWithCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [-[SKTexture textureByApplyingCIFilter:]](https://developer.apple.com/documentation/spritekit/sktexture/1520388-texturebyapplyingcifilter)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)textureByApplyingCIFilter:(CIFilter *)filter ``` |
| To | ``` - (instancetype _Nonnull)textureByApplyingCIFilter:(CIFilter * _Nonnull)filter ``` |

Modified [-[SKTexture textureByGeneratingNormalMap]](https://developer.apple.com/documentation/spritekit/sktexture/1519687-texturebygeneratingnormalmap)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)textureByGeneratingNormalMap ``` |
| To | ``` - (instancetype _Nonnull)textureByGeneratingNormalMap ``` |

Modified [-[SKTexture textureByGeneratingNormalMapWithSmoothness:contrast:]](https://developer.apple.com/documentation/spritekit/sktexture/1520441-texturebygeneratingnormalmapwith)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)textureByGeneratingNormalMapWithSmoothness:(CGFloat)smoothness contrast:(CGFloat)contrast ``` |
| To | ``` - (instancetype _Nonnull)textureByGeneratingNormalMapWithSmoothness:(CGFloat)smoothness contrast:(CGFloat)contrast ``` |

Modified [+[SKTexture textureNoiseWithSmoothness:size:grayscale:]](https://developer.apple.com/documentation/spritekit/sktexture/1519971-texturenoisewithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureNoiseWithSmoothness:(CGFloat)smoothness size:(CGSize)size grayscale:(BOOL)grayscale ``` |
| To | ``` + (instancetype _Nonnull)textureNoiseWithSmoothness:(CGFloat)smoothness size:(CGSize)size grayscale:(BOOL)grayscale ``` |

Modified [+[SKTexture textureVectorNoiseWithSmoothness:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1520393-texturevectornoisewithsmoothness)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureVectorNoiseWithSmoothness:(CGFloat)smoothness size:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)textureVectorNoiseWithSmoothness:(CGFloat)smoothness size:(CGSize)size ``` |

Modified [+[SKTexture textureWithCGImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1519576-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithCGImage:(CGImageRef)image ``` |
| To | ``` + (instancetype _Nonnull)textureWithCGImage:(CGImageRef _Nonnull)image ``` |

Modified [+[SKTexture textureWithData:size:]](https://developer.apple.com/documentation/spritekit/sktexture/1519962-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithData:(NSData *)pixelData size:(CGSize)size ``` |
| To | ``` + (instancetype _Nonnull)textureWithData:(NSData * _Nonnull)pixelData size:(CGSize)size ``` |

Modified [+[SKTexture textureWithData:size:flipped:]](https://developer.apple.com/documentation/spritekit/sktexture/1519674-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithData:(NSData *)pixelData size:(CGSize)size flipped:(BOOL)flipped ``` |
| To | ``` + (instancetype _Nonnull)textureWithData:(NSData * _Nonnull)pixelData size:(CGSize)size flipped:(BOOL)flipped ``` |

Modified [+[SKTexture textureWithData:size:rowLength:alignment:]](https://developer.apple.com/documentation/spritekit/sktexture/1520181-texturewithdata)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithData:(NSData *)pixelData size:(CGSize)size rowLength:(unsigned int)rowLength alignment:(unsigned int)alignment ``` |
| To | ``` + (instancetype _Nonnull)textureWithData:(NSData * _Nonnull)pixelData size:(CGSize)size rowLength:(unsigned int)rowLength alignment:(unsigned int)alignment ``` |

Modified [+[SKTexture textureWithImage:]](https://developer.apple.com/documentation/spritekit/sktexture/1520136-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithImage:(NSImage *)image ``` |
| To | ``` + (instancetype _Nonnull)textureWithImage:(NSImage * _Nonnull)image ``` |

Modified [+[SKTexture textureWithImageNamed:]](https://developer.apple.com/documentation/spritekit/sktexture/1520086-texturewithimagenamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithImageNamed:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)textureWithImageNamed:(NSString * _Nonnull)name ``` |

Modified [+[SKTexture textureWithRect:inTexture:]](https://developer.apple.com/documentation/spritekit/sktexture/1520425-texturewithrect)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)textureWithRect:(CGRect)rect inTexture:(SKTexture *)texture ``` |
| To | ``` + (instancetype _Nonnull)textureWithRect:(CGRect)rect inTexture:(SKTexture * _Nonnull)texture ``` |

#### SKTextureAtlas.h

Added [+[SKTextureAtlas preloadTextureAtlasesNamed:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427377-preloadtextureatlasesnamed)Modified [+[SKTextureAtlas atlasNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427381-atlasnamed)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)atlasNamed:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)atlasNamed:(NSString * _Nonnull)name ``` |

Modified [+[SKTextureAtlas atlasWithDictionary:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427383-atlaswithdictionary)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)atlasWithDictionary:(NSDictionary *)properties ``` |
| To | ``` + (instancetype _Nonnull)atlasWithDictionary:(NSDictionary<NSString *,id> * _Nonnull)properties ``` |

Modified [+[SKTextureAtlas preloadTextureAtlases:withCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427379-preloadtextureatlases)

|  | Declaration |
| --- | --- |
| From | ``` + (void)preloadTextureAtlases:(NSArray *)textureAtlases withCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)preloadTextureAtlases:(NSArray<SKTextureAtlas *> * _Nonnull)textureAtlases withCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [-[SKTextureAtlas preloadWithCompletionHandler:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427385-preloadwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)preloadWithCompletionHandler:(void (^)(void))completionHandler ``` |
| To | ``` - (void)preloadWithCompletionHandler:(void (^ _Nonnull)(void))completionHandler ``` |

Modified [-[SKTextureAtlas textureNamed:]](https://developer.apple.com/documentation/spritekit/sktextureatlas/1427375-texturenamed)

|  | Declaration |
| --- | --- |
| From | ``` - (SKTexture *)textureNamed:(NSString *)name ``` |
| To | ``` - (SKTexture * _Nonnull)textureNamed:(NSString * _Nonnull)name ``` |

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

Modified [+[SKTransition crossFadeWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395897-crossfade)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)crossFadeWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)crossFadeWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition doorsCloseHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395899-doorsclosehorizontal)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)doorsCloseHorizontalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)doorsCloseHorizontalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition doorsCloseVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395914-doorscloseverticalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)doorsCloseVerticalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)doorsCloseVerticalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition doorsOpenHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395875-doorsopenhorizontalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)doorsOpenHorizontalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)doorsOpenHorizontalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition doorsOpenVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395909-doorsopenverticalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)doorsOpenVerticalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)doorsOpenVerticalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition doorwayWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395881-doorwaywithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)doorwayWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)doorwayWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition fadeWithColor:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395871-fade)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)fadeWithColor:(NSColor *)color duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)fadeWithColor:(NSColor * _Nonnull)color duration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition fadeWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395907-fadewithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)fadeWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)fadeWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition flipHorizontalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395901-fliphorizontalwithduration)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)flipHorizontalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)flipHorizontalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition flipVerticalWithDuration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395889-flipvertical)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)flipVerticalWithDuration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)flipVerticalWithDuration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition moveInWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395905-moveinwithdirection)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)moveInWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)moveInWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition pushWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395903-push)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)pushWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)pushWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition revealWithDirection:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395887-reveal)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)revealWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)revealWithDirection:(SKTransitionDirection)direction duration:(NSTimeInterval)sec ``` |

Modified [+[SKTransition transitionWithCIFilter:duration:]](https://developer.apple.com/documentation/spritekit/sktransition/1395895-init)

|  | Declaration |
| --- | --- |
| From | ``` + (SKTransition *)transitionWithCIFilter:(CIFilter *)filter duration:(NSTimeInterval)sec ``` |
| To | ``` + (SKTransition * _Nonnull)transitionWithCIFilter:(CIFilter * _Nonnull)filter duration:(NSTimeInterval)sec ``` |

#### SKUniform.h

Modified [-[SKUniform initWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455420-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name ``` |

Modified [-[SKUniform initWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455447-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name float:(float)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name float:(float)value ``` |

Modified [-[SKUniform initWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455431-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatMatrix2:(GLKMatrix2)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatMatrix2:(GLKMatrix2)value ``` |

Modified [-[SKUniform initWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455462-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatMatrix3:(GLKMatrix3)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatMatrix3:(GLKMatrix3)value ``` |

Modified [-[SKUniform initWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455429-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatMatrix4:(GLKMatrix4)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatMatrix4:(GLKMatrix4)value ``` |

Modified [-[SKUniform initWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455444-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatVector2:(GLKVector2)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatVector2:(GLKVector2)value ``` |

Modified [-[SKUniform initWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455416-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatVector3:(GLKVector3)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatVector3:(GLKVector3)value ``` |

Modified [-[SKUniform initWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455418-initwithname)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name floatVector4:(GLKVector4)value ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name floatVector4:(GLKVector4)value ``` |

Modified [-[SKUniform initWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455452-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithName:(NSString *)name texture:(SKTexture *)texture ``` |
| To | ``` - (instancetype _Nonnull)initWithName:(NSString * _Nonnull)name texture:(SKTexture * _Nullable)texture ``` |

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

Modified [+[SKUniform uniformWithName:]](https://developer.apple.com/documentation/spritekit/skuniform/1455458-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name ``` |

Modified [+[SKUniform uniformWithName:float:]](https://developer.apple.com/documentation/spritekit/skuniform/1455412-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name float:(float)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name float:(float)value ``` |

Modified [+[SKUniform uniformWithName:floatMatrix2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455463-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatMatrix2:(GLKMatrix2)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatMatrix2:(GLKMatrix2)value ``` |

Modified [+[SKUniform uniformWithName:floatMatrix3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455402-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatMatrix3:(GLKMatrix3)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatMatrix3:(GLKMatrix3)value ``` |

Modified [+[SKUniform uniformWithName:floatMatrix4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455446-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatMatrix4:(GLKMatrix4)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatMatrix4:(GLKMatrix4)value ``` |

Modified [+[SKUniform uniformWithName:floatVector2:]](https://developer.apple.com/documentation/spritekit/skuniform/1455472-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatVector2:(GLKVector2)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatVector2:(GLKVector2)value ``` |

Modified [+[SKUniform uniformWithName:floatVector3:]](https://developer.apple.com/documentation/spritekit/skuniform/1455414-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatVector3:(GLKVector3)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatVector3:(GLKVector3)value ``` |

Modified [+[SKUniform uniformWithName:floatVector4:]](https://developer.apple.com/documentation/spritekit/skuniform/1455465-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name floatVector4:(GLKVector4)value ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name floatVector4:(GLKVector4)value ``` |

Modified [+[SKUniform uniformWithName:texture:]](https://developer.apple.com/documentation/spritekit/skuniform/1455470-uniformwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)uniformWithName:(NSString *)name texture:(SKTexture *)texture ``` |
| To | ``` + (instancetype _Nonnull)uniformWithName:(NSString * _Nonnull)name texture:(SKTexture * _Nonnull)texture ``` |

#### SKVersion.h (Added)

Added #def SK_VERSION

#### SKVideoNode.h

Added [-[SKVideoNode initWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407922-init)Added [-[SKVideoNode initWithURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407898-init)Added [+[SKVideoNode videoNodeWithFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407924-videonodewithfilenamed)Added [+[SKVideoNode videoNodeWithURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407902-videonodewithurl)Modified [-[SKVideoNode initWithAVPlayer:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407900-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithAVPlayer:(AVPlayer *)player ``` |
| To | ``` - (instancetype _Nonnull)initWithAVPlayer:(AVPlayer * _Nonnull)player ``` |

Modified [-[SKVideoNode initWithCoder:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407907-initwithcoder)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCoder:(NSCoder *)aDecoder ``` |
| To | ``` - (instancetype _Nullable)initWithCoder:(NSCoder * _Nonnull)aDecoder ``` |

Modified [-[SKVideoNode initWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407918-init)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` - (instancetype)initWithVideoFileNamed:(NSString *)videoFile ``` | OS X 10.9 | -- |
| To | ``` - (instancetype _Nonnull)initWithVideoFileNamed:(NSString * _Nonnull)videoFile ``` | OS X 10.8 | OS X 10.10 |

Modified [-[SKVideoNode initWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407908-initwithvideourl)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` - (instancetype)initWithVideoURL:(NSURL *)url ``` | OS X 10.9 | -- |
| To | ``` - (instancetype _Nonnull)initWithVideoURL:(NSURL * _Nonnull)url ``` | OS X 10.8 | OS X 10.10 |

Modified [+[SKVideoNode videoNodeWithAVPlayer:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407920-videonodewithavplayer)

|  | Declaration |
| --- | --- |
| From | ``` + (SKVideoNode *)videoNodeWithAVPlayer:(AVPlayer *)player ``` |
| To | ``` + (SKVideoNode * _Nonnull)videoNodeWithAVPlayer:(AVPlayer * _Nonnull)player ``` |

Modified [+[SKVideoNode videoNodeWithVideoFileNamed:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407914-videonodewithvideofilenamed)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` + (SKVideoNode *)videoNodeWithVideoFileNamed:(NSString *)videoFile ``` | OS X 10.9 | -- |
| To | ``` + (SKVideoNode * _Nonnull)videoNodeWithVideoFileNamed:(NSString * _Nonnull)videoFile ``` | OS X 10.8 | OS X 10.10 |

Modified [+[SKVideoNode videoNodeWithVideoURL:]](https://developer.apple.com/documentation/spritekit/skvideonode/1407906-videonodewithvideourl)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` + (SKVideoNode *)videoNodeWithVideoURL:(NSURL *)videoURL ``` | OS X 10.9 | -- |
| To | ``` + (SKVideoNode * _Nonnull)videoNodeWithVideoURL:(NSURL * _Nonnull)videoURL ``` | OS X 10.8 | OS X 10.10 |

#### SKView.h

Modified [-[SKView convertPoint:fromScene:]](https://developer.apple.com/documentation/spritekit/skview/1520328-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)point fromScene:(SKScene *)scene ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)point fromScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKView convertPoint:toScene:]](https://developer.apple.com/documentation/spritekit/skview/1519847-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)point toScene:(SKScene *)scene ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)point toScene:(SKScene * _Nonnull)scene ``` |

Modified [-[SKView presentScene:]](https://developer.apple.com/documentation/spritekit/skview/1519705-presentscene)

|  | Declaration |
| --- | --- |
| From | ``` - (void)presentScene:(SKScene *)scene ``` |
| To | ``` - (void)presentScene:(SKScene * _Nullable)scene ``` |

Modified [-[SKView presentScene:transition:]](https://developer.apple.com/documentation/spritekit/skview/1520090-presentscene)

|  | Declaration |
| --- | --- |
| From | ``` - (void)presentScene:(SKScene *)scene transition:(SKTransition *)transition ``` |
| To | ``` - (void)presentScene:(SKScene * _Nonnull)scene transition:(SKTransition * _Nonnull)transition ``` |

Modified [SKView.scene](https://developer.apple.com/documentation/spritekit/skview/1520084-scene)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) SKScene *scene ``` |
| To | ``` @property(nonatomic, readonly, nullable) SKScene *scene ``` |

Modified [-[SKView textureFromNode:]](https://developer.apple.com/documentation/spritekit/skview/1520114-texture)

|  | Declaration |
| --- | --- |
| From | ``` - (SKTexture *)textureFromNode:(SKNode *)node ``` |
| To | ``` - (SKTexture * _Nullable)textureFromNode:(SKNode * _Nonnull)node ``` |

Modified [-[SKView textureFromNode:crop:]](https://developer.apple.com/documentation/spritekit/skview/1519994-texturefromnode)

|  | Declaration |
| --- | --- |
| From | ``` - (SKTexture *)textureFromNode:(SKNode *)node crop:(CGRect)crop ``` |
| To | ``` - (SKTexture * _Nullable)textureFromNode:(SKNode * _Nonnull)node crop:(CGRect)crop ``` |

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
