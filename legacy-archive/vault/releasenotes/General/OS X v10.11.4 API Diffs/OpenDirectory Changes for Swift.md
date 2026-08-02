---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/OpenDirectory.html
archived_at: '2026-07-18T02:53:52.788606Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# OpenDirectory Changes for Swift

### OpenDirectory

Modified [ODContext](https://developer.apple.com/documentation/opendirectory/odcontext)

|  | Name | Declaration |
| --- | --- | --- |
| From | ODContextRef | ``` typealias ODContextRef = ODContext ``` |
| To | ODContext | ``` class ODContext { } ``` |

Modified [ODNodeRef](https://developer.apple.com/documentation/opendirectory/odnoderef)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODNodeRef = ODNode ``` |
| To | ``` class ODNodeRef { } ``` |

Modified [ODQueryRef](https://developer.apple.com/documentation/opendirectory/odqueryref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODQueryRef = ODQuery ``` |
| To | ``` class ODQueryRef { } ``` |

Modified [ODRecordRef](https://developer.apple.com/documentation/opendirectory/odrecordref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODRecordRef = ODRecord ``` |
| To | ``` class ODRecordRef { } ``` |

Modified [ODSessionRef](https://developer.apple.com/documentation/opendirectory/odsessionref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODSessionRef = ODSession ``` |
| To | ``` class ODSessionRef { } ``` |

Modified [kODSessionDefault](https://developer.apple.com/documentation/opendirectory/kodsessiondefault)

|  | Declaration |
| --- | --- |
| From | ``` var kODSessionDefault: Unmanaged<ODSession>! ``` |
| To | ``` var kODSessionDefault: Unmanaged<ODSessionRef>! ``` |

Modified [ODNodeAddAccountPolicy(_: ODNodeRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427169-odnodeaddaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeAddAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeAddAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeCopyAccountPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary!](https://developer.apple.com/documentation/opendirectory/1427963-odnodecopyaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyAccountPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODNodeCopyAccountPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |

Modified [ODNodeCopyDetails(_: ODNodeRef!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427681-odnodecopydetails)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyDetails(_ node: ODNode!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopyDetails(_ node: ODNodeRef!, _ keys: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopyPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1426916-odnodecopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopyPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopyRecord(_: ODNodeRef!, _: String!, _: CFString!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>!](https://developer.apple.com/documentation/opendirectory/1427368-odnodecopyrecord)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributes: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` |
| To | ``` func ODNodeCopyRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributes: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>! ``` |

Modified [ODNodeCopySubnodeNames(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427388-odnodecopysubnodenames)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySubnodeNames(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopySupportedAttributes(_: ODNodeRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427263-odnodecopysupportedattributes)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedAttributes(_ node: ODNode!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySupportedAttributes(_ node: ODNodeRef!, _ recordType: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopySupportedPolicies(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427601-odnodecopysupportedpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedPolicies(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODNodeCopySupportedPolicies(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODNodeCopySupportedRecordTypes(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427209-odnodecopysupportedrecordtypes)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopySupportedRecordTypes(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCopyUnreachableSubnodeNames(_: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1428190-odnodecopyunreachablesubnodename)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODNodeCopyUnreachableSubnodeNames(_ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODNodeCreateCopy(_: CFAllocator!, _: ODNodeRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1427771-odnodecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNode!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` |
| To | ``` func ODNodeCreateCopy(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCreateRecord(_: ODNodeRef!, _: String!, _: CFString!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>!](https://developer.apple.com/documentation/opendirectory/1427989-odnodecreaterecord)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateRecord(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecord>! ``` |
| To | ``` func ODNodeCreateRecord(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ attributeDict: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODRecordRef>! ``` |

Modified [ODNodeCreateWithName(_: CFAllocator!, _: ODSessionRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1427133-odnodecreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` |
| To | ``` func ODNodeCreateWithName(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCreateWithNodeType(_: CFAllocator!, _: ODSessionRef!, _: ODNodeType, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>!](https://developer.apple.com/documentation/opendirectory/1428021-odnodecreatewithnodetype)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSession!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNode>! ``` |
| To | ``` func ODNodeCreateWithNodeType(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ nodeType: ODNodeType, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODNodeRef>! ``` |

Modified [ODNodeCustomCall(_: ODNodeRef!, _: CFIndex, _: CFData!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData!](https://developer.apple.com/documentation/opendirectory/1427838-odnodecustomcall)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCustomCall(_ node: ODNode!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData! ``` |
| To | ``` func ODNodeCustomCall(_ node: ODNodeRef!, _ customCode: CFIndex, _ data: CFData!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFData! ``` |

Modified [ODNodeCustomFunction(_: ODNodeRef!, _: CFString!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject!](https://developer.apple.com/documentation/opendirectory/1427565-odnodecustomfunction)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeCustomFunction(_ node: ODNode!, _ function: CFString!, _ payload: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` |
| To | ``` func ODNodeCustomFunction(_ node: ODNodeRef!, _ function: CFString!, _ payload: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> AnyObject! ``` |

Modified [ODNodeGetName(_: ODNodeRef!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/opendirectory/1426944-odnodegetname)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeGetName(_ node: ODNode!) -> Unmanaged<CFString>! ``` |
| To | ``` func ODNodeGetName(_ node: ODNodeRef!) -> Unmanaged<CFString>! ``` |

Modified [ODNodePasswordContentCheck(_: ODNodeRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1426938-odnodepasswordcontentcheck)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodePasswordContentCheck(_ node: ODNode!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodePasswordContentCheck(_ node: ODNodeRef!, _ password: CFString!, _ recordName: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeRemoveAccountPolicy(_: ODNodeRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427805-odnoderemoveaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeRemoveAccountPolicy(_ node: ODNode!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeRemoveAccountPolicy(_ node: ODNodeRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeRemovePolicy(_: ODNodeRef!, _: ODPolicyType!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427219-odnoderemovepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeRemovePolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeRemovePolicy(_ node: ODNodeRef!, _ policyType: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeSetAccountPolicies(_: ODNodeRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427971-odnodesetaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetAccountPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetAccountPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeSetCredentials(_: ODNodeRef!, _: String!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427179-odnodesetcredentials)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetCredentials(_ node: ODNode!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetCredentials(_ node: ODNodeRef!, _ recordType: String!, _ recordName: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeSetCredentialsExtended(_: ODNodeRef!, _: String!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>, _: UnsafeMutablePointer<Unmanaged<ODContext>?>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1428069-odnodesetcredentialsextended)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetCredentialsExtended(_ node: ODNode!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetCredentialsExtended(_ node: ODNodeRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeSetPolicies(_: ODNodeRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427235-odnodesetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetPolicies(_ node: ODNode!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetPolicies(_ node: ODNodeRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODNodeSetPolicy(_: ODNodeRef!, _: ODPolicyType!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427861-odnodesetpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODNodeSetPolicy(_ node: ODNode!, _ policyType: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODNodeSetPolicy(_ node: ODNodeRef!, _ policyType: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODPolicyType](https://developer.apple.com/documentation/opendirectory/odpolicytype)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODPolicyType = ODPolicyType ``` |
| To | ``` typealias ODPolicyType = CFStringRef ``` |

Modified [ODQueryCallback](https://developer.apple.com/documentation/opendirectory/odquerycallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias ODQueryCallback = (ODQuery!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias ODQueryCallback = (ODQueryRef!, CFArray!, CFError!, UnsafeMutablePointer<Void>) -> Void ``` |

Modified [ODQueryCopyResults(_: ODQueryRef!, _: Bool, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1426942-odquerycopyresults)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCopyResults(_ query: ODQuery!, _ allowPartialResults: Bool, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODQueryCopyResults(_ query: ODQueryRef!, _ allowPartialResults: Bool, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODQueryCreateWithNode(_: CFAllocator!, _: ODNodeRef!, _: AnyObject!, _: String!, _: ODMatchType, _: AnyObject!, _: AnyObject!, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>!](https://developer.apple.com/documentation/opendirectory/1427159-odquerycreatewithnode)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNode!, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` |
| To | ``` func ODQueryCreateWithNode(_ allocator: CFAllocator!, _ node: ODNodeRef!, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>! ``` |

Modified [ODQueryCreateWithNodeType(_: CFAllocator!, _: ODNodeType, _: AnyObject!, _: String!, _: ODMatchType, _: AnyObject!, _: AnyObject!, _: CFIndex, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>!](https://developer.apple.com/documentation/opendirectory/1428246-odquerycreatewithnodetype)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQuery>! ``` |
| To | ``` func ODQueryCreateWithNodeType(_ allocator: CFAllocator!, _ nodeType: ODNodeType, _ recordTypeOrList: AnyObject!, _ attribute: String!, _ matchType: ODMatchType, _ queryValueOrList: AnyObject!, _ returnAttributeOrList: AnyObject!, _ maxResults: CFIndex, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODQueryRef>! ``` |

Modified [ODQueryScheduleWithRunLoop(_: ODQueryRef!, _: CFRunLoop!, _: CFString!)](https://developer.apple.com/documentation/opendirectory/1427247-odqueryschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryScheduleWithRunLoop(_ query: ODQuery!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func ODQueryScheduleWithRunLoop(_ query: ODQueryRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |

Modified [ODQuerySetCallback(_: ODQueryRef!, _: ODQueryCallback!, _: UnsafeMutablePointer<Void>)](https://developer.apple.com/documentation/opendirectory/1427306-odquerysetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySetCallback(_ query: ODQuery!, _ callback: ODQueryCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |
| To | ``` func ODQuerySetCallback(_ query: ODQueryRef!, _ callback: ODQueryCallback!, _ userInfo: UnsafeMutablePointer<Void>) ``` |

Modified [ODQuerySetDispatchQueue(_: ODQueryRef!, _: dispatch_queue_t!)](https://developer.apple.com/documentation/opendirectory/1427637-odquerysetdispatchqueue)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySetDispatchQueue(_ query: ODQuery!, _ queue: dispatch_queue_t!) ``` |
| To | ``` func ODQuerySetDispatchQueue(_ query: ODQueryRef!, _ queue: dispatch_queue_t!) ``` |

Modified [ODQuerySynchronize(_: ODQueryRef!)](https://developer.apple.com/documentation/opendirectory/1428133-odquerysynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func ODQuerySynchronize(_ query: ODQuery!) ``` |
| To | ``` func ODQuerySynchronize(_ query: ODQueryRef!) ``` |

Modified [ODQueryUnscheduleFromRunLoop(_: ODQueryRef!, _: CFRunLoop!, _: CFString!)](https://developer.apple.com/documentation/opendirectory/1427456-odqueryunschedulefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func ODQueryUnscheduleFromRunLoop(_ query: ODQuery!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |
| To | ``` func ODQueryUnscheduleFromRunLoop(_ query: ODQueryRef!, _ runLoop: CFRunLoop!, _ runLoopMode: CFString!) ``` |

Modified [ODRecordAddAccountPolicy(_: ODRecordRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427181-odrecordaddaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordAddMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427898-odrecordaddmember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordAddValue(_: ODRecordRef!, _: String!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427832-odrecordaddvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAddValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAddValue(_ record: ODRecordRef!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordAuthenticationAllowed(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427977-odrecordauthenticationallowed)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordAuthenticationAllowed(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordAuthenticationAllowed(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordChangePassword(_: ODRecordRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1428272-odrecordchangepassword)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordChangePassword(_ record: ODRecord!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordChangePassword(_ record: ODRecordRef!, _ oldPassword: CFString!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordContainsMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427923-odrecordcontainsmember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordContainsMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordContainsMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordCopyAccountPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary!](https://developer.apple.com/documentation/opendirectory/1427023-odrecordcopyaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyAccountPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |
| To | ``` func ODRecordCopyAccountPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> CFDictionary! ``` |

Modified [ODRecordCopyDetails(_: ODRecordRef!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427472-odrecordcopydetails)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyDetails(_ record: ODRecord!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyDetails(_ record: ODRecordRef!, _ attributes: CFArray!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyEffectivePolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427362-odrecordcopyeffectivepolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyEffectivePolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427298-odrecordcopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopyPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopySupportedPolicies(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>!](https://developer.apple.com/documentation/opendirectory/1427055-odrecordcopysupportedpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopySupportedPolicies(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |
| To | ``` func ODRecordCopySupportedPolicies(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFDictionary>! ``` |

Modified [ODRecordCopyValues(_: ODRecordRef!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1428186-odrecordcopyvalues)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordCopyValues(_ record: ODRecord!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODRecordCopyValues(_ record: ODRecordRef!, _ attribute: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODRecordDelete(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427118-odrecorddelete)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordDelete(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordDelete(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordGetRecordName(_: ODRecordRef!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/opendirectory/1428047-odrecordgetrecordname)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordGetRecordName(_ record: ODRecord!) -> Unmanaged<CFString>! ``` |
| To | ``` func ODRecordGetRecordName(_ record: ODRecordRef!) -> Unmanaged<CFString>! ``` |

Modified [ODRecordGetRecordType(_: ODRecordRef!) -> Unmanaged<CFString>!](https://developer.apple.com/documentation/opendirectory/1428067-odrecordgetrecordtype)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordGetRecordType(_ record: ODRecord!) -> Unmanaged<CFString>! ``` |
| To | ``` func ODRecordGetRecordType(_ record: ODRecordRef!) -> Unmanaged<CFString>! ``` |

Modified [ODRecordPasswordChangeAllowed(_: ODRecordRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427135-odrecordpasswordchangeallowed)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecord!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordPasswordChangeAllowed(_ record: ODRecordRef!, _ newPassword: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordRemoveAccountPolicy(_: ODRecordRef!, _: CFDictionary!, _: String!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427675-odrecordremoveaccountpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecord!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveAccountPolicy(_ record: ODRecordRef!, _ policy: CFDictionary!, _ category: String!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordRemoveMember(_: ODRecordRef!, _: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427621-odrecordremovemember)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveMember(_ group: ODRecord!, _ member: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveMember(_ group: ODRecordRef!, _ member: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordRemovePolicy(_: ODRecordRef!, _: ODPolicyType!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427063-odrecordremovepolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemovePolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemovePolicy(_ record: ODRecordRef!, _ policy: ODPolicyType!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordRemoveValue(_: ODRecordRef!, _: String!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427332-odrecordremovevalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordRemoveValue(_ record: ODRecord!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordRemoveValue(_ record: ODRecordRef!, _ attribute: String!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSecondsUntilAuthenticationsExpire(_: ODRecordRef!) -> Int64](https://developer.apple.com/documentation/opendirectory/1427380-odrecordsecondsuntilauthenticati)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSecondsUntilAuthenticationsExpire(_ record: ODRecord!) -> Int64 ``` |
| To | ``` func ODRecordSecondsUntilAuthenticationsExpire(_ record: ODRecordRef!) -> Int64 ``` |

Modified [ODRecordSecondsUntilPasswordExpires(_: ODRecordRef!) -> Int64](https://developer.apple.com/documentation/opendirectory/1427195-odrecordsecondsuntilpasswordexpi)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSecondsUntilPasswordExpires(_ record: ODRecord!) -> Int64 ``` |
| To | ``` func ODRecordSecondsUntilPasswordExpires(_ record: ODRecordRef!) -> Int64 ``` |

Modified [ODRecordSetAccountPolicies(_: ODRecordRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427703-odrecordsetaccountpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetAccountPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetAccountPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSetNodeCredentials(_: ODRecordRef!, _: CFString!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427646-odrecordsetnodecredentials)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetNodeCredentials(_ record: ODRecord!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetNodeCredentials(_ record: ODRecordRef!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSetNodeCredentialsExtended(_: ODRecordRef!, _: String!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>, _: UnsafeMutablePointer<Unmanaged<ODContext>?>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427347-odrecordsetnodecredentialsextend)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecord!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetNodeCredentialsExtended(_ record: ODRecordRef!, _ recordType: String!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSetPolicies(_: ODRecordRef!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427387-odrecordsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetPolicies(_ record: ODRecord!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetPolicies(_ record: ODRecordRef!, _ policies: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSetPolicy(_: ODRecordRef!, _: ODPolicyType!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1428137-odrecordsetpolicy)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetPolicy(_ record: ODRecord!, _ policy: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetPolicy(_ record: ODRecordRef!, _ policy: ODPolicyType!, _ value: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSetValue(_: ODRecordRef!, _: String!, _: AnyObject!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427997-odrecordsetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSetValue(_ record: ODRecord!, _ attribute: String!, _ valueOrValues: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSetValue(_ record: ODRecordRef!, _ attribute: String!, _ valueOrValues: AnyObject!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordSynchronize(_: ODRecordRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1428125-odrecordsynchronize)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordSynchronize(_ record: ODRecord!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordSynchronize(_ record: ODRecordRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordVerifyPassword(_: ODRecordRef!, _: CFString!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427277-odrecordverifypassword)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordVerifyPassword(_ record: ODRecord!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordVerifyPassword(_ record: ODRecordRef!, _ password: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordVerifyPasswordExtended(_: ODRecordRef!, _: String!, _: CFArray!, _: UnsafeMutablePointer<Unmanaged<CFArray>?>, _: UnsafeMutablePointer<Unmanaged<ODContext>?>, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool](https://developer.apple.com/documentation/opendirectory/1427104-odrecordverifypasswordextended)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecord!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |
| To | ``` func ODRecordVerifyPasswordExtended(_ record: ODRecordRef!, _ authType: String!, _ authItems: CFArray!, _ outAuthItems: UnsafeMutablePointer<Unmanaged<CFArray>?>, _ outContext: UnsafeMutablePointer<Unmanaged<ODContext>?>, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Bool ``` |

Modified [ODRecordWillAuthenticationsExpire(_: ODRecordRef!, _: UInt64) -> Bool](https://developer.apple.com/documentation/opendirectory/1427171-odrecordwillauthenticationsexpir)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordWillAuthenticationsExpire(_ record: ODRecord!, _ willExpireIn: UInt64) -> Bool ``` |
| To | ``` func ODRecordWillAuthenticationsExpire(_ record: ODRecordRef!, _ willExpireIn: UInt64) -> Bool ``` |

Modified [ODRecordWillPasswordExpire(_: ODRecordRef!, _: UInt64) -> Bool](https://developer.apple.com/documentation/opendirectory/1427185-odrecordwillpasswordexpire)

|  | Declaration |
| --- | --- |
| From | ``` func ODRecordWillPasswordExpire(_ record: ODRecord!, _ willExpireIn: UInt64) -> Bool ``` |
| To | ``` func ODRecordWillPasswordExpire(_ record: ODRecordRef!, _ willExpireIn: UInt64) -> Bool ``` |

Modified [ODSessionCopyNodeNames(_: CFAllocator!, _: ODSessionRef!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!](https://developer.apple.com/documentation/opendirectory/1427427-odsessioncopynodenames)

|  | Declaration |
| --- | --- |
| From | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSession!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |
| To | ``` func ODSessionCopyNodeNames(_ allocator: CFAllocator!, _ session: ODSessionRef!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` |

Modified [ODSessionCreate(_: CFAllocator!, _: CFDictionary!, _: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSessionRef>!](https://developer.apple.com/documentation/opendirectory/1427961-odsessioncreate)

|  | Declaration |
| --- | --- |
| From | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSession>! ``` |
| To | ``` func ODSessionCreate(_ allocator: CFAllocator!, _ options: CFDictionary!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ODSessionRef>! ``` |

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
