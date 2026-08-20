---
title: CircleLayout
apple_id: DTS40012315
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: UIKit
published: '2015-07-31'
source_url: https://developer.apple.com/library/archive/samplecode/CircleLayout/Listings/CircleLayout_ViewController_m.html
archived_at: '2026-07-18T03:03:20.387523Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CircleLayout](CircleLayout.md)


[Next](CircleLayout-Cell.m.md)[Previous](CircleLayout-AppDelegate.m.md)

# CircleLayout/ViewController.m

```objc
/*
Copyright (C) 2015 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The primary view controller for this app.
*/

#import "ViewController.h"
#import "Cell.h"

NSString * const cellIdentifier = @"MY_CELL";

@interface ViewController ()
@property (nonatomic, assign) NSInteger cellCount;
@end

@implementation ViewController

-(void)viewDidLoad
{
    [super viewDidLoad];
    self.cellCount = 20;
    UITapGestureRecognizer* tapRecognizer = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(handleTapGesture:)];
    [self.collectionView addGestureRecognizer:tapRecognizer];
    [self.collectionView registerClass:[Cell class] forCellWithReuseIdentifier:cellIdentifier];
    [self.collectionView reloadData];
    self.collectionView.backgroundColor = [UIColor whiteColor];
}

- (NSInteger)collectionView:(UICollectionView *)view numberOfItemsInSection:(NSInteger)section;
{
    return self.cellCount;
}

- (UICollectionViewCell *)collectionView:(UICollectionView *)cv cellForItemAtIndexPath:(NSIndexPath *)indexPath;
{
    Cell *cell = [cv dequeueReusableCellWithReuseIdentifier:cellIdentifier forIndexPath:indexPath];
    return cell;
}

- (void)handleTapGesture:(UITapGestureRecognizer *)sender {

    if (sender.state == UIGestureRecognizerStateEnded)
    {
        CGPoint initialPinchPoint = [sender locationInView:self.collectionView];
        NSIndexPath* tappedCellPath = [self.collectionView indexPathForItemAtPoint:initialPinchPoint];
        if (tappedCellPath!=nil)
        {
            self.cellCount = self.cellCount - 1;
            [self.collectionView performBatchUpdates:^{
                [self.collectionView deleteItemsAtIndexPaths:@[tappedCellPath]];

            } completion:nil];
        }
        else
        {
            self.cellCount = self.cellCount + 1;
            [self.collectionView performBatchUpdates:^{
                [self.collectionView insertItemsAtIndexPaths:@[[NSIndexPath indexPathForItem:0 inSection:0]]];
            } completion:nil];
        }
    }
}

@end
```

[Next](CircleLayout-Cell.m.md)[Previous](CircleLayout-AppDelegate.m.md)

