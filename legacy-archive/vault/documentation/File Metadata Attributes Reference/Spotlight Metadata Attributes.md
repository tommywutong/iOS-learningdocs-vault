---
title: File Metadata Attributes Reference
apple_id: TP40001689
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreServices
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/CoreServices/Reference/MetadataAttributesRef/Reference/CommonAttrs.html
archived_at: '2026-07-15T07:23:03.728936Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [File Metadata Attributes Reference](About%20the%20File%20Metadata%20Attributes%20Reference.md)


[Next](iCloud%20Metadata%20Attributes.md)[Previous](About%20the%20File%20Metadata%20Attributes%20Reference.md)

# Spotlight Metadata Attributes

Common Spotlight Metadata Attribute Keys

Spotlight Metadata attribute keys that are common to many file types.

| kMDItemAttributeChangeDate | kMDItemAttributeChangeDate |
| Date and time of the last change made to a metadata attribute. | Date and time of the last change made to a metadata attribute. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAudiences | kMDItemAudiences |
| The audience for which the file is intended. The audience may be determined by the creator or the publisher or by a third party. | The audience for which the file is intended. The audience may be determined by the creator or the publisher or by a third party. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAuthors | kMDItemAuthors |
| The author, or authors, of the contents of the file. The order of the authors is preserved, but does not represent the main author or relative importance of the authors. | The author, or authors, of the contents of the file. The order of the authors is preserved, but does not represent the main author or relative importance of the authors. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAuthorAddresses | kMDItemAuthorAddresses |
| This attribute indicates the author addresses of the document. | This attribute indicates the author addresses of the document. |
| __Value Type:__ | Array of CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.6 and later. |

