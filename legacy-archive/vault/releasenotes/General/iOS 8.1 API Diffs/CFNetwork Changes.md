---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/CFNetwork.html
archived_at: '2026-07-18T02:56:07.776154Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# CFNetwork Changes

## CFNetwork

Removed CFNetServiceBrowserFlags.valueRemoved CFNetServiceRegisterFlags.valueAdded CFNetServiceBrowserFlags.init(rawValue: CFOptionFlags)Added CFNetServiceRegisterFlags.init(rawValue: CFOptionFlags)Modified CFNetServiceBrowserFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFNetServiceBrowserFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` |
| To | ``` struct CFNetServiceBrowserFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var MoreComing: CFNetServiceBrowserFlags { get }     static var IsDomain: CFNetServiceBrowserFlags { get }     static var IsDefault: CFNetServiceBrowserFlags { get }     static var IsRegistrationDomain: CFNetServiceBrowserFlags { get }     static var Remove: CFNetServiceBrowserFlags { get } } ``` |

Modified CFNetServiceBrowserFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFNetServiceRegisterFlags [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFNetServiceRegisterFlags : RawOptionSetType {     init(_ value: CFOptionFlags)     var value: CFOptionFlags     static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } } ``` |
| To | ``` struct CFNetServiceRegisterFlags : RawOptionSetType {     init(_ rawValue: CFOptionFlags)     init(rawValue rawValue: CFOptionFlags)     static var FlagNoAutoRename: CFNetServiceRegisterFlags { get } } ``` |

