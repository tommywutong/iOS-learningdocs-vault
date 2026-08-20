---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_CloudPhoto_h.html
archived_at: '2026-07-18T03:03:33.473606Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-PhotoTableCell.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.m.md)

# CloudPhotos (iOS)/CloudPhotos/CloudPhoto.h

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Object to describe a photo in this app: a wrapper for CKRecord
 */

@import UIKit;
@import CloudKit;

@interface CloudPhoto : NSObject

@property (nonatomic, strong) CKRecord *cloudRecord;

@property (nonatomic, strong, getter = getPhotoTitle, setter = setPhotoTitle:) NSString *photoTitle;
@property (nonatomic, strong, getter = getPhotoDate, setter = setPhotoDate:) NSDate *photoDate;
@property (nonatomic, strong, getter = getPhotoLocation, setter = setPhotoLocation:) CLLocation *photoLocation;

@property (assign) BOOL isMyPhoto;
@property (assign) double distanceFromUser;   // in kilometers

- (id)initWithRecord:(CKRecord *)record;

- (BOOL)isPhotoNearMe;
- (BOOL)isRecentPhoto;

- (UIImage *)getPhotoImage;
- (void)setPhotoImage:(NSURL *)imageURL;

- (void)photoOwner:(void (^)(NSString *owner))completionHandler;

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-PhotoTableCell.h.md)[Previous](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.m.md)