| kMDItemCity | kMDItemCity |
| Identifies city of origin according to guidelines established by the provider. For example, "New York", "Cupertino", or "Toronto". | Identifies city of origin according to guidelines established by the provider. For example, "New York", "Cupertino", or "Toronto". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemComment | kMDItemComment |
| A comment related to the file. This comment is not displayed by the Finder. | A comment related to the file. This comment is not displayed by the Finder. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContactKeywords | kMDItemContactKeywords |
| A list of contacts that are associated with this document, not including the authors. | A list of contacts that are associated with this document, not including the authors. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContentCreationDate | kMDItemContentCreationDate |
| The date and time that the content was created. | The date and time that the content was created. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContentModificationDate | kMDItemContentModificationDate |
| Date and time when the content of this item was modified. | Date and time when the content of this item was modified. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContentType | kMDItemContentType |
| Uniform Type Identifier of the file. For example, a jpeg image file will have a value of public.jpeg. The value of this attribute is set by the Spotlight importer. Changes to this value are lost when the file attributes are next imported. This attribute is marked as `nosearch`. You must specify this attribute key explicitly in a query in order for its contents to be searched. | Uniform Type Identifier of the file. For example, a jpeg image file will have a value of public.jpeg. The value of this attribute is set by the Spotlight importer. Changes to this value are lost when the file attributes are next imported. This attribute is marked as `nosearch`. You must specify this attribute key explicitly in a query in order for its contents to be searched. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContentTypeTree | kMDItemContentTypeTree |
| Uniform Type Identifier hierarchy of the file. For example, a jpeg image file will return an array containing “public.jpeg”, “public.image”, and “public.data”. The value of this attribute is set by the Spotlight importer. Changes to this value are lost when the file attributes are next imported. This attribute is marked as `nosearch`. You must specify this attribute key explicitly in a query in order for its contents to be searched. | Uniform Type Identifier hierarchy of the file. For example, a jpeg image file will return an array containing “public.jpeg”, “public.image”, and “public.data”. The value of this attribute is set by the Spotlight importer. Changes to this value are lost when the file attributes are next imported. This attribute is marked as `nosearch`. You must specify this attribute key explicitly in a query in order for its contents to be searched. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemContributors | kMDItemContributors |
| Entities responsible for making contributions to the content of the resource. Examples of a contributor include a person, an organization or a service. | Entities responsible for making contributions to the content of the resource. Examples of a contributor include a person, an organization or a service. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemCopyright | kMDItemCopyright |
| Copyright owner of the file contents. | Copyright owner of the file contents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemCountry | kMDItemCountry |
| The full, publishable name of the country or primary location where the intellectual property of the item was created, according to guidelines of the provider. | The full, publishable name of the country or primary location where the intellectual property of the item was created, according to guidelines of the provider. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemCoverage | kMDItemCoverage |
| Extent or scope of the content of the resource. Coverage will typically include spatial location (a place name or geographic co-ordinates), temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity). Recommended best practice is to select a value from a controlled vocabulary, and that, where appropriate, named places or time periods be used in preference to numeric identifiers such as sets of co-ordinates or date ranges. | Extent or scope of the content of the resource. Coverage will typically include spatial location (a place name or geographic co-ordinates), temporal period (a period label, date, or date range) or jurisdiction (such as a named administrative entity). Recommended best practice is to select a value from a controlled vocabulary, and that, where appropriate, named places or time periods be used in preference to numeric identifiers such as sets of co-ordinates or date ranges. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemCreator | kMDItemCreator |
| Name of the application used to create the document content. For example, "Pages" or "Keynote". | Name of the application used to create the document content. For example, "Pages" or "Keynote". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemDescription | kMDItemDescription |
| Description of the kind of item this file represents. | Description of the kind of item this file represents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemDisplayName | kMDItemDisplayName |
| Localized version of the file name. This is the localized version of the LaunchServices call  `LSCopyDisplayNameForURL()` / `LSCopyDisplayNameForRef()` . | Localized version of the file name. This is the localized version of the LaunchServices call  `LSCopyDisplayNameForURL()` / `LSCopyDisplayNameForRef()` . |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemDueDate | kMDItemDueDate |
| Date this item is due. | Date this item is due. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemDurationSeconds | kMDItemDurationSeconds |
| The duration, in seconds, of the content of the item. A value of 10.5 represents media that is 10 and 1/2 seconds long. | The duration, in seconds, of the content of the item. A value of 10.5 represents media that is 10 and 1/2 seconds long. |
| __Value Type:__ | CFNumber |
| __Units:__ | seconds |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemEmailAddresses | kMDItemEmailAddresses |
| Email addresses related to this item. | Email addresses related to this item. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemEncodingApplications | kMDItemEncodingApplications |
| Applications used to convert the original content into it's current form. For example, a PDF file might have an encoding application set to "Distiller". | Applications used to convert the original content into it's current form. For example, a PDF file might have an encoding application set to "Distiller". |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFinderComment | kMDItemFinderComment |
| Finder comments for this item. | Finder comments for this item. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFonts | kMDItemFonts |
| Fonts used by this item. You should store the font's full name, the postscript name, or the font family name, based on the available information. | Fonts used by this item. You should store the font's full name, the postscript name, or the font family name, based on the available information. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemHeadline | kMDItemHeadline |
| Publishable entry providing a synopsis of the contents of the item. For example, "Apple Introduces the iPod Photo". | Publishable entry providing a synopsis of the contents of the item. For example, "Apple Introduces the iPod Photo". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemIdentifier | kMDItemIdentifier |
| Formal identifier used to reference the resource within a given context. For example, the Message-ID of a mail message. | Formal identifier used to reference the resource within a given context. For example, the Message-ID of a mail message. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemInstantMessageAddresses | kMDItemInstantMessageAddresses |
| Instant message addresses related to this item. | Instant message addresses related to this item. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemInstructions | kMDItemInstructions |
| Instructions concerning the use of the item, such as embargoes and warnings. For example, "Second of four stories". | Instructions concerning the use of the item, such as embargoes and warnings. For example, "Second of four stories". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemKeywords | kMDItemKeywords |
| Keywords associated with this file. For example, "Birthday", "Important", etc. | Keywords associated with this file. For example, "Birthday", "Important", etc. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemKind | kMDItemKind |
| Description of the kind of item this file represents. | Description of the kind of item this file represents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemLanguages | kMDItemLanguages |
| Indicates the languages used by the item. The recommended best practice for the values of this attribute are defined by RFC 3066. | Indicates the languages used by the item. The recommended best practice for the values of this attribute are defined by RFC 3066. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemLastUsedDate | kMDItemLastUsedDate |
| Date and time that the file was last used. This value is updated automatically by LaunchServices every time a file is opened by double clicking, or by asking LaunchServices to open a file. | Date and time that the file was last used. This value is updated automatically by LaunchServices every time a file is opened by double clicking, or by asking LaunchServices to open a file. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemNumberOfPages | kMDItemNumberOfPages |
| Number of pages in the document. | Number of pages in the document. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemNamedLocation | kMDItemNamedLocation |
| The name of the location or point of interest associated with the item. The name may be user provided. | The name of the location or point of interest associated with the item. The name may be user provided. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.6 and later. |

