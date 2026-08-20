---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/QuartzCore.html
archived_at: '2026-07-18T02:53:11.475099Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# QuartzCore Changes for Objective-C

### QuartzCore

#### CAAnimation.h

Added [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)Added [CASpringAnimation.damping](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412532-damping)Added [CASpringAnimation.initialVelocity](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412443-initialvelocity)Added [CASpringAnimation.mass](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412540-mass)Added [CASpringAnimation.settlingDuration](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412524-settlingduration)Added [CASpringAnimation.stiffness](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412515-stiffness)Modified [+[CAAnimation animation]](https://developer.apple.com/documentation/quartzcore/caanimation/1412479-animation)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)animation ``` |
| To | ``` + (instancetype _Nonnull)animation ``` |

Modified [+[CAAnimation defaultValueForKey:]](https://developer.apple.com/documentation/quartzcore/caanimation/1412530-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultValueForKey:(NSString *)key ``` |
| To | ``` + (id _Nullable)defaultValueForKey:(NSString * _Nonnull)key ``` |

Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id delegate ``` |
| To | ``` @property(strong, nullable) id delegate ``` |

Modified [-[CAAnimation shouldArchiveValueForKey:]](https://developer.apple.com/documentation/quartzcore/caanimation/1412525-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldArchiveValueForKey:(NSString *)key ``` |
| To | ``` - (BOOL)shouldArchiveValueForKey:(NSString * _Nonnull)key ``` |

Modified [CAAnimation.timingFunction](https://developer.apple.com/documentation/quartzcore/caanimation/1412456-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) CAMediaTimingFunction *timingFunction ``` |
| To | ``` @property(strong, nullable) CAMediaTimingFunction *timingFunction ``` |

Modified [CAAnimationGroup.animations](https://developer.apple.com/documentation/quartzcore/caanimationgroup/1412516-animations)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *animations ``` |
| To | ``` @property(copy, nullable) NSArray<CAAnimation *> *animations ``` |

Modified [CABasicAnimation.byValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412445-byvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id byValue ``` |
| To | ``` @property(strong, nullable) id byValue ``` |

Modified [CABasicAnimation.fromValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412519-fromvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id fromValue ``` |
| To | ``` @property(strong, nullable) id fromValue ``` |

Modified [CABasicAnimation.toValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412523-tovalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id toValue ``` |
| To | ``` @property(strong, nullable) id toValue ``` |

Modified [CAKeyframeAnimation.biasValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412485-biasvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *biasValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *biasValues ``` |

Modified [CAKeyframeAnimation.calculationMode](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412500-calculationmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *calculationMode ``` |
| To | ``` @property(copy, nonnull) NSString *calculationMode ``` |

Modified [CAKeyframeAnimation.continuityValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412491-continuityvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *continuityValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *continuityValues ``` |

Modified [CAKeyframeAnimation.keyTimes](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412522-keytimes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *keyTimes ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *keyTimes ``` |

Modified [CAKeyframeAnimation.path](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412474-path)

|  | Declaration |
| --- | --- |
| From | ``` @property CGPathRef path ``` |
| To | ``` @property(nullable) CGPathRef path ``` |

Modified [CAKeyframeAnimation.rotationMode](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412454-rotationmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *rotationMode ``` |
| To | ``` @property(copy, nullable) NSString *rotationMode ``` |

Modified [CAKeyframeAnimation.tensionValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412475-tensionvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *tensionValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *tensionValues ``` |

Modified [CAKeyframeAnimation.timingFunctions](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412465-timingfunctions)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *timingFunctions ``` |
| To | ``` @property(copy, nullable) NSArray<CAMediaTimingFunction *> *timingFunctions ``` |

Modified [CAKeyframeAnimation.values](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412498-values)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *values ``` |
| To | ``` @property(copy, nullable) NSArray *values ``` |

Modified [+[CAPropertyAnimation animationWithKeyPath:]](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412534-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)animationWithKeyPath:(NSString *)path ``` |
| To | ``` + (instancetype _Nonnull)animationWithKeyPath:(NSString * _Nullable)path ``` |

Modified [CAPropertyAnimation.keyPath](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412496-keypath)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *keyPath ``` |
| To | ``` @property(copy, nullable) NSString *keyPath ``` |

Modified [CAPropertyAnimation.valueFunction](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412447-valuefunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) CAValueFunction *valueFunction ``` |
| To | ``` @property(strong, nullable) CAValueFunction *valueFunction ``` |

Modified [CATransition.filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id filter ``` |
| To | ``` @property(strong, nullable) id filter ``` |

Modified [CATransition.subtype](https://developer.apple.com/documentation/quartzcore/catransition/1412467-subtype)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *subtype ``` |
| To | ``` @property(copy, nullable) NSString *subtype ``` |

Modified [CATransition.type](https://developer.apple.com/documentation/quartzcore/catransition/1412502-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *type ``` |
| To | ``` @property(copy, nonnull) NSString *type ``` |

Modified -[NSObject animationDidStart:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)animationDidStart:(CAAnimation *)anim ``` |
| To | ``` - (void)animationDidStart:(CAAnimation * _Nonnull)anim ``` |

Modified -[NSObject animationDidStop:finished:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)animationDidStop:(CAAnimation *)anim finished:(BOOL)flag ``` |
| To | ``` - (void)animationDidStop:(CAAnimation * _Nonnull)anim finished:(BOOL)flag ``` |

#### CACIFilterAdditions.h (Removed)

Removed CIFilter(CACIFilterAdditions)Modified [CIFilter.enabled](https://developer.apple.com/documentation/coreimage/cifilter/1438276-enabled)

|  | Header |
| --- | --- |
| From | QuartzCore/CACIFilterAdditions.h |
| To | CoreImage/CIFilter.h |

Modified [CIFilter.name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(copy) NSString *name ``` | QuartzCore/CACIFilterAdditions.h |
| To | ``` @property(nonatomic, copy, nonnull) NSString *name ``` | CoreImage/CIFilter.h |

#### CAConstraintLayoutManager.h

Modified [+[CAConstraint constraintWithAttribute:relativeTo:attribute:]](https://developer.apple.com/documentation/quartzcore/caconstraint/1521924-constraintwithattribute)

|  | Declaration |
| --- | --- |
| From | ``` + (id)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString *)srcId attribute:(CAConstraintAttribute)srcAttr ``` |
| To | ``` + (instancetype _Nonnull)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString * _Nonnull)srcId attribute:(CAConstraintAttribute)srcAttr ``` |

Modified [+[CAConstraint constraintWithAttribute:relativeTo:attribute:offset:]](https://developer.apple.com/documentation/quartzcore/caconstraint/1522328-constraintwithattribute)

|  | Declaration |
| --- | --- |
| From | ``` + (id)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString *)srcId attribute:(CAConstraintAttribute)srcAttr offset:(CGFloat)c ``` |
| To | ``` + (instancetype _Nonnull)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString * _Nonnull)srcId attribute:(CAConstraintAttribute)srcAttr offset:(CGFloat)c ``` |

Modified [+[CAConstraint constraintWithAttribute:relativeTo:attribute:scale:offset:]](https://developer.apple.com/documentation/quartzcore/caconstraint/1574941-constraintwithattribute)

|  | Declaration |
| --- | --- |
| From | ``` + (id)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString *)srcId attribute:(CAConstraintAttribute)srcAttr scale:(CGFloat)m offset:(CGFloat)c ``` |
| To | ``` + (instancetype _Nonnull)constraintWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString * _Nonnull)srcId attribute:(CAConstraintAttribute)srcAttr scale:(CGFloat)m offset:(CGFloat)c ``` |

Modified [-[CAConstraint initWithAttribute:relativeTo:attribute:scale:offset:]](https://developer.apple.com/documentation/quartzcore/caconstraint/1522213-initwithattribute)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString *)srcId attribute:(CAConstraintAttribute)srcAttr scale:(CGFloat)m offset:(CGFloat)c ``` |
| To | ``` - (instancetype _Nonnull)initWithAttribute:(CAConstraintAttribute)attr relativeTo:(NSString * _Nonnull)srcId attribute:(CAConstraintAttribute)srcAttr scale:(CGFloat)m offset:(CGFloat)c ``` |

Modified [CAConstraint.sourceName](https://developer.apple.com/documentation/quartzcore/caconstraint/1522224-sourcename)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *sourceName ``` |
| To | ``` @property(readonly, nonnull) NSString *sourceName ``` |

Modified [+[CAConstraintLayoutManager layoutManager]](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager/1574940-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` + (id)layoutManager ``` |
| To | ``` + (instancetype _Nonnull)layoutManager ``` |

Modified [-[CALayer addConstraint:]](https://developer.apple.com/documentation/quartzcore/calayer/1521899-addconstraint)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addConstraint:(CAConstraint *)c ``` |
| To | ``` - (void)addConstraint:(CAConstraint * _Nonnull)c ``` |

Modified [CALayer.constraints](https://developer.apple.com/documentation/quartzcore/calayer/1521906-constraints)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *constraints ``` |
| To | ``` @property(copy, nullable) NSArray<CAConstraint *> *constraints ``` |

#### CAEmitterBehavior.h

Modified +[CAEmitterBehavior attributesForKey:]

|  | Declaration |
| --- | --- |
| From | ``` + (NSDictionary *)attributesForKey:(NSString *)key ``` |
| To | ``` + (NSDictionary * _Nonnull)attributesForKey:(NSString * _Nonnull)key ``` |

Modified -[CAEmitterBehavior attributesForKeyPath:]

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)attributesForKeyPath:(NSString *)keyPath ``` |
| To | ``` - (NSDictionary * _Nonnull)attributesForKeyPath:(NSString * _Nonnull)keyPath ``` |

Modified +[CAEmitterBehavior behaviorTypes]

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)behaviorTypes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)behaviorTypes ``` |

Modified +[CAEmitterBehavior behaviorWithType:]

|  | Declaration |
| --- | --- |
| From | ``` + (CAEmitterBehavior *)behaviorWithType:(NSString *)type ``` |
| To | ``` + (CAEmitterBehavior * _Nonnull)behaviorWithType:(NSString * _Nonnull)type ``` |

Modified -[CAEmitterBehavior initWithType:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithType:(NSString *)type ``` |
| To | ``` - (id _Nonnull)initWithType:(NSString * _Nonnull)type ``` |

Modified -[CAEmitterBehavior inputKeys]

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)inputKeys ``` |
| To | ``` - (NSArray * _Nonnull)inputKeys ``` |

Modified CAEmitterBehavior.name

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified CAEmitterBehavior.type

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *type ``` |
| To | ``` @property(readonly, nonnull) NSString *type ``` |

#### CAEmitterCell.h

Added [CAEmitterCell.contentsScale](https://developer.apple.com/documentation/quartzcore/caemittercell/1522197-contentsscale)Modified [CAEmitterCell.color](https://developer.apple.com/documentation/quartzcore/caemittercell/1522322-color)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef color ``` |
| To | ``` @property(nullable) CGColorRef color ``` |

Modified [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id contents ``` |
| To | ``` @property(strong, nullable) id contents ``` |

Modified [+[CAEmitterCell defaultValueForKey:]](https://developer.apple.com/documentation/quartzcore/caemittercell/1521964-defaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultValueForKey:(NSString *)key ``` |
| To | ``` + (id _Nullable)defaultValueForKey:(NSString * _Nonnull)key ``` |

Modified [+[CAEmitterCell emitterCell]](https://developer.apple.com/documentation/quartzcore/caemittercell/1584370-emittercell)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)emitterCell ``` |
| To | ``` + (instancetype _Nonnull)emitterCell ``` |

Modified [CAEmitterCell.emitterCells](https://developer.apple.com/documentation/quartzcore/caemittercell/1521866-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *emitterCells ``` |
| To | ``` @property(copy, nullable) NSArray<CAEmitterCell *> *emitterCells ``` |

Modified [CAEmitterCell.magnificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522228-magnificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *magnificationFilter ``` |
| To | ``` @property(copy, nonnull) NSString *magnificationFilter ``` |

Modified [CAEmitterCell.minificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522222-minificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *minificationFilter ``` |
| To | ``` @property(copy, nonnull) NSString *minificationFilter ``` |

Modified [CAEmitterCell.name](https://developer.apple.com/documentation/quartzcore/caemittercell/1521909-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [-[CAEmitterCell shouldArchiveValueForKey:]](https://developer.apple.com/documentation/quartzcore/caemittercell/1522005-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldArchiveValueForKey:(NSString *)key ``` |
| To | ``` - (BOOL)shouldArchiveValueForKey:(NSString * _Nonnull)key ``` |

Modified [CAEmitterCell.style](https://developer.apple.com/documentation/quartzcore/caemittercell/1521925-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *style ``` |
| To | ``` @property(copy, nullable) NSDictionary *style ``` |

#### CAEmitterLayer.h

Modified [CAEmitterLayer.emitterCells](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521923-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *emitterCells ``` |
| To | ``` @property(copy, nullable) NSArray<CAEmitterCell *> *emitterCells ``` |

Modified [CAEmitterLayer.emitterMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522128-emittermode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *emitterMode ``` |
| To | ``` @property(copy, nonnull) NSString *emitterMode ``` |

Modified [CAEmitterLayer.emitterShape](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521919-emittershape)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *emitterShape ``` |
| To | ``` @property(copy, nonnull) NSString *emitterShape ``` |

Modified [CAEmitterLayer.renderMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522104-rendermode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *renderMode ``` |
| To | ``` @property(copy, nonnull) NSString *renderMode ``` |

#### CAGradientLayer.h

Modified [CAGradientLayer.colors](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462403-colors)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *colors ``` |
| To | ``` @property(copy, nullable) NSArray *colors ``` |

Modified [CAGradientLayer.locations](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462410-locations)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *locations ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *locations ``` |

Modified [CAGradientLayer.type](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462413-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *type ``` |
| To | ``` @property(copy, nonnull) NSString *type ``` |

#### CALayer.h

Added NSNull(CAActionAdditions)Modified [-[CAAction runActionForKey:object:arguments:]](https://developer.apple.com/documentation/quartzcore/caaction/1410806-run)

|  | Declaration |
| --- | --- |
| From | ``` - (void)runActionForKey:(NSString *)event object:(id)anObject arguments:(NSDictionary *)dict ``` |
| To | ``` - (void)runActionForKey:(NSString * _Nonnull)event object:(id _Nonnull)anObject arguments:(NSDictionary * _Nullable)dict ``` |

Modified [-[CALayer actionForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410844-action)

|  | Declaration |
| --- | --- |
| From | ``` - (id<CAAction>)actionForKey:(NSString *)event ``` |
| To | ``` - (id<CAAction> _Nullable)actionForKey:(NSString * _Nonnull)event ``` |

Modified [CALayer.actions](https://developer.apple.com/documentation/quartzcore/calayer/1410789-actions)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *actions ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id<CAAction>> *actions ``` |

Modified [-[CALayer addAnimation:forKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410848-addanimation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addAnimation:(CAAnimation *)anim forKey:(NSString *)key ``` |
| To | ``` - (void)addAnimation:(CAAnimation * _Nonnull)anim forKey:(NSString * _Nullable)key ``` |

Modified [-[CALayer addSublayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410833-addsublayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addSublayer:(CALayer *)layer ``` |
| To | ``` - (void)addSublayer:(CALayer * _Nonnull)layer ``` |

Modified [-[CALayer animationForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410808-animationforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (CAAnimation *)animationForKey:(NSString *)key ``` |
| To | ``` - (CAAnimation * _Nullable)animationForKey:(NSString * _Nonnull)key ``` |

Modified [-[CALayer animationKeys]](https://developer.apple.com/documentation/quartzcore/calayer/1410937-animationkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)animationKeys ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)animationKeys ``` |

Modified [CALayer.backgroundColor](https://developer.apple.com/documentation/quartzcore/calayer/1410966-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef backgroundColor ``` |
| To | ``` @property(nullable) CGColorRef backgroundColor ``` |

Modified [CALayer.backgroundFilters](https://developer.apple.com/documentation/quartzcore/calayer/1410827-backgroundfilters)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *backgroundFilters ``` |
| To | ``` @property(copy, nullable) NSArray *backgroundFilters ``` |

Modified [CALayer.borderColor](https://developer.apple.com/documentation/quartzcore/calayer/1410903-bordercolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef borderColor ``` |
| To | ``` @property(nullable) CGColorRef borderColor ``` |

Modified [CALayer.compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id compositingFilter ``` |
| To | ``` @property(strong, nullable) id compositingFilter ``` |

Modified [CALayer.contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id contents ``` |
| To | ``` @property(strong, nullable) id contents ``` |

Modified [CALayer.contentsGravity](https://developer.apple.com/documentation/quartzcore/calayer/1410872-contentsgravity)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *contentsGravity ``` |
| To | ``` @property(copy, nonnull) NSString *contentsGravity ``` |

Modified [-[CALayer convertPoint:fromLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410825-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)p fromLayer:(CALayer *)l ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)p fromLayer:(CALayer * _Nullable)l ``` |

Modified [-[CALayer convertPoint:toLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410881-convert)

|  | Declaration |
| --- | --- |
| From | ``` - (CGPoint)convertPoint:(CGPoint)p toLayer:(CALayer *)l ``` |
| To | ``` - (CGPoint)convertPoint:(CGPoint)p toLayer:(CALayer * _Nullable)l ``` |

Modified [-[CALayer convertRect:fromLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410948-convertrect)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)convertRect:(CGRect)r fromLayer:(CALayer *)l ``` |
| To | ``` - (CGRect)convertRect:(CGRect)r fromLayer:(CALayer * _Nullable)l ``` |

Modified [-[CALayer convertRect:toLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410742-convertrect)

|  | Declaration |
| --- | --- |
| From | ``` - (CGRect)convertRect:(CGRect)r toLayer:(CALayer *)l ``` |
| To | ``` - (CGRect)convertRect:(CGRect)r toLayer:(CALayer * _Nullable)l ``` |

Modified [-[CALayer convertTime:fromLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410821-converttime)

|  | Declaration |
| --- | --- |
| From | ``` - (CFTimeInterval)convertTime:(CFTimeInterval)t fromLayer:(CALayer *)l ``` |
| To | ``` - (CFTimeInterval)convertTime:(CFTimeInterval)t fromLayer:(CALayer * _Nullable)l ``` |

Modified [-[CALayer convertTime:toLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410823-converttime)

|  | Declaration |
| --- | --- |
| From | ``` - (CFTimeInterval)convertTime:(CFTimeInterval)t toLayer:(CALayer *)l ``` |
| To | ``` - (CFTimeInterval)convertTime:(CFTimeInterval)t toLayer:(CALayer * _Nullable)l ``` |

Modified [+[CALayer defaultActionForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410954-defaultactionforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id<CAAction>)defaultActionForKey:(NSString *)event ``` |
| To | ``` + (id<CAAction> _Nullable)defaultActionForKey:(NSString * _Nonnull)event ``` |

Modified [+[CALayer defaultValueForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410886-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (id)defaultValueForKey:(NSString *)key ``` |
| To | ``` + (id _Nullable)defaultValueForKey:(NSString * _Nonnull)key ``` |

Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id delegate ``` |
| To | ``` @property(weak, nullable) id delegate ``` |

Modified [-[CALayer drawInContext:]](https://developer.apple.com/documentation/quartzcore/calayer/1410757-draw)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawInContext:(CGContextRef)ctx ``` |
| To | ``` - (void)drawInContext:(CGContextRef _Nonnull)ctx ``` |

Modified [CALayer.filters](https://developer.apple.com/documentation/quartzcore/calayer/1410901-filters)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *filters ``` |
| To | ``` @property(copy, nullable) NSArray *filters ``` |

Modified [-[CALayer hitTest:]](https://developer.apple.com/documentation/quartzcore/calayer/1410972-hittest)

|  | Declaration |
| --- | --- |
| From | ``` - (CALayer *)hitTest:(CGPoint)p ``` |
| To | ``` - (CALayer * _Nullable)hitTest:(CGPoint)p ``` |

Modified [-[CALayer init]](https://developer.apple.com/documentation/quartzcore/calayer/1410835-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

Modified [-[CALayer initWithLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410842-initwithlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLayer:(id)layer ``` |
| To | ``` - (instancetype _Nonnull)initWithLayer:(id _Nonnull)layer ``` |

Modified [-[CALayer insertSublayer:above:]](https://developer.apple.com/documentation/quartzcore/calayer/1410798-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertSublayer:(CALayer *)layer above:(CALayer *)sibling ``` |
| To | ``` - (void)insertSublayer:(CALayer * _Nonnull)layer above:(CALayer * _Nullable)sibling ``` |

Modified [-[CALayer insertSublayer:atIndex:]](https://developer.apple.com/documentation/quartzcore/calayer/1410944-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertSublayer:(CALayer *)layer atIndex:(unsigned int)idx ``` |
| To | ``` - (void)insertSublayer:(CALayer * _Nonnull)layer atIndex:(unsigned int)idx ``` |

Modified [-[CALayer insertSublayer:below:]](https://developer.apple.com/documentation/quartzcore/calayer/1410840-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)insertSublayer:(CALayer *)layer below:(CALayer *)sibling ``` |
| To | ``` - (void)insertSublayer:(CALayer * _Nonnull)layer below:(CALayer * _Nullable)sibling ``` |

Modified [+[CALayer layer]](https://developer.apple.com/documentation/quartzcore/calayer/1410793-layer)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)layer ``` |
| To | ``` + (instancetype _Nonnull)layer ``` |

Modified [CALayer.layoutManager](https://developer.apple.com/documentation/quartzcore/calayer/1410749-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id layoutManager ``` |
| To | ``` @property(strong, nullable) id layoutManager ``` |

Modified [CALayer.magnificationFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410907-magnificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *magnificationFilter ``` |
| To | ``` @property(copy, nonnull) NSString *magnificationFilter ``` |

Modified [CALayer.mask](https://developer.apple.com/documentation/quartzcore/calayer/1410861-mask)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) CALayer *mask ``` |
| To | ``` @property(strong, nullable) CALayer *mask ``` |

Modified [CALayer.minificationFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410898-minificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *minificationFilter ``` |
| To | ``` @property(copy, nonnull) NSString *minificationFilter ``` |

Modified [-[CALayer modelLayer]](https://developer.apple.com/documentation/quartzcore/calayer/1410853-modellayer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)modelLayer ``` |
| To | ``` - (id _Nonnull)modelLayer ``` |

Modified [CALayer.name](https://developer.apple.com/documentation/quartzcore/calayer/1410879-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *name ``` |
| To | ``` @property(copy, nullable) NSString *name ``` |

Modified [+[CALayer needsDisplayForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410769-needsdisplayforkey)

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)needsDisplayForKey:(NSString *)key ``` |
| To | ``` + (BOOL)needsDisplayForKey:(NSString * _Nonnull)key ``` |

Modified [-[CALayer presentationLayer]](https://developer.apple.com/documentation/quartzcore/calayer/1410744-presentation)

|  | Declaration |
| --- | --- |
| From | ``` - (id)presentationLayer ``` |
| To | ``` - (id _Nullable)presentationLayer ``` |

Modified [-[CALayer removeAnimationForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410939-removeanimation)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeAnimationForKey:(NSString *)key ``` |
| To | ``` - (void)removeAnimationForKey:(NSString * _Nonnull)key ``` |

Modified [-[CALayer renderInContext:]](https://developer.apple.com/documentation/quartzcore/calayer/1410909-renderincontext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)renderInContext:(CGContextRef)ctx ``` |
| To | ``` - (void)renderInContext:(CGContextRef _Nonnull)ctx ``` |

Modified [-[CALayer replaceSublayer:with:]](https://developer.apple.com/documentation/quartzcore/calayer/1410820-replacesublayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replaceSublayer:(CALayer *)layer with:(CALayer *)layer2 ``` |
| To | ``` - (void)replaceSublayer:(CALayer * _Nonnull)layer with:(CALayer * _Nonnull)layer2 ``` |

Modified [CALayer.shadowColor](https://developer.apple.com/documentation/quartzcore/calayer/1410829-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef shadowColor ``` |
| To | ``` @property(nullable) CGColorRef shadowColor ``` |

Modified [CALayer.shadowPath](https://developer.apple.com/documentation/quartzcore/calayer/1410771-shadowpath)

|  | Declaration |
| --- | --- |
| From | ``` @property CGPathRef shadowPath ``` |
| To | ``` @property(nullable) CGPathRef shadowPath ``` |

Modified [-[CALayer shouldArchiveValueForKey:]](https://developer.apple.com/documentation/quartzcore/calayer/1410753-shouldarchivevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)shouldArchiveValueForKey:(NSString *)key ``` |
| To | ``` - (BOOL)shouldArchiveValueForKey:(NSString * _Nonnull)key ``` |

Modified [CALayer.style](https://developer.apple.com/documentation/quartzcore/calayer/1410875-style)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *style ``` |
| To | ``` @property(copy, nullable) NSDictionary *style ``` |

Modified [CALayer.sublayers](https://developer.apple.com/documentation/quartzcore/calayer/1410802-sublayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *sublayers ``` |
| To | ``` @property(copy, nullable) NSArray<CALayer *> *sublayers ``` |

Modified [CALayer.superlayer](https://developer.apple.com/documentation/quartzcore/calayer/1410761-superlayer)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) CALayer *superlayer ``` |
| To | ``` @property(readonly, nullable) CALayer *superlayer ``` |

Modified -[NSObject actionForLayer:forKey:]

|  | Declaration |
| --- | --- |
| From | ``` - (id<CAAction>)actionForLayer:(CALayer *)layer forKey:(NSString *)event ``` |
| To | ``` - (id<CAAction> _Nullable)actionForLayer:(CALayer * _Nonnull)layer forKey:(NSString * _Nonnull)event ``` |

Modified -[NSObject displayLayer:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)displayLayer:(CALayer *)layer ``` |
| To | ``` - (void)displayLayer:(CALayer * _Nonnull)layer ``` |

Modified -[NSObject drawLayer:inContext:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawLayer:(CALayer *)layer inContext:(CGContextRef)ctx ``` |
| To | ``` - (void)drawLayer:(CALayer * _Nonnull)layer inContext:(CGContextRef _Nonnull)ctx ``` |

Modified -[NSObject invalidateLayoutOfLayer:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)invalidateLayoutOfLayer:(CALayer *)layer ``` |
| To | ``` - (void)invalidateLayoutOfLayer:(CALayer * _Nonnull)layer ``` |

Modified -[NSObject layoutSublayersOfLayer:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)layoutSublayersOfLayer:(CALayer *)layer ``` |
| To | ``` - (void)layoutSublayersOfLayer:(CALayer * _Nonnull)layer ``` |

Modified -[NSObject preferredSizeOfLayer:]

|  | Declaration |
| --- | --- |
| From | ``` - (CGSize)preferredSizeOfLayer:(CALayer *)layer ``` |
| To | ``` - (CGSize)preferredSizeOfLayer:(CALayer * _Nonnull)layer ``` |

#### CAMediaTiming.h

Removed [kCAFillModeFrozen](https://developer.apple.com/documentation/quartzcore/camediatiming/fill_modes/kcafillmodefrozen)Modified [CAMediaTiming.fillMode](https://developer.apple.com/documentation/quartzcore/camediatiming/1427656-fillmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *fillMode ``` |
| To | ``` @property(copy, nonnull) NSString *fillMode ``` |

#### CAMediaTimingFunction.h

Modified [+[CAMediaTimingFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1521979-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype _Nonnull)functionWithName:(NSString * _Nonnull)name ``` |

#### CAMetalLayer.h (Added)

Added [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable)Added [CAMetalDrawable.layer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478165-layer)Added [CAMetalDrawable.texture](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478159-texture)Added [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)Added [CAMetalLayer.colorspace](https://developer.apple.com/documentation/quartzcore/cametallayer/1478170-colorspace)Added [CAMetalLayer.device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device)Added [CAMetalLayer.drawableSize](https://developer.apple.com/documentation/quartzcore/cametallayer/1478174-drawablesize)Added [CAMetalLayer.framebufferOnly](https://developer.apple.com/documentation/quartzcore/cametallayer/1478168-framebufferonly)Added [-[CAMetalLayer nextDrawable]](https://developer.apple.com/documentation/quartzcore/cametallayer/1478172-nextdrawable)Added [CAMetalLayer.pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat)Added [CAMetalLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/cametallayer/1478157-presentswithtransaction)Added [CAMetalLayer.wantsExtendedDynamicRangeContent](https://developer.apple.com/documentation/quartzcore/cametallayer/1478161-wantsextendeddynamicrangecontent)

#### CAOpenGLLayer.h

Added [CAOpenGLLayer.colorspace](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521873-colorspace)Added [CAOpenGLLayer.wantsExtendedDynamicRangeContent](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521900-wantsextendeddynamicrangecontent)Modified [-[CAOpenGLLayer canDrawInCGLContext:pixelFormat:forLayerTime:displayTime:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1522184-candraw)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)canDrawInCGLContext:(CGLContextObj)ctx pixelFormat:(CGLPixelFormatObj)pf forLayerTime:(CFTimeInterval)t displayTime:(const CVTimeStamp *)ts ``` |
| To | ``` - (BOOL)canDrawInCGLContext:(CGLContextObj _Nonnull)ctx pixelFormat:(CGLPixelFormatObj _Nonnull)pf forLayerTime:(CFTimeInterval)t displayTime:(const CVTimeStamp * _Nonnull)ts ``` |

Modified [-[CAOpenGLLayer copyCGLContextForPixelFormat:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521894-copycglcontextforpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` - (CGLContextObj)copyCGLContextForPixelFormat:(CGLPixelFormatObj)pf ``` |
| To | ``` - (CGLContextObj _Nonnull)copyCGLContextForPixelFormat:(CGLPixelFormatObj _Nonnull)pf ``` |

Modified [-[CAOpenGLLayer copyCGLPixelFormatForDisplayMask:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1522052-copycglpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` - (CGLPixelFormatObj)copyCGLPixelFormatForDisplayMask:(uint32_t)mask ``` |
| To | ``` - (CGLPixelFormatObj _Nonnull)copyCGLPixelFormatForDisplayMask:(uint32_t)mask ``` |

Modified [-[CAOpenGLLayer drawInCGLContext:pixelFormat:forLayerTime:displayTime:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1522316-draw)

|  | Declaration |
| --- | --- |
| From | ``` - (void)drawInCGLContext:(CGLContextObj)ctx pixelFormat:(CGLPixelFormatObj)pf forLayerTime:(CFTimeInterval)t displayTime:(const CVTimeStamp *)ts ``` |
| To | ``` - (void)drawInCGLContext:(CGLContextObj _Nonnull)ctx pixelFormat:(CGLPixelFormatObj _Nonnull)pf forLayerTime:(CFTimeInterval)t displayTime:(const CVTimeStamp * _Nonnull)ts ``` |

Modified [-[CAOpenGLLayer releaseCGLContext:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521850-releasecglcontext)

|  | Declaration |
| --- | --- |
| From | ``` - (void)releaseCGLContext:(CGLContextObj)ctx ``` |
| To | ``` - (void)releaseCGLContext:(CGLContextObj _Nonnull)ctx ``` |

Modified [-[CAOpenGLLayer releaseCGLPixelFormat:]](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521910-releasecglpixelformat)

|  | Declaration |
| --- | --- |
| From | ``` - (void)releaseCGLPixelFormat:(CGLPixelFormatObj)pf ``` |
| To | ``` - (void)releaseCGLPixelFormat:(CGLPixelFormatObj _Nonnull)pf ``` |

#### CARemoteLayerClient.h

Modified [-[CARemoteLayerClient initWithServerPort:]](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418377-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithServerPort:(mach_port_t)port ``` |
| To | ``` - (instancetype _Nonnull)initWithServerPort:(mach_port_t)port ``` |

Modified [CARemoteLayerClient.layer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418373-layer)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) CALayer *layer ``` |
| To | ``` @property(strong, nullable) CALayer *layer ``` |

#### CARemoteLayerServer.h

Modified [+[CALayer layerWithRemoteClientId:]](https://developer.apple.com/documentation/quartzcore/calayer/1522119-layerwithremoteclientid)

|  | Declaration |
| --- | --- |
| From | ``` + (CALayer *)layerWithRemoteClientId:(uint32_t)client_id ``` |
| To | ``` + (CALayer * _Nonnull)layerWithRemoteClientId:(uint32_t)client_id ``` |

Modified [+[CARemoteLayerServer sharedServer]](https://developer.apple.com/documentation/quartzcore/caremotelayerserver/1521954-sharedserver)

|  | Declaration |
| --- | --- |
| From | ``` + (CARemoteLayerServer *)sharedServer ``` |
| To | ``` + (CARemoteLayerServer * _Nonnull)sharedServer ``` |

#### CARenderer.h

Modified [-[CARenderer beginFrameAtTime:timeStamp:]](https://developer.apple.com/documentation/quartzcore/carenderer/1519595-beginframe)

|  | Declaration |
| --- | --- |
| From | ``` - (void)beginFrameAtTime:(CFTimeInterval)t timeStamp:(CVTimeStamp *)ts ``` |
| To | ``` - (void)beginFrameAtTime:(CFTimeInterval)t timeStamp:(CVTimeStamp * _Nullable)ts ``` |

Modified [CARenderer.layer](https://developer.apple.com/documentation/quartzcore/carenderer/1519583-layer)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) CALayer *layer ``` |
| To | ``` @property(strong, nullable) CALayer *layer ``` |

Modified [+[CARenderer rendererWithCGLContext:options:]](https://developer.apple.com/documentation/quartzcore/carenderer/1519589-rendererwithcglcontext)

|  | Declaration |
| --- | --- |
| From | ``` + (CARenderer *)rendererWithCGLContext:(void *)ctx options:(NSDictionary *)dict ``` |
| To | ``` + (CARenderer * _Nonnull)rendererWithCGLContext:(void * _Nonnull)ctx options:(NSDictionary * _Nullable)dict ``` |

#### CAReplicatorLayer.h

Modified [CAReplicatorLayer.instanceColor](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/1522154-instancecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef instanceColor ``` |
| To | ``` @property(nullable) CGColorRef instanceColor ``` |

#### CAScrollLayer.h

Modified [CAScrollLayer.scrollMode](https://developer.apple.com/documentation/quartzcore/cascrolllayer/1522111-scrollmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *scrollMode ``` |
| To | ``` @property(copy, nonnull) NSString *scrollMode ``` |

#### CAShapeLayer.h

Modified [CAShapeLayer.fillColor](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522248-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef fillColor ``` |
| To | ``` @property(nullable) CGColorRef fillColor ``` |

Modified [CAShapeLayer.fillRule](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522146-fillrule)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *fillRule ``` |
| To | ``` @property(copy, nonnull) NSString *fillRule ``` |

Modified [CAShapeLayer.lineCap](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521905-linecap)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *lineCap ``` |
| To | ``` @property(copy, nonnull) NSString *lineCap ``` |

Modified [CAShapeLayer.lineDashPattern](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521921-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *lineDashPattern ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *lineDashPattern ``` |

Modified [CAShapeLayer.lineJoin](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522147-linejoin)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *lineJoin ``` |
| To | ``` @property(copy, nonnull) NSString *lineJoin ``` |

Modified [CAShapeLayer.path](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521904-path)

|  | Declaration |
| --- | --- |
| From | ``` @property CGPathRef path ``` |
| To | ``` @property(nullable) CGPathRef path ``` |

Modified [CAShapeLayer.strokeColor](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521897-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef strokeColor ``` |
| To | ``` @property(nullable) CGColorRef strokeColor ``` |

#### CATextLayer.h

Added [CATextLayer.allowsFontSubpixelQuantization](https://developer.apple.com/documentation/quartzcore/catextlayer/1515300-allowsfontsubpixelquantization)Modified [CATextLayer.alignmentMode](https://developer.apple.com/documentation/quartzcore/catextlayer/1515301-alignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *alignmentMode ``` |
| To | ``` @property(copy, nonnull) NSString *alignmentMode ``` |

Modified [CATextLayer.font](https://developer.apple.com/documentation/quartzcore/catextlayer/1515303-font)

|  | Declaration |
| --- | --- |
| From | ``` @property CFTypeRef font ``` |
| To | ``` @property(nullable) CFTypeRef font ``` |

Modified [CATextLayer.foregroundColor](https://developer.apple.com/documentation/quartzcore/catextlayer/1515305-foregroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` @property CGColorRef foregroundColor ``` |
| To | ``` @property(nullable) CGColorRef foregroundColor ``` |

Modified [CATextLayer.string](https://developer.apple.com/documentation/quartzcore/catextlayer/1515295-string)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) id string ``` |
| To | ``` @property(copy, nullable) id string ``` |

Modified [CATextLayer.truncationMode](https://developer.apple.com/documentation/quartzcore/catextlayer/1515296-truncationmode)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *truncationMode ``` |
| To | ``` @property(copy, nonnull) NSString *truncationMode ``` |

#### CATransaction.h

Modified [+[CATransaction animationTimingFunction]](https://developer.apple.com/documentation/quartzcore/catransaction/1448269-animationtimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` + (CAMediaTimingFunction *)animationTimingFunction ``` |
| To | ``` + (CAMediaTimingFunction * _Nullable)animationTimingFunction ``` |

Modified [+[CATransaction completionBlock]](https://developer.apple.com/documentation/quartzcore/catransaction/1448280-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void (^)(void))completionBlock ``` |
| To | ``` + (void (^ _Nullable)(void))completionBlock ``` |

Modified [+[CATransaction setAnimationTimingFunction:]](https://developer.apple.com/documentation/quartzcore/catransaction/1448279-setanimationtimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction *)function ``` |
| To | ``` + (void)setAnimationTimingFunction:(CAMediaTimingFunction * _Nullable)function ``` |

Modified [+[CATransaction setCompletionBlock:]](https://developer.apple.com/documentation/quartzcore/catransaction/1448281-setcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setCompletionBlock:(void (^)(void))block ``` |
| To | ``` + (void)setCompletionBlock:(void (^ _Nullable)(void))block ``` |

Modified [+[CATransaction setValue:forKey:]](https://developer.apple.com/documentation/quartzcore/catransaction/1448278-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setValue:(id)anObject forKey:(NSString *)key ``` |
| To | ``` + (void)setValue:(id _Nullable)anObject forKey:(NSString * _Nonnull)key ``` |

Modified [+[CATransaction valueForKey:]](https://developer.apple.com/documentation/quartzcore/catransaction/1448259-value)

|  | Declaration |
| --- | --- |
| From | ``` + (id)valueForKey:(NSString *)key ``` |
| To | ``` + (id _Nullable)valueForKey:(NSString * _Nonnull)key ``` |

#### CATransform3D.h

Modified [+[NSValue valueWithCATransform3D:]](https://developer.apple.com/documentation/foundation/nsvalue/1436556-init)

|  | Declaration |
| --- | --- |
| From | ``` + (NSValue *)valueWithCATransform3D:(CATransform3D)t ``` |
| To | ``` + (NSValue * _Nonnull)valueWithCATransform3D:(CATransform3D)t ``` |

#### CAValueFunction.h

Modified [+[CAValueFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1522115-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype _Nullable)functionWithName:(NSString * _Nonnull)name ``` |

Modified [CAValueFunction.name](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1521888-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly) NSString *name ``` |
| To | ``` @property(readonly, nonnull) NSString *name ``` |

#### CIColor.h (Removed)

Modified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Protocols | Header |
| --- | --- | --- |
| From | NSCoding, NSCopying | CoreImage/CIColor.h |
| To | NSCopying, NSSecureCoding | CoreImage/CIColor.h |

Modified [CIColor.alpha](https://developer.apple.com/documentation/coreimage/cicolor/1437981-alpha)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)alpha ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly) CGFloat alpha ``` | CoreImage/CIColor.h |

Modified [CIColor.blue](https://developer.apple.com/documentation/coreimage/cicolor/1438033-blue)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)blue ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly) CGFloat blue ``` | CoreImage/CIColor.h |

Modified [CIColor.colorSpace](https://developer.apple.com/documentation/coreimage/cicolor/1437917-colorspace)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGColorSpaceRef)colorSpace ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly, nonnull) CGColorSpaceRef colorSpace ``` | CoreImage/CIColor.h |

Modified [+[CIColor colorWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1502106-colorwithcgcolor)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIColor *)colorWithCGColor:(CGColorRef)c ``` | CoreImage/CIColor.h |
| To | ``` + (instancetype _Nonnull)colorWithCGColor:(CGColorRef _Nonnull)c ``` | CoreImage/CIColor.h |

Modified [+[CIColor colorWithRed:green:blue:]](https://developer.apple.com/documentation/coreimage/cicolor/1437941-colorwithred)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIColor *)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b ``` | CoreImage/CIColor.h |
| To | ``` + (instancetype _Nonnull)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b ``` | CoreImage/CIColor.h |

Modified [+[CIColor colorWithRed:green:blue:alpha:]](https://developer.apple.com/documentation/coreimage/cicolor/1502111-colorwithred)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIColor *)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b alpha:(CGFloat)a ``` | CoreImage/CIColor.h |
| To | ``` + (instancetype _Nonnull)colorWithRed:(CGFloat)r green:(CGFloat)g blue:(CGFloat)b alpha:(CGFloat)a ``` | CoreImage/CIColor.h |

Modified [+[CIColor colorWithString:]](https://developer.apple.com/documentation/coreimage/cicolor/1438059-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIColor *)colorWithString:(NSString *)representation ``` | CoreImage/CIColor.h |
| To | ``` + (instancetype _Nonnull)colorWithString:(NSString * _Nonnull)representation ``` | CoreImage/CIColor.h |

Modified [CIColor.components](https://developer.apple.com/documentation/coreimage/cicolor/1437862-components)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (const CGFloat *)components ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly, nonnull) const CGFloat *components ``` | CoreImage/CIColor.h |

Modified [CIColor.green](https://developer.apple.com/documentation/coreimage/cicolor/1437607-green)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)green ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly) CGFloat green ``` | CoreImage/CIColor.h |

Modified [-[CIColor initWithCGColor:]](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)

|  | Declaration | Header | Designated Initializer |
| --- | --- | --- | --- |
| From | ``` - (id)initWithCGColor:(CGColorRef)c ``` | CoreImage/CIColor.h | -- |
| To | ``` - (instancetype _Nonnull)initWithCGColor:(CGColorRef _Nonnull)c ``` | CoreImage/CIColor.h | yes |

Modified [CIColor.numberOfComponents](https://developer.apple.com/documentation/coreimage/cicolor/1438151-numberofcomponents)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (size_t)numberOfComponents ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly) size_t numberOfComponents ``` | CoreImage/CIColor.h |

Modified [CIColor.red](https://developer.apple.com/documentation/coreimage/cicolor/1437969-red)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)red ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly) CGFloat red ``` | CoreImage/CIColor.h |

Modified [CIColor.stringRepresentation](https://developer.apple.com/documentation/coreimage/cicolor/1437910-stringrepresentation)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSString *)stringRepresentation ``` | CoreImage/CIColor.h |
| To | ``` @property(readonly, nonnull) NSString *stringRepresentation ``` | CoreImage/CIColor.h |

#### CIContext.h (Removed)

Modified [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)

|  | Header |
| --- | --- |
| From | CoreImage/CIContext.h |
| To | CoreImage/CIContext.h |

Modified [-[CIContext clearCaches]](https://developer.apple.com/documentation/coreimage/cicontext/1437790-clearcaches)

|  | Header |
| --- | --- |
| From | CoreImage/CIContext.h |
| To | CoreImage/CIContext.h |

Modified [+[CIContext contextForOfflineGPUAtIndex:]](https://developer.apple.com/documentation/coreimage/cicontext/1437772-contextforofflinegpuatindex)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIContext *)contextForOfflineGPUAtIndex:(unsigned int)index ``` | CoreImage/CIContext.h |
| To | ``` + (CIContext * _Nonnull)contextForOfflineGPUAtIndex:(unsigned int)index ``` | CoreImage/CIContext.h |

Modified [+[CIContext contextForOfflineGPUAtIndex:colorSpace:options:sharedContext:]](https://developer.apple.com/documentation/coreimage/cicontext/1437758-contextforofflinegpuatindex)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIContext *)contextForOfflineGPUAtIndex:(unsigned int)index colorSpace:(CGColorSpaceRef)colorSpace options:(NSDictionary *)options sharedContext:(CGLContextObj)sharedContext ``` | CoreImage/CIContext.h |
| To | ``` + (CIContext * _Nonnull)contextForOfflineGPUAtIndex:(unsigned int)index colorSpace:(CGColorSpaceRef _Nullable)colorSpace options:(NSDictionary<NSString *,id> * _Nullable)options sharedContext:(CGLContextObj _Nullable)sharedContext ``` | CoreImage/CIContext.h |

Modified [+[CIContext contextWithCGContext:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1437864-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIContext *)contextWithCGContext:(CGContextRef)ctx options:(NSDictionary *)dict ``` | CoreImage/CIContext.h |
| To | ``` + (CIContext * _Nonnull)contextWithCGContext:(CGContextRef _Nonnull)cgctx options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIContext.h |

Modified [+[CIContext contextWithCGLContext:pixelFormat:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1438137-contextwithcglcontext)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIContext *)contextWithCGLContext:(CGLContextObj)ctx pixelFormat:(CGLPixelFormatObj)pf colorSpace:(CGColorSpaceRef)cs options:(NSDictionary *)dict ``` | CoreImage/CIContext.h |
| To | ``` + (CIContext * _Nonnull)contextWithCGLContext:(CGLContextObj _Nonnull)cglctx pixelFormat:(CGLPixelFormatObj _Nullable)pixelFormat colorSpace:(CGColorSpaceRef _Nullable)colorSpace options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIContext.h |

Modified [+[CIContext contextWithCGLContext:pixelFormat:options:]](https://developer.apple.com/documentation/coreimage/cicontext/1473525-contextwithcglcontext)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIContext *)contextWithCGLContext:(CGLContextObj)ctx pixelFormat:(CGLPixelFormatObj)pf options:(NSDictionary *)dict ``` | CoreImage/CIContext.h |
| To | ``` + (CIContext * _Nonnull)contextWithCGLContext:(CGLContextObj _Nonnull)cglctx pixelFormat:(CGLPixelFormatObj _Nullable)pixelFormat options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIContext.h |

Modified [-[CIContext createCGImage:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGImageRef)createCGImage:(CIImage *)im fromRect:(CGRect)r ``` | CoreImage/CIContext.h |
| To | ``` - (CGImageRef _Nonnull)createCGImage:(CIImage * _Nonnull)image fromRect:(CGRect)fromRect ``` | CoreImage/CIContext.h |

Modified [-[CIContext createCGImage:fromRect:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGImageRef)createCGImage:(CIImage *)im fromRect:(CGRect)r format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIContext.h |
| To | ``` - (CGImageRef _Nonnull)createCGImage:(CIImage * _Nonnull)image fromRect:(CGRect)fromRect format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIContext.h |

Modified [-[CIContext createCGLayerWithSize:info:]](https://developer.apple.com/documentation/coreimage/cicontext/1438267-createcglayerwithsize)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` - (CGLayerRef)createCGLayerWithSize:(CGSize)size info:(CFDictionaryRef)d ``` | -- | CoreImage/CIContext.h |
| To | ``` - (CGLayerRef _Nonnull)createCGLayerWithSize:(CGSize)size info:(CFDictionaryRef _Nullable)info ``` | OS X 10.11 | CoreImage/CIContext.h |

Modified [-[CIContext drawImage:atPoint:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)drawImage:(CIImage *)im atPoint:(CGPoint)p fromRect:(CGRect)src ``` | CoreImage/CIContext.h |
| To | ``` - (void)drawImage:(CIImage * _Nonnull)image atPoint:(CGPoint)atPoint fromRect:(CGRect)fromRect ``` | CoreImage/CIContext.h |

Modified [-[CIContext drawImage:inRect:fromRect:]](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)drawImage:(CIImage *)im inRect:(CGRect)dest fromRect:(CGRect)src ``` | CoreImage/CIContext.h |
| To | ``` - (void)drawImage:(CIImage * _Nonnull)image inRect:(CGRect)inRect fromRect:(CGRect)fromRect ``` | CoreImage/CIContext.h |

Modified [+[CIContext offlineGPUCount]](https://developer.apple.com/documentation/coreimage/cicontext/1437817-offlinegpucount)

|  | Header |
| --- | --- |
| From | CoreImage/CIContext.h |
| To | CoreImage/CIContext.h |

Modified [-[CIContext reclaimResources]](https://developer.apple.com/documentation/coreimage/cicontext/1437967-reclaimresources)

|  | Header |
| --- | --- |
| From | CoreImage/CIContext.h |
| To | CoreImage/CIContext.h |

Modified [-[CIContext render:toBitmap:rowBytes:bounds:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)render:(CIImage *)im toBitmap:(void *)data rowBytes:(ptrdiff_t)rb bounds:(CGRect)r format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIContext.h |
| To | ``` - (void)render:(CIImage * _Nonnull)image toBitmap:(void * _Nonnull)data rowBytes:(ptrdiff_t)rowBytes bounds:(CGRect)bounds format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIContext.h |

Modified [-[CIContext render:toIOSurface:bounds:colorSpace:]](https://developer.apple.com/documentation/coreimage/cicontext/1437778-render)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)render:(CIImage *)im toIOSurface:(IOSurfaceRef)surface bounds:(CGRect)r colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIContext.h |
| To | ``` - (void)render:(CIImage * _Nonnull)image toIOSurface:(IOSurfaceRef _Nonnull)surface bounds:(CGRect)bounds colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIContext.h |

Modified [kCIContextOutputColorSpace](https://developer.apple.com/documentation/coreimage/cicontextoption/1438052-outputcolorspace)

|  | Introduction | Header |
| --- | --- | --- |
| From | OS X 10.4 | CoreImage/CIContext.h |
| To | OS X 10.6 | CoreImage/CIContext.h |

Modified [kCIContextUseSoftwareRenderer](https://developer.apple.com/documentation/coreimage/cicontextoption/1438047-usesoftwarerenderer)

|  | Introduction | Header |
| --- | --- | --- |
| From | OS X 10.4 | CoreImage/CIContext.h |
| To | OS X 10.6 | CoreImage/CIContext.h |

Modified [kCIContextWorkingColorSpace](https://developer.apple.com/documentation/coreimage/cicontextoption/1437728-workingcolorspace)

|  | Introduction | Header |
| --- | --- | --- |
| From | OS X 10.4 | CoreImage/CIContext.h |
| To | OS X 10.6 | CoreImage/CIContext.h |

#### CIDetector.h (Removed)

Modified [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [+[CIDetector detectorOfType:context:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIDetector *)detectorOfType:(NSString *)type context:(CIContext *)context options:(NSDictionary *)options ``` | CoreImage/CIDetector.h |
| To | ``` + (CIDetector * _Nonnull)detectorOfType:(NSString * _Nonnull)type context:(CIContext * _Nullable)context options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIDetector.h |

Modified [-[CIDetector featuresInImage:]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray *)featuresInImage:(CIImage *)image ``` | CoreImage/CIDetector.h |
| To | ``` - (NSArray<CIFeature *> * _Nonnull)featuresInImage:(CIImage * _Nonnull)image ``` | CoreImage/CIDetector.h |

Modified [-[CIDetector featuresInImage:options:]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray *)featuresInImage:(CIImage *)image options:(NSDictionary *)options ``` | CoreImage/CIDetector.h |
| To | ``` - (NSArray<CIFeature *> * _Nonnull)featuresInImage:(CIImage * _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIDetector.h |

Modified [CIDetectorAccuracy](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorAccuracyHigh](https://developer.apple.com/documentation/coreimage/cidetectoraccuracyhigh)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorAccuracyLow](https://developer.apple.com/documentation/coreimage/cidetectoraccuracylow)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorAspectRatio](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorEyeBlink](https://developer.apple.com/documentation/coreimage/cidetectoreyeblink)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorFocalLength](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorImageOrientation](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorMinFeatureSize](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorSmile](https://developer.apple.com/documentation/coreimage/cidetectorsmile)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorTracking](https://developer.apple.com/documentation/coreimage/cidetectortracking)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorTypeFace](https://developer.apple.com/documentation/coreimage/cidetectortypeface)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorTypeQRCode](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

Modified [CIDetectorTypeRectangle](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIDetector.h |
| To | CoreImage/CIDetector.h |

#### CIFeature.h (Removed)

Modified [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.bounds](https://developer.apple.com/documentation/coreimage/cifacefeature/1438068-bounds)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.faceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1437689-faceangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasFaceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1438165-hasfaceangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasLeftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437900-haslefteyeposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasMouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437976-hasmouthposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasRightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438076-hasrighteyeposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasSmile](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasTrackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437731-hastrackingframecount)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.hasTrackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437683-hastrackingid)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.leftEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437630-lefteyeclosed)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.leftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437923-lefteyeposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.mouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438020-mouthposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.rightEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437615-righteyeclosed)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.rightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438213-righteyeposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.trackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437953-trackingframecount)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFaceFeature.trackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437709-trackingid)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFeature.bounds](https://developer.apple.com/documentation/coreimage/cifeature/1437782-bounds)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, retain) NSString *type ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly, retain, nonnull) NSString *type ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomLeft ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint bottomLeft ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomRight ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint bottomRight ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGRect bounds ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGRect bounds ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, copy) NSString *messageString ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly, nonnull) NSString *messageString ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint topLeft ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint topLeft ``` | CoreImage/CIFeature.h |

Modified [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint topRight ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint topRight ``` | CoreImage/CIFeature.h |

Modified [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomLeft ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint bottomLeft ``` | CoreImage/CIFeature.h |

Modified [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint bottomRight ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint bottomRight ``` | CoreImage/CIFeature.h |

Modified [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGRect bounds ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGRect bounds ``` | CoreImage/CIFeature.h |

Modified [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint topLeft ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint topLeft ``` | CoreImage/CIFeature.h |

Modified [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, assign) CGPoint topRight ``` | CoreImage/CIFeature.h |
| To | ``` @property(readonly) CGPoint topRight ``` | CoreImage/CIFeature.h |

Modified [CIFeatureTypeFace](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

Modified [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIFeature.h |
| To | CoreImage/CIFeature.h |

#### CIFilter.h (Removed)

Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Protocols | Header |
| --- | --- | --- |
| From | NSCoding, NSCopying | CoreImage/CIFilter.h |
| To | NSCopying, NSSecureCoding | CoreImage/CIFilter.h |

Modified [-[CIFilter apply:]](https://developer.apple.com/documentation/coreimage/cifilter/1562058-apply)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)apply:(CIKernel *)k, ... ``` | CoreImage/CIFilter.h |
| To | ``` - (CIImage * _Nullable)apply:(CIKernel * _Nonnull)k, ... ``` | CoreImage/CIFilter.h |

Modified [-[CIFilter apply:arguments:options:]](https://developer.apple.com/documentation/coreimage/cifilter/1438077-apply)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)apply:(CIKernel *)k arguments:(NSArray *)args options:(NSDictionary *)dict ``` | CoreImage/CIFilter.h |
| To | ``` - (CIImage * _Nullable)apply:(CIKernel * _Nonnull)k arguments:(NSArray * _Nullable)args options:(NSDictionary<NSString *,id> * _Nullable)dict ``` | CoreImage/CIFilter.h |

Modified [CIFilter.attributes](https://developer.apple.com/documentation/coreimage/cifilter/1437661-attributes)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSDictionary *)attributes ``` | CoreImage/CIFilter.h |
| To | ``` @property(nonatomic, readonly, nonnull) NSDictionary<NSString *,id> *attributes ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterArrayFromSerializedXMP:inputImageExtent:error:]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSArray *)filterArrayFromSerializedXMP:(NSData *)xmpData inputImageExtent:(CGRect)extent error:(NSError **)outError ``` | CoreImage/CIFilter.h |
| To | ``` + (NSArray<CIFilter *> * _Nonnull)filterArrayFromSerializedXMP:(NSData * _Nonnull)xmpData inputImageExtent:(CGRect)extent error:(NSError * _Nullable * _Nullable)outError ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterNamesInCategories:]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSArray *)filterNamesInCategories:(NSArray *)categories ``` | CoreImage/CIFilter.h |
| To | ``` + (NSArray<NSString *> * _Nonnull)filterNamesInCategories:(NSArray<NSString *> * _Nullable)categories ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterNamesInCategory:]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSArray *)filterNamesInCategory:(NSString *)category ``` | CoreImage/CIFilter.h |
| To | ``` + (NSArray<NSString *> * _Nonnull)filterNamesInCategory:(NSString * _Nullable)category ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterWithName:]](https://developer.apple.com/documentation/coreimage/cifilter/1438255-filterwithname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIFilter *)filterWithName:(NSString *)name ``` | CoreImage/CIFilter.h |
| To | ``` + (CIFilter * _Nullable)filterWithName:(NSString * _Nonnull)name ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterWithName:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cifilter/1562057-filterwithname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIFilter *)filterWithName:(NSString *)name keysAndValues:(id)key0, ... ``` | CoreImage/CIFilter.h |
| To | ``` + (CIFilter * _Nullable)filterWithName:(NSString * _Nonnull)name keysAndValues:(id)key0, ... ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter filterWithName:withInputParameters:]](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIFilter *)filterWithName:(NSString *)name withInputParameters:(NSDictionary *)params ``` | CoreImage/CIFilter.h |
| To | ``` + (CIFilter * _Nullable)filterWithName:(NSString * _Nonnull)name withInputParameters:(NSDictionary<NSString *,id> * _Nullable)params ``` | CoreImage/CIFilter.h |

Modified [CIFilter.inputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438013-inputkeys)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray *)inputKeys ``` | CoreImage/CIFilter.h |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *inputKeys ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter localizedDescriptionForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)

|  | Declaration | Introduction | Header |
| --- | --- | --- | --- |
| From | ``` + (NSString *)localizedDescriptionForFilterName:(NSString *)filterName ``` | OS X 10.5 | CoreImage/CIFilter.h |
| To | ``` + (NSString * _Nullable)localizedDescriptionForFilterName:(NSString * _Nonnull)filterName ``` | OS X 10.4 | CoreImage/CIFilter.h |

Modified [+[CIFilter localizedNameForCategory:]](https://developer.apple.com/documentation/coreimage/cifilter/1438057-localizedname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSString *)localizedNameForCategory:(NSString *)category ``` | CoreImage/CIFilter.h |
| To | ``` + (NSString * _Nonnull)localizedNameForCategory:(NSString * _Nonnull)category ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter localizedNameForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437697-localizedname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSString *)localizedNameForFilterName:(NSString *)filterName ``` | CoreImage/CIFilter.h |
| To | ``` + (NSString * _Nullable)localizedNameForFilterName:(NSString * _Nonnull)filterName ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter localizedReferenceDocumentationForFilterName:]](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)

|  | Declaration | Introduction | Header |
| --- | --- | --- | --- |
| From | ``` + (NSURL *)localizedReferenceDocumentationForFilterName:(NSString *)filterName ``` | OS X 10.5 | CoreImage/CIFilter.h |
| To | ``` + (NSURL * _Nullable)localizedReferenceDocumentationForFilterName:(NSString * _Nonnull)filterName ``` | OS X 10.4 | CoreImage/CIFilter.h |

Modified [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` @property(readonly, nonatomic) CIImage *outputImage ``` | CoreImage/CIFilter.h |
| To | ``` @property(readonly, nonatomic, nullable) CIImage *outputImage ``` | CoreImage/CIFilter.h |

Modified [CIFilter.outputKeys](https://developer.apple.com/documentation/coreimage/cifilter/1438122-outputkeys)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray *)outputKeys ``` | CoreImage/CIFilter.h |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *outputKeys ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter registerFilterName:constructor:classAttributes:]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (void)registerFilterName:(NSString *)name constructor:(id<CIFilterConstructor>)anObject classAttributes:(NSDictionary *)attributes ``` | CoreImage/CIFilter.h |
| To | ``` + (void)registerFilterName:(NSString * _Nonnull)name constructor:(id<CIFilterConstructor> _Nonnull)anObject classAttributes:(NSDictionary<NSString *,id> * _Nonnull)attributes ``` | CoreImage/CIFilter.h |

Modified [+[CIFilter serializedXMPFromFilters:inputImageExtent:]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSData *)serializedXMPFromFilters:(NSArray *)filters inputImageExtent:(CGRect)extent ``` | CoreImage/CIFilter.h |
| To | ``` + (NSData * _Nonnull)serializedXMPFromFilters:(NSArray<CIFilter *> * _Nonnull)filters inputImageExtent:(CGRect)extent ``` | CoreImage/CIFilter.h |

Modified [-[CIFilter setDefaults]](https://developer.apple.com/documentation/coreimage/cifilter/1437902-setdefaults)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified CIFilter(CIFilterRegistry)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified CIFilter(CIFilterXMPSerialization)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIApplyOptionColorSpace](https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIApplyOptionDefinition](https://developer.apple.com/documentation/coreimage/kciapplyoptiondefinition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIApplyOptionExtent](https://developer.apple.com/documentation/coreimage/kciapplyoptionextent)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIApplyOptionUserInfo](https://developer.apple.com/documentation/coreimage/kciapplyoptionuserinfo)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeClass](https://developer.apple.com/documentation/coreimage/kciattributeclass)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeDefault](https://developer.apple.com/documentation/coreimage/kciattributedefault)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeDescription](https://developer.apple.com/documentation/coreimage/kciattributedescription)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeDisplayName](https://developer.apple.com/documentation/coreimage/kciattributedisplayname)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeFilterCategories](https://developer.apple.com/documentation/coreimage/kciattributefiltercategories)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeFilterDisplayName](https://developer.apple.com/documentation/coreimage/kciattributefilterdisplayname)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeFilterName](https://developer.apple.com/documentation/coreimage/kciattributefiltername)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeIdentity](https://developer.apple.com/documentation/coreimage/kciattributeidentity)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeMax](https://developer.apple.com/documentation/coreimage/kciattributemax)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeMin](https://developer.apple.com/documentation/coreimage/kciattributemin)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeName](https://developer.apple.com/documentation/coreimage/kciattributename)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeReferenceDocumentation](https://developer.apple.com/documentation/coreimage/kciattributereferencedocumentation)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeSliderMax](https://developer.apple.com/documentation/coreimage/kciattributeslidermax)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeSliderMin](https://developer.apple.com/documentation/coreimage/kciattributeslidermin)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeType](https://developer.apple.com/documentation/coreimage/kciattributetype)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeAngle](https://developer.apple.com/documentation/coreimage/kciattributetypeangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeBoolean](https://developer.apple.com/documentation/coreimage/kciattributetypeboolean)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeCount](https://developer.apple.com/documentation/coreimage/kciattributetypecount)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeDistance](https://developer.apple.com/documentation/coreimage/kciattributetypedistance)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeGradient](https://developer.apple.com/documentation/coreimage/kciattributetypegradient)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeInteger](https://developer.apple.com/documentation/coreimage/kciattributetypeinteger)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeOffset](https://developer.apple.com/documentation/coreimage/kciattributetypeoffset)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeOpaqueColor](https://developer.apple.com/documentation/coreimage/kciattributetypeopaquecolor)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypePosition](https://developer.apple.com/documentation/coreimage/kciattributetypeposition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypePosition3](https://developer.apple.com/documentation/coreimage/kciattributetypeposition3)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeRectangle](https://developer.apple.com/documentation/coreimage/kciattributetyperectangle)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeScalar](https://developer.apple.com/documentation/coreimage/kciattributetypescalar)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIAttributeTypeTime](https://developer.apple.com/documentation/coreimage/kciattributetypetime)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryBlur](https://developer.apple.com/documentation/coreimage/kcicategoryblur)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryBuiltIn](https://developer.apple.com/documentation/coreimage/kcicategorybuiltin)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryColorAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorycoloradjustment)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryColorEffect](https://developer.apple.com/documentation/coreimage/kcicategorycoloreffect)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryCompositeOperation](https://developer.apple.com/documentation/coreimage/kcicategorycompositeoperation)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryDistortionEffect](https://developer.apple.com/documentation/coreimage/kcicategorydistortioneffect)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryFilterGenerator](https://developer.apple.com/documentation/coreimage/kcicategoryfiltergenerator)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryGenerator](https://developer.apple.com/documentation/coreimage/kcicategorygenerator)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryGeometryAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorygeometryadjustment)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryGradient](https://developer.apple.com/documentation/coreimage/kcicategorygradient)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryHalftoneEffect](https://developer.apple.com/documentation/coreimage/kcicategoryhalftoneeffect)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryHighDynamicRange](https://developer.apple.com/documentation/coreimage/kcicategoryhighdynamicrange)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryInterlaced](https://developer.apple.com/documentation/coreimage/kcicategoryinterlaced)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryNonSquarePixels](https://developer.apple.com/documentation/coreimage/kcicategorynonsquarepixels)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryReduction](https://developer.apple.com/documentation/coreimage/kcicategoryreduction)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategorySharpen](https://developer.apple.com/documentation/coreimage/kcicategorysharpen)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryStillImage](https://developer.apple.com/documentation/coreimage/kcicategorystillimage)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryStylize](https://developer.apple.com/documentation/coreimage/kcicategorystylize)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryTileEffect](https://developer.apple.com/documentation/coreimage/kcicategorytileeffect)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryTransition](https://developer.apple.com/documentation/coreimage/kcicategorytransition)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCICategoryVideo](https://developer.apple.com/documentation/coreimage/kcicategoryvideo)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputAngleKey](https://developer.apple.com/documentation/coreimage/kciinputanglekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputAspectRatioKey](https://developer.apple.com/documentation/coreimage/kciinputaspectratiokey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputBackgroundImageKey](https://developer.apple.com/documentation/coreimage/kciinputbackgroundimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputBrightnessKey](https://developer.apple.com/documentation/coreimage/kciinputbrightnesskey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputCenterKey](https://developer.apple.com/documentation/coreimage/kciinputcenterkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputColorKey](https://developer.apple.com/documentation/coreimage/kciinputcolorkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputContrastKey](https://developer.apple.com/documentation/coreimage/kciinputcontrastkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputEVKey](https://developer.apple.com/documentation/coreimage/kciinputevkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputExtentKey](https://developer.apple.com/documentation/coreimage/kciinputextentkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputGradientImageKey](https://developer.apple.com/documentation/coreimage/kciinputgradientimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputImageKey](https://developer.apple.com/documentation/coreimage/kciinputimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputIntensityKey](https://developer.apple.com/documentation/coreimage/kciinputintensitykey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputMaskImageKey](https://developer.apple.com/documentation/coreimage/kciinputmaskimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputRadiusKey](https://developer.apple.com/documentation/coreimage/kciinputradiuskey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputRefractionKey](https://developer.apple.com/documentation/coreimage/kciinputrefractionkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputSaturationKey](https://developer.apple.com/documentation/coreimage/kciinputsaturationkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputScaleKey](https://developer.apple.com/documentation/coreimage/kciinputscalekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputShadingImageKey](https://developer.apple.com/documentation/coreimage/kciinputshadingimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputSharpnessKey](https://developer.apple.com/documentation/coreimage/kciinputsharpnesskey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputTargetImageKey](https://developer.apple.com/documentation/coreimage/kciinputtargetimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputTimeKey](https://developer.apple.com/documentation/coreimage/kciinputtimekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputTransformKey](https://developer.apple.com/documentation/coreimage/kciinputtransformkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputWidthKey](https://developer.apple.com/documentation/coreimage/kciinputwidthkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIOutputImageKey](https://developer.apple.com/documentation/coreimage/kcioutputimagekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIUIParameterSet](https://developer.apple.com/documentation/coreimage/kciuiparameterset)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIUISetAdvanced](https://developer.apple.com/documentation/coreimage/kciuisetadvanced)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIUISetBasic](https://developer.apple.com/documentation/coreimage/kciuisetbasic)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIUISetDevelopment](https://developer.apple.com/documentation/coreimage/kciuisetdevelopment)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIUISetIntermediate](https://developer.apple.com/documentation/coreimage/kciuisetintermediate)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilter.h |
| To | CoreImage/CIFilter.h |

#### CIFilterConstructor.h (Removed)

Modified [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilterConstructor.h |
| To | CoreImage/CIFilterConstructor.h |

Modified [-[CIFilterConstructor filterWithName:]](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilter *)filterWithName:(NSString *)name ``` | CoreImage/CIFilterConstructor.h |
| To | ``` - (CIFilter * _Nullable)filterWithName:(NSString * _Nonnull)name ``` | CoreImage/CIFilterConstructor.h |

#### CIFilterGenerator.h (Removed)

Removed [-[CIFilterGenerator setClassAttributes:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437855-classattributes)Modified [CIFilterGenerator](https://developer.apple.com/documentation/coreimage/cifiltergenerator)

|  | Protocols | Header |
| --- | --- | --- |
| From | CIFilterConstructor, NSCoding, NSCopying | CoreImage/CIFilterGenerator.h |
| To | CIFilterConstructor, NSCopying, NSSecureCoding | CoreImage/CIFilterGenerator.h |

Modified [CIFilterGenerator.classAttributes](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437855-classattributes)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSDictionary *)classAttributes ``` | CoreImage/CIFilterGenerator.h |
| To | ``` @property(retain, nonatomic, nonnull) NSDictionary *classAttributes ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator connectObject:withKey:toObject:withKey:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438159-connect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)connectObject:(id)sourceObject withKey:(NSString *)sourceKey toObject:(id)targetObject withKey:(NSString *)targetKey ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)connectObject:(id _Nonnull)sourceObject withKey:(NSString * _Nullable)sourceKey toObject:(id _Nonnull)targetObject withKey:(NSString * _Nonnull)targetKey ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator disconnectObject:withKey:toObject:withKey:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438075-disconnectobject)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)disconnectObject:(id)sourceObject withKey:(NSString *)key toObject:(id)targetObject withKey:(NSString *)targetKey ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)disconnectObject:(id _Nonnull)sourceObject withKey:(NSString * _Nonnull)key toObject:(id _Nonnull)targetObject withKey:(NSString * _Nonnull)targetKey ``` | CoreImage/CIFilterGenerator.h |

Modified [CIFilterGenerator.exportedKeys](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437955-exportedkeys)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSDictionary *)exportedKeys ``` | CoreImage/CIFilterGenerator.h |
| To | ``` @property(readonly, nonatomic, nonnull) NSDictionary *exportedKeys ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator exportKey:fromObject:withName:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438155-exportkey)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)exportKey:(NSString *)key fromObject:(id)targetObject withName:(NSString *)exportedKeyName ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)exportKey:(NSString * _Nonnull)key fromObject:(id _Nonnull)targetObject withName:(NSString * _Nullable)exportedKeyName ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator filter]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438044-filter)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilter *)filter ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (CIFilter * _Nonnull)filter ``` | CoreImage/CIFilterGenerator.h |

Modified [+[CIFilterGenerator filterGenerator]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1525954-filtergenerator)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIFilterGenerator *)filterGenerator ``` | CoreImage/CIFilterGenerator.h |
| To | ``` + (CIFilterGenerator * _Nonnull)filterGenerator ``` | CoreImage/CIFilterGenerator.h |

Modified [+[CIFilterGenerator filterGeneratorWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1525950-filtergeneratorwithcontentsofurl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIFilterGenerator *)filterGeneratorWithContentsOfURL:(NSURL *)aURL ``` | CoreImage/CIFilterGenerator.h |
| To | ``` + (CIFilterGenerator * _Nullable)filterGeneratorWithContentsOfURL:(NSURL * _Nonnull)aURL ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator initWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437742-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)aURL ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (id _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)aURL ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator registerFilterName:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437891-registerfiltername)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)registerFilterName:(NSString *)name ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)registerFilterName:(NSString * _Nonnull)name ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator removeExportedKey:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438191-removeexportedkey)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)removeExportedKey:(NSString *)exportedKeyName ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)removeExportedKey:(NSString * _Nonnull)exportedKeyName ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator setAttributes:forExportedKey:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438069-setattributes)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)setAttributes:(NSDictionary *)attributes forExportedKey:(NSString *)key ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (void)setAttributes:(NSDictionary * _Nonnull)attributes forExportedKey:(NSString * _Nonnull)key ``` | CoreImage/CIFilterGenerator.h |

Modified [-[CIFilterGenerator writeToURL:atomically:]](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438179-writetourl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (BOOL)writeToURL:(NSURL *)aURL atomically:(BOOL)flag ``` | CoreImage/CIFilterGenerator.h |
| To | ``` - (BOOL)writeToURL:(NSURL * _Nonnull)aURL atomically:(BOOL)flag ``` | CoreImage/CIFilterGenerator.h |

Modified [kCIFilterGeneratorExportedKey](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilterGenerator.h |
| To | CoreImage/CIFilterGenerator.h |

Modified [kCIFilterGeneratorExportedKeyName](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeyname)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilterGenerator.h |
| To | CoreImage/CIFilterGenerator.h |

Modified [kCIFilterGeneratorExportedKeyTargetObject](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeytargetobject)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilterGenerator.h |
| To | CoreImage/CIFilterGenerator.h |

#### CIFilterShape.h (Removed)

Modified [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)

|  | Header |
| --- | --- |
| From | CoreImage/CIFilterShape.h |
| To | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape initWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-initwithrect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |
| To | ``` - (instancetype _Nonnull)initWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape insetByX:Y:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetbyx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)insetByX:(int)dx Y:(int)dy ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)insetByX:(int)dx Y:(int)dy ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape intersectWith:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)intersectWith:(CIFilterShape *)s2 ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)intersectWith:(CIFilterShape * _Nonnull)s2 ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape intersectWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437806-intersect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)intersectWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)intersectWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |

Modified [+[CIFilterShape shapeWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1562074-shapewithrect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (id)shapeWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |
| To | ``` + (instancetype _Nonnull)shapeWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape transformBy:interior:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437808-transform)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)transformBy:(CGAffineTransform)m interior:(BOOL)flag ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)transformBy:(CGAffineTransform)m interior:(BOOL)flag ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape unionWith:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1438227-unionwith)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)unionWith:(CIFilterShape *)s2 ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)unionWith:(CIFilterShape * _Nonnull)s2 ``` | CoreImage/CIFilterShape.h |

Modified [-[CIFilterShape unionWithRect:]](https://developer.apple.com/documentation/coreimage/cifiltershape/1437601-unionwithrect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)unionWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |
| To | ``` - (CIFilterShape * _Nonnull)unionWithRect:(CGRect)r ``` | CoreImage/CIFilterShape.h |

#### CIImage.h (Removed)

Removed [-[CIImage autoAdjustmentFilters]](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Protocols | Header |
| --- | --- | --- |
| From | NSCoding, NSCopying | CoreImage/CIImage.h |
| To | NSCopying, NSSecureCoding | CoreImage/CIImage.h |

Modified [-[CIImage autoAdjustmentFiltersWithOptions:]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilters)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSArray *)autoAdjustmentFiltersWithOptions:(NSDictionary *)dict ``` | CoreImage/CIImage.h |
| To | ``` - (NSArray<CIFilter *> * _Nonnull)autoAdjustmentFiltersWithOptions:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [CIImage.colorSpace](https://developer.apple.com/documentation/coreimage/ciimage/1437750-colorspace)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGColorSpaceRef)colorSpace ``` | CoreImage/CIImage.h |
| To | ``` @property(atomic, readonly, nullable) CGColorSpaceRef colorSpace ``` | CoreImage/CIImage.h |

Modified [CIImage.definition](https://developer.apple.com/documentation/coreimage/ciimage/1437804-definition)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)definition ``` | CoreImage/CIImage.h |
| To | ``` @property(atomic, readonly, nonnull) CIFilterShape *definition ``` | CoreImage/CIImage.h |

Modified [+[CIImage emptyImage]](https://developer.apple.com/documentation/coreimage/ciimage/1438023-emptyimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)emptyImage ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)emptyImage ``` | CoreImage/CIImage.h |

Modified [CIImage.extent](https://developer.apple.com/documentation/coreimage/ciimage/1437996-extent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGRect)extent ``` | CoreImage/CIImage.h |
| To | ``` @property(readonly, atomic) CGRect extent ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByApplyingFilter:withInputParameters:]](https://developer.apple.com/documentation/coreimage/ciimage/1437589-applyingfilter)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByApplyingFilter:(NSString *)filterName withInputParameters:(NSDictionary *)params ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByApplyingFilter:(NSString * _Nonnull)filterName withInputParameters:(NSDictionary<NSString *,id> * _Nullable)params ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByApplyingOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1438223-imagebyapplyingorientation)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByApplyingOrientation:(int)orientation ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByApplyingOrientation:(int)orientation ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByApplyingTransform:]](https://developer.apple.com/documentation/coreimage/ciimage/1438203-imagebyapplyingtransform)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByApplyingTransform:(CGAffineTransform)matrix ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByApplyingTransform:(CGAffineTransform)matrix ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByClampingToExtent]](https://developer.apple.com/documentation/coreimage/ciimage/1437628-clampedtoextent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByClampingToExtent ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByClampingToExtent ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByCompositingOverImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437837-composited)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByCompositingOverImage:(CIImage *)dest ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByCompositingOverImage:(CIImage * _Nonnull)dest ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageByCroppingToRect:]](https://developer.apple.com/documentation/coreimage/ciimage/1437833-imagebycroppingtorect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)imageByCroppingToRect:(CGRect)r ``` | CoreImage/CIImage.h |
| To | ``` - (CIImage * _Nonnull)imageByCroppingToRect:(CGRect)rect ``` | CoreImage/CIImage.h |

Modified [-[CIImage imageTransformForOrientation:]](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [+[CIImage imageWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547023-imagewithbitmapdata)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithBitmapData:(NSData *)d bytesPerRow:(size_t)bpr size:(CGSize)size format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithBitmapData:(NSData * _Nonnull)data bytesPerRow:(size_t)bytesPerRow size:(CGSize)size format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCGImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1547025-imagewithcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithCGImage:(CGImageRef)image ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCGImage:(CGImageRef _Nonnull)image ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547021-imagewithcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithCGImage:(CGImageRef)image options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCGImage:(CGImageRef _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCGLayer:]](https://developer.apple.com/documentation/coreimage/ciimage/1547022-imagewithcglayer)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` + (CIImage *)imageWithCGLayer:(CGLayerRef)layer ``` | -- | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCGLayer:(CGLayerRef _Nonnull)layer ``` | OS X 10.11 | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCGLayer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1546998-imagewithcglayer)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` + (CIImage *)imageWithCGLayer:(CGLayerRef)layer options:(NSDictionary *)d ``` | -- | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCGLayer:(CGLayerRef _Nonnull)layer options:(NSDictionary<NSString *,id> * _Nullable)options ``` | OS X 10.11 | CoreImage/CIImage.h |

Modified [+[CIImage imageWithColor:]](https://developer.apple.com/documentation/coreimage/ciimage/1547012-imagewithcolor)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithColor:(CIColor *)color ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithColor:(CIColor * _Nonnull)color ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/ciimage/1547027-imagewithcontentsofurl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithContentsOfURL:(NSURL *)url ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nullable)imageWithContentsOfURL:(NSURL * _Nonnull)url ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1546997-imagewithcontentsofurl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithContentsOfURL:(NSURL *)url options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nullable)imageWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCVImageBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1547007-imagewithcvimagebuffer)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithCVImageBuffer:(CVImageBufferRef)imageBuffer ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCVImageBuffer:(CVImageBufferRef _Nonnull)imageBuffer ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithCVImageBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547028-imagewithcvimagebuffer)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithCVImageBuffer:(CVImageBufferRef)imageBuffer options:(NSDictionary *)dict ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithCVImageBuffer:(CVImageBufferRef _Nonnull)imageBuffer options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithData:]](https://developer.apple.com/documentation/coreimage/ciimage/1547029-imagewithdata)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithData:(NSData *)data ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nullable)imageWithData:(NSData * _Nonnull)data ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547016-imagewithdata)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithData:(NSData *)data options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nullable)imageWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithIOSurface:]](https://developer.apple.com/documentation/coreimage/ciimage/1547024-imagewithiosurface)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithIOSurface:(IOSurfaceRef)surface ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithIOSurface:(IOSurfaceRef _Nonnull)surface ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithIOSurface:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547001-imagewithiosurface)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithIOSurface:(IOSurfaceRef)surface options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithIOSurface:(IOSurfaceRef _Nonnull)surface options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1547006-imagewithtexture)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIImage.h |

Modified [+[CIImage imageWithTexture:size:flipped:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1547000-imagewithtexture)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImage *)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag options:(NSDictionary *)options ``` | CoreImage/CIImage.h |
| To | ``` + (CIImage * _Nonnull)imageWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithBitmapData:bytesPerRow:size:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithBitmapData:(NSData *)d bytesPerRow:(size_t)bpr size:(CGSize)size format:(CIFormat)f colorSpace:(CGColorSpaceRef)c ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithBitmapData:(NSData * _Nonnull)data bytesPerRow:(size_t)bytesPerRow size:(CGSize)size format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithCGImage:]](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)image ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCGImage:(CGImageRef _Nonnull)image ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithCGImage:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCGImage:(CGImageRef)image options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCGImage:(CGImageRef _Nonnull)image options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithCGLayer:]](https://developer.apple.com/documentation/coreimage/ciimage/1438065-initwithcglayer)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` - (id)initWithCGLayer:(CGLayerRef)layer ``` | -- | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCGLayer:(CGLayerRef _Nonnull)layer ``` | OS X 10.11 | CoreImage/CIImage.h |

Modified [-[CIImage initWithCGLayer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437687-init)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` - (id)initWithCGLayer:(CGLayerRef)layer options:(NSDictionary *)d ``` | -- | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCGLayer:(CGLayerRef _Nonnull)layer options:(NSDictionary<NSString *,id> * _Nullable)options ``` | OS X 10.11 | CoreImage/CIImage.h |

Modified [-[CIImage initWithColor:]](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithColor:(CIColor *)color ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithColor:(CIColor * _Nonnull)color ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithContentsOfURL:]](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithContentsOfURL:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437867-initwithcontentsofurl)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithContentsOfURL:(NSURL *)url options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nullable)initWithContentsOfURL:(NSURL * _Nonnull)url options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithCVImageBuffer:]](https://developer.apple.com/documentation/coreimage/ciimage/1438012-initwithcvimagebuffer)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCVImageBuffer:(CVImageBufferRef)imageBuffer ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCVImageBuffer:(CVImageBufferRef _Nonnull)imageBuffer ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithCVImageBuffer:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437617-initwithcvimagebuffer)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCVImageBuffer:(CVImageBufferRef)imageBuffer options:(NSDictionary *)dict ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithCVImageBuffer:(CVImageBufferRef _Nonnull)imageBuffer options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithData:]](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithData:(NSData *)data ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithData:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438032-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithData:(NSData *)data options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nullable)initWithData:(NSData * _Nonnull)data options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithIOSurface:]](https://developer.apple.com/documentation/coreimage/ciimage/1438030-initwithiosurface)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithIOSurface:(IOSurfaceRef)surface ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithIOSurface:(IOSurfaceRef _Nonnull)surface ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithIOSurface:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1438181-initwithiosurface)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithIOSurface:(IOSurfaceRef)surface options:(NSDictionary *)d ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithIOSurface:(IOSurfaceRef _Nonnull)surface options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithIOSurface:plane:format:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437670-init)

|  | Declaration | Deprecation | Header |
| --- | --- | --- | --- |
| From | ``` - (id)initWithIOSurface:(IOSurfaceRef)surface plane:(size_t)plane format:(CIFormat)format options:(NSDictionary *)d ``` | -- | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithIOSurface:(IOSurfaceRef _Nonnull)surface plane:(size_t)plane format:(CIFormat)format options:(NSDictionary<NSString *,id> * _Nullable)options ``` | OS X 10.11 | CoreImage/CIImage.h |

Modified [-[CIImage initWithTexture:size:flipped:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimage/1438015-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag colorSpace:(CGColorSpaceRef)cs ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped colorSpace:(CGColorSpaceRef _Nullable)colorSpace ``` | CoreImage/CIImage.h |

Modified [-[CIImage initWithTexture:size:flipped:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437880-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flag options:(NSDictionary *)options ``` | CoreImage/CIImage.h |
| To | ``` - (instancetype _Nonnull)initWithTexture:(unsigned int)name size:(CGSize)size flipped:(BOOL)flipped options:(NSDictionary<NSString *,id> * _Nullable)options ``` | CoreImage/CIImage.h |

Modified [CIImage.properties](https://developer.apple.com/documentation/coreimage/ciimage/1437733-properties)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSDictionary *)properties ``` | CoreImage/CIImage.h |
| To | ``` @property(atomic, readonly, nonnull) NSDictionary<NSString *,id> *properties ``` | CoreImage/CIImage.h |

Modified [CIImage.url](https://developer.apple.com/documentation/coreimage/ciimage/1438195-url)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSURL *)url ``` | CoreImage/CIImage.h |
| To | ``` @property(atomic, readonly, nullable) NSURL *url ``` | CoreImage/CIImage.h |

Modified [CIFormat](https://developer.apple.com/documentation/coreimage/ciformat)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified CIImage(AutoAdjustment)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIFormatARGB8](https://developer.apple.com/documentation/coreimage/ciformat/1437883-argb8)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIFormatRGBA16](https://developer.apple.com/documentation/coreimage/ciformat/1437999-rgba16)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIFormatRGBAf](https://developer.apple.com/documentation/coreimage/kciformatrgbaf)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIFormatRGBAh](https://developer.apple.com/documentation/coreimage/kciformatrgbah)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageAutoAdjustCrop](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438229-crop)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageAutoAdjustEnhance](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1437819-enhance)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageAutoAdjustFeatures](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438029-features)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageAutoAdjustLevel](https://developer.apple.com/documentation/coreimage/kciimageautoadjustlevel)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageAutoAdjustRedEye](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1437988-redeye)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageColorSpace](https://developer.apple.com/documentation/coreimage/ciimageoption/1438131-colorspace)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageProperties](https://developer.apple.com/documentation/coreimage/ciimageoption/1437679-properties)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageTextureFormat](https://developer.apple.com/documentation/coreimage/kciimagetextureformat)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

Modified [kCIImageTextureTarget](https://developer.apple.com/documentation/coreimage/kciimagetexturetarget)

|  | Header |
| --- | --- |
| From | CoreImage/CIImage.h |
| To | CoreImage/CIImage.h |

#### CIImageAccumulator.h (Removed)

Modified [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageAccumulator.h |
| To | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator clear]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427720-clear)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageAccumulator.h |
| To | CoreImage/CIImageAccumulator.h |

Modified [CIImageAccumulator.extent](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427714-extent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGRect)extent ``` | CoreImage/CIImageAccumulator.h |
| To | ``` @property(readonly) CGRect extent ``` | CoreImage/CIImageAccumulator.h |

Modified [CIImageAccumulator.format](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427716-format)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFormat)format ``` | CoreImage/CIImageAccumulator.h |
| To | ``` @property(readonly) CIFormat format ``` | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator image]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427704-image)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIImage *)image ``` | CoreImage/CIImageAccumulator.h |
| To | ``` - (CIImage * _Nonnull)image ``` | CoreImage/CIImageAccumulator.h |

Modified [+[CIImageAccumulator imageAccumulatorWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427722-imageaccumulatorwithextent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImageAccumulator *)imageAccumulatorWithExtent:(CGRect)extent format:(CIFormat)format ``` | CoreImage/CIImageAccumulator.h |
| To | ``` + (instancetype _Nonnull)imageAccumulatorWithExtent:(CGRect)extent format:(CIFormat)format ``` | CoreImage/CIImageAccumulator.h |

Modified [+[CIImageAccumulator imageAccumulatorWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427712-imageaccumulatorwithextent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIImageAccumulator *)imageAccumulatorWithExtent:(CGRect)extent format:(CIFormat)format colorSpace:(CGColorSpaceRef)colorSpace ``` | CoreImage/CIImageAccumulator.h |
| To | ``` + (instancetype _Nonnull)imageAccumulatorWithExtent:(CGRect)extent format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nonnull)colorSpace ``` | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator initWithExtent:format:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithExtent:(CGRect)extent format:(CIFormat)format ``` | CoreImage/CIImageAccumulator.h |
| To | ``` - (instancetype _Nonnull)initWithExtent:(CGRect)extent format:(CIFormat)format ``` | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator initWithExtent:format:colorSpace:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithExtent:(CGRect)extent format:(CIFormat)format colorSpace:(CGColorSpaceRef)colorSpace ``` | CoreImage/CIImageAccumulator.h |
| To | ``` - (instancetype _Nonnull)initWithExtent:(CGRect)extent format:(CIFormat)format colorSpace:(CGColorSpaceRef _Nonnull)colorSpace ``` | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator setImage:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427702-setimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)setImage:(CIImage *)im ``` | CoreImage/CIImageAccumulator.h |
| To | ``` - (void)setImage:(CIImage * _Nonnull)image ``` | CoreImage/CIImageAccumulator.h |

Modified [-[CIImageAccumulator setImage:dirtyRect:]](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)setImage:(CIImage *)im dirtyRect:(CGRect)r ``` | CoreImage/CIImageAccumulator.h |
| To | ``` - (void)setImage:(CIImage * _Nonnull)image dirtyRect:(CGRect)dirtyRect ``` | CoreImage/CIImageAccumulator.h |

#### CIImageProvider.h (Removed)

Modified [+[CIImage imageWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1579115-imagewithimageprovider)

|  | Declaration | Introduction | Header |
| --- | --- | --- | --- |
| From | ``` + (CIImage *)imageWithImageProvider:(id)p size:(size_t)width :(size_t)height format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs options:(NSDictionary *)dict ``` | OS X 10.6 | CoreImage/CIImageProvider.h |
| To | ``` + (CIImage * _Nonnull)imageWithImageProvider:(id _Nonnull)p size:(size_t)width :(size_t)height format:(CIFormat)f colorSpace:(CGColorSpaceRef _Nullable)cs options:(NSDictionary<NSString *,id> * _Nullable)options ``` | OS X 10.4 | CoreImage/CIImageProvider.h |

Modified [-[CIImage initWithImageProvider:size::format:colorSpace:options:]](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)

|  | Declaration | Introduction | Header |
| --- | --- | --- | --- |
| From | ``` - (id)initWithImageProvider:(id)p size:(size_t)width :(size_t)height format:(CIFormat)f colorSpace:(CGColorSpaceRef)cs options:(NSDictionary *)dict ``` | OS X 10.6 | CoreImage/CIImageProvider.h |
| To | ``` - (instancetype _Nonnull)initWithImageProvider:(id _Nonnull)p size:(size_t)width :(size_t)height format:(CIFormat)f colorSpace:(CGColorSpaceRef _Nullable)cs options:(NSDictionary<NSString *,id> * _Nullable)options ``` | OS X 10.4 | CoreImage/CIImageProvider.h |

Modified [-[NSObject provideImageData:bytesPerRow:origin::size::userInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)provideImageData:(void *)data bytesPerRow:(size_t)rowbytes origin:(size_t)x :(size_t)y size:(size_t)width :(size_t)height userInfo:(id)info ``` | CoreImage/CIImageProvider.h |
| To | ``` - (void)provideImageData:(void * _Nonnull)data bytesPerRow:(size_t)rowbytes origin:(size_t)x :(size_t)y size:(size_t)width :(size_t)height userInfo:(id _Nullable)info ``` | CoreImage/CIImageProvider.h |

Modified CIImage(CIImageProvider)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageProvider.h |
| To | CoreImage/CIImageProvider.h |

Modified [kCIImageProviderTileSize](https://developer.apple.com/documentation/coreimage/kciimageprovidertilesize)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageProvider.h |
| To | CoreImage/CIImageProvider.h |

Modified [kCIImageProviderUserInfo](https://developer.apple.com/documentation/coreimage/kciimageprovideruserinfo)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageProvider.h |
| To | CoreImage/CIImageProvider.h |

Modified NSObject(CIImageProvider)

|  | Header |
| --- | --- |
| From | CoreImage/CIImageProvider.h |
| To | CoreImage/CIImageProvider.h |

#### CIKernel.h (Removed)

Modified [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)

|  | Header |
| --- | --- |
| From | CoreImage/CIKernel.h |
| To | CoreImage/CIKernel.h |

Modified [+[CIKernel kernelsWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (NSArray *)kernelsWithString:(NSString *)s ``` | CoreImage/CIKernel.h |
| To | ``` + (NSArray<CIKernel *> * _Nullable)kernelsWithString:(NSString * _Nonnull)string ``` | CoreImage/CIKernel.h |

Modified [+[CIKernel kernelWithString:]](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIKernel *)kernelWithString:(NSString *)s ``` | CoreImage/CIKernel.h |
| To | ``` + (instancetype _Nullable)kernelWithString:(NSString * _Nonnull)string ``` | CoreImage/CIKernel.h |

Modified [CIKernel.name](https://developer.apple.com/documentation/coreimage/cikernel/1438067-name)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSString *)name ``` | CoreImage/CIKernel.h |
| To | ``` @property(atomic, readonly, nonnull) NSString *name ``` | CoreImage/CIKernel.h |

Modified [-[CIKernel setROISelector:]](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (void)setROISelector:(SEL)aMethod ``` | CoreImage/CIKernel.h |
| To | ``` - (void)setROISelector:(SEL _Nonnull)method ``` | CoreImage/CIKernel.h |

#### CIPlugIn.h (Removed)

Modified [CIPlugIn](https://developer.apple.com/documentation/coreimage/ciplugin)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugIn.h |
| To | CoreImage/CIPlugIn.h |

Modified [+[CIPlugIn loadAllPlugIns]](https://developer.apple.com/documentation/coreimage/ciplugin/1437653-loadallplugins)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugIn.h |
| To | CoreImage/CIPlugIn.h |

Modified [+[CIPlugIn loadNonExecutablePlugIns]](https://developer.apple.com/documentation/coreimage/ciplugin/1437599-loadnonexecutableplugins)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugIn.h |
| To | CoreImage/CIPlugIn.h |

Modified [+[CIPlugIn loadPlugIn:allowExecutableCode:]](https://developer.apple.com/documentation/coreimage/ciplugin/1438187-loadplugin)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugIn.h |
| To | CoreImage/CIPlugIn.h |

Modified [+[CIPlugIn loadPlugIn:allowNonExecutable:]](https://developer.apple.com/documentation/coreimage/ciplugin/1551323-loadplugin)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugIn.h |
| To | CoreImage/CIPlugIn.h |

#### CIPlugInInterface.h (Removed)

Modified [CIPlugInRegistration](https://developer.apple.com/documentation/coreimage/cipluginregistration)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugInInterface.h |
| To | CoreImage/CIPlugInInterface.h |

Modified [-[CIPlugInRegistration load:]](https://developer.apple.com/documentation/coreimage/cipluginregistration/1437823-load)

|  | Header |
| --- | --- |
| From | CoreImage/CIPlugInInterface.h |
| To | CoreImage/CIPlugInInterface.h |

#### CIRAWFilter.h (Removed)

Modified [+[CIFilter filterWithImageData:options:]](https://developer.apple.com/documentation/coreimage/cifilter/1437879-init)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [+[CIFilter filterWithImageURL:options:]](https://developer.apple.com/documentation/coreimage/cifilter/1438096-init)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified CIFilter(CIRAWFilter)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIActiveKeys](https://developer.apple.com/documentation/coreimage/kciactivekeys)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputAllowDraftModeKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438010-allowdraftmode)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputBiasKey](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIFilter.h |

Modified [kCIInputBoostKey](https://developer.apple.com/documentation/coreimage/kciinputboostkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputBoostShadowAmountKey](https://developer.apple.com/documentation/coreimage/kciinputboostshadowamountkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputColorNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437640-colornoisereductionamount)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputDecoderVersionKey](https://developer.apple.com/documentation/coreimage/kciinputdecoderversionkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputEnableChromaticNoiseTrackingKey](https://developer.apple.com/documentation/coreimage/kciinputenablechromaticnoisetrackingkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputEnableSharpeningKey](https://developer.apple.com/documentation/coreimage/kciinputenablesharpeningkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputEnableVendorLensCorrectionKey](https://developer.apple.com/documentation/coreimage/kciinputenablevendorlenscorrectionkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputIgnoreImageOrientationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437949-ignoreimageorientation)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputImageOrientationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437637-imageorientation)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputLinearSpaceFilter](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438078-linearspacefilter)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputLuminanceNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputluminancenoisereductionamountkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNeutralChromaticityXKey](https://developer.apple.com/documentation/coreimage/kciinputneutralchromaticityxkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNeutralChromaticityYKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438039-neutralchromaticityy)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNeutralLocationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437915-neutrallocation)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNeutralTemperatureKey](https://developer.apple.com/documentation/coreimage/kciinputneutraltemperaturekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNeutralTintKey](https://developer.apple.com/documentation/coreimage/kciinputneutraltintkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductionamountkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNoiseReductionContrastAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437681-noisereductioncontrastamount)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNoiseReductionDetailAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductiondetailamountkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputNoiseReductionSharpnessAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductionsharpnessamountkey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIInputScaleFactorKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437936-scalefactor)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCIOutputNativeSizeKey](https://developer.apple.com/documentation/coreimage/kcioutputnativesizekey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

Modified [kCISupportedDecoderVersionsKey](https://developer.apple.com/documentation/coreimage/kcisupporteddecoderversionskey)

|  | Header |
| --- | --- |
| From | CoreImage/CIRAWFilter.h |
| To | CoreImage/CIRAWFilter.h |

#### CISampler.h (Removed)

Modified [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [CISampler.definition](https://developer.apple.com/documentation/coreimage/cisampler/1437877-definition)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CIFilterShape *)definition ``` | CoreImage/CISampler.h |
| To | ``` @property(readonly, nonnull) CIFilterShape *definition ``` | CoreImage/CISampler.h |

Modified [CISampler.extent](https://developer.apple.com/documentation/coreimage/cisampler/1437872-extent)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGRect)extent ``` | CoreImage/CISampler.h |
| To | ``` @property(readonly) CGRect extent ``` | CoreImage/CISampler.h |

Modified [-[CISampler initWithImage:]](https://developer.apple.com/documentation/coreimage/cisampler/1438117-initwithimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithImage:(CIImage *)im ``` | CoreImage/CISampler.h |
| To | ``` - (instancetype _Nonnull)initWithImage:(CIImage * _Nonnull)im ``` | CoreImage/CISampler.h |

Modified [-[CISampler initWithImage:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cisampler/1555077-initwithimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithImage:(CIImage *)im keysAndValues:(id)key0, ... ``` | CoreImage/CISampler.h |
| To | ``` - (instancetype _Nonnull)initWithImage:(CIImage * _Nonnull)im keysAndValues:(id)key0, ... ``` | CoreImage/CISampler.h |

Modified [-[CISampler initWithImage:options:]](https://developer.apple.com/documentation/coreimage/cisampler/1437963-init)

|  | Declaration | Header | Designated Initializer |
| --- | --- | --- | --- |
| From | ``` - (id)initWithImage:(CIImage *)im options:(NSDictionary *)dict ``` | CoreImage/CISampler.h | -- |
| To | ``` - (instancetype _Nonnull)initWithImage:(CIImage * _Nonnull)im options:(NSDictionary * _Nullable)dict ``` | CoreImage/CISampler.h | yes |

Modified [+[CISampler samplerWithImage:]](https://developer.apple.com/documentation/coreimage/cisampler/1555075-samplerwithimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CISampler *)samplerWithImage:(CIImage *)im ``` | CoreImage/CISampler.h |
| To | ``` + (instancetype _Nonnull)samplerWithImage:(CIImage * _Nonnull)im ``` | CoreImage/CISampler.h |

Modified [+[CISampler samplerWithImage:keysAndValues:]](https://developer.apple.com/documentation/coreimage/cisampler/1555078-samplerwithimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CISampler *)samplerWithImage:(CIImage *)im keysAndValues:(id)key0, ... ``` | CoreImage/CISampler.h |
| To | ``` + (instancetype _Nonnull)samplerWithImage:(CIImage * _Nonnull)im keysAndValues:(id)key0, ... ``` | CoreImage/CISampler.h |

Modified [+[CISampler samplerWithImage:options:]](https://developer.apple.com/documentation/coreimage/cisampler/1555076-samplerwithimage)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CISampler *)samplerWithImage:(CIImage *)im options:(NSDictionary *)dict ``` | CoreImage/CISampler.h |
| To | ``` + (instancetype _Nonnull)samplerWithImage:(CIImage * _Nonnull)im options:(NSDictionary * _Nullable)dict ``` | CoreImage/CISampler.h |

Modified [kCISamplerAffineMatrix](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerFilterLinear](https://developer.apple.com/documentation/coreimage/kcisamplerfilterlinear)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerFilterMode](https://developer.apple.com/documentation/coreimage/kcisamplerfiltermode)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerFilterNearest](https://developer.apple.com/documentation/coreimage/kcisamplerfilternearest)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerWrapBlack](https://developer.apple.com/documentation/coreimage/kcisamplerwrapblack)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerWrapClamp](https://developer.apple.com/documentation/coreimage/kcisamplerwrapclamp)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

Modified [kCISamplerWrapMode](https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode)

|  | Header |
| --- | --- |
| From | CoreImage/CISampler.h |
| To | CoreImage/CISampler.h |

#### CIVector.h (Removed)

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Protocols | Header |
| --- | --- | --- |
| From | NSCoding, NSCopying | CoreImage/CIVector.h |
| To | NSCopying, NSSecureCoding | CoreImage/CIVector.h |

Modified [CIVector.CGAffineTransformValue](https://developer.apple.com/documentation/coreimage/civector/1438249-cgaffinetransformvalue)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGAffineTransform)CGAffineTransformValue ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGAffineTransform CGAffineTransformValue ``` | CoreImage/CIVector.h |

Modified [CIVector.CGPointValue](https://developer.apple.com/documentation/coreimage/civector/1437672-cgpointvalue)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGPoint)CGPointValue ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGPoint CGPointValue ``` | CoreImage/CIVector.h |

Modified [CIVector.CGRectValue](https://developer.apple.com/documentation/coreimage/civector/1438108-cgrectvalue)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGRect)CGRectValue ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGRect CGRectValue ``` | CoreImage/CIVector.h |

Modified [CIVector.count](https://developer.apple.com/documentation/coreimage/civector/1438197-count)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (size_t)count ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) size_t count ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCGAffineTransform:(CGAffineTransform)r ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithCGAffineTransform:(CGAffineTransform)r ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1438133-initwithcgpoint)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCGPoint:(CGPoint)p ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithCGPoint:(CGPoint)p ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1437644-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithCGRect:(CGRect)r ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithCGRect:(CGRect)r ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithString:]](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithString:(NSString *)representation ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithString:(NSString * _Nonnull)representation ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1437849-init)

|  | Declaration | Header | Designated Initializer |
| --- | --- | --- | --- |
| From | ``` - (id)initWithValues:(const CGFloat *)values count:(size_t)count ``` | CoreImage/CIVector.h | -- |
| To | ``` - (instancetype _Nonnull)initWithValues:(const CGFloat * _Nonnull)values count:(size_t)count ``` | CoreImage/CIVector.h | yes |

Modified [-[CIVector initWithX:]](https://developer.apple.com/documentation/coreimage/civector/1437657-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1437865-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` | CoreImage/CIVector.h |

Modified [-[CIVector initWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1438088-init)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (id)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` | CoreImage/CIVector.h |
| To | ``` - (instancetype _Nonnull)initWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` | CoreImage/CIVector.h |

Modified [CIVector.stringRepresentation](https://developer.apple.com/documentation/coreimage/civector/1437752-stringrepresentation)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (NSString *)stringRepresentation ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly, nonnull) NSString *stringRepresentation ``` | CoreImage/CIVector.h |

Modified [-[CIVector valueAtIndex:]](https://developer.apple.com/documentation/coreimage/civector/1438207-valueatindex)

|  | Header |
| --- | --- |
| From | CoreImage/CIVector.h |
| To | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithCGAffineTransform:]](https://developer.apple.com/documentation/coreimage/civector/1564090-vectorwithcgaffinetransform)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithCGAffineTransform:(CGAffineTransform)t ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithCGAffineTransform:(CGAffineTransform)t ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithCGPoint:]](https://developer.apple.com/documentation/coreimage/civector/1564086-vectorwithcgpoint)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithCGPoint:(CGPoint)p ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithCGPoint:(CGPoint)p ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithCGRect:]](https://developer.apple.com/documentation/coreimage/civector/1564085-vectorwithcgrect)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithCGRect:(CGRect)r ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithCGRect:(CGRect)r ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithString:]](https://developer.apple.com/documentation/coreimage/civector/1564093-vectorwithstring)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithString:(NSString *)representation ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithString:(NSString * _Nonnull)representation ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithValues:count:]](https://developer.apple.com/documentation/coreimage/civector/1564088-vectorwithvalues)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithValues:(const CGFloat *)values count:(size_t)count ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithValues:(const CGFloat * _Nonnull)values count:(size_t)count ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithX:]](https://developer.apple.com/documentation/coreimage/civector/1564092-vectorwithx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithX:Y:]](https://developer.apple.com/documentation/coreimage/civector/1564091-vectorwithx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithX:Y:Z:]](https://developer.apple.com/documentation/coreimage/civector/1564089-vectorwithx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z ``` | CoreImage/CIVector.h |

Modified [+[CIVector vectorWithX:Y:Z:W:]](https://developer.apple.com/documentation/coreimage/civector/1564087-vectorwithx)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` + (CIVector *)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` | CoreImage/CIVector.h |
| To | ``` + (instancetype _Nonnull)vectorWithX:(CGFloat)x Y:(CGFloat)y Z:(CGFloat)z W:(CGFloat)w ``` | CoreImage/CIVector.h |

Modified [CIVector.W](https://developer.apple.com/documentation/coreimage/civector/1438058-w)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)W ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGFloat W ``` | CoreImage/CIVector.h |

Modified [CIVector.X](https://developer.apple.com/documentation/coreimage/civector/1437738-x)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)X ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGFloat X ``` | CoreImage/CIVector.h |

Modified [CIVector.Y](https://developer.apple.com/documentation/coreimage/civector/1437843-y)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)Y ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGFloat Y ``` | CoreImage/CIVector.h |

Modified [CIVector.Z](https://developer.apple.com/documentation/coreimage/civector/1437627-z)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` - (CGFloat)Z ``` | CoreImage/CIVector.h |
| To | ``` @property(readonly) CGFloat Z ``` | CoreImage/CIVector.h |

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
