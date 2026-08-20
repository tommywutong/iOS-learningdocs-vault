---
title: iOS 6.1 API Diffs
apple_id: TP40012875
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS61APIDiffs/index.html
archived_at: '2026-07-18T02:55:50.295875Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)


# iOS 6.0 to iOS 6.1 API Differences

## Accelerate

No changes

## Accounts

No changes

## AddressBook

No changes

## AddressBookUI

No changes

## AdSupport

No changes

## AssetsLibrary

No changes

## AudioToolbox

No changes

## AudioUnit

No changes

## AVFoundation

No changes

## CFNetwork

No changes

## CoreAudio

No changes

## CoreBluetooth

No changes

## CoreData

No changes

## CoreFoundation

No changes

## CoreGraphics

No changes

## CoreImage

No changes

## CoreLocation

No changes

## CoreMedia

No changes

## CoreMIDI

No changes

## CoreMotion

No changes

## CoreTelephony

No changes

## CoreText

No changes

## CoreVideo

No changes

## EventKit

No changes

## EventKitUI

No changes

## ExternalAccessory

No changes

## Foundation

No changes

## GameKit

No changes

## GLKit

No changes

## GSS

No changes

## iAd

No changes

## ImageIO

No changes

## IOKit

No changes

## MapKit

MKLocalSearch.hAdded [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch)Added [-[MKLocalSearch cancel]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452160-cancel)Added [-[MKLocalSearch initWithRequest:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452759-init)Added [MKLocalSearch.searching](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452349-issearching)Added [-[MKLocalSearch startWithCompletionHandler:]](https://developer.apple.com/documentation/mapkit/mklocalsearch/1452652-startwithcompletionhandler)Added [MKLocalSearchCompletionHandler](https://developer.apple.com/documentation/mapkit/mklocalsearch/completionhandler)MKLocalSearchRequest.hAdded [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request)Added [MKLocalSearchRequest.naturalLanguageQuery](https://developer.apple.com/documentation/mapkit/mklocalsearchrequest/1452353-naturallanguagequery)Added [MKLocalSearchRequest.region](https://developer.apple.com/documentation/mapkit/mklocalsearchrequest/1451919-region)MKLocalSearchResponse.hAdded [MKLocalSearchResponse](https://developer.apple.com/documentation/mapkit/mklocalsearch/response)Added [MKLocalSearchResponse.boundingRegion](https://developer.apple.com/documentation/mapkit/mklocalsearch/response/1452501-boundingregion)Added [MKLocalSearchResponse.mapItems](https://developer.apple.com/documentation/mapkit/mklocalsearchresponse/1451939-mapitems)

## MediaPlayer

No changes

## MediaToolbox

No changes

## MessageUI

No changes

## MobileCoreServices

No changes

## NewsstandKit

No changes

## OpenAL

No changes

## OpenGLES

No changes

## PassKit

No changes

## QuartzCore

No changes

## QuickLook

No changes

## Security

No changes

## Social

No changes

## StoreKit

No changes

## SystemConfiguration

No changes

## Twitter

No changes

## UIKit

UICollectionViewLayout.hModified [+[UICollectionViewLayoutAttributes layoutAttributesForSupplementaryViewOfKind:withIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617801-init)

|  | Declaration |
| --- | --- |
| From | + (id)layoutAttributesForSupplementaryViewOfKind:(NSString \*)elementKind withIndexPath:(NSIndexPath \*)indexPath |
| To | + (instancetype)layoutAttributesForSupplementaryViewOfKind:(NSString \*)elementKind withIndexPath:(NSIndexPath \*)indexPath |

Modified [+[UICollectionViewLayoutAttributes layoutAttributesForDecorationViewOfKind:withIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617786-layoutattributesfordecorationvie)

|  | Declaration |
| --- | --- |
| From | + (id)layoutAttributesForDecorationViewOfKind:(NSString \*)decorationViewKind withIndexPath:(NSIndexPath \*)indexPath |
| To | + (instancetype)layoutAttributesForDecorationViewOfKind:(NSString \*)decorationViewKind withIndexPath:(NSIndexPath \*)indexPath |

Modified [+[UICollectionViewLayoutAttributes layoutAttributesForCellWithIndexPath:]](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/1617759-layoutattributesforcellwithindex)

|  | Declaration |
| --- | --- |
| From | + (id)layoutAttributesForCellWithIndexPath:(NSIndexPath \*)indexPath |
| To | + (instancetype)layoutAttributesForCellWithIndexPath:(NSIndexPath \*)indexPath |

UIKitDefines.hRemoved #def instancetypeUINavigationController.hModified [-[UINavigationController initWithNavigationBarClass:toolbarClass:]](https://developer.apple.com/documentation/uikit/uinavigationcontroller/1621866-initwithnavigationbarclass)

|  | Declaration |
| --- | --- |
| From | - (id)initWithNavigationBarClass:(Class)navigationBarClass toolbarClass:(Class)toolbarClass |
| To | - (instancetype)initWithNavigationBarClass:(Class)navigationBarClass toolbarClass:(Class)toolbarClass |

## VideoToolbox

No changes

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