| kMDItemOrganizations | kMDItemOrganizations |
| Companies or organizations that created the document. | Companies or organizations that created the document. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPageHeight | kMDItemPageHeight |
| Height of the document page, in points (72 points per inch). For PDF files this indicates the height of the first page only. | Height of the document page, in points (72 points per inch). For PDF files this indicates the height of the first page only. |
| __Value Type:__ | CFNumber |
| __Units:__ | points |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPageWidth | kMDItemPageWidth |
| Width of the document page, in points (72 points per inch). For PDF files this indicates the width of the first page only. | Width of the document page, in points (72 points per inch). For PDF files this indicates the width of the first page only. |
| __Value Type:__ | CFNumber |
| __Units:__ | points |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemParticipants | kMDItemParticipants |
| The list of people who are visible in an image or movie or written about in a document. | The list of people who are visible in an image or movie or written about in a document. |
| __Value Type:__ | Array of CFStringss |
| __Framework:__ | CoreServices/CoreServices |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.6 and later. |

| kMDItemPhoneNumbers | kMDItemPhoneNumbers |
| Phone numbers related to this item. | Phone numbers related to this item. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemProjects | kMDItemProjects |
| List of projects related to this item. For example, if you were working on a movie, all of the files could be marked as belonging to the project “My Movie”. | List of projects related to this item. For example, if you were working on a movie, all of the files could be marked as belonging to the project “My Movie”. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPublishers | kMDItemPublishers |
| Publishers of the item. For example, a person, an organization, or a service. | Publishers of the item. For example, a person, an organization, or a service. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemRecipients | kMDItemRecipients |
| Recipients of this item. | Recipients of this item. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemRecipientAddresses | kMDItemRecipientAddresses |
| This attribute indicates the recipient addresses of the document. | This attribute indicates the recipient addresses of the document. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.6 and later. |

| kMDItemRights | kMDItemRights |
| Provides a link to information about rights held on the document. Contains a rights management statement for the document, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), copyright, and various property rights. If this attribute is absent, no assumptions can be made about the status of these and other rights with respect to the document. | Provides a link to information about rights held on the document. Contains a rights management statement for the document, or reference a service providing such information. Rights information often encompasses Intellectual Property Rights (IPR), copyright, and various property rights. If this attribute is absent, no assumptions can be made about the status of these and other rights with respect to the document. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemSecurityMethod | kMDItemSecurityMethod |
| Encryption method used to make the item secure. PDF files return "None" or "Password Encrypted". | Encryption method used to make the item secure. PDF files return "None" or "Password Encrypted". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemStarRating | kMDItemStarRating |
| User rating of this item. For example, the user rating (number of stars) of an iTunes track. | User rating of this item. For example, the user rating (number of stars) of an iTunes track. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemStateOrProvince | kMDItemStateOrProvince |
| Province or state of origin according to guidelines established by the provider. For example, "CA", "Ontario", or "Sussex". | Province or state of origin according to guidelines established by the provider. For example, "CA", "Ontario", or "Sussex". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemTextContent | kMDItemTextContent |
| Contains a text representation of the content of the document. Data in multiple fields should be combined using a whitespace character as a separator. An application's Spotlight importer provides the content of this attribute. Applications can create queries using this attribute, but are not able to read the value of this attribute directly. | Contains a text representation of the content of the document. Data in multiple fields should be combined using a whitespace character as a separator. An application's Spotlight importer provides the content of this attribute. Applications can create queries using this attribute, but are not able to read the value of this attribute directly. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemTitle | kMDItemTitle |
| Title of the item. For example, this could be the title of a document, the name of an song, or the subject of an email message. | Title of the item. For example, this could be the title of a document, the name of an song, or the subject of an email message. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemVersion | kMDItemVersion |
| Version number of the item. | Version number of the item. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemWhereFroms | kMDItemWhereFroms |
| Describes where the item was obtained from. For example, a downloaded file may refer to the URL, files received by email may indicate the sender’s email address, message subject, etc. | Describes where the item was obtained from. For example, a downloaded file may refer to the URL, files received by email may indicate the sender’s email address, message subject, etc. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

