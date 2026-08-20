---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreSpotlight.html
archived_at: '2026-07-18T02:57:07.638867Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreSpotlight Changes for Swift

### CoreSpotlight

Modified [CSCustomAttributeKey](https://developer.apple.com/documentation/corespotlight/cscustomattributekey)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSCustomAttributeKey : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init?(keyName keyName: String)     init?(keyName keyName: String, searchable searchable: Bool, searchableByDefault searchableByDefault: Bool, unique unique: Bool, multiValued multiValued: Bool)     var keyName: String { get }     var searchable: Bool { get }     var searchableByDefault: Bool { get }     var unique: Bool { get }     var multiValued: Bool { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CSCustomAttributeKey : NSObject, NSCopying, NSSecureCoding {     convenience init?(keyName keyName: String)     init?(keyName keyName: String, searchable searchable: Bool, searchableByDefault searchableByDefault: Bool, unique unique: Bool, multiValued multiValued: Bool)     var keyName: String { get }     var searchable: Bool { get }     var searchableByDefault: Bool { get }     var unique: Bool { get }     var multiValued: Bool { get } } ``` | NSCopying, NSSecureCoding |

Modified [CSIndexErrorCode [enum]](https://developer.apple.com/documentation/corespotlight/csindexerror/code)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CSIndexExtensionRequestHandler](https://developer.apple.com/documentation/corespotlight/csindexextensionrequesthandler)

|  | Protocols |
| --- | --- |
| From | AnyObject, CSSearchableIndexDelegate, NSExtensionRequestHandling, NSObjectProtocol |
| To | CSSearchableIndexDelegate, NSExtensionRequestHandling |

Modified [CSLocalizedString](https://developer.apple.com/documentation/corespotlight/cslocalizedstring)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CSPerson](https://developer.apple.com/documentation/corespotlight/csperson)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSPerson : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(displayName displayName: String?, handles handles: [String], handleIdentifier handleIdentifier: String)     var displayName: String? { get }     var handles: [String] { get }     var handleIdentifier: String { get }     var contactIdentifier: String? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CSPerson : NSObject, NSSecureCoding, NSCopying {     init(displayName displayName: String?, handles handles: [String], handleIdentifier handleIdentifier: String)     var displayName: String? { get }     var handles: [String] { get }     var handleIdentifier: String { get }     var contactIdentifier: String? } ``` | NSCopying, NSSecureCoding |

Modified [CSSearchableIndex](https://developer.apple.com/documentation/corespotlight/cssearchableindex)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CSSearchableItem](https://developer.apple.com/documentation/corespotlight/cssearchableitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSSearchableItem : NSObject, NSSecureCoding, NSCoding, NSCopying {     init(uniqueIdentifier uniqueIdentifier: String?, domainIdentifier domainIdentifier: String?, attributeSet attributeSet: CSSearchableItemAttributeSet)     var uniqueIdentifier: String     var domainIdentifier: String?     @NSCopying var expirationDate: NSDate!     var attributeSet: CSSearchableItemAttributeSet } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CSSearchableItem : NSObject, NSSecureCoding, NSCopying {     init(uniqueIdentifier uniqueIdentifier: String?, domainIdentifier domainIdentifier: String?, attributeSet attributeSet: CSSearchableItemAttributeSet)     var uniqueIdentifier: String     var domainIdentifier: String?     @NSCopying var expirationDate: NSDate!     var attributeSet: CSSearchableItemAttributeSet } ``` | NSCopying, NSSecureCoding |

Modified [CSSearchableItemAttributeSet](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CSSearchableItemAttributeSet : NSObject, NSCopying, NSSecureCoding, NSCoding {     init(itemContentType itemContentType: String) } extension CSSearchableItemAttributeSet {     func setValue(_ value: NSSecureCoding?, forCustomKey key: CSCustomAttributeKey)     func valueForCustomKey(_ key: CSCustomAttributeKey) -> NSSecureCoding? } extension CSSearchableItemAttributeSet {     var subject: String?     var theme: String?     var contentDescription: String?     var identifier: String?     var audiences: [String]?     var fileSize: NSNumber?     var pageCount: NSNumber?     var pageWidth: NSNumber?     var pageHeight: NSNumber?     var securityMethod: String?     var creator: String?     var encodingApplications: [String]?     var kind: String?     var fontNames: [String]? } extension CSSearchableItemAttributeSet {     var dueDate: NSDate?     var completionDate: NSDate?     var startDate: NSDate?     var endDate: NSDate?     var importantDates: [NSDate]?     @NSCopying var allDay: NSNumber? } extension CSSearchableItemAttributeSet {     var displayName: String?     var alternateNames: [String]?     var path: String?     var contentURL: NSURL?     var thumbnailURL: NSURL?     @NSCopying var thumbnailData: NSData?     var relatedUniqueIdentifier: String?     var metadataModificationDate: NSDate?     var contentType: String?     var contentTypeTree: [String]?     var keywords: [String]?     var title: String? } extension CSSearchableItemAttributeSet {     @NSCopying var supportsPhoneCall: NSNumber?     @NSCopying var supportsNavigation: NSNumber? } extension CSSearchableItemAttributeSet {     var containerTitle: String?     var containerDisplayName: String?     var containerIdentifier: String?     @NSCopying var containerOrder: NSNumber? } extension CSSearchableItemAttributeSet {     var pixelHeight: NSNumber?     var pixelWidth: NSNumber?     var pixelCount: NSNumber?     var colorSpace: String?     var bitsPerSample: NSNumber?     var flashOn: NSNumber?     var focalLength: NSNumber?     var focalLength35mm: NSNumber?     var acquisitionMake: String?     var acquisitionModel: String?     var cameraOwner: String?     var lensModel: String?     var ISOSpeed: NSNumber?     var orientation: NSNumber?     var layerNames: [String]?     var whiteBalance: NSNumber?     var aperture: NSNumber?     var profileName: String?     var resolutionWidthDPI: NSNumber?     var resolutionHeightDPI: NSNumber?     var exposureMode: NSNumber?     var exposureTime: NSNumber?     var EXIFVersion: String?     var EXIFGPSVersion: String?     var hasAlphaChannel: NSNumber?     var redEyeOn: NSNumber?     var meteringMode: String?     var maxAperture: NSNumber?     var fNumber: NSNumber?     var exposureProgram: String?     var exposureTimeString: String? } extension CSSearchableItemAttributeSet {     var editors: [String]?     var participants: [String]?     var projects: [String]?     var downloadedDate: NSDate?     var contentSources: [String]?     var comment: String?     var copyright: String?     var lastUsedDate: NSDate?     var contentCreationDate: NSDate?     var contentModificationDate: NSDate?     var addedDate: NSDate?     var duration: NSNumber?     var contactKeywords: [String]?     var version: String?     var codecs: [String]?     var mediaTypes: [String]?     var streamable: NSNumber?     var totalBitRate: NSNumber?     var videoBitRate: NSNumber?     var audioBitRate: NSNumber?     var deliveryType: NSNumber?     var organizations: [String]?     var role: String?     var languages: [String]?     var rights: String?     var publishers: [String]?     var contributors: [String]?     var coverage: [String]?     var rating: NSNumber?     var ratingDescription: String?     var playCount: NSNumber?     var information: String?     var director: String?     var producer: String?     var genre: String?     var performers: [String]?     var originalFormat: String?     var originalSource: String?     var local: NSNumber?     var contentRating: NSNumber?     var URL: NSURL? } extension CSSearchableItemAttributeSet {     var audioSampleRate: NSNumber?     var audioChannelCount: NSNumber?     var tempo: NSNumber?     var keySignature: String?     var timeSignature: String?     var audioEncodingApplication: String?     var composer: String?     var lyricist: String?     var album: String?     var artist: String?     var audioTrackNumber: NSNumber?     var recordingDate: NSDate?     var musicalGenre: String?     var generalMIDISequence: NSNumber?     var musicalInstrumentCategory: String?     var musicalInstrumentName: String? } extension CSSearchableItemAttributeSet {     var accountIdentifier: String?     var accountHandles: [String]?     @NSCopying var HTMLContentData: NSData?     var textContent: String?     var authors: [CSPerson]?     var primaryRecipients: [CSPerson]?     var additionalRecipients: [CSPerson]?     var hiddenAdditionalRecipients: [CSPerson]?     var emailHeaders: [String : [AnyObject]]?     var mailboxIdentifiers: [String]?     var authorNames: [String]?     var recipientNames: [String]?     var authorEmailAddresses: [String]?     var recipientEmailAddresses: [String]?     var authorAddresses: [String]?     var recipientAddresses: [String]?     var phoneNumbers: [String]?     var emailAddresses: [String]?     var instantMessageAddresses: [String]?     var likelyJunk: NSNumber } extension CSSearchableItemAttributeSet {     var headline: String?     var instructions: String?     var city: String?     var stateOrProvince: String?     var country: String?     var altitude: NSNumber?     var latitude: NSNumber?     var longitude: NSNumber?     var speed: NSNumber?     var timestamp: NSDate?     var imageDirection: NSNumber?     var namedLocation: String?     var GPSTrack: NSNumber?     var GPSStatus: String?     var GPSMeasureMode: String?     var GPSDOP: NSNumber?     var GPSMapDatum: String?     var GPSDestLatitude: NSNumber?     var GPSDestLongitude: NSNumber?     var GPSDestBearing: NSNumber?     var GPSDestDistance: NSNumber?     var GPSProcessingMethod: String?     var GPSAreaInformation: String?     var GPSDateStamp: NSDate?     var GPSDifferental: NSNumber? } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CSSearchableItemAttributeSet : NSObject, NSCopying, NSSecureCoding {     init(itemContentType itemContentType: String) } extension CSSearchableItemAttributeSet {     func setValue(_ value: NSSecureCoding?, forCustomKey key: CSCustomAttributeKey)     func valueForCustomKey(_ key: CSCustomAttributeKey) -> NSSecureCoding? } extension CSSearchableItemAttributeSet {     var subject: String?     var theme: String?     var contentDescription: String?     var identifier: String?     var audiences: [String]?     var fileSize: NSNumber?     var pageCount: NSNumber?     var pageWidth: NSNumber?     var pageHeight: NSNumber?     var securityMethod: String?     var creator: String?     var encodingApplications: [String]?     var kind: String?     var fontNames: [String]? } extension CSSearchableItemAttributeSet {     var dueDate: NSDate?     var completionDate: NSDate?     var startDate: NSDate?     var endDate: NSDate?     var importantDates: [NSDate]?     @NSCopying var allDay: NSNumber? } extension CSSearchableItemAttributeSet {     var displayName: String?     var alternateNames: [String]?     var path: String?     var contentURL: NSURL?     var thumbnailURL: NSURL?     @NSCopying var thumbnailData: NSData?     var relatedUniqueIdentifier: String?     var metadataModificationDate: NSDate?     var contentType: String?     var contentTypeTree: [String]?     var keywords: [String]?     var title: String? } extension CSSearchableItemAttributeSet {     @NSCopying var supportsPhoneCall: NSNumber?     @NSCopying var supportsNavigation: NSNumber? } extension CSSearchableItemAttributeSet {     var containerTitle: String?     var containerDisplayName: String?     var containerIdentifier: String?     @NSCopying var containerOrder: NSNumber? } extension CSSearchableItemAttributeSet {     var pixelHeight: NSNumber?     var pixelWidth: NSNumber?     var pixelCount: NSNumber?     var colorSpace: String?     var bitsPerSample: NSNumber?     var flashOn: NSNumber?     var focalLength: NSNumber?     var focalLength35mm: NSNumber?     var acquisitionMake: String?     var acquisitionModel: String?     var cameraOwner: String?     var lensModel: String?     var ISOSpeed: NSNumber?     var orientation: NSNumber?     var layerNames: [String]?     var whiteBalance: NSNumber?     var aperture: NSNumber?     var profileName: String?     var resolutionWidthDPI: NSNumber?     var resolutionHeightDPI: NSNumber?     var exposureMode: NSNumber?     var exposureTime: NSNumber?     var EXIFVersion: String?     var EXIFGPSVersion: String?     var hasAlphaChannel: NSNumber?     var redEyeOn: NSNumber?     var meteringMode: String?     var maxAperture: NSNumber?     var fNumber: NSNumber?     var exposureProgram: String?     var exposureTimeString: String? } extension CSSearchableItemAttributeSet {     var editors: [String]?     var participants: [String]?     var projects: [String]?     var downloadedDate: NSDate?     var contentSources: [String]?     var comment: String?     var copyright: String?     var lastUsedDate: NSDate?     var contentCreationDate: NSDate?     var contentModificationDate: NSDate?     var addedDate: NSDate?     var duration: NSNumber?     var contactKeywords: [String]?     var version: String?     var codecs: [String]?     var mediaTypes: [String]?     var streamable: NSNumber?     var totalBitRate: NSNumber?     var videoBitRate: NSNumber?     var audioBitRate: NSNumber?     var deliveryType: NSNumber?     var organizations: [String]?     var role: String?     var languages: [String]?     var rights: String?     var publishers: [String]?     var contributors: [String]?     var coverage: [String]?     var rating: NSNumber?     var ratingDescription: String?     var playCount: NSNumber?     var information: String?     var director: String?     var producer: String?     var genre: String?     var performers: [String]?     var originalFormat: String?     var originalSource: String?     var local: NSNumber?     var contentRating: NSNumber?     var URL: NSURL? } extension CSSearchableItemAttributeSet {     var audioSampleRate: NSNumber?     var audioChannelCount: NSNumber?     var tempo: NSNumber?     var keySignature: String?     var timeSignature: String?     var audioEncodingApplication: String?     var composer: String?     var lyricist: String?     var album: String?     var artist: String?     var audioTrackNumber: NSNumber?     var recordingDate: NSDate?     var musicalGenre: String?     var generalMIDISequence: NSNumber?     var musicalInstrumentCategory: String?     var musicalInstrumentName: String? } extension CSSearchableItemAttributeSet {     var accountIdentifier: String?     var accountHandles: [String]?     @NSCopying var HTMLContentData: NSData?     var textContent: String?     var authors: [CSPerson]?     var primaryRecipients: [CSPerson]?     var additionalRecipients: [CSPerson]?     var hiddenAdditionalRecipients: [CSPerson]?     var emailHeaders: [String : [AnyObject]]?     var mailboxIdentifiers: [String]?     var authorNames: [String]?     var recipientNames: [String]?     var authorEmailAddresses: [String]?     var recipientEmailAddresses: [String]?     var authorAddresses: [String]?     var recipientAddresses: [String]?     var phoneNumbers: [String]?     var emailAddresses: [String]?     var instantMessageAddresses: [String]?     var likelyJunk: NSNumber } extension CSSearchableItemAttributeSet {     var headline: String?     var instructions: String?     var city: String?     var stateOrProvince: String?     var country: String?     var altitude: NSNumber?     var latitude: NSNumber?     var longitude: NSNumber?     var speed: NSNumber?     var timestamp: NSDate?     var imageDirection: NSNumber?     var namedLocation: String?     var GPSTrack: NSNumber?     var GPSStatus: String?     var GPSMeasureMode: String?     var GPSDOP: NSNumber?     var GPSMapDatum: String?     var GPSDestLatitude: NSNumber?     var GPSDestLongitude: NSNumber?     var GPSDestBearing: NSNumber?     var GPSDestDistance: NSNumber?     var GPSProcessingMethod: String?     var GPSAreaInformation: String?     var GPSDateStamp: NSDate?     var GPSDifferental: NSNumber? } ``` | NSCopying, NSSecureCoding |

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
