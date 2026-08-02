---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/WebKit.html
archived_at: '2026-07-18T02:56:38.405522Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# WebKit Changes for Objective-C

### WebKit

#### WKBackForwardList.h

Modified [WKBackForwardList.backList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516698-backlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *backList ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKBackForwardListItem *> *backList ``` |

Modified [WKBackForwardList.forwardList](https://developer.apple.com/documentation/webkit/wkbackforwardlist/1516701-forwardlist)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *forwardList ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKBackForwardListItem *> *forwardList ``` |

#### WKError.h

Added [WKErrorJavaScriptResultTypeIsUnsupported](https://developer.apple.com/documentation/webkit/wkerrorcode/wkerrorjavascriptresulttypeisunsupported)

#### WKFrameInfo.h

Added [WKFrameInfo.securityOrigin](https://developer.apple.com/documentation/webkit/wkframeinfo/1503089-securityorigin)

#### WKNavigationDelegate.h

Added [-[WKNavigationDelegate webViewWebContentProcessDidTerminate:]](https://developer.apple.com/documentation/webkit/wknavigationdelegate/1455639-webviewwebcontentprocessdidtermi)

#### WKSecurityOrigin.h (Added)

Added [WKSecurityOrigin](https://developer.apple.com/documentation/webkit/wksecurityorigin)Added [WKSecurityOrigin.host](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536794-host)Added [WKSecurityOrigin.port](https://developer.apple.com/documentation/webkit/wksecurityorigin/1536403-port)Added [WKSecurityOrigin.protocol](https://developer.apple.com/documentation/webkit/wksecurityorigin/1537470-protocol)

#### WKUIDelegate.h

Added [-[WKUIDelegate webViewDidClose:]](https://developer.apple.com/documentation/webkit/wkuidelegate/1537390-webviewdidclose)

#### WKUserContentController.h

Modified [WKUserContentController.userScripts](https://developer.apple.com/documentation/webkit/wkusercontentcontroller/1538046-userscripts)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSArray *userScripts ``` |
| To | ``` @property(nonatomic, readonly, copy, nonnull) NSArray<WKUserScript *> *userScripts ``` |

#### WKWebsiteDataRecord.h (Added)

Added [WKWebsiteDataRecord](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord)Added [WKWebsiteDataRecord.dataTypes](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1538007-datatypes)Added [WKWebsiteDataRecord.displayName](https://developer.apple.com/documentation/webkit/wkwebsitedatarecord/1537733-displayname)Added [WKWebsiteDataTypeCookies](https://developer.apple.com/documentation/webkit/wkwebsitedatatypecookies)Added [WKWebsiteDataTypeDiskCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypediskcache)Added [WKWebsiteDataTypeIndexedDBDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeindexeddbdatabases)Added [WKWebsiteDataTypeLocalStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypelocalstorage)Added [WKWebsiteDataTypeMemoryCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypememorycache)Added [WKWebsiteDataTypeOfflineWebApplicationCache](https://developer.apple.com/documentation/webkit/wkwebsitedatatypeofflinewebapplicationcache)Added [WKWebsiteDataTypeSessionStorage](https://developer.apple.com/documentation/webkit/wkwebsitedatatypesessionstorage)Added [WKWebsiteDataTypeWebSQLDatabases](https://developer.apple.com/documentation/webkit/wkwebsitedatatypewebsqldatabases)

#### WKWebsiteDataStore.h (Added)

Added [WKWebsiteDataStore](https://developer.apple.com/documentation/webkit/wkwebsitedatastore)Added [+[WKWebsiteDataStore allWebsiteDataTypes]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532929-allwebsitedatatypes)Added [+[WKWebsiteDataStore defaultDataStore]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532937-defaultdatastore)Added [-[WKWebsiteDataStore fetchDataRecordsOfTypes:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532932-fetchdatarecords)Added [+[WKWebsiteDataStore nonPersistentDataStore]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532934-nonpersistentdatastore)Added [WKWebsiteDataStore.persistent](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532928-persistent)Added [-[WKWebsiteDataStore removeDataOfTypes:forDataRecords:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532936-removedataoftypes)Added [-[WKWebsiteDataStore removeDataOfTypes:modifiedSince:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebsitedatastore/1532938-removedataoftypes)

#### WKWebView.h

Added [WKWebView.allowsLinkPreview](https://developer.apple.com/documentation/webkit/wkwebview/1415000-allowslinkpreview)Added [WKWebView.certificateChain](https://developer.apple.com/documentation/webkit/wkwebview/1414958-certificatechain)Added [WKWebView.customUserAgent](https://developer.apple.com/documentation/webkit/wkwebview/1414950-customuseragent)Added [-[WKWebView loadData:MIMEType:characterEncodingName:baseURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1415011-loaddata)Added [-[WKWebView loadFileURL:allowingReadAccessToURL:]](https://developer.apple.com/documentation/webkit/wkwebview/1414973-loadfileurl)Modified [-[WKWebView evaluateJavaScript:completionHandler:]](https://developer.apple.com/documentation/webkit/wkwebview/1415017-evaluatejavascript)

|  | Declaration |
| --- | --- |
| From | ``` - (void)evaluateJavaScript:(NSString *)javaScriptString completionHandler:(void (^)(id, NSError *))completionHandler ``` |
| To | ``` - (void)evaluateJavaScript:(NSString * _Nonnull)javaScriptString completionHandler:(void (^ _Nullable)(id _Nullable, NSError * _Nullable error))completionHandler ``` |

#### WKWebViewConfiguration.h

Added [WKWebViewConfiguration.allowsAirPlayForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395673-allowsairplayformediaplayback)Added [WKWebViewConfiguration.allowsPictureInPictureMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614792-allowspictureinpicturemediaplayb)Added [WKWebViewConfiguration.applicationNameForUserAgent](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395665-applicationnameforuseragent)Added [WKWebViewConfiguration.requiresUserActionForMediaPlayback](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614794-requiresuseractionformediaplayba)Added [WKWebViewConfiguration.websiteDataStore](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1395661-websitedatastore)Added WKWebViewConfiguration(WKDeprecated)Modified [WKWebViewConfiguration.mediaPlaybackAllowsAirPlay](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614726-mediaplaybackallowsairplay)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [WKWebViewConfiguration.mediaPlaybackRequiresUserAction](https://developer.apple.com/documentation/webkit/wkwebviewconfiguration/1614727-mediaplaybackrequiresuseraction)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

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
