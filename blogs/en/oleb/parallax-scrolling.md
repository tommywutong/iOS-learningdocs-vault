---
title: Parallax Scrolling
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/05/parallax-scrolling-collectionview/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6857b0d52fdf7804'
translated: false
---

> 原文：[Parallax Scrolling](https://oleb.net/blog/2014/05/parallax-scrolling-collectionview/)　·　Ole Begemann

# Parallax Scrolling

<sub>A list of photos in a collection view. Note the parallax effect of the images when the list scrolls. [Download the video (H.264)](https://oleb.net/media/parallax-scrolling-640x1136.mp4).</sub>

[Parallax scrolling](https://en.wikipedia.org/wiki/Parallax_scrolling) is a big UI design trend these days. In this article, I want to show you how to write a collection view that applies a nice parallax effect to its cells during scrolling. It is similar to the photos view in the WhatsApp app. Check out the video on the right for a demo.

# The Idea

It looks like we will have to constantly reposition the images according to the current scroll position. We know that [scroll views scroll by translating their bounds](https://oleb.net/blog/2014/04/understanding-uiscrollview/). This suggests a fairly simple solution for our problem:

1. Whenever the collection view scrolls, compute the center point of the collection view’s `bounds`. This will be the reference point: a cell’s distance from this point should determine the amount by which we shift the image the cell displays.
2. For each visible cell, compute the distance of its center point (in the collection view’s coordinate system) to the reference point. Move the cell’s image view by a factor that is proportional to the (vertical) distance.

Since a [`UICollectionView`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionView_class/Reference/Reference.html) is a [`UIScrollView`](https://developer.apple.com/library/ios/documentation/uikit/reference/UIScrollView_Class/Reference/UIScrollView.html), we could translate this directly into code. It would just be a matter of implementing the `scrollViewDidScroll:` delegate method in your view controller, asking the collection view for all visible cells, and modifying them directly.^[1](#fn:1) Since we are dealing with a collection view, there is a more elegant way, however.

The positionign of the images inside the cells is a question of _layout_, and collection views provide a mechanism to encapsulate all layout code in a separate object. By writing a custom collection view layout, we can implement the parallax effect in a fairly transparent way.

# A Custom Collection View Layout

A collection view layout is responsible for determining all attributes that are relevant for the positioning and sizing of the collection view’s cells (and of supplementary and decoration views, but we are not dealing with those in this example). Layouts use [`UICollectionViewLayoutAttributes`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionViewLayoutAttributes_class/Reference/Reference.html) objects to pass layout properties to cells, and we should take a look at that class first before we implement our custom layout.

**Update May 4, 2014:** I updated the code and text with [some](https://twitter.com/LilyInTech/status/462675687296348160) [fixes](https://twitter.com/LilyInTech/status/462677425067790336) [suggested](https://twitter.com/LilyInTech/status/462676836489510913) by Lily Ballard. Thank you Lily!

## UICollectionViewLayoutAttributes

`UICollectionViewLayoutAttributes` supports several standard attributes and it can be subclassed to define custom ones. Our layout should compute another value called `parallaxOffset` that tells the cell the amount by which it should shift its image up or down. So let’s create our own `ParallaxLayoutAttributes` class that includes a `parallaxOffset` property:

```
// ParallaxLayoutAttributes.h
@import UIKit;

@interface ParallaxLayoutAttributes : UICollectionViewLayoutAttributes

@property (nonatomic) CGPoint parallaxOffset;

@end

// ParallaxLayoutAttributes.m
#import "ParallaxLayoutAttributes.h"

@implementation ParallaxLayoutAttributes

- (id)copyWithZone:(NSZone *)zone
{
    ParallaxLayoutAttributes *copy = [super copyWithZone:zone];
    NSAssert([copy isKindOfClass:[self class]], @"copy must have the same class");
    copy.parallaxOffset = self.parallaxOffset;
    return copy;
}

- (BOOL)isEqual:(id)object
{
    if (![object isKindOfClass:[ParallaxLayoutAttributes class]]) {
        return NO;
    }

    ParallaxLayoutAttributes *otherObject = object;
    if (!CGPointEqualToPoint(self.parallaxOffset, otherObject.parallaxOffset)) {
        return NO;
    }
    return [super isEqual:otherObject];
}

@end
```

I declare `parallaxOffset` as a `CGPoint` although we are only dealing with vertical offsets in this example. This gives us the option to support horizontal offsets in the future, too.

As you can see, the class implementation makes sure to take the added property into account when instances are copied or compared. This requirement is clearly noted in the documentation for `UICollectionViewLayoutAttributes`:

> Because layout attribute objects may be copied by the collection view, make sure your subclass conforms to the `NSCopying` protocol by implementing any methods appropriate for copying your custom attributes to new instances of your subclass. … If you subclass and implement any custom layout attributes, you must also override the inherited `isEqual:` method to compare the values of your properties.

**Update May 4, 2014:** My original implementation of the `isEqual:` method was missing the check of the class of the parameter.

## Subclassing UICollectionViewFlowLayout

We can base our own layout on the existing `UICollectionViewFlowLayout` implementation. The flow layout already performs all the computations to position and size the cells correctly — all we have to do is add our own calculation for the parallax offset to that result.

I am going to discuss the implementation of our `ParallaxFlowLayout` class piece by piece:

```
// ParallaxFlowLayout.h
@import UIKit;

@interface ParallaxFlowLayout : UICollectionViewFlowLayout

@property (nonatomic, readonly) CGFloat maxParallaxOffset;

@end
```

Our layout class has one read-only property that reports the maximum parallax offset a (visible) cell can have. The collection view uses this information to report the correct size for each cell. It also passes this value to each cell so that the cell knows how big it should make its internal image view.

```
// ParallaxFlowLayout.m
#import "ParallaxFlowLayout.h"
#import "ParallaxLayoutAttributes.h"

static const CGFloat MaxParallaxOffset = 30.0;

@implementation ParallaxFlowLayout

+ (Class)layoutAttributesClass
{
    return [ParallaxLayoutAttributes class];
}

- (CGFloat)maxParallaxOffset
{
    return MaxParallaxOffset;
}
```

We first override the `+layoutAttributesClass` class method to tell the layout which class it should use to instantiate layout attributes objects. This ensures that each layout attributes object has the `parallaxOffset` property we defined above. Also, we return a constant value for `maxParallaxOffset`.

```
- (BOOL)shouldInvalidateLayoutForBoundsChange:(CGRect)newBounds
{
    return YES;
}
```

This tells the collection view that the layout needs to be recomputed on every bounds change (i.e., every time the view scrolls). The default is `NO` because layout invalidations are potentially expensive and most layouts do not require an update on each scroll event — ours does because the cells’ parallax offsets change with scrolling.

```
- (NSArray *)layoutAttributesForElementsInRect:(CGRect)rect
{
    NSArray *layoutAttributesArray =
        [super layoutAttributesForElementsInRect:rect];
    for (ParallaxLayoutAttributes *layoutAttributes in layoutAttributesArray) {
        if (layoutAttributes.representedElementCategory ==
            UICollectionElementCategoryCell)
        {
            layoutAttributes.parallaxOffset =
                [self parallaxOffsetForLayoutAttributes:layoutAttributes];
        }
    }
    return layoutAttributesArray;
}

- (UICollectionViewLayoutAttributes *)layoutAttributesForItemAtIndexPath:(NSIndexPath *)indexPath
{
    ParallaxLayoutAttributes *layoutAttributes = (ParallaxLayoutAttributes *)
        [super layoutAttributesForItemAtIndexPath:indexPath];
    layoutAttributes.parallaxOffset =
        [self parallaxOffsetForLayoutAttributes:layoutAttributes];
    return layoutAttributes;
}
```

These two methods are invoked by the collection view whenever it needs to ask the layout to provide the layout attributes for one or multiple cells. Our implementation is simple: let `super` do the work for the standard layout attributes and then invoke our own custom method `parallaxOffsetForLayoutAttributes:` (discussed below) to compute the parallax offset.

**Update May 4, 2014:** Note that the layout attributes array in `layoutAttributesForElementsInRect:` may include layout attributes for supplementary and decoration views. Since we don’t want to apply a parallax to those views, we check the `representedElementCategory` to set the parallax offset only on cells.

Should performance become a problem due to the frequent layout invalidations, we could try caching the results returned from the `super` invocations and only recompute the parallax offset during scrolling.^[2](#fn:2) To make this work, we would have to do the following:

- Subclass [`UICollectionViewLayoutInvalidationContext`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionViewLayoutInvalidationContext_class/Reference/Reference.html). Define a boolean property called `invalidateParallaxOffset` in the subclass.
- Override the [`+invalidationContextClass`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionViewLayout_class/Reference/Reference.html#//apple_ref/doc/uid/TP40012185-CH1-SW38) and return the custom `UICollectionViewLayoutInvalidationContext` subclass.
- Override [`invalidationContextForBoundsChange:`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionViewLayout_class/Reference/Reference.html#//apple_ref/doc/uid/TP40012185-CH1-SW39). In the implementation, invoke `super` first, then check if the bounds change only affected the origin (i.e., the size of the bounds has remained constant). If so, set `invalidateParallaxOffset = YES` on the context object before you return it.
- Implement [`invalidateLayoutWithContext:`](https://developer.apple.com/library/ios/documentation/uikit/reference/UICollectionViewLayout_class/Reference/Reference.html#//apple_ref/doc/uid/TP40012185-CH1-SW42). If the context parameter has `parallaxOffset == NO` set, throw away the cached layout information.

```
- (CGPoint)parallaxOffsetForLayoutAttributes:(ParallaxLayoutAttributes *)layoutAttributes
{
    NSParameterAssert(layoutAttributes != nil);
    NSParameterAssert([layoutAttributes isKindOfClass:[ParallaxLayoutAttributes class]]);

    CGRect bounds = self.collectionView.bounds;
    CGPoint boundsCenter = CGPointMake(CGRectGetMidX(bounds),
        CGRectGetMidY(bounds));
    CGPoint cellCenter = layoutAttributes.center;
    CGPoint offsetFromCenter = CGPointMake(boundsCenter.x - cellCenter.x,
        boundsCenter.y - cellCenter.y);

    CGSize cellSize = layoutAttributes.size;
    CGFloat maxVerticalOffsetWhereCellIsStillVisible =
        (bounds.size.height / 2) + (cellSize.height / 2);
    CGFloat scaleFactor = self.maxParallaxOffset /
        maxVerticalOffsetWhereCellIsStillVisible;

    CGPoint parallaxOffset = CGPointMake(0.0, offsetFromCenter.y * scaleFactor);

    return parallaxOffset;
}

@end
```

The computation of the parallax offset follows the idea outlined above. We first determine the center of the collection view’s current bounds and calculate the cell’s distance from that point. The `parallaxOffset` is then scaled in such a way that it reaches `maxParallaxOffset` just as the cell moves outside the visible bounds.

## Applying Parallax Offset to Cells

The final piece of the puzzle is the implementation of the collection view cells. The image view that displays the photo must be taller than the cell itself to provide room for shifting it. By setting up a layout constraint that makes the image view’s height equal to the cell’s height plus `2 * maxParallaxOffset`, we make sure we can move the image view up or down by `maxParallaxOffset` without running out of content.

I also set up a second layout constraint that centers the image view vertically in the cell:

```
// ParallaxPhotoCell.m
self.imageViewCenterYConstraint = [NSLayoutConstraint constraintWithItem:self.imageView
    attribute:NSLayoutAttributeCenterY
    relatedBy:NSLayoutRelationEqual
    toItem:self.contentView
    attribute:NSLayoutAttributeCenterY
    multiplier:1
    constant:0];
[self.contentView addConstraint:self.imageViewCenterYConstraint];
```

By later setting the `constant` of this constraint to the `parallaxOffset` we get from the layout, we can shift the image view very easily. `UICollectionViewCell` includes a method named `applyLayoutAttributes:` for this purpose, which we override to apply the parallax offset to the constraint:

```
- (void)applyLayoutAttributes:(UICollectionViewLayoutAttributes *)layoutAttributes
{
    [super applyLayoutAttributes:layoutAttributes];

    NSParameterAssert(layoutAttributes != nil);
    NSParameterAssert([layoutAttributes isKindOfClass:[ParallaxLayoutAttributes class]]);

    ParallaxLayoutAttributes *parallaxLayoutAttributes =
        (ParallaxLayoutAttributes *)layoutAttributes;
    self.imageViewCenterYConstraint.constant =
        parallaxLayoutAttributes.parallaxOffset.y;
}
```

# Conclusion

And that’s it. I’m not showing the implementation of the collection view controller here as it is mostly boilerplate (setting up the data source and configuring the cells). The full code [is available on GitHub](https://github.com/ole/CollectionViewParallaxScrolling).

Writing a custom collection view layout takes a few more lines of code than the straightforward implementation, but it is repaid by a much clearer separation of concerns.

**Update February 21, 2015:** Engin Kurutepe wrote [a follow-up article](http://www.kurutepe.com/2015/02/parallax-scrolling-as-a-category-on-uicollectionview/) in which he discusses possible performance problems with my approach. If your collection view layout is computation-intensive, you should definitely investigate caching or take a look at Engin’s solution.

1. If you want to check out how one would implement this, [this project on GitHub](https://github.com/mayuur/MJParallaxCollectionView) uses this approach. [↩︎](#fnref:1)
2. You should measure carefully if caching actually improves performance in this case. It’s perfectly possible that `UICollectionViewFlowLayout` already performs some caching internally and adding another caching layer wouldn’t help a bit. [↩︎](#fnref:2)
