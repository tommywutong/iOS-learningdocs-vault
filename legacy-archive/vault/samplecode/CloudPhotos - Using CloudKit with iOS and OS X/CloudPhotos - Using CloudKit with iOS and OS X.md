---
title: 'CloudPhotos : Using CloudKit with iOS and OS X'
apple_id: TP40016061
resource_type: Sample Code
platform: iOS|macOS
topic: null
technology: CloudKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/CloudPhotos/Introduction/Intro.html
archived_at: '2026-07-18T03:03:31.259032Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CloudPhotos%20%28iOS%29-CloudPhotos-main.m.md)

# CloudPhotos : Using CloudKit with iOS and OS X

|  |  |
| --- | --- |
| __Last Revision:__ | Version 3.1, 2017-03-09 Added OS X version. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3danrrfvjgk5tjonuw63sinfzxi33spewui33oorggs3tlivwgk3lfnz2esrc7ge) |
| __Build Requirements:__ | iOS 9.0 SDK or later, OS X 10.11 SDK or later |
| __Runtime Requirements:__ | iOS 9.0 or later, OS X 10.11 or later |

CloudPhotos is a clear and concise CloudKit sample showing how to share photos among other users. Photos are represented as CKRecords, holding the photo (CKAsset), its title (NSString), creation date (NSDate) and the location (CLLocation) it was created. The sample will display all photos found in the public CloudKit container. Users can view photo records, but only the owner of photo records can change or delete them. The attributes that can be edited are the photo itself and it’s title, the creation date and location data are read-only. Users add photo records from their photo library or camera role.

CloudPhotos covers a good range of CloudKit APIs in a clear, concise way. The sample offers code and strategies in handling real world situations when using CloudKit. One important feature is the proper handling of user log in and out, and turning on or off the network. The sample deals with these kinds of situations and updates its user interface accordingly. No network means no access to the Cloud, and no login means users can’t add or change photos, yet they can still view them as read only.

So it makes sense for developers who choose to start writing CloudKit code to use CloudPhotos as a guide.

[Next](CloudPhotos%20%28iOS%29-CloudPhotos-main.m.md)