Image Metadata Attribute Keys

Metadata attribute keys that are common to image files.

| kMDItemAcquisitionMake | kMDItemAcquisitionMake |
| Manufacturer of the device used to acquire the document contents. | Manufacturer of the device used to acquire the document contents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAcquisitionModel | kMDItemAcquisitionModel |
| Model of the device used to acquire the document contents. | Model of the device used to acquire the document contents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAlbum | kMDItemAlbum |
| Title for the collection containing this item. This is analogous to a record label or photo album. | Title for the collection containing this item. This is analogous to a record label or photo album. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAperture | kMDItemAperture |
| Aperture setting used when the image was created. This unit is the APEX value. | Aperture setting used when the image was created. This unit is the APEX value. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemBitsPerSample | kMDItemBitsPerSample |
| Number of bits per sample. For example, the bit depth of an image (8-bit, 16-bit etc...) or the bit depth per audio sample of uncompressed audio data (8, 16, 24, 32, 64, etc..). | Number of bits per sample. For example, the bit depth of an image (8-bit, 16-bit etc...) or the bit depth per audio sample of uncompressed audio data (8, 16, 24, 32, 64, etc..). |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemColorSpace | kMDItemColorSpace |
| Color space model used by the document contents. For example, “RGB”, “CMYK”, “YUV”, or “YCbCr”. | Color space model used by the document contents. For example, “RGB”, “CMYK”, “YUV”, or “YCbCr”. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemEXIFVersion | kMDItemEXIFVersion |
| Version of the EXIF header used to generate the metadata. | Version of the EXIF header used to generate the metadata. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemExposureMode | kMDItemExposureMode |
| Exposure mode used to acquire the document contents. | Exposure mode used to acquire the document contents. |
| __Value Type:__ | CFNumber |
| __Expected Values:__ | 0 (auto exposure), 1 (manual exposure), 2 (auto bracket) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemExposureProgram | kMDItemExposureProgram |
| Type of exposure program used by the camera to acquire the document contents. Possible values include: Manual, Normal, Aperture priority, etc. | Type of exposure program used by the camera to acquire the document contents. Possible values include: Manual, Normal, Aperture priority, etc. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemExposureTimeSeconds | kMDItemExposureTimeSeconds |
| Exposure time used to capture the document contents. | Exposure time used to capture the document contents. |
| __Value Type:__ | CFNumber |
| __Units:__ | seconds |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemExposureTimeString | kMDItemExposureTimeString |
| Time when the document contents were captured. Typically this corresponds to when a photograph is exposed. | Time when the document contents were captured. Typically this corresponds to when a photograph is exposed. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFNumber | kMDItemFNumber |
| Diameter of the aperture relative to the effective focal length of the lens. | Diameter of the aperture relative to the effective focal length of the lens. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFlashOnOff | kMDItemFlashOnOff |
| Whether a camera flash was used to capture the document contents. | Whether a camera flash was used to capture the document contents. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFocalLength | kMDItemFocalLength |
| Actual focal length of the lens, in millimeters. | Actual focal length of the lens, in millimeters. |
| __Value Type:__ | CFNumber |
| __Units:__ | millimeters |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemHasAlphaChannel | kMDItemHasAlphaChannel |
| Whether the image has an alpha channel. | Whether the image has an alpha channel. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemISOSpeed | kMDItemISOSpeed |
| ISO speed used to acquire the document contents. For example, 100, 200, 400, etc. | ISO speed used to acquire the document contents. For example, 100, 200, 400, etc. |
| __Value Type:__ | CFNumber |
| __Units:__ | ISO Speed |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemLayerNames | kMDItemLayerNames |
| Names of the layers in the file. | Names of the layers in the file. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMaxAperture | kMDItemMaxAperture |
| Smallest F number of the lens in APEX value units, usually in the range of 00.00 to 99.99. | Smallest F number of the lens in APEX value units, usually in the range of 00.00 to 99.99. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMeteringMode | kMDItemMeteringMode |
| Metering mode used to acquire the image. | Metering mode used to acquire the image. |
| __Value Type:__ | CFString |
| __Expected Values:__ | Unknown, Average, CenterWeightedAverage, Spot, MultiSpot, Pattern, Partial |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemOrientation | kMDItemOrientation |
| Orientation of the document contents. | Orientation of the document contents. |
| __Value Type:__ | CFNumber |
| __Expected Values:__ | 0 (landscape), 1 (portrait) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPixelHeight | kMDItemPixelHeight |
| Height, in pixels, of the contents. For example, the image height or the video frame height. | Height, in pixels, of the contents. For example, the image height or the video frame height. |
| __Value Type:__ | CFNumber |
| __Units:__ | pixels |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPixelWidth | kMDItemPixelWidth |
| Width, in pixels, of the contents. For example, the image width or the video frame width. | Width, in pixels, of the contents. For example, the image width or the video frame width. |
| __Value Type:__ | CFNumber |
| __Units:__ | pixels |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPixelCount | kMDItemPixelCount |
| The total number of pixels in the contents.. Same as `[kMDItemPixelWidth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojufvjvonzw)` \* `[kMDItemPixelHeight](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojufvjvonzv)`. | The total number of pixels in the contents.. Same as `[kMDItemPixelWidth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojufvjvonzw)` \* `[kMDItemPixelHeight](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmojufvjvonzv)`. |
| __Value Type:__ | CFNumber |
| __Units:__ | pixels |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.6 and later. |

