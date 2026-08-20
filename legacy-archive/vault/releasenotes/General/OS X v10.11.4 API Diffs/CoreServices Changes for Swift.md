---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/CoreServices.html
archived_at: '2026-07-18T02:53:50.805402Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# CoreServices Changes for Swift

### CoreServices

Modified [CSIdentity](https://developer.apple.com/documentation/coreservices/csidentityref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CSIdentityRef | ``` typealias CSIdentityRef = CSIdentity ``` |
| To | CSIdentity | ``` class CSIdentity { } ``` |

Modified [CSIdentityAuthority](https://developer.apple.com/documentation/coreservices/csidentityauthority)

|  | Name | Declaration |
| --- | --- | --- |
| From | CSIdentityAuthorityRef | ``` typealias CSIdentityAuthorityRef = CSIdentityAuthority ``` |
| To | CSIdentityAuthority | ``` class CSIdentityAuthority { } ``` |

Modified [CSIdentityQuery](https://developer.apple.com/documentation/coreservices/csidentityqueryref)

|  | Name | Declaration |
| --- | --- | --- |
| From | CSIdentityQueryRef | ``` typealias CSIdentityQueryRef = CSIdentityQuery ``` |
| To | CSIdentityQuery | ``` class CSIdentityQuery { } ``` |

Modified [DCSDictionary](https://developer.apple.com/documentation/coreservices/dcsdictionary)

|  | Name | Declaration |
| --- | --- | --- |
| From | DCSDictionaryRef | ``` typealias DCSDictionaryRef = DCSDictionary ``` |
| To | DCSDictionary | ``` class DCSDictionary { } ``` |

Modified [LSItemInfoRecord [struct]](https://developer.apple.com/documentation/coreservices/lsiteminforecord)

|  | Declaration |
| --- | --- |
| From | ``` struct LSItemInfoRecord {     var flags: LSItemInfoFlags     var filetype: OSType     var creator: OSType     var `extension`: Unmanaged<CFString>!     init()     init(flags flags: LSItemInfoFlags, filetype filetype: OSType, creator creator: OSType, `extension` `extension`: Unmanaged<CFString>!) } ``` |
| To | ``` struct LSItemInfoRecord {     var flags: LSItemInfoFlags     var filetype: OSType     var creator: OSType     var `extension`: Unmanaged<CFString>!     init()     init(flags flags: LSItemInfoFlags, filetype filetype: OSType, creator creator: OSType, extension extension: Unmanaged<CFString>!) } ``` |

Modified [LSItemInfoRecord.init(flags: LSItemInfoFlags, filetype: OSType, creator: OSType, extension: Unmanaged<CFString>!)](https://developer.apple.com/documentation/coreservices/lsiteminforecord/1448481-init)

|  | Declaration |
| --- | --- |
| From | ``` init(flags flags: LSItemInfoFlags, filetype filetype: OSType, creator creator: OSType, `extension` `extension`: Unmanaged<CFString>!) ``` |
| To | ``` init(flags flags: LSItemInfoFlags, filetype filetype: OSType, creator creator: OSType, extension extension: Unmanaged<CFString>!) ``` |

Modified [LSSharedFileList](https://developer.apple.com/documentation/coreservices/lssharedfilelistref)

|  | Name | Declaration |
| --- | --- | --- |
| From | LSSharedFileListRef | ``` typealias LSSharedFileListRef = LSSharedFileList ``` |
| To | LSSharedFileList | ``` class LSSharedFileList { } ``` |

Modified [LSSharedFileListItem](https://developer.apple.com/documentation/coreservices/lssharedfilelistitemref)

|  | Name | Declaration |
| --- | --- | --- |
| From | LSSharedFileListItemRef | ``` typealias LSSharedFileListItemRef = LSSharedFileListItem ``` |
| To | LSSharedFileListItem | ``` class LSSharedFileListItem { } ``` |

Modified [MDItem](https://developer.apple.com/documentation/coreservices/mditem)

|  | Name | Declaration |
| --- | --- | --- |
| From | MDItemRef | ``` typealias MDItemRef = MDItem ``` |
| To | MDItem | ``` class MDItem { } ``` |

Modified [MDLabel](https://developer.apple.com/documentation/coreservices/mdlabelref)

|  | Name | Declaration |
| --- | --- | --- |
| From | MDLabelRef | ``` typealias MDLabelRef = MDLabel ``` |
| To | MDLabel | ``` class MDLabel { } ``` |

Modified [MDQuery](https://developer.apple.com/documentation/coreservices/mdqueryref)

|  | Name | Declaration |
| --- | --- | --- |
| From | MDQueryRef | ``` typealias MDQueryRef = MDQuery ``` |
| To | MDQuery | ``` class MDQuery { } ``` |

Modified [SKIndex](https://developer.apple.com/documentation/coreservices/skindex)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKIndexRef | ``` typealias SKIndexRef = SKIndex ``` |
| To | SKIndex | ``` class SKIndex { } ``` |

Modified [SKIndexDocumentIterator](https://developer.apple.com/documentation/coreservices/skindexdocumentiteratorref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKIndexDocumentIteratorRef | ``` typealias SKIndexDocumentIteratorRef = SKIndexDocumentIterator ``` |
| To | SKIndexDocumentIterator | ``` class SKIndexDocumentIterator { } ``` |

Modified [SKSearch](https://developer.apple.com/documentation/coreservices/sksearch)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKSearchRef | ``` typealias SKSearchRef = SKSearch ``` |
| To | SKSearch | ``` class SKSearch { } ``` |

Modified [SKSearchGroup](https://developer.apple.com/documentation/coreservices/sksearchgroupref)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKSearchGroupRef | ``` typealias SKSearchGroupRef = SKSearchGroup ``` |
| To | SKSearchGroup | ``` class SKSearchGroup { } ``` |

Modified [SKSearchResults](https://developer.apple.com/documentation/coreservices/sksearchresults)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKSearchResultsRef | ``` typealias SKSearchResultsRef = SKSearchResults ``` |
| To | SKSearchResults | ``` class SKSearchResults { } ``` |

Modified [SKSummary](https://developer.apple.com/documentation/coreservices/sksummary)

|  | Name | Declaration |
| --- | --- | --- |
| From | SKSummaryRef | ``` typealias SKSummaryRef = SKSummary ``` |
| To | SKSummary | ``` class SKSummary { } ``` |

Modified [MDQuerySetCreateResultFunction(_: MDQuery!, _: MDQueryCreateResultFunction!, _: UnsafeMutablePointer<Void>, _: UnsafePointer<CFArrayCallBacks>)](https://developer.apple.com/documentation/coreservices/1413064-mdquerysetcreateresultfunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ `func`: MDQueryCreateResultFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateResultFunction(_ query: MDQuery!, _ func: MDQueryCreateResultFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |

Modified [MDQuerySetCreateValueFunction(_: MDQuery!, _: MDQueryCreateValueFunction!, _: UnsafeMutablePointer<Void>, _: UnsafePointer<CFArrayCallBacks>)](https://developer.apple.com/documentation/coreservices/1413017-mdquerysetcreatevaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ `func`: MDQueryCreateValueFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func MDQuerySetCreateValueFunction(_ query: MDQuery!, _ func: MDQueryCreateValueFunction!, _ context: UnsafeMutablePointer<Void>, _ cb: UnsafePointer<CFArrayCallBacks>) ``` |

Modified [SKDocument](https://developer.apple.com/documentation/coreservices/skdocument)

|  | Declaration |
| --- | --- |
| From | ``` typealias SKDocumentRef = SKDocument ``` |
| To | ``` typealias SKDocument = CFTypeRef ``` |

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
