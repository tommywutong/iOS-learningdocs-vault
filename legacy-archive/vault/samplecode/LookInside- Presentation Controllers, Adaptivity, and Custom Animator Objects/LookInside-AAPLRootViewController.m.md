---
title: 'LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects'
apple_id: TP40014643
resource_type: Sample Code
platform: iOS
topic: null
technology: UIKit
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LookInside/Listings/LookInside_AAPLRootViewController_m.html
archived_at: '2026-07-18T03:13:49.681435Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LookInside: Presentation Controllers, Adaptivity, and Custom Animator Objects](LookInside-%20Presentation%20Controllers%2C%20Adaptivity%2C%20and%20Custom%20Animator%20Objects.md)


[Next](LookInside-AAPLOverlayViewController.m.md)[Previous](LookInside-AAPLCoolPresentationController.m.md)

# LookInside/AAPLRootViewController.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  AAPLRootViewController implementation.

 */

#import "AAPLRootViewController.h"
#import "AAPLPhotoCollectionViewCell.h"
#import "AAPLOverlayViewController.h"

#import "AAPLOverlayTransitioner.h"
#import "AAPLCoolTransitioner.h"

#define kNumberOfViews (37)
#define kViewsWide (5)
#define kViewMargin (2.0)
#define kCellReuseIdentifier @"CellReuseIdentifier"

@implementation AAPLRootViewController

- (instancetype)init
{
    UICollectionViewFlowLayout *layout = [[UICollectionViewFlowLayout alloc] init];
    self = [super initWithCollectionViewLayout:layout];
    if (self)
    {
        [self configureTitleBar];
    }
    return self;
}

- (void)viewDidLoad
{
    [[self collectionView] registerClass:[AAPLPhotoCollectionViewCell class] forCellWithReuseIdentifier:kCellReuseIdentifier];
    [[self collectionView] setBackgroundColor:nil];
    UICollectionViewFlowLayout *layout = (UICollectionViewFlowLayout *)[self collectionViewLayout];

    [layout setMinimumInteritemSpacing:kViewMargin];
    [layout setMinimumLineSpacing:kViewMargin];

    [self viewWillTransitionToSize:[[self view] bounds].size withTransitionCoordinator:nil];
}

- (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    return kNumberOfViews;
}

- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath
{
    AAPLPhotoCollectionViewCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:kCellReuseIdentifier forIndexPath:indexPath];
    NSString *photoName = [@([indexPath item]) stringValue];
    UIImage *photo = [UIImage imageNamed:photoName];

    [cell setImage:photo];

    return cell;
}

- (void)collectionView:(UICollectionView *)collectionView didSelectItemAtIndexPath:(NSIndexPath *)indexPath
{
    AAPLOverlayViewController *overlay = [[AAPLOverlayViewController alloc] init];

    // Change our transitioning delegate based on whether or not the presentation should be awesome

    if([self presentationShouldBeAwesome])
    {
        _transitioningDelegate = [[AAPLCoolTransitioningDelegate alloc] init];
    }
    else
    {
        _transitioningDelegate = [[AAPLOverlayTransitioningDelegate alloc] init];
    }

    [overlay setTransitioningDelegate:[self transitioningDelegate]];

    AAPLPhotoCollectionViewCell *selectedCell = (AAPLPhotoCollectionViewCell *)[collectionView cellForItemAtIndexPath:indexPath];

    [overlay setPhotoView:selectedCell];

    [self presentViewController:overlay animated:YES completion:NULL];
}

- (BOOL)presentationShouldBeAwesome
{
    return [[self coolSwitch] isOn];
}

- (void)viewWillTransitionToSize:(CGSize)size withTransitionCoordinator:(id<UIViewControllerTransitionCoordinator>)coordinator
{
    [super viewWillTransitionToSize:size withTransitionCoordinator:coordinator];

    CGFloat itemWidth = size.width / kViewsWide;
    itemWidth -= kViewMargin;

    // Base our item size off of our view size
    [(UICollectionViewFlowLayout *)[[self collectionView] collectionViewLayout] setItemSize:CGSizeMake(itemWidth, itemWidth)];
    [[self collectionViewLayout] invalidateLayout];
}

- (NSUInteger)supportedInterfaceOrientations
{
    return UIInterfaceOrientationMaskAll;
}

- (void)configureTitleBar
{
    [self setTitle:NSLocalizedString(@"LookInside Photos", @"App Title")];
    [self setEdgesForExtendedLayout:UIRectEdgeLeft | UIRectEdgeBottom | UIRectEdgeRight];

    _coolSwitch = [[UISwitch alloc] init];
    [[self coolSwitch] setOnTintColor:[UIColor purpleColor]];
    [[self coolSwitch] setTintColor:[UIColor colorWithRed:1.0 green:0.0 blue:0.0 alpha:0.2]];

    UIBarButtonItem *enablecoolBarButtonItem = [[UIBarButtonItem alloc] initWithCustomView:[self coolSwitch]];

    [[self navigationItem] setLeftBarButtonItem:enablecoolBarButtonItem];
}

@end
```

[Next](LookInside-AAPLOverlayViewController.m.md)[Previous](LookInside-AAPLCoolPresentationController.m.md)