| kMDItemProfileName | kMDItemProfileName |
| Name of the color profile used by the document contents. | Name of the color profile used by the document contents. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemRedEyeOnOff | kMDItemRedEyeOnOff |
| Whether red-eye reduction was used to take the picture. | Whether red-eye reduction was used to take the picture. |
| __Value Type:__ | CFBoolean |
| __Expected Values:__ | 0 (no red-eye reduction mode or unknown), 1 (red-eye reduction used) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemResolutionHeightDPI | kMDItemResolutionHeightDPI |
| Resolution height, in DPI, of the item. | Resolution height, in DPI, of the item. |
| __Value Type:__ | CFNumber |
| __Units:__ | dots per inch (DPI) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemResolutionWidthDPI | kMDItemResolutionWidthDPI |
| Resolution width, in DPI, of the item. | Resolution width, in DPI, of the item. |
| __Value Type:__ | CFNumber |
| __Units:__ | dots per inch (DPI) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemWhiteBalance | kMDItemWhiteBalance |
| White balance setting of the camera when the picture was taken. | White balance setting of the camera when the picture was taken. |
| __Value Type:__ | CFNumber |
| __Expected Values:__ | 0 (auto white balance), 1 (manual) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

Video Metadata Attribute Keys

Metadata attribute keys that are common to video files.

