---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Listings/CloudPhotos__iOS__CloudPhotos_CloudPhoto_m.html
archived_at: '2026-07-18T03:03:33.509285Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudPhotos : Using CloudKit with iOS and OS X](CloudPhotos%20-%20Using%20CloudKit%20with%20iOS%20and%20OS%20X.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.h.md)[Previous](LICENSE.txt.md)

# CloudPhotos (iOS)/CloudPhotos/CloudPhoto.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Object to describe a photo in this app: a wrapper for CKRecord
 */

#import "CloudPhoto.h"
#import "APLCloudManager.h"
#import "AppDelegate.h"

@implementation CloudPhoto

- (id)initWithRecord:(CKRecord *)record
{
    self = [super init];
    if (self != nil)
    {
        _cloudRecord = record;
        _isMyPhoto = [CloudManager isMyRecord:self.cloudRecord.creatorUserRecordID];
        _distanceFromUser = -1;
    }
    return self;
}

- (BOOL)isPhotoNearMe
{
    return self.distanceFromUser < kNearMeDistance && self.distanceFromUser != -1;
}

- (BOOL)isRecentPhoto
{
    NSCalendar *calendar = [NSCalendar currentCalendar];

    NSDate *date1 = [NSDate date];
    NSDate *date2 = [calendar startOfDayForDate:self.photoDate];

    NSDateComponents *components = [calendar components:NSCalendarUnitDay fromDate:date2 toDate:date1 options:0];

    return components.day <= 5; // recent within last 5 days}
}


// TITLE
- (NSString *)getPhotoTitle
{
    return self.cloudRecord[[APLCloudManager PhotoTitleAttribute]];
}
- (void)setPhotoTitle:(NSString *)title
{
    self.cloudRecord[[APLCloudManager PhotoTitleAttribute]] = title;
}

// DATE
- (NSString *)getPhotoDate
{
    return self.cloudRecord[[APLCloudManager PhotoDateAttribute]];
}
- (void)setPhotoDate:(NSDate *)date
{
    self.cloudRecord[[APLCloudManager PhotoDateAttribute]] = date;
}

// LOCATION
- (CLLocation *)getPhotoLocation
{
    return self.cloudRecord[[APLCloudManager PhotoLocationAttribute]];
}
- (void)setPhotoLocation:(CLLocation *)location
{
    self.cloudRecord[[APLCloudManager PhotoLocationAttribute]] = location;
}

// IMAGE
- (UIImage *)getPhotoImage
{
    CKAsset *photoAsset = self.cloudRecord[[APLCloudManager PhotoAssetAttribute]];
    UIImage *imageData = [UIImage imageWithContentsOfFile: photoAsset.fileURL.path];
    return imageData;
}

- (void)setPhotoImage:(NSURL *)imageURL
{
    CKAsset *asset = [[CKAsset alloc] initWithFileURL:imageURL];
    self.cloudRecord[[APLCloudManager PhotoAssetAttribute]] = asset;
}

// OWNER
// asynchronously fetches the owner of a given photo, and uses the completion handler to return it back
- (void)photoOwner:(void (^)(NSString *owner))completionHandler
{
    [UIApplication sharedApplication].networkActivityIndicatorVisible = YES;

    [CloudManager fetchUserNameFromRecordID:self.cloudRecord.creatorUserRecordID completionHandler:^(NSString *familyName) {

        [UIApplication sharedApplication].networkActivityIndicatorVisible = NO;

        completionHandler(familyName);
    }];
}

@end
```

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-CloudPhoto.h.md)[Previous](LICENSE.txt.md)

