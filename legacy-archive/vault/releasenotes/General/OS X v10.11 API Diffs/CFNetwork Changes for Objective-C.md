---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CFNetwork.html
archived_at: '2026-07-18T02:52:56.343826Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CFNetwork Changes for Objective-C

### CFNetwork

#### CFFTPStream.h

Modified [CFFTPCreateParsedResourceListing()](https://developer.apple.com/documentation/cfnetwork/1426546-cfftpcreateparsedresourcelisting)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CFIndex CFFTPCreateParsedResourceListing (     CFAllocatorRef alloc,     const UInt8 *buffer,     CFIndex bufferLength,     CFDictionaryRef *parsed ); ``` | -- |
| To | ``` CFIndex CFFTPCreateParsedResourceListing (     CFAllocatorRef _Nullable alloc,     const UInt8 * _Nonnull buffer,     CFIndex bufferLength,     CFDictionaryRef  _Nullable * _Nullable parsed ); ``` | OS X 10.11 |

Modified [CFReadStreamCreateWithFTPURL()](https://developer.apple.com/documentation/cfnetwork/1426792-cfreadstreamcreatewithftpurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CFReadStreamRef CFReadStreamCreateWithFTPURL (     CFAllocatorRef alloc,     CFURLRef ftpURL ); ``` | -- |
| To | ``` CFReadStreamRef _Nonnull CFReadStreamCreateWithFTPURL (     CFAllocatorRef _Nullable alloc,     CFURLRef _Nonnull ftpURL ); ``` | OS X 10.11 |

Modified [CFWriteStreamCreateWithFTPURL()](https://developer.apple.com/documentation/cfnetwork/1426626-cfwritestreamcreatewithftpurl)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CFWriteStreamRef CFWriteStreamCreateWithFTPURL (     CFAllocatorRef alloc,     CFURLRef ftpURL ); ``` | -- |
| To | ``` CFWriteStreamRef _Nonnull CFWriteStreamCreateWithFTPURL (     CFAllocatorRef _Nullable alloc,     CFURLRef _Nonnull ftpURL ); ``` | OS X 10.11 |

Modified [kCFFTPResourceGroup](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcegroup)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceLink](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcelink)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceModDate](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemoddate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceMode](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcemode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceName](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcename)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceOwner](https://developer.apple.com/documentation/cfnetwork/kcfftpresourceowner)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceSize](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcesize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFFTPResourceType](https://developer.apple.com/documentation/cfnetwork/kcfftpresourcetype)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPAttemptPersistentConnection](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpattemptpersistentconnection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPFetchResourceInfo](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpfetchresourceinfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPFileTransferOffset](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpfiletransferoffset)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPPassword](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftppassword)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyhost)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyPassword](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxypassword)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyport)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPProxyUser](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpproxyuser)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPResourceSize](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpresourcesize)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPUsePassiveMode](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusepassivemode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyFTPUserName](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyftpusername)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CFHost.h

Modified [CFHostCancelInfoResolution()](https://developer.apple.com/documentation/cfnetwork/1426691-cfhostcancelinforesolution)

|  | Declaration |
| --- | --- |
| From | ``` void CFHostCancelInfoResolution (     CFHostRef theHost,     CFHostInfoType info ); ``` |
| To | ``` void CFHostCancelInfoResolution (     CFHostRef _Nonnull theHost,     CFHostInfoType info ); ``` |

Modified [CFHostCreateCopy()](https://developer.apple.com/documentation/cfnetwork/1426854-cfhostcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CFHostRef CFHostCreateCopy (     CFAllocatorRef alloc,     CFHostRef host ); ``` |
| To | ``` CFHostRef _Nonnull CFHostCreateCopy (     CFAllocatorRef _Nullable alloc,     CFHostRef _Nonnull host ); ``` |

Modified [CFHostCreateWithAddress()](https://developer.apple.com/documentation/cfnetwork/1426421-cfhostcreatewithaddress)

|  | Declaration |
| --- | --- |
| From | ``` CFHostRef CFHostCreateWithAddress (     CFAllocatorRef allocator,     CFDataRef addr ); ``` |
| To | ``` CFHostRef _Nonnull CFHostCreateWithAddress (     CFAllocatorRef _Nullable allocator,     CFDataRef _Nonnull addr ); ``` |

Modified [CFHostCreateWithName()](https://developer.apple.com/documentation/cfnetwork/1426488-cfhostcreatewithname)

|  | Declaration |
| --- | --- |
| From | ``` CFHostRef CFHostCreateWithName (     CFAllocatorRef allocator,     CFStringRef hostname ); ``` |
| To | ``` CFHostRef _Nonnull CFHostCreateWithName (     CFAllocatorRef _Nullable allocator,     CFStringRef _Nonnull hostname ); ``` |

Modified [CFHostGetAddressing()](https://developer.apple.com/documentation/cfnetwork/1426861-cfhostgetaddressing)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFHostGetAddressing (     CFHostRef theHost,     Boolean *hasBeenResolved ); ``` |
| To | ``` CFArrayRef _Nullable CFHostGetAddressing (     CFHostRef _Nonnull theHost,     Boolean * _Nullable hasBeenResolved ); ``` |

Modified [CFHostGetNames()](https://developer.apple.com/documentation/cfnetwork/1426909-cfhostgetnames)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFHostGetNames (     CFHostRef theHost,     Boolean *hasBeenResolved ); ``` |
| To | ``` CFArrayRef _Nullable CFHostGetNames (     CFHostRef _Nonnull theHost,     Boolean * _Nullable hasBeenResolved ); ``` |

Modified [CFHostGetReachability()](https://developer.apple.com/documentation/cfnetwork/1426531-cfhostgetreachability)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CFHostGetReachability (     CFHostRef theHost,     Boolean *hasBeenResolved ); ``` |
| To | ``` CFDataRef _Nullable CFHostGetReachability (     CFHostRef _Nonnull theHost,     Boolean * _Nullable hasBeenResolved ); ``` |

Modified [CFHostScheduleWithRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426596-cfhostschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void CFHostScheduleWithRunLoop (     CFHostRef theHost,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFHostScheduleWithRunLoop (     CFHostRef _Nonnull theHost,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFHostSetClient()](https://developer.apple.com/documentation/cfnetwork/1426540-cfhostsetclient)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHostSetClient (     CFHostRef theHost,     CFHostClientCallBack clientCB,     CFHostClientContext *clientContext ); ``` |
| To | ``` Boolean CFHostSetClient (     CFHostRef _Nonnull theHost,     CFHostClientCallBack _Nullable clientCB,     CFHostClientContext * _Nullable clientContext ); ``` |

Modified [CFHostStartInfoResolution()](https://developer.apple.com/documentation/cfnetwork/1426672-cfhoststartinforesolution)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHostStartInfoResolution (     CFHostRef theHost,     CFHostInfoType info,     CFStreamError *error ); ``` |
| To | ``` Boolean CFHostStartInfoResolution (     CFHostRef _Nonnull theHost,     CFHostInfoType info,     CFStreamError * _Nullable error ); ``` |

Modified [CFHostUnscheduleFromRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426425-cfhostunschedulefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void CFHostUnscheduleFromRunLoop (     CFHostRef theHost,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFHostUnscheduleFromRunLoop (     CFHostRef _Nonnull theHost,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### CFHTTPAuthentication.h

Modified [CFHTTPAuthenticationAppliesToRequest()](https://developer.apple.com/documentation/cfnetwork/1426544-cfhttpauthenticationappliestoreq)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPAuthenticationAppliesToRequest (     CFHTTPAuthenticationRef auth,     CFHTTPMessageRef request ); ``` |
| To | ``` Boolean CFHTTPAuthenticationAppliesToRequest (     CFHTTPAuthenticationRef _Nonnull auth,     CFHTTPMessageRef _Nonnull request ); ``` |

Modified [CFHTTPAuthenticationCopyDomains()](https://developer.apple.com/documentation/cfnetwork/1426456-cfhttpauthenticationcopydomains)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFHTTPAuthenticationCopyDomains (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` CFArrayRef _Nonnull CFHTTPAuthenticationCopyDomains (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPAuthenticationCopyMethod()](https://developer.apple.com/documentation/cfnetwork/1426688-cfhttpauthenticationcopymethod)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPAuthenticationCopyMethod (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` CFStringRef _Nonnull CFHTTPAuthenticationCopyMethod (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPAuthenticationCopyRealm()](https://developer.apple.com/documentation/cfnetwork/1426624-cfhttpauthenticationcopyrealm)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPAuthenticationCopyRealm (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` CFStringRef _Nonnull CFHTTPAuthenticationCopyRealm (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPAuthenticationCreateFromResponse()](https://developer.apple.com/documentation/cfnetwork/1426594-cfhttpauthenticationcreatefromre)

|  | Declaration |
| --- | --- |
| From | ``` CFHTTPAuthenticationRef CFHTTPAuthenticationCreateFromResponse (     CFAllocatorRef alloc,     CFHTTPMessageRef response ); ``` |
| To | ``` CFHTTPAuthenticationRef _Nonnull CFHTTPAuthenticationCreateFromResponse (     CFAllocatorRef _Nullable alloc,     CFHTTPMessageRef _Nonnull response ); ``` |

Modified [CFHTTPAuthenticationIsValid()](https://developer.apple.com/documentation/cfnetwork/1426694-cfhttpauthenticationisvalid)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPAuthenticationIsValid (     CFHTTPAuthenticationRef auth,     CFStreamError *error ); ``` |
| To | ``` Boolean CFHTTPAuthenticationIsValid (     CFHTTPAuthenticationRef _Nonnull auth,     CFStreamError * _Nullable error ); ``` |

Modified [CFHTTPAuthenticationRequiresAccountDomain()](https://developer.apple.com/documentation/cfnetwork/1426760-cfhttpauthenticationrequiresacco)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPAuthenticationRequiresAccountDomain (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` Boolean CFHTTPAuthenticationRequiresAccountDomain (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPAuthenticationRequiresOrderedRequests()](https://developer.apple.com/documentation/cfnetwork/1426505-cfhttpauthenticationrequiresorde)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPAuthenticationRequiresOrderedRequests (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` Boolean CFHTTPAuthenticationRequiresOrderedRequests (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPAuthenticationRequiresUserNameAndPassword()](https://developer.apple.com/documentation/cfnetwork/1426849-cfhttpauthenticationrequiresuser)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPAuthenticationRequiresUserNameAndPassword (     CFHTTPAuthenticationRef auth ); ``` |
| To | ``` Boolean CFHTTPAuthenticationRequiresUserNameAndPassword (     CFHTTPAuthenticationRef _Nonnull auth ); ``` |

Modified [CFHTTPMessageApplyCredentialDictionary()](https://developer.apple.com/documentation/cfnetwork/1426625-cfhttpmessageapplycredentialdict)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageApplyCredentialDictionary (     CFHTTPMessageRef request,     CFHTTPAuthenticationRef auth,     CFDictionaryRef dict,     CFStreamError *error ); ``` |
| To | ``` Boolean CFHTTPMessageApplyCredentialDictionary (     CFHTTPMessageRef _Nonnull request,     CFHTTPAuthenticationRef _Nonnull auth,     CFDictionaryRef _Nonnull dict,     CFStreamError * _Nullable error ); ``` |

Modified [CFHTTPMessageApplyCredentials()](https://developer.apple.com/documentation/cfnetwork/1426525-cfhttpmessageapplycredentials)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageApplyCredentials (     CFHTTPMessageRef request,     CFHTTPAuthenticationRef auth,     CFStringRef username,     CFStringRef password,     CFStreamError *error ); ``` |
| To | ``` Boolean CFHTTPMessageApplyCredentials (     CFHTTPMessageRef _Nonnull request,     CFHTTPAuthenticationRef _Nonnull auth,     CFStringRef _Nullable username,     CFStringRef _Nullable password,     CFStreamError * _Nullable error ); ``` |

#### CFHTTPMessage.h

Added [kCFHTTPVersion2_0](https://developer.apple.com/documentation/cfnetwork/kcfhttpversion2_0)Modified [CFHTTPMessageAddAuthentication()](https://developer.apple.com/documentation/cfnetwork/1387294-cfhttpmessageaddauthentication)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageAddAuthentication (     CFHTTPMessageRef request,     CFHTTPMessageRef authenticationFailureResponse,     CFStringRef username,     CFStringRef password,     CFStringRef authenticationScheme,     Boolean forProxy ); ``` |
| To | ``` Boolean CFHTTPMessageAddAuthentication (     CFHTTPMessageRef _Nonnull request,     CFHTTPMessageRef _Nullable authenticationFailureResponse,     CFStringRef _Nonnull username,     CFStringRef _Nonnull password,     CFStringRef _Nullable authenticationScheme,     Boolean forProxy ); ``` |

Modified [CFHTTPMessageAppendBytes()](https://developer.apple.com/documentation/cfnetwork/1387288-cfhttpmessageappendbytes)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageAppendBytes (     CFHTTPMessageRef message,     const UInt8 *newBytes,     CFIndex numBytes ); ``` |
| To | ``` Boolean CFHTTPMessageAppendBytes (     CFHTTPMessageRef _Nonnull message,     const UInt8 * _Nonnull newBytes,     CFIndex numBytes ); ``` |

Modified [CFHTTPMessageCopyAllHeaderFields()](https://developer.apple.com/documentation/cfnetwork/1387311-cfhttpmessagecopyallheaderfields)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CFHTTPMessageCopyAllHeaderFields (     CFHTTPMessageRef message ); ``` |
| To | ``` CFDictionaryRef _Nullable CFHTTPMessageCopyAllHeaderFields (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageCopyBody()](https://developer.apple.com/documentation/cfnetwork/1387262-cfhttpmessagecopybody)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CFHTTPMessageCopyBody (     CFHTTPMessageRef message ); ``` |
| To | ``` CFDataRef _Nullable CFHTTPMessageCopyBody (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageCopyHeaderFieldValue()](https://developer.apple.com/documentation/cfnetwork/1387300-cfhttpmessagecopyheaderfieldvalu)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPMessageCopyHeaderFieldValue (     CFHTTPMessageRef message,     CFStringRef headerField ); ``` |
| To | ``` CFStringRef _Nullable CFHTTPMessageCopyHeaderFieldValue (     CFHTTPMessageRef _Nonnull message,     CFStringRef _Nonnull headerField ); ``` |

Modified [CFHTTPMessageCopyRequestMethod()](https://developer.apple.com/documentation/cfnetwork/1387270-cfhttpmessagecopyrequestmethod)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPMessageCopyRequestMethod (     CFHTTPMessageRef request ); ``` |
| To | ``` CFStringRef _Nullable CFHTTPMessageCopyRequestMethod (     CFHTTPMessageRef _Nonnull request ); ``` |

Modified [CFHTTPMessageCopyRequestURL()](https://developer.apple.com/documentation/cfnetwork/1387280-cfhttpmessagecopyrequesturl)

|  | Declaration |
| --- | --- |
| From | ``` CFURLRef CFHTTPMessageCopyRequestURL (     CFHTTPMessageRef request ); ``` |
| To | ``` CFURLRef _Nullable CFHTTPMessageCopyRequestURL (     CFHTTPMessageRef _Nonnull request ); ``` |

Modified [CFHTTPMessageCopyResponseStatusLine()](https://developer.apple.com/documentation/cfnetwork/1387296-cfhttpmessagecopyresponsestatusl)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPMessageCopyResponseStatusLine (     CFHTTPMessageRef response ); ``` |
| To | ``` CFStringRef _Nullable CFHTTPMessageCopyResponseStatusLine (     CFHTTPMessageRef _Nonnull response ); ``` |

Modified [CFHTTPMessageCopySerializedMessage()](https://developer.apple.com/documentation/cfnetwork/1387278-cfhttpmessagecopyserializedmessa)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CFHTTPMessageCopySerializedMessage (     CFHTTPMessageRef message ); ``` |
| To | ``` CFDataRef _Nullable CFHTTPMessageCopySerializedMessage (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageCopyVersion()](https://developer.apple.com/documentation/cfnetwork/1387273-cfhttpmessagecopyversion)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFHTTPMessageCopyVersion (     CFHTTPMessageRef message ); ``` |
| To | ``` CFStringRef _Nonnull CFHTTPMessageCopyVersion (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageCreateCopy()](https://developer.apple.com/documentation/cfnetwork/1387266-cfhttpmessagecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CFHTTPMessageRef CFHTTPMessageCreateCopy (     CFAllocatorRef alloc,     CFHTTPMessageRef message ); ``` |
| To | ``` CFHTTPMessageRef _Nonnull CFHTTPMessageCreateCopy (     CFAllocatorRef _Nullable alloc,     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageCreateEmpty()](https://developer.apple.com/documentation/cfnetwork/1387318-cfhttpmessagecreateempty)

|  | Declaration |
| --- | --- |
| From | ``` CFHTTPMessageRef CFHTTPMessageCreateEmpty (     CFAllocatorRef alloc,     Boolean isRequest ); ``` |
| To | ``` CFHTTPMessageRef _Nonnull CFHTTPMessageCreateEmpty (     CFAllocatorRef _Nullable alloc,     Boolean isRequest ); ``` |

Modified [CFHTTPMessageCreateRequest()](https://developer.apple.com/documentation/cfnetwork/1387314-cfhttpmessagecreaterequest)

|  | Declaration |
| --- | --- |
| From | ``` CFHTTPMessageRef CFHTTPMessageCreateRequest (     CFAllocatorRef alloc,     CFStringRef requestMethod,     CFURLRef url,     CFStringRef httpVersion ); ``` |
| To | ``` CFHTTPMessageRef _Nonnull CFHTTPMessageCreateRequest (     CFAllocatorRef _Nullable alloc,     CFStringRef _Nonnull requestMethod,     CFURLRef _Nonnull url,     CFStringRef _Nonnull httpVersion ); ``` |

Modified [CFHTTPMessageCreateResponse()](https://developer.apple.com/documentation/cfnetwork/1387272-cfhttpmessagecreateresponse)

|  | Declaration |
| --- | --- |
| From | ``` CFHTTPMessageRef CFHTTPMessageCreateResponse (     CFAllocatorRef alloc,     CFIndex statusCode,     CFStringRef statusDescription,     CFStringRef httpVersion ); ``` |
| To | ``` CFHTTPMessageRef _Nonnull CFHTTPMessageCreateResponse (     CFAllocatorRef _Nullable alloc,     CFIndex statusCode,     CFStringRef _Nullable statusDescription,     CFStringRef _Nonnull httpVersion ); ``` |

Modified [CFHTTPMessageGetResponseStatusCode()](https://developer.apple.com/documentation/cfnetwork/1387284-cfhttpmessagegetresponsestatusco)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex CFHTTPMessageGetResponseStatusCode (     CFHTTPMessageRef response ); ``` |
| To | ``` CFIndex CFHTTPMessageGetResponseStatusCode (     CFHTTPMessageRef _Nonnull response ); ``` |

Modified [CFHTTPMessageIsHeaderComplete()](https://developer.apple.com/documentation/cfnetwork/1387264-cfhttpmessageisheadercomplete)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageIsHeaderComplete (     CFHTTPMessageRef message ); ``` |
| To | ``` Boolean CFHTTPMessageIsHeaderComplete (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageIsRequest()](https://developer.apple.com/documentation/cfnetwork/1387308-cfhttpmessageisrequest)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFHTTPMessageIsRequest (     CFHTTPMessageRef message ); ``` |
| To | ``` Boolean CFHTTPMessageIsRequest (     CFHTTPMessageRef _Nonnull message ); ``` |

Modified [CFHTTPMessageSetBody()](https://developer.apple.com/documentation/cfnetwork/1387302-cfhttpmessagesetbody)

|  | Declaration |
| --- | --- |
| From | ``` void CFHTTPMessageSetBody (     CFHTTPMessageRef message,     CFDataRef bodyData ); ``` |
| To | ``` void CFHTTPMessageSetBody (     CFHTTPMessageRef _Nonnull message,     CFDataRef _Nonnull bodyData ); ``` |

Modified [CFHTTPMessageSetHeaderFieldValue()](https://developer.apple.com/documentation/cfnetwork/1387276-cfhttpmessagesetheaderfieldvalue)

|  | Declaration |
| --- | --- |
| From | ``` void CFHTTPMessageSetHeaderFieldValue (     CFHTTPMessageRef message,     CFStringRef headerField,     CFStringRef value ); ``` |
| To | ``` void CFHTTPMessageSetHeaderFieldValue (     CFHTTPMessageRef _Nonnull message,     CFStringRef _Nonnull headerField,     CFStringRef _Nullable value ); ``` |

#### CFHTTPStream.h

Modified [CFHTTPReadStreamSetRedirectsAutomatically()](https://developer.apple.com/documentation/cfnetwork/1558218-cfhttpreadstreamsetredirectsauto)

|  | Declaration |
| --- | --- |
| From | ``` void CFHTTPReadStreamSetRedirectsAutomatically (     CFReadStreamRef httpStream,     Boolean shouldAutoRedirect ); ``` |
| To | ``` void CFHTTPReadStreamSetRedirectsAutomatically (     CFReadStreamRef _Nonnull httpStream,     Boolean shouldAutoRedirect ); ``` |

Modified [CFReadStreamCreateForHTTPRequest()](https://developer.apple.com/documentation/cfnetwork/1426845-cfreadstreamcreateforhttprequest)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` CFReadStreamRef CFReadStreamCreateForHTTPRequest (     CFAllocatorRef alloc,     CFHTTPMessageRef request ); ``` | OS X 10.1 | -- |
| To | ``` CFReadStreamRef _Nonnull CFReadStreamCreateForHTTPRequest (     CFAllocatorRef _Nullable alloc,     CFHTTPMessageRef _Nonnull request ); ``` | OS X 10.2 | OS X 10.11 |

Modified [CFReadStreamCreateForStreamedHTTPRequest()](https://developer.apple.com/documentation/cfnetwork/1426381-cfreadstreamcreateforstreamedhtt)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CFReadStreamRef CFReadStreamCreateForStreamedHTTPRequest (     CFAllocatorRef alloc,     CFHTTPMessageRef requestHeaders,     CFReadStreamRef requestBody ); ``` | -- |
| To | ``` CFReadStreamRef _Nonnull CFReadStreamCreateForStreamedHTTPRequest (     CFAllocatorRef _Nullable alloc,     CFHTTPMessageRef _Nonnull requestHeaders,     CFReadStreamRef _Nonnull requestBody ); ``` | OS X 10.11 |

Modified [kCFStreamPropertyHTTPAttemptPersistentConnection](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpattemptpersistentconnection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPFinalRequest](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPFinalURL](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpfinalurl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxy)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxyhost)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpproxyport)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPRequestBytesWrittenCount](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttprequestbyteswrittencount)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPResponseHeader](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpresponseheader)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPShouldAutoredirect](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpshouldautoredirect)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPSProxyHost](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpsproxyhost)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified [kCFStreamPropertyHTTPSProxyPort](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertyhttpsproxyport)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### CFNetDiagnostics.h

Modified [CFNetDiagnosticCopyNetworkStatusPassively()](https://developer.apple.com/documentation/cfnetwork/1426472-cfnetdiagnosticcopynetworkstatus)

|  | Declaration |
| --- | --- |
| From | ``` CFNetDiagnosticStatus CFNetDiagnosticCopyNetworkStatusPassively (     CFNetDiagnosticRef details,     CFStringRef *description ); ``` |
| To | ``` CFNetDiagnosticStatus CFNetDiagnosticCopyNetworkStatusPassively (     CFNetDiagnosticRef _Nonnull details,     CFStringRef  _Nullable * _Nullable description ); ``` |

Modified [CFNetDiagnosticCreateWithStreams()](https://developer.apple.com/documentation/cfnetwork/1426752-cfnetdiagnosticcreatewithstreams)

|  | Declaration |
| --- | --- |
| From | ``` CFNetDiagnosticRef CFNetDiagnosticCreateWithStreams (     CFAllocatorRef alloc,     CFReadStreamRef readStream,     CFWriteStreamRef writeStream ); ``` |
| To | ``` CFNetDiagnosticRef _Nonnull CFNetDiagnosticCreateWithStreams (     CFAllocatorRef _Nullable alloc,     CFReadStreamRef _Nullable readStream,     CFWriteStreamRef _Nullable writeStream ); ``` |

Modified [CFNetDiagnosticCreateWithURL()](https://developer.apple.com/documentation/cfnetwork/1426741-cfnetdiagnosticcreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` CFNetDiagnosticRef CFNetDiagnosticCreateWithURL (     CFAllocatorRef alloc,     CFURLRef url ); ``` |
| To | ``` CFNetDiagnosticRef _Nonnull CFNetDiagnosticCreateWithURL (     CFAllocatorRef _Nonnull alloc,     CFURLRef _Nonnull url ); ``` |

Modified [CFNetDiagnosticDiagnoseProblemInteractively()](https://developer.apple.com/documentation/cfnetwork/1426588-cfnetdiagnosticdiagnoseproblemin)

|  | Declaration |
| --- | --- |
| From | ``` CFNetDiagnosticStatus CFNetDiagnosticDiagnoseProblemInteractively (     CFNetDiagnosticRef details ); ``` |
| To | ``` CFNetDiagnosticStatus CFNetDiagnosticDiagnoseProblemInteractively (     CFNetDiagnosticRef _Nonnull details ); ``` |

Modified [CFNetDiagnosticSetName()](https://developer.apple.com/documentation/cfnetwork/1426627-cfnetdiagnosticsetname)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetDiagnosticSetName (     CFNetDiagnosticRef details,     CFStringRef name ); ``` |
| To | ``` void CFNetDiagnosticSetName (     CFNetDiagnosticRef _Nonnull details,     CFStringRef _Nonnull name ); ``` |

#### CFNetServices.h

Modified [CFNetServiceBrowserCreate()](https://developer.apple.com/documentation/cfnetwork/1426560-cfnetservicebrowsercreate)

|  | Declaration |
| --- | --- |
| From | ``` CFNetServiceBrowserRef CFNetServiceBrowserCreate (     CFAllocatorRef alloc,     CFNetServiceBrowserClientCallBack clientCB,     CFNetServiceClientContext *clientContext ); ``` |
| To | ``` CFNetServiceBrowserRef _Nonnull CFNetServiceBrowserCreate (     CFAllocatorRef _Nullable alloc,     CFNetServiceBrowserClientCallBack _Nonnull clientCB,     CFNetServiceClientContext * _Nonnull clientContext ); ``` |

Modified [CFNetServiceBrowserInvalidate()](https://developer.apple.com/documentation/cfnetwork/1426399-cfnetservicebrowserinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceBrowserInvalidate (     CFNetServiceBrowserRef browser ); ``` |
| To | ``` void CFNetServiceBrowserInvalidate (     CFNetServiceBrowserRef _Nonnull browser ); ``` |

Modified [CFNetServiceBrowserScheduleWithRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426904-cfnetservicebrowserschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceBrowserScheduleWithRunLoop (     CFNetServiceBrowserRef browser,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceBrowserScheduleWithRunLoop (     CFNetServiceBrowserRef _Nonnull browser,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFNetServiceBrowserSearchForDomains()](https://developer.apple.com/documentation/cfnetwork/1426893-cfnetservicebrowsersearchfordoma)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceBrowserSearchForDomains (     CFNetServiceBrowserRef browser,     Boolean registrationDomains,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceBrowserSearchForDomains (     CFNetServiceBrowserRef _Nonnull browser,     Boolean registrationDomains,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceBrowserSearchForServices()](https://developer.apple.com/documentation/cfnetwork/1426405-cfnetservicebrowsersearchforserv)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceBrowserSearchForServices (     CFNetServiceBrowserRef browser,     CFStringRef domain,     CFStringRef serviceType,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceBrowserSearchForServices (     CFNetServiceBrowserRef _Nonnull browser,     CFStringRef _Nonnull domain,     CFStringRef _Nonnull serviceType,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceBrowserStopSearch()](https://developer.apple.com/documentation/cfnetwork/1426523-cfnetservicebrowserstopsearch)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceBrowserStopSearch (     CFNetServiceBrowserRef browser,     CFStreamError *error ); ``` |
| To | ``` void CFNetServiceBrowserStopSearch (     CFNetServiceBrowserRef _Nonnull browser,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceBrowserUnscheduleFromRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426565-cfnetservicebrowserunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceBrowserUnscheduleFromRunLoop (     CFNetServiceBrowserRef browser,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceBrowserUnscheduleFromRunLoop (     CFNetServiceBrowserRef _Nonnull browser,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFNetServiceCancel()](https://developer.apple.com/documentation/cfnetwork/1426533-cfnetservicecancel)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceCancel (     CFNetServiceRef theService ); ``` |
| To | ``` void CFNetServiceCancel (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceCreate()](https://developer.apple.com/documentation/cfnetwork/1426628-cfnetservicecreate)

|  | Declaration |
| --- | --- |
| From | ``` CFNetServiceRef CFNetServiceCreate (     CFAllocatorRef alloc,     CFStringRef domain,     CFStringRef serviceType,     CFStringRef name,     SInt32 port ); ``` |
| To | ``` CFNetServiceRef _Nonnull CFNetServiceCreate (     CFAllocatorRef _Nullable alloc,     CFStringRef _Nonnull domain,     CFStringRef _Nonnull serviceType,     CFStringRef _Nonnull name,     SInt32 port ); ``` |

Modified [CFNetServiceCreateCopy()](https://developer.apple.com/documentation/cfnetwork/1426654-cfnetservicecreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CFNetServiceRef CFNetServiceCreateCopy (     CFAllocatorRef alloc,     CFNetServiceRef service ); ``` |
| To | ``` CFNetServiceRef _Nonnull CFNetServiceCreateCopy (     CFAllocatorRef _Nullable alloc,     CFNetServiceRef _Nonnull service ); ``` |

Modified [CFNetServiceCreateDictionaryWithTXTData()](https://developer.apple.com/documentation/cfnetwork/1426852-cfnetservicecreatedictionarywith)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CFNetServiceCreateDictionaryWithTXTData (     CFAllocatorRef alloc,     CFDataRef txtRecord ); ``` |
| To | ``` CFDictionaryRef _Nullable CFNetServiceCreateDictionaryWithTXTData (     CFAllocatorRef _Nullable alloc,     CFDataRef _Nonnull txtRecord ); ``` |

Modified [CFNetServiceCreateTXTDataWithDictionary()](https://developer.apple.com/documentation/cfnetwork/1426572-cfnetservicecreatetxtdatawithdic)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CFNetServiceCreateTXTDataWithDictionary (     CFAllocatorRef alloc,     CFDictionaryRef keyValuePairs ); ``` |
| To | ``` CFDataRef _Nullable CFNetServiceCreateTXTDataWithDictionary (     CFAllocatorRef _Nullable alloc,     CFDictionaryRef _Nonnull keyValuePairs ); ``` |

Modified [CFNetServiceGetAddressing()](https://developer.apple.com/documentation/cfnetwork/1426743-cfnetservicegetaddressing)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFNetServiceGetAddressing (     CFNetServiceRef theService ); ``` |
| To | ``` CFArrayRef _Nullable CFNetServiceGetAddressing (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetDomain()](https://developer.apple.com/documentation/cfnetwork/1426607-cfnetservicegetdomain)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFNetServiceGetDomain (     CFNetServiceRef theService ); ``` |
| To | ``` CFStringRef _Nonnull CFNetServiceGetDomain (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetName()](https://developer.apple.com/documentation/cfnetwork/1426782-cfnetservicegetname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFNetServiceGetName (     CFNetServiceRef theService ); ``` |
| To | ``` CFStringRef _Nonnull CFNetServiceGetName (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetPortNumber()](https://developer.apple.com/documentation/cfnetwork/1426503-cfnetservicegetportnumber)

|  | Declaration |
| --- | --- |
| From | ``` SInt32 CFNetServiceGetPortNumber (     CFNetServiceRef theService ); ``` |
| To | ``` SInt32 CFNetServiceGetPortNumber (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetProtocolSpecificInformation()](https://developer.apple.com/documentation/cfnetwork/1574813-cfnetservicegetprotocolspecifici)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFNetServiceGetProtocolSpecificInformation (     CFNetServiceRef theService ); ``` |
| To | ``` CFStringRef _Nullable CFNetServiceGetProtocolSpecificInformation (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetTargetHost()](https://developer.apple.com/documentation/cfnetwork/1426656-cfnetservicegettargethost)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFNetServiceGetTargetHost (     CFNetServiceRef theService ); ``` |
| To | ``` CFStringRef _Nullable CFNetServiceGetTargetHost (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetTXTData()](https://developer.apple.com/documentation/cfnetwork/1426664-cfnetservicegettxtdata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CFNetServiceGetTXTData (     CFNetServiceRef theService ); ``` |
| To | ``` CFDataRef _Nullable CFNetServiceGetTXTData (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceGetType()](https://developer.apple.com/documentation/cfnetwork/1426806-cfnetservicegettype)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CFNetServiceGetType (     CFNetServiceRef theService ); ``` |
| To | ``` CFStringRef _Nonnull CFNetServiceGetType (     CFNetServiceRef _Nonnull theService ); ``` |

Modified [CFNetServiceMonitorCreate()](https://developer.apple.com/documentation/cfnetwork/1426665-cfnetservicemonitorcreate)

|  | Declaration |
| --- | --- |
| From | ``` CFNetServiceMonitorRef CFNetServiceMonitorCreate (     CFAllocatorRef alloc,     CFNetServiceRef theService,     CFNetServiceMonitorClientCallBack clientCB,     CFNetServiceClientContext *clientContext ); ``` |
| To | ``` CFNetServiceMonitorRef _Nonnull CFNetServiceMonitorCreate (     CFAllocatorRef _Nullable alloc,     CFNetServiceRef _Nonnull theService,     CFNetServiceMonitorClientCallBack _Nonnull clientCB,     CFNetServiceClientContext * _Nonnull clientContext ); ``` |

Modified [CFNetServiceMonitorInvalidate()](https://developer.apple.com/documentation/cfnetwork/1426906-cfnetservicemonitorinvalidate)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceMonitorInvalidate (     CFNetServiceMonitorRef monitor ); ``` |
| To | ``` void CFNetServiceMonitorInvalidate (     CFNetServiceMonitorRef _Nonnull monitor ); ``` |

Modified [CFNetServiceMonitorScheduleWithRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426880-cfnetservicemonitorschedulewithr)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceMonitorScheduleWithRunLoop (     CFNetServiceMonitorRef monitor,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceMonitorScheduleWithRunLoop (     CFNetServiceMonitorRef _Nonnull monitor,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFNetServiceMonitorStart()](https://developer.apple.com/documentation/cfnetwork/1426842-cfnetservicemonitorstart)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceMonitorStart (     CFNetServiceMonitorRef monitor,     CFNetServiceMonitorType recordType,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceMonitorStart (     CFNetServiceMonitorRef _Nonnull monitor,     CFNetServiceMonitorType recordType,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceMonitorStop()](https://developer.apple.com/documentation/cfnetwork/1426696-cfnetservicemonitorstop)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceMonitorStop (     CFNetServiceMonitorRef monitor,     CFStreamError *error ); ``` |
| To | ``` void CFNetServiceMonitorStop (     CFNetServiceMonitorRef _Nonnull monitor,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceMonitorUnscheduleFromRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426400-cfnetservicemonitorunschedulefro)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceMonitorUnscheduleFromRunLoop (     CFNetServiceMonitorRef monitor,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceMonitorUnscheduleFromRunLoop (     CFNetServiceMonitorRef _Nonnull monitor,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFNetServiceRegister()](https://developer.apple.com/documentation/cfnetwork/1574816-cfnetserviceregister)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceRegister (     CFNetServiceRef theService,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceRegister (     CFNetServiceRef _Nonnull theService,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceRegisterWithOptions()](https://developer.apple.com/documentation/cfnetwork/1426790-cfnetserviceregisterwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceRegisterWithOptions (     CFNetServiceRef theService,     CFOptionFlags options,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceRegisterWithOptions (     CFNetServiceRef _Nonnull theService,     CFOptionFlags options,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceResolve()](https://developer.apple.com/documentation/cfnetwork/1574815-cfnetserviceresolve)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceResolve (     CFNetServiceRef theService,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceResolve (     CFNetServiceRef _Nonnull theService,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceResolveWithTimeout()](https://developer.apple.com/documentation/cfnetwork/1426563-cfnetserviceresolvewithtimeout)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceResolveWithTimeout (     CFNetServiceRef theService,     CFTimeInterval timeout,     CFStreamError *error ); ``` |
| To | ``` Boolean CFNetServiceResolveWithTimeout (     CFNetServiceRef _Nonnull theService,     CFTimeInterval timeout,     CFStreamError * _Nullable error ); ``` |

Modified [CFNetServiceScheduleWithRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426730-cfnetserviceschedulewithrunloop)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceScheduleWithRunLoop (     CFNetServiceRef theService,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceScheduleWithRunLoop (     CFNetServiceRef _Nonnull theService,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

Modified [CFNetServiceSetClient()](https://developer.apple.com/documentation/cfnetwork/1426447-cfnetservicesetclient)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceSetClient (     CFNetServiceRef theService,     CFNetServiceClientCallBack clientCB,     CFNetServiceClientContext *clientContext ); ``` |
| To | ``` Boolean CFNetServiceSetClient (     CFNetServiceRef _Nonnull theService,     CFNetServiceClientCallBack _Nullable clientCB,     CFNetServiceClientContext * _Nullable clientContext ); ``` |

Modified [CFNetServiceSetProtocolSpecificInformation()](https://developer.apple.com/documentation/cfnetwork/1574812-cfnetservicesetprotocolspecifici)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceSetProtocolSpecificInformation (     CFNetServiceRef theService,     CFStringRef theInfo ); ``` |
| To | ``` void CFNetServiceSetProtocolSpecificInformation (     CFNetServiceRef _Nonnull theService,     CFStringRef _Nullable theInfo ); ``` |

Modified [CFNetServiceSetTXTData()](https://developer.apple.com/documentation/cfnetwork/1426670-cfnetservicesettxtdata)

|  | Declaration |
| --- | --- |
| From | ``` Boolean CFNetServiceSetTXTData (     CFNetServiceRef theService,     CFDataRef txtRecord ); ``` |
| To | ``` Boolean CFNetServiceSetTXTData (     CFNetServiceRef _Nonnull theService,     CFDataRef _Nonnull txtRecord ); ``` |

Modified [CFNetServiceUnscheduleFromRunLoop()](https://developer.apple.com/documentation/cfnetwork/1426679-cfnetserviceunschedulefromrunloo)

|  | Declaration |
| --- | --- |
| From | ``` void CFNetServiceUnscheduleFromRunLoop (     CFNetServiceRef theService,     CFRunLoopRef runLoop,     CFStringRef runLoopMode ); ``` |
| To | ``` void CFNetServiceUnscheduleFromRunLoop (     CFNetServiceRef _Nonnull theService,     CFRunLoopRef _Nonnull runLoop,     CFStringRef _Nonnull runLoopMode ); ``` |

#### CFNetworkErrors.h

Added [kCFURLErrorAppTransportSecurityRequiresSecureConnection](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/kcfurlerrorapptransportsecurityrequiressecureconnection)

#### CFProxySupport.h

Modified [CFNetworkCopyProxiesForAutoConfigurationScript()](https://developer.apple.com/documentation/cfnetwork/1426611-cfnetworkcopyproxiesforautoconfi)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFNetworkCopyProxiesForAutoConfigurationScript (     CFStringRef proxyAutoConfigurationScript,     CFURLRef targetURL,     CFErrorRef *error ); ``` |
| To | ``` CFArrayRef _Nullable CFNetworkCopyProxiesForAutoConfigurationScript (     CFStringRef _Nonnull proxyAutoConfigurationScript,     CFURLRef _Nonnull targetURL,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [CFNetworkCopyProxiesForURL()](https://developer.apple.com/documentation/cfnetwork/1426639-cfnetworkcopyproxiesforurl)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CFNetworkCopyProxiesForURL (     CFURLRef url,     CFDictionaryRef proxySettings ); ``` |
| To | ``` CFArrayRef _Nonnull CFNetworkCopyProxiesForURL (     CFURLRef _Nonnull url,     CFDictionaryRef _Nonnull proxySettings ); ``` |

Modified [CFNetworkCopySystemProxySettings()](https://developer.apple.com/documentation/cfnetwork/1426754-cfnetworkcopysystemproxysettings)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CFNetworkCopySystemProxySettings (     void ); ``` |
| To | ``` CFDictionaryRef _Nullable CFNetworkCopySystemProxySettings (     void ); ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationScript()](https://developer.apple.com/documentation/cfnetwork/1426362-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef CFNetworkExecuteProxyAutoConfigurationScript (     CFStringRef proxyAutoConfigurationScript,     CFURLRef targetURL,     CFProxyAutoConfigurationResultCallback cb,     CFStreamClientContext *clientContext ); ``` |
| To | ``` CFRunLoopSourceRef _Nonnull CFNetworkExecuteProxyAutoConfigurationScript (     CFStringRef _Nonnull proxyAutoConfigurationScript,     CFURLRef _Nonnull targetURL,     CFProxyAutoConfigurationResultCallback _Nonnull cb,     CFStreamClientContext * _Nonnull clientContext ); ``` |

Modified [CFNetworkExecuteProxyAutoConfigurationURL()](https://developer.apple.com/documentation/cfnetwork/1426392-cfnetworkexecuteproxyautoconfigu)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef CFNetworkExecuteProxyAutoConfigurationURL (     CFURLRef proxyAutoConfigURL,     CFURLRef targetURL,     CFProxyAutoConfigurationResultCallback cb,     CFStreamClientContext *clientContext ); ``` |
| To | ``` CFRunLoopSourceRef _Nonnull CFNetworkExecuteProxyAutoConfigurationURL (     CFURLRef _Nonnull proxyAutoConfigURL,     CFURLRef _Nonnull targetURL,     CFProxyAutoConfigurationResultCallback _Nonnull cb,     CFStreamClientContext * _Nonnull clientContext ); ``` |

#### CFSocketStream.h

Added [kCFStreamPropertySocketExtendedBackgroundIdleMode](https://developer.apple.com/documentation/cfnetwork/kcfstreampropertysocketextendedbackgroundidlemode)Modified [CFSocketStreamSOCKSGetError()](https://developer.apple.com/documentation/cfnetwork/1426548-cfsocketstreamsocksgeterror)

|  | Declaration |
| --- | --- |
| From | ``` SInt32 CFSocketStreamSOCKSGetError (     const CFStreamError *error ); ``` |
| To | ``` SInt32 CFSocketStreamSOCKSGetError (     const CFStreamError * _Nonnull error ); ``` |

Modified [CFSocketStreamSOCKSGetErrorSubdomain()](https://developer.apple.com/documentation/cfnetwork/1426737-cfsocketstreamsocksgeterrorsubdo)

|  | Declaration |
| --- | --- |
| From | ``` SInt32 CFSocketStreamSOCKSGetErrorSubdomain (     const CFStreamError *error ); ``` |
| To | ``` SInt32 CFSocketStreamSOCKSGetErrorSubdomain (     const CFStreamError * _Nonnull error ); ``` |

Modified [CFStreamCreatePairWithSocketToCFHost()](https://developer.apple.com/documentation/cfnetwork/1426831-cfstreamcreatepairwithsockettocf)

|  | Declaration |
| --- | --- |
| From | ``` void CFStreamCreatePairWithSocketToCFHost (     CFAllocatorRef alloc,     CFHostRef host,     SInt32 port,     CFReadStreamRef *readStream,     CFWriteStreamRef *writeStream ); ``` |
| To | ``` void CFStreamCreatePairWithSocketToCFHost (     CFAllocatorRef _Nullable alloc,     CFHostRef _Nonnull host,     SInt32 port,     CFReadStreamRef  _Nullable * _Nullable readStream,     CFWriteStreamRef  _Nullable * _Nullable writeStream ); ``` |

Modified [CFStreamCreatePairWithSocketToNetService()](https://developer.apple.com/documentation/cfnetwork/1426794-cfstreamcreatepairwithsockettone)

|  | Declaration |
| --- | --- |
| From | ``` void CFStreamCreatePairWithSocketToNetService (     CFAllocatorRef alloc,     CFNetServiceRef service,     CFReadStreamRef *readStream,     CFWriteStreamRef *writeStream ); ``` |
| To | ``` void CFStreamCreatePairWithSocketToNetService (     CFAllocatorRef _Nullable alloc,     CFNetServiceRef _Nonnull service,     CFReadStreamRef  _Nullable * _Nullable readStream,     CFWriteStreamRef  _Nullable * _Nullable writeStream ); ``` |

Modified [kCFStreamNetworkServiceTypeVoIP](https://developer.apple.com/documentation/cfnetwork/kcfstreamnetworkservicetypevoip)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

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