| kMDItemAudioBitRate | kMDItemAudioBitRate |
| Bit rate of the audio in the media. | Bit rate of the audio in the media. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemCodecs | kMDItemCodecs |
| Codecs used to encode/decode the media. | Codecs used to encode/decode the media. |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemDeliveryType | kMDItemDeliveryType |
| Method used to deliver streaming media. | Method used to deliver streaming media. |
| __Value Type:__ | CFString |
| __Expected Values:__ | "Fast Start", "RTSP" |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMediaTypes | kMDItemMediaTypes |
| Media types present in the content. For example, a QuickTime movie may return:  |  | | --- | | ``` kMDItemMediaTypes = (Sound, Video, "Hinted Video Track", "Hinted Sound Track") ``` | | ``` kMDItemMediaTypes = (Sound, Video) ``` | | ``` kMDItemMediaTypes = ("MPEG1 Muxed") ``` | | Media types present in the content. For example, a QuickTime movie may return:  |  | | --- | | ``` kMDItemMediaTypes = (Sound, Video, "Hinted Video Track", "Hinted Sound Track") ``` | | ``` kMDItemMediaTypes = (Sound, Video) ``` | | ``` kMDItemMediaTypes = ("MPEG1 Muxed") ``` | |
| __Value Type:__ | Array of  CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemStreamable | kMDItemStreamable |
| Whether the content is prepared for streaming. | Whether the content is prepared for streaming. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemTotalBitRate | kMDItemTotalBitRate |
| Total bit rate, audio and video combined, of the media. | Total bit rate, audio and video combined, of the media. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemVideoBitRate | kMDItemVideoBitRate |
| Bit rate of the video in the media. | Bit rate of the video in the media. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

Audio Metadata Attribute Keys

Metadata attribute keys that describe an audio file.

