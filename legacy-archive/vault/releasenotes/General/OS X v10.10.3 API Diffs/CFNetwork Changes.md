---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/CFNetwork.html
archived_at: '2026-07-18T02:52:07.005135Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# CFNetwork Changes

## CFNetwork

Removed CFNetServiceBrowserFlags.IsRegistrationDomainRemoved CFNetServiceBrowserFlags.valueRemoved CFNetServiceRegisterFlags.valueAdded CFHostClientContext.init()Added CFHostClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Added CFNetServiceBrowserFlags.init(rawValue: CFOptionFlags)Added CFNetServiceClientContext.init()Added CFNetServiceClientContext.init(version: CFIndex, info: UnsafeMutablePointer<Void>, retain: CFAllocatorRetainCallBack, release: CFAllocatorReleaseCallBack, copyDescription: CFAllocatorCopyDescriptionCallBack)Added CFNetServiceRegisterFlags.init(rawValue: CFOptionFlags)Modified CFHostClientContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack } ``` |
| To | ``` struct CFHostClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |

Modified CFHostClientContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFNetServiceBrowserFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceBrowserFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` | RawOptionSet |
| To | ``` struct CFNetServiceBrowserFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` | RawOptionSetType |

Modified CFNetServiceBrowserFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFNetServiceClientContext [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafePointer<()>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack } ``` |
| To | ``` struct CFNetServiceClientContext {     var version: CFIndex     var info: UnsafeMutablePointer<Void>     var retain: CFAllocatorRetainCallBack     var release: CFAllocatorReleaseCallBack     var copyDescription: CFAllocatorCopyDescriptionCallBack     init()     init(version version: CFIndex, info info: UnsafeMutablePointer<Void>, retain retain: CFAllocatorRetainCallBack, release release: CFAllocatorReleaseCallBack, copyDescription copyDescription: CFAllocatorCopyDescriptionCallBack) } ``` |

Modified CFNetServiceClientContext.info

|  | Declaration |
| --- | --- |
| From | ``` var info: UnsafePointer<()> ``` |
| To | ``` var info: UnsafeMutablePointer<Void> ``` |

Modified CFNetServiceRegisterFlags [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFNetServiceRegisterFlags : RawOptionSet {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } } ``` | RawOptionSet |
| To | ``` struct CFNetServiceRegisterFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } } ``` | RawOptionSetType |

Modified CFNetServiceRegisterFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFFTPCreateParsedResourceListing(CFAllocator!, UnsafePointer<UInt8>, CFIndex, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator!, _ buffer: ConstUnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafePointer<Unmanaged<CFDictionary>?>) -> CFIndex ``` | OS X 10.10 |
| To | ``` func CFFTPCreateParsedResourceListing(_ alloc: CFAllocator!, _ buffer: UnsafePointer<UInt8>, _ bufferLength: CFIndex, _ parsed: UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex ``` | OS X 10.3 |

