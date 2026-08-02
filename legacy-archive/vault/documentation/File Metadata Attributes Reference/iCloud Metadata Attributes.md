---
title: File Metadata Attributes Reference
apple_id: TP40001689
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/Articles/iCloudAttrs.html
archived_at: '2026-07-15T07:23:02.463759Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [File Metadata Attributes Reference](About%20the%20File%20Metadata%20Attributes%20Reference.md)


[Next](Document%20Revision%20History.md)[Previous](Spotlight%20Metadata%20Attributes.md)

# iCloud Metadata Attributes

These metadata attributes provide information on iCloud files. The attributes allow you to determine if a file is in the cloud, whether the file is uploading or downloading to or from iCloud, and the percentage of the action in progress.

General iCloud Attributes

These attributes provide general information on the status of iCloud files.

| NSMetadataItemIsUbiquitousKey | NSMetadataItemIsUbiquitousKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the item is stored in the cloud. | The value is an `NSNumber` object that contains a Boolean indicating whether the item is stored in the cloud. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

| NSMetadataUbiquitousItemHasUnresolvedConflictsKey | NSMetadataUbiquitousItemHasUnresolvedConflictsKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the item is currently in conflict with another version of the file somewhere else. | The value is an `NSNumber` object that contains a Boolean indicating whether the item is currently in conflict with another version of the file somewhere else. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

| NSMetadataUbiquitousItemIsDownloadedKey | NSMetadataUbiquitousItemIsDownloadedKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the current version of the item has been downloaded and is available locally. This attribute is deprecated. Use `[NSMetadataUbiquitousItemDownloadingStatusKey](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytenztfvjvomju)` instead. | The value is an `NSNumber` object that contains a Boolean indicating whether the current version of the item has been downloaded and is available locally. This attribute is deprecated. Use `[NSMetadataUbiquitousItemDownloadingStatusKey](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytenztfvjvomju)` instead. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 through OS X 10.9.Available in iOS 5.0 through iOS 7.0. |

| NSMetadataUbiquitousItemDownloadingStatusKey | NSMetadataUbiquitousItemDownloadingStatusKey |
| The value is a string constant that indicates the download status of the item. Possible values of the string are given in Downloading Status Values. | The value is a string constant that indicates the download status of the item. Possible values of the string are given in Downloading Status Values. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in iOS 7.0 and later. |

iCloud Downloading Attributes

The following attributes provide information on the download state of an iCloud file.

| NSMetadataUbiquitousItemIsDownloadingKey | NSMetadataUbiquitousItemIsDownloadingKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the item is currently being downloaded to the local device. | The value is an `NSNumber` object that contains a Boolean indicating whether the item is currently being downloaded to the local device. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

| NSMetadataUbiquitousItemPercentDownloadedKey | NSMetadataUbiquitousItemPercentDownloadedKey |
| The value is an `NSNumber` object that contains the percentage of the file that has already been downloaded from the cloud. | The value is an `NSNumber` object that contains the percentage of the file that has already been downloaded from the cloud. |
| __Value Type:__ | NSNumber |
| __Expected Values:__ | A double in the range 0.0 to 100.0. |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

iCloud Uploading Attributes

The following attributes provide information on the upload state of an iCloud file.

| NSMetadataUbiquitousItemIsUploadedKey | NSMetadataUbiquitousItemIsUploadedKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the item has been uploaded to the cloud. | The value is an `NSNumber` object that contains a Boolean indicating whether the item has been uploaded to the cloud. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

| NSMetadataUbiquitousItemIsUploadingKey | NSMetadataUbiquitousItemIsUploadingKey |
| The value is an `NSNumber` object that contains a Boolean indicating whether the current version of the item is currently being uploaded to the cloud. | The value is an `NSNumber` object that contains a Boolean indicating whether the current version of the item is currently being uploaded to the cloud. |
| __Value Type:__ | NSNumber |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

| NSMetadataUbiquitousItemPercentUploadedKey | NSMetadataUbiquitousItemPercentUploadedKey |
| The value is an `NSNumber` object that contains the percentage of the file that has already been uploaded to the cloud. | The value is an `NSNumber` object that contains the percentage of the file that has already been uploaded to the cloud. |
| __Value Type:__ | NSNumber |
| __Expected Values:__ | A double in the range 0.0 to 100.0. |
| __Framework:__ | /System/Library/Frameworks/Foundation.framework |
| __Header:__ | NSMetadata.h |
| __Availability:__ | Available in OS X v10.7 and later.Available in iOS 5.0 and later. |

[Next](Document%20Revision%20History.md)[Previous](Spotlight%20Metadata%20Attributes.md)

