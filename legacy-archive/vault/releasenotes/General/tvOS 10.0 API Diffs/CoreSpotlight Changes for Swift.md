---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/CoreSpotlight.html
archived_at: '2026-07-18T02:57:39.733387Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreSpotlight Changes for Swift

### CoreSpotlight

Added [CSSearchableItemAttributeSet.fullyFormattedAddress](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649301-fullyformattedaddress)Added [CSSearchableItemAttributeSet.postalCode](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649284-postalcode)Added [CSSearchableItemAttributeSet.subThoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649290-subthoroughfare)Added [CSSearchableItemAttributeSet.thoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649310-thoroughfare)Modified [CSSearchableIndex.beginBatch()](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620331-beginindexbatch)

|  | Declaration |
| --- | --- |
| From | ``` func beginIndexBatch() ``` |
| To | ``` func beginBatch() ``` |

Modified [CSSearchableIndex.endBatch(withClientState: Data, completionHandler: ( (Error?) -> Swift.Void)?)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620344-endindexbatchwithclientstate)

|  | Declaration |
| --- | --- |
| From | ``` func endIndexBatchWithClientState(_ clientState: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |
| To | ``` func endBatch(withClientState clientState: Data, completionHandler completionHandler: (@escaping (Error?) -> Swift.Void)? = nil) ``` |

Modified [CSSearchableIndex.fetchLastClientState(completionHandler: (Data?, Error?) -> Swift.Void)](https://developer.apple.com/documentation/corespotlight/cssearchableindex/1620346-fetchlastclientstate)

|  | Declaration |
| --- | --- |
| From | ``` func fetchLastClientStateWithCompletionHandler(_ completionHandler: (NSData?, NSError?) -> Void) ``` |
| To | ``` func fetchLastClientState(completionHandler completionHandler: @escaping (Data?, Error?) -> Swift.Void) ``` |

Modified [CSSearchableItemAttributeSet.addedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616029-addeddate)

|  | Declaration |
| --- | --- |
| From | ``` var addedDate: NSDate? ``` |
| To | ``` var addedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.allDay](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616636-allday)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var allDay: NSNumber? ``` |
| To | ``` var allDay: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.completionDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616637-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate? ``` |
| To | ``` var completionDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.containerOrder](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621586-containerorder)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var containerOrder: NSNumber? ``` |
| To | ``` var containerOrder: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.contentCreationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616001-contentcreationdate)

|  | Declaration |
| --- | --- |
| From | ``` var contentCreationDate: NSDate? ``` |
| To | ``` var contentCreationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.contentModificationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616085-contentmodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var contentModificationDate: NSDate? ``` |
| To | ``` var contentModificationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.contentURL](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621651-contenturl)

|  | Declaration |
| --- | --- |
| From | ``` var contentURL: NSURL? ``` |
| To | ``` var contentURL: URL? ``` |

Modified [CSSearchableItemAttributeSet.downloadedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616035-downloadeddate)

|  | Declaration |
| --- | --- |
| From | ``` var downloadedDate: NSDate? ``` |
| To | ``` var downloadedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.dueDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616641-duedate)

|  | Declaration |
| --- | --- |
| From | ``` var dueDate: NSDate? ``` |
| To | ``` var dueDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.emailHeaders](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621568-emailheaders)

|  | Declaration |
| --- | --- |
| From | ``` var emailHeaders: [String : [AnyObject]]? ``` |
| To | ``` var emailHeaders: [String : [Any]]? ``` |

Modified [CSSearchableItemAttributeSet.endDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616638-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate? ``` |
| To | ``` var endDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.exifgpsVersion](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621543-exifgpsversion)

|  | Declaration |
| --- | --- |
| From | ``` var EXIFGPSVersion: String? ``` |
| To | ``` var exifgpsVersion: String? ``` |

Modified [CSSearchableItemAttributeSet.exifVersion](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621550-exifversion)

|  | Declaration |
| --- | --- |
| From | ``` var EXIFVersion: String? ``` |
| To | ``` var exifVersion: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsAreaInformation](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620581-gpsareainformation)

