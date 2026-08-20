---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/AddressBook.html
archived_at: '2026-07-18T02:54:24.445667Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# AddressBook Changes

## AddressBook

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

ABAddressBook.hAdded [-[ABAddressBook addRecord:error:]](https://developer.apple.com/documentation/addressbook/abaddressbook/1458709-addrecord)Added [-[ABAddressBook removeRecord:error:]](https://developer.apple.com/documentation/addressbook/abaddressbook/1458388-removerecord)Added [ABAddRecordsError](https://developer.apple.com/documentation/addressbook/abaddrecordserror)Added [ABAddressBookErrorDomain](https://developer.apple.com/documentation/addressbook/abaddressbookerrordomain)Added [ABMultiValueIdentifiersErrorKey](https://developer.apple.com/documentation/addressbook/abmultivalueidentifierserrorkey)Added [ABPropertyReadOnlyError](https://developer.apple.com/documentation/addressbook/1529225-errors/abpropertyreadonlyerror)Added [ABPropertyUnsupportedBySourceError](https://developer.apple.com/documentation/addressbook/1529225-errors/abpropertyunsupportedbysourceerror)Added [ABPropertyValueValidationError](https://developer.apple.com/documentation/addressbook/abpropertyvaluevalidationerror)Added [ABRemoveRecordsError](https://developer.apple.com/documentation/addressbook/abremoverecordserror)ABAddressBookC.hModified [ABAddPropertiesAndTypes()](https://developer.apple.com/documentation/addressbook/1430200-abaddpropertiesandtypes)

|  | Declaration |
| --- | --- |
| From | CFIndex ABAddPropertiesAndTypes ( ABAddressBookRef addressBook, CFStringRef recordType, CFDictionaryRef propertiesAnTypes); |
| To | CFIndex ABAddPropertiesAndTypes ( ABAddressBookRef addressBook, CFStringRef recordType, CFDictionaryRef propertiesAndTypes); |

ABGlobals.hAdded [kABBirthdayComponentsProperty](https://developer.apple.com/documentation/addressbook/kabbirthdaycomponentsproperty)Added [kABInstantMessageProperty](https://developer.apple.com/documentation/addressbook/kabinstantmessageproperty)Added [kABInstantMessageServiceAIM](https://developer.apple.com/documentation/addressbook/kabinstantmessageserviceaim)Added [kABInstantMessageServiceFacebook](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicefacebook)Added [kABInstantMessageServiceGaduGadu](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicegadugadu)Added [kABInstantMessageServiceGoogleTalk](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicegoogletalk)Added [kABInstantMessageServiceICQ](https://developer.apple.com/documentation/addressbook/kabinstantmessageserviceicq)Added [kABInstantMessageServiceJabber](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicejabber)Added [kABInstantMessageServiceKey](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicekey)Added [kABInstantMessageServiceMSN](https://developer.apple.com/documentation/addressbook/kabinstantmessageservicemsn)Added [kABInstantMessageServiceQQ](https://developer.apple.com/documentation/addressbook/kabinstantmessageserviceqq)Added [kABInstantMessageServiceSkype](https://developer.apple.com/documentation/addressbook/kabinstantmessageserviceskype)Added [kABInstantMessageServiceYahoo](https://developer.apple.com/documentation/addressbook/kabinstantmessageserviceyahoo)Added [kABInstantMessageUsernameKey](https://developer.apple.com/documentation/addressbook/kabinstantmessageusernamekey)Added [kABMobileMeLabel](https://developer.apple.com/documentation/addressbook/kabmobilemelabel)Added [kABOtherDateComponentsProperty](https://developer.apple.com/documentation/addressbook/kabotherdatecomponentsproperty)Added [kABSocialProfileProperty](https://developer.apple.com/documentation/addressbook/kabsocialprofileproperty)Added [kABSocialProfileServiceFacebook](https://developer.apple.com/documentation/addressbook/kabsocialprofileservicefacebook)Added [kABSocialProfileServiceFlickr](https://developer.apple.com/documentation/addressbook/kabsocialprofileserviceflickr)Added [kABSocialProfileServiceKey](https://developer.apple.com/documentation/addressbook/kabsocialprofileservicekey)Added [kABSocialProfileServiceLinkedIn](https://developer.apple.com/documentation/addressbook/kabsocialprofileservicelinkedin)Added [kABSocialProfileServiceMySpace](https://developer.apple.com/documentation/addressbook/kabsocialprofileservicemyspace)Added [kABSocialProfileServiceTwitter](https://developer.apple.com/documentation/addressbook/kabsocialprofileservicetwitter)Added [kABSocialProfileURLKey](https://developer.apple.com/documentation/addressbook/kabsocialprofileurlkey)Added [kABSocialProfileUserIdentifierKey](https://developer.apple.com/documentation/addressbook/kabsocialprofileuseridentifierkey)Added [kABSocialProfileUsernameKey](https://developer.apple.com/documentation/addressbook/kabsocialprofileusernamekey)Modified [kABJabberWorkLabel](https://developer.apple.com/documentation/addressbook/kabjabberworklabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABICQHomeLabel](https://developer.apple.com/documentation/addressbook/kabicqhomelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABJabberInstantProperty](https://developer.apple.com/documentation/addressbook/kabjabberinstantproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABYahooWorkLabel](https://developer.apple.com/documentation/addressbook/kabyahooworklabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABAIMWorkLabel](https://developer.apple.com/documentation/addressbook/kabaimworklabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABJabberHomeLabel](https://developer.apple.com/documentation/addressbook/kabjabberhomelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABYahooHomeLabel](https://developer.apple.com/documentation/addressbook/kabyahoohomelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABMSNHomeLabel](https://developer.apple.com/documentation/addressbook/kabmsnhomelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABAIMHomeLabel](https://developer.apple.com/documentation/addressbook/kabaimhomelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABMSNInstantProperty](https://developer.apple.com/documentation/addressbook/kabmsninstantproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABICQInstantProperty](https://developer.apple.com/documentation/addressbook/kabicqinstantproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABICQWorkLabel](https://developer.apple.com/documentation/addressbook/kabicqworklabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABAIMMobileMeLabel](https://developer.apple.com/documentation/addressbook/kabaimmobilemelabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABYahooInstantProperty](https://developer.apple.com/documentation/addressbook/kabyahooinstantproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABMSNWorkLabel](https://developer.apple.com/documentation/addressbook/kabmsnworklabel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kABAIMInstantProperty](https://developer.apple.com/documentation/addressbook/kabaiminstantproperty)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ABPersonView.hAdded [ABPersonView](https://developer.apple.com/documentation/addressbook/abpersonview)Added [ABPersonView.editing](https://developer.apple.com/documentation/addressbook/abpersonview/1411312-editing)Added [ABPersonView.person](https://developer.apple.com/documentation/addressbook/abpersonview/1411310-person)ABRecord.hAdded [-[ABRecord setValue:forProperty:error:]](https://developer.apple.com/documentation/addressbook/abrecord/1400521-setvalue)ABTypedefs.hAdded [kABDateComponentsProperty](https://developer.apple.com/documentation/addressbook/kabdatecomponentsproperty)Added [kABMultiDateComponentsProperty](https://developer.apple.com/documentation/addressbook/kabmultidatecomponentsproperty)

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
