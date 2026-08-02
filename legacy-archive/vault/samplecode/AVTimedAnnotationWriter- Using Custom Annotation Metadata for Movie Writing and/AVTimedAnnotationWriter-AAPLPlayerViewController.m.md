---
title: 'AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing
  and Playback'
apple_id: TP40014496
resource_type: Sample Code
platform: iOS
topic: null
technology: AVFoundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVTimedAnnotationWriter/Listings/AVTimedAnnotationWriter_AAPLPlayerViewController_m.html
archived_at: '2026-07-18T03:00:31.779776Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVTimedAnnotationWriter: Using Custom Annotation Metadata for Movie Writing and Playback](AVTimedAnnotationWriter-%20Using%20Custom%20Annotation%20Metadata%20for%20Movie%20Writing%20and.md)


[Next](AVTimedAnnotationWriter-AAPLViewController.m.md)[Previous](AVTimedAnnotationWriter-AAPLAppDelegate.h.md)

# AVTimedAnnotationWriter/AAPLPlayerViewController.m

```objc
/*
 Copyright (C) 2014 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:

  Player view controller which sets up playback of movie file with metadata and uses AVPlayerItemMetadataOutput to render circle and text annotation during playback.

 */

@import AVFoundation;

#import "AAPLPlayerViewController.h"
#import "AAPLTimedAnnotationWriter.h"
#import "AAPLPlayerView.h"

@interface AAPLPlayerViewController () <AVPlayerItemMetadataOutputPushDelegate>

// Video track
@property AVAssetTrack      *videoTrack;

// Annotation state
@property CAShapeLayer      *circleLayer;
@property UILabel           *annotationText;
@property UIColor           *annotationColor;

@end

@implementation AAPLPlayerViewController

- (void)setupPlaybackWithURL:(NSURL *)movieURL
{
    if (!self.player)
    {
        // Set up player to preview the file which was just exported
        AVAsset *asset = [AVURLAsset assetWithURL:movieURL];
        [asset loadValuesAsynchronouslyForKeys:@[@"tracks"] completionHandler:^{
            // Get the first enabled video track in the asset.
            NSArray *videoTracks = [asset tracksWithMediaType:AVMediaTypeVideo];
            NSUInteger firstEnabledVideoTrackIndex = [videoTracks indexOfObjectPassingTest:^(id obj, NSUInteger idx, BOOL *stop)
            {
                AVAssetTrack *videoTrack = (AVAssetTrack *)obj;
                if ([videoTrack isEnabled])
                {
                    *stop = YES;
                    return YES;
                }
                return NO;
            }];

            if (firstEnabledVideoTrackIndex != NSNotFound)
            {
                self.videoTrack = [videoTracks objectAtIndex:firstEnabledVideoTrackIndex];
            }
        }];

        AVPlayerItem *playerItem = [AVPlayerItem playerItemWithAsset:asset];
        // Add player item metadata output to receive timed metadata groups during playback
        AVPlayerItemMetadataOutput *output = [[AVPlayerItemMetadataOutput alloc] initWithIdentifiers:nil];
        [output setDelegate:self queue:dispatch_get_main_queue()];
        [playerItem addOutput:output];
        self.player = [AVPlayer playerWithPlayerItem:playerItem];

        // Default annotation color is set to green
        self.annotationColor = [UIColor greenColor];
        // We use two finger tap to change the annotation color
        UITapGestureRecognizer *twoFingerTap = [[UITapGestureRecognizer alloc] initWithTarget:self action:@selector(changeAnnotationColor:)];
        [twoFingerTap setNumberOfTouchesRequired:2];
        [self.view addGestureRecognizer:twoFingerTap];
    }
}

#pragma mark - AVPlayerItemMetadataOutputPushDelegate

- (void)metadataOutput:(AVPlayerItemMetadataOutput *)output didOutputTimedMetadataGroups:(NSArray *)groups fromPlayerItemTrack:(AVPlayerItemTrack *)track
{
    NSArray *referencedTracks = [[track assetTrack] associatedTracksOfType:AVTrackAssociationTypeMetadataReferent];
    if (![referencedTracks containsObject:self.videoTrack])
        return;

    for (AVTimedMetadataGroup *group in groups)
    {
        // Circle coordinate item
        AVMetadataItem *centerItem = [[AVMetadataItem metadataItemsFromArray:[group items] filteredByIdentifier:AAPLTimedAnnotationWriterCircleCenterCoordinateIdentifier] firstObject];
        // Circle radius item
        AVMetadataItem *radiusItem = [[AVMetadataItem metadataItemsFromArray:[group items] filteredByIdentifier:AAPLTimedAnnotationWriterCircleRadiusIdentifier] firstObject];
        // Annotation text item
        AVMetadataItem *textItem = [[AVMetadataItem metadataItemsFromArray:[group items] filteredByIdentifier:AAPLTimedAnnotationWriterCommentFieldIdentifier] firstObject];

        float radius = 0.0;
        CGPoint center = CGPointZero;
        NSString *commentText = nil;

        if (radiusItem.value)
            radius = [(NSNumber *)radiusItem.value floatValue];
        if (centerItem.value)
            center = CGPointMake([[(NSDictionary *)centerItem.value objectForKey:@"X"] floatValue], [[(NSDictionary *)centerItem.value objectForKey:@"Y"] floatValue]);
        if (textItem.value)
            commentText = textItem.stringValue;

        // Create CAShapeLayer which has gray rectangle with 0.5 opacity and circle (focus ring) of radius with 0 opacity
        // This shape layer is similar to the one drawn in updateCircleLayerWithCenter:radius:
        // Here we use the positioning information from AVPlayerItemMetadataOutput
        UIBezierPath *path = [UIBezierPath bezierPathWithRoundedRect:CGRectMake(-2000, -2000, self.view.bounds.size.width * 5, self.view.bounds.size.height * 5) cornerRadius:0];
        UIBezierPath *circlePath = [UIBezierPath bezierPathWithRoundedRect:CGRectMake(center.x - radius, center.y - radius, 2.0*radius, 2.0*radius) cornerRadius:radius];
        [path appendPath:circlePath];
        [path setUsesEvenOddFillRule:YES];

        CAShapeLayer *fillLayer = [CAShapeLayer layer];
        fillLayer.path = path.CGPath;
        fillLayer.fillRule = kCAFillRuleEvenOdd;
        fillLayer.fillColor = [UIColor clearColor].CGColor;
        fillLayer.strokeColor = self.annotationColor.CGColor;
        fillLayer.lineWidth = 5;
        fillLayer.opacity = 0.5;

        [self.circleLayer removeFromSuperlayer];
        self.circleLayer = fillLayer;
        [self.circleLayer setHidden:NO];
        [self.view.layer addSublayer:self.circleLayer];

        UILabel *newAnnotationText = [[UILabel alloc] initWithFrame:CGRectMake(center.x + radius, center.y - radius, 200, 40)];
        newAnnotationText.text = commentText;
        newAnnotationText.textColor = [UIColor whiteColor];
        newAnnotationText.backgroundColor = self.annotationColor;
        newAnnotationText.textAlignment = NSTextAlignmentCenter;

        [self.annotationText removeFromSuperview];
        self.annotationText = newAnnotationText;
        [self.view addSubview:self.annotationText];
    }
}

#pragma mark - Gesture resognizer

- (void)changeAnnotationColor:(UITapGestureRecognizer *)recognizer
{
    // For every two finger tap we change the color of the annotation being drawn from green -> blue -> red -> green
    if ([self.annotationColor isEqual:[UIColor greenColor]])
    {
        self.annotationColor = [UIColor blueColor];
    }
    else if ([self.annotationColor isEqual:[UIColor blueColor]])
    {
        self.annotationColor = [UIColor redColor];
    }
    else if ([self.annotationColor isEqual:[UIColor redColor]])
    {
        self.annotationColor = [UIColor greenColor];
    }

    // Update circleLayer and annotationText color to match the new color
    self.circleLayer.strokeColor = self.annotationColor.CGColor;
    self.annotationText.backgroundColor = self.annotationColor;
}

@end
```

[Next](AVTimedAnnotationWriter-AAPLViewController.m.md)[Previous](AVTimedAnnotationWriter-AAPLAppDelegate.h.md)

