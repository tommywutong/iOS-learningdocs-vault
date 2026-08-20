---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/CoreServices.html
archived_at: '2026-07-18T02:58:42.668607Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# CoreServices Changes

## CoreServices

CFNetworkErrors.hAdded [kCFErrorPACFileAuth](https://developer.apple.com/documentation/cfnetwork/cfnetworkerrors/cferrorpacfileauth)CFProxySupport.hAdded [CFNetworkCopySystemProxySettings()](https://developer.apple.com/documentation/cfnetwork/1426754-cfnetworkcopysystemproxysettings)Added CFNetworkProxyAutoConfigurationSetAuthentication()Added [kCFNetworkProxiesExceptionsList](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesexceptionslist)Added [kCFNetworkProxiesExcludeSimpleHostnames](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesexcludesimplehostnames)Added [kCFNetworkProxiesFTPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpenable)Added [kCFNetworkProxiesFTPPassive](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftppassive)Added [kCFNetworkProxiesFTPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpport)Added [kCFNetworkProxiesFTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesftpproxy)Added [kCFNetworkProxiesGopherEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherenable)Added [kCFNetworkProxiesGopherPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherport)Added [kCFNetworkProxiesGopherProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesgopherproxy)Added [kCFNetworkProxiesHTTPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpenable)Added [kCFNetworkProxiesHTTPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpport)Added [kCFNetworkProxiesHTTPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpproxy)Added [kCFNetworkProxiesHTTPSEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsenable)Added [kCFNetworkProxiesHTTPSPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsport)Added [kCFNetworkProxiesHTTPSProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxieshttpsproxy)Added [kCFNetworkProxiesProxyAutoConfigEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigenable)Added [kCFNetworkProxiesProxyAutoConfigURLString](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautoconfigurlstring)Added [kCFNetworkProxiesProxyAutoDiscoveryEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesproxyautodiscoveryenable)Added [kCFNetworkProxiesRTSPEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspenable)Added [kCFNetworkProxiesRTSPPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspport)Added [kCFNetworkProxiesRTSPProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiesrtspproxy)Added [kCFNetworkProxiesSOCKSEnable](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksenable)Added [kCFNetworkProxiesSOCKSPort](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksport)Added [kCFNetworkProxiesSOCKSProxy](https://developer.apple.com/documentation/cfnetwork/kcfnetworkproxiessocksproxy)Added [kCFProxyAutoConfigurationHTTPResponseKey](https://developer.apple.com/documentation/cfnetwork/kcfproxyautoconfigurationhttpresponsekey)CFSocketStream.hModified [CFSocketStreamSOCKSGetError()](https://developer.apple.com/documentation/cfnetwork/1426548-cfsocketstreamsocksgeterror)

|  | Declaration |
| --- | --- |
| Old | SInt32 CFSocketStreamSOCKSGetError ( CFStreamError \*error); |
| New | SInt32 CFSocketStreamSOCKSGetError ( const CFStreamError \*error); |

Modified [CFSocketStreamSOCKSGetErrorSubdomain()](https://developer.apple.com/documentation/cfnetwork/1426737-cfsocketstreamsocksgeterrorsubdo)

|  | Declaration |
| --- | --- |
| Old | SInt32 CFSocketStreamSOCKSGetErrorSubdomain ( CFStreamError \*error); |
| New | SInt32 CFSocketStreamSOCKSGetErrorSubdomain ( const CFStreamError \*error); |

Files.hAdded [FSForkInfoFlags](https://developer.apple.com/documentation/coreservices/fsforkinfoflags)Added [kForkInfoFlagsFileLockedBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsfilelockedbit)Added [kForkInfoFlagsFileLockedMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsfilelockedmask)Added [kForkInfoFlagsLargeFileBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagslargefilebit)Added [kForkInfoFlagsLargeFileMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagslargefilemask)Added [kForkInfoFlagsModifiedBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsmodifiedbit)Added [kForkInfoFlagsModifiedMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsmodifiedmask)Added [kForkInfoFlagsOwnClumpBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsownclumpbit)Added [kForkInfoFlagsOwnClumpMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsownclumpmask)Added [kForkInfoFlagsResourceBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsresourcebit)Added [kForkInfoFlagsResourceMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagsresourcemask)Added [kForkInfoFlagsSharedWriteBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagssharedwritebit)Added [kForkInfoFlagsSharedWriteMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagssharedwritemask)Added [kForkInfoFlagsWriteBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagswritebit)Added [kForkInfoFlagsWriteLockedBit](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagswritelockedbit)Added [kForkInfoFlagsWriteLockedMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagswritelockedmask)Added [kForkInfoFlagsWriteMask](https://developer.apple.com/documentation/coreservices/1566512-anonymous/kforkinfoflagswritemask)KeychainCore.hModified [kcfindgenericpassword()](https://developer.apple.com/documentation/coreservices/1562994-kcfindgenericpassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCDeleteItem()](https://developer.apple.com/documentation/coreservices/1563195-kcdeleteitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindGenericPassword()](https://developer.apple.com/documentation/coreservices/1563056-kcfindgenericpassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCMakeKCRefFromAlias()](https://developer.apple.com/documentation/coreservices/1563083-kcmakekcreffromalias)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetDefaultKeychain()](https://developer.apple.com/documentation/coreservices/1563054-kcgetdefaultkeychain)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetKeychain()](https://developer.apple.com/documentation/coreservices/1563140-kcgetkeychain)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCLock()](https://developer.apple.com/documentation/coreservices/1563012-kclock)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCSetInteractionAllowed()](https://developer.apple.com/documentation/coreservices/1563079-kcsetinteractionallowed)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCIsInteractionAllowed()](https://developer.apple.com/documentation/coreservices/1563065-kcisinteractionallowed)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetData()](https://developer.apple.com/documentation/coreservices/1563092-kcgetdata)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCSetAttribute()](https://developer.apple.com/documentation/coreservices/1563089-kcsetattribute)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCUpdateItem()](https://developer.apple.com/documentation/coreservices/1563138-kcupdateitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindAppleSharePassword()](https://developer.apple.com/documentation/coreservices/1563124-kcfindapplesharepassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [NewKCCallbackUPP()](https://developer.apple.com/documentation/coreservices/1562977-newkccallbackupp)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindFirstItem()](https://developer.apple.com/documentation/coreservices/1563050-kcfindfirstitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCRemoveCallback()](https://developer.apple.com/documentation/coreservices/1563066-kcremovecallback)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCAddCallback()](https://developer.apple.com/documentation/coreservices/1563150-kcaddcallback)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetKeychainName()](https://developer.apple.com/documentation/coreservices/1563052-kcgetkeychainname)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCCountKeychains()](https://developer.apple.com/documentation/coreservices/1563038-kccountkeychains)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [InvokeKCCallbackUPP()](https://developer.apple.com/documentation/coreservices/1563117-invokekccallbackupp)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCMakeAliasFromKCRef()](https://developer.apple.com/documentation/coreservices/1563163-kcmakealiasfromkcref)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [kcfindinternetpasswordwithpath()](https://developer.apple.com/documentation/coreservices/1563135-kcfindinternetpasswordwithpath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCMakeKCRefFromFSRef()](https://developer.apple.com/documentation/coreservices/1563116-kcmakekcreffromfsref)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCSetDefaultKeychain()](https://developer.apple.com/documentation/coreservices/1563084-kcsetdefaultkeychain)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCReleaseKeychain()](https://developer.apple.com/documentation/coreservices/1563130-kcreleasekeychain)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindInternetPasswordWithPath()](https://developer.apple.com/documentation/coreservices/1563059-kcfindinternetpasswordwithpath)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetStatus()](https://developer.apple.com/documentation/coreservices/1563057-kcgetstatus)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCReleaseSearch()](https://developer.apple.com/documentation/coreservices/1562982-kcreleasesearch)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [kcfindapplesharepassword()](https://developer.apple.com/documentation/coreservices/1563164-kcfindapplesharepassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [DisposeKCCallbackUPP()](https://developer.apple.com/documentation/coreservices/1563023-disposekccallbackupp)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCCopyItem()](https://developer.apple.com/documentation/coreservices/1562984-kccopyitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [kcgetkeychainname()](https://developer.apple.com/documentation/coreservices/1563005-kcgetkeychainname)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCReleaseItem()](https://developer.apple.com/documentation/coreservices/1563161-kcreleaseitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetAttribute()](https://developer.apple.com/documentation/coreservices/1563176-kcgetattribute)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindInternetPassword()](https://developer.apple.com/documentation/coreservices/1563101-kcfindinternetpassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCFindNextItem()](https://developer.apple.com/documentation/coreservices/1563007-kcfindnextitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCSetData()](https://developer.apple.com/documentation/coreservices/1563018-kcsetdata)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCGetIndKeychain()](https://developer.apple.com/documentation/coreservices/1563047-kcgetindkeychain)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [kcfindinternetpassword()](https://developer.apple.com/documentation/coreservices/1563036-kcfindinternetpassword)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

Modified [KCNewItem()](https://developer.apple.com/documentation/coreservices/1563010-kcnewitem)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.6 |

MDItem.hAdded [MDItemCreateWithURL()](https://developer.apple.com/documentation/coreservices/1427034-mditemcreatewithurl)Added [kMDItemAuthorAddresses](https://developer.apple.com/documentation/coreservices/kmditemauthoraddresses)Added [kMDItemPixelCount](https://developer.apple.com/documentation/coreservices/kmditempixelcount)Added [kMDItemRecipientAddresses](https://developer.apple.com/documentation/coreservices/kmditemrecipientaddresses)MDQuery.hAdded [MDQuerySetSortComparatorBlock()](https://developer.apple.com/documentation/coreservices/1413021-mdquerysetsortcomparatorblock) (no architecture available)SKAnalysis.hModified [kSKLanguageTypes](https://developer.apple.com/documentation/coreservices/ksklanguagetypes)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

SKSearch.hModified [SKSearchGroupGetTypeID()](https://developer.apple.com/documentation/coreservices/1448637-sksearchgroupgettypeid)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

Modified [SKSearchResultsGetTypeID()](https://developer.apple.com/documentation/coreservices/1448603-sksearchresultsgettypeid)

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.4 |

TextCommon.hAdded [kTextEncodingUnicodeV5_1](https://developer.apple.com/documentation/coreservices/1400188-unicode_and_iso_ucs_text_encodin/ktextencodingunicodev5_1)TextEncodingConverter.hAdded [kTECDisableFallbacksBit](https://developer.apple.com/documentation/coreservices/1571807-anonymous/ktecdisablefallbacksbit)Added [kTECDisableFallbacksMask](https://developer.apple.com/documentation/coreservices/1571833-anonymous/ktecdisablefallbacksmask)Added [kTECDisableLooseMappingsBit](https://developer.apple.com/documentation/coreservices/1571807-anonymous/ktecdisableloosemappingsbit)Added [kTECDisableLooseMappingsMask](https://developer.apple.com/documentation/coreservices/1571833-anonymous/ktecdisableloosemappingsmask)Modified [TECCreateSniffer()](https://developer.apple.com/documentation/coreservices/1571832-teccreatesniffer)

|  | Declaration |
| --- | --- |
| Old | OSStatus TECCreateSniffer ( TECSnifferObjectRef \*encodingSniffer, TextEncoding testEncodings[], ItemCount numTextEncodings); |
| New | OSStatus TECCreateSniffer ( TECSnifferObjectRef \*encodingSniffer, const TextEncoding testEncodings[], ItemCount numTextEncodings); |

fp.hRemoved #def ldtox80Removed #def x80toldModified [atanl()](https://developer.apple.com/documentation/kernel/1557198-atanl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [roundl()](https://developer.apple.com/documentation/kernel/1557143-roundl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [coshl()](https://developer.apple.com/documentation/kernel/1557214-coshl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [log10l()](https://developer.apple.com/documentation/kernel/1557363-log10l)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [sqrtl()](https://developer.apple.com/documentation/kernel/1557199-sqrtl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [atanhl()](https://developer.apple.com/documentation/kernel/1557230-atanhl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [expm1l()](https://developer.apple.com/documentation/kernel/1557178-expm1l)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [fmaxl()](https://developer.apple.com/documentation/kernel/1557200-fmaxl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [copysignl()](https://developer.apple.com/documentation/kernel/1557294-copysignl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [logbl()](https://developer.apple.com/documentation/kernel/1557168-logbl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [rintl()](https://developer.apple.com/documentation/kernel/1557349-rintl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [remainderl()](https://developer.apple.com/documentation/kernel/1557193-remainderl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [acoshl()](https://developer.apple.com/documentation/kernel/1557266-acoshl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [floorl()](https://developer.apple.com/documentation/kernel/1557330-floorl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [fminl()](https://developer.apple.com/documentation/kernel/1557215-fminl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [fabsl()](https://developer.apple.com/documentation/kernel/1557341-fabsl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [sinl()](https://developer.apple.com/documentation/kernel/1557325-sinl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [acosl()](https://developer.apple.com/documentation/kernel/1557197-acosl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [sinhl()](https://developer.apple.com/documentation/kernel/1557240-sinhl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [lgammal()](https://developer.apple.com/documentation/kernel/1557282-lgammal)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [erfcl()](https://developer.apple.com/documentation/kernel/1557164-erfcl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [log1pl()](https://developer.apple.com/documentation/kernel/1557274-log1pl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [ldexpl()](https://developer.apple.com/documentation/kernel/1557365-ldexpl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [nearbyintl()](https://developer.apple.com/documentation/kernel/1557159-nearbyintl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [powl()](https://developer.apple.com/documentation/kernel/1557343-powl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified rinttoll()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [asinl()](https://developer.apple.com/documentation/kernel/1557222-asinl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [log2l()](https://developer.apple.com/documentation/kernel/1557169-log2l)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified roundtoll()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [expl()](https://developer.apple.com/documentation/kernel/1557224-expl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [exp2l()](https://developer.apple.com/documentation/kernel/1557194-exp2l)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [atan2l()](https://developer.apple.com/documentation/kernel/1557326-atan2l)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [fdiml()](https://developer.apple.com/documentation/kernel/1557241-fdiml)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [ceill()](https://developer.apple.com/documentation/kernel/1557207-ceill)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [remquol()](https://developer.apple.com/documentation/kernel/1557307-remquol)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [asinhl()](https://developer.apple.com/documentation/kernel/1557157-asinhl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [truncl()](https://developer.apple.com/documentation/kernel/1557153-truncl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified gammal()

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [hypotl()](https://developer.apple.com/documentation/kernel/1557299-hypotl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [erfl()](https://developer.apple.com/documentation/kernel/1557285-erfl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [frexpl()](https://developer.apple.com/documentation/kernel/1557175-frexpl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [logl()](https://developer.apple.com/documentation/kernel/1557184-logl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [cosl()](https://developer.apple.com/documentation/kernel/1557255-cosl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [tanl()](https://developer.apple.com/documentation/kernel/1557239-tanl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

Modified [tanhl()](https://developer.apple.com/documentation/kernel/1557188-tanhl)

|  | Architectures |
| --- | --- |
| Old | ppc,ppc64 |
| New | none? |

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