Modified CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication!, CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationCopyRealm(CFHTTPAuthentication!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationCreateFromResponse(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFHTTPAuthentication>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationIsValid(CFHTTPAuthentication!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication!, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHTTPAuthenticationIsValid(_ auth: CFHTTPAuthentication!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.2 |

Modified CFHTTPAuthenticationRequiresAccountDomain(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFHTTPAuthenticationRequiresOrderedRequests(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFHTTPAuthenticationRequiresUserNameAndPassword(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHTTPMessageAddAuthentication(CFHTTPMessage!, CFHTTPMessage!, CFString!, CFString!, CFString!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageAppendBytes(CFHTTPMessage!, UnsafePointer<UInt8>, CFIndex) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHTTPMessageAppendBytes(_ message: CFHTTPMessage!, _ newBytes: ConstUnsafePointer<UInt8>, _ numBytes: CFIndex) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHTTPMessageAppendBytes(_ message: CFHTTPMessage!, _ newBytes: UnsafePointer<UInt8>, _ numBytes: CFIndex) -> Boolean ``` | OS X 10.1 |

Modified CFHTTPMessageApplyCredentialDictionary(CFHTTPMessage!, CFHTTPAuthentication!, CFDictionary!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ dict: CFDictionary!, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHTTPMessageApplyCredentialDictionary(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ dict: CFDictionary!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.4 |

Modified CFHTTPMessageApplyCredentials(CFHTTPMessage!, CFHTTPAuthentication!, CFString!, CFString!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ username: CFString!, _ password: CFString!, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHTTPMessageApplyCredentials(_ request: CFHTTPMessage!, _ auth: CFHTTPAuthentication!, _ username: CFString!, _ password: CFString!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.2 |

Modified CFHTTPMessageCopyAllHeaderFields(CFHTTPMessage!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyBody(CFHTTPMessage!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyHeaderFieldValue(CFHTTPMessage!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyRequestMethod(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyRequestURL(CFHTTPMessage!) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyResponseStatusLine(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopySerializedMessage(CFHTTPMessage!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCopyVersion(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCreateCopy(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCreateEmpty(CFAllocator!, Boolean) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCreateRequest(CFAllocator!, CFString!, CFURL!, CFString!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageCreateResponse(CFAllocator!, CFIndex, CFString!, CFString!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageGetResponseStatusCode(CFHTTPMessage!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageIsHeaderComplete(CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageIsRequest(CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageSetBody(CFHTTPMessage!, CFData!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHTTPMessageSetHeaderFieldValue(CFHTTPMessage!, CFString!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFHostCancelInfoResolution(CFHost!, CFHostInfoType)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFHostClientCallBack = CFunctionPointer<((CFHost!, CFHostInfoType, ConstUnsafePointer<CFStreamError>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFHostClientCallBack = CFunctionPointer<((CFHost!, CFHostInfoType, UnsafePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFHostCreateCopy(CFAllocator!, CFHost!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostCreateWithAddress(CFAllocator!, CFData!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostCreateWithName(CFAllocator!, CFString!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostGetAddressing(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHostGetAddressing(_ theHost: CFHost!, _ hasBeenResolved: UnsafePointer<Boolean>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CFHostGetAddressing(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>! ``` | OS X 10.3 |

Modified CFHostGetNames(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHostGetNames(_ theHost: CFHost!, _ hasBeenResolved: UnsafePointer<Boolean>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CFHostGetNames(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>! ``` | OS X 10.3 |

Modified CFHostGetReachability(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFData>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHostGetReachability(_ theHost: CFHost!, _ hasBeenResolved: UnsafePointer<Boolean>) -> Unmanaged<CFData>! ``` | OS X 10.10 |
| To | ``` func CFHostGetReachability(_ theHost: CFHost!, _ hasBeenResolved: UnsafeMutablePointer<Boolean>) -> Unmanaged<CFData>! ``` | OS X 10.3 |

Modified CFHostGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostScheduleWithRunLoop(CFHost!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFHostSetClient(CFHost!, CFHostClientCallBack, UnsafeMutablePointer<CFHostClientContext>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHostSetClient(_ theHost: CFHost!, _ clientCB: CFHostClientCallBack, _ clientContext: UnsafePointer<CFHostClientContext>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHostSetClient(_ theHost: CFHost!, _ clientCB: CFHostClientCallBack, _ clientContext: UnsafeMutablePointer<CFHostClientContext>) -> Boolean ``` | OS X 10.3 |

Modified CFHostStartInfoResolution(CFHost!, CFHostInfoType, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFHostStartInfoResolution(_ theHost: CFHost!, _ info: CFHostInfoType, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFHostStartInfoResolution(_ theHost: CFHost!, _ info: CFHostInfoType, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.3 |

Modified CFHostUnscheduleFromRunLoop(CFHost!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic!, _ description: UnsafePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus ``` | OS X 10.10 |
| To | ``` func CFNetDiagnosticCopyNetworkStatusPassively(_ details: CFNetDiagnostic!, _ description: UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus ``` | OS X 10.4 |

Modified CFNetDiagnosticCreateWithStreams(CFAllocator!, CFReadStream!, CFWriteStream!) -> Unmanaged<CFNetDiagnostic>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetDiagnosticCreateWithURL(CFAllocator!, CFURL!) -> Unmanaged<CFNetDiagnostic>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic!) -> CFNetDiagnosticStatus

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetDiagnosticSetName(CFNetDiagnostic!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceBrowserClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceBrowserClientCallBack = CFunctionPointer<((CFNetServiceBrowser!, CFOptionFlags, AnyObject!, UnsafePointer<CFStreamError>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFNetServiceBrowserClientCallBack = CFunctionPointer<((CFNetServiceBrowser!, CFOptionFlags, AnyObject!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFNetServiceBrowserCreate(CFAllocator!, CFNetServiceBrowserClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator!, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>! ``` | OS X 10.10 |
| To | ``` func CFNetServiceBrowserCreate(_ alloc: CFAllocator!, _ clientCB: CFNetServiceBrowserClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>! ``` | OS X 10.2 |

Modified CFNetServiceBrowserGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceBrowserInvalidate(CFNetServiceBrowser!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceBrowserScheduleWithRunLoop(CFNetServiceBrowser!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser!, Boolean, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser!, _ registrationDomains: Boolean, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceBrowserSearchForDomains(_ browser: CFNetServiceBrowser!, _ registrationDomains: Boolean, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.2 |

Modified CFNetServiceBrowserSearchForServices(CFNetServiceBrowser!, CFString!, CFString!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser!, _ domain: CFString!, _ serviceType: CFString!, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceBrowserSearchForServices(_ browser: CFNetServiceBrowser!, _ domain: CFString!, _ serviceType: CFString!, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.2 |

Modified CFNetServiceBrowserStopSearch(CFNetServiceBrowser!, UnsafeMutablePointer<CFStreamError>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser!, _ error: UnsafePointer<CFStreamError>) ``` | OS X 10.10 |
| To | ``` func CFNetServiceBrowserStopSearch(_ browser: CFNetServiceBrowser!, _ error: UnsafeMutablePointer<CFStreamError>) ``` | OS X 10.2 |

Modified CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceCancel(CFNetService!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceClientCallBack = CFunctionPointer<((CFNetService!, UnsafePointer<CFStreamError>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFNetServiceClientCallBack = CFunctionPointer<((CFNetService!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFNetServiceCreate(CFAllocator!, CFString!, CFString!, CFString!, Int32) -> Unmanaged<CFNetService>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceCreateCopy(CFAllocator!, CFNetService!) -> Unmanaged<CFNetService>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFNetServiceCreateDictionaryWithTXTData(CFAllocator!, CFData!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceCreateTXTDataWithDictionary(CFAllocator!, CFDictionary!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceGetAddressing(CFNetService!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceGetDomain(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceGetName(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceGetPortNumber(CFNetService!) -> Int32

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFNetServiceGetTXTData(CFNetService!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceGetTargetHost(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceGetType(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceMonitorClientCallBack

|  | Declaration |
| --- | --- |
| From | ``` typealias CFNetServiceMonitorClientCallBack = CFunctionPointer<((CFNetServiceMonitor!, CFNetService!, CFNetServiceMonitorType, CFData!, UnsafePointer<CFStreamError>, UnsafePointer<()>) -> Void)> ``` |
| To | ``` typealias CFNetServiceMonitorClientCallBack = CFunctionPointer<((CFNetServiceMonitor!, CFNetService!, CFNetServiceMonitorType, CFData!, UnsafeMutablePointer<CFStreamError>, UnsafeMutablePointer<Void>) -> Void)> ``` |

Modified CFNetServiceMonitorCreate(CFAllocator!, CFNetService!, CFNetServiceMonitorClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator!, _ theService: CFNetService!, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>! ``` | OS X 10.10 |
| To | ``` func CFNetServiceMonitorCreate(_ alloc: CFAllocator!, _ theService: CFNetService!, _ clientCB: CFNetServiceMonitorClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>! ``` | OS X 10.4 |

Modified CFNetServiceMonitorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceMonitorInvalidate(CFNetServiceMonitor!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceMonitorScheduleWithRunLoop(CFNetServiceMonitor!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceMonitorStart(CFNetServiceMonitor!, CFNetServiceMonitorType, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor!, _ recordType: CFNetServiceMonitorType, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceMonitorStart(_ monitor: CFNetServiceMonitor!, _ recordType: CFNetServiceMonitorType, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.4 |

Modified CFNetServiceMonitorStop(CFNetServiceMonitor!, UnsafeMutablePointer<CFStreamError>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor!, _ error: UnsafePointer<CFStreamError>) ``` | OS X 10.10 |
| To | ``` func CFNetServiceMonitorStop(_ monitor: CFNetServiceMonitor!, _ error: UnsafeMutablePointer<CFStreamError>) ``` | OS X 10.4 |

Modified CFNetServiceMonitorUnscheduleFromRunLoop(CFNetServiceMonitor!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceRegisterWithOptions(CFNetService!, CFOptionFlags, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService!, _ options: CFOptionFlags, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceRegisterWithOptions(_ theService: CFNetService!, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.4 |

Modified CFNetServiceResolveWithTimeout(CFNetService!, CFTimeInterval, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService!, _ timeout: CFTimeInterval, _ error: UnsafePointer<CFStreamError>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceResolveWithTimeout(_ theService: CFNetService!, _ timeout: CFTimeInterval, _ error: UnsafeMutablePointer<CFStreamError>) -> Boolean ``` | OS X 10.4 |

Modified CFNetServiceScheduleWithRunLoop(CFNetService!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetServiceSetClient(CFNetService!, CFNetServiceClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Boolean

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetServiceSetClient(_ theService: CFNetService!, _ clientCB: CFNetServiceClientCallBack, _ clientContext: UnsafePointer<CFNetServiceClientContext>) -> Boolean ``` | OS X 10.10 |
| To | ``` func CFNetServiceSetClient(_ theService: CFNetService!, _ clientCB: CFNetServiceClientCallBack, _ clientContext: UnsafeMutablePointer<CFNetServiceClientContext>) -> Boolean ``` | OS X 10.2 |

Modified CFNetServiceSetTXTData(CFNetService!, CFData!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified CFNetServiceUnscheduleFromRunLoop(CFNetService!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFNetworkCopyProxiesForAutoConfigurationScript(CFString!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ error: UnsafePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.10 |
| To | ``` func CFNetworkCopyProxiesForAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>! ``` | OS X 10.5 |

Modified CFNetworkCopyProxiesForURL(CFURL!, CFDictionary!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified CFNetworkExecuteProxyAutoConfigurationScript(CFString!, CFURL!, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10 |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationScript(_ proxyAutoConfigurationScript: CFString!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.5 |

Modified CFNetworkExecuteProxyAutoConfigurationURL(CFURL!, CFURL!, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>!

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.10 |
| To | ``` func CFNetworkExecuteProxyAutoConfigurationURL(_ proxyAutoConfigURL: CFURL!, _ targetURL: CFURL!, _ cb: CFProxyAutoConfigurationResultCallback, _ clientContext: UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>! ``` | OS X 10.5 |

Modified CFProxyAutoConfigurationResultCallback

|  | Declaration |
| --- | --- |
| From | ``` typealias CFProxyAutoConfigurationResultCallback = CFunctionPointer<((UnsafePointer<()>, CFArray!, CFError!) -> Void)> ``` |
| To | ``` typealias CFProxyAutoConfigurationResultCallback = CFunctionPointer<((UnsafeMutablePointer<Void>, CFArray!, CFError!) -> Void)> ``` |

Modified CFReadStreamCreateForHTTPRequest(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified CFReadStreamCreateForStreamedHTTPRequest(CFAllocator!, CFHTTPMessage!, CFReadStream!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified CFReadStreamCreateWithFTPURL(CFAllocator!, CFURL!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified CFSocketStreamSOCKSGetError(UnsafePointer<CFStreamError>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketStreamSOCKSGetError(_ error: ConstUnsafePointer<CFStreamError>) -> Int32 ``` |
| To | ``` func CFSocketStreamSOCKSGetError(_ error: UnsafePointer<CFStreamError>) -> Int32 ``` |

Modified CFSocketStreamSOCKSGetErrorSubdomain(UnsafePointer<CFStreamError>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func CFSocketStreamSOCKSGetErrorSubdomain(_ error: ConstUnsafePointer<CFStreamError>) -> Int32 ``` |
| To | ``` func CFSocketStreamSOCKSGetErrorSubdomain(_ error: UnsafePointer<CFStreamError>) -> Int32 ``` |

Modified CFStreamCreatePairWithSocketToCFHost(CFAllocator!, CFHost!, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator!, _ host: CFHost!, _ port: Int32, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>) ``` | OS X 10.10 |
| To | ``` func CFStreamCreatePairWithSocketToCFHost(_ alloc: CFAllocator!, _ host: CFHost!, _ port: Int32, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` | OS X 10.3 |

Modified CFStreamCreatePairWithSocketToNetService(CFAllocator!, CFNetService!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator!, _ service: CFNetService!, _ readStream: UnsafePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafePointer<Unmanaged<CFWriteStream>?>) ``` | OS X 10.10 |
| To | ``` func CFStreamCreatePairWithSocketToNetService(_ alloc: CFAllocator!, _ service: CFNetService!, _ readStream: UnsafeMutablePointer<Unmanaged<CFReadStream>?>, _ writeStream: UnsafeMutablePointer<Unmanaged<CFWriteStream>?>) ``` | OS X 10.3 |

Modified CFWriteStreamCreateWithFTPURL(CFAllocator!, CFURL!) -> Unmanaged<CFWriteStream>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFDNSServiceFailureKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainCFNetwork

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFErrorDomainWinSock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFFTPResourceGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceLink

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceModDate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceOwner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPResourceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFFTPStatusCodeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFGetAddrInfoFailureKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFHTTPAuthenticationAccountDomain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFHTTPAuthenticationPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFHTTPAuthenticationSchemeBasic

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFHTTPAuthenticationSchemeDigest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFHTTPAuthenticationSchemeKerberos

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFHTTPAuthenticationSchemeNTLM

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFHTTPAuthenticationSchemeNegotiate

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFHTTPAuthenticationSchemeNegotiate2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFHTTPAuthenticationSchemeOAuth1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFHTTPAuthenticationSchemeXMobileMeAuthToken

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFHTTPAuthenticationUsername

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFHTTPVersion1_0

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kCFHTTPVersion1_1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kCFNetworkProxiesExceptionsList

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesExcludeSimpleHostnames

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesFTPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesFTPPassive

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesFTPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesFTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesGopherEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesGopherPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesGopherProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPSEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPSPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesHTTPSProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesProxyAutoConfigEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesProxyAutoConfigJavaScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFNetworkProxiesProxyAutoConfigURLString

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesProxyAutoDiscoveryEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesRTSPEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesRTSPPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesRTSPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesSOCKSEnable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesSOCKSPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFNetworkProxiesSOCKSProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kCFProxyAutoConfigurationHTTPResponseKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyAutoConfigurationJavaScriptKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFProxyAutoConfigurationURLKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyHostNameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyPasswordKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyPortNumberKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeAutoConfigurationJavaScript

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFProxyTypeAutoConfigurationURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeFTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeHTTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeHTTPS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyTypeSOCKS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFProxyUsernameKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFSOCKSNegotiationMethodKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFSOCKSStatusCodeKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFSOCKSVersionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFStreamErrorDomainFTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamErrorDomainHTTP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kCFStreamErrorDomainMach

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamErrorDomainNetDB

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamErrorDomainNetServices

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamErrorDomainSOCKS

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.0 |

Modified kCFStreamErrorDomainSSL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamErrorDomainSystemConfiguration

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamErrorDomainWinSock

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFStreamNetworkServiceType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFStreamNetworkServiceTypeBackground

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFStreamNetworkServiceTypeVideo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFStreamNetworkServiceTypeVoIP

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFStreamNetworkServiceTypeVoice

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified kCFStreamPropertyConnectionIsCellular

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCFStreamPropertyFTPAttemptPersistentConnection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPFetchResourceInfo

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPFileTransferOffset

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPProxyHost

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPProxyPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPProxyPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPProxyUser

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPResourceSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPUsePassiveMode

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyFTPUserName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyHTTPAttemptPersistentConnection

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPFinalRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFStreamPropertyHTTPFinalURL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPProxyHost

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPProxyPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPRequestBytesWrittenCount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertyHTTPResponseHeader

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.1 |

Modified kCFStreamPropertyHTTPSProxyHost

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPSProxyPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyHTTPShouldAutoredirect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertyNoCellular

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified kCFStreamPropertyProxyLocalBypass

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamPropertySOCKSPassword

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySOCKSProxy

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySOCKSProxyHost

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySOCKSProxyPort

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySOCKSUser

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySOCKSVersion

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySSLContext

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified kCFStreamPropertySSLPeerTrust

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFStreamPropertySSLSettings

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamPropertyShouldCloseNativeSocket

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamPropertySocketRemoteHost

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertySocketRemoteNetService

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.3 |

Modified kCFStreamPropertySocketSecurityLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSSLCertificates

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamSSLIsServer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamSSLLevel

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamSSLPeerName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamSSLValidatesCertificateChain

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.4 |

Modified kCFStreamSocketSOCKSVersion4

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSOCKSVersion5

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSecurityLevelNegotiatedSSL

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSecurityLevelNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSecurityLevelSSLv2

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSecurityLevelSSLv3

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFStreamSocketSecurityLevelTLSv1

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.2 |

Modified kCFURLErrorFailingURLErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified kCFURLErrorFailingURLStringErrorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

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
