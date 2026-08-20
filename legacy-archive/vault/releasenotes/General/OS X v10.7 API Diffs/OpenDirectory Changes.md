---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/OpenDirectory.html
archived_at: '2026-07-18T02:54:37.078867Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# OpenDirectory Changes

## OpenDirectory

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

CFODContext.hModified [ODContextGetTypeID()](https://developer.apple.com/documentation/opendirectory/1427795-odcontextgettypeid)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODContext.h |

CFODNode.hModified [ODNodeCreateCopy()](https://developer.apple.com/documentation/opendirectory/1427771-odnodecreatecopy)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODNodeRef ODNodeCreateCopy ( CFAllocatorRef inAllocator, ODNodeRef inNode, CFErrorRef \*outError); |
| To | CFODNode.h | ODNodeRef ODNodeCreateCopy ( CFAllocatorRef allocator, ODNodeRef node, CFErrorRef \*error); |

Modified [ODNodeSetCredentialsExtended()](https://developer.apple.com/documentation/opendirectory/1428069-odnodesetcredentialsextended)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODNodeSetCredentialsExtended ( ODNodeRef inNode, ODRecordType inRecordType, ODAuthenticationType inAuthType, CFArrayRef inAuthItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*outError); |
| To | CFODNode.h | bool ODNodeSetCredentialsExtended ( ODNodeRef node, ODRecordType recordType, ODAuthenticationType authType, CFArrayRef authItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*error); |

Modified [ODNodeSetCredentialsUsingKerberosCache()](https://developer.apple.com/documentation/opendirectory/1537206-odnodesetcredentialsusingkerbero)

|  | Header | Deprecation | Declaration |
| --- | --- | --- | --- |
| From | CFOpenDirectory.h | _none_ | bool ODNodeSetCredentialsUsingKerberosCache ( ODNodeRef inNode, CFStringRef inCacheName, CFErrorRef \*outError); |
| To | CFODNode.h | OS X v10.7 | bool ODNodeSetCredentialsUsingKerberosCache ( ODNodeRef node, CFStringRef cacheName, CFErrorRef \*error); |

Modified [ODNodeCreateWithNodeType()](https://developer.apple.com/documentation/opendirectory/1428021-odnodecreatewithnodetype)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODNodeRef ODNodeCreateWithNodeType ( CFAllocatorRef inAllocator, ODSessionRef inSession, ODNodeType inType, CFErrorRef \*outError); |
| To | CFODNode.h | ODNodeRef ODNodeCreateWithNodeType ( CFAllocatorRef allocator, ODSessionRef session, ODNodeType nodeType, CFErrorRef \*error); |

Modified [ODNodeCopySupportedAttributes()](https://developer.apple.com/documentation/opendirectory/1427263-odnodecopysupportedattributes)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODNodeCopySupportedAttributes ( ODNodeRef inNode, ODRecordType inRecordType, CFErrorRef \*outError); |
| To | CFODNode.h | CFArrayRef ODNodeCopySupportedAttributes ( ODNodeRef node, ODRecordType recordType, CFErrorRef \*error); |

Modified [ODNodeCopyRecord()](https://developer.apple.com/documentation/opendirectory/1427368-odnodecopyrecord)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODRecordRef ODNodeCopyRecord ( ODNodeRef inNode, ODRecordType inRecordType, CFStringRef inRecordName, CFArrayRef inAttributes, CFErrorRef \*outError); |
| To | CFODNode.h | ODRecordRef ODNodeCopyRecord ( ODNodeRef node, ODRecordType recordType, CFStringRef recordName, CFTypeRef attributes, CFErrorRef \*error); |

Modified [ODNodeGetTypeID()](https://developer.apple.com/documentation/opendirectory/1427551-odnodegettypeid)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODNode.h |

Modified [ODNodeCopySupportedRecordTypes()](https://developer.apple.com/documentation/opendirectory/1427209-odnodecopysupportedrecordtypes)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODNodeCopySupportedRecordTypes ( ODNodeRef inNode, CFErrorRef \*outError); |
| To | CFODNode.h | CFArrayRef ODNodeCopySupportedRecordTypes ( ODNodeRef node, CFErrorRef \*error); |

Modified [ODNodeCustomCall()](https://developer.apple.com/documentation/opendirectory/1427838-odnodecustomcall)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFDataRef ODNodeCustomCall ( ODNodeRef inNode, CFIndex inCustomCode, CFDataRef inSendData, CFErrorRef \*outError); |
| To | CFODNode.h | CFDataRef ODNodeCustomCall ( ODNodeRef node, CFIndex customCode, CFDataRef data, CFErrorRef \*error); |

Modified [ODNodeCreateWithName()](https://developer.apple.com/documentation/opendirectory/1427133-odnodecreatewithname)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODNodeRef ODNodeCreateWithName ( CFAllocatorRef inAllocator, ODSessionRef inSession, CFStringRef inNodeName, CFErrorRef \*outError); |
| To | CFODNode.h | ODNodeRef ODNodeCreateWithName ( CFAllocatorRef allocator, ODSessionRef session, CFStringRef nodeName, CFErrorRef \*error); |

Modified [ODNodeGetName()](https://developer.apple.com/documentation/opendirectory/1426944-odnodegetname)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFStringRef ODNodeGetName ( ODNodeRef inNode); |
| To | CFODNode.h | CFStringRef ODNodeGetName ( ODNodeRef node); |

Modified [ODNodeCreateRecord()](https://developer.apple.com/documentation/opendirectory/1427989-odnodecreaterecord)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODRecordRef ODNodeCreateRecord ( ODNodeRef inNode, ODRecordType inRecordType, CFStringRef inRecordName, CFDictionaryRef inAttributes, CFErrorRef \*outError); |
| To | CFODNode.h | ODRecordRef ODNodeCreateRecord ( ODNodeRef node, ODRecordType recordType, CFStringRef recordName, CFDictionaryRef attributeDict, CFErrorRef \*error); |

Modified [ODNodeSetCredentials()](https://developer.apple.com/documentation/opendirectory/1427179-odnodesetcredentials)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODNodeSetCredentials ( ODNodeRef inNode, ODRecordType inRecordType, CFStringRef inRecordName, CFStringRef inPassword, CFErrorRef \*outError); |
| To | CFODNode.h | bool ODNodeSetCredentials ( ODNodeRef node, ODRecordType recordType, CFStringRef recordName, CFStringRef password, CFErrorRef \*error); |

Modified [ODNodeCopySubnodeNames()](https://developer.apple.com/documentation/opendirectory/1427388-odnodecopysubnodenames)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODNodeCopySubnodeNames ( ODNodeRef inNode, CFErrorRef \*outError); |
| To | CFODNode.h | CFArrayRef ODNodeCopySubnodeNames ( ODNodeRef node, CFErrorRef \*error); |

Modified [ODNodeCopyUnreachableSubnodeNames()](https://developer.apple.com/documentation/opendirectory/1428190-odnodecopyunreachablesubnodename)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODNodeCopyUnreachableSubnodeNames ( ODNodeRef inNode, CFErrorRef \*outError); |
| To | CFODNode.h | CFArrayRef ODNodeCopyUnreachableSubnodeNames ( ODNodeRef node, CFErrorRef \*error); |

Modified [ODNodeCopyDetails()](https://developer.apple.com/documentation/opendirectory/1427681-odnodecopydetails)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFDictionaryRef ODNodeCopyDetails ( ODNodeRef inNode, CFArrayRef inKeys, CFErrorRef \*outError); |
| To | CFODNode.h | CFDictionaryRef ODNodeCopyDetails ( ODNodeRef node, CFArrayRef keys, CFErrorRef \*error); |

CFODQuery.hModified [ODQueryScheduleWithRunLoop()](https://developer.apple.com/documentation/opendirectory/1427247-odqueryschedulewithrunloop)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | void ODQueryScheduleWithRunLoop ( ODQueryRef inQuery, CFRunLoopRef inRunLoop, CFStringRef inRunLoopMode); |
| To | CFODQuery.h | void ODQueryScheduleWithRunLoop ( ODQueryRef query, CFRunLoopRef runLoop, CFStringRef runLoopMode); |

Modified [ODQuerySetCallback()](https://developer.apple.com/documentation/opendirectory/1427306-odquerysetcallback)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | void ODQuerySetCallback ( ODQueryRef inQuery, ODQueryCallback inCallback, void \*inUserInfo); |
| To | CFODQuery.h | void ODQuerySetCallback ( ODQueryRef query, ODQueryCallback callback, void \*userInfo); |

Modified [ODQueryGetTypeID()](https://developer.apple.com/documentation/opendirectory/1427793-odquerygettypeid)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODQuery.h |

Modified [ODQueryCopyResults()](https://developer.apple.com/documentation/opendirectory/1426942-odquerycopyresults)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODQueryCopyResults ( ODQueryRef inQuery, bool inAllowPartialResults, CFErrorRef \*outError); |
| To | CFODQuery.h | CFArrayRef ODQueryCopyResults ( ODQueryRef query, bool allowPartialResults, CFErrorRef \*error); |

Modified [ODQueryCreateWithNodeType()](https://developer.apple.com/documentation/opendirectory/1428246-odquerycreatewithnodetype)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODQueryRef ODQueryCreateWithNodeType ( CFAllocatorRef inAllocator, ODNodeType inType, CFTypeRef inRecordTypeOrList, ODAttributeType inAttribute, ODMatchType inMatchType, CFTypeRef inQueryValueOrList, CFTypeRef inReturnAttributeOrList, CFIndex inMaxResults, CFErrorRef \*outError); |
| To | CFODQuery.h | ODQueryRef ODQueryCreateWithNodeType ( CFAllocatorRef allocator, ODNodeType nodeType, CFTypeRef recordTypeOrList, ODAttributeType attribute, ODMatchType matchType, CFTypeRef queryValueOrList, CFTypeRef returnAttributeOrList, CFIndex maxResults, CFErrorRef \*error); |

Modified [ODQuerySetDispatchQueue()](https://developer.apple.com/documentation/opendirectory/1427637-odquerysetdispatchqueue)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | void ODQuerySetDispatchQueue ( ODQueryRef inQuery, dispatch_queue_t inQueue); |
| To | CFODQuery.h | void ODQuerySetDispatchQueue ( ODQueryRef query, dispatch_queue_t queue); |

Modified [ODQueryCallback](https://developer.apple.com/documentation/opendirectory/odquerycallback)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODQuery.h |

Modified [ODQuerySynchronize()](https://developer.apple.com/documentation/opendirectory/1428133-odquerysynchronize)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | void ODQuerySynchronize ( ODQueryRef inQuery); |
| To | CFODQuery.h | void ODQuerySynchronize ( ODQueryRef query); |

Modified [ODQueryCreateWithNode()](https://developer.apple.com/documentation/opendirectory/1427159-odquerycreatewithnode)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODQueryRef ODQueryCreateWithNode ( CFAllocatorRef inAllocator, ODNodeRef inNode, CFTypeRef inRecordTypeOrList, ODAttributeType inAttribute, ODMatchType inMatchType, CFTypeRef inQueryValueOrList, CFTypeRef inReturnAttributeOrList, CFIndex inMaxResults, CFErrorRef \*outError); |
| To | CFODQuery.h | ODQueryRef ODQueryCreateWithNode ( CFAllocatorRef allocator, ODNodeRef node, CFTypeRef recordTypeOrList, ODAttributeType attribute, ODMatchType matchType, CFTypeRef queryValueOrList, CFTypeRef returnAttributeOrList, CFIndex maxResults, CFErrorRef \*error); |

Modified [ODQueryUnscheduleFromRunLoop()](https://developer.apple.com/documentation/opendirectory/1427456-odqueryunschedulefromrunloop)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | void ODQueryUnscheduleFromRunLoop ( ODQueryRef inQuery, CFRunLoopRef inRunLoop, CFStringRef inRunLoopMode); |
| To | CFODQuery.h | void ODQueryUnscheduleFromRunLoop ( ODQueryRef query, CFRunLoopRef runLoop, CFStringRef runLoopMode); |

CFODRecord.hModified [ODRecordRemoveValue()](https://developer.apple.com/documentation/opendirectory/1427332-odrecordremovevalue)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordRemoveValue ( ODRecordRef inRecord, ODAttributeType inAttribute, CFTypeRef inValue, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordRemoveValue ( ODRecordRef record, ODAttributeType attribute, CFTypeRef value, CFErrorRef \*error); |

Modified [ODRecordAddMember()](https://developer.apple.com/documentation/opendirectory/1427898-odrecordaddmember)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordAddMember ( ODRecordRef inGroup, ODRecordRef inMember, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordAddMember ( ODRecordRef group, ODRecordRef member, CFErrorRef \*error); |

Modified [ODRecordRemoveMember()](https://developer.apple.com/documentation/opendirectory/1427621-odrecordremovemember)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordRemoveMember ( ODRecordRef inGroup, ODRecordRef inMember, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordRemoveMember ( ODRecordRef group, ODRecordRef member, CFErrorRef \*error); |

Modified [ODRecordCopyDetails()](https://developer.apple.com/documentation/opendirectory/1427472-odrecordcopydetails)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFDictionaryRef ODRecordCopyDetails ( ODRecordRef inRecord, CFArrayRef inAttributes, CFErrorRef \*outError); |
| To | CFODRecord.h | CFDictionaryRef ODRecordCopyDetails ( ODRecordRef record, CFArrayRef attributes, CFErrorRef \*error); |

Modified [ODRecordAddValue()](https://developer.apple.com/documentation/opendirectory/1427832-odrecordaddvalue)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordAddValue ( ODRecordRef inRecord, ODAttributeType inAttribute, CFTypeRef inValue, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordAddValue ( ODRecordRef record, ODAttributeType attribute, CFTypeRef value, CFErrorRef \*error); |

Modified [ODRecordSetNodeCredentialsUsingKerberosCache()](https://developer.apple.com/documentation/opendirectory/1492463-odrecordsetnodecredentialsusingk)

|  | Header | Deprecation | Declaration |
| --- | --- | --- | --- |
| From | CFOpenDirectory.h | _none_ | bool ODRecordSetNodeCredentialsUsingKerberosCache ( ODRecordRef inRecord, CFStringRef inCacheName, CFErrorRef \*outError); |
| To | CFODRecord.h | OS X v10.7 | bool ODRecordSetNodeCredentialsUsingKerberosCache ( ODRecordRef record, CFStringRef cacheName, CFErrorRef \*error); |

Modified [ODRecordGetRecordName()](https://developer.apple.com/documentation/opendirectory/1428047-odrecordgetrecordname)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFStringRef ODRecordGetRecordName ( ODRecordRef inRecord); |
| To | CFODRecord.h | CFStringRef ODRecordGetRecordName ( ODRecordRef record); |

Modified [ODRecordChangePassword()](https://developer.apple.com/documentation/opendirectory/1428272-odrecordchangepassword)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordChangePassword ( ODRecordRef inRecord, CFStringRef inOldPassword, CFStringRef inNewPassword, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordChangePassword ( ODRecordRef record, CFStringRef oldPassword, CFStringRef newPassword, CFErrorRef \*error); |

Modified [ODRecordSetNodeCredentials()](https://developer.apple.com/documentation/opendirectory/1427646-odrecordsetnodecredentials)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordSetNodeCredentials ( ODRecordRef inRecord, CFStringRef inUsername, CFStringRef inPassword, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordSetNodeCredentials ( ODRecordRef record, CFStringRef username, CFStringRef password, CFErrorRef \*error); |

Modified [ODRecordVerifyPasswordExtended()](https://developer.apple.com/documentation/opendirectory/1427104-odrecordverifypasswordextended)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordVerifyPasswordExtended ( ODRecordRef inRecord, ODAuthenticationType inAuthType, CFArrayRef inAuthItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordVerifyPasswordExtended ( ODRecordRef record, ODAuthenticationType authType, CFArrayRef authItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*error); |

Modified [ODRecordCopyPasswordPolicy()](https://developer.apple.com/documentation/opendirectory/1492461-odrecordcopypasswordpolicy)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFDictionaryRef ODRecordCopyPasswordPolicy ( CFAllocatorRef inAllocator, ODRecordRef inRecord, CFErrorRef \*outError); |
| To | CFODRecord.h | CFDictionaryRef ODRecordCopyPasswordPolicy ( CFAllocatorRef allocator, ODRecordRef record, CFErrorRef \*error); |

Modified [ODRecordDelete()](https://developer.apple.com/documentation/opendirectory/1427118-odrecorddelete)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordDelete ( ODRecordRef inRecord, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordDelete ( ODRecordRef record, CFErrorRef \*error); |

Modified [ODRecordSetNodeCredentialsExtended()](https://developer.apple.com/documentation/opendirectory/1427347-odrecordsetnodecredentialsextend)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordSetNodeCredentialsExtended ( ODRecordRef inRecord, ODRecordType inRecordType, ODAuthenticationType inAuthType, CFArrayRef inAuthItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordSetNodeCredentialsExtended ( ODRecordRef record, ODRecordType recordType, ODAuthenticationType authType, CFArrayRef authItems, CFArrayRef \*outAuthItems, ODContextRef \*outContext, CFErrorRef \*error); |

Modified [ODRecordVerifyPassword()](https://developer.apple.com/documentation/opendirectory/1427277-odrecordverifypassword)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordVerifyPassword ( ODRecordRef inRecord, CFStringRef inPassword, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordVerifyPassword ( ODRecordRef record, CFStringRef password, CFErrorRef \*error); |

Modified [ODRecordGetTypeID()](https://developer.apple.com/documentation/opendirectory/1427466-odrecordgettypeid)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODRecord.h |

Modified [ODRecordContainsMember()](https://developer.apple.com/documentation/opendirectory/1427923-odrecordcontainsmember)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordContainsMember ( ODRecordRef inGroup, ODRecordRef inMember, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordContainsMember ( ODRecordRef group, ODRecordRef member, CFErrorRef \*error); |

Modified [ODRecordCopyValues()](https://developer.apple.com/documentation/opendirectory/1428186-odrecordcopyvalues)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODRecordCopyValues ( ODRecordRef inRecord, ODAttributeType inAttribute, CFErrorRef \*outError); |
| To | CFODRecord.h | CFArrayRef ODRecordCopyValues ( ODRecordRef record, ODAttributeType attribute, CFErrorRef \*error); |

Modified [ODRecordGetRecordType()](https://developer.apple.com/documentation/opendirectory/1428067-odrecordgetrecordtype)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFStringRef ODRecordGetRecordType ( ODRecordRef inRecord); |
| To | CFODRecord.h | CFStringRef ODRecordGetRecordType ( ODRecordRef record); |

Modified [ODRecordSynchronize()](https://developer.apple.com/documentation/opendirectory/1428125-odrecordsynchronize)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordSynchronize ( ODRecordRef inRecord, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordSynchronize ( ODRecordRef record, CFErrorRef \*error); |

Modified [ODRecordSetValue()](https://developer.apple.com/documentation/opendirectory/1427997-odrecordsetvalue)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | bool ODRecordSetValue ( ODRecordRef inRecord, ODAttributeType inAttribute, CFTypeRef inValueOrValues, CFErrorRef \*outError); |
| To | CFODRecord.h | bool ODRecordSetValue ( ODRecordRef record, ODAttributeType attribute, CFTypeRef valueOrValues, CFErrorRef \*error); |

CFODSession.hModified [kODSessionDefault](https://developer.apple.com/documentation/opendirectory/kodsessiondefault)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODSession.h |

Modified [ODSessionGetTypeID()](https://developer.apple.com/documentation/opendirectory/1427498-odsessiongettypeid)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFODSession.h |

Modified [ODSessionCopyNodeNames()](https://developer.apple.com/documentation/opendirectory/1427427-odsessioncopynodenames)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | CFArrayRef ODSessionCopyNodeNames ( CFAllocatorRef inAllocator, ODSessionRef inSession, CFErrorRef \*outError); |
| To | CFODSession.h | CFArrayRef ODSessionCopyNodeNames ( CFAllocatorRef allocator, ODSessionRef session, CFErrorRef \*error); |

Modified [ODSessionCreate()](https://developer.apple.com/documentation/opendirectory/1427961-odsessioncreate)

|  | Header | Declaration |
| --- | --- | --- |
| From | CFOpenDirectory.h | ODSessionRef ODSessionCreate ( CFAllocatorRef inAllocator, CFDictionaryRef inOptions, CFErrorRef \*outError); |
| To | CFODSession.h | ODSessionRef ODSessionCreate ( CFAllocatorRef allocator, CFDictionaryRef options, CFErrorRef \*error); |

CFOpenDirectoryConstants.hAdded [kODAttributeTypeAdvertisedServices](https://developer.apple.com/documentation/opendirectory/kodattributetypeadvertisedservices)Added [kODAttributeTypeAltSecurityIdentities](https://developer.apple.com/documentation/opendirectory/kodattributetypealtsecurityidentities)Added [kODAttributeTypeHardwareUUID](https://developer.apple.com/documentation/opendirectory/kodattributetypehardwareuuid)Added [kODAttributeTypeKerberosServices](https://developer.apple.com/documentation/opendirectory/kodattributetypekerberosservices)Added [kODAttributeTypeLocaleRelay](https://developer.apple.com/documentation/opendirectory/kodattributetypelocalerelay)Added [kODAttributeTypeLocaleSubnets](https://developer.apple.com/documentation/opendirectory/kodattributetypelocalesubnets)Added [kODAttributeTypeMetaAmbiguousName](https://developer.apple.com/documentation/opendirectory/kodattributetypemetaambiguousname)Added [kODAttributeTypeMetaAugmentedAttributes](https://developer.apple.com/documentation/opendirectory/kodattributetypemetaaugmentedattributes)Added [kODAttributeTypeMetaRecordName](https://developer.apple.com/documentation/opendirectory/kodattributetypemetarecordname)Added [kODAttributeTypeNetworkInterfaces](https://developer.apple.com/documentation/opendirectory/kodattributetypenetworkinterfaces)Added [kODAttributeTypeOperatingSystem](https://developer.apple.com/documentation/opendirectory/kodattributetypeoperatingsystem)Added [kODAttributeTypeOperatingSystemVersion](https://developer.apple.com/documentation/opendirectory/kodattributetypeoperatingsystemversion)Added [kODAttributeTypeParentLocales](https://developer.apple.com/documentation/opendirectory/kodattributetypeparentlocales)Added [kODAttributeTypePrimaryLocale](https://developer.apple.com/documentation/opendirectory/kodattributetypeprimarylocale)Added [kODAttributeTypeTrustInformation](https://developer.apple.com/documentation/opendirectory/kodattributetypetrustinformation)Added [kODAuthenticationTypeSetCertificateHashAsCurrent](https://developer.apple.com/documentation/opendirectory/kodauthenticationtypesetcertificatehashascurrent)Added [kODErrorNodeDisabled](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrornodedisabled)Added [kODErrorPluginOperationTimeout](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorpluginoperationtimeout)Added [kODErrorRecordNoLongerExists](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorrecordnolongerexists)Added [kODErrorSuccess](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsuccess)Modified [kODErrorCredentialsParameterError](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialsparametererror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorNodeUnknownName](https://developer.apple.com/documentation/opendirectory/koderrornodeunknownname)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsServerError](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsservererror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordAttributeValueNotFound](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorrecordattributevaluenotfound)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordReadOnlyNode](https://developer.apple.com/documentation/opendirectory/koderrorrecordreadonlynode)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorQuerySynchronize](https://developer.apple.com/documentation/opendirectory/koderrorquerysynchronize)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorPluginError](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorpluginerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordChangeTooSoon](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialspasswordchangetoosoon)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODSessionProxyPassword](https://developer.apple.com/documentation/opendirectory/kodsessionproxypassword)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordTooLong](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialspasswordtoolong)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorQueryUnsupportedMatchType](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorqueryunsupportedmatchtype)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordPermissionError](https://developer.apple.com/documentation/opendirectory/koderrorrecordpermissionerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODSessionProxyPort](https://developer.apple.com/documentation/opendirectory/kodsessionproxyport)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODSessionProxyAddress](https://developer.apple.com/documentation/opendirectory/kodsessionproxyaddress)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsAccountDisabled](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialsaccountdisabled)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordNeedsDigit](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordneedsdigit)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordTypeDisabled](https://developer.apple.com/documentation/opendirectory/koderrorrecordtypedisabled)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsInvalidComputer](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsinvalidcomputer)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorNodeUnknownHost](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrornodeunknownhost)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsContactMaster](https://developer.apple.com/documentation/opendirectory/koderrorcredentialscontactmaster)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionNormalDaemonInUse](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionnormaldaemoninuse)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsOperationFailed](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsoperationfailed)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordAttributeUnknownType](https://developer.apple.com/documentation/opendirectory/koderrorrecordattributeunknowntype)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordInvalidType](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorrecordinvalidtype)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionProxyUnknownHost](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionproxyunknownhost)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsServerTimeout](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsservertimeout)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorNodeConnectionFailed](https://developer.apple.com/documentation/opendirectory/koderrornodeconnectionfailed)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionProxyCommunicationError](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionproxycommunicationerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionProxyIPUnreachable](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionproxyipunreachable)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordAlreadyExists](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorrecordalreadyexists)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified ODFrameworkErrors

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordQualityFailed](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordqualityfailed)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorQueryTimeout](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorquerytimeout)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsServerUnreachable](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialsserverunreachable)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordExpired](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordexpired)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsInvalid](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsinvalid)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionProxyVersionMismatch](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionproxyversionmismatch)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordNeedsLetter](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordneedsletter)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODSessionProxyUsername](https://developer.apple.com/documentation/opendirectory/kodsessionproxyusername)

|  | Header |
| --- | --- |
| From | CFOpenDirectory.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsAccountInactive](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsaccountinactive)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordAttributeValueSchemaError](https://developer.apple.com/documentation/opendirectory/koderrorrecordattributevalueschemaerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordParameterError](https://developer.apple.com/documentation/opendirectory/koderrorrecordparametererror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordUnrecoverable](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordunrecoverable)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordTooShort](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialspasswordtooshort)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionLocalOnlyDaemonInUse](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessionlocalonlydaemoninuse)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsMethodNotSupported](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialsmethodnotsupported)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsAccountNotFound](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsaccountnotfound)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsNotAuthorized](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsnotauthorized)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsPasswordChangeRequired](https://developer.apple.com/documentation/opendirectory/koderrorcredentialspasswordchangerequired)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorRecordAttributeNotFound](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorrecordattributenotfound)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsInvalidLogonHours](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorcredentialsinvalidlogonhours)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionDaemonNotRunning](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessiondaemonnotrunning)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsServerNotFound](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsservernotfound)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorSessionDaemonRefused](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrorsessiondaemonrefused)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODAuthenticationTypeSecureHash](https://developer.apple.com/documentation/opendirectory/kodauthenticationtypesecurehash)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [kODErrorDaemonError](https://developer.apple.com/documentation/opendirectory/odframeworkerrors/koderrordaemonerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorPluginOperationNotSupported](https://developer.apple.com/documentation/opendirectory/koderrorpluginoperationnotsupported)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsAccountExpired](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsaccountexpired)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorNodeUnknownType](https://developer.apple.com/documentation/opendirectory/koderrornodeunknowntype)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorQueryInvalidMatchType](https://developer.apple.com/documentation/opendirectory/koderrorqueryinvalidmatchtype)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

Modified [kODErrorCredentialsServerCommunicationError](https://developer.apple.com/documentation/opendirectory/koderrorcredentialsservercommunicationerror)

|  | Header |
| --- | --- |
| From | CFOpenDirectoryErrors.h |
| To | CFOpenDirectoryConstants.h |

ODNode.hModified [-[ODNode supportedRecordTypesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1427314-supportedrecordtypes)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode createRecordWithRecordType:name:attributes:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427031-createrecord)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode recordWithRecordType:name:attributes:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1428065-recordwithrecordtype)

|  | Header | Declaration |
| --- | --- | --- |
| From | NSOpenDirectory.h | - (ODRecord \*)recordWithRecordType:(ODRecordType)inRecordType name:(NSString \*)inRecordName attributes:(NSArray \*)inAttributes error:(NSError \*\*)outError |
| To | ODNode.h | - (ODRecord \*)recordWithRecordType:(ODRecordType)inRecordType name:(NSString \*)inRecordName attributes:(id)inAttributes error:(NSError \*\*)outError |

Modified [-[ODNode customCall:sendData:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427478-customcall)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode setCredentialsUsingKerberosCache:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427785-setcredentialsusingkerberoscache)

|  | Header | Deprecation |
| --- | --- | --- |
| From | NSOpenDirectory.h | _none_ |
| To | ODNode.h | OS X v10.7 |

Modified [ODNode.nodeName](https://developer.apple.com/documentation/opendirectory/odnode/1427779-nodename)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode supportedAttributesForRecordType:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1428017-supportedattributesforrecordtype)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode unreachableSubnodeNamesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1427251-unreachablesubnodenamesandreturn)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode initWithSession:name:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1428278-init)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode initWithSession:type:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427701-init)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode subnodeNamesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odnode/1428155-subnodenamesandreturnerror)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode nodeDetailsForKeys:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427177-nodedetailsforkeys)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode setCredentialsWithRecordType:recordName:password:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1427290-setcredentialswithrecordtype)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [ODNode](https://developer.apple.com/documentation/opendirectory/odnode)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [+[ODNode nodeWithSession:name:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1569409-nodewithsession)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [-[ODNode setCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1426987-setcredentialswithrecordtype)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

Modified [+[ODNode nodeWithSession:type:error:]](https://developer.apple.com/documentation/opendirectory/odnode/1569410-nodewithsession)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODNode.h |

ODQuery.hModified [ODQuery.delegate](https://developer.apple.com/documentation/opendirectory/odquery/1391713-delegate)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQuery initWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:]](https://developer.apple.com/documentation/opendirectory/odquery/1391711-init)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQueryDelegate query:foundResults:error:]](https://developer.apple.com/documentation/opendirectory/odquerydelegate/1391704-query)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [ODQuery](https://developer.apple.com/documentation/opendirectory/odquery)

|  | Header | Protocols |
| --- | --- | --- |
| From | NSOpenDirectory.h | _none_ |
| To | ODQuery.h | NSCopying |

Modified [ODQuery.operationQueue](https://developer.apple.com/documentation/opendirectory/odquery/1391696-operationqueue)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQuery scheduleInRunLoop:forMode:]](https://developer.apple.com/documentation/opendirectory/odquery/1391698-scheduleinrunloop)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQuery synchronize]](https://developer.apple.com/documentation/opendirectory/odquery/1391697-synchronize)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQuery resultsAllowingPartial:error:]](https://developer.apple.com/documentation/opendirectory/odquery/1391702-resultsallowingpartial)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [-[ODQuery removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/opendirectory/odquery/1391695-removefromrunloop)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [+[ODQuery queryWithNode:forRecordTypes:attribute:matchType:queryValues:returnAttributes:maximumResults:error:]](https://developer.apple.com/documentation/opendirectory/odquery/1391709-querywithnode)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

Modified [ODQueryDelegate](https://developer.apple.com/documentation/opendirectory/odquerydelegate)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODQuery.h |

ODRecord.hModified [-[ODRecord passwordPolicyAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1470047-passwordpolicyandreturnerror)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord addMemberRecord:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427807-addmemberrecord)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord removeMemberRecord:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427555-removememberrecord)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord valuesForAttribute:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427803-valuesforattribute)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord setNodeCredentials:password:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427258-setnodecredentials)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [ODRecord.recordName](https://developer.apple.com/documentation/opendirectory/odrecord/1426976-recordname)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord synchronizeAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427579-synchronizeandreturnerror)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord isMemberRecord:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427975-ismemberrecord)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord deleteRecordAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427488-deleterecordandreturnerror)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord setValue:forAttribute:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427911-setvalue)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord changePassword:toPassword:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427145-changepassword)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord addValue:toAttribute:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427729-addvalue)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [ODRecord](https://developer.apple.com/documentation/opendirectory/odrecord)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord removeValue:fromAttribute:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1428290-removevalue)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord removeValuesForAttribute:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427273-removevaluesforattribute)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord verifyPassword:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427894-verifypassword)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [ODRecord.recordType](https://developer.apple.com/documentation/opendirectory/odrecord/1427211-recordtype)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord verifyExtendedWithAuthenticationType:authenticationItems:continueItems:context:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427575-verifyextendedwithauthentication)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord setNodeCredentialsUsingKerberosCache:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1470016-setnodecredentialsusingkerberosc)

|  | Header | Deprecation |
| --- | --- | --- |
| From | NSOpenDirectory.h | _none_ |
| To | ODRecord.h | OS X v10.7 |

Modified [-[ODRecord setNodeCredentialsWithRecordType:authenticationType:authenticationItems:continueItems:context:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427282-setnodecredentialswithrecordtype)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified ODRecord(ODRecordGroupExtensions)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

Modified [-[ODRecord recordDetailsForAttributes:error:]](https://developer.apple.com/documentation/opendirectory/odrecord/1427081-recorddetails)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODRecord.h |

ODSession.hModified [+[ODSession sessionWithOptions:error:]](https://developer.apple.com/documentation/opendirectory/odsession/1563458-sessionwithoptions)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [-[ODSession nodeNamesAndReturnError:]](https://developer.apple.com/documentation/opendirectory/odsession/1427490-nodenames)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [ODSessionProxyUsername](https://developer.apple.com/documentation/opendirectory/odsessionproxyusername)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [-[ODSession initWithOptions:error:]](https://developer.apple.com/documentation/opendirectory/odsession/1427223-init)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [+[ODSession defaultSession]](https://developer.apple.com/documentation/opendirectory/odsession/1428153-default)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [ODSession](https://developer.apple.com/documentation/opendirectory/odsession)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [ODSessionProxyAddress](https://developer.apple.com/documentation/opendirectory/odsessionproxyaddress)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [ODSessionProxyPassword](https://developer.apple.com/documentation/opendirectory/odsessionproxypassword)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

Modified [ODSessionProxyPort](https://developer.apple.com/documentation/opendirectory/odsessionproxyport)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | ODSession.h |

OpenDirectory.hModified [ODFrameworkErrorDomain](https://developer.apple.com/documentation/opendirectory/odframeworkerrordomain)

|  | Header |
| --- | --- |
| From | NSOpenDirectory.h |
| To | OpenDirectory.h |

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