|  | Declaration |
| --- | --- |
| From | ``` var GPSAreaInformation: String? ``` |
| To | ``` var gpsAreaInformation: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsDateStamp](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620587-gpsdatestamp)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDateStamp: NSDate? ``` |
| To | ``` var gpsDateStamp: Date? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestBearing](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620577-gpsdestbearing)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestBearing: NSNumber? ``` |
| To | ``` var gpsDestBearing: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestDistance](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620582-gpsdestdistance)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestDistance: NSNumber? ``` |
| To | ``` var gpsDestDistance: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestLatitude](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620572-gpsdestlatitude)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestLatitude: NSNumber? ``` |
| To | ``` var gpsDestLatitude: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDestLongitude](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620580-gpsdestlongitude)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDestLongitude: NSNumber? ``` |
| To | ``` var gpsDestLongitude: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsDifferental](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620592-gpsdifferental)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDifferental: NSNumber? ``` |
| To | ``` var gpsDifferental: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsdop](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620593-gpsdop)

|  | Declaration |
| --- | --- |
| From | ``` var GPSDOP: NSNumber? ``` |
| To | ``` var gpsdop: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.gpsMapDatum](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620583-gpsmapdatum)

|  | Declaration |
| --- | --- |
| From | ``` var GPSMapDatum: String? ``` |
| To | ``` var gpsMapDatum: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsMeasureMode](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620573-gpsmeasuremode)

|  | Declaration |
| --- | --- |
| From | ``` var GPSMeasureMode: String? ``` |
| To | ``` var gpsMeasureMode: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsProcessingMethod](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620575-gpsprocessingmethod)

|  | Declaration |
| --- | --- |
| From | ``` var GPSProcessingMethod: String? ``` |
| To | ``` var gpsProcessingMethod: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsStatus](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620589-gpsstatus)

|  | Declaration |
| --- | --- |
| From | ``` var GPSStatus: String? ``` |
| To | ``` var gpsStatus: String? ``` |

Modified [CSSearchableItemAttributeSet.gpsTrack](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620588-gpstrack)

|  | Declaration |
| --- | --- |
| From | ``` var GPSTrack: NSNumber? ``` |
| To | ``` var gpsTrack: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.htmlContentData](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621669-htmlcontentdata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var HTMLContentData: NSData? ``` |
| To | ``` var htmlContentData: Data? ``` |

Modified [CSSearchableItemAttributeSet.importantDates](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616639-importantdates)

|  | Declaration |
| --- | --- |
| From | ``` var importantDates: [NSDate]? ``` |
| To | ``` var importantDates: [Date]? ``` |

Modified [CSSearchableItemAttributeSet.isoSpeed](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621548-isospeed)

|  | Declaration |
| --- | --- |
| From | ``` var ISOSpeed: NSNumber? ``` |
| To | ``` var isoSpeed: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.lastUsedDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616018-lastuseddate)

|  | Declaration |
| --- | --- |
| From | ``` var lastUsedDate: NSDate? ``` |
| To | ``` var lastUsedDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.metadataModificationDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621657-metadatamodificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var metadataModificationDate: NSDate? ``` |
| To | ``` var metadataModificationDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.recordingDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616051-recordingdate)

|  | Declaration |
| --- | --- |
| From | ``` var recordingDate: NSDate? ``` |
| To | ``` var recordingDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.startDate](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616640-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate? ``` |
| To | ``` var startDate: Date? ``` |

Modified [CSSearchableItemAttributeSet.supportsNavigation](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621564-supportsnavigation)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var supportsNavigation: NSNumber? ``` |
| To | ``` var supportsNavigation: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.supportsPhoneCall](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621653-supportsphonecall)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var supportsPhoneCall: NSNumber? ``` |
| To | ``` var supportsPhoneCall: NSNumber? ``` |

Modified [CSSearchableItemAttributeSet.thumbnailData](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621582-thumbnaildata)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var thumbnailData: NSData? ``` |
| To | ``` var thumbnailData: Data? ``` |

Modified [CSSearchableItemAttributeSet.thumbnailURL](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621560-thumbnailurl)

|  | Declaration |
| --- | --- |
| From | ``` var thumbnailURL: NSURL? ``` |
| To | ``` var thumbnailURL: URL? ``` |

Modified [CSSearchableItemAttributeSet.timestamp](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1620574-timestamp)

|  | Declaration |
| --- | --- |
| From | ``` var timestamp: NSDate? ``` |
| To | ``` var timestamp: Date? ``` |

Modified [CSSearchableItemAttributeSet.url](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616087-url)

|  | Declaration |
| --- | --- |
| From | ``` var URL: NSURL? ``` |
| To | ``` var url: URL? ``` |

Modified [CSSearchableItemAttributeSet.value(forCustomKey: CSCustomAttributeKey) -> NSSecureCoding?](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616407-value)

|  | Declaration |
| --- | --- |
| From | ``` func valueForCustomKey(_ key: CSCustomAttributeKey) -> NSSecureCoding? ``` |
| To | ``` func value(forCustomKey key: CSCustomAttributeKey) -> NSSecureCoding? ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
