---
title: 'PhotoMap: Loading and displaying geotagged photos as MapKit annotations'
apple_id: DTS40011109
resource_type: Sample Code
platform: iOS
topic: User Experience
technology: MapKit
published: '2018-04-26'
source_url: https://developer.apple.com/library/archive/samplecode/PhotoMap/Listings/PhotoMap_LoadingStatus_m.html
archived_at: '2026-07-18T03:18:52.104093Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PhotoMap: Loading and displaying geotagged photos as MapKit annotations](PhotoMap-%20Loading%20and%20displaying%20geotagged%20photos%20as%20MapKit%20annotations.md)


[Next](PhotoMap-PhotoMapViewController.m.md)[Previous](PhotoMap-PhotoMapAppDelegate.h.md)

# PhotoMap/LoadingStatus.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View for displaying the loading status.
 */

#import "LoadingStatus.h"

@interface LoadingStatus ()

@property (nonatomic, strong) UIActivityIndicatorView *progress;
@property (nonatomic, strong) UILabel *loadingLabel;

@end


#pragma mark -

@implementation LoadingStatus

+ (id)defaultLoadingStatusWithWidth:(CGFloat)width {

    return [[LoadingStatus alloc] initWithFrame:CGRectMake(0.0, 0.0, width, 40.0)];
}

- (id)initWithFrame:(CGRect)frame {

    if ((self = [super initWithFrame:frame])) {
        self.backgroundColor = [UIColor colorWithRed:0.0f green:0.0f blue:0.0f alpha:0.4f];

        NSString *loadingString = @"Loading Photos…";

        UIFont *loadingFont = [UIFont boldSystemFontOfSize:17.0f];

        NSDictionary *attrs = @{NSFontAttributeName:loadingFont};

        CGRect rect = [loadingString boundingRectWithSize:CGSizeMake(CGRectGetWidth(frame), CGRectGetHeight(frame))
                                         options:(NSStringDrawingUsesLineFragmentOrigin | NSStringDrawingUsesFontLeading)
                                      attributes:attrs
                                         context:nil];
        CGSize labelSize = rect.size;

        CGFloat centerX = floor((CGRectGetWidth(frame) / 2.0f) - (labelSize.width / 2.0f));
        CGFloat centerY = floor((CGRectGetHeight(frame) / 2.0f) - (labelSize.height / 2.0f));
        _loadingLabel = [[UILabel alloc] initWithFrame: CGRectMake(centerX, centerY, labelSize.width, labelSize.height)];
        self.loadingLabel.backgroundColor = [UIColor clearColor];
        self.loadingLabel.textColor = [UIColor whiteColor];
        self.loadingLabel.text = loadingString;
        self.loadingLabel.font = loadingFont;

        _progress = [[UIActivityIndicatorView alloc] initWithActivityIndicatorStyle:UIActivityIndicatorViewStyleWhite];
        CGRect progressFrame = self.progress.frame;
        progressFrame.origin.x = centerX - CGRectGetWidth(progressFrame) - 8.0f;
        progressFrame.origin.y = centerY;
        self.progress.frame = progressFrame;

        [self addSubview:self.progress];
        [self addSubview:self.loadingLabel];

    }
    return self;
}

- (void)willRemoveSubview:(UIView *)subview {

    if (subview == self.progress)
        [self.progress stopAnimating];

    [super willRemoveSubview:subview];
}

- (void)didMoveToWindow {

    [super didMoveToWindow];

    [self.progress startAnimating];
}

- (void)removeFromSuperviewWithFade {

    [UIView animateWithDuration:0.3f animations:^(void) {
        self.alpha = 0.0f;
    } completion:^(BOOL finished) {
        if (finished) {
            [self removeFromSuperview];
        }
    }];
}

@end
```

[Next](PhotoMap-PhotoMapViewController.m.md)[Previous](PhotoMap-PhotoMapAppDelegate.h.md)