| kMDItemAppleLoopDescriptors | kMDItemAppleLoopDescriptors |
| Specifies multiple pieces of descriptive information about a loop. Besides genre and instrument, files can contain descriptive information that help users in refining searches. | Specifies multiple pieces of descriptive information about a loop. Besides genre and instrument, files can contain descriptive information that help users in refining searches. |
| __Value Type:__ | Array of CFStrings |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAppleLoopsKeyFilterType | kMDItemAppleLoopsKeyFilterType |
| Specifies key filtering information about a loop. Loops are matched against projects that often differ in a major or minor key. To assist users in identifying loops that will "fit" with their compositions, loops can be tagged with one of the following key filters: "AnyKey", "Minor", "Major", "NeitherKey", or "BothKeys". "AnyKey" means that it fits with anything (whether in a major key, minor key or neither). "Minor" fits with compositions in a minor key. "NeitherKey" doesn't work well with compositions that are in major or minor key. "BothKeys" means it fits with compositions that are in major or minor key. | Specifies key filtering information about a loop. Loops are matched against projects that often differ in a major or minor key. To assist users in identifying loops that will "fit" with their compositions, loops can be tagged with one of the following key filters: "AnyKey", "Minor", "Major", "NeitherKey", or "BothKeys". "AnyKey" means that it fits with anything (whether in a major key, minor key or neither). "Minor" fits with compositions in a minor key. "NeitherKey" doesn't work well with compositions that are in major or minor key. "BothKeys" means it fits with compositions that are in major or minor key. |
| __Value Type:__ | CFString |
| __Expected Values:__ | "AnyKey", "Minor", "Major" , "NeitherKey", "BothKeys" |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAppleLoopsLoopMode | kMDItemAppleLoopsLoopMode |
| Specifies how a file should be played. Tagged files can either be loops or non-loops (e.g., a cymbal crash). "Looping" indicates if the file should be treated as a loop. "Non-looping" indicates the file should not be treated as a loop. | Specifies how a file should be played. Tagged files can either be loops or non-loops (e.g., a cymbal crash). "Looping" indicates if the file should be treated as a loop. "Non-looping" indicates the file should not be treated as a loop. |
| __Value Type:__ | CFString |
| __Expected Values:__ | "Looping", "Non-looping" |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAppleLoopsRootKey | kMDItemAppleLoopsRootKey |
| Specifies the loop's original key. The key is the root note or tonic for the loop, and does not include the scale type | Specifies the loop's original key. The key is the root note or tonic for the loop, and does not include the scale type |
| __Value Type:__ | CFString |
| __Expected Values:__ | "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B", "NoKey" |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAudioChannelCount | kMDItemAudioChannelCount |
| Number of channels in the audio data contained in the file. This integer value only represents the number of discrete channels of audio data found in the file. It does not indicate any configuration of the data in regards to a user's speaker setup. | Number of channels in the audio data contained in the file. This integer value only represents the number of discrete channels of audio data found in the file. It does not indicate any configuration of the data in regards to a user's speaker setup. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAudioEncodingApplication | kMDItemAudioEncodingApplication |
| Name of the application that encoded the audio of the document. | Name of the application that encoded the audio of the document. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAudioSampleRate | kMDItemAudioSampleRate |
| Sample rate of the item's audio data. The sample rate is a float value representing Hz (audio_frames/second). For example: 44100.0, 22254.54. | Sample rate of the item's audio data. The sample rate is a float value representing Hz (audio_frames/second). For example: 44100.0, 22254.54. |
| __Value Type:__ | CFNumber |
| __Units:__ | Hz (audio_frames/second) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemAudioTrackNumber | kMDItemAudioTrackNumber |
| Track number of a song or composition when it is part of an album. | Track number of a song or composition when it is part of an album. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemComposer | kMDItemComposer |
| Composer of the song in the audio file. | Composer of the song in the audio file. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemIsGeneralMIDISequence | kMDItemIsGeneralMIDISequence |
| Whether the MIDI sequence contained in the file is set up for use with a General MIDI device. | Whether the MIDI sequence contained in the file is set up for use with a General MIDI device. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemKeySignature | kMDItemKeySignature |
| Musical key of the song in the audio file. For example: "C", "Dm", "F#m", "Bb". | Musical key of the song in the audio file. For example: "C", "Dm", "F#m", "Bb". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemLyricist | kMDItemLyricist |
| Lyricist of the song in the audio file. | Lyricist of the song in the audio file. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMusicalGenre | kMDItemMusicalGenre |
| Musical genre of the song or composition contained in the audio file. For example: "Jazz", "Pop", "Rock", "Classical". | Musical genre of the song or composition contained in the audio file. For example: "Jazz", "Pop", "Rock", "Classical". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMusicalInstrumentCategory | kMDItemMusicalInstrumentCategory |
| Specifies the category of an instrument. Files should have an instrument associated with them ("Other Instrument" is provided as a catch-all). For some categories, such as "Keyboards", there are instrument names which provide a more detailed instrument definition, for example "Piano" or "Organ". | Specifies the category of an instrument. Files should have an instrument associated with them ("Other Instrument" is provided as a catch-all). For some categories, such as "Keyboards", there are instrument names which provide a more detailed instrument definition, for example "Piano" or "Organ". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemMusicalInstrumentName | kMDItemMusicalInstrumentName |
| Specifies the name of instrument relative to the instrument category. Files can have an instrument name associated with them if they have certain instrument categories. For example, the "Percussion" category has multiple instruments, including "Conga" and "Bongo". | Specifies the name of instrument relative to the instrument category. Files can have an instrument name associated with them if they have certain instrument categories. For example, the "Percussion" category has multiple instruments, including "Conga" and "Bongo". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemRecordingDate | kMDItemRecordingDate |
| Recording date of the song or composition. This is in contrast to `kMDItemContentCreationDate` which, could indicate the creation date of an edited or "mastered" version of the original art. | Recording date of the song or composition. This is in contrast to `kMDItemContentCreationDate` which, could indicate the creation date of an edited or "mastered" version of the original art. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemRecordingYear | kMDItemRecordingYear |
| Year the item was recorded. For example: 1964, 1995, 1997, or 2003. | Year the item was recorded. For example: 1964, 1995, 1997, or 2003. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemTempo | kMDItemTempo |
| Tempo of the music in the audio file. A floating point value. | Tempo of the music in the audio file. A floating point value. |
| __Value Type:__ | CFNumber |
| __Units:__ | Beats per Minute (BPM) |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemTimeSignature | kMDItemTimeSignature |
| Time signature of the musical composition contained in the audio/MIDI file. For example: "4/4", "7/8". | Time signature of the musical composition contained in the audio/MIDI file. For example: "4/4", "7/8". |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

