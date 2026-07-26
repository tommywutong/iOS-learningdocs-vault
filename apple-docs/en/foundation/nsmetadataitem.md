---
title: NSMetadataItem
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataitem
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataitem.json'
content_hash: 'sha256:67a98b30d6ad1cd6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataItem

<sub>Class</sub>

The metadata associated with a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMetadataItem
```

## Overview

Metadata items provide a simple interface to retrieve the available attribute names and values.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Metadata Item

- [- initWithURL:](<nsmetadataitem/init(url_)-9xxs3.md>) — Initializes a metadata item with a given URL.

### Getting Item Attributes

- [attributes](nsmetadataitem/attributes.md) — An array containing the attribute keys for the metadata item’s values.
- [- valueForAttribute:](<nsmetadataitem/value(forattribute_).md>) — Returns the receiver’s metadata attribute name specified by a given key.
- [- valuesForAttributes:](<nsmetadataitem/values(forattributes_).md>) — Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.

### Item Attribute Keys

- [NSMetadataItemAudiencesKey](nsmetadataitemaudienceskey.md)
- [NSMetadataItemAudioBitRateKey](nsmetadataitemaudiobitratekey.md)
- [NSMetadataItemAudioChannelCountKey](nsmetadataitemaudiochannelcountkey.md)
- [NSMetadataItemAudioEncodingApplicationKey](nsmetadataitemaudioencodingapplicationkey.md)
- [NSMetadataItemAudioSampleRateKey](nsmetadataitemaudiosampleratekey.md)
- [NSMetadataItemAudioTrackNumberKey](nsmetadataitemaudiotracknumberkey.md)
- [NSMetadataItemAuthorAddressesKey](nsmetadataitemauthoraddresseskey.md)
- [NSMetadataItemAuthorEmailAddressesKey](nsmetadataitemauthoremailaddresseskey.md)
- [NSMetadataItemAuthorsKey](nsmetadataitemauthorskey.md)
- [NSMetadataItemAcquisitionMakeKey](nsmetadataitemacquisitionmakekey.md)
- [NSMetadataItemAcquisitionModelKey](nsmetadataitemacquisitionmodelkey.md)
- [NSMetadataItemAlbumKey](nsmetadataitemalbumkey.md)
- [NSMetadataItemAltitudeKey](nsmetadataitemaltitudekey.md)
- [NSMetadataItemApertureKey](nsmetadataitemaperturekey.md)
- [NSMetadataItemAppleLoopDescriptorsKey](nsmetadataitemappleloopdescriptorskey.md)
- [NSMetadataItemAppleLoopsKeyFilterTypeKey](nsmetadataitemappleloopskeyfiltertypekey.md)
- [NSMetadataItemAppleLoopsLoopModeKey](nsmetadataitemappleloopsloopmodekey.md)
- [NSMetadataItemAppleLoopsRootKeyKey](nsmetadataitemappleloopsrootkeykey.md)
- [NSMetadataItemApplicationCategoriesKey](nsmetadataitemapplicationcategorieskey.md)
- [NSMetadataItemAttributeChangeDateKey](nsmetadataitemattributechangedatekey.md)
- [NSMetadataItemFSNameKey](nsmetadataitemfsnamekey.md)
- [NSMetadataItemDisplayNameKey](nsmetadataitemdisplaynamekey.md)
- [NSMetadataItemURLKey](nsmetadataitemurlkey.md)
- [NSMetadataItemPathKey](nsmetadataitempathkey.md)
- [NSMetadataItemFSSizeKey](nsmetadataitemfssizekey.md)
- [NSMetadataItemFSCreationDateKey](nsmetadataitemfscreationdatekey.md)
- [NSMetadataItemFSContentChangeDateKey](nsmetadataitemfscontentchangedatekey.md)
- [NSMetadataItemBitsPerSampleKey](nsmetadataitembitspersamplekey.md)
- [NSMetadataItemCFBundleIdentifierKey](nsmetadataitemcfbundleidentifierkey.md)
- [NSMetadataItemCameraOwnerKey](nsmetadataitemcameraownerkey.md)
- [NSMetadataItemCityKey](nsmetadataitemcitykey.md)
- [NSMetadataItemCodecsKey](nsmetadataitemcodecskey.md)
- [NSMetadataItemColorSpaceKey](nsmetadataitemcolorspacekey.md)
- [NSMetadataItemCommentKey](nsmetadataitemcommentkey.md)
- [NSMetadataItemComposerKey](nsmetadataitemcomposerkey.md)
- [NSMetadataItemContactKeywordsKey](nsmetadataitemcontactkeywordskey.md)
- [NSMetadataItemContentCreationDateKey](nsmetadataitemcontentcreationdatekey.md)
- [NSMetadataItemContentModificationDateKey](nsmetadataitemcontentmodificationdatekey.md)
- [NSMetadataItemContentTypeKey](nsmetadataitemcontenttypekey.md) — The content type (UTI) of the metadata item.
- [NSMetadataItemContentTypeTreeKey](nsmetadataitemcontenttypetreekey.md) — The content type tree of the metadata item.
- [NSMetadataItemContributorsKey](nsmetadataitemcontributorskey.md)
- [NSMetadataItemCopyrightKey](nsmetadataitemcopyrightkey.md)
- [NSMetadataItemCountryKey](nsmetadataitemcountrykey.md)
- [NSMetadataItemCoverageKey](nsmetadataitemcoveragekey.md)
- [NSMetadataItemCreatorKey](nsmetadataitemcreatorkey.md)
- [NSMetadataItemDateAddedKey](nsmetadataitemdateaddedkey.md)
- [NSMetadataItemDeliveryTypeKey](nsmetadataitemdeliverytypekey.md)
- [NSMetadataItemDescriptionKey](nsmetadataitemdescriptionkey.md)
- [NSMetadataItemDirectorKey](nsmetadataitemdirectorkey.md)
- [NSMetadataItemDownloadedDateKey](nsmetadataitemdownloadeddatekey.md)
- [NSMetadataItemDueDateKey](nsmetadataitemduedatekey.md)
- [NSMetadataItemDurationSecondsKey](nsmetadataitemdurationsecondskey.md)
- [NSMetadataItemEXIFGPSVersionKey](nsmetadataitemexifgpsversionkey.md)
- [NSMetadataItemEXIFVersionKey](nsmetadataitemexifversionkey.md)
- [NSMetadataItemEditorsKey](nsmetadataitemeditorskey.md)
- [NSMetadataItemEmailAddressesKey](nsmetadataitememailaddresseskey.md)
- [NSMetadataItemEncodingApplicationsKey](nsmetadataitemencodingapplicationskey.md)
- [NSMetadataItemExecutableArchitecturesKey](nsmetadataitemexecutablearchitectureskey.md)
- [NSMetadataItemExecutablePlatformKey](nsmetadataitemexecutableplatformkey.md)
- [NSMetadataItemExposureModeKey](nsmetadataitemexposuremodekey.md)
- [NSMetadataItemExposureProgramKey](nsmetadataitemexposureprogramkey.md)
- [NSMetadataItemExposureTimeSecondsKey](nsmetadataitemexposuretimesecondskey.md)
- [NSMetadataItemExposureTimeStringKey](nsmetadataitemexposuretimestringkey.md)
- [NSMetadataItemFNumberKey](nsmetadataitemfnumberkey.md)
- [NSMetadataItemFinderCommentKey](nsmetadataitemfindercommentkey.md)
- [NSMetadataItemFlashOnOffKey](nsmetadataitemflashonoffkey.md)
- [NSMetadataItemFocalLength35mmKey](nsmetadataitemfocallength35mmkey.md)
- [NSMetadataItemFocalLengthKey](nsmetadataitemfocallengthkey.md)
- [NSMetadataItemFontsKey](nsmetadataitemfontskey.md)
- [NSMetadataItemGPSAreaInformationKey](nsmetadataitemgpsareainformationkey.md)
- [NSMetadataItemGPSDOPKey](nsmetadataitemgpsdopkey.md)
- [NSMetadataItemGPSDateStampKey](nsmetadataitemgpsdatestampkey.md)
- [NSMetadataItemGPSDestBearingKey](nsmetadataitemgpsdestbearingkey.md)
- [NSMetadataItemGPSDestDistanceKey](nsmetadataitemgpsdestdistancekey.md)
- [NSMetadataItemGPSDestLatitudeKey](nsmetadataitemgpsdestlatitudekey.md)
- [NSMetadataItemGPSDestLongitudeKey](nsmetadataitemgpsdestlongitudekey.md)
- [NSMetadataItemGPSDifferentalKey](nsmetadataitemgpsdifferentalkey.md)
- [NSMetadataItemGPSMapDatumKey](nsmetadataitemgpsmapdatumkey.md)
- [NSMetadataItemGPSMeasureModeKey](nsmetadataitemgpsmeasuremodekey.md)
- [NSMetadataItemGPSProcessingMethodKey](nsmetadataitemgpsprocessingmethodkey.md)
- [NSMetadataItemGPSStatusKey](nsmetadataitemgpsstatuskey.md)
- [NSMetadataItemGPSTrackKey](nsmetadataitemgpstrackkey.md)
- [NSMetadataItemGenreKey](nsmetadataitemgenrekey.md)
- [NSMetadataItemHasAlphaChannelKey](nsmetadataitemhasalphachannelkey.md)
- [NSMetadataItemHeadlineKey](nsmetadataitemheadlinekey.md)
- [NSMetadataItemISOSpeedKey](nsmetadataitemisospeedkey.md)
- [NSMetadataItemIdentifierKey](nsmetadataitemidentifierkey.md)
- [NSMetadataItemImageDirectionKey](nsmetadataitemimagedirectionkey.md)
- [NSMetadataItemInformationKey](nsmetadataiteminformationkey.md)
- [NSMetadataItemInstantMessageAddressesKey](nsmetadataiteminstantmessageaddresseskey.md)
- [NSMetadataItemInstructionsKey](nsmetadataiteminstructionskey.md)
- [NSMetadataItemIsApplicationManagedKey](nsmetadataitemisapplicationmanagedkey.md)
- [NSMetadataItemIsGeneralMIDISequenceKey](nsmetadataitemisgeneralmidisequencekey.md)
- [NSMetadataItemIsLikelyJunkKey](nsmetadataitemislikelyjunkkey.md)
- [NSMetadataItemKeySignatureKey](nsmetadataitemkeysignaturekey.md)
- [NSMetadataItemKeywordsKey](nsmetadataitemkeywordskey.md)
- [NSMetadataItemKindKey](nsmetadataitemkindkey.md)
- [NSMetadataItemLanguagesKey](nsmetadataitemlanguageskey.md)
- [NSMetadataItemLastUsedDateKey](nsmetadataitemlastuseddatekey.md)
- [NSMetadataItemLatitudeKey](nsmetadataitemlatitudekey.md)
- [NSMetadataItemLayerNamesKey](nsmetadataitemlayernameskey.md)
- [NSMetadataItemLensModelKey](nsmetadataitemlensmodelkey.md)
- [NSMetadataItemLongitudeKey](nsmetadataitemlongitudekey.md)
- [NSMetadataItemLyricistKey](nsmetadataitemlyricistkey.md)
- [NSMetadataItemMaxApertureKey](nsmetadataitemmaxaperturekey.md)
- [NSMetadataItemMediaTypesKey](nsmetadataitemmediatypeskey.md)
- [NSMetadataItemMeteringModeKey](nsmetadataitemmeteringmodekey.md)
- [NSMetadataItemMusicalGenreKey](nsmetadataitemmusicalgenrekey.md)
- [NSMetadataItemMusicalInstrumentCategoryKey](nsmetadataitemmusicalinstrumentcategorykey.md)
- [NSMetadataItemMusicalInstrumentNameKey](nsmetadataitemmusicalinstrumentnamekey.md)
- [NSMetadataItemNamedLocationKey](nsmetadataitemnamedlocationkey.md)
- [NSMetadataItemNumberOfPagesKey](nsmetadataitemnumberofpageskey.md)
- [NSMetadataItemOrganizationsKey](nsmetadataitemorganizationskey.md)
- [NSMetadataItemOrientationKey](nsmetadataitemorientationkey.md)
- [NSMetadataItemOriginalFormatKey](nsmetadataitemoriginalformatkey.md)
- [NSMetadataItemOriginalSourceKey](nsmetadataitemoriginalsourcekey.md)
- [NSMetadataItemPageHeightKey](nsmetadataitempageheightkey.md)
- [NSMetadataItemPageWidthKey](nsmetadataitempagewidthkey.md)
- [NSMetadataItemParticipantsKey](nsmetadataitemparticipantskey.md)
- [NSMetadataItemPerformersKey](nsmetadataitemperformerskey.md)
- [NSMetadataItemPhoneNumbersKey](nsmetadataitemphonenumberskey.md)
- [NSMetadataItemPixelCountKey](nsmetadataitempixelcountkey.md)
- [NSMetadataItemPixelHeightKey](nsmetadataitempixelheightkey.md)
- [NSMetadataItemPixelWidthKey](nsmetadataitempixelwidthkey.md)
- [NSMetadataItemProducerKey](nsmetadataitemproducerkey.md)
- [NSMetadataItemProfileNameKey](nsmetadataitemprofilenamekey.md)
- [NSMetadataItemProjectsKey](nsmetadataitemprojectskey.md)
- [NSMetadataItemPublishersKey](nsmetadataitempublisherskey.md)
- [NSMetadataItemRecipientAddressesKey](nsmetadataitemrecipientaddresseskey.md)
- [NSMetadataItemRecipientEmailAddressesKey](nsmetadataitemrecipientemailaddresseskey.md)
- [NSMetadataItemRecipientsKey](nsmetadataitemrecipientskey.md)
- [NSMetadataItemRecordingDateKey](nsmetadataitemrecordingdatekey.md)
- [NSMetadataItemRecordingYearKey](nsmetadataitemrecordingyearkey.md)
- [NSMetadataItemRedEyeOnOffKey](nsmetadataitemredeyeonoffkey.md)
- [NSMetadataItemResolutionHeightDPIKey](nsmetadataitemresolutionheightdpikey.md)
- [NSMetadataItemResolutionWidthDPIKey](nsmetadataitemresolutionwidthdpikey.md)
- [NSMetadataItemRightsKey](nsmetadataitemrightskey.md)
- [NSMetadataItemSecurityMethodKey](nsmetadataitemsecuritymethodkey.md)
- [NSMetadataItemSpeedKey](nsmetadataitemspeedkey.md)
- [NSMetadataItemStarRatingKey](nsmetadataitemstarratingkey.md)
- [NSMetadataItemStateOrProvinceKey](nsmetadataitemstateorprovincekey.md)
- [NSMetadataItemStreamableKey](nsmetadataitemstreamablekey.md)
- [NSMetadataItemSubjectKey](nsmetadataitemsubjectkey.md)
- [NSMetadataItemTempoKey](nsmetadataitemtempokey.md)
- [NSMetadataItemTextContentKey](nsmetadataitemtextcontentkey.md)
- [NSMetadataItemThemeKey](nsmetadataitemthemekey.md)
- [NSMetadataItemTimeSignatureKey](nsmetadataitemtimesignaturekey.md)
- [NSMetadataItemTimestampKey](nsmetadataitemtimestampkey.md)
- [NSMetadataItemTitleKey](nsmetadataitemtitlekey.md)
- [NSMetadataItemTotalBitRateKey](nsmetadataitemtotalbitratekey.md)
- [NSMetadataItemVersionKey](nsmetadataitemversionkey.md)
- [NSMetadataItemVideoBitRateKey](nsmetadataitemvideobitratekey.md)
- [NSMetadataItemWhereFromsKey](nsmetadataitemwherefromskey.md)
- [NSMetadataItemWhiteBalanceKey](nsmetadataitemwhitebalancekey.md)

### iCloud Keys

- [NSMetadataItemIsUbiquitousKey](nsmetadataitemisubiquitouskey.md)
- [NSMetadataUbiquitousItemContainerDisplayNameKey](nsmetadataubiquitousitemcontainerdisplaynamekey.md) — The display name of the container that stores the ubiquitous item.
- [NSMetadataUbiquitousItemDownloadRequestedKey](nsmetadataubiquitousitemdownloadrequestedkey.md) — A Boolean value indicating whether a download has been requested for the ubiquitous item.
- [NSMetadataUbiquitousItemIsExternalDocumentKey](nsmetadataubiquitousitemisexternaldocumentkey.md) — A Boolean value indicating whether the ubiquitous item is from an external document.
- [NSMetadataUbiquitousItemURLInLocalContainerKey](nsmetadataubiquitousitemurlinlocalcontainerkey.md) — The URL for the ubiquitous item in the local container.
- [NSMetadataUbiquitousItemHasUnresolvedConflictsKey](nsmetadataubiquitousitemhasunresolvedconflictskey.md)
- [NSMetadataUbiquitousItemIsDownloadedKey](nsmetadataubiquitousitemisdownloadedkey.md) _(deprecated)_
- [NSMetadataUbiquitousItemIsDownloadingKey](nsmetadataubiquitousitemisdownloadingkey.md)
- [NSMetadataUbiquitousItemIsUploadedKey](nsmetadataubiquitousitemisuploadedkey.md)
- [NSMetadataUbiquitousItemIsUploadingKey](nsmetadataubiquitousitemisuploadingkey.md)
- [NSMetadataUbiquitousItemPercentDownloadedKey](nsmetadataubiquitousitempercentdownloadedkey.md)
- [NSMetadataUbiquitousItemPercentUploadedKey](nsmetadataubiquitousitempercentuploadedkey.md)
- [NSMetadataUbiquitousItemDownloadingStatusKey](nsmetadataubiquitousitemdownloadingstatuskey.md)
- [NSMetadataUbiquitousItemDownloadingErrorKey](nsmetadataubiquitousitemdownloadingerrorkey.md)
- [NSMetadataUbiquitousItemUploadingErrorKey](nsmetadataubiquitousitemuploadingerrorkey.md)
- [NSMetadataUbiquitousItemIsSharedKey](nsmetadataubiquitousitemissharedkey.md) — A Boolean value indicating whether the ubiquitous item is shared.
- [NSMetadataUbiquitousSharedItemCurrentUserPermissionsKey](nsmetadataubiquitousshareditemcurrentuserpermissionskey.md) — The permissions for the current user, or `nil` if not shared.
- [NSMetadataUbiquitousSharedItemCurrentUserRoleKey](nsmetadataubiquitousshareditemcurrentuserrolekey.md) — The current user’s role for the shared item, or `nil` if not shared.
- [NSMetadataUbiquitousSharedItemMostRecentEditorNameComponentsKey](nsmetadataubiquitousshareditemmostrecenteditornamecomponentskey.md) — The name components of the most recent editor of the shared document, or `nil` if it is the current user.
- [NSMetadataUbiquitousSharedItemOwnerNameComponentsKey](nsmetadataubiquitousshareditemownernamecomponentskey.md) — The name components of the shared item’s owner, or `nil` if the current user is the owner.

### iCloud Download Status Values

- [NSMetadataUbiquitousItemDownloadingStatusCurrent](nsmetadataubiquitousitemdownloadingstatuscurrent.md)
- [NSMetadataUbiquitousItemDownloadingStatusDownloaded](nsmetadataubiquitousitemdownloadingstatusdownloaded.md)
- [NSMetadataUbiquitousItemDownloadingStatusNotDownloaded](nsmetadataubiquitousitemdownloadingstatusnotdownloaded.md)

### iCloud Sharing Permissions Values

- [NSMetadataUbiquitousSharedItemPermissionsReadOnly](nsmetadataubiquitousshareditempermissionsreadonly.md) — The current user is only allowed to read this item.
- [NSMetadataUbiquitousSharedItemPermissionsReadWrite](nsmetadataubiquitousshareditempermissionsreadwrite.md) — The current user is allowed to both read and write this item.

### iCloud Sharing Role Values

- [NSMetadataUbiquitousSharedItemRoleOwner](nsmetadataubiquitousshareditemroleowner.md) — The current user is the owner of the shared item.
- [NSMetadataUbiquitousSharedItemRoleParticipant](nsmetadataubiquitousshareditemroleparticipant.md) — The current user is a participant of the shared item.

### Initializers

- [init(URL:)](<nsmetadataitem/init(url_)-viww.md>)

## See Also

### File Search

- [NSMetadataQuery](nsmetadataquery.md) — A query that you perform against Spotlight metadata.
- [NSMetadataQueryDelegate](nsmetadataquerydelegate.md) — An interface that enables the delegate of a metadata query to provide substitute results or attributes.
