---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/CoreSpotlight.html
archived_at: '2026-07-18T02:54:54.996501Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# CoreSpotlight Changes for Objective-C

### CoreSpotlight

#### CSSearchableItem.h

Added [CSQueryContinuationActionType](https://developer.apple.com/documentation/corespotlight/csquerycontinuationactiontype)Added [CSSearchQueryString](https://developer.apple.com/documentation/corespotlight/cssearchquerystring)

#### CSSearchableItemAttributeSet_Events.h

Modified [CSSearchableItemAttributeSet.allDay](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616636-allday)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSNumber *allDay ``` |
| To | ``` @property(strong) NSNumber *allDay ``` |

#### CSSearchableItemAttributeSet_General.h

Added [CSSearchableItemAttributeSet.domainIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649285-domainidentifier)Added [CSSearchableItemAttributeSet.weakRelatedUniqueIdentifier](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649297-weakrelateduniqueidentifier)Modified [CSSearchableItemAttributeSet.containerOrder](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621586-containerorder)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSNumber *containerOrder ``` |
| To | ``` @property(strong) NSNumber *containerOrder ``` |

Modified [CSSearchableItemAttributeSet.supportsNavigation](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621564-supportsnavigation)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSNumber *supportsNavigation ``` |
| To | ``` @property(strong) NSNumber *supportsNavigation ``` |

Modified [CSSearchableItemAttributeSet.supportsPhoneCall](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1621653-supportsphonecall)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSNumber *supportsPhoneCall ``` |
| To | ``` @property(strong) NSNumber *supportsPhoneCall ``` |

Modified [CSSearchableItemAttributeSet.version](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616093-version)

|  | Header |
| --- | --- |
| From | CoreSpotlight/CSSearchableItemAttributeSet_Media.h |
| To | CoreSpotlight/CSSearchableItemAttributeSet_General.h |

#### CSSearchableItemAttributeSet_Media.h

Modified [CSSearchableItemAttributeSet.version](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1616093-version)

|  | Header |
| --- | --- |
| From | CoreSpotlight/CSSearchableItemAttributeSet_Media.h |
| To | CoreSpotlight/CSSearchableItemAttributeSet_General.h |

#### CSSearchableItemAttributeSet_Places.h

Added [CSSearchableItemAttributeSet.fullyFormattedAddress](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649301-fullyformattedaddress)Added [CSSearchableItemAttributeSet.postalCode](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649284-postalcode)Added [CSSearchableItemAttributeSet.subThoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649290-subthoroughfare)Added [CSSearchableItemAttributeSet.thoroughfare](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/1649310-thoroughfare)

#### CSSearchQuery.h (Added)

Added [CSSearchQuery](https://developer.apple.com/documentation/corespotlight/cssearchquery)Added [-[CSSearchQuery cancel]](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649309-cancel)Added [CSSearchQuery.cancelled](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649294-cancelled)Added [CSSearchQuery.completionHandler](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649312-completionhandler)Added [CSSearchQuery.foundItemCount](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649300-founditemcount)Added [CSSearchQuery.foundItemsHandler](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649306-founditemshandler)Added [-[CSSearchQuery initWithQueryString:attributes:]](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649308-initwithquerystring)Added [CSSearchQuery.protectionClasses](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649311-protectionclasses)Added [-[CSSearchQuery start]](https://developer.apple.com/documentation/corespotlight/cssearchquery/1649296-start)Added [CSSearchQueryErrorCode](https://developer.apple.com/documentation/corespotlight/cssearchqueryerrorcode)Added [CSSearchQueryErrorCodeCancelled](https://developer.apple.com/documentation/corespotlight/cssearchqueryerrorcode/cssearchqueryerrorcodecancelled)Added [CSSearchQueryErrorCodeIndexUnreachable](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/indexunreachable)Added [CSSearchQueryErrorCodeInvalidQuery](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/invalidquery)Added [CSSearchQueryErrorCodeUnknown](https://developer.apple.com/documentation/corespotlight/cssearchqueryerror/code/unknown)Added [CSSearchQueryErrorDomain](https://developer.apple.com/documentation/corespotlight/cssearchqueryerrordomain)

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
