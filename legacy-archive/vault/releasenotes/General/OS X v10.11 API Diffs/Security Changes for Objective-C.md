---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/Security.html
archived_at: '2026-07-18T02:53:13.126330Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Security Changes for Objective-C

### Security

#### Authorization.h

Modified [AuthorizationCopyInfo()](https://developer.apple.com/documentation/security/1397734-authorizationcopyinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationCopyInfo (     AuthorizationRef authorization,     AuthorizationString tag,     AuthorizationItemSet **info ); ``` |
| To | ``` OSStatus AuthorizationCopyInfo (     AuthorizationRef _Nonnull authorization,     AuthorizationString _Nullable tag,     AuthorizationItemSet * _Nullable * _Nonnull info ); ``` |

Modified [AuthorizationCopyPrivilegedReference()](https://developer.apple.com/documentation/security/1540021-authorizationcopyprivilegedrefer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationCopyPrivilegedReference (     AuthorizationRef *authorization,     AuthorizationFlags flags ); ``` |
| To | ``` OSStatus AuthorizationCopyPrivilegedReference (     AuthorizationRef  _Nullable * _Nonnull authorization,     AuthorizationFlags flags ); ``` |

Modified [AuthorizationCopyRights()](https://developer.apple.com/documentation/security/1395770-authorizationcopyrights)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationCopyRights (     AuthorizationRef authorization,     const AuthorizationRights *rights,     const AuthorizationEnvironment *environment,     AuthorizationFlags flags,     AuthorizationRights **authorizedRights ); ``` |
| To | ``` OSStatus AuthorizationCopyRights (     AuthorizationRef _Nonnull authorization,     const AuthorizationRights * _Nonnull rights,     const AuthorizationEnvironment * _Nullable environment,     AuthorizationFlags flags,     AuthorizationRights * _Nullable * _Nullable authorizedRights ); ``` |

Modified [AuthorizationCopyRightsAsync()](https://developer.apple.com/documentation/security/1394914-authorizationcopyrightsasync)

|  | Declaration |
| --- | --- |
| From | ``` void AuthorizationCopyRightsAsync (     AuthorizationRef authorization,     const AuthorizationRights *rights,     const AuthorizationEnvironment *environment,     AuthorizationFlags flags,     AuthorizationAsyncCallback callbackBlock ); ``` |
| To | ``` void AuthorizationCopyRightsAsync (     AuthorizationRef _Nonnull authorization,     const AuthorizationRights * _Nonnull rights,     const AuthorizationEnvironment * _Nullable environment,     AuthorizationFlags flags,     AuthorizationAsyncCallback _Nonnull callbackBlock ); ``` |

Modified [AuthorizationCreate()](https://developer.apple.com/documentation/security/1397453-authorizationcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationCreate (     const AuthorizationRights *rights,     const AuthorizationEnvironment *environment,     AuthorizationFlags flags,     AuthorizationRef *authorization ); ``` |
| To | ``` OSStatus AuthorizationCreate (     const AuthorizationRights * _Nullable rights,     const AuthorizationEnvironment * _Nullable environment,     AuthorizationFlags flags,     AuthorizationRef  _Nullable * _Nullable authorization ); ``` |

Modified [AuthorizationCreateFromExternalForm()](https://developer.apple.com/documentation/security/1400640-authorizationcreatefromexternalf)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationCreateFromExternalForm (     const AuthorizationExternalForm *extForm,     AuthorizationRef *authorization ); ``` |
| To | ``` OSStatus AuthorizationCreateFromExternalForm (     const AuthorizationExternalForm * _Nonnull extForm,     AuthorizationRef  _Nullable * _Nonnull authorization ); ``` |

Modified [AuthorizationExecuteWithPrivileges()](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationExecuteWithPrivileges (     AuthorizationRef authorization,     const char *pathToTool,     AuthorizationFlags options,     char *const *arguments,     FILE **communicationsPipe ); ``` |
| To | ``` OSStatus AuthorizationExecuteWithPrivileges (     AuthorizationRef _Nonnull authorization,     const char * _Nonnull pathToTool,     AuthorizationFlags options,     char *const  _Nonnull * _Nonnull arguments,     FILE * _Nullable * _Nullable communicationsPipe ); ``` |

Modified [AuthorizationFree()](https://developer.apple.com/documentation/security/1394257-authorizationfree)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationFree (     AuthorizationRef authorization,     AuthorizationFlags flags ); ``` |
| To | ``` OSStatus AuthorizationFree (     AuthorizationRef _Nonnull authorization,     AuthorizationFlags flags ); ``` |

Modified [AuthorizationFreeItemSet()](https://developer.apple.com/documentation/security/1392929-authorizationfreeitemset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationFreeItemSet (     AuthorizationItemSet *set ); ``` |
| To | ``` OSStatus AuthorizationFreeItemSet (     AuthorizationItemSet * _Nonnull set ); ``` |

Modified [AuthorizationMakeExternalForm()](https://developer.apple.com/documentation/security/1397335-authorizationmakeexternalform)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationMakeExternalForm (     AuthorizationRef authorization,     AuthorizationExternalForm *extForm ); ``` |
| To | ``` OSStatus AuthorizationMakeExternalForm (     AuthorizationRef _Nonnull authorization,     AuthorizationExternalForm * _Nonnull extForm ); ``` |

#### AuthorizationDB.h

Modified [AuthorizationRightGet()](https://developer.apple.com/documentation/security/1397961-authorizationrightget)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationRightGet (     const char *rightName,     CFDictionaryRef *rightDefinition ); ``` |
| To | ``` OSStatus AuthorizationRightGet (     const char * _Nonnull rightName,     CFDictionaryRef  _Nullable * _Nullable rightDefinition ); ``` |

Modified [AuthorizationRightRemove()](https://developer.apple.com/documentation/security/1393681-authorizationrightremove)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationRightRemove (     AuthorizationRef authRef,     const char *rightName ); ``` |
| To | ``` OSStatus AuthorizationRightRemove (     AuthorizationRef _Nonnull authRef,     const char * _Nonnull rightName ); ``` |

Modified [AuthorizationRightSet()](https://developer.apple.com/documentation/security/1399311-authorizationrightset)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationRightSet (     AuthorizationRef authRef,     const char *rightName,     CFTypeRef rightDefinition,     CFStringRef descriptionKey,     CFBundleRef bundle,     CFStringRef localeTableName ); ``` |
| To | ``` OSStatus AuthorizationRightSet (     AuthorizationRef _Nonnull authRef,     const char * _Nonnull rightName,     CFTypeRef _Nonnull rightDefinition,     CFStringRef _Nullable descriptionKey,     CFBundleRef _Nullable bundle,     CFStringRef _Nullable localeTableName ); ``` |

#### AuthorizationPlugin.h

Modified [AuthorizationPluginCreate()](https://developer.apple.com/documentation/security/1543160-authorizationplugincreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus AuthorizationPluginCreate (     const AuthorizationCallbacks *callbacks,     AuthorizationPluginRef *outPlugin,     const AuthorizationPluginInterface **outPluginInterface ); ``` |
| To | ``` OSStatus AuthorizationPluginCreate (     const AuthorizationCallbacks * _Nonnull callbacks,     AuthorizationPluginRef  _Nullable * _Nonnull outPlugin,     const AuthorizationPluginInterface * _Nullable * _Nonnull outPluginInterface ); ``` |

#### AuthSession.h

Modified [SessionGetInfo()](https://developer.apple.com/documentation/security/1593382-sessiongetinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SessionGetInfo (     SecuritySessionId session,     SecuritySessionId *sessionId,     SessionAttributeBits *attributes ); ``` |
| To | ``` OSStatus SessionGetInfo (     SecuritySessionId session,     SecuritySessionId * _Nullable sessionId,     SessionAttributeBits * _Nullable attributes ); ``` |

#### CMSDecoder.h

Modified [CMSDecoderCopyAllCerts()](https://developer.apple.com/documentation/security/1396602-cmsdecodercopyallcerts)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopyAllCerts (     CMSDecoderRef cmsDecoder,     CFArrayRef *certsOut ); ``` |
| To | ``` OSStatus CMSDecoderCopyAllCerts (     CMSDecoderRef _Nonnull cmsDecoder,     CFArrayRef  _Nullable * _Nonnull certsOut ); ``` |

Modified [CMSDecoderCopyContent()](https://developer.apple.com/documentation/security/1396553-cmsdecodercopycontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopyContent (     CMSDecoderRef cmsDecoder,     CFDataRef *contentOut ); ``` |
| To | ``` OSStatus CMSDecoderCopyContent (     CMSDecoderRef _Nonnull cmsDecoder,     CFDataRef  _Nullable * _Nonnull contentOut ); ``` |

Modified [CMSDecoderCopyDetachedContent()](https://developer.apple.com/documentation/security/1392572-cmsdecodercopydetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopyDetachedContent (     CMSDecoderRef cmsDecoder,     CFDataRef *detachedContentOut ); ``` |
| To | ``` OSStatus CMSDecoderCopyDetachedContent (     CMSDecoderRef _Nonnull cmsDecoder,     CFDataRef  _Nullable * _Nonnull detachedContentOut ); ``` |

Modified [CMSDecoderCopyEncapsulatedContentType()](https://developer.apple.com/documentation/security/1400582-cmsdecodercopyencapsulatedconten)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopyEncapsulatedContentType (     CMSDecoderRef cmsDecoder,     CFDataRef *eContentTypeOut ); ``` |
| To | ``` OSStatus CMSDecoderCopyEncapsulatedContentType (     CMSDecoderRef _Nonnull cmsDecoder,     CFDataRef  _Nullable * _Nonnull eContentTypeOut ); ``` |

Modified [CMSDecoderCopySignerCert()](https://developer.apple.com/documentation/security/1398566-cmsdecodercopysignercert)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerCert (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     SecCertificateRef *signerCertOut ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerCert (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     SecCertificateRef  _Nullable * _Nonnull signerCertOut ); ``` |

Modified [CMSDecoderCopySignerEmailAddress()](https://developer.apple.com/documentation/security/1400778-cmsdecodercopysigneremailaddress)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerEmailAddress (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     CFStringRef *signerEmailAddressOut ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerEmailAddress (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     CFStringRef  _Nullable * _Nonnull signerEmailAddressOut ); ``` |

Modified [CMSDecoderCopySignerSigningTime()](https://developer.apple.com/documentation/security/1401770-cmsdecodercopysignersigningtime)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerSigningTime (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     CFAbsoluteTime *signingTime ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerSigningTime (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     CFAbsoluteTime * _Nonnull signingTime ); ``` |

Modified [CMSDecoderCopySignerStatus()](https://developer.apple.com/documentation/security/1396762-cmsdecodercopysignerstatus)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerStatus (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     CFTypeRef policyOrArray,     Boolean evaluateSecTrust,     CMSSignerStatus *signerStatusOut,     SecTrustRef *secTrustOut,     OSStatus *certVerifyResultCodeOut ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerStatus (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     CFTypeRef _Nonnull policyOrArray,     Boolean evaluateSecTrust,     CMSSignerStatus * _Nullable signerStatusOut,     SecTrustRef  _Nullable * _Nullable secTrustOut,     OSStatus * _Nullable certVerifyResultCodeOut ); ``` |

Modified [CMSDecoderCopySignerTimestamp()](https://developer.apple.com/documentation/security/1399271-cmsdecodercopysignertimestamp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerTimestamp (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     CFAbsoluteTime *timestamp ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerTimestamp (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     CFAbsoluteTime * _Nonnull timestamp ); ``` |

Modified [CMSDecoderCopySignerTimestampCertificates()](https://developer.apple.com/documentation/security/1392952-cmsdecodercopysignertimestampcer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerTimestampCertificates (     CMSDecoderRef cmsDecoder,     size_t signerIndex,     CFArrayRef *certificateRefs ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerTimestampCertificates (     CMSDecoderRef _Nonnull cmsDecoder,     size_t signerIndex,     CFArrayRef  _Nullable * _Nonnull certificateRefs ); ``` |

Modified [CMSDecoderCopySignerTimestampWithPolicy()](https://developer.apple.com/documentation/security/1395908-cmsdecodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCopySignerTimestampWithPolicy (     CMSDecoderRef cmsDecoder,     CFTypeRef timeStampPolicy,     size_t signerIndex,     CFAbsoluteTime *timestamp ); ``` |
| To | ``` OSStatus CMSDecoderCopySignerTimestampWithPolicy (     CMSDecoderRef _Nonnull cmsDecoder,     CFTypeRef _Nullable timeStampPolicy,     size_t signerIndex,     CFAbsoluteTime * _Nonnull timestamp ); ``` |

Modified [CMSDecoderCreate()](https://developer.apple.com/documentation/security/1392600-cmsdecodercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderCreate (     CMSDecoderRef *cmsDecoderOut ); ``` |
| To | ``` OSStatus CMSDecoderCreate (     CMSDecoderRef  _Nullable * _Nonnull cmsDecoderOut ); ``` |

Modified [CMSDecoderFinalizeMessage()](https://developer.apple.com/documentation/security/1398714-cmsdecoderfinalizemessage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderFinalizeMessage (     CMSDecoderRef cmsDecoder ); ``` |
| To | ``` OSStatus CMSDecoderFinalizeMessage (     CMSDecoderRef _Nonnull cmsDecoder ); ``` |

Modified [CMSDecoderGetNumSigners()](https://developer.apple.com/documentation/security/1395297-cmsdecodergetnumsigners)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderGetNumSigners (     CMSDecoderRef cmsDecoder,     size_t *numSignersOut ); ``` |
| To | ``` OSStatus CMSDecoderGetNumSigners (     CMSDecoderRef _Nonnull cmsDecoder,     size_t * _Nonnull numSignersOut ); ``` |

Modified [CMSDecoderIsContentEncrypted()](https://developer.apple.com/documentation/security/1396082-cmsdecoderiscontentencrypted)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderIsContentEncrypted (     CMSDecoderRef cmsDecoder,     Boolean *isEncryptedOut ); ``` |
| To | ``` OSStatus CMSDecoderIsContentEncrypted (     CMSDecoderRef _Nonnull cmsDecoder,     Boolean * _Nonnull isEncryptedOut ); ``` |

Modified [CMSDecoderSetDetachedContent()](https://developer.apple.com/documentation/security/1402067-cmsdecodersetdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderSetDetachedContent (     CMSDecoderRef cmsDecoder,     CFDataRef detachedContent ); ``` |
| To | ``` OSStatus CMSDecoderSetDetachedContent (     CMSDecoderRef _Nonnull cmsDecoder,     CFDataRef _Nonnull detachedContent ); ``` |

Modified [CMSDecoderSetSearchKeychain()](https://developer.apple.com/documentation/security/1392933-cmsdecodersetsearchkeychain)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderSetSearchKeychain (     CMSDecoderRef cmsDecoder,     CFTypeRef keychainOrArray ); ``` |
| To | ``` OSStatus CMSDecoderSetSearchKeychain (     CMSDecoderRef _Nonnull cmsDecoder,     CFTypeRef _Nonnull keychainOrArray ); ``` |

Modified [CMSDecoderUpdateMessage()](https://developer.apple.com/documentation/security/1393876-cmsdecoderupdatemessage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSDecoderUpdateMessage (     CMSDecoderRef cmsDecoder,     const void *msgBytes,     size_t msgBytesLen ); ``` |
| To | ``` OSStatus CMSDecoderUpdateMessage (     CMSDecoderRef _Nonnull cmsDecoder,     const void * _Nonnull msgBytes,     size_t msgBytesLen ); ``` |

#### CMSEncoder.h

Added [CMSEncoderSetSignerAlgorithm()](https://developer.apple.com/documentation/security/1387135-cmsencodersetsigneralgorithm)Added [kCMSEncoderDigestAlgorithmSHA1](https://developer.apple.com/documentation/security/kcmsencoderdigestalgorithmsha1)Added [kCMSEncoderDigestAlgorithmSHA256](https://developer.apple.com/documentation/security/kcmsencoderdigestalgorithmsha256)Modified [CMSEncode()](https://developer.apple.com/documentation/security/1387147-cmsencode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncode (     CFTypeRef signers,     CFTypeRef recipients,     const CSSM_OID *eContentType,     Boolean detachedContent,     CMSSignedAttributes signedAttributes,     const void *content,     size_t contentLen,     CFDataRef *encodedContentOut ); ``` |
| To | ``` OSStatus CMSEncode (     CFTypeRef _Nullable signers,     CFTypeRef _Nullable recipients,     const CSSM_OID * _Nullable eContentType,     Boolean detachedContent,     CMSSignedAttributes signedAttributes,     const void * _Nonnull content,     size_t contentLen,     CFDataRef  _Nullable * _Nonnull encodedContentOut ); ``` |

Modified [CMSEncodeContent()](https://developer.apple.com/documentation/security/1387113-cmsencodecontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncodeContent (     CFTypeRef signers,     CFTypeRef recipients,     CFTypeRef eContentTypeOID,     Boolean detachedContent,     CMSSignedAttributes signedAttributes,     const void *content,     size_t contentLen,     CFDataRef *encodedContentOut ); ``` |
| To | ``` OSStatus CMSEncodeContent (     CFTypeRef _Nullable signers,     CFTypeRef _Nullable recipients,     CFTypeRef _Nullable eContentTypeOID,     Boolean detachedContent,     CMSSignedAttributes signedAttributes,     const void * _Nonnull content,     size_t contentLen,     CFDataRef  _Nullable * _Nullable encodedContentOut ); ``` |

Modified [CMSEncoderAddRecipients()](https://developer.apple.com/documentation/security/1387129-cmsencoderaddrecipients)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderAddRecipients (     CMSEncoderRef cmsEncoder,     CFTypeRef recipientOrArray ); ``` |
| To | ``` OSStatus CMSEncoderAddRecipients (     CMSEncoderRef _Nonnull cmsEncoder,     CFTypeRef _Nonnull recipientOrArray ); ``` |

Modified [CMSEncoderAddSignedAttributes()](https://developer.apple.com/documentation/security/1387117-cmsencoderaddsignedattributes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderAddSignedAttributes (     CMSEncoderRef cmsEncoder,     CMSSignedAttributes signedAttributes ); ``` |
| To | ``` OSStatus CMSEncoderAddSignedAttributes (     CMSEncoderRef _Nonnull cmsEncoder,     CMSSignedAttributes signedAttributes ); ``` |

Modified [CMSEncoderAddSigners()](https://developer.apple.com/documentation/security/1387177-cmsencoderaddsigners)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderAddSigners (     CMSEncoderRef cmsEncoder,     CFTypeRef signerOrArray ); ``` |
| To | ``` OSStatus CMSEncoderAddSigners (     CMSEncoderRef _Nonnull cmsEncoder,     CFTypeRef _Nonnull signerOrArray ); ``` |

Modified [CMSEncoderAddSupportingCerts()](https://developer.apple.com/documentation/security/1387168-cmsencoderaddsupportingcerts)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderAddSupportingCerts (     CMSEncoderRef cmsEncoder,     CFTypeRef certOrArray ); ``` |
| To | ``` OSStatus CMSEncoderAddSupportingCerts (     CMSEncoderRef _Nonnull cmsEncoder,     CFTypeRef _Nonnull certOrArray ); ``` |

Modified [CMSEncoderCopyEncapsulatedContentType()](https://developer.apple.com/documentation/security/1387151-cmsencodercopyencapsulatedconten)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopyEncapsulatedContentType (     CMSEncoderRef cmsEncoder,     CFDataRef *eContentTypeOut ); ``` |
| To | ``` OSStatus CMSEncoderCopyEncapsulatedContentType (     CMSEncoderRef _Nonnull cmsEncoder,     CFDataRef  _Nullable * _Nonnull eContentTypeOut ); ``` |

Modified [CMSEncoderCopyEncodedContent()](https://developer.apple.com/documentation/security/1387145-cmsencodercopyencodedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopyEncodedContent (     CMSEncoderRef cmsEncoder,     CFDataRef *encodedContentOut ); ``` |
| To | ``` OSStatus CMSEncoderCopyEncodedContent (     CMSEncoderRef _Nonnull cmsEncoder,     CFDataRef  _Nullable * _Nonnull encodedContentOut ); ``` |

Modified [CMSEncoderCopyRecipients()](https://developer.apple.com/documentation/security/1387125-cmsencodercopyrecipients)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopyRecipients (     CMSEncoderRef cmsEncoder,     CFArrayRef *recipientsOut ); ``` |
| To | ``` OSStatus CMSEncoderCopyRecipients (     CMSEncoderRef _Nonnull cmsEncoder,     CFArrayRef  _Nullable * _Nonnull recipientsOut ); ``` |

Modified [CMSEncoderCopySigners()](https://developer.apple.com/documentation/security/1387139-cmsencodercopysigners)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopySigners (     CMSEncoderRef cmsEncoder,     CFArrayRef *signersOut ); ``` |
| To | ``` OSStatus CMSEncoderCopySigners (     CMSEncoderRef _Nonnull cmsEncoder,     CFArrayRef  _Nullable * _Nonnull signersOut ); ``` |

Modified [CMSEncoderCopySignerTimestamp()](https://developer.apple.com/documentation/security/1387179-cmsencodercopysignertimestamp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopySignerTimestamp (     CMSEncoderRef cmsEncoder,     size_t signerIndex,     CFAbsoluteTime *timestamp ); ``` |
| To | ``` OSStatus CMSEncoderCopySignerTimestamp (     CMSEncoderRef _Nonnull cmsEncoder,     size_t signerIndex,     CFAbsoluteTime * _Nonnull timestamp ); ``` |

Modified [CMSEncoderCopySignerTimestampWithPolicy()](https://developer.apple.com/documentation/security/1387162-cmsencodercopysignertimestampwit)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopySignerTimestampWithPolicy (     CMSEncoderRef cmsEncoder,     CFTypeRef timeStampPolicy,     size_t signerIndex,     CFAbsoluteTime *timestamp ); ``` |
| To | ``` OSStatus CMSEncoderCopySignerTimestampWithPolicy (     CMSEncoderRef _Nonnull cmsEncoder,     CFTypeRef _Nullable timeStampPolicy,     size_t signerIndex,     CFAbsoluteTime * _Nonnull timestamp ); ``` |

Modified [CMSEncoderCopySupportingCerts()](https://developer.apple.com/documentation/security/1387159-cmsencodercopysupportingcerts)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCopySupportingCerts (     CMSEncoderRef cmsEncoder,     CFArrayRef *certsOut ); ``` |
| To | ``` OSStatus CMSEncoderCopySupportingCerts (     CMSEncoderRef _Nonnull cmsEncoder,     CFArrayRef  _Nullable * _Nonnull certsOut ); ``` |

Modified [CMSEncoderCreate()](https://developer.apple.com/documentation/security/1387170-cmsencodercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderCreate (     CMSEncoderRef *cmsEncoderOut ); ``` |
| To | ``` OSStatus CMSEncoderCreate (     CMSEncoderRef  _Nullable * _Nonnull cmsEncoderOut ); ``` |

Modified [CMSEncoderGetCertificateChainMode()](https://developer.apple.com/documentation/security/1387173-cmsencodergetcertificatechainmod)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderGetCertificateChainMode (     CMSEncoderRef cmsEncoder,     CMSCertificateChainMode *chainModeOut ); ``` |
| To | ``` OSStatus CMSEncoderGetCertificateChainMode (     CMSEncoderRef _Nonnull cmsEncoder,     CMSCertificateChainMode * _Nonnull chainModeOut ); ``` |

Modified [CMSEncoderGetHasDetachedContent()](https://developer.apple.com/documentation/security/1387123-cmsencodergethasdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderGetHasDetachedContent (     CMSEncoderRef cmsEncoder,     Boolean *detachedContentOut ); ``` |
| To | ``` OSStatus CMSEncoderGetHasDetachedContent (     CMSEncoderRef _Nonnull cmsEncoder,     Boolean * _Nonnull detachedContentOut ); ``` |

Modified [CMSEncoderSetCertificateChainMode()](https://developer.apple.com/documentation/security/1387160-cmsencodersetcertificatechainmod)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderSetCertificateChainMode (     CMSEncoderRef cmsEncoder,     CMSCertificateChainMode chainMode ); ``` |
| To | ``` OSStatus CMSEncoderSetCertificateChainMode (     CMSEncoderRef _Nonnull cmsEncoder,     CMSCertificateChainMode chainMode ); ``` |

Modified [CMSEncoderSetEncapsulatedContentType()](https://developer.apple.com/documentation/security/1387172-cmsencodersetencapsulatedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderSetEncapsulatedContentType (     CMSEncoderRef cmsEncoder,     const CSSM_OID *eContentType ); ``` |
| To | ``` OSStatus CMSEncoderSetEncapsulatedContentType (     CMSEncoderRef _Nonnull cmsEncoder,     const CSSM_OID * _Nonnull eContentType ); ``` |

Modified [CMSEncoderSetEncapsulatedContentTypeOID()](https://developer.apple.com/documentation/security/1387115-cmsencodersetencapsulatedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderSetEncapsulatedContentTypeOID (     CMSEncoderRef cmsEncoder,     CFTypeRef eContentTypeOID ); ``` |
| To | ``` OSStatus CMSEncoderSetEncapsulatedContentTypeOID (     CMSEncoderRef _Nonnull cmsEncoder,     CFTypeRef _Nonnull eContentTypeOID ); ``` |

Modified [CMSEncoderSetHasDetachedContent()](https://developer.apple.com/documentation/security/1387164-cmsencodersethasdetachedcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderSetHasDetachedContent (     CMSEncoderRef cmsEncoder,     Boolean detachedContent ); ``` |
| To | ``` OSStatus CMSEncoderSetHasDetachedContent (     CMSEncoderRef _Nonnull cmsEncoder,     Boolean detachedContent ); ``` |

Modified [CMSEncoderUpdateContent()](https://developer.apple.com/documentation/security/1387141-cmsencoderupdatecontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus CMSEncoderUpdateContent (     CMSEncoderRef cmsEncoder,     const void *content,     size_t contentLen ); ``` |
| To | ``` OSStatus CMSEncoderUpdateContent (     CMSEncoderRef _Nonnull cmsEncoder,     const void * _Nonnull content,     size_t contentLen ); ``` |

#### CSCommon.h

Added [errSecCSInvalidPlatform](https://developer.apple.com/documentation/security/errseccsinvalidplatform)Added [errSecCSInvalidSymlink](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinvalidsymlink)Added [errSecCSTooBig](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccstoobig)Added [kSecCSCheckTrustedAnchors](https://developer.apple.com/documentation/security/seccsflags/1393485-checktrustedanchors)

#### cssmtype.h

Added [CSSM_PADDING_SIGRAW](https://developer.apple.com/documentation/security/1568331-anonymous/cssm_padding_sigraw)

#### oids.h (Added)

Added [DERByte](https://developer.apple.com/documentation/security/derbyte)Added [DERItem](https://developer.apple.com/documentation/security/deritem)Added [DERSize](https://developer.apple.com/documentation/security/dersize)Added [oidAdCAIssuer](https://developer.apple.com/documentation/security/oidadcaissuer)Added [oidAdOCSP](https://developer.apple.com/documentation/security/oidadocsp)Added [oidAnyExtendedKeyUsage](https://developer.apple.com/documentation/security/oidanyextendedkeyusage)Added [oidAnyPolicy](https://developer.apple.com/documentation/security/oidanypolicy)Added [oidAuthorityInfoAccess](https://developer.apple.com/documentation/security/oidauthorityinfoaccess)Added [oidAuthorityKeyIdentifier](https://developer.apple.com/documentation/security/oidauthoritykeyidentifier)Added [oidBasicConstraints](https://developer.apple.com/documentation/security/oidbasicconstraints)Added [oidCertificatePolicies](https://developer.apple.com/documentation/security/oidcertificatepolicies)Added [oidCommonName](https://developer.apple.com/documentation/security/oidcommonname)Added [oidCountryName](https://developer.apple.com/documentation/security/oidcountryname)Added [oidCrlDistributionPoints](https://developer.apple.com/documentation/security/oidcrldistributionpoints)Added [oidDescription](https://developer.apple.com/documentation/security/oiddescription)Added [oidEcPubKey](https://developer.apple.com/documentation/security/oidecpubkey)Added [oidEmailAddress](https://developer.apple.com/documentation/security/oidemailaddress)Added [oidEntrustVersInfo](https://developer.apple.com/documentation/security/oidentrustversinfo)Added [oidExtendedKeyUsage](https://developer.apple.com/documentation/security/oidextendedkeyusage)Added [oidExtendedKeyUsageClientAuth](https://developer.apple.com/documentation/security/oidextendedkeyusageclientauth)Added [oidExtendedKeyUsageCodeSigning](https://developer.apple.com/documentation/security/oidextendedkeyusagecodesigning)Added [oidExtendedKeyUsageEmailProtection](https://developer.apple.com/documentation/security/oidextendedkeyusageemailprotection)Added [oidExtendedKeyUsageIPSec](https://developer.apple.com/documentation/security/oidextendedkeyusageipsec)Added [oidExtendedKeyUsageMicrosoftSGC](https://developer.apple.com/documentation/security/oidextendedkeyusagemicrosoftsgc)Added [oidExtendedKeyUsageNetscapeSGC](https://developer.apple.com/documentation/security/oidextendedkeyusagenetscapesgc)Added [oidExtendedKeyUsageOCSPSigning](https://developer.apple.com/documentation/security/oidextendedkeyusageocspsigning)Added [oidExtendedKeyUsageServerAuth](https://developer.apple.com/documentation/security/oidextendedkeyusageserverauth)Added [oidExtendedKeyUsageTimeStamping](https://developer.apple.com/documentation/security/oidextendedkeyusagetimestamping)Added [oidFee](https://developer.apple.com/documentation/security/oidfee)Added [oidFriendlyName](https://developer.apple.com/documentation/security/oidfriendlyname)Added [oidGoogleEmbeddedSignedCertificateTimestamp](https://developer.apple.com/documentation/security/oidgoogleembeddedsignedcertificatetimestamp)Added [oidGoogleOCSPSignedCertificateTimestamp](https://developer.apple.com/documentation/security/oidgoogleocspsignedcertificatetimestamp)Added [oidInhibitAnyPolicy](https://developer.apple.com/documentation/security/oidinhibitanypolicy)Added [oidIssuerAltName](https://developer.apple.com/documentation/security/oidissueraltname)Added [oidKeyUsage](https://developer.apple.com/documentation/security/oidkeyusage)Added [oidLocalityName](https://developer.apple.com/documentation/security/oidlocalityname)Added [oidLocalKeyId](https://developer.apple.com/documentation/security/oidlocalkeyid)Added [oidMd2](https://developer.apple.com/documentation/security/oidmd2)Added [oidMd2Rsa](https://developer.apple.com/documentation/security/oidmd2rsa)Added [oidMd4](https://developer.apple.com/documentation/security/oidmd4)Added [oidMd4Rsa](https://developer.apple.com/documentation/security/oidmd4rsa)Added [oidMd5](https://developer.apple.com/documentation/security/oidmd5)Added [oidMd5Fee](https://developer.apple.com/documentation/security/oidmd5fee)Added [oidMd5Rsa](https://developer.apple.com/documentation/security/oidmd5rsa)Added [oidMSNTPrincipalName](https://developer.apple.com/documentation/security/oidmsntprincipalname)Added [oidNameConstraints](https://developer.apple.com/documentation/security/oidnameconstraints)Added [oidNetscapeCertType](https://developer.apple.com/documentation/security/oidnetscapecerttype)Added [oidOrganizationalUnitName](https://developer.apple.com/documentation/security/oidorganizationalunitname)Added [oidOrganizationName](https://developer.apple.com/documentation/security/oidorganizationname)Added [oidPolicyConstraints](https://developer.apple.com/documentation/security/oidpolicyconstraints)Added [oidPolicyMappings](https://developer.apple.com/documentation/security/oidpolicymappings)Added [oidPrivateKeyUsagePeriod](https://developer.apple.com/documentation/security/oidprivatekeyusageperiod)Added [oidQtCps](https://developer.apple.com/documentation/security/oidqtcps)Added [oidQtUNotice](https://developer.apple.com/documentation/security/oidqtunotice)Added [oidRsa](https://developer.apple.com/documentation/security/oidrsa)Added [oidSha1](https://developer.apple.com/documentation/security/oidsha1)Added [oidSha1Dsa](https://developer.apple.com/documentation/security/oidsha1dsa)Added [oidSha1DsaCommonOIW](https://developer.apple.com/documentation/security/oidsha1dsacommonoiw)Added [oidSha1DsaOIW](https://developer.apple.com/documentation/security/oidsha1dsaoiw)Added [oidSha1Ecdsa](https://developer.apple.com/documentation/security/oidsha1ecdsa)Added [oidSha1Fee](https://developer.apple.com/documentation/security/oidsha1fee)Added [oidSha1Rsa](https://developer.apple.com/documentation/security/oidsha1rsa)Added [oidSha1RsaOIW](https://developer.apple.com/documentation/security/oidsha1rsaoiw)Added [oidSha224](https://developer.apple.com/documentation/security/oidsha224)Added [oidSha224Ecdsa](https://developer.apple.com/documentation/security/oidsha224ecdsa)Added [oidSha224Rsa](https://developer.apple.com/documentation/security/oidsha224rsa)Added [oidSha256](https://developer.apple.com/documentation/security/oidsha256)Added [oidSha256Ecdsa](https://developer.apple.com/documentation/security/oidsha256ecdsa)Added [oidSha256Rsa](https://developer.apple.com/documentation/security/oidsha256rsa)Added [oidSha384](https://developer.apple.com/documentation/security/oidsha384)Added [oidSha384Ecdsa](https://developer.apple.com/documentation/security/oidsha384ecdsa)Added [oidSha384Rsa](https://developer.apple.com/documentation/security/oidsha384rsa)Added [oidSha512](https://developer.apple.com/documentation/security/oidsha512)Added [oidSha512Ecdsa](https://developer.apple.com/documentation/security/oidsha512ecdsa)Added [oidSha512Rsa](https://developer.apple.com/documentation/security/oidsha512rsa)Added [oidStateOrProvinceName](https://developer.apple.com/documentation/security/oidstateorprovincename)Added [oidSubjectAltName](https://developer.apple.com/documentation/security/oidsubjectaltname)Added [oidSubjectInfoAccess](https://developer.apple.com/documentation/security/oidsubjectinfoaccess)Added [oidSubjectKeyIdentifier](https://developer.apple.com/documentation/security/oidsubjectkeyidentifier)

#### SecAccess.h

Modified [SecAccessCopyACLList()](https://developer.apple.com/documentation/security/1398213-secaccesscopyacllist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessCopyACLList (     SecAccessRef accessRef,     CFArrayRef *aclList ); ``` |
| To | ``` OSStatus SecAccessCopyACLList (     SecAccessRef _Nonnull accessRef,     CFArrayRef  _Nullable * _Nonnull aclList ); ``` |

Modified [SecAccessCopyMatchingACLList()](https://developer.apple.com/documentation/security/1400464-secaccesscopymatchingacllist)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SecAccessCopyMatchingACLList (     SecAccessRef accessRef,     CFTypeRef authorizationTag ); ``` |
| To | ``` CFArrayRef _Nullable SecAccessCopyMatchingACLList (     SecAccessRef _Nonnull accessRef,     CFTypeRef _Nonnull authorizationTag ); ``` |

Modified [SecAccessCopyOwnerAndACL()](https://developer.apple.com/documentation/security/1402089-secaccesscopyownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessCopyOwnerAndACL (     SecAccessRef accessRef,     uid_t *userId,     gid_t *groupId,     SecAccessOwnerType *ownerType,     CFArrayRef *aclList ); ``` |
| To | ``` OSStatus SecAccessCopyOwnerAndACL (     SecAccessRef _Nonnull accessRef,     uid_t * _Nullable userId,     gid_t * _Nullable groupId,     SecAccessOwnerType * _Nullable ownerType,     CFArrayRef  _Nullable * _Nullable aclList ); ``` |

Modified [SecAccessCopySelectedACLList()](https://developer.apple.com/documentation/security/1521111-secaccesscopyselectedacllist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessCopySelectedACLList (     SecAccessRef accessRef,     CSSM_ACL_AUTHORIZATION_TAG action,     CFArrayRef *aclList ); ``` |
| To | ``` OSStatus SecAccessCopySelectedACLList (     SecAccessRef _Nonnull accessRef,     CSSM_ACL_AUTHORIZATION_TAG action,     CFArrayRef  _Nullable * _Nonnull aclList ); ``` |

Modified [SecAccessCreate()](https://developer.apple.com/documentation/security/1393522-secaccesscreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessCreate (     CFStringRef descriptor,     CFArrayRef trustedlist,     SecAccessRef *accessRef ); ``` |
| To | ``` OSStatus SecAccessCreate (     CFStringRef _Nonnull descriptor,     CFArrayRef _Nullable trustedlist,     SecAccessRef  _Nullable * _Nonnull accessRef ); ``` |

Modified [SecAccessCreateFromOwnerAndACL()](https://developer.apple.com/documentation/security/1521118-secaccesscreatefromownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessCreateFromOwnerAndACL (     const CSSM_ACL_OWNER_PROTOTYPE *owner,     uint32 aclCount,     const CSSM_ACL_ENTRY_INFO *acls,     SecAccessRef *accessRef ); ``` |
| To | ``` OSStatus SecAccessCreateFromOwnerAndACL (     const CSSM_ACL_OWNER_PROTOTYPE * _Nonnull owner,     uint32 aclCount,     const CSSM_ACL_ENTRY_INFO * _Nonnull acls,     SecAccessRef  _Nullable * _Nonnull accessRef ); ``` |

Modified [SecAccessCreateWithOwnerAndACL()](https://developer.apple.com/documentation/security/1395706-secaccesscreatewithownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` SecAccessRef SecAccessCreateWithOwnerAndACL (     uid_t userId,     gid_t groupId,     SecAccessOwnerType ownerType,     CFArrayRef acls,     CFErrorRef *error ); ``` |
| To | ``` SecAccessRef _Nullable SecAccessCreateWithOwnerAndACL (     uid_t userId,     gid_t groupId,     SecAccessOwnerType ownerType,     CFArrayRef _Nullable acls,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecAccessGetOwnerAndACL()](https://developer.apple.com/documentation/security/1521095-secaccessgetownerandacl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAccessGetOwnerAndACL (     SecAccessRef accessRef,     CSSM_ACL_OWNER_PROTOTYPE_PTR *owner,     uint32 *aclCount,     CSSM_ACL_ENTRY_INFO_PTR *acls ); ``` |
| To | ``` OSStatus SecAccessGetOwnerAndACL (     SecAccessRef _Nonnull accessRef,     CSSM_ACL_OWNER_PROTOTYPE_PTR  _Nullable * _Nonnull owner,     uint32 * _Nonnull aclCount,     CSSM_ACL_ENTRY_INFO_PTR  _Nullable * _Nonnull acls ); ``` |

#### SecAccessControl.h

Added [kSecAccessControlDevicePasscode](https://developer.apple.com/documentation/security/secaccesscontrolcreateflags/1394326-devicepasscode)Modified [SecAccessControlCreateWithFlags()](https://developer.apple.com/documentation/security/1394452-secaccesscontrolcreatewithflags)

|  | Declaration |
| --- | --- |
| From | ``` SecAccessControlRef SecAccessControlCreateWithFlags (     CFAllocatorRef allocator,     CFTypeRef protection,     SecAccessControlCreateFlags flags,     CFErrorRef *error ); ``` |
| To | ``` SecAccessControlRef _Nullable SecAccessControlCreateWithFlags (     CFAllocatorRef _Nullable allocator,     CFTypeRef _Nonnull protection,     SecAccessControlCreateFlags flags,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecACL.h

Modified [SecACLCopyAuthorizations()](https://developer.apple.com/documentation/security/1396830-secaclcopyauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SecACLCopyAuthorizations (     SecACLRef acl ); ``` |
| To | ``` CFArrayRef _Nonnull SecACLCopyAuthorizations (     SecACLRef _Nonnull acl ); ``` |

Modified [SecACLCopyContents()](https://developer.apple.com/documentation/security/1400970-secaclcopycontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLCopyContents (     SecACLRef acl,     CFArrayRef *applicationList,     CFStringRef *description,     SecKeychainPromptSelector *promptSelector ); ``` |
| To | ``` OSStatus SecACLCopyContents (     SecACLRef _Nonnull acl,     CFArrayRef  _Nullable * _Nonnull applicationList,     CFStringRef  _Nullable * _Nonnull description,     SecKeychainPromptSelector * _Nonnull promptSelector ); ``` |

Modified [SecACLCopySimpleContents()](https://developer.apple.com/documentation/security/1577133-secaclcopysimplecontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLCopySimpleContents (     SecACLRef acl,     CFArrayRef *applicationList,     CFStringRef *description,     CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector ); ``` |
| To | ``` OSStatus SecACLCopySimpleContents (     SecACLRef _Nonnull acl,     CFArrayRef  _Nullable * _Nonnull applicationList,     CFStringRef  _Nullable * _Nonnull description,     CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR * _Nonnull promptSelector ); ``` |

Modified [SecACLCreateFromSimpleContents()](https://developer.apple.com/documentation/security/1577132-secaclcreatefromsimplecontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLCreateFromSimpleContents (     SecAccessRef access,     CFArrayRef applicationList,     CFStringRef description,     const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector,     SecACLRef *newAcl ); ``` |
| To | ``` OSStatus SecACLCreateFromSimpleContents (     SecAccessRef _Nonnull access,     CFArrayRef _Nullable applicationList,     CFStringRef _Nonnull description,     const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR * _Nonnull promptSelector,     SecACLRef  _Nullable * _Nonnull newAcl ); ``` |

Modified [SecACLCreateWithSimpleContents()](https://developer.apple.com/documentation/security/1402295-secaclcreatewithsimplecontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLCreateWithSimpleContents (     SecAccessRef access,     CFArrayRef applicationList,     CFStringRef description,     SecKeychainPromptSelector promptSelector,     SecACLRef *newAcl ); ``` |
| To | ``` OSStatus SecACLCreateWithSimpleContents (     SecAccessRef _Nonnull access,     CFArrayRef _Nullable applicationList,     CFStringRef _Nonnull description,     SecKeychainPromptSelector promptSelector,     SecACLRef  _Nullable * _Nonnull newAcl ); ``` |

Modified [SecACLGetAuthorizations()](https://developer.apple.com/documentation/security/1577131-secaclgetauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLGetAuthorizations (     SecACLRef acl,     CSSM_ACL_AUTHORIZATION_TAG *tags,     uint32 *tagCount ); ``` |
| To | ``` OSStatus SecACLGetAuthorizations (     SecACLRef _Nonnull acl,     CSSM_ACL_AUTHORIZATION_TAG * _Nonnull tags,     uint32 * _Nonnull tagCount ); ``` |

Modified [SecACLRemove()](https://developer.apple.com/documentation/security/1398788-secaclremove)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLRemove (     SecACLRef aclRef ); ``` |
| To | ``` OSStatus SecACLRemove (     SecACLRef _Nonnull aclRef ); ``` |

Modified [SecACLSetAuthorizations()](https://developer.apple.com/documentation/security/1577130-secaclsetauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLSetAuthorizations (     SecACLRef acl,     CSSM_ACL_AUTHORIZATION_TAG *tags,     uint32 tagCount ); ``` |
| To | ``` OSStatus SecACLSetAuthorizations (     SecACLRef _Nonnull acl,     CSSM_ACL_AUTHORIZATION_TAG * _Nonnull tags,     uint32 tagCount ); ``` |

Modified [SecACLSetContents()](https://developer.apple.com/documentation/security/1400997-secaclsetcontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLSetContents (     SecACLRef acl,     CFArrayRef applicationList,     CFStringRef description,     SecKeychainPromptSelector promptSelector ); ``` |
| To | ``` OSStatus SecACLSetContents (     SecACLRef _Nonnull acl,     CFArrayRef _Nullable applicationList,     CFStringRef _Nonnull description,     SecKeychainPromptSelector promptSelector ); ``` |

Modified [SecACLSetSimpleContents()](https://developer.apple.com/documentation/security/1577129-secaclsetsimplecontents)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLSetSimpleContents (     SecACLRef acl,     CFArrayRef applicationList,     CFStringRef description,     const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR *promptSelector ); ``` |
| To | ``` OSStatus SecACLSetSimpleContents (     SecACLRef _Nonnull acl,     CFArrayRef _Nullable applicationList,     CFStringRef _Nonnull description,     const CSSM_ACL_KEYCHAIN_PROMPT_SELECTOR * _Nonnull promptSelector ); ``` |

Modified [SecACLUpdateAuthorizations()](https://developer.apple.com/documentation/security/1392184-secaclupdateauthorizations)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecACLUpdateAuthorizations (     SecACLRef acl,     CFArrayRef authorizations ); ``` |
| To | ``` OSStatus SecACLUpdateAuthorizations (     SecACLRef _Nonnull acl,     CFArrayRef _Nonnull authorizations ); ``` |

#### SecAsn1Coder.h

Modified [SecAsn1AllocCopy()](https://developer.apple.com/documentation/security/1428212-secasn1alloccopy)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1AllocCopy (     SecAsn1CoderRef coder,     const void *src,     size_t len,     SecAsn1Item *dest ); ``` |
| To | ``` OSStatus SecAsn1AllocCopy (     SecAsn1CoderRef _Nonnull coder,     const void * _Nonnull src,     size_t len,     SecAsn1Item * _Nonnull dest ); ``` |

Modified [SecAsn1AllocCopyItem()](https://developer.apple.com/documentation/security/1428197-secasn1alloccopyitem)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1AllocCopyItem (     SecAsn1CoderRef coder,     const SecAsn1Item *src,     SecAsn1Item *dest ); ``` |
| To | ``` OSStatus SecAsn1AllocCopyItem (     SecAsn1CoderRef _Nonnull coder,     const SecAsn1Item * _Nonnull src,     SecAsn1Item * _Nonnull dest ); ``` |

Modified [SecAsn1AllocItem()](https://developer.apple.com/documentation/security/1428206-secasn1allocitem)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1AllocItem (     SecAsn1CoderRef coder,     SecAsn1Item *item,     size_t len ); ``` |
| To | ``` OSStatus SecAsn1AllocItem (     SecAsn1CoderRef _Nonnull coder,     SecAsn1Item * _Nonnull item,     size_t len ); ``` |

Modified [SecAsn1CoderCreate()](https://developer.apple.com/documentation/security/1428210-secasn1codercreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1CoderCreate (     SecAsn1CoderRef *coder ); ``` |
| To | ``` OSStatus SecAsn1CoderCreate (     SecAsn1CoderRef  _Nullable * _Nonnull coder ); ``` |

Modified [SecAsn1CoderRelease()](https://developer.apple.com/documentation/security/1428199-secasn1coderrelease)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1CoderRelease (     SecAsn1CoderRef coder ); ``` |
| To | ``` OSStatus SecAsn1CoderRelease (     SecAsn1CoderRef _Nonnull coder ); ``` |

Modified [SecAsn1Decode()](https://developer.apple.com/documentation/security/1428193-secasn1decode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1Decode (     SecAsn1CoderRef coder,     const void *src,     size_t len,     const SecAsn1Template *templates,     void *dest ); ``` |
| To | ``` OSStatus SecAsn1Decode (     SecAsn1CoderRef _Nonnull coder,     const void * _Nonnull src,     size_t len,     const SecAsn1Template * _Nonnull templates,     void * _Nonnull dest ); ``` |

Modified [SecAsn1DecodeData()](https://developer.apple.com/documentation/security/1428204-secasn1decodedata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1DecodeData (     SecAsn1CoderRef coder,     const SecAsn1Item *src,     const SecAsn1Template *templ,     void *dest ); ``` |
| To | ``` OSStatus SecAsn1DecodeData (     SecAsn1CoderRef _Nonnull coder,     const SecAsn1Item * _Nonnull src,     const SecAsn1Template * _Nonnull templ,     void * _Nonnull dest ); ``` |

Modified [SecAsn1EncodeItem()](https://developer.apple.com/documentation/security/1428195-secasn1encodeitem)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecAsn1EncodeItem (     SecAsn1CoderRef coder,     const void *src,     const SecAsn1Template *templates,     SecAsn1Item *dest ); ``` |
| To | ``` OSStatus SecAsn1EncodeItem (     SecAsn1CoderRef _Nonnull coder,     const void * _Nonnull src,     const SecAsn1Template * _Nonnull templates,     SecAsn1Item * _Nonnull dest ); ``` |

Modified [SecAsn1Malloc()](https://developer.apple.com/documentation/security/1428208-secasn1malloc)

|  | Declaration |
| --- | --- |
| From | ``` void * SecAsn1Malloc (     SecAsn1CoderRef coder,     size_t len ); ``` |
| To | ``` void * _Nonnull SecAsn1Malloc (     SecAsn1CoderRef _Nonnull coder,     size_t len ); ``` |

Modified [SecAsn1OidCompare()](https://developer.apple.com/documentation/security/1428201-secasn1oidcompare)

|  | Declaration |
| --- | --- |
| From | ``` bool SecAsn1OidCompare (     const SecAsn1Oid *oid1,     const SecAsn1Oid *oid2 ); ``` |
| To | ``` bool SecAsn1OidCompare (     const SecAsn1Oid * _Nonnull oid1,     const SecAsn1Oid * _Nonnull oid2 ); ``` |

#### SecBase.h

Modified [SecCopyErrorMessageString()](https://developer.apple.com/documentation/security/1394686-seccopyerrormessagestring)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SecCopyErrorMessageString (     OSStatus status,     void *reserved ); ``` |
| To | ``` CFStringRef _Nullable SecCopyErrorMessageString (     OSStatus status,     void * _Nullable reserved ); ``` |

#### SecCertificate.h

Modified [SecCertificateAddToKeychain()](https://developer.apple.com/documentation/security/1396090-seccertificateaddtokeychain)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateAddToKeychain (     SecCertificateRef certificate,     SecKeychainRef keychain ); ``` |
| To | ``` OSStatus SecCertificateAddToKeychain (     SecCertificateRef _Nonnull certificate,     SecKeychainRef _Nullable keychain ); ``` |

Modified [SecCertificateCopyCommonName()](https://developer.apple.com/documentation/security/1394814-seccertificatecopycommonname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateCopyCommonName (     SecCertificateRef certificate,     CFStringRef *commonName ); ``` |
| To | ``` OSStatus SecCertificateCopyCommonName (     SecCertificateRef _Nonnull certificate,     CFStringRef  _Nullable * _Nonnull commonName ); ``` |

Modified [SecCertificateCopyData()](https://developer.apple.com/documentation/security/1396080-seccertificatecopydata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecCertificateCopyData (     SecCertificateRef certificate ); ``` |
| To | ``` CFDataRef _Nonnull SecCertificateCopyData (     SecCertificateRef _Nonnull certificate ); ``` |

Modified [SecCertificateCopyEmailAddresses()](https://developer.apple.com/documentation/security/1396049-seccertificatecopyemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateCopyEmailAddresses (     SecCertificateRef certificate,     CFArrayRef *emailAddresses ); ``` |
| To | ``` OSStatus SecCertificateCopyEmailAddresses (     SecCertificateRef _Nonnull certificate,     CFArrayRef  _Nullable * _Nonnull emailAddresses ); ``` |

Modified [SecCertificateCopyLongDescription()](https://developer.apple.com/documentation/security/1396088-seccertificatecopylongdescriptio)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SecCertificateCopyLongDescription (     CFAllocatorRef alloc,     SecCertificateRef certificate,     CFErrorRef *error ); ``` |
| To | ``` CFStringRef _Nullable SecCertificateCopyLongDescription (     CFAllocatorRef _Nullable alloc,     SecCertificateRef _Nonnull certificate,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCopyNormalizedIssuerContent()](https://developer.apple.com/documentation/security/1392318-seccertificatecopynormalizedissu)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecCertificateCopyNormalizedIssuerContent (     SecCertificateRef certificate,     CFErrorRef *error ); ``` |
| To | ``` CFDataRef _Nullable SecCertificateCopyNormalizedIssuerContent (     SecCertificateRef _Nonnull certificate,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCopyNormalizedSubjectContent()](https://developer.apple.com/documentation/security/1396030-seccertificatecopynormalizedsubj)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecCertificateCopyNormalizedSubjectContent (     SecCertificateRef certificate,     CFErrorRef *error ); ``` |
| To | ``` CFDataRef _Nullable SecCertificateCopyNormalizedSubjectContent (     SecCertificateRef _Nonnull certificate,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCopyPreference()](https://developer.apple.com/documentation/security/1396094-seccertificatecopypreference)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateCopyPreference (     CFStringRef name,     uint32 keyUsage,     SecCertificateRef *certificate ); ``` |
| To | ``` OSStatus SecCertificateCopyPreference (     CFStringRef _Nonnull name,     uint32 keyUsage,     SecCertificateRef  _Nullable * _Nonnull certificate ); ``` |

Modified [SecCertificateCopyPreferred()](https://developer.apple.com/documentation/security/1396028-seccertificatecopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` SecCertificateRef SecCertificateCopyPreferred (     CFStringRef name,     CFArrayRef keyUsage ); ``` |
| To | ``` SecCertificateRef _Nullable SecCertificateCopyPreferred (     CFStringRef _Nonnull name,     CFArrayRef _Nullable keyUsage ); ``` |

Modified [SecCertificateCopyPublicKey()](https://developer.apple.com/documentation/security/1396096-seccertificatecopypublickey)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateCopyPublicKey (     SecCertificateRef certificate,     SecKeyRef *key ); ``` |
| To | ``` OSStatus SecCertificateCopyPublicKey (     SecCertificateRef _Nonnull certificate,     SecKeyRef  _Nullable * _Nonnull key ); ``` |

Modified [SecCertificateCopySerialNumber()](https://developer.apple.com/documentation/security/1394241-seccertificatecopyserialnumber)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecCertificateCopySerialNumber (     SecCertificateRef certificate,     CFErrorRef *error ); ``` |
| To | ``` CFDataRef _Nullable SecCertificateCopySerialNumber (     SecCertificateRef _Nonnull certificate,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCopyShortDescription()](https://developer.apple.com/documentation/security/1396036-seccertificatecopyshortdescripti)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SecCertificateCopyShortDescription (     CFAllocatorRef alloc,     SecCertificateRef certificate,     CFErrorRef *error ); ``` |
| To | ``` CFStringRef _Nullable SecCertificateCopyShortDescription (     CFAllocatorRef _Nullable alloc,     SecCertificateRef _Nonnull certificate,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCopySubjectSummary()](https://developer.apple.com/documentation/security/1396041-seccertificatecopysubjectsummary)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef SecCertificateCopySubjectSummary (     SecCertificateRef certificate ); ``` |
| To | ``` CFStringRef _Nonnull SecCertificateCopySubjectSummary (     SecCertificateRef _Nonnull certificate ); ``` |

Modified [SecCertificateCopyValues()](https://developer.apple.com/documentation/security/1396051-seccertificatecopyvalues)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SecCertificateCopyValues (     SecCertificateRef certificate,     CFArrayRef keys,     CFErrorRef *error ); ``` |
| To | ``` CFDictionaryRef _Nullable SecCertificateCopyValues (     SecCertificateRef _Nonnull certificate,     CFArrayRef _Nullable keys,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecCertificateCreateFromData()](https://developer.apple.com/documentation/security/1396025-seccertificatecreatefromdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateCreateFromData (     const CSSM_DATA *data,     CSSM_CERT_TYPE type,     CSSM_CERT_ENCODING encoding,     SecCertificateRef *certificate ); ``` |
| To | ``` OSStatus SecCertificateCreateFromData (     const CSSM_DATA * _Nonnull data,     CSSM_CERT_TYPE type,     CSSM_CERT_ENCODING encoding,     SecCertificateRef  _Nullable * _Nonnull certificate ); ``` |

Modified [SecCertificateCreateWithData()](https://developer.apple.com/documentation/security/1396073-seccertificatecreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` SecCertificateRef SecCertificateCreateWithData (     CFAllocatorRef allocator,     CFDataRef data ); ``` |
| To | ``` SecCertificateRef _Nullable SecCertificateCreateWithData (     CFAllocatorRef _Nullable allocator,     CFDataRef _Nonnull data ); ``` |

Modified [SecCertificateGetAlgorithmID()](https://developer.apple.com/documentation/security/1396071-seccertificategetalgorithmid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetAlgorithmID (     SecCertificateRef certificate,     const CSSM_X509_ALGORITHM_IDENTIFIER **algid ); ``` |
| To | ``` OSStatus SecCertificateGetAlgorithmID (     SecCertificateRef _Nonnull certificate,     const CSSM_X509_ALGORITHM_IDENTIFIER * _Nullable * _Nonnull algid ); ``` |

Modified [SecCertificateGetCLHandle()](https://developer.apple.com/documentation/security/1396053-seccertificategetclhandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetCLHandle (     SecCertificateRef certificate,     CSSM_CL_HANDLE *clHandle ); ``` |
| To | ``` OSStatus SecCertificateGetCLHandle (     SecCertificateRef _Nonnull certificate,     CSSM_CL_HANDLE * _Nonnull clHandle ); ``` |

Modified [SecCertificateGetData()](https://developer.apple.com/documentation/security/1396100-seccertificategetdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetData (     SecCertificateRef certificate,     CSSM_DATA_PTR data ); ``` |
| To | ``` OSStatus SecCertificateGetData (     SecCertificateRef _Nonnull certificate,     CSSM_DATA_PTR _Nonnull data ); ``` |

Modified [SecCertificateGetIssuer()](https://developer.apple.com/documentation/security/1396068-seccertificategetissuer)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetIssuer (     SecCertificateRef certificate,     const CSSM_X509_NAME **issuer ); ``` |
| To | ``` OSStatus SecCertificateGetIssuer (     SecCertificateRef _Nonnull certificate,     const CSSM_X509_NAME * _Nullable * _Nonnull issuer ); ``` |

Modified [SecCertificateGetSubject()](https://developer.apple.com/documentation/security/1396032-seccertificategetsubject)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetSubject (     SecCertificateRef certificate,     const CSSM_X509_NAME **subject ); ``` |
| To | ``` OSStatus SecCertificateGetSubject (     SecCertificateRef _Nonnull certificate,     const CSSM_X509_NAME * _Nullable * _Nonnull subject ); ``` |

Modified [SecCertificateGetType()](https://developer.apple.com/documentation/security/1396092-seccertificategettype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateGetType (     SecCertificateRef certificate,     CSSM_CERT_TYPE *certificateType ); ``` |
| To | ``` OSStatus SecCertificateGetType (     SecCertificateRef _Nonnull certificate,     CSSM_CERT_TYPE * _Nonnull certificateType ); ``` |

Modified [SecCertificateSetPreference()](https://developer.apple.com/documentation/security/1396063-seccertificatesetpreference)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateSetPreference (     SecCertificateRef certificate,     CFStringRef name,     uint32 keyUsage,     CFDateRef date ); ``` |
| To | ``` OSStatus SecCertificateSetPreference (     SecCertificateRef _Nonnull certificate,     CFStringRef _Nonnull name,     uint32 keyUsage,     CFDateRef _Nullable date ); ``` |

Modified [SecCertificateSetPreferred()](https://developer.apple.com/documentation/security/1393683-seccertificatesetpreferred)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCertificateSetPreferred (     SecCertificateRef certificate,     CFStringRef name,     CFArrayRef keyUsage ); ``` |
| To | ``` OSStatus SecCertificateSetPreferred (     SecCertificateRef _Nullable certificate,     CFStringRef _Nonnull name,     CFArrayRef _Nullable keyUsage ); ``` |

#### SecCode.h

Added [kSecCodeInfoPlatformIdentifier](https://developer.apple.com/documentation/security/kseccodeinfoplatformidentifier)Modified [SecCodeCheckValidity()](https://developer.apple.com/documentation/security/1396726-seccodecheckvalidity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCheckValidity (     SecCodeRef code,     SecCSFlags flags,     SecRequirementRef requirement ); ``` |
| To | ``` OSStatus SecCodeCheckValidity (     SecCodeRef _Nonnull code,     SecCSFlags flags,     SecRequirementRef _Nullable requirement ); ``` |

Modified [SecCodeCheckValidityWithErrors()](https://developer.apple.com/documentation/security/1395272-seccodecheckvaliditywitherrors)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCheckValidityWithErrors (     SecCodeRef code,     SecCSFlags flags,     SecRequirementRef requirement,     CFErrorRef *errors ); ``` |
| To | ``` OSStatus SecCodeCheckValidityWithErrors (     SecCodeRef _Nonnull code,     SecCSFlags flags,     SecRequirementRef _Nullable requirement,     CFErrorRef  _Nullable * _Nullable errors ); ``` |

Modified [SecCodeCopyDesignatedRequirement()](https://developer.apple.com/documentation/security/1397726-seccodecopydesignatedrequirement)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopyDesignatedRequirement (     SecStaticCodeRef code,     SecCSFlags flags,     SecRequirementRef *requirement ); ``` |
| To | ``` OSStatus SecCodeCopyDesignatedRequirement (     SecStaticCodeRef _Nonnull code,     SecCSFlags flags,     SecRequirementRef  _Nullable * _Nonnull requirement ); ``` |

Modified [SecCodeCopyGuestWithAttributes()](https://developer.apple.com/documentation/security/1395560-seccodecopyguestwithattributes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopyGuestWithAttributes (     SecCodeRef host,     CFDictionaryRef attributes,     SecCSFlags flags,     SecCodeRef *guest ); ``` |
| To | ``` OSStatus SecCodeCopyGuestWithAttributes (     SecCodeRef _Nullable host,     CFDictionaryRef _Nullable attributes,     SecCSFlags flags,     SecCodeRef  _Nullable * _Nonnull guest ); ``` |

Modified [SecCodeCopyHost()](https://developer.apple.com/documentation/security/1398794-seccodecopyhost)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopyHost (     SecCodeRef guest,     SecCSFlags flags,     SecCodeRef *host ); ``` |
| To | ``` OSStatus SecCodeCopyHost (     SecCodeRef _Nonnull guest,     SecCSFlags flags,     SecCodeRef  _Nullable * _Nonnull host ); ``` |

Modified [SecCodeCopyPath()](https://developer.apple.com/documentation/security/1398853-seccodecopypath)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopyPath (     SecStaticCodeRef staticCode,     SecCSFlags flags,     CFURLRef *path ); ``` |
| To | ``` OSStatus SecCodeCopyPath (     SecStaticCodeRef _Nonnull staticCode,     SecCSFlags flags,     CFURLRef  _Nullable * _Nonnull path ); ``` |

Modified [SecCodeCopySelf()](https://developer.apple.com/documentation/security/1402140-seccodecopyself)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopySelf (     SecCSFlags flags,     SecCodeRef *self ); ``` |
| To | ``` OSStatus SecCodeCopySelf (     SecCSFlags flags,     SecCodeRef  _Nullable * _Nonnull self ); ``` |

Modified [SecCodeCopySigningInformation()](https://developer.apple.com/documentation/security/1395809-seccodecopysigninginformation)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopySigningInformation (     SecStaticCodeRef code,     SecCSFlags flags,     CFDictionaryRef *information ); ``` |
| To | ``` OSStatus SecCodeCopySigningInformation (     SecStaticCodeRef _Nonnull code,     SecCSFlags flags,     CFDictionaryRef  _Nullable * _Nonnull information ); ``` |

Modified [SecCodeCopyStaticCode()](https://developer.apple.com/documentation/security/1401695-seccodecopystaticcode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeCopyStaticCode (     SecCodeRef code,     SecCSFlags flags,     SecStaticCodeRef *staticCode ); ``` |
| To | ``` OSStatus SecCodeCopyStaticCode (     SecCodeRef _Nonnull code,     SecCSFlags flags,     SecStaticCodeRef  _Nullable * _Nonnull staticCode ); ``` |

Modified [SecCodeMapMemory()](https://developer.apple.com/documentation/security/1393719-seccodemapmemory)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecCodeMapMemory (     SecStaticCodeRef code,     SecCSFlags flags ); ``` |
| To | ``` OSStatus SecCodeMapMemory (     SecStaticCodeRef _Nonnull code,     SecCSFlags flags ); ``` |

#### SecCodeHost.h

Modified [SecHostCreateGuest()](https://developer.apple.com/documentation/security/1396597-sechostcreateguest)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecHostCreateGuest (     SecGuestRef host,     uint32_t status,     CFURLRef path,     CFDictionaryRef attributes,     SecCSFlags flags,     SecGuestRef *newGuest ); ``` |
| To | ``` OSStatus SecHostCreateGuest (     SecGuestRef host,     uint32_t status,     CFURLRef _Nonnull path,     CFDictionaryRef _Nullable attributes,     SecCSFlags flags,     SecGuestRef * _Nonnull newGuest ); ``` |

Modified [SecHostSelectedGuest()](https://developer.apple.com/documentation/security/1396527-sechostselectedguest)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecHostSelectedGuest (     SecCSFlags flags,     SecGuestRef *guestRef ); ``` |
| To | ``` OSStatus SecHostSelectedGuest (     SecCSFlags flags,     SecGuestRef * _Nonnull guestRef ); ``` |

Modified [SecHostSetGuestStatus()](https://developer.apple.com/documentation/security/1397494-sechostsetgueststatus)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecHostSetGuestStatus (     SecGuestRef guestRef,     uint32_t status,     CFDictionaryRef attributes,     SecCSFlags flags ); ``` |
| To | ``` OSStatus SecHostSetGuestStatus (     SecGuestRef guestRef,     uint32_t status,     CFDictionaryRef _Nullable attributes,     SecCSFlags flags ); ``` |

#### SecCustomTransform.h

Modified [SecTranformCustomGetAttribute()](https://developer.apple.com/documentation/security/1552632-sectranformcustomgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTranformCustomGetAttribute (     SecTransformImplementationRef ref,     SecTransformStringOrAttributeRef attribute,     SecTransformMetaAttributeType type ); ``` |
| To | ``` CFTypeRef _Nullable SecTranformCustomGetAttribute (     SecTransformImplementationRef _Nonnull ref,     SecTransformStringOrAttributeRef _Nonnull attribute,     SecTransformMetaAttributeType type ); ``` |

Modified [SecTransformCreate()](https://developer.apple.com/documentation/security/1395256-sectransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecTransformCreate (     CFStringRef name,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecTransformCreate (     CFStringRef _Nonnull name,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTransformCustomGetAttribute()](https://developer.apple.com/documentation/security/1397766-sectransformcustomgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformCustomGetAttribute (     SecTransformImplementationRef ref,     SecTransformStringOrAttributeRef attribute,     SecTransformMetaAttributeType type ); ``` |
| To | ``` CFTypeRef _Nullable SecTransformCustomGetAttribute (     SecTransformImplementationRef _Nonnull ref,     SecTransformStringOrAttributeRef _Nonnull attribute,     SecTransformMetaAttributeType type ); ``` |

Modified [SecTransformCustomSetAttribute()](https://developer.apple.com/documentation/security/1392556-sectransformcustomsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformCustomSetAttribute (     SecTransformImplementationRef ref,     SecTransformStringOrAttributeRef attribute,     SecTransformMetaAttributeType type,     CFTypeRef value ); ``` |
| To | ``` CFTypeRef _Nullable SecTransformCustomSetAttribute (     SecTransformImplementationRef _Nonnull ref,     SecTransformStringOrAttributeRef _Nonnull attribute,     SecTransformMetaAttributeType type,     CFTypeRef _Nullable value ); ``` |

Modified [SecTransformNoData()](https://developer.apple.com/documentation/security/1393788-sectransformnodata)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformNoData (     void ); ``` |
| To | ``` CFTypeRef _Nonnull SecTransformNoData (     void ); ``` |

Modified [SecTransformPushbackAttribute()](https://developer.apple.com/documentation/security/1400559-sectransformpushbackattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformPushbackAttribute (     SecTransformImplementationRef ref,     SecTransformStringOrAttributeRef attribute,     CFTypeRef value ); ``` |
| To | ``` CFTypeRef _Nullable SecTransformPushbackAttribute (     SecTransformImplementationRef _Nonnull ref,     SecTransformStringOrAttributeRef _Nonnull attribute,     CFTypeRef _Nonnull value ); ``` |

Modified [SecTransformRegister()](https://developer.apple.com/documentation/security/1393997-sectransformregister)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SecTransformRegister (     CFStringRef uniqueName,     SecTransformCreateFP createTransformFunction,     CFErrorRef *error ); ``` |
| To | ``` Boolean SecTransformRegister (     CFStringRef _Nonnull uniqueName,     SecTransformCreateFP _Nonnull createTransformFunction,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTransformSetAttributeAction()](https://developer.apple.com/documentation/security/1396035-sectransformsetattributeaction)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef SecTransformSetAttributeAction (     SecTransformImplementationRef ref,     CFStringRef action,     SecTransformStringOrAttributeRef attribute,     SecTransformAttributeActionBlock newAction ); ``` |
| To | ``` CFErrorRef _Nullable SecTransformSetAttributeAction (     SecTransformImplementationRef _Nonnull ref,     CFStringRef _Nonnull action,     SecTransformStringOrAttributeRef _Nullable attribute,     SecTransformAttributeActionBlock _Nonnull newAction ); ``` |

Modified [SecTransformSetDataAction()](https://developer.apple.com/documentation/security/1399597-sectransformsetdataaction)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef SecTransformSetDataAction (     SecTransformImplementationRef ref,     CFStringRef action,     SecTransformDataBlock newAction ); ``` |
| To | ``` CFErrorRef _Nullable SecTransformSetDataAction (     SecTransformImplementationRef _Nonnull ref,     CFStringRef _Nonnull action,     SecTransformDataBlock _Nonnull newAction ); ``` |

Modified [SecTransformSetTransformAction()](https://developer.apple.com/documentation/security/1402097-sectransformsettransformaction)

|  | Declaration |
| --- | --- |
| From | ``` CFErrorRef SecTransformSetTransformAction (     SecTransformImplementationRef ref,     CFStringRef action,     SecTransformActionBlock newAction ); ``` |
| To | ``` CFErrorRef _Nullable SecTransformSetTransformAction (     SecTransformImplementationRef _Nonnull ref,     CFStringRef _Nonnull action,     SecTransformActionBlock _Nonnull newAction ); ``` |

#### SecDecodeTransform.h

Modified [SecDecodeTransformCreate()](https://developer.apple.com/documentation/security/1395244-secdecodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecDecodeTransformCreate (     CFTypeRef DecodeType,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecDecodeTransformCreate (     CFTypeRef _Nonnull DecodeType,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecDigestTransform.h

Modified [SecDigestTransformCreate()](https://developer.apple.com/documentation/security/1394846-secdigesttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecDigestTransformCreate (     CFTypeRef digestType,     CFIndex digestLength,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nonnull SecDigestTransformCreate (     CFTypeRef _Nullable digestType,     CFIndex digestLength,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecEncodeTransform.h

Modified [SecEncodeTransformCreate()](https://developer.apple.com/documentation/security/1399382-secencodetransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecEncodeTransformCreate (     CFTypeRef encodeType,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecEncodeTransformCreate (     CFTypeRef _Nonnull encodeType,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecEncryptTransform.h

Modified [SecDecryptTransformCreate()](https://developer.apple.com/documentation/security/1399526-secdecrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecDecryptTransformCreate (     SecKeyRef keyRef,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nonnull SecDecryptTransformCreate (     SecKeyRef _Nonnull keyRef,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecEncryptTransformCreate()](https://developer.apple.com/documentation/security/1399605-secencrypttransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecEncryptTransformCreate (     SecKeyRef keyRef,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nonnull SecEncryptTransformCreate (     SecKeyRef _Nonnull keyRef,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecIdentity.h

Modified [SecIdentityCopyCertificate()](https://developer.apple.com/documentation/security/1401305-secidentitycopycertificate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentityCopyCertificate (     SecIdentityRef identityRef,     SecCertificateRef *certificateRef ); ``` |
| To | ``` OSStatus SecIdentityCopyCertificate (     SecIdentityRef _Nonnull identityRef,     SecCertificateRef  _Nullable * _Nonnull certificateRef ); ``` |

Modified [SecIdentityCopyPreference()](https://developer.apple.com/documentation/security/1543662-secidentitycopypreference)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentityCopyPreference (     CFStringRef name,     CSSM_KEYUSE keyUsage,     CFArrayRef validIssuers,     SecIdentityRef *identity ); ``` |
| To | ``` OSStatus SecIdentityCopyPreference (     CFStringRef _Nonnull name,     CSSM_KEYUSE keyUsage,     CFArrayRef _Nullable validIssuers,     SecIdentityRef  _Nullable * _Nonnull identity ); ``` |

Modified [SecIdentityCopyPreferred()](https://developer.apple.com/documentation/security/1399556-secidentitycopypreferred)

|  | Declaration |
| --- | --- |
| From | ``` SecIdentityRef SecIdentityCopyPreferred (     CFStringRef name,     CFArrayRef keyUsage,     CFArrayRef validIssuers ); ``` |
| To | ``` SecIdentityRef _Nullable SecIdentityCopyPreferred (     CFStringRef _Nonnull name,     CFArrayRef _Nullable keyUsage,     CFArrayRef _Nullable validIssuers ); ``` |

Modified [SecIdentityCopyPrivateKey()](https://developer.apple.com/documentation/security/1392978-secidentitycopyprivatekey)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentityCopyPrivateKey (     SecIdentityRef identityRef,     SecKeyRef *privateKeyRef ); ``` |
| To | ``` OSStatus SecIdentityCopyPrivateKey (     SecIdentityRef _Nonnull identityRef,     SecKeyRef  _Nullable * _Nonnull privateKeyRef ); ``` |

Modified [SecIdentityCopySystemIdentity()](https://developer.apple.com/documentation/security/1393646-secidentitycopysystemidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentityCopySystemIdentity (     CFStringRef domain,     SecIdentityRef *idRef,     CFStringRef *actualDomain ); ``` |
| To | ``` OSStatus SecIdentityCopySystemIdentity (     CFStringRef _Nonnull domain,     SecIdentityRef  _Nullable * _Nonnull idRef,     CFStringRef  _Nullable * _Nullable actualDomain ); ``` |

Modified [SecIdentityCreateWithCertificate()](https://developer.apple.com/documentation/security/1401160-secidentitycreatewithcertificate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentityCreateWithCertificate (     CFTypeRef keychainOrArray,     SecCertificateRef certificateRef,     SecIdentityRef *identityRef ); ``` |
| To | ``` OSStatus SecIdentityCreateWithCertificate (     CFTypeRef _Nullable keychainOrArray,     SecCertificateRef _Nonnull certificateRef,     SecIdentityRef  _Nullable * _Nonnull identityRef ); ``` |

Modified [SecIdentitySetPreference()](https://developer.apple.com/documentation/security/1543664-secidentitysetpreference)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentitySetPreference (     SecIdentityRef identity,     CFStringRef name,     CSSM_KEYUSE keyUsage ); ``` |
| To | ``` OSStatus SecIdentitySetPreference (     SecIdentityRef _Nonnull identity,     CFStringRef _Nonnull name,     CSSM_KEYUSE keyUsage ); ``` |

Modified [SecIdentitySetPreferred()](https://developer.apple.com/documentation/security/1395862-secidentitysetpreferred)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentitySetPreferred (     SecIdentityRef identity,     CFStringRef name,     CFArrayRef keyUsage ); ``` |
| To | ``` OSStatus SecIdentitySetPreferred (     SecIdentityRef _Nullable identity,     CFStringRef _Nonnull name,     CFArrayRef _Nullable keyUsage ); ``` |

Modified [SecIdentitySetSystemIdentity()](https://developer.apple.com/documentation/security/1398082-secidentitysetsystemidentity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentitySetSystemIdentity (     CFStringRef domain,     SecIdentityRef idRef ); ``` |
| To | ``` OSStatus SecIdentitySetSystemIdentity (     CFStringRef _Nonnull domain,     SecIdentityRef _Nullable idRef ); ``` |

#### SecIdentitySearch.h

Modified [SecIdentitySearchCopyNext()](https://developer.apple.com/documentation/security/1396825-secidentitysearchcopynext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentitySearchCopyNext (     SecIdentitySearchRef searchRef,     SecIdentityRef *identity ); ``` |
| To | ``` OSStatus SecIdentitySearchCopyNext (     SecIdentitySearchRef _Nonnull searchRef,     SecIdentityRef  _Nullable * _Nullable identity ); ``` |

Modified [SecIdentitySearchCreate()](https://developer.apple.com/documentation/security/1396821-secidentitysearchcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecIdentitySearchCreate (     CFTypeRef keychainOrArray,     CSSM_KEYUSE keyUsage,     SecIdentitySearchRef *searchRef ); ``` |
| To | ``` OSStatus SecIdentitySearchCreate (     CFTypeRef _Nullable keychainOrArray,     CSSM_KEYUSE keyUsage,     SecIdentitySearchRef  _Nullable * _Nullable searchRef ); ``` |

#### SecImportExport.h

Modified [SecItemExport()](https://developer.apple.com/documentation/security/1394828-secitemexport)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemExport (     CFTypeRef secItemOrArray,     SecExternalFormat outputFormat,     SecItemImportExportFlags flags,     const SecItemImportExportKeyParameters *keyParams,     CFDataRef *exportedData ); ``` |
| To | ``` OSStatus SecItemExport (     CFTypeRef _Nonnull secItemOrArray,     SecExternalFormat outputFormat,     SecItemImportExportFlags flags,     const SecItemImportExportKeyParameters * _Nullable keyParams,     CFDataRef  _Nullable * _Nonnull exportedData ); ``` |

Modified [SecItemImport()](https://developer.apple.com/documentation/security/1395728-secitemimport)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemImport (     CFDataRef importedData,     CFStringRef fileNameOrExtension,     SecExternalFormat *inputFormat,     SecExternalItemType *itemType,     SecItemImportExportFlags flags,     const SecItemImportExportKeyParameters *keyParams,     SecKeychainRef importKeychain,     CFArrayRef *outItems ); ``` |
| To | ``` OSStatus SecItemImport (     CFDataRef _Nonnull importedData,     CFStringRef _Nullable fileNameOrExtension,     SecExternalFormat * _Nullable inputFormat,     SecExternalItemType * _Nullable itemType,     SecItemImportExportFlags flags,     const SecItemImportExportKeyParameters * _Nullable keyParams,     SecKeychainRef _Nullable importKeychain,     CFArrayRef  _Nullable * _Nullable outItems ); ``` |

Modified [SecKeychainItemExport()](https://developer.apple.com/documentation/security/1412386-seckeychainitemexport)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemExport (     CFTypeRef keychainItemOrArray,     SecExternalFormat outputFormat,     SecItemImportExportFlags flags,     const SecKeyImportExportParameters *keyParams,     CFDataRef *exportedData ); ``` |
| To | ``` OSStatus SecKeychainItemExport (     CFTypeRef _Nonnull keychainItemOrArray,     SecExternalFormat outputFormat,     SecItemImportExportFlags flags,     const SecKeyImportExportParameters * _Nullable keyParams,     CFDataRef  _Nullable * _Nonnull exportedData ); ``` |

Modified [SecKeychainItemImport()](https://developer.apple.com/documentation/security/1412415-seckeychainitemimport)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemImport (     CFDataRef importedData,     CFStringRef fileNameOrExtension,     SecExternalFormat *inputFormat,     SecExternalItemType *itemType,     SecItemImportExportFlags flags,     const SecKeyImportExportParameters *keyParams,     SecKeychainRef importKeychain,     CFArrayRef *outItems ); ``` |
| To | ``` OSStatus SecKeychainItemImport (     CFDataRef _Nonnull importedData,     CFStringRef _Nullable fileNameOrExtension,     SecExternalFormat * _Nullable inputFormat,     SecExternalItemType * _Nullable itemType,     SecItemImportExportFlags flags,     const SecKeyImportExportParameters * _Nullable keyParams,     SecKeychainRef _Nullable importKeychain,     CFArrayRef  _Nullable * _Nullable outItems ); ``` |

Modified [SecPKCS12Import()](https://developer.apple.com/documentation/security/1396915-secpkcs12import)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPKCS12Import (     CFDataRef pkcs12_data,     CFDictionaryRef options,     CFArrayRef *items ); ``` |
| To | ``` OSStatus SecPKCS12Import (     CFDataRef _Nonnull pkcs12_data,     CFDictionaryRef _Nonnull options,     CFArrayRef  _Nullable * _Nonnull items ); ``` |

#### SecItem.h

Added [kSecUseAuthenticationContext](https://developer.apple.com/documentation/security/ksecuseauthenticationcontext)Added [kSecUseAuthenticationUI](https://developer.apple.com/documentation/security/ksecuseauthenticationui)Added [kSecUseAuthenticationUIAllow](https://developer.apple.com/documentation/security/ksecuseauthenticationuiallow)Added [kSecUseAuthenticationUIFail](https://developer.apple.com/documentation/security/ksecuseauthenticationuifail)Added [kSecUseAuthenticationUISkip](https://developer.apple.com/documentation/security/ksecuseauthenticationuiskip)Added [kSecUseOperationPrompt](https://developer.apple.com/documentation/security/ksecuseoperationprompt)Modified [SecItemAdd()](https://developer.apple.com/documentation/security/1401659-secitemadd)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemAdd (     CFDictionaryRef attributes,     CFTypeRef *result ); ``` |
| To | ``` OSStatus SecItemAdd (     CFDictionaryRef _Nonnull attributes,     CFTypeRef  _Nullable * _Nullable result ); ``` |

Modified [SecItemCopyMatching()](https://developer.apple.com/documentation/security/1398306-secitemcopymatching)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemCopyMatching (     CFDictionaryRef query,     CFTypeRef *result ); ``` |
| To | ``` OSStatus SecItemCopyMatching (     CFDictionaryRef _Nonnull query,     CFTypeRef  _Nullable * _Nullable result ); ``` |

Modified [SecItemDelete()](https://developer.apple.com/documentation/security/1395547-secitemdelete)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemDelete (     CFDictionaryRef query ); ``` |
| To | ``` OSStatus SecItemDelete (     CFDictionaryRef _Nonnull query ); ``` |

Modified [SecItemUpdate()](https://developer.apple.com/documentation/security/1393617-secitemupdate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecItemUpdate (     CFDictionaryRef query,     CFDictionaryRef attributesToUpdate ); ``` |
| To | ``` OSStatus SecItemUpdate (     CFDictionaryRef _Nonnull query,     CFDictionaryRef _Nonnull attributesToUpdate ); ``` |

#### SecKey.h

Added [kSecPaddingSigRaw](https://developer.apple.com/documentation/security/secpadding/1401132-sigraw)Modified [SecKeyCreateFromData()](https://developer.apple.com/documentation/security/1393853-seckeycreatefromdata)

|  | Declaration |
| --- | --- |
| From | ``` SecKeyRef SecKeyCreateFromData (     CFDictionaryRef parameters,     CFDataRef keyData,     CFErrorRef *error ); ``` |
| To | ``` SecKeyRef _Nullable SecKeyCreateFromData (     CFDictionaryRef _Nonnull parameters,     CFDataRef _Nonnull keyData,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecKeyCreatePair()](https://developer.apple.com/documentation/security/1495765-seckeycreatepair)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyCreatePair (     SecKeychainRef keychainRef,     CSSM_ALGORITHMS algorithm,     uint32 keySizeInBits,     CSSM_CC_HANDLE contextHandle,     CSSM_KEYUSE publicKeyUsage,     uint32 publicKeyAttr,     CSSM_KEYUSE privateKeyUsage,     uint32 privateKeyAttr,     SecAccessRef initialAccess,     SecKeyRef *publicKey,     SecKeyRef *privateKey ); ``` |
| To | ``` OSStatus SecKeyCreatePair (     SecKeychainRef _Nullable keychainRef,     CSSM_ALGORITHMS algorithm,     uint32 keySizeInBits,     CSSM_CC_HANDLE contextHandle,     CSSM_KEYUSE publicKeyUsage,     uint32 publicKeyAttr,     CSSM_KEYUSE privateKeyUsage,     uint32 privateKeyAttr,     SecAccessRef _Nullable initialAccess,     SecKeyRef  _Nullable * _Nullable publicKey,     SecKeyRef  _Nullable * _Nullable privateKey ); ``` |

Modified [SecKeyDeriveFromPassword()](https://developer.apple.com/documentation/security/1395028-seckeyderivefrompassword)

|  | Declaration |
| --- | --- |
| From | ``` SecKeyRef SecKeyDeriveFromPassword (     CFStringRef password,     CFDictionaryRef parameters,     CFErrorRef *error ); ``` |
| To | ``` SecKeyRef _Nullable SecKeyDeriveFromPassword (     CFStringRef _Nonnull password,     CFDictionaryRef _Nonnull parameters,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecKeyGenerate()](https://developer.apple.com/documentation/security/1495754-seckeygenerate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyGenerate (     SecKeychainRef keychainRef,     CSSM_ALGORITHMS algorithm,     uint32 keySizeInBits,     CSSM_CC_HANDLE contextHandle,     CSSM_KEYUSE keyUsage,     uint32 keyAttr,     SecAccessRef initialAccess,     SecKeyRef *keyRef ); ``` |
| To | ``` OSStatus SecKeyGenerate (     SecKeychainRef _Nullable keychainRef,     CSSM_ALGORITHMS algorithm,     uint32 keySizeInBits,     CSSM_CC_HANDLE contextHandle,     CSSM_KEYUSE keyUsage,     uint32 keyAttr,     SecAccessRef _Nullable initialAccess,     SecKeyRef  _Nullable * _Nullable keyRef ); ``` |

Modified [SecKeyGeneratePair()](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyGeneratePair (     CFDictionaryRef parameters,     SecKeyRef *publicKey,     SecKeyRef *privateKey ); ``` |
| To | ``` OSStatus SecKeyGeneratePair (     CFDictionaryRef _Nonnull parameters,     SecKeyRef  _Nullable * _Nullable publicKey,     SecKeyRef  _Nullable * _Nullable privateKey ); ``` |

Modified [SecKeyGeneratePairAsync()](https://developer.apple.com/documentation/security/1394698-seckeygeneratepairasync)

|  | Declaration |
| --- | --- |
| From | ``` void SecKeyGeneratePairAsync (     CFDictionaryRef parameters,     dispatch_queue_t deliveryQueue,     SecKeyGeneratePairBlock result ); ``` |
| To | ``` void SecKeyGeneratePairAsync (     CFDictionaryRef _Nonnull parameters,     dispatch_queue_t _Nonnull deliveryQueue,     SecKeyGeneratePairBlock _Nonnull result ); ``` |

Modified [SecKeyGenerateSymmetric()](https://developer.apple.com/documentation/security/1401861-seckeygeneratesymmetric)

|  | Declaration |
| --- | --- |
| From | ``` SecKeyRef SecKeyGenerateSymmetric (     CFDictionaryRef parameters,     CFErrorRef *error ); ``` |
| To | ``` SecKeyRef _Nullable SecKeyGenerateSymmetric (     CFDictionaryRef _Nonnull parameters,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecKeyGetBlockSize()](https://developer.apple.com/documentation/security/1394222-seckeygetblocksize)

|  | Declaration |
| --- | --- |
| From | ``` size_t SecKeyGetBlockSize (     SecKeyRef key ); ``` |
| To | ``` size_t SecKeyGetBlockSize (     SecKeyRef _Nonnull key ); ``` |

Modified [SecKeyGetCredentials()](https://developer.apple.com/documentation/security/1495756-seckeygetcredentials)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyGetCredentials (     SecKeyRef keyRef,     CSSM_ACL_AUTHORIZATION_TAG operation,     SecCredentialType credentialType,     const CSSM_ACCESS_CREDENTIALS **outCredentials ); ``` |
| To | ``` OSStatus SecKeyGetCredentials (     SecKeyRef _Nonnull keyRef,     CSSM_ACL_AUTHORIZATION_TAG operation,     SecCredentialType credentialType,     const CSSM_ACCESS_CREDENTIALS * _Nullable * _Nonnull outCredentials ); ``` |

Modified [SecKeyGetCSPHandle()](https://developer.apple.com/documentation/security/1495747-seckeygetcsphandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyGetCSPHandle (     SecKeyRef keyRef,     CSSM_CSP_HANDLE *cspHandle ); ``` |
| To | ``` OSStatus SecKeyGetCSPHandle (     SecKeyRef _Nonnull keyRef,     CSSM_CSP_HANDLE * _Nonnull cspHandle ); ``` |

Modified [SecKeyGetCSSMKey()](https://developer.apple.com/documentation/security/1495763-seckeygetcssmkey)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeyGetCSSMKey (     SecKeyRef key,     const CSSM_KEY **cssmKey ); ``` |
| To | ``` OSStatus SecKeyGetCSSMKey (     SecKeyRef _Nonnull key,     const CSSM_KEY * _Nullable * _Nonnull cssmKey ); ``` |

Modified [SecKeyUnwrapSymmetric()](https://developer.apple.com/documentation/security/1394725-seckeyunwrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` SecKeyRef SecKeyUnwrapSymmetric (     CFDataRef *keyToUnwrap,     SecKeyRef unwrappingKey,     CFDictionaryRef parameters,     CFErrorRef *error ); ``` |
| To | ``` SecKeyRef _Nullable SecKeyUnwrapSymmetric (     CFDataRef  _Nullable * _Nonnull keyToUnwrap,     SecKeyRef _Nonnull unwrappingKey,     CFDictionaryRef _Nonnull parameters,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecKeyWrapSymmetric()](https://developer.apple.com/documentation/security/1396734-seckeywrapsymmetric)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecKeyWrapSymmetric (     SecKeyRef keyToWrap,     SecKeyRef wrappingKey,     CFDictionaryRef parameters,     CFErrorRef *error ); ``` |
| To | ``` CFDataRef _Nullable SecKeyWrapSymmetric (     SecKeyRef _Nonnull keyToWrap,     SecKeyRef _Nonnull wrappingKey,     CFDictionaryRef _Nonnull parameters,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecKeychain.h

Modified [SecKeychainAddCallback()](https://developer.apple.com/documentation/security/1394998-seckeychainaddcallback)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainAddCallback (     SecKeychainCallback callbackFunction,     SecKeychainEventMask eventMask,     void *userContext ); ``` |
| To | ``` OSStatus SecKeychainAddCallback (     SecKeychainCallback _Nonnull callbackFunction,     SecKeychainEventMask eventMask,     void * _Nullable userContext ); ``` |

Modified [SecKeychainAddGenericPassword()](https://developer.apple.com/documentation/security/1398366-seckeychainaddgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainAddGenericPassword (     SecKeychainRef keychain,     UInt32 serviceNameLength,     const char *serviceName,     UInt32 accountNameLength,     const char *accountName,     UInt32 passwordLength,     const void *passwordData,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainAddGenericPassword (     SecKeychainRef _Nullable keychain,     UInt32 serviceNameLength,     const char * _Nullable serviceName,     UInt32 accountNameLength,     const char * _Nullable accountName,     UInt32 passwordLength,     const void * _Nonnull passwordData,     SecKeychainItemRef  _Nullable * _Nullable itemRef ); ``` |

Modified [SecKeychainAddInternetPassword()](https://developer.apple.com/documentation/security/1393322-seckeychainaddinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainAddInternetPassword (     SecKeychainRef keychain,     UInt32 serverNameLength,     const char *serverName,     UInt32 securityDomainLength,     const char *securityDomain,     UInt32 accountNameLength,     const char *accountName,     UInt32 pathLength,     const char *path,     UInt16 port,     SecProtocolType protocol,     SecAuthenticationType authenticationType,     UInt32 passwordLength,     const void *passwordData,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainAddInternetPassword (     SecKeychainRef _Nullable keychain,     UInt32 serverNameLength,     const char * _Nullable serverName,     UInt32 securityDomainLength,     const char * _Nullable securityDomain,     UInt32 accountNameLength,     const char * _Nullable accountName,     UInt32 pathLength,     const char * _Nullable path,     UInt16 port,     SecProtocolType protocol,     SecAuthenticationType authenticationType,     UInt32 passwordLength,     const void * _Nonnull passwordData,     SecKeychainItemRef  _Nullable * _Nullable itemRef ); ``` |

Modified [SecKeychainAttributeInfoForItemID()](https://developer.apple.com/documentation/security/1392372-seckeychainattributeinfoforitemi)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainAttributeInfoForItemID (     SecKeychainRef keychain,     UInt32 itemID,     SecKeychainAttributeInfo **info ); ``` |
| To | ``` OSStatus SecKeychainAttributeInfoForItemID (     SecKeychainRef _Nullable keychain,     UInt32 itemID,     SecKeychainAttributeInfo * _Nullable * _Nonnull info ); ``` |

Modified [SecKeychainCopyAccess()](https://developer.apple.com/documentation/security/1394733-seckeychaincopyaccess)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopyAccess (     SecKeychainRef keychain,     SecAccessRef *access ); ``` |
| To | ``` OSStatus SecKeychainCopyAccess (     SecKeychainRef _Nullable keychain,     SecAccessRef  _Nullable * _Nonnull access ); ``` |

Modified [SecKeychainCopyDefault()](https://developer.apple.com/documentation/security/1400743-seckeychaincopydefault)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopyDefault (     SecKeychainRef *keychain ); ``` |
| To | ``` OSStatus SecKeychainCopyDefault (     SecKeychainRef  _Nullable * _Nonnull keychain ); ``` |

Modified [SecKeychainCopyDomainDefault()](https://developer.apple.com/documentation/security/1401993-seckeychaincopydomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopyDomainDefault (     SecPreferencesDomain domain,     SecKeychainRef *keychain ); ``` |
| To | ``` OSStatus SecKeychainCopyDomainDefault (     SecPreferencesDomain domain,     SecKeychainRef  _Nullable * _Nonnull keychain ); ``` |

Modified [SecKeychainCopyDomainSearchList()](https://developer.apple.com/documentation/security/1396688-seckeychaincopydomainsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopyDomainSearchList (     SecPreferencesDomain domain,     CFArrayRef *searchList ); ``` |
| To | ``` OSStatus SecKeychainCopyDomainSearchList (     SecPreferencesDomain domain,     CFArrayRef  _Nullable * _Nonnull searchList ); ``` |

Modified [SecKeychainCopySearchList()](https://developer.apple.com/documentation/security/1402440-seckeychaincopysearchlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopySearchList (     CFArrayRef *searchList ); ``` |
| To | ``` OSStatus SecKeychainCopySearchList (     CFArrayRef  _Nullable * _Nonnull searchList ); ``` |

Modified [SecKeychainCopySettings()](https://developer.apple.com/documentation/security/1395746-seckeychaincopysettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCopySettings (     SecKeychainRef keychain,     SecKeychainSettings *outSettings ); ``` |
| To | ``` OSStatus SecKeychainCopySettings (     SecKeychainRef _Nullable keychain,     SecKeychainSettings * _Nonnull outSettings ); ``` |

Modified [SecKeychainCreate()](https://developer.apple.com/documentation/security/1401214-seckeychaincreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainCreate (     const char *pathName,     UInt32 passwordLength,     const void *password,     Boolean promptUser,     SecAccessRef initialAccess,     SecKeychainRef *keychain ); ``` |
| To | ``` OSStatus SecKeychainCreate (     const char * _Nonnull pathName,     UInt32 passwordLength,     const void * _Nullable password,     Boolean promptUser,     SecAccessRef _Nullable initialAccess,     SecKeychainRef  _Nullable * _Nonnull keychain ); ``` |

Modified [SecKeychainDelete()](https://developer.apple.com/documentation/security/1395206-seckeychaindelete)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainDelete (     SecKeychainRef keychainOrArray ); ``` |
| To | ``` OSStatus SecKeychainDelete (     SecKeychainRef _Nullable keychainOrArray ); ``` |

Modified [SecKeychainFindGenericPassword()](https://developer.apple.com/documentation/security/1397301-seckeychainfindgenericpassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainFindGenericPassword (     CFTypeRef keychainOrArray,     UInt32 serviceNameLength,     const char *serviceName,     UInt32 accountNameLength,     const char *accountName,     UInt32 *passwordLength,     void **passwordData,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainFindGenericPassword (     CFTypeRef _Nullable keychainOrArray,     UInt32 serviceNameLength,     const char * _Nullable serviceName,     UInt32 accountNameLength,     const char * _Nullable accountName,     UInt32 * _Nullable passwordLength,     void * _Nullable * _Nullable passwordData,     SecKeychainItemRef  _Nullable * _Nullable itemRef ); ``` |

Modified [SecKeychainFindInternetPassword()](https://developer.apple.com/documentation/security/1397763-seckeychainfindinternetpassword)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainFindInternetPassword (     CFTypeRef keychainOrArray,     UInt32 serverNameLength,     const char *serverName,     UInt32 securityDomainLength,     const char *securityDomain,     UInt32 accountNameLength,     const char *accountName,     UInt32 pathLength,     const char *path,     UInt16 port,     SecProtocolType protocol,     SecAuthenticationType authenticationType,     UInt32 *passwordLength,     void **passwordData,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainFindInternetPassword (     CFTypeRef _Nullable keychainOrArray,     UInt32 serverNameLength,     const char * _Nullable serverName,     UInt32 securityDomainLength,     const char * _Nullable securityDomain,     UInt32 accountNameLength,     const char * _Nullable accountName,     UInt32 pathLength,     const char * _Nullable path,     UInt16 port,     SecProtocolType protocol,     SecAuthenticationType authenticationType,     UInt32 * _Nullable passwordLength,     void * _Nullable * _Nullable passwordData,     SecKeychainItemRef  _Nullable * _Nullable itemRef ); ``` |

Modified [SecKeychainFreeAttributeInfo()](https://developer.apple.com/documentation/security/1400217-seckeychainfreeattributeinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainFreeAttributeInfo (     SecKeychainAttributeInfo *info ); ``` |
| To | ``` OSStatus SecKeychainFreeAttributeInfo (     SecKeychainAttributeInfo * _Nonnull info ); ``` |

Modified [SecKeychainGetCSPHandle()](https://developer.apple.com/documentation/security/1536084-seckeychaingetcsphandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetCSPHandle (     SecKeychainRef keychain,     CSSM_CSP_HANDLE *cspHandle ); ``` |
| To | ``` OSStatus SecKeychainGetCSPHandle (     SecKeychainRef _Nullable keychain,     CSSM_CSP_HANDLE * _Nonnull cspHandle ); ``` |

Modified [SecKeychainGetDLDBHandle()](https://developer.apple.com/documentation/security/1536077-seckeychaingetdldbhandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetDLDBHandle (     SecKeychainRef keychain,     CSSM_DL_DB_HANDLE *dldbHandle ); ``` |
| To | ``` OSStatus SecKeychainGetDLDBHandle (     SecKeychainRef _Nullable keychain,     CSSM_DL_DB_HANDLE * _Nonnull dldbHandle ); ``` |

Modified [SecKeychainGetPath()](https://developer.apple.com/documentation/security/1401073-seckeychaingetpath)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetPath (     SecKeychainRef keychain,     UInt32 *ioPathLength,     char *pathName ); ``` |
| To | ``` OSStatus SecKeychainGetPath (     SecKeychainRef _Nullable keychain,     UInt32 * _Nonnull ioPathLength,     char * _Nonnull pathName ); ``` |

Modified [SecKeychainGetPreferenceDomain()](https://developer.apple.com/documentation/security/1397034-seckeychaingetpreferencedomain)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetPreferenceDomain (     SecPreferencesDomain *domain ); ``` |
| To | ``` OSStatus SecKeychainGetPreferenceDomain (     SecPreferencesDomain * _Nonnull domain ); ``` |

Modified [SecKeychainGetStatus()](https://developer.apple.com/documentation/security/1399085-seckeychaingetstatus)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetStatus (     SecKeychainRef keychain,     SecKeychainStatus *keychainStatus ); ``` |
| To | ``` OSStatus SecKeychainGetStatus (     SecKeychainRef _Nullable keychain,     SecKeychainStatus * _Nonnull keychainStatus ); ``` |

Modified [SecKeychainGetUserInteractionAllowed()](https://developer.apple.com/documentation/security/1393621-seckeychaingetuserinteractionall)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetUserInteractionAllowed (     Boolean *state ); ``` |
| To | ``` OSStatus SecKeychainGetUserInteractionAllowed (     Boolean * _Nonnull state ); ``` |

Modified [SecKeychainGetVersion()](https://developer.apple.com/documentation/security/1393890-seckeychaingetversion)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainGetVersion (     UInt32 *returnVers ); ``` |
| To | ``` OSStatus SecKeychainGetVersion (     UInt32 * _Nonnull returnVers ); ``` |

Modified [SecKeychainLock()](https://developer.apple.com/documentation/security/1402180-seckeychainlock)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainLock (     SecKeychainRef keychain ); ``` |
| To | ``` OSStatus SecKeychainLock (     SecKeychainRef _Nullable keychain ); ``` |

Modified [SecKeychainOpen()](https://developer.apple.com/documentation/security/1396431-seckeychainopen)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainOpen (     const char *pathName,     SecKeychainRef *keychain ); ``` |
| To | ``` OSStatus SecKeychainOpen (     const char * _Nonnull pathName,     SecKeychainRef  _Nullable * _Nonnull keychain ); ``` |

Modified [SecKeychainRemoveCallback()](https://developer.apple.com/documentation/security/1398240-seckeychainremovecallback)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainRemoveCallback (     SecKeychainCallback callbackFunction ); ``` |
| To | ``` OSStatus SecKeychainRemoveCallback (     SecKeychainCallback _Nonnull callbackFunction ); ``` |

Modified [SecKeychainSetAccess()](https://developer.apple.com/documentation/security/1392434-seckeychainsetaccess)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetAccess (     SecKeychainRef keychain,     SecAccessRef access ); ``` |
| To | ``` OSStatus SecKeychainSetAccess (     SecKeychainRef _Nullable keychain,     SecAccessRef _Nonnull access ); ``` |

Modified [SecKeychainSetDefault()](https://developer.apple.com/documentation/security/1393097-seckeychainsetdefault)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetDefault (     SecKeychainRef keychain ); ``` |
| To | ``` OSStatus SecKeychainSetDefault (     SecKeychainRef _Nullable keychain ); ``` |

Modified [SecKeychainSetDomainDefault()](https://developer.apple.com/documentation/security/1398802-seckeychainsetdomaindefault)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetDomainDefault (     SecPreferencesDomain domain,     SecKeychainRef keychain ); ``` |
| To | ``` OSStatus SecKeychainSetDomainDefault (     SecPreferencesDomain domain,     SecKeychainRef _Nullable keychain ); ``` |

Modified [SecKeychainSetDomainSearchList()](https://developer.apple.com/documentation/security/1398572-seckeychainsetdomainsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetDomainSearchList (     SecPreferencesDomain domain,     CFArrayRef searchList ); ``` |
| To | ``` OSStatus SecKeychainSetDomainSearchList (     SecPreferencesDomain domain,     CFArrayRef _Nonnull searchList ); ``` |

Modified [SecKeychainSetSearchList()](https://developer.apple.com/documentation/security/1397619-seckeychainsetsearchlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetSearchList (     CFArrayRef searchList ); ``` |
| To | ``` OSStatus SecKeychainSetSearchList (     CFArrayRef _Nonnull searchList ); ``` |

Modified [SecKeychainSetSettings()](https://developer.apple.com/documentation/security/1393109-seckeychainsetsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSetSettings (     SecKeychainRef keychain,     const SecKeychainSettings *newSettings ); ``` |
| To | ``` OSStatus SecKeychainSetSettings (     SecKeychainRef _Nullable keychain,     const SecKeychainSettings * _Nonnull newSettings ); ``` |

Modified [SecKeychainUnlock()](https://developer.apple.com/documentation/security/1400341-seckeychainunlock)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainUnlock (     SecKeychainRef keychain,     UInt32 passwordLength,     const void *password,     Boolean usePassword ); ``` |
| To | ``` OSStatus SecKeychainUnlock (     SecKeychainRef _Nullable keychain,     UInt32 passwordLength,     const void * _Nullable password,     Boolean usePassword ); ``` |

#### SecKeychainItem.h

Modified [SecKeychainItemCopyAccess()](https://developer.apple.com/documentation/security/1397585-seckeychainitemcopyaccess)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCopyAccess (     SecKeychainItemRef itemRef,     SecAccessRef *access ); ``` |
| To | ``` OSStatus SecKeychainItemCopyAccess (     SecKeychainItemRef _Nonnull itemRef,     SecAccessRef  _Nullable * _Nonnull access ); ``` |

Modified [SecKeychainItemCopyAttributesAndData()](https://developer.apple.com/documentation/security/1400528-seckeychainitemcopyattributesand)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCopyAttributesAndData (     SecKeychainItemRef itemRef,     SecKeychainAttributeInfo *info,     SecItemClass *itemClass,     SecKeychainAttributeList **attrList,     UInt32 *length,     void **outData ); ``` |
| To | ``` OSStatus SecKeychainItemCopyAttributesAndData (     SecKeychainItemRef _Nonnull itemRef,     SecKeychainAttributeInfo * _Nullable info,     SecItemClass * _Nullable itemClass,     SecKeychainAttributeList * _Nullable * _Nullable attrList,     UInt32 * _Nullable length,     void * _Nullable * _Nullable outData ); ``` |

Modified [SecKeychainItemCopyContent()](https://developer.apple.com/documentation/security/1401412-seckeychainitemcopycontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCopyContent (     SecKeychainItemRef itemRef,     SecItemClass *itemClass,     SecKeychainAttributeList *attrList,     UInt32 *length,     void **outData ); ``` |
| To | ``` OSStatus SecKeychainItemCopyContent (     SecKeychainItemRef _Nonnull itemRef,     SecItemClass * _Nullable itemClass,     SecKeychainAttributeList * _Nullable attrList,     UInt32 * _Nullable length,     void * _Nullable * _Nullable outData ); ``` |

Modified [SecKeychainItemCopyFromPersistentReference()](https://developer.apple.com/documentation/security/1393535-seckeychainitemcopyfrompersisten)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCopyFromPersistentReference (     CFDataRef persistentItemRef,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainItemCopyFromPersistentReference (     CFDataRef _Nonnull persistentItemRef,     SecKeychainItemRef  _Nullable * _Nonnull itemRef ); ``` |

Modified [SecKeychainItemCopyKeychain()](https://developer.apple.com/documentation/security/1398355-seckeychainitemcopykeychain)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCopyKeychain (     SecKeychainItemRef itemRef,     SecKeychainRef *keychainRef ); ``` |
| To | ``` OSStatus SecKeychainItemCopyKeychain (     SecKeychainItemRef _Nonnull itemRef,     SecKeychainRef  _Nullable * _Nonnull keychainRef ); ``` |

Modified [SecKeychainItemCreateCopy()](https://developer.apple.com/documentation/security/1396024-seckeychainitemcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCreateCopy (     SecKeychainItemRef itemRef,     SecKeychainRef destKeychainRef,     SecAccessRef initialAccess,     SecKeychainItemRef *itemCopy ); ``` |
| To | ``` OSStatus SecKeychainItemCreateCopy (     SecKeychainItemRef _Nonnull itemRef,     SecKeychainRef _Nullable destKeychainRef,     SecAccessRef _Nonnull initialAccess,     SecKeychainItemRef  _Nullable * _Nonnull itemCopy ); ``` |

Modified [SecKeychainItemCreateFromContent()](https://developer.apple.com/documentation/security/1393225-seckeychainitemcreatefromcontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCreateFromContent (     SecItemClass itemClass,     SecKeychainAttributeList *attrList,     UInt32 length,     const void *data,     SecKeychainRef keychainRef,     SecAccessRef initialAccess,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainItemCreateFromContent (     SecItemClass itemClass,     SecKeychainAttributeList * _Nonnull attrList,     UInt32 length,     const void * _Nullable data,     SecKeychainRef _Nullable keychainRef,     SecAccessRef _Nullable initialAccess,     SecKeychainItemRef  _Nullable * _Nullable itemRef ); ``` |

Modified [SecKeychainItemCreatePersistentReference()](https://developer.apple.com/documentation/security/1400643-seckeychainitemcreatepersistentr)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemCreatePersistentReference (     SecKeychainItemRef itemRef,     CFDataRef *persistentItemRef ); ``` |
| To | ``` OSStatus SecKeychainItemCreatePersistentReference (     SecKeychainItemRef _Nonnull itemRef,     CFDataRef  _Nullable * _Nonnull persistentItemRef ); ``` |

Modified [SecKeychainItemDelete()](https://developer.apple.com/documentation/security/1400090-seckeychainitemdelete)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemDelete (     SecKeychainItemRef itemRef ); ``` |
| To | ``` OSStatus SecKeychainItemDelete (     SecKeychainItemRef _Nonnull itemRef ); ``` |

Modified [SecKeychainItemFreeAttributesAndData()](https://developer.apple.com/documentation/security/1397736-seckeychainitemfreeattributesand)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemFreeAttributesAndData (     SecKeychainAttributeList *attrList,     void *data ); ``` |
| To | ``` OSStatus SecKeychainItemFreeAttributesAndData (     SecKeychainAttributeList * _Nullable attrList,     void * _Nullable data ); ``` |

Modified [SecKeychainItemFreeContent()](https://developer.apple.com/documentation/security/1402019-seckeychainitemfreecontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemFreeContent (     SecKeychainAttributeList *attrList,     void *data ); ``` |
| To | ``` OSStatus SecKeychainItemFreeContent (     SecKeychainAttributeList * _Nullable attrList,     void * _Nullable data ); ``` |

Modified [SecKeychainItemGetDLDBHandle()](https://developer.apple.com/documentation/security/1415616-seckeychainitemgetdldbhandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemGetDLDBHandle (     SecKeychainItemRef keyItemRef,     CSSM_DL_DB_HANDLE *dldbHandle ); ``` |
| To | ``` OSStatus SecKeychainItemGetDLDBHandle (     SecKeychainItemRef _Nonnull keyItemRef,     CSSM_DL_DB_HANDLE * _Nonnull dldbHandle ); ``` |

Modified [SecKeychainItemGetUniqueRecordID()](https://developer.apple.com/documentation/security/1415615-seckeychainitemgetuniquerecordid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemGetUniqueRecordID (     SecKeychainItemRef itemRef,     const CSSM_DB_UNIQUE_RECORD **uniqueRecordID ); ``` |
| To | ``` OSStatus SecKeychainItemGetUniqueRecordID (     SecKeychainItemRef _Nonnull itemRef,     const CSSM_DB_UNIQUE_RECORD * _Nullable * _Nonnull uniqueRecordID ); ``` |

Modified [SecKeychainItemModifyAttributesAndData()](https://developer.apple.com/documentation/security/1399963-seckeychainitemmodifyattributesa)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemModifyAttributesAndData (     SecKeychainItemRef itemRef,     const SecKeychainAttributeList *attrList,     UInt32 length,     const void *data ); ``` |
| To | ``` OSStatus SecKeychainItemModifyAttributesAndData (     SecKeychainItemRef _Nonnull itemRef,     const SecKeychainAttributeList * _Nullable attrList,     UInt32 length,     const void * _Nullable data ); ``` |

Modified [SecKeychainItemModifyContent()](https://developer.apple.com/documentation/security/1397154-seckeychainitemmodifycontent)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemModifyContent (     SecKeychainItemRef itemRef,     const SecKeychainAttributeList *attrList,     UInt32 length,     const void *data ); ``` |
| To | ``` OSStatus SecKeychainItemModifyContent (     SecKeychainItemRef _Nonnull itemRef,     const SecKeychainAttributeList * _Nullable attrList,     UInt32 length,     const void * _Nullable data ); ``` |

Modified [SecKeychainItemSetAccess()](https://developer.apple.com/documentation/security/1395210-seckeychainitemsetaccess)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainItemSetAccess (     SecKeychainItemRef itemRef,     SecAccessRef access ); ``` |
| To | ``` OSStatus SecKeychainItemSetAccess (     SecKeychainItemRef _Nonnull itemRef,     SecAccessRef _Nonnull access ); ``` |

#### SecKeychainSearch.h

Modified [SecKeychainSearchCopyNext()](https://developer.apple.com/documentation/security/1515362-seckeychainsearchcopynext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSearchCopyNext (     SecKeychainSearchRef searchRef,     SecKeychainItemRef *itemRef ); ``` |
| To | ``` OSStatus SecKeychainSearchCopyNext (     SecKeychainSearchRef _Nonnull searchRef,     SecKeychainItemRef  _Nullable * _Nonnull itemRef ); ``` |

Modified [SecKeychainSearchCreateFromAttributes()](https://developer.apple.com/documentation/security/1515366-seckeychainsearchcreatefromattri)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecKeychainSearchCreateFromAttributes (     CFTypeRef keychainOrArray,     SecItemClass itemClass,     const SecKeychainAttributeList *attrList,     SecKeychainSearchRef *searchRef ); ``` |
| To | ``` OSStatus SecKeychainSearchCreateFromAttributes (     CFTypeRef _Nullable keychainOrArray,     SecItemClass itemClass,     const SecKeychainAttributeList * _Nullable attrList,     SecKeychainSearchRef  _Nullable * _Nonnull searchRef ); ``` |

#### SecPolicy.h

Added [kSecPolicyApplePayIssuerEncryption](https://developer.apple.com/documentation/security/ksecpolicyapplepayissuerencryption)Modified [SecPolicyCopyProperties()](https://developer.apple.com/documentation/security/1401915-secpolicycopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SecPolicyCopyProperties (     SecPolicyRef policyRef ); ``` |
| To | ``` CFDictionaryRef _Nonnull SecPolicyCopyProperties (     SecPolicyRef _Nonnull policyRef ); ``` |

Modified [SecPolicyCreateBasicX509()](https://developer.apple.com/documentation/security/1397202-secpolicycreatebasicx509)

|  | Declaration |
| --- | --- |
| From | ``` SecPolicyRef SecPolicyCreateBasicX509 (     void ); ``` |
| To | ``` SecPolicyRef _Nonnull SecPolicyCreateBasicX509 (     void ); ``` |

Modified [SecPolicyCreateRevocation()](https://developer.apple.com/documentation/security/1400026-secpolicycreaterevocation)

|  | Declaration |
| --- | --- |
| From | ``` SecPolicyRef SecPolicyCreateRevocation (     CFOptionFlags revocationFlags ); ``` |
| To | ``` SecPolicyRef _Nonnull SecPolicyCreateRevocation (     CFOptionFlags revocationFlags ); ``` |

Modified [SecPolicyCreateSSL()](https://developer.apple.com/documentation/security/1392592-secpolicycreatessl)

|  | Declaration |
| --- | --- |
| From | ``` SecPolicyRef SecPolicyCreateSSL (     Boolean server,     CFStringRef hostname ); ``` |
| To | ``` SecPolicyRef _Nonnull SecPolicyCreateSSL (     Boolean server,     CFStringRef _Nullable hostname ); ``` |

Modified [SecPolicyCreateWithOID()](https://developer.apple.com/documentation/security/1563598-secpolicycreatewithoid)

|  | Declaration |
| --- | --- |
| From | ``` SecPolicyRef SecPolicyCreateWithOID (     CFTypeRef policyOID ); ``` |
| To | ``` SecPolicyRef _Nullable SecPolicyCreateWithOID (     CFTypeRef _Nonnull policyOID ); ``` |

Modified [SecPolicyCreateWithProperties()](https://developer.apple.com/documentation/security/1394568-secpolicycreatewithproperties)

|  | Declaration |
| --- | --- |
| From | ``` SecPolicyRef SecPolicyCreateWithProperties (     CFTypeRef policyIdentifier,     CFDictionaryRef properties ); ``` |
| To | ``` SecPolicyRef _Nullable SecPolicyCreateWithProperties (     CFTypeRef _Nonnull policyIdentifier,     CFDictionaryRef _Nullable properties ); ``` |

Modified [SecPolicyGetOID()](https://developer.apple.com/documentation/security/1563594-secpolicygetoid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicyGetOID (     SecPolicyRef policyRef,     CSSM_OID *oid ); ``` |
| To | ``` OSStatus SecPolicyGetOID (     SecPolicyRef _Nonnull policyRef,     CSSM_OID * _Nonnull oid ); ``` |

Modified [SecPolicyGetTPHandle()](https://developer.apple.com/documentation/security/1563593-secpolicygettphandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicyGetTPHandle (     SecPolicyRef policyRef,     CSSM_TP_HANDLE *tpHandle ); ``` |
| To | ``` OSStatus SecPolicyGetTPHandle (     SecPolicyRef _Nonnull policyRef,     CSSM_TP_HANDLE * _Nonnull tpHandle ); ``` |

Modified [SecPolicyGetValue()](https://developer.apple.com/documentation/security/1563595-secpolicygetvalue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicyGetValue (     SecPolicyRef policyRef,     CSSM_DATA *value ); ``` |
| To | ``` OSStatus SecPolicyGetValue (     SecPolicyRef _Nonnull policyRef,     CSSM_DATA * _Nonnull value ); ``` |

Modified [SecPolicySetProperties()](https://developer.apple.com/documentation/security/1563596-secpolicysetproperties)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicySetProperties (     SecPolicyRef policyRef,     CFDictionaryRef properties ); ``` |
| To | ``` OSStatus SecPolicySetProperties (     SecPolicyRef _Nonnull policyRef,     CFDictionaryRef _Nonnull properties ); ``` |

Modified [SecPolicySetValue()](https://developer.apple.com/documentation/security/1563597-secpolicysetvalue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicySetValue (     SecPolicyRef policyRef,     const CSSM_DATA *value ); ``` |
| To | ``` OSStatus SecPolicySetValue (     SecPolicyRef _Nonnull policyRef,     const CSSM_DATA * _Nonnull value ); ``` |

#### SecPolicySearch.h

Modified [SecPolicySearchCopyNext()](https://developer.apple.com/documentation/security/1562856-secpolicysearchcopynext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicySearchCopyNext (     SecPolicySearchRef searchRef,     SecPolicyRef *policyRef ); ``` |
| To | ``` OSStatus SecPolicySearchCopyNext (     SecPolicySearchRef _Nonnull searchRef,     SecPolicyRef  _Nullable * _Nonnull policyRef ); ``` |

Modified [SecPolicySearchCreate()](https://developer.apple.com/documentation/security/1562858-secpolicysearchcreate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecPolicySearchCreate (     CSSM_CERT_TYPE certType,     const CSSM_OID *policyOID,     const CSSM_DATA *value,     SecPolicySearchRef *searchRef ); ``` |
| To | ``` OSStatus SecPolicySearchCreate (     CSSM_CERT_TYPE certType,     const CSSM_OID * _Nonnull policyOID,     const CSSM_DATA * _Nullable value,     SecPolicySearchRef  _Nullable * _Nonnull searchRef ); ``` |

#### SecRandom.h

Modified [SecRandomCopyBytes()](https://developer.apple.com/documentation/security/1399291-secrandomcopybytes)

|  | Declaration |
| --- | --- |
| From | ``` int SecRandomCopyBytes (     SecRandomRef rnd,     size_t count,     uint8_t *bytes ); ``` |
| To | ``` int SecRandomCopyBytes (     SecRandomRef _Nullable rnd,     size_t count,     uint8_t * _Nonnull bytes ); ``` |

#### SecRequirement.h

Modified [SecRequirementCopyData()](https://developer.apple.com/documentation/security/1401647-secrequirementcopydata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecRequirementCopyData (     SecRequirementRef requirement,     SecCSFlags flags,     CFDataRef *data ); ``` |
| To | ``` OSStatus SecRequirementCopyData (     SecRequirementRef _Nonnull requirement,     SecCSFlags flags,     CFDataRef  _Nullable * _Nonnull data ); ``` |

Modified [SecRequirementCopyString()](https://developer.apple.com/documentation/security/1394253-secrequirementcopystring)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecRequirementCopyString (     SecRequirementRef requirement,     SecCSFlags flags,     CFStringRef *text ); ``` |
| To | ``` OSStatus SecRequirementCopyString (     SecRequirementRef _Nonnull requirement,     SecCSFlags flags,     CFStringRef  _Nullable * _Nonnull text ); ``` |

Modified [SecRequirementCreateWithData()](https://developer.apple.com/documentation/security/1396013-secrequirementcreatewithdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecRequirementCreateWithData (     CFDataRef data,     SecCSFlags flags,     SecRequirementRef *requirement ); ``` |
| To | ``` OSStatus SecRequirementCreateWithData (     CFDataRef _Nonnull data,     SecCSFlags flags,     SecRequirementRef  _Nullable * _Nonnull requirement ); ``` |

Modified [SecRequirementCreateWithString()](https://developer.apple.com/documentation/security/1394522-secrequirementcreatewithstring)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecRequirementCreateWithString (     CFStringRef text,     SecCSFlags flags,     SecRequirementRef *requirement ); ``` |
| To | ``` OSStatus SecRequirementCreateWithString (     CFStringRef _Nonnull text,     SecCSFlags flags,     SecRequirementRef  _Nullable * _Nonnull requirement ); ``` |

Modified [SecRequirementCreateWithStringAndErrors()](https://developer.apple.com/documentation/security/1401166-secrequirementcreatewithstringan)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecRequirementCreateWithStringAndErrors (     CFStringRef text,     SecCSFlags flags,     CFErrorRef *errors,     SecRequirementRef *requirement ); ``` |
| To | ``` OSStatus SecRequirementCreateWithStringAndErrors (     CFStringRef _Nonnull text,     SecCSFlags flags,     CFErrorRef  _Nullable * _Nullable errors,     SecRequirementRef  _Nullable * _Nonnull requirement ); ``` |

#### SecSignVerifyTransform.h

Modified [SecSignTransformCreate()](https://developer.apple.com/documentation/security/1398780-secsigntransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecSignTransformCreate (     SecKeyRef key,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecSignTransformCreate (     SecKeyRef _Nonnull key,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecVerifyTransformCreate()](https://developer.apple.com/documentation/security/1393414-secverifytransformcreate)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecVerifyTransformCreate (     SecKeyRef key,     CFDataRef signature,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecVerifyTransformCreate (     SecKeyRef _Nonnull key,     CFDataRef _Nullable signature,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecStaticCode.h

Added [kSecCSRestrictSymlinks](https://developer.apple.com/documentation/security/1543778-static_code_validation_flags/kseccsrestrictsymlinks)Modified [SecStaticCodeCheckValidity()](https://developer.apple.com/documentation/security/1395784-secstaticcodecheckvalidity)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecStaticCodeCheckValidity (     SecStaticCodeRef staticCode,     SecCSFlags flags,     SecRequirementRef requirement ); ``` |
| To | ``` OSStatus SecStaticCodeCheckValidity (     SecStaticCodeRef _Nonnull staticCode,     SecCSFlags flags,     SecRequirementRef _Nullable requirement ); ``` |

Modified [SecStaticCodeCheckValidityWithErrors()](https://developer.apple.com/documentation/security/1395252-secstaticcodecheckvaliditywither)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecStaticCodeCheckValidityWithErrors (     SecStaticCodeRef staticCode,     SecCSFlags flags,     SecRequirementRef requirement,     CFErrorRef *errors ); ``` |
| To | ``` OSStatus SecStaticCodeCheckValidityWithErrors (     SecStaticCodeRef _Nonnull staticCode,     SecCSFlags flags,     SecRequirementRef _Nullable requirement,     CFErrorRef  _Nullable * _Nullable errors ); ``` |

Modified [SecStaticCodeCreateWithPath()](https://developer.apple.com/documentation/security/1396899-secstaticcodecreatewithpath)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecStaticCodeCreateWithPath (     CFURLRef path,     SecCSFlags flags,     SecStaticCodeRef *staticCode ); ``` |
| To | ``` OSStatus SecStaticCodeCreateWithPath (     CFURLRef _Nonnull path,     SecCSFlags flags,     SecStaticCodeRef  _Nullable * _Nonnull staticCode ); ``` |

Modified [SecStaticCodeCreateWithPathAndAttributes()](https://developer.apple.com/documentation/security/1394237-secstaticcodecreatewithpathandat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecStaticCodeCreateWithPathAndAttributes (     CFURLRef path,     SecCSFlags flags,     CFDictionaryRef attributes,     SecStaticCodeRef *staticCode ); ``` |
| To | ``` OSStatus SecStaticCodeCreateWithPathAndAttributes (     CFURLRef _Nonnull path,     SecCSFlags flags,     CFDictionaryRef _Nonnull attributes,     SecStaticCodeRef  _Nullable * _Nonnull staticCode ); ``` |

#### SecTask.h

Modified [SecTaskCopyValueForEntitlement()](https://developer.apple.com/documentation/security/1393461-sectaskcopyvalueforentitlement)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTaskCopyValueForEntitlement (     SecTaskRef task,     CFStringRef entitlement,     CFErrorRef *error ); ``` |
| To | ``` CFTypeRef _Nullable SecTaskCopyValueForEntitlement (     SecTaskRef _Nonnull task,     CFStringRef _Nonnull entitlement,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTaskCopyValuesForEntitlements()](https://developer.apple.com/documentation/security/1397627-sectaskcopyvaluesforentitlements)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SecTaskCopyValuesForEntitlements (     SecTaskRef task,     CFArrayRef entitlements,     CFErrorRef *error ); ``` |
| To | ``` CFDictionaryRef _Nullable SecTaskCopyValuesForEntitlements (     SecTaskRef _Nonnull task,     CFArrayRef _Nonnull entitlements,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTaskCreateFromSelf()](https://developer.apple.com/documentation/security/1400321-sectaskcreatefromself)

|  | Declaration |
| --- | --- |
| From | ``` SecTaskRef SecTaskCreateFromSelf (     CFAllocatorRef allocator ); ``` |
| To | ``` SecTaskRef _Nullable SecTaskCreateFromSelf (     CFAllocatorRef _Nullable allocator ); ``` |

Modified [SecTaskCreateWithAuditToken()](https://developer.apple.com/documentation/security/1401168-sectaskcreatewithaudittoken)

|  | Declaration |
| --- | --- |
| From | ``` SecTaskRef SecTaskCreateWithAuditToken (     CFAllocatorRef allocator,     audit_token_t token ); ``` |
| To | ``` SecTaskRef _Nullable SecTaskCreateWithAuditToken (     CFAllocatorRef _Nullable allocator,     audit_token_t token ); ``` |

#### SecTransform.h

Modified [SecTransformConnectTransforms()](https://developer.apple.com/documentation/security/1401298-sectransformconnecttransforms)

|  | Declaration |
| --- | --- |
| From | ``` SecGroupTransformRef SecTransformConnectTransforms (     SecTransformRef sourceTransformRef,     CFStringRef sourceAttributeName,     SecTransformRef destinationTransformRef,     CFStringRef destinationAttributeName,     SecGroupTransformRef group,     CFErrorRef *error ); ``` |
| To | ``` SecGroupTransformRef _Nullable SecTransformConnectTransforms (     SecTransformRef _Nonnull sourceTransformRef,     CFStringRef _Nonnull sourceAttributeName,     SecTransformRef _Nonnull destinationTransformRef,     CFStringRef _Nonnull destinationAttributeName,     SecGroupTransformRef _Nonnull group,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTransformCopyExternalRepresentation()](https://developer.apple.com/documentation/security/1397283-sectransformcopyexternalrepresen)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SecTransformCopyExternalRepresentation (     SecTransformRef transformRef ); ``` |
| To | ``` CFDictionaryRef _Nonnull SecTransformCopyExternalRepresentation (     SecTransformRef _Nonnull transformRef ); ``` |

Modified [SecTransformCreateFromExternalRepresentation()](https://developer.apple.com/documentation/security/1397563-sectransformcreatefromexternalre)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecTransformCreateFromExternalRepresentation (     CFDictionaryRef dictionary,     CFErrorRef *error ); ``` |
| To | ``` SecTransformRef _Nullable SecTransformCreateFromExternalRepresentation (     CFDictionaryRef _Nonnull dictionary,     CFErrorRef  _Nullable * _Nullable error ); ``` |

Modified [SecTransformCreateGroupTransform()](https://developer.apple.com/documentation/security/1400301-sectransformcreategrouptransform)

|  | Declaration |
| --- | --- |
| From | ``` SecGroupTransformRef SecTransformCreateGroupTransform (     void ); ``` |
| To | ``` SecGroupTransformRef _Nonnull SecTransformCreateGroupTransform (     void ); ``` |

Modified [SecTransformExecute()](https://developer.apple.com/documentation/security/1395776-sectransformexecute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformExecute (     SecTransformRef transformRef,     CFErrorRef *errorRef ); ``` |
| To | ``` CFTypeRef _Nonnull SecTransformExecute (     SecTransformRef _Nonnull transformRef,     CFErrorRef  _Nullable * _Nullable errorRef ); ``` |

Modified [SecTransformExecuteAsync()](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync)

|  | Declaration |
| --- | --- |
| From | ``` void SecTransformExecuteAsync (     SecTransformRef transformRef,     dispatch_queue_t deliveryQueue,     SecMessageBlock deliveryBlock ); ``` |
| To | ``` void SecTransformExecuteAsync (     SecTransformRef _Nonnull transformRef,     dispatch_queue_t _Nonnull deliveryQueue,     SecMessageBlock _Nonnull deliveryBlock ); ``` |

Modified [SecTransformFindByName()](https://developer.apple.com/documentation/security/1401448-sectransformfindbyname)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecTransformFindByName (     SecGroupTransformRef transform,     CFStringRef name ); ``` |
| To | ``` SecTransformRef _Nullable SecTransformFindByName (     SecGroupTransformRef _Nonnull transform,     CFStringRef _Nonnull name ); ``` |

Modified [SecTransformGetAttribute()](https://developer.apple.com/documentation/security/1398748-sectransformgetattribute)

|  | Declaration |
| --- | --- |
| From | ``` CFTypeRef SecTransformGetAttribute (     SecTransformRef transformRef,     CFStringRef key ); ``` |
| To | ``` CFTypeRef _Nullable SecTransformGetAttribute (     SecTransformRef _Nonnull transformRef,     CFStringRef _Nonnull key ); ``` |

Modified [SecTransformSetAttribute()](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute)

|  | Declaration |
| --- | --- |
| From | ``` Boolean SecTransformSetAttribute (     SecTransformRef transformRef,     CFStringRef key,     CFTypeRef value,     CFErrorRef *error ); ``` |
| To | ``` Boolean SecTransformSetAttribute (     SecTransformRef _Nonnull transformRef,     CFStringRef _Nonnull key,     CFTypeRef _Nonnull value,     CFErrorRef  _Nullable * _Nullable error ); ``` |

#### SecTransformReadTransform.h

Modified [SecTransformCreateReadTransformWithReadStream()](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw)

|  | Declaration |
| --- | --- |
| From | ``` SecTransformRef SecTransformCreateReadTransformWithReadStream (     CFReadStreamRef inputStream ); ``` |
| To | ``` SecTransformRef _Nonnull SecTransformCreateReadTransformWithReadStream (     CFReadStreamRef _Nonnull inputStream ); ``` |

#### SecTrust.h

Modified [SecTrustCopyAnchorCertificates()](https://developer.apple.com/documentation/security/1401507-sectrustcopyanchorcertificates)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustCopyAnchorCertificates (     CFArrayRef *anchors ); ``` |
| To | ``` OSStatus SecTrustCopyAnchorCertificates (     CFArrayRef  _Nullable * _Nonnull anchors ); ``` |

Modified [SecTrustCopyCustomAnchorCertificates()](https://developer.apple.com/documentation/security/1401743-sectrustcopycustomanchorcertific)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustCopyCustomAnchorCertificates (     SecTrustRef trust,     CFArrayRef *anchors ); ``` |
| To | ``` OSStatus SecTrustCopyCustomAnchorCertificates (     SecTrustRef _Nonnull trust,     CFArrayRef  _Nullable * _Nonnull anchors ); ``` |

Modified [SecTrustCopyExceptions()](https://developer.apple.com/documentation/security/1400106-sectrustcopyexceptions)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef SecTrustCopyExceptions (     SecTrustRef trust ); ``` |
| To | ``` CFDataRef _Nonnull SecTrustCopyExceptions (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustCopyPolicies()](https://developer.apple.com/documentation/security/1392716-sectrustcopypolicies)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustCopyPolicies (     SecTrustRef trust,     CFArrayRef *policies ); ``` |
| To | ``` OSStatus SecTrustCopyPolicies (     SecTrustRef _Nonnull trust,     CFArrayRef  _Nullable * _Nonnull policies ); ``` |

Modified [SecTrustCopyProperties()](https://developer.apple.com/documentation/security/1401567-sectrustcopyproperties)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef SecTrustCopyProperties (     SecTrustRef trust ); ``` |
| To | ``` CFArrayRef _Nullable SecTrustCopyProperties (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustCopyPublicKey()](https://developer.apple.com/documentation/security/1396135-sectrustcopypublickey)

|  | Declaration |
| --- | --- |
| From | ``` SecKeyRef SecTrustCopyPublicKey (     SecTrustRef trust ); ``` |
| To | ``` SecKeyRef _Nullable SecTrustCopyPublicKey (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustCopyResult()](https://developer.apple.com/documentation/security/1398612-sectrustcopyresult)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef SecTrustCopyResult (     SecTrustRef trust ); ``` |
| To | ``` CFDictionaryRef _Nullable SecTrustCopyResult (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustCreateWithCertificates()](https://developer.apple.com/documentation/security/1401555-sectrustcreatewithcertificates)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustCreateWithCertificates (     CFTypeRef certificates,     CFTypeRef policies,     SecTrustRef *trust ); ``` |
| To | ``` OSStatus SecTrustCreateWithCertificates (     CFTypeRef _Nonnull certificates,     CFTypeRef _Nullable policies,     SecTrustRef  _Nullable * _Nonnull trust ); ``` |

Modified [SecTrustEvaluate()](https://developer.apple.com/documentation/security/1394363-sectrustevaluate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustEvaluate (     SecTrustRef trust,     SecTrustResultType *result ); ``` |
| To | ``` OSStatus SecTrustEvaluate (     SecTrustRef _Nonnull trust,     SecTrustResultType * _Nullable result ); ``` |

Modified [SecTrustEvaluateAsync()](https://developer.apple.com/documentation/security/1400632-sectrustevaluateasync)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustEvaluateAsync (     SecTrustRef trust,     dispatch_queue_t queue,     SecTrustCallback result ); ``` |
| To | ``` OSStatus SecTrustEvaluateAsync (     SecTrustRef _Nonnull trust,     dispatch_queue_t _Nullable queue,     SecTrustCallback _Nonnull result ); ``` |

Modified [SecTrustGetCertificateAtIndex()](https://developer.apple.com/documentation/security/1395987-sectrustgetcertificateatindex)

|  | Declaration |
| --- | --- |
| From | ``` SecCertificateRef SecTrustGetCertificateAtIndex (     SecTrustRef trust,     CFIndex ix ); ``` |
| To | ``` SecCertificateRef _Nullable SecTrustGetCertificateAtIndex (     SecTrustRef _Nonnull trust,     CFIndex ix ); ``` |

Modified [SecTrustGetCertificateCount()](https://developer.apple.com/documentation/security/1397024-sectrustgetcertificatecount)

|  | Declaration |
| --- | --- |
| From | ``` CFIndex SecTrustGetCertificateCount (     SecTrustRef trust ); ``` |
| To | ``` CFIndex SecTrustGetCertificateCount (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustGetCssmResult()](https://developer.apple.com/documentation/security/1524311-sectrustgetcssmresult)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetCssmResult (     SecTrustRef trust,     CSSM_TP_VERIFY_CONTEXT_RESULT_PTR *result ); ``` |
| To | ``` OSStatus SecTrustGetCssmResult (     SecTrustRef _Nonnull trust,     CSSM_TP_VERIFY_CONTEXT_RESULT_PTR  _Nullable * _Nonnull result ); ``` |

Modified [SecTrustGetCssmResultCode()](https://developer.apple.com/documentation/security/1524327-sectrustgetcssmresultcode)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetCssmResultCode (     SecTrustRef trust,     OSStatus *resultCode ); ``` |
| To | ``` OSStatus SecTrustGetCssmResultCode (     SecTrustRef _Nonnull trust,     OSStatus * _Nonnull resultCode ); ``` |

Modified [SecTrustGetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1400259-sectrustgetnetworkfetchallowed)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetNetworkFetchAllowed (     SecTrustRef trust,     Boolean *allowFetch ); ``` |
| To | ``` OSStatus SecTrustGetNetworkFetchAllowed (     SecTrustRef _Nonnull trust,     Boolean * _Nonnull allowFetch ); ``` |

Modified [SecTrustGetResult()](https://developer.apple.com/documentation/security/1524331-sectrustgetresult)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetResult (     SecTrustRef trustRef,     SecTrustResultType *result,     CFArrayRef *certChain,     CSSM_TP_APPLE_EVIDENCE_INFO **statusChain ); ``` |
| To | ``` OSStatus SecTrustGetResult (     SecTrustRef _Nonnull trustRef,     SecTrustResultType * _Nullable result,     CFArrayRef  _Nullable * _Nonnull certChain,     CSSM_TP_APPLE_EVIDENCE_INFO * _Nullable * _Nonnull statusChain ); ``` |

Modified [SecTrustGetTPHandle()](https://developer.apple.com/documentation/security/1524309-sectrustgettphandle)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetTPHandle (     SecTrustRef trust,     CSSM_TP_HANDLE *handle ); ``` |
| To | ``` OSStatus SecTrustGetTPHandle (     SecTrustRef _Nonnull trust,     CSSM_TP_HANDLE * _Nonnull handle ); ``` |

Modified [SecTrustGetTrustResult()](https://developer.apple.com/documentation/security/1396077-sectrustgettrustresult)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustGetTrustResult (     SecTrustRef trust,     SecTrustResultType *result ); ``` |
| To | ``` OSStatus SecTrustGetTrustResult (     SecTrustRef _Nonnull trust,     SecTrustResultType * _Nonnull result ); ``` |

Modified [SecTrustGetVerifyTime()](https://developer.apple.com/documentation/security/1395935-sectrustgetverifytime)

|  | Declaration |
| --- | --- |
| From | ``` CFAbsoluteTime SecTrustGetVerifyTime (     SecTrustRef trust ); ``` |
| To | ``` CFAbsoluteTime SecTrustGetVerifyTime (     SecTrustRef _Nonnull trust ); ``` |

Modified [SecTrustSetAnchorCertificates()](https://developer.apple.com/documentation/security/1396098-sectrustsetanchorcertificates)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetAnchorCertificates (     SecTrustRef trust,     CFArrayRef anchorCertificates ); ``` |
| To | ``` OSStatus SecTrustSetAnchorCertificates (     SecTrustRef _Nonnull trust,     CFArrayRef _Nonnull anchorCertificates ); ``` |

Modified [SecTrustSetAnchorCertificatesOnly()](https://developer.apple.com/documentation/security/1399071-sectrustsetanchorcertificatesonl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetAnchorCertificatesOnly (     SecTrustRef trust,     Boolean anchorCertificatesOnly ); ``` |
| To | ``` OSStatus SecTrustSetAnchorCertificatesOnly (     SecTrustRef _Nonnull trust,     Boolean anchorCertificatesOnly ); ``` |

Modified [SecTrustSetExceptions()](https://developer.apple.com/documentation/security/1395676-sectrustsetexceptions)

|  | Declaration |
| --- | --- |
| From | ``` bool SecTrustSetExceptions (     SecTrustRef trust,     CFDataRef exceptions ); ``` |
| To | ``` bool SecTrustSetExceptions (     SecTrustRef _Nonnull trust,     CFDataRef _Nonnull exceptions ); ``` |

Modified [SecTrustSetKeychains()](https://developer.apple.com/documentation/security/1395644-sectrustsetkeychains)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetKeychains (     SecTrustRef trust,     CFTypeRef keychainOrArray ); ``` |
| To | ``` OSStatus SecTrustSetKeychains (     SecTrustRef _Nonnull trust,     CFTypeRef _Nullable keychainOrArray ); ``` |

Modified [SecTrustSetNetworkFetchAllowed()](https://developer.apple.com/documentation/security/1395083-sectrustsetnetworkfetchallowed)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetNetworkFetchAllowed (     SecTrustRef trust,     Boolean allowFetch ); ``` |
| To | ``` OSStatus SecTrustSetNetworkFetchAllowed (     SecTrustRef _Nonnull trust,     Boolean allowFetch ); ``` |

Modified [SecTrustSetOCSPResponse()](https://developer.apple.com/documentation/security/1400880-sectrustsetocspresponse)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetOCSPResponse (     SecTrustRef trust,     CFTypeRef responseData ); ``` |
| To | ``` OSStatus SecTrustSetOCSPResponse (     SecTrustRef _Nonnull trust,     CFTypeRef _Nullable responseData ); ``` |

Modified [SecTrustSetOptions()](https://developer.apple.com/documentation/security/1392875-sectrustsetoptions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetOptions (     SecTrustRef trustRef,     SecTrustOptionFlags options ); ``` |
| To | ``` OSStatus SecTrustSetOptions (     SecTrustRef _Nonnull trustRef,     SecTrustOptionFlags options ); ``` |

Modified [SecTrustSetParameters()](https://developer.apple.com/documentation/security/1524326-sectrustsetparameters)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetParameters (     SecTrustRef trustRef,     CSSM_TP_ACTION action,     CFDataRef actionData ); ``` |
| To | ``` OSStatus SecTrustSetParameters (     SecTrustRef _Nonnull trustRef,     CSSM_TP_ACTION action,     CFDataRef _Nonnull actionData ); ``` |

Modified [SecTrustSetPolicies()](https://developer.apple.com/documentation/security/1398399-sectrustsetpolicies)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetPolicies (     SecTrustRef trust,     CFTypeRef policies ); ``` |
| To | ``` OSStatus SecTrustSetPolicies (     SecTrustRef _Nonnull trust,     CFTypeRef _Nonnull policies ); ``` |

Modified [SecTrustSetVerifyDate()](https://developer.apple.com/documentation/security/1397216-sectrustsetverifydate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSetVerifyDate (     SecTrustRef trust,     CFDateRef verifyDate ); ``` |
| To | ``` OSStatus SecTrustSetVerifyDate (     SecTrustRef _Nonnull trust,     CFDateRef _Nonnull verifyDate ); ``` |

#### SecTrustedApplication.h

Modified [SecTrustedApplicationCopyData()](https://developer.apple.com/documentation/security/1401737-sectrustedapplicationcopydata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustedApplicationCopyData (     SecTrustedApplicationRef appRef,     CFDataRef *data ); ``` |
| To | ``` OSStatus SecTrustedApplicationCopyData (     SecTrustedApplicationRef _Nonnull appRef,     CFDataRef  _Nullable * _Nonnull data ); ``` |

Modified [SecTrustedApplicationCreateFromPath()](https://developer.apple.com/documentation/security/1400622-sectrustedapplicationcreatefromp)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustedApplicationCreateFromPath (     const char *path,     SecTrustedApplicationRef *app ); ``` |
| To | ``` OSStatus SecTrustedApplicationCreateFromPath (     const char * _Nullable path,     SecTrustedApplicationRef  _Nullable * _Nonnull app ); ``` |

Modified [SecTrustedApplicationSetData()](https://developer.apple.com/documentation/security/1397440-sectrustedapplicationsetdata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustedApplicationSetData (     SecTrustedApplicationRef appRef,     CFDataRef data ); ``` |
| To | ``` OSStatus SecTrustedApplicationSetData (     SecTrustedApplicationRef _Nonnull appRef,     CFDataRef _Nonnull data ); ``` |

#### SecTrustSettings.h

Modified [SecTrustSettingsCopyCertificates()](https://developer.apple.com/documentation/security/1397413-sectrustsettingscopycertificates)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsCopyCertificates (     SecTrustSettingsDomain domain,     CFArrayRef *certArray ); ``` |
| To | ``` OSStatus SecTrustSettingsCopyCertificates (     SecTrustSettingsDomain domain,     CFArrayRef  _Nullable * _Nullable certArray ); ``` |

Modified [SecTrustSettingsCopyModificationDate()](https://developer.apple.com/documentation/security/1397941-sectrustsettingscopymodification)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsCopyModificationDate (     SecCertificateRef certRef,     SecTrustSettingsDomain domain,     CFDateRef *modificationDate ); ``` |
| To | ``` OSStatus SecTrustSettingsCopyModificationDate (     SecCertificateRef _Nonnull certRef,     SecTrustSettingsDomain domain,     CFDateRef  _Nullable * _Nonnull modificationDate ); ``` |

Modified [SecTrustSettingsCopyTrustSettings()](https://developer.apple.com/documentation/security/1400261-sectrustsettingscopytrustsetting)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsCopyTrustSettings (     SecCertificateRef certRef,     SecTrustSettingsDomain domain,     CFArrayRef *trustSettings ); ``` |
| To | ``` OSStatus SecTrustSettingsCopyTrustSettings (     SecCertificateRef _Nonnull certRef,     SecTrustSettingsDomain domain,     CFArrayRef  _Nullable * _Nonnull trustSettings ); ``` |

Modified [SecTrustSettingsCreateExternalRepresentation()](https://developer.apple.com/documentation/security/1402355-sectrustsettingscreateexternalre)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsCreateExternalRepresentation (     SecTrustSettingsDomain domain,     CFDataRef *trustSettings ); ``` |
| To | ``` OSStatus SecTrustSettingsCreateExternalRepresentation (     SecTrustSettingsDomain domain,     CFDataRef  _Nullable * _Nonnull trustSettings ); ``` |

Modified [SecTrustSettingsImportExternalRepresentation()](https://developer.apple.com/documentation/security/1392836-sectrustsettingsimportexternalre)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsImportExternalRepresentation (     SecTrustSettingsDomain domain,     CFDataRef trustSettings ); ``` |
| To | ``` OSStatus SecTrustSettingsImportExternalRepresentation (     SecTrustSettingsDomain domain,     CFDataRef _Nonnull trustSettings ); ``` |

Modified [SecTrustSettingsRemoveTrustSettings()](https://developer.apple.com/documentation/security/1395904-sectrustsettingsremovetrustsetti)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsRemoveTrustSettings (     SecCertificateRef certRef,     SecTrustSettingsDomain domain ); ``` |
| To | ``` OSStatus SecTrustSettingsRemoveTrustSettings (     SecCertificateRef _Nonnull certRef,     SecTrustSettingsDomain domain ); ``` |

Modified [SecTrustSettingsSetTrustSettings()](https://developer.apple.com/documentation/security/1399119-sectrustsettingssettrustsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SecTrustSettingsSetTrustSettings (     SecCertificateRef certRef,     SecTrustSettingsDomain domain,     CFTypeRef trustSettingsDictOrArray ); ``` |
| To | ``` OSStatus SecTrustSettingsSetTrustSettings (     SecCertificateRef _Nonnull certRef,     SecTrustSettingsDomain domain,     CFTypeRef _Nullable trustSettingsDictOrArray ); ``` |

#### SecureTransport.h

Added [errSSLClientHelloReceived](https://developer.apple.com/documentation/security/errsslclienthelloreceived)Added [errSSLWeakPeerEphemeralDHKey](https://developer.apple.com/documentation/security/1503828-secure_transport_result_codes/errsslweakpeerephemeraldhkey)Added [kSSLSessionOptionAllowServerIdentityChange](https://developer.apple.com/documentation/security/sslsessionoption/allowserveridentitychange)Added [kSSLSessionOptionBreakOnClientHello](https://developer.apple.com/documentation/security/sslsessionoption/ksslsessionoptionbreakonclienthello)Added kSSLSessionStrengthPolicyATSv1Added kSSLSessionStrengthPolicyDefaultAdded SSLSessionStrengthPolicyAdded SSLSetSessionStrengthPolicy()Modified [SSLAddDistinguishedName()](https://developer.apple.com/documentation/security/1400906-ssladddistinguishedname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLAddDistinguishedName (     SSLContextRef context,     const void *derDN,     size_t derDNLen ); ``` |
| To | ``` OSStatus SSLAddDistinguishedName (     SSLContextRef _Nonnull context,     const void * _Nullable derDN,     size_t derDNLen ); ``` |

Modified [SSLClose()](https://developer.apple.com/documentation/security/1397869-sslclose)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLClose (     SSLContextRef context ); ``` |
| To | ``` OSStatus SSLClose (     SSLContextRef _Nonnull context ); ``` |

Modified [SSLCopyCertificateAuthorities()](https://developer.apple.com/documentation/security/1401971-sslcopycertificateauthorities)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLCopyCertificateAuthorities (     SSLContextRef context,     CFArrayRef *certificates ); ``` |
| To | ``` OSStatus SSLCopyCertificateAuthorities (     SSLContextRef _Nonnull context,     CFArrayRef  _Nullable * _Nonnull certificates ); ``` |

Modified [SSLCopyDistinguishedNames()](https://developer.apple.com/documentation/security/1398461-sslcopydistinguishednames)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLCopyDistinguishedNames (     SSLContextRef context,     CFArrayRef *names ); ``` |
| To | ``` OSStatus SSLCopyDistinguishedNames (     SSLContextRef _Nonnull context,     CFArrayRef  _Nullable * _Nonnull names ); ``` |

Modified [SSLCopyPeerCertificates()](https://developer.apple.com/documentation/security/1503748-sslcopypeercertificates)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLCopyPeerCertificates (     SSLContextRef context,     CFArrayRef *certs ); ``` |
| To | ``` OSStatus SSLCopyPeerCertificates (     SSLContextRef _Nonnull context,     CFArrayRef  _Nullable * _Nonnull certs ); ``` |

Modified [SSLCopyPeerTrust()](https://developer.apple.com/documentation/security/1397674-sslcopypeertrust)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLCopyPeerTrust (     SSLContextRef context,     SecTrustRef *trust ); ``` |
| To | ``` OSStatus SSLCopyPeerTrust (     SSLContextRef _Nonnull context,     SecTrustRef  _Nullable * _Nonnull trust ); ``` |

Modified [SSLCopyTrustedRoots()](https://developer.apple.com/documentation/security/1503838-sslcopytrustedroots)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLCopyTrustedRoots (     SSLContextRef context,     CFArrayRef *trustedRoots ); ``` |
| To | ``` OSStatus SSLCopyTrustedRoots (     SSLContextRef _Nonnull context,     CFArrayRef  _Nullable * _Nonnull trustedRoots ); ``` |

Modified [SSLCreateContext()](https://developer.apple.com/documentation/security/1393063-sslcreatecontext)

|  | Declaration |
| --- | --- |
| From | ``` SSLContextRef SSLCreateContext (     CFAllocatorRef alloc,     SSLProtocolSide protocolSide,     SSLConnectionType connectionType ); ``` |
| To | ``` SSLContextRef _Nullable SSLCreateContext (     CFAllocatorRef _Nullable alloc,     SSLProtocolSide protocolSide,     SSLConnectionType connectionType ); ``` |

Modified [SSLDisposeContext()](https://developer.apple.com/documentation/security/1503799-ssldisposecontext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLDisposeContext (     SSLContextRef context ); ``` |
| To | ``` OSStatus SSLDisposeContext (     SSLContextRef _Nonnull context ); ``` |

Modified [SSLGetAllowsAnyRoot()](https://developer.apple.com/documentation/security/1503841-sslgetallowsanyroot)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetAllowsAnyRoot (     SSLContextRef context,     Boolean *anyRoot ); ``` |
| To | ``` OSStatus SSLGetAllowsAnyRoot (     SSLContextRef _Nonnull context,     Boolean * _Nonnull anyRoot ); ``` |

Modified [SSLGetAllowsExpiredCerts()](https://developer.apple.com/documentation/security/1503806-sslgetallowsexpiredcerts)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetAllowsExpiredCerts (     SSLContextRef context,     Boolean *allowsExpired ); ``` |
| To | ``` OSStatus SSLGetAllowsExpiredCerts (     SSLContextRef _Nonnull context,     Boolean * _Nonnull allowsExpired ); ``` |

Modified [SSLGetAllowsExpiredRoots()](https://developer.apple.com/documentation/security/1503740-sslgetallowsexpiredroots)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetAllowsExpiredRoots (     SSLContextRef context,     Boolean *allowsExpired ); ``` |
| To | ``` OSStatus SSLGetAllowsExpiredRoots (     SSLContextRef _Nonnull context,     Boolean * _Nonnull allowsExpired ); ``` |

Modified [SSLGetBufferedReadSize()](https://developer.apple.com/documentation/security/1394958-sslgetbufferedreadsize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetBufferedReadSize (     SSLContextRef context,     size_t *bufSize ); ``` |
| To | ``` OSStatus SSLGetBufferedReadSize (     SSLContextRef _Nonnull context,     size_t * _Nonnull bufSize ); ``` |

Modified [SSLGetClientCertificateState()](https://developer.apple.com/documentation/security/1396612-sslgetclientcertificatestate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetClientCertificateState (     SSLContextRef context,     SSLClientCertificateState *clientState ); ``` |
| To | ``` OSStatus SSLGetClientCertificateState (     SSLContextRef _Nonnull context,     SSLClientCertificateState * _Nonnull clientState ); ``` |

Modified [SSLGetConnection()](https://developer.apple.com/documentation/security/1397993-sslgetconnection)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetConnection (     SSLContextRef context,     SSLConnectionRef *connection ); ``` |
| To | ``` OSStatus SSLGetConnection (     SSLContextRef _Nonnull context,     SSLConnectionRef  _Nullable * _Nonnull connection ); ``` |

Modified [SSLGetDatagramWriteSize()](https://developer.apple.com/documentation/security/1401259-sslgetdatagramwritesize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetDatagramWriteSize (     SSLContextRef dtlsContext,     size_t *bufSize ); ``` |
| To | ``` OSStatus SSLGetDatagramWriteSize (     SSLContextRef _Nonnull dtlsContext,     size_t * _Nonnull bufSize ); ``` |

Modified [SSLGetDiffieHellmanParams()](https://developer.apple.com/documentation/security/1399892-sslgetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetDiffieHellmanParams (     SSLContextRef context,     const void **dhParams,     size_t *dhParamsLen ); ``` |
| To | ``` OSStatus SSLGetDiffieHellmanParams (     SSLContextRef _Nonnull context,     const void * _Nullable * _Nonnull dhParams,     size_t * _Nonnull dhParamsLen ); ``` |

Modified [SSLGetEnableCertVerify()](https://developer.apple.com/documentation/security/1503774-sslgetenablecertverify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetEnableCertVerify (     SSLContextRef context,     Boolean *enableVerify ); ``` |
| To | ``` OSStatus SSLGetEnableCertVerify (     SSLContextRef _Nonnull context,     Boolean * _Nonnull enableVerify ); ``` |

Modified [SSLGetEnabledCiphers()](https://developer.apple.com/documentation/security/1399101-sslgetenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetEnabledCiphers (     SSLContextRef context,     SSLCipherSuite *ciphers,     size_t *numCiphers ); ``` |
| To | ``` OSStatus SSLGetEnabledCiphers (     SSLContextRef _Nonnull context,     SSLCipherSuite * _Nonnull ciphers,     size_t * _Nonnull numCiphers ); ``` |

Modified [SSLGetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1399678-sslgetmaxdatagramrecordsize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetMaxDatagramRecordSize (     SSLContextRef dtlsContext,     size_t *maxSize ); ``` |
| To | ``` OSStatus SSLGetMaxDatagramRecordSize (     SSLContextRef _Nonnull dtlsContext,     size_t * _Nonnull maxSize ); ``` |

Modified [SSLGetNegotiatedCipher()](https://developer.apple.com/documentation/security/1394448-sslgetnegotiatedcipher)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetNegotiatedCipher (     SSLContextRef context,     SSLCipherSuite *cipherSuite ); ``` |
| To | ``` OSStatus SSLGetNegotiatedCipher (     SSLContextRef _Nonnull context,     SSLCipherSuite * _Nonnull cipherSuite ); ``` |

Modified [SSLGetNegotiatedProtocolVersion()](https://developer.apple.com/documentation/security/1397382-sslgetnegotiatedprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetNegotiatedProtocolVersion (     SSLContextRef context,     SSLProtocol *protocol ); ``` |
| To | ``` OSStatus SSLGetNegotiatedProtocolVersion (     SSLContextRef _Nonnull context,     SSLProtocol * _Nonnull protocol ); ``` |

Modified [SSLGetNumberEnabledCiphers()](https://developer.apple.com/documentation/security/1399570-sslgetnumberenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetNumberEnabledCiphers (     SSLContextRef context,     size_t *numCiphers ); ``` |
| To | ``` OSStatus SSLGetNumberEnabledCiphers (     SSLContextRef _Nonnull context,     size_t * _Nonnull numCiphers ); ``` |

Modified [SSLGetNumberSupportedCiphers()](https://developer.apple.com/documentation/security/1402304-sslgetnumbersupportedciphers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetNumberSupportedCiphers (     SSLContextRef context,     size_t *numCiphers ); ``` |
| To | ``` OSStatus SSLGetNumberSupportedCiphers (     SSLContextRef _Nonnull context,     size_t * _Nonnull numCiphers ); ``` |

Modified [SSLGetPeerDomainName()](https://developer.apple.com/documentation/security/1400295-sslgetpeerdomainname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetPeerDomainName (     SSLContextRef context,     char *peerName,     size_t *peerNameLen ); ``` |
| To | ``` OSStatus SSLGetPeerDomainName (     SSLContextRef _Nonnull context,     char * _Nonnull peerName,     size_t * _Nonnull peerNameLen ); ``` |

Modified [SSLGetPeerDomainNameLength()](https://developer.apple.com/documentation/security/1398086-sslgetpeerdomainnamelength)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetPeerDomainNameLength (     SSLContextRef context,     size_t *peerNameLen ); ``` |
| To | ``` OSStatus SSLGetPeerDomainNameLength (     SSLContextRef _Nonnull context,     size_t * _Nonnull peerNameLen ); ``` |

Modified [SSLGetPeerID()](https://developer.apple.com/documentation/security/1395882-sslgetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetPeerID (     SSLContextRef context,     const void **peerID,     size_t *peerIDLen ); ``` |
| To | ``` OSStatus SSLGetPeerID (     SSLContextRef _Nonnull context,     const void * _Nullable * _Nonnull peerID,     size_t * _Nonnull peerIDLen ); ``` |

Modified [SSLGetProtocolVersion()](https://developer.apple.com/documentation/security/1503847-sslgetprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetProtocolVersion (     SSLContextRef context,     SSLProtocol *protocol ); ``` |
| To | ``` OSStatus SSLGetProtocolVersion (     SSLContextRef _Nonnull context,     SSLProtocol * _Nonnull protocol ); ``` |

Modified [SSLGetProtocolVersionEnabled()](https://developer.apple.com/documentation/security/1503767-sslgetprotocolversionenabled)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetProtocolVersionEnabled (     SSLContextRef context,     SSLProtocol protocol,     Boolean *enable ); ``` |
| To | ``` OSStatus SSLGetProtocolVersionEnabled (     SSLContextRef _Nonnull context,     SSLProtocol protocol,     Boolean * _Nonnull enable ); ``` |

Modified [SSLGetProtocolVersionMax()](https://developer.apple.com/documentation/security/1396167-sslgetprotocolversionmax)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetProtocolVersionMax (     SSLContextRef context,     SSLProtocol *maxVersion ); ``` |
| To | ``` OSStatus SSLGetProtocolVersionMax (     SSLContextRef _Nonnull context,     SSLProtocol * _Nonnull maxVersion ); ``` |

Modified [SSLGetProtocolVersionMin()](https://developer.apple.com/documentation/security/1395690-sslgetprotocolversionmin)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetProtocolVersionMin (     SSLContextRef context,     SSLProtocol *minVersion ); ``` |
| To | ``` OSStatus SSLGetProtocolVersionMin (     SSLContextRef _Nonnull context,     SSLProtocol * _Nonnull minVersion ); ``` |

Modified [SSLGetRsaBlinding()](https://developer.apple.com/documentation/security/1503742-sslgetrsablinding)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetRsaBlinding (     SSLContextRef context,     Boolean *blinding ); ``` |
| To | ``` OSStatus SSLGetRsaBlinding (     SSLContextRef _Nonnull context,     Boolean * _Nonnull blinding ); ``` |

Modified [SSLGetSessionOption()](https://developer.apple.com/documentation/security/1392604-sslgetsessionoption)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetSessionOption (     SSLContextRef context,     SSLSessionOption option,     Boolean *value ); ``` |
| To | ``` OSStatus SSLGetSessionOption (     SSLContextRef _Nonnull context,     SSLSessionOption option,     Boolean * _Nonnull value ); ``` |

Modified [SSLGetSessionState()](https://developer.apple.com/documentation/security/1393517-sslgetsessionstate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetSessionState (     SSLContextRef context,     SSLSessionState *state ); ``` |
| To | ``` OSStatus SSLGetSessionState (     SSLContextRef _Nonnull context,     SSLSessionState * _Nonnull state ); ``` |

Modified [SSLGetSupportedCiphers()](https://developer.apple.com/documentation/security/1395230-sslgetsupportedciphers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLGetSupportedCiphers (     SSLContextRef context,     SSLCipherSuite *ciphers,     size_t *numCiphers ); ``` |
| To | ``` OSStatus SSLGetSupportedCiphers (     SSLContextRef _Nonnull context,     SSLCipherSuite * _Nonnull ciphers,     size_t * _Nonnull numCiphers ); ``` |

Modified [SSLHandshake()](https://developer.apple.com/documentation/security/1400161-sslhandshake)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLHandshake (     SSLContextRef context ); ``` |
| To | ``` OSStatus SSLHandshake (     SSLContextRef _Nonnull context ); ``` |

Modified [SSLNewContext()](https://developer.apple.com/documentation/security/1503793-sslnewcontext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLNewContext (     Boolean isServer,     SSLContextRef *contextPtr ); ``` |
| To | ``` OSStatus SSLNewContext (     Boolean isServer,     SSLContextRef  _Nullable * _Nonnull contextPtr ); ``` |

Modified [SSLRead()](https://developer.apple.com/documentation/security/1394324-sslread)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLRead (     SSLContextRef context,     void *data,     size_t dataLength,     size_t *processed ); ``` |
| To | ``` OSStatus SSLRead (     SSLContextRef _Nonnull context,     void * _Nonnull data,     size_t dataLength,     size_t * _Nonnull processed ); ``` |

Modified [SSLSetAllowsAnyRoot()](https://developer.apple.com/documentation/security/1503848-sslsetallowsanyroot)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetAllowsAnyRoot (     SSLContextRef context,     Boolean anyRoot ); ``` |
| To | ``` OSStatus SSLSetAllowsAnyRoot (     SSLContextRef _Nonnull context,     Boolean anyRoot ); ``` |

Modified [SSLSetAllowsExpiredCerts()](https://developer.apple.com/documentation/security/1503738-sslsetallowsexpiredcerts)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetAllowsExpiredCerts (     SSLContextRef context,     Boolean allowsExpired ); ``` |
| To | ``` OSStatus SSLSetAllowsExpiredCerts (     SSLContextRef _Nonnull context,     Boolean allowsExpired ); ``` |

Modified [SSLSetAllowsExpiredRoots()](https://developer.apple.com/documentation/security/1503782-sslsetallowsexpiredroots)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetAllowsExpiredRoots (     SSLContextRef context,     Boolean allowsExpired ); ``` |
| To | ``` OSStatus SSLSetAllowsExpiredRoots (     SSLContextRef _Nonnull context,     Boolean allowsExpired ); ``` |

Modified [SSLSetCertificate()](https://developer.apple.com/documentation/security/1392400-sslsetcertificate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetCertificate (     SSLContextRef context,     CFArrayRef certRefs ); ``` |
| To | ``` OSStatus SSLSetCertificate (     SSLContextRef _Nonnull context,     CFArrayRef _Nonnull certRefs ); ``` |

Modified [SSLSetCertificateAuthorities()](https://developer.apple.com/documentation/security/1396770-sslsetcertificateauthorities)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetCertificateAuthorities (     SSLContextRef context,     CFTypeRef certificateOrArray,     Boolean replaceExisting ); ``` |
| To | ``` OSStatus SSLSetCertificateAuthorities (     SSLContextRef _Nonnull context,     CFTypeRef _Nonnull certificateOrArray,     Boolean replaceExisting ); ``` |

Modified [SSLSetClientSideAuthenticate()](https://developer.apple.com/documentation/security/1397567-sslsetclientsideauthenticate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetClientSideAuthenticate (     SSLContextRef context,     SSLAuthenticate auth ); ``` |
| To | ``` OSStatus SSLSetClientSideAuthenticate (     SSLContextRef _Nonnull context,     SSLAuthenticate auth ); ``` |

Modified [SSLSetConnection()](https://developer.apple.com/documentation/security/1398843-sslsetconnection)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetConnection (     SSLContextRef context,     SSLConnectionRef connection ); ``` |
| To | ``` OSStatus SSLSetConnection (     SSLContextRef _Nonnull context,     SSLConnectionRef _Nullable connection ); ``` |

Modified [SSLSetDatagramHelloCookie()](https://developer.apple.com/documentation/security/1398936-sslsetdatagramhellocookie)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetDatagramHelloCookie (     SSLContextRef dtlsContext,     const void *cookie,     size_t cookieLen ); ``` |
| To | ``` OSStatus SSLSetDatagramHelloCookie (     SSLContextRef _Nonnull dtlsContext,     const void * _Nullable cookie,     size_t cookieLen ); ``` |

Modified [SSLSetDiffieHellmanParams()](https://developer.apple.com/documentation/security/1392524-sslsetdiffiehellmanparams)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetDiffieHellmanParams (     SSLContextRef context,     const void *dhParams,     size_t dhParamsLen ); ``` |
| To | ``` OSStatus SSLSetDiffieHellmanParams (     SSLContextRef _Nonnull context,     const void * _Nullable dhParams,     size_t dhParamsLen ); ``` |

Modified [SSLSetEnableCertVerify()](https://developer.apple.com/documentation/security/1503735-sslsetenablecertverify)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetEnableCertVerify (     SSLContextRef context,     Boolean enableVerify ); ``` |
| To | ``` OSStatus SSLSetEnableCertVerify (     SSLContextRef _Nonnull context,     Boolean enableVerify ); ``` |

Modified [SSLSetEnabledCiphers()](https://developer.apple.com/documentation/security/1397188-sslsetenabledciphers)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetEnabledCiphers (     SSLContextRef context,     const SSLCipherSuite *ciphers,     size_t numCiphers ); ``` |
| To | ``` OSStatus SSLSetEnabledCiphers (     SSLContextRef _Nonnull context,     const SSLCipherSuite * _Nonnull ciphers,     size_t numCiphers ); ``` |

Modified [SSLSetEncryptionCertificate()](https://developer.apple.com/documentation/security/1398098-sslsetencryptioncertificate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` OSStatus SSLSetEncryptionCertificate (     SSLContextRef context,     CFArrayRef certRefs ); ``` | -- |
| To | ``` OSStatus SSLSetEncryptionCertificate (     SSLContextRef _Nonnull context,     CFArrayRef _Nonnull certRefs ); ``` | OS X 10.11 |

Modified [SSLSetIOFuncs()](https://developer.apple.com/documentation/security/1396081-sslsetiofuncs)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetIOFuncs (     SSLContextRef context,     SSLReadFunc readFunc,     SSLWriteFunc writeFunc ); ``` |
| To | ``` OSStatus SSLSetIOFuncs (     SSLContextRef _Nonnull context,     SSLReadFunc _Nonnull readFunc,     SSLWriteFunc _Nonnull writeFunc ); ``` |

Modified [SSLSetMaxDatagramRecordSize()](https://developer.apple.com/documentation/security/1394978-sslsetmaxdatagramrecordsize)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetMaxDatagramRecordSize (     SSLContextRef dtlsContext,     size_t maxSize ); ``` |
| To | ``` OSStatus SSLSetMaxDatagramRecordSize (     SSLContextRef _Nonnull dtlsContext,     size_t maxSize ); ``` |

Modified [SSLSetPeerDomainName()](https://developer.apple.com/documentation/security/1393047-sslsetpeerdomainname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetPeerDomainName (     SSLContextRef context,     const char *peerName,     size_t peerNameLen ); ``` |
| To | ``` OSStatus SSLSetPeerDomainName (     SSLContextRef _Nonnull context,     const char * _Nullable peerName,     size_t peerNameLen ); ``` |

Modified [SSLSetPeerID()](https://developer.apple.com/documentation/security/1400006-sslsetpeerid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetPeerID (     SSLContextRef context,     const void *peerID,     size_t peerIDLen ); ``` |
| To | ``` OSStatus SSLSetPeerID (     SSLContextRef _Nonnull context,     const void * _Nullable peerID,     size_t peerIDLen ); ``` |

Modified [SSLSetProtocolVersion()](https://developer.apple.com/documentation/security/1503760-sslsetprotocolversion)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetProtocolVersion (     SSLContextRef context,     SSLProtocol version ); ``` |
| To | ``` OSStatus SSLSetProtocolVersion (     SSLContextRef _Nonnull context,     SSLProtocol version ); ``` |

Modified [SSLSetProtocolVersionEnabled()](https://developer.apple.com/documentation/security/1503754-sslsetprotocolversionenabled)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetProtocolVersionEnabled (     SSLContextRef context,     SSLProtocol protocol,     Boolean enable ); ``` |
| To | ``` OSStatus SSLSetProtocolVersionEnabled (     SSLContextRef _Nonnull context,     SSLProtocol protocol,     Boolean enable ); ``` |

Modified [SSLSetProtocolVersionMax()](https://developer.apple.com/documentation/security/1393798-sslsetprotocolversionmax)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetProtocolVersionMax (     SSLContextRef context,     SSLProtocol maxVersion ); ``` |
| To | ``` OSStatus SSLSetProtocolVersionMax (     SSLContextRef _Nonnull context,     SSLProtocol maxVersion ); ``` |

Modified [SSLSetProtocolVersionMin()](https://developer.apple.com/documentation/security/1398139-sslsetprotocolversionmin)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetProtocolVersionMin (     SSLContextRef context,     SSLProtocol minVersion ); ``` |
| To | ``` OSStatus SSLSetProtocolVersionMin (     SSLContextRef _Nonnull context,     SSLProtocol minVersion ); ``` |

Modified [SSLSetRsaBlinding()](https://developer.apple.com/documentation/security/1503756-sslsetrsablinding)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetRsaBlinding (     SSLContextRef context,     Boolean blinding ); ``` |
| To | ``` OSStatus SSLSetRsaBlinding (     SSLContextRef _Nonnull context,     Boolean blinding ); ``` |

Modified [SSLSetSessionOption()](https://developer.apple.com/documentation/security/1399173-sslsetsessionoption)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetSessionOption (     SSLContextRef context,     SSLSessionOption option,     Boolean value ); ``` |
| To | ``` OSStatus SSLSetSessionOption (     SSLContextRef _Nonnull context,     SSLSessionOption option,     Boolean value ); ``` |

Modified [SSLSetTrustedRoots()](https://developer.apple.com/documentation/security/1503776-sslsettrustedroots)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLSetTrustedRoots (     SSLContextRef context,     CFArrayRef trustedRoots,     Boolean replaceExisting ); ``` |
| To | ``` OSStatus SSLSetTrustedRoots (     SSLContextRef _Nonnull context,     CFArrayRef _Nonnull trustedRoots,     Boolean replaceExisting ); ``` |

Modified [SSLWrite()](https://developer.apple.com/documentation/security/1400864-sslwrite)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus SSLWrite (     SSLContextRef context,     const void *data,     size_t dataLength,     size_t *processed ); ``` |
| To | ``` OSStatus SSLWrite (     SSLContextRef _Nonnull context,     const void * _Nullable data,     size_t dataLength,     size_t * _Nonnull processed ); ``` |

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
