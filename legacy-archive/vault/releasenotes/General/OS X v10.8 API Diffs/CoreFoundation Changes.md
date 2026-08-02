---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/CoreFoundation.html
archived_at: '2026-07-18T02:53:57.718388Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# CoreFoundation Changes

## CoreFoundation

CFBase.hAdded #def CF_CONSUMEDAdded #def CF_ENUMAdded CF_ENUM() (no architecture available)Added #def CF_ENUM_AVAILABLEAdded #def CF_ENUM_AVAILABLE_IOSAdded #def CF_ENUM_AVAILABLE_MACAdded #def CF_ENUM_DEPRECATEDAdded #def CF_ENUM_DEPRECATED_IOSAdded #def CF_ENUM_DEPRECATED_MACAdded #def CF_IMPLICIT_BRIDGING_DISABLEDAdded #def CF_IMPLICIT_BRIDGING_ENABLEDAdded #def CF_OPTIONSAdded #def CF_RELEASES_ARGUMENTAdded [#def kCFCoreFoundationVersionNumber10_6_6](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_6)Added [#def kCFCoreFoundationVersionNumber10_6_7](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_7)Added [#def kCFCoreFoundationVersionNumber10_6_8](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_6_8)Added [#def kCFCoreFoundationVersionNumber10_7](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7)Added [#def kCFCoreFoundationVersionNumber10_7_1](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_1)Added [#def kCFCoreFoundationVersionNumber10_7_2](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_2)Added [#def kCFCoreFoundationVersionNumber10_7_3](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_3)Added [#def kCFCoreFoundationVersionNumber10_7_4](https://developer.apple.com/documentation/corefoundation/kcfcorefoundationversionnumber10_7_4)CFCalendar.hAdded CF_OPTIONS() (no architecture available)CFData.hAdded CF_ENUM_AVAILABLE() (no architecture available)CFFileSecurity.hAdded [CFFileSecurityClearProperties()](https://developer.apple.com/documentation/corefoundation/1426500-cffilesecurityclearproperties)Added [kCFFileSecurityClearAccessControlList](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426502-accesscontrollist)Added [kCFFileSecurityClearGroup](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426529-group)Added [kCFFileSecurityClearGroupUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/kcffilesecuritycleargroupuuid)Added [kCFFileSecurityClearMode](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426504-mode)Added [kCFFileSecurityClearOwner](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/1426515-owner)Added [kCFFileSecurityClearOwnerUUID](https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions/kcffilesecurityclearowneruuid)CFSocket.hAdded CF_ENUM_AVAILABLE (no architecture available)CFURL.hAdded [CFURLStartAccessingSecurityScopedResource()](https://developer.apple.com/documentation/corefoundation/1543318-cfurlstartaccessingsecurityscope)Added [CFURLStopAccessingSecurityScopedResource()](https://developer.apple.com/documentation/corefoundation/1542381-cfurlstopaccessingsecurityscoped)Added [kCFURLBookmarkCreationSecurityScopeAllowOnlyReadAccess](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1543362-securityscopeallowonlyreadaccess)Added [kCFURLBookmarkCreationWithSecurityScope](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkcreationoptions/1542198-withsecurityscope)Added [kCFURLBookmarkResolutionWithSecurityScope](https://developer.apple.com/documentation/corefoundation/cfurlbookmarkresolutionoptions/1542878-cfurlbookmarkresolutionwithsecur)Added [kCFURLIsExcludedFromBackupKey](https://developer.apple.com/documentation/corefoundation/kcfurlisexcludedfrombackupkey)Added [kCFURLPathKey](https://developer.apple.com/documentation/corefoundation/kcfurlpathkey)Modified [kCFURLUbiquitousItemPercentUploadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentuploadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [kCFURLUbiquitousItemPercentDownloadedKey](https://developer.apple.com/documentation/corefoundation/kcfurlubiquitousitempercentdownloadedkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

CFXMLNode.hModified [CFXMLNodeGetInfoPtr()](https://developer.apple.com/documentation/corefoundation/1443276-cfxmlnodegetinfoptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeCreateWithNode()](https://developer.apple.com/documentation/corefoundation/1443294-cfxmltreecreatewithnode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeGetNode()](https://developer.apple.com/documentation/corefoundation/1443309-cfxmltreegetnode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeCreateCopy()](https://developer.apple.com/documentation/corefoundation/1443284-cfxmlnodecreatecopy)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeGetTypeID()](https://developer.apple.com/documentation/corefoundation/1443278-cfxmlnodegettypeid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeGetVersion()](https://developer.apple.com/documentation/corefoundation/1443286-cfxmlnodegetversion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeGetTypeCode()](https://developer.apple.com/documentation/corefoundation/1443354-cfxmlnodegettypecode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeCreate()](https://developer.apple.com/documentation/corefoundation/1443360-cfxmlnodecreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLNodeGetString()](https://developer.apple.com/documentation/corefoundation/1443256-cfxmlnodegetstring)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

CFXMLParser.hModified [CFXMLParserGetSourceURL()](https://developer.apple.com/documentation/corefoundation/1553098-cfxmlparsergetsourceurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserCopyErrorDescription()](https://developer.apple.com/documentation/corefoundation/1553087-cfxmlparsercopyerrordescription)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetContext()](https://developer.apple.com/documentation/corefoundation/1553101-cfxmlparsergetcontext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetTypeID()](https://developer.apple.com/documentation/corefoundation/1553097-cfxmlparsergettypeid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeCreateFromDataWithError()](https://developer.apple.com/documentation/corefoundation/1553096-cfxmltreecreatefromdatawitherror)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetDocument()](https://developer.apple.com/documentation/corefoundation/1553086-cfxmlparsergetdocument)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserAbort()](https://developer.apple.com/documentation/corefoundation/1553085-cfxmlparserabort)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeCreateXMLData()](https://developer.apple.com/documentation/corefoundation/1553089-cfxmltreecreatexmldata)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetCallBacks()](https://developer.apple.com/documentation/corefoundation/1553091-cfxmlparsergetcallbacks)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserParse()](https://developer.apple.com/documentation/corefoundation/1553100-cfxmlparserparse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetLineNumber()](https://developer.apple.com/documentation/corefoundation/1553093-cfxmlparsergetlinenumber)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserCreateWithDataFromURL()](https://developer.apple.com/documentation/corefoundation/1553095-cfxmlparsercreatewithdatafromurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserCreate()](https://developer.apple.com/documentation/corefoundation/1553099-cfxmlparsercreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeCreateFromData()](https://developer.apple.com/documentation/corefoundation/1553090-cfxmltreecreatefromdata)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetLocation()](https://developer.apple.com/documentation/corefoundation/1553094-cfxmlparsergetlocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLParserGetStatusCode()](https://developer.apple.com/documentation/corefoundation/1553092-cfxmlparsergetstatuscode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

Modified [CFXMLTreeCreateWithDataFromURL()](https://developer.apple.com/documentation/corefoundation/1553088-cfxmltreecreatewithdatafromurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.8 |

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