Modified CFNetServiceRegisterFlags.init(_: CFOptionFlags)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: CFOptionFlags) ``` |
| To | ``` init(_ rawValue: CFOptionFlags) ``` |

Modified CFFTPCreateParsedResourceListing(CFAllocator!, UnsafePointer<UInt8>, CFIndex, UnsafeMutablePointer<Unmanaged<CFDictionary>?>) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationAppliesToRequest(CFHTTPAuthentication!, CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationCopyDomains(CFHTTPAuthentication!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationCopyMethod(CFHTTPAuthentication!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationCopyRealm(CFHTTPAuthentication!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationCreateFromResponse(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFHTTPAuthentication>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationIsValid(CFHTTPAuthentication!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationRequiresAccountDomain(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationRequiresOrderedRequests(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPAuthenticationRequiresUserNameAndPassword(CFHTTPAuthentication!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageAddAuthentication(CFHTTPMessage!, CFHTTPMessage!, CFString!, CFString!, CFString!, Boolean) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageAppendBytes(CFHTTPMessage!, UnsafePointer<UInt8>, CFIndex) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageApplyCredentialDictionary(CFHTTPMessage!, CFHTTPAuthentication!, CFDictionary!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageApplyCredentials(CFHTTPMessage!, CFHTTPAuthentication!, CFString!, CFString!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyAllHeaderFields(CFHTTPMessage!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyBody(CFHTTPMessage!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyHeaderFieldValue(CFHTTPMessage!, CFString!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyRequestMethod(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyRequestURL(CFHTTPMessage!) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyResponseStatusLine(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopySerializedMessage(CFHTTPMessage!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCopyVersion(CFHTTPMessage!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCreateCopy(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCreateEmpty(CFAllocator!, Boolean) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCreateRequest(CFAllocator!, CFString!, CFURL!, CFString!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageCreateResponse(CFAllocator!, CFIndex, CFString!, CFString!) -> Unmanaged<CFHTTPMessage>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageGetResponseStatusCode(CFHTTPMessage!) -> CFIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageIsHeaderComplete(CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageIsRequest(CFHTTPMessage!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageSetBody(CFHTTPMessage!, CFData!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHTTPMessageSetHeaderFieldValue(CFHTTPMessage!, CFString!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostCancelInfoResolution(CFHost!, CFHostInfoType)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostCreateCopy(CFAllocator!, CFHost!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostCreateWithAddress(CFAllocator!, CFData!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostCreateWithName(CFAllocator!, CFString!) -> Unmanaged<CFHost>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostGetAddressing(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostGetNames(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostGetReachability(CFHost!, UnsafeMutablePointer<Boolean>) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostScheduleWithRunLoop(CFHost!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostSetClient(CFHost!, CFHostClientCallBack, UnsafeMutablePointer<CFHostClientContext>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostStartInfoResolution(CFHost!, CFHostInfoType, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFHostUnscheduleFromRunLoop(CFHost!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetDiagnosticCopyNetworkStatusPassively(CFNetDiagnostic!, UnsafeMutablePointer<Unmanaged<CFString>?>) -> CFNetDiagnosticStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetDiagnosticCreateWithStreams(CFAllocator!, CFReadStream!, CFWriteStream!) -> Unmanaged<CFNetDiagnostic>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetDiagnosticCreateWithURL(CFAllocator!, CFURL!) -> Unmanaged<CFNetDiagnostic>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetDiagnosticDiagnoseProblemInteractively(CFNetDiagnostic!) -> CFNetDiagnosticStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetDiagnosticSetName(CFNetDiagnostic!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserCreate(CFAllocator!, CFNetServiceBrowserClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceBrowser>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserInvalidate(CFNetServiceBrowser!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserScheduleWithRunLoop(CFNetServiceBrowser!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserSearchForDomains(CFNetServiceBrowser!, Boolean, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserSearchForServices(CFNetServiceBrowser!, CFString!, CFString!, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserStopSearch(CFNetServiceBrowser!, UnsafeMutablePointer<CFStreamError>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceBrowserUnscheduleFromRunLoop(CFNetServiceBrowser!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceCancel(CFNetService!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceCreate(CFAllocator!, CFString!, CFString!, CFString!, Int32) -> Unmanaged<CFNetService>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceCreateCopy(CFAllocator!, CFNetService!) -> Unmanaged<CFNetService>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceCreateDictionaryWithTXTData(CFAllocator!, CFData!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceCreateTXTDataWithDictionary(CFAllocator!, CFDictionary!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetAddressing(CFNetService!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetDomain(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetName(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetPortNumber(CFNetService!) -> Int32

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetTXTData(CFNetService!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetTargetHost(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetType(CFNetService!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorCreate(CFAllocator!, CFNetService!, CFNetServiceMonitorClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Unmanaged<CFNetServiceMonitor>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorGetTypeID() -> CFTypeID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorInvalidate(CFNetServiceMonitor!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorScheduleWithRunLoop(CFNetServiceMonitor!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorStart(CFNetServiceMonitor!, CFNetServiceMonitorType, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorStop(CFNetServiceMonitor!, UnsafeMutablePointer<CFStreamError>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceMonitorUnscheduleFromRunLoop(CFNetServiceMonitor!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceRegisterWithOptions(CFNetService!, CFOptionFlags, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceResolveWithTimeout(CFNetService!, CFTimeInterval, UnsafeMutablePointer<CFStreamError>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceScheduleWithRunLoop(CFNetService!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceSetClient(CFNetService!, CFNetServiceClientCallBack, UnsafeMutablePointer<CFNetServiceClientContext>) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceSetTXTData(CFNetService!, CFData!) -> Boolean

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetServiceUnscheduleFromRunLoop(CFNetService!, CFRunLoop!, CFString!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetworkCopyProxiesForAutoConfigurationScript(CFString!, CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetworkCopyProxiesForURL(CFURL!, CFDictionary!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetworkCopySystemProxySettings() -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetworkExecuteProxyAutoConfigurationScript(CFString!, CFURL!, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFNetworkExecuteProxyAutoConfigurationURL(CFURL!, CFURL!, CFProxyAutoConfigurationResultCallback, UnsafeMutablePointer<CFStreamClientContext>) -> Unmanaged<CFRunLoopSource>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFReadStreamCreateForHTTPRequest(CFAllocator!, CFHTTPMessage!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFReadStreamCreateForStreamedHTTPRequest(CFAllocator!, CFHTTPMessage!, CFReadStream!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFReadStreamCreateWithFTPURL(CFAllocator!, CFURL!) -> Unmanaged<CFReadStream>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStreamCreatePairWithSocketToCFHost(CFAllocator!, CFHost!, Int32, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFStreamCreatePairWithSocketToNetService(CFAllocator!, CFNetService!, UnsafeMutablePointer<Unmanaged<CFReadStream>?>, UnsafeMutablePointer<Unmanaged<CFWriteStream>?>)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CFWriteStreamCreateWithFTPURL(CFAllocator!, CFURL!) -> Unmanaged<CFWriteStream>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFDNSServiceFailureKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainCFNetwork

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFErrorDomainWinSock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceLink

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceModDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceOwner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPResourceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFFTPStatusCodeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFGetAddrInfoFailureKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationAccountDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeBasic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeDigest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeKerberos

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeNTLM

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeNegotiate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPAuthenticationSchemeNegotiate2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCFHTTPAuthenticationSchemeOAuth1

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kCFHTTPAuthenticationSchemeXMobileMeAuthToken

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.3 |

Modified kCFHTTPAuthenticationUsername

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPVersion1_0

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFHTTPVersion1_1

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNetworkProxiesHTTPEnable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNetworkProxiesHTTPPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNetworkProxiesHTTPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNetworkProxiesProxyAutoConfigEnable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFNetworkProxiesProxyAutoConfigJavaScript

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCFNetworkProxiesProxyAutoConfigURLString

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyAutoConfigurationHTTPResponseKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyAutoConfigurationJavaScriptKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCFProxyAutoConfigurationURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyHostNameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyPasswordKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyPortNumberKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeAutoConfigurationJavaScript

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCFProxyTypeAutoConfigurationURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeFTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeHTTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeHTTPS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyTypeSOCKS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFProxyUsernameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFSOCKSNegotiationMethodKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFSOCKSStatusCodeKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFSOCKSVersionKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainFTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainHTTP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainMach

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainNetDB

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainNetServices

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainSOCKS

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainSSL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainSystemConfiguration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamErrorDomainWinSock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamNetworkServiceType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFStreamNetworkServiceTypeBackground

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFStreamNetworkServiceTypeVideo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFStreamNetworkServiceTypeVoIP

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCFStreamNetworkServiceTypeVoice

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFStreamPropertyConnectionIsCellular

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kCFStreamPropertyFTPAttemptPersistentConnection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPFetchResourceInfo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPFileTransferOffset

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPProxyHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPProxyPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPProxyPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPProxyUser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPResourceSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPUsePassiveMode

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyFTPUserName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPAttemptPersistentConnection

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPFinalRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPFinalURL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPProxyHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPProxyPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPRequestBytesWrittenCount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPResponseHeader

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPSProxyHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPSProxyPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyHTTPShouldAutoredirect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyNoCellular

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFStreamPropertyProxyLocalBypass

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSPassword

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSProxy

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSProxyHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSProxyPort

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSUser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySOCKSVersion

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySSLContext

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCFStreamPropertySSLPeerTrust

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySSLSettings

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertyShouldCloseNativeSocket

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySocketRemoteHost

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySocketRemoteNetService

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamPropertySocketSecurityLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSSLCertificates

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSSLIsServer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSSLLevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSSLPeerName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSSLValidatesCertificateChain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSOCKSVersion4

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSOCKSVersion5

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSecurityLevelNegotiatedSSL

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSecurityLevelNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSecurityLevelSSLv2

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSecurityLevelSSLv3

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFStreamSocketSecurityLevelTLSv1

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCFURLErrorFailingURLErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

Modified kCFURLErrorFailingURLStringErrorKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.2 |

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