File System Metadata Attribute Keys

Metadata attribute keys that describe the file system attributes for a file. These attributes are available for files on any mounted volume.

| kMDItemFSContentChangeDate | kMDItemFSContentChangeDate |
| Date the file contents last changed. | Date the file contents last changed. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSCreationDate | kMDItemFSCreationDate |
| Date that the contents of the file were created. | Date that the contents of the file were created. |
| __Value Type:__ | CFDate |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSInvisible | kMDItemFSInvisible |
| Whether the file is invisible. | Whether the file is invisible. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSIsExtensionHidden | kMDItemFSIsExtensionHidden |
| Whether the file extension of the file is hidden. | Whether the file extension of the file is hidden. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSLabel | kMDItemFSLabel |
| Index of the Finder label of the file. Possible values are 0 through 7. | Index of the Finder label of the file. Possible values are 0 through 7. |
| __Value Type:__ | CFNumber |
| __Expected Values:__ | 0 through 7 |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSName | kMDItemFSName |
| File name of the item. | File name of the item. |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSNodeCount | kMDItemFSNodeCount |
| Number of files in a directory. | Number of files in a directory. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSOwnerGroupID | kMDItemFSOwnerGroupID |
| Group ID of the owner of the file. | Group ID of the owner of the file. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSOwnerUserID | kMDItemFSOwnerUserID |
| User ID of the owner of the file. | User ID of the owner of the file. |
| __Value Type:__ | CFNumber |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemFSSize | kMDItemFSSize |
| Size, in bytes, of the file on disk. | Size, in bytes, of the file on disk. |
| __Value Type:__ | CFNumber |
| __Units:__ | bytes |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

| kMDItemPath | kMDItemPath |
| Complete path to the file. This value of this attribute can be retrieved, but can't be used in a query or to sort search results. This attribute can’t be used as a member of the `valueListAttrs` array parameter for [MDQueryCreate](https://developer.apple.com/documentation/coreservices/1413029-mdquerycreate) or [MDQueryCreateSubset](https://developer.apple.com/documentation/coreservices/1413027-mdquerycreatesubset). | Complete path to the file. This value of this attribute can be retrieved, but can't be used in a query or to sort search results. This attribute can’t be used as a member of the `valueListAttrs` array parameter for [MDQueryCreate](https://developer.apple.com/documentation/coreservices/1413029-mdquerycreate) or [MDQueryCreateSubset](https://developer.apple.com/documentation/coreservices/1413027-mdquerycreatesubset). |
| __Value Type:__ | CFString |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Available in OS X v10.4 and later. |

Deprecated Metadata Attribute Keys

Metadata attribute keys that have been deprecated.

| kMDItemFSExists | kMDItemFSExists |
| This attribute is deprecated and was never implemented. | This attribute is deprecated and was never implemented. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Deprecated in OS X v10.4 and later. |

| kMDItemFSIsReadable | kMDItemFSIsReadable |
| This attribute is deprecated and was never implemented. | This attribute is deprecated and was never implemented. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Deprecated in OS X v10.4 and later. |

| kMDItemFSIsWriteable | kMDItemFSIsWriteable |
| This attribute is deprecated and was never implemented. | This attribute is deprecated and was never implemented. |
| __Value Type:__ | CFBoolean |
| __Framework:__ | CoreServices/CoreServices.h |
| __Header:__ | MDItem.h |
| __Availability:__ | Deprecated in OS X v10.4 and later. |

[Next](iCloud%20Metadata%20Attributes.md)[Previous](About%20the%20File%20Metadata%20Attributes%20Reference.md)

