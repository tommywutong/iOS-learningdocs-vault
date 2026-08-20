---
title: 'AVCamManual: Extending AVCam to Use Manual Capture API'
apple_id: TP40014578
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-15'
source_url: https://developer.apple.com/library/archive/samplecode/AVCamManual/Listings/AVCamManual_AVCamManualPhotoCaptureDelegate_m.html
archived_at: '2026-07-18T03:00:02.784722Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCamManual: Extending AVCam to Use Manual Capture API](AVCamManual-%20Extending%20AVCam%20to%20Use%20Manual%20Capture%20API.md)


[Next](AVCamManual-AVCamManualPreviewView.h.md)[Previous](AVCamManual-AVCamManualPreviewView.m.md)

# AVCamManual/AVCamManualPhotoCaptureDelegate.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    Photo capture delegate.
*/

#import "AVCamManualPhotoCaptureDelegate.h"

@import Photos;

@interface AVCamManualPhotoCaptureDelegate ()

@property (nonatomic, readwrite) AVCapturePhotoSettings *requestedPhotoSettings;
@property (nonatomic) void (^willCapturePhotoAnimation)();
@property (nonatomic) void (^completed)(AVCamManualPhotoCaptureDelegate *photoCaptureDelegate);

@property (nonatomic) NSData *jpegPhotoData;
@property (nonatomic) NSData *dngPhotoData;

@end

@implementation AVCamManualPhotoCaptureDelegate

- (instancetype)initWithRequestedPhotoSettings:(AVCapturePhotoSettings *)requestedPhotoSettings willCapturePhotoAnimation:(void (^)())willCapturePhotoAnimation completed:(void (^)(AVCamManualPhotoCaptureDelegate *))completed
{
    self = [super init];
    if ( self ) {
        self.requestedPhotoSettings = requestedPhotoSettings;
        self.willCapturePhotoAnimation = willCapturePhotoAnimation;
        self.completed = completed;
    }
    return self;
}

- (void)didFinish
{
    self.completed( self );
}

- (void)captureOutput:(AVCapturePhotoOutput *)captureOutput willCapturePhotoForResolvedSettings:(AVCaptureResolvedPhotoSettings *)resolvedSettings
{
    self.willCapturePhotoAnimation();
}

- (void)captureOutput:(AVCapturePhotoOutput *)captureOutput didFinishProcessingPhotoSampleBuffer:(CMSampleBufferRef)photoSampleBuffer previewPhotoSampleBuffer:(CMSampleBufferRef)previewPhotoSampleBuffer resolvedSettings:(AVCaptureResolvedPhotoSettings *)resolvedSettings bracketSettings:(AVCaptureBracketedStillImageSettings *)bracketSettings error:(NSError *)error
{
    if ( error != nil ) {
        NSLog( @"Error capturing photo: %@", error );
        return;
    }

    self.jpegPhotoData = [AVCapturePhotoOutput JPEGPhotoDataRepresentationForJPEGSampleBuffer:photoSampleBuffer previewPhotoSampleBuffer:previewPhotoSampleBuffer];
}

- (void)captureOutput:(AVCapturePhotoOutput *)captureOutput didFinishProcessingRawPhotoSampleBuffer:(CMSampleBufferRef)rawSampleBuffer previewPhotoSampleBuffer:(CMSampleBufferRef)previewPhotoSampleBuffer resolvedSettings:(AVCaptureResolvedPhotoSettings *)resolvedSettings bracketSettings:(AVCaptureBracketedStillImageSettings *)bracketSettings error:(NSError *)error
{
    if ( error != nil ) {
        NSLog( @"Error capturing RAW photo: %@", error );
        return;
    }

    self.dngPhotoData = [AVCapturePhotoOutput DNGPhotoDataRepresentationForRawSampleBuffer:rawSampleBuffer previewPhotoSampleBuffer:previewPhotoSampleBuffer];
}

- (void)captureOutput:(AVCapturePhotoOutput *)captureOutput didFinishCaptureForResolvedSettings:(AVCaptureResolvedPhotoSettings *)resolvedSettings error:(NSError *)error
{
    if ( error != nil ) {
        NSLog( @"Error capturing photo: %@", error );
        [self didFinish];
        return;
    }

    if ( self.jpegPhotoData == nil && self.dngPhotoData == nil ) {
        NSLog( @"No photo data resource" );
        [self didFinish];
        return;
    }

    [PHPhotoLibrary requestAuthorization:^( PHAuthorizationStatus status ) {
        if ( status == PHAuthorizationStatusAuthorized ) {

            NSURL *temporaryDNGFileURL;
            if ( self.dngPhotoData ) {
                temporaryDNGFileURL = [NSURL fileURLWithPath:[NSTemporaryDirectory() stringByAppendingPathComponent:[NSString stringWithFormat:@"%lld.dng", resolvedSettings.uniqueID]]];
                [self.dngPhotoData writeToURL:temporaryDNGFileURL atomically:YES];
            }

            [[PHPhotoLibrary sharedPhotoLibrary] performChanges:^{
                PHAssetCreationRequest *creationRequest = [PHAssetCreationRequest creationRequestForAsset];

                if ( self.jpegPhotoData ) {
                    [creationRequest addResourceWithType:PHAssetResourceTypePhoto data:self.jpegPhotoData options:nil];

                    if ( temporaryDNGFileURL ) {
                        PHAssetResourceCreationOptions *companionDNGResourceOptions = [[PHAssetResourceCreationOptions alloc] init];
                        companionDNGResourceOptions.shouldMoveFile = YES;
                        [creationRequest addResourceWithType:PHAssetResourceTypeAlternatePhoto fileURL:temporaryDNGFileURL options:companionDNGResourceOptions];
                    }
                }
                else {
                    PHAssetResourceCreationOptions *dngResourceOptions = [[PHAssetResourceCreationOptions alloc] init];
                    dngResourceOptions.shouldMoveFile = YES;
                    [creationRequest addResourceWithType:PHAssetResourceTypePhoto fileURL:temporaryDNGFileURL options:dngResourceOptions];
                }

            } completionHandler:^( BOOL success, NSError * _Nullable error ) {
                if ( ! success ) {
                    NSLog( @"Error occurred while saving photo to photo library: %@", error );
                }

                if ( [[NSFileManager defaultManager] fileExistsAtPath:temporaryDNGFileURL.path] ) {
                    [[NSFileManager defaultManager] removeItemAtURL:temporaryDNGFileURL error:nil];
                }

                [self didFinish];
            }];
        }
        else {
            NSLog( @"Not authorized to save photo" );
            [self didFinish];
        }
    }];
}

@end
```

[Next](AVCamManual-AVCamManualPreviewView.h.md)[Previous](AVCamManual-AVCamManualPreviewView.m.md)

