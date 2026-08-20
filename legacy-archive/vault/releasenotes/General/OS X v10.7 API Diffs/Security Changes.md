---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Security.html
archived_at: '2026-07-18T02:54:39.084657Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Security Changes

## Security

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

AuthSession.hRemoved sessionWasInitializedAuthorization.hAdded [AuthorizationAsyncCallback](https://developer.apple.com/documentation/security/authorizationasynccallback)Added [AuthorizationCopyRightsAsync()](https://developer.apple.com/documentation/security/1394914-authorizationcopyrightsasync)Modified [AuthorizationCopyPrivilegedReference()](https://developer.apple.com/documentation/security/1540021-authorizationcopyprivilegedrefer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [AuthorizationExecuteWithPrivileges()](https://developer.apple.com/documentation/security/1540038-authorizationexecutewithprivileg)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CMSEncoder.hAdded [CMSEncodeContent()](https://developer.apple.com/documentation/security/1387113-cmsencodecontent)Added [CMSEncoderSetEncapsulatedContentTypeOID()](https://developer.apple.com/documentation/security/1387115-cmsencodersetencapsulatedcontent)CSCommon.hRemoved errSecCSInvalidOperationAdded [errSecCSInfoPlistFailed](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsinfoplistfailed)Added [errSecCSNoMainExecutable](https://developer.apple.com/documentation/security/1574088-code_signing_services_result_cod/errseccsnomainexecutable)Added [kSecCFErrorArchitecture](https://developer.apple.com/documentation/security/kseccferrorarchitecture)Added [kSecPluginRequirementType](https://developer.apple.com/documentation/security/secrequirementtype/ksecpluginrequirementtype)SecACL.hAdded [SecACLCopyAuthorizations()](https://developer.apple.com/documentation/security/1396830-secaclcopyauthorizations)Added [SecACLCopyContents()](https://developer.apple.com/documentation/security/1400970-secaclcopycontents)Added [SecACLCreateWithSimpleContents()](https://developer.apple.com/documentation/security/1402295-secaclcreatewithsimplecontents)Added [SecACLSetContents()](https://developer.apple.com/documentation/security/1400997-secaclsetcontents)Added [SecACLUpdateAuthorizations()](https://developer.apple.com/documentation/security/1392184-secaclupdateauthorizations)Added [SecKeychainPromptSelector](https://developer.apple.com/documentation/security/seckeychainpromptselector)Added [kSecKeychainPromptInvalid](https://developer.apple.com/documentation/security/seckeychainpromptselector/1392308-invalid)Added [kSecKeychainPromptInvalidAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptinvalidact)Added [kSecKeychainPromptRequirePassphase](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptrequirepassphase)Added [kSecKeychainPromptUnsigned](https://developer.apple.com/documentation/security/seckeychainpromptselector/1400870-unsigned)Added [kSecKeychainPromptUnsignedAct](https://developer.apple.com/documentation/security/seckeychainpromptselector/kseckeychainpromptunsignedact)Modified [SecACLCreateFromSimpleContents()](https://developer.apple.com/documentation/security/1577132-secaclcreatefromsimplecontents)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecACLSetAuthorizations()](https://developer.apple.com/documentation/security/1577130-secaclsetauthorizations)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecACLSetSimpleContents()](https://developer.apple.com/documentation/security/1577129-secaclsetsimplecontents)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecACLCopySimpleContents()](https://developer.apple.com/documentation/security/1577133-secaclcopysimplecontents)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecACLGetAuthorizations()](https://developer.apple.com/documentation/security/1577131-secaclgetauthorizations)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecAccess.hAdded [SecAccessCopyMatchingACLList()](https://developer.apple.com/documentation/security/1400464-secaccesscopymatchingacllist)Added [SecAccessCopyOwnerAndACL()](https://developer.apple.com/documentation/security/1402089-secaccesscopyownerandacl)Added [SecAccessCreateWithOwnerAndACL()](https://developer.apple.com/documentation/security/1395706-secaccesscreatewithownerandacl)Added [SecAccessOwnerType](https://developer.apple.com/documentation/security/secaccessownertype)Added [kSecACLAuthorizationAny](https://developer.apple.com/documentation/security/ksecaclauthorizationany)Added [kSecACLAuthorizationChangeACL](https://developer.apple.com/documentation/security/ksecaclauthorizationchangeacl)Added [kSecACLAuthorizationChangeOwner](https://developer.apple.com/documentation/security/ksecaclauthorizationchangeowner)Added [kSecACLAuthorizationDecrypt](https://developer.apple.com/documentation/security/ksecaclauthorizationdecrypt)Added [kSecACLAuthorizationDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationdelete)Added [kSecACLAuthorizationDerive](https://developer.apple.com/documentation/security/ksecaclauthorizationderive)Added [kSecACLAuthorizationEncrypt](https://developer.apple.com/documentation/security/ksecaclauthorizationencrypt)Added [kSecACLAuthorizationExportClear](https://developer.apple.com/documentation/security/ksecaclauthorizationexportclear)Added [kSecACLAuthorizationExportWrapped](https://developer.apple.com/documentation/security/ksecaclauthorizationexportwrapped)Added [kSecACLAuthorizationGenKey](https://developer.apple.com/documentation/security/ksecaclauthorizationgenkey)Added [kSecACLAuthorizationImportClear](https://developer.apple.com/documentation/security/ksecaclauthorizationimportclear)Added [kSecACLAuthorizationImportWrapped](https://developer.apple.com/documentation/security/ksecaclauthorizationimportwrapped)Added [kSecACLAuthorizationKeychainCreate](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychaincreate)Added [kSecACLAuthorizationKeychainDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychaindelete)Added [kSecACLAuthorizationKeychainItemDelete](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemdelete)Added [kSecACLAuthorizationKeychainItemInsert](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainiteminsert)Added [kSecACLAuthorizationKeychainItemModify](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemmodify)Added [kSecACLAuthorizationKeychainItemRead](https://developer.apple.com/documentation/security/ksecaclauthorizationkeychainitemread)Added [kSecACLAuthorizationLogin](https://developer.apple.com/documentation/security/ksecaclauthorizationlogin)Added [kSecACLAuthorizationMAC](https://developer.apple.com/documentation/security/ksecaclauthorizationmac)Added [kSecACLAuthorizationSign](https://developer.apple.com/documentation/security/ksecaclauthorizationsign)Added [kSecHonorRoot](https://developer.apple.com/documentation/security/1521098-secaccessownertype_values/ksechonorroot)Added [kSecMatchBits](https://developer.apple.com/documentation/security/ksecmatchbits)Added [kSecUseOnlyGID](https://developer.apple.com/documentation/security/ksecuseonlygid)Added [kSecUseOnlyUID](https://developer.apple.com/documentation/security/ksecuseonlyuid)Modified [SecAccessGetOwnerAndACL()](https://developer.apple.com/documentation/security/1521095-secaccessgetownerandacl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecAccessCreateFromOwnerAndACL()](https://developer.apple.com/documentation/security/1521118-secaccesscreatefromownerandacl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecAccessCopySelectedACLList()](https://developer.apple.com/documentation/security/1521111-secaccesscopyselectedacllist)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecBase.hAdded [errSecACLAddFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecacladdfailed)Added [errSecACLChangeFailed](https://developer.apple.com/documentation/security/errsecaclchangefailed)Added [errSecACLDeleteFailed](https://developer.apple.com/documentation/security/errsecacldeletefailed)Added [errSecACLReplaceFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecaclreplacefailed)Added [errSecAddinLoadFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecaddinloadfailed)Added [errSecAddinUnloadFailed](https://developer.apple.com/documentation/security/errsecaddinunloadfailed)Added [errSecAlgorithmMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecalgorithmmismatch)Added [errSecAlreadyLoggedIn](https://developer.apple.com/documentation/security/errsecalreadyloggedin)Added [errSecAppleAddAppACLSubject](https://developer.apple.com/documentation/security/errsecappleaddappaclsubject)Added [errSecAppleInvalidKeyEndDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecappleinvalidkeyenddate)Added [errSecAppleInvalidKeyStartDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecappleinvalidkeystartdate)Added [errSecApplePublicKeyIncomplete](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplepublickeyincomplete)Added [errSecAppleSSLv2Rollback](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplesslv2rollback)Added [errSecAppleSignatureMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecapplesignaturemismatch)Added [errSecAttachHandleBusy](https://developer.apple.com/documentation/security/errsecattachhandlebusy)Added [errSecAttributeNotInContext](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecattributenotincontext)Added [errSecBlockSizeMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecblocksizemismatch)Added [errSecCRLAlreadySigned](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlalreadysigned)Added [errSecCRLBadURI](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlbaduri)Added [errSecCRLExpired](https://developer.apple.com/documentation/security/errseccrlexpired)Added [errSecCRLNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlnotfound)Added [errSecCRLNotTrusted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlnottrusted)Added [errSecCRLNotValidYet](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlnotvalidyet)Added [errSecCRLPolicyFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccrlpolicyfailed)Added [errSecCRLServerDown](https://developer.apple.com/documentation/security/errseccrlserverdown)Added [errSecCallbackFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccallbackfailed)Added [errSecCertificateCannotOperate](https://developer.apple.com/documentation/security/errseccertificatecannotoperate)Added [errSecCertificateExpired](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificateexpired)Added [errSecCertificateNotValidYet](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccertificatenotvalidyet)Added [errSecCertificateRevoked](https://developer.apple.com/documentation/security/errseccertificaterevoked)Added [errSecCertificateSuspended](https://developer.apple.com/documentation/security/errseccertificatesuspended)Added [errSecCodeSigningBadCertChainLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningbadcertchainlength)Added [errSecCodeSigningBadPathLengthConstraint](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningbadpathlengthconstraint)Added [errSecCodeSigningDevelopment](https://developer.apple.com/documentation/security/errseccodesigningdevelopment)Added [errSecCodeSigningNoBasicConstraints](https://developer.apple.com/documentation/security/errseccodesigningnobasicconstraints)Added [errSecCodeSigningNoExtendedKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseccodesigningnoextendedkeyusage)Added [errSecConversionError](https://developer.apple.com/documentation/security/errsecconversionerror)Added [errSecDatabaseLocked](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdatabaselocked)Added [errSecDatastoreIsOpen](https://developer.apple.com/documentation/security/errsecdatastoreisopen)Added [errSecDeviceError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdeviceerror)Added [errSecDeviceFailed](https://developer.apple.com/documentation/security/errsecdevicefailed)Added [errSecDeviceReset](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdevicereset)Added [errSecDeviceVerifyFailed](https://developer.apple.com/documentation/security/errsecdeviceverifyfailed)Added [errSecDiskFull](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecdiskfull)Added [errSecEMMLoadFailed](https://developer.apple.com/documentation/security/errsecemmloadfailed)Added [errSecEMMUnloadFailed](https://developer.apple.com/documentation/security/errsecemmunloadfailed)Added [errSecEndOfData](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecendofdata)Added [errSecEventNotificationCallbackNotFound](https://developer.apple.com/documentation/security/errseceventnotificationcallbacknotfound)Added [errSecFieldSpecifiedMultiple](https://developer.apple.com/documentation/security/errsecfieldspecifiedmultiple)Added [errSecFileTooBig](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecfiletoobig)Added [errSecFunctionFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecfunctionfailed)Added [errSecFunctionIntegrityFail](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecfunctionintegrityfail)Added [errSecHostNameMismatch](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsechostnamemismatch)Added [errSecIDPFailure](https://developer.apple.com/documentation/security/errsecidpfailure)Added [errSecIncompatibleDatabaseBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatibledatabaseblob)Added [errSecIncompatibleFieldFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatiblefieldformat)Added [errSecIncompatibleKeyBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatiblekeyblob)Added [errSecIncompatibleVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompatibleversion)Added [errSecIncompleteCertRevocationCheck](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecincompletecertrevocationcheck)Added [errSecInputLengthError](https://developer.apple.com/documentation/security/errsecinputlengtherror)Added [errSecInsufficientClientID](https://developer.apple.com/documentation/security/errsecinsufficientclientid)Added [errSecInsufficientCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinsufficientcredentials)Added [errSecInternalError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinternalerror)Added [errSecInvaldCRLAuthority](https://developer.apple.com/documentation/security/errsecinvaldcrlauthority)Added [errSecInvalidACL](https://developer.apple.com/documentation/security/errsecinvalidacl)Added [errSecInvalidAccessCredentials](https://developer.apple.com/documentation/security/errsecinvalidaccesscredentials)Added [errSecInvalidAccessRequest](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaccessrequest)Added [errSecInvalidAction](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaction)Added [errSecInvalidAddinFunctionTable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidaddinfunctiontable)Added [errSecInvalidAlgorithm](https://developer.apple.com/documentation/security/errsecinvalidalgorithm)Added [errSecInvalidAlgorithmParms](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidalgorithmparms)Added [errSecInvalidAttributeAccessCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeaccesscredentials)Added [errSecInvalidAttributeBase](https://developer.apple.com/documentation/security/errsecinvalidattributebase)Added [errSecInvalidAttributeBlockSize](https://developer.apple.com/documentation/security/errsecinvalidattributeblocksize)Added [errSecInvalidAttributeDLDBHandle](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributedldbhandle)Added [errSecInvalidAttributeEffectiveBits](https://developer.apple.com/documentation/security/errsecinvalidattributeeffectivebits)Added [errSecInvalidAttributeEndDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeenddate)Added [errSecInvalidAttributeInitVector](https://developer.apple.com/documentation/security/errsecinvalidattributeinitvector)Added [errSecInvalidAttributeIterationCount](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeiterationcount)Added [errSecInvalidAttributeKey](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributekey)Added [errSecInvalidAttributeKeyLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributekeylength)Added [errSecInvalidAttributeKeyType](https://developer.apple.com/documentation/security/errsecinvalidattributekeytype)Added [errSecInvalidAttributeLabel](https://developer.apple.com/documentation/security/errsecinvalidattributelabel)Added [errSecInvalidAttributeMode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributemode)Added [errSecInvalidAttributeOutputSize](https://developer.apple.com/documentation/security/errsecinvalidattributeoutputsize)Added [errSecInvalidAttributePadding](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributepadding)Added [errSecInvalidAttributePassphrase](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributepassphrase)Added [errSecInvalidAttributePrime](https://developer.apple.com/documentation/security/errsecinvalidattributeprime)Added [errSecInvalidAttributePrivateKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeprivatekeyformat)Added [errSecInvalidAttributePublicKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidattributepublickeyformat)Added [errSecInvalidAttributeRandom](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributerandom)Added [errSecInvalidAttributeRounds](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributerounds)Added [errSecInvalidAttributeSalt](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributesalt)Added [errSecInvalidAttributeSeed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeseed)Added [errSecInvalidAttributeStartDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributestartdate)Added [errSecInvalidAttributeSubprime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributesubprime)Added [errSecInvalidAttributeSymmetricKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidattributesymmetrickeyformat)Added [errSecInvalidAttributeVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributeversion)Added [errSecInvalidAttributeWrappedKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidattributewrappedkeyformat)Added [errSecInvalidAuthority](https://developer.apple.com/documentation/security/errsecinvalidauthority)Added [errSecInvalidAuthorityKeyID](https://developer.apple.com/documentation/security/errsecinvalidauthoritykeyid)Added [errSecInvalidBaseACLs](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidbaseacls)Added [errSecInvalidBundleInfo](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidbundleinfo)Added [errSecInvalidCRL](https://developer.apple.com/documentation/security/errsecinvalidcrl)Added [errSecInvalidCRLEncoding](https://developer.apple.com/documentation/security/errsecinvalidcrlencoding)Added [errSecInvalidCRLGroup](https://developer.apple.com/documentation/security/errsecinvalidcrlgroup)Added [errSecInvalidCRLIndex](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcrlindex)Added [errSecInvalidCRLType](https://developer.apple.com/documentation/security/errsecinvalidcrltype)Added [errSecInvalidCertAuthority](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcertauthority)Added [errSecInvalidCertificateGroup](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcertificategroup)Added [errSecInvalidCertificateRef](https://developer.apple.com/documentation/security/errsecinvalidcertificateref)Added [errSecInvalidContext](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidcontext)Added [errSecInvalidDBList](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaliddblist)Added [errSecInvalidDBLocation](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvaliddblocation)Added [errSecInvalidData](https://developer.apple.com/documentation/security/errsecinvaliddata)Added [errSecInvalidDatabaseBlob](https://developer.apple.com/documentation/security/errsecinvaliddatabaseblob)Added [errSecInvalidDigestAlgorithm](https://developer.apple.com/documentation/security/errsecinvaliddigestalgorithm)Added [errSecInvalidEncoding](https://developer.apple.com/documentation/security/errsecinvalidencoding)Added [errSecInvalidExtendedKeyUsage](https://developer.apple.com/documentation/security/errsecinvalidextendedkeyusage)Added [errSecInvalidFormType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidformtype)Added [errSecInvalidGUID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidguid)Added [errSecInvalidHandle](https://developer.apple.com/documentation/security/errsecinvalidhandle)Added [errSecInvalidHandleUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidhandleusage)Added [errSecInvalidID](https://developer.apple.com/documentation/security/errsecinvalidid)Added [errSecInvalidIDLinkage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalididlinkage)Added [errSecInvalidIdentifier](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalididentifier)Added [errSecInvalidIndex](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidindex)Added [errSecInvalidIndexInfo](https://developer.apple.com/documentation/security/errsecinvalidindexinfo)Added [errSecInvalidInputVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidinputvector)Added [errSecInvalidKeyAttributeMask](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyattributemask)Added [errSecInvalidKeyBlob](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyblob)Added [errSecInvalidKeyFormat](https://developer.apple.com/documentation/security/errsecinvalidkeyformat)Added [errSecInvalidKeyHierarchy](https://developer.apple.com/documentation/security/errsecinvalidkeyhierarchy)Added [errSecInvalidKeyLabel](https://developer.apple.com/documentation/security/errsecinvalidkeylabel)Added [errSecInvalidKeyRef](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyref)Added [errSecInvalidKeyUsageForPolicy](https://developer.apple.com/documentation/security/errsecinvalidkeyusageforpolicy)Added [errSecInvalidKeyUsageMask](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidkeyusagemask)Added [errSecInvalidLoginName](https://developer.apple.com/documentation/security/errsecinvalidloginname)Added [errSecInvalidModifyMode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidmodifymode)Added [errSecInvalidName](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidname)Added [errSecInvalidNetworkAddress](https://developer.apple.com/documentation/security/errsecinvalidnetworkaddress)Added [errSecInvalidNewOwner](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidnewowner)Added [errSecInvalidNumberOfFields](https://developer.apple.com/documentation/security/errsecinvalidnumberoffields)Added [errSecInvalidOutputVector](https://developer.apple.com/documentation/security/errsecinvalidoutputvector)Added [errSecInvalidPVC](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidpvc)Added [errSecInvalidParsingModule](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidparsingmodule)Added [errSecInvalidPassthroughID](https://developer.apple.com/documentation/security/errsecinvalidpassthroughid)Added [errSecInvalidPointer](https://developer.apple.com/documentation/security/errsecinvalidpointer)Added [errSecInvalidPolicyIdentifiers](https://developer.apple.com/documentation/security/errsecinvalidpolicyidentifiers)Added [errSecInvalidQuery](https://developer.apple.com/documentation/security/errsecinvalidquery)Added [errSecInvalidReason](https://developer.apple.com/documentation/security/errsecinvalidreason)Added [errSecInvalidRecord](https://developer.apple.com/documentation/security/errsecinvalidrecord)Added [errSecInvalidRequestInputs](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidrequestinputs)Added [errSecInvalidRequestor](https://developer.apple.com/documentation/security/errsecinvalidrequestor)Added [errSecInvalidResponseVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidresponsevector)Added [errSecInvalidRoot](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidroot)Added [errSecInvalidSampleValue](https://developer.apple.com/documentation/security/errsecinvalidsamplevalue)Added [errSecInvalidScope](https://developer.apple.com/documentation/security/errsecinvalidscope)Added [errSecInvalidServiceMask](https://developer.apple.com/documentation/security/errsecinvalidservicemask)Added [errSecInvalidSignature](https://developer.apple.com/documentation/security/errsecinvalidsignature)Added [errSecInvalidStopOnPolicy](https://developer.apple.com/documentation/security/errsecinvalidstoponpolicy)Added [errSecInvalidSubServiceID](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidsubserviceid)Added [errSecInvalidSubjectKeyID](https://developer.apple.com/documentation/security/errsecinvalidsubjectkeyid)Added [errSecInvalidSubjectName](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecinvalidsubjectname)Added [errSecInvalidTimeString](https://developer.apple.com/documentation/security/errsecinvalidtimestring)Added [errSecInvalidTuple](https://developer.apple.com/documentation/security/errsecinvalidtuple)Added [errSecInvalidTupleCredendtials](https://developer.apple.com/documentation/security/errsecinvalidtuplecredendtials)Added [errSecInvalidTupleGroup](https://developer.apple.com/documentation/security/errsecinvalidtuplegroup)Added [errSecInvalidValidityPeriod](https://developer.apple.com/documentation/security/errsecinvalidvalidityperiod)Added [errSecInvalidValue](https://developer.apple.com/documentation/security/errsecinvalidvalue)Added [errSecKeyBlobTypeIncorrect](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyblobtypeincorrect)Added [errSecKeyHeaderInconsistent](https://developer.apple.com/documentation/security/errseckeyheaderinconsistent)Added [errSecKeyUsageIncorrect](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseckeyusageincorrect)Added [errSecLibraryReferenceNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errseclibraryreferencenotfound)Added [errSecMDSError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmdserror)Added [errSecMemoryError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmemoryerror)Added [errSecMissingAlgorithmParms](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingalgorithmparms)Added [errSecMissingAttributeAccessCredentials](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeaccesscredentials)Added [errSecMissingAttributeBase](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributebase)Added [errSecMissingAttributeBlockSize](https://developer.apple.com/documentation/security/errsecmissingattributeblocksize)Added [errSecMissingAttributeDLDBHandle](https://developer.apple.com/documentation/security/errsecmissingattributedldbhandle)Added [errSecMissingAttributeEffectiveBits](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeeffectivebits)Added [errSecMissingAttributeEndDate](https://developer.apple.com/documentation/security/errsecmissingattributeenddate)Added [errSecMissingAttributeInitVector](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeinitvector)Added [errSecMissingAttributeIterationCount](https://developer.apple.com/documentation/security/errsecmissingattributeiterationcount)Added [errSecMissingAttributeKey](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributekey)Added [errSecMissingAttributeKeyLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributekeylength)Added [errSecMissingAttributeKeyType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributekeytype)Added [errSecMissingAttributeLabel](https://developer.apple.com/documentation/security/errsecmissingattributelabel)Added [errSecMissingAttributeMode](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributemode)Added [errSecMissingAttributeOutputSize](https://developer.apple.com/documentation/security/errsecmissingattributeoutputsize)Added [errSecMissingAttributePadding](https://developer.apple.com/documentation/security/errsecmissingattributepadding)Added [errSecMissingAttributePassphrase](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributepassphrase)Added [errSecMissingAttributePrime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeprime)Added [errSecMissingAttributePrivateKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeprivatekeyformat)Added [errSecMissingAttributePublicKeyFormat](https://developer.apple.com/documentation/security/errsecmissingattributepublickeyformat)Added [errSecMissingAttributeRandom](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributerandom)Added [errSecMissingAttributeRounds](https://developer.apple.com/documentation/security/errsecmissingattributerounds)Added [errSecMissingAttributeSalt](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributesalt)Added [errSecMissingAttributeSeed](https://developer.apple.com/documentation/security/errsecmissingattributeseed)Added [errSecMissingAttributeStartDate](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributestartdate)Added [errSecMissingAttributeSubprime](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributesubprime)Added [errSecMissingAttributeSymmetricKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributesymmetrickeyformat)Added [errSecMissingAttributeVersion](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributeversion)Added [errSecMissingAttributeWrappedKeyFormat](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmissingattributewrappedkeyformat)Added [errSecMissingValue](https://developer.apple.com/documentation/security/errsecmissingvalue)Added [errSecMobileMeCSRVerifyFailure](https://developer.apple.com/documentation/security/errsecmobilemecsrverifyfailure)Added [errSecMobileMeFailedConsistencyCheck](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemefailedconsistencycheck)Added [errSecMobileMeNoRequestPending](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemenorequestpending)Added [errSecMobileMeRequestAlreadyPending](https://developer.apple.com/documentation/security/errsecmobilemerequestalreadypending)Added [errSecMobileMeRequestQueued](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemerequestqueued)Added [errSecMobileMeRequestRedirected](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemerequestredirected)Added [errSecMobileMeServerAlreadyExists](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemeserveralreadyexists)Added [errSecMobileMeServerError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemeservererror)Added [errSecMobileMeServerNotAvailable](https://developer.apple.com/documentation/security/errsecmobilemeservernotavailable)Added [errSecMobileMeServerServiceErr](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmobilemeserverserviceerr)Added [errSecModuleManagerInitializeFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulemanagerinitializefailed)Added [errSecModuleManagerNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulemanagernotfound)Added [errSecModuleManifestVerifyFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulemanifestverifyfailed)Added [errSecModuleNotLoaded](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecmodulenotloaded)Added [errSecMultipleValuesUnsupported](https://developer.apple.com/documentation/security/errsecmultiplevaluesunsupported)Added [errSecNetworkFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnetworkfailure)Added [errSecNoBasicConstraints](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnobasicconstraints)Added [errSecNoBasicConstraintsCA](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnobasicconstraintsca)Added [errSecNoDefaultAuthority](https://developer.apple.com/documentation/security/errsecnodefaultauthority)Added [errSecNoFieldValues](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnofieldvalues)Added [errSecNotInitialized](https://developer.apple.com/documentation/security/errsecnotinitialized)Added [errSecNotLoggedIn](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnotloggedin)Added [errSecNotSigner](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecnotsigner)Added [errSecNotTrusted](https://developer.apple.com/documentation/security/errsecnottrusted)Added [errSecOCSPBadRequest](https://developer.apple.com/documentation/security/errsecocspbadrequest)Added [errSecOCSPBadResponse](https://developer.apple.com/documentation/security/errsecocspbadresponse)Added [errSecOCSPNoSigner](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspnosigner)Added [errSecOCSPNotTrustedToAnchor](https://developer.apple.com/documentation/security/errsecocspnottrustedtoanchor)Added [errSecOCSPResponderInternalError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspresponderinternalerror)Added [errSecOCSPResponderMalformedReq](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocsprespondermalformedreq)Added [errSecOCSPResponderSignatureRequired](https://developer.apple.com/documentation/security/errsecocsprespondersignaturerequired)Added [errSecOCSPResponderTryLater](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocsprespondertrylater)Added [errSecOCSPResponderUnauthorized](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspresponderunauthorized)Added [errSecOCSPResponseNonceMismatch](https://developer.apple.com/documentation/security/errsecocspresponsenoncemismatch)Added [errSecOCSPSignatureError](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspsignatureerror)Added [errSecOCSPStatusUnrecognized](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspstatusunrecognized)Added [errSecOCSPUnavailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecocspunavailable)Added [errSecOutputLengthError](https://developer.apple.com/documentation/security/errsecoutputlengtherror)Added [errSecPVCAlreadyConfigured](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpvcalreadyconfigured)Added [errSecPVCReferentNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpvcreferentnotfound)Added [errSecPathLengthConstraintExceeded](https://developer.apple.com/documentation/security/errsecpathlengthconstraintexceeded)Added [errSecPrivilegeNotGranted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecprivilegenotgranted)Added [errSecPrivilegeNotSupported](https://developer.apple.com/documentation/security/errsecprivilegenotsupported)Added [errSecPublicKeyInconsistent](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecpublickeyinconsistent)Added [errSecQuerySizeUnknown](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecquerysizeunknown)Added [errSecQuotaExceeded](https://developer.apple.com/documentation/security/errsecquotaexceeded)Added [errSecRecordModified](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecrecordmodified)Added [errSecRejectedForm](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecrejectedform)Added [errSecRequestDescriptor](https://developer.apple.com/documentation/security/errsecrequestdescriptor)Added [errSecRequestLost](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecrequestlost)Added [errSecRequestRejected](https://developer.apple.com/documentation/security/errsecrequestrejected)Added [errSecResourceSignBadCertChainLength](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecresourcesignbadcertchainlength)Added [errSecResourceSignBadExtKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecresourcesignbadextkeyusage)Added [errSecSMIMEBadExtendedKeyUsage](https://developer.apple.com/documentation/security/errsecsmimebadextendedkeyusage)Added [errSecSMIMEBadKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimebadkeyusage)Added [errSecSMIMEEmailAddressesNotFound](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimeemailaddressesnotfound)Added [errSecSMIMEKeyUsageNotCritical](https://developer.apple.com/documentation/security/errsecsmimekeyusagenotcritical)Added [errSecSMIMENoEmailAddress](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimenoemailaddress)Added [errSecSMIMESubjAltNameNotCritical](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsmimesubjaltnamenotcritical)Added [errSecSSLBadExtendedKeyUsage](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecsslbadextendedkeyusage)Added [errSecSelfCheckFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecselfcheckfailed)Added [errSecServiceNotAvailable](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecservicenotavailable)Added [errSecStagedOperationInProgress](https://developer.apple.com/documentation/security/errsecstagedoperationinprogress)Added [errSecStagedOperationNotStarted](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecstagedoperationnotstarted)Added [errSecTagNotFound](https://developer.apple.com/documentation/security/errsectagnotfound)Added [errSecTrustSettingDeny](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsectrustsettingdeny)Added [errSecUnknownCRLExtension](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknowncrlextension)Added [errSecUnknownCertExtension](https://developer.apple.com/documentation/security/errsecunknowncertextension)Added [errSecUnknownCriticalExtensionFlag](https://developer.apple.com/documentation/security/errsecunknowncriticalextensionflag)Added [errSecUnknownQualifiedCertStatement](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknownqualifiedcertstatement)Added [errSecUnknownTag](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunknowntag)Added [errSecUnsupportedAddressType](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedaddresstype)Added [errSecUnsupportedFieldFormat](https://developer.apple.com/documentation/security/errsecunsupportedfieldformat)Added [errSecUnsupportedIndexInfo](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedindexinfo)Added [errSecUnsupportedKeyAttributeMask](https://developer.apple.com/documentation/security/errsecunsupportedkeyattributemask)Added [errSecUnsupportedKeyFormat](https://developer.apple.com/documentation/security/errsecunsupportedkeyformat)Added [errSecUnsupportedKeyLabel](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedkeylabel)Added [errSecUnsupportedKeySize](https://developer.apple.com/documentation/security/errsecunsupportedkeysize)Added [errSecUnsupportedKeyUsageMask](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedkeyusagemask)Added [errSecUnsupportedLocality](https://developer.apple.com/documentation/security/errsecunsupportedlocality)Added [errSecUnsupportedNumAttributes](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumattributes)Added [errSecUnsupportedNumIndexes](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumindexes)Added [errSecUnsupportedNumRecordTypes](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumrecordtypes)Added [errSecUnsupportedNumSelectionPreds](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportednumselectionpreds)Added [errSecUnsupportedOperator](https://developer.apple.com/documentation/security/errsecunsupportedoperator)Added [errSecUnsupportedQueryLimits](https://developer.apple.com/documentation/security/errsecunsupportedquerylimits)Added [errSecUnsupportedService](https://developer.apple.com/documentation/security/errsecunsupportedservice)Added [errSecUnsupportedVectorOfBuffers](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecunsupportedvectorofbuffers)Added [errSecVerificationFailure](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecverificationfailure)Added [errSecVerifyActionFailed](https://developer.apple.com/documentation/security/1542001-security_framework_result_codes/errsecverifyactionfailed)Added [errSecVerifyFailed](https://developer.apple.com/documentation/security/errsecverifyfailed)SecCertificate.hAdded [SecCertificateCopyLongDescription()](https://developer.apple.com/documentation/security/1396088-seccertificatecopylongdescriptio)Added [SecCertificateCopyNormalizedIssuerContent()](https://developer.apple.com/documentation/security/1392318-seccertificatecopynormalizedissu)Added [SecCertificateCopyNormalizedSubjectContent()](https://developer.apple.com/documentation/security/1396030-seccertificatecopynormalizedsubj)Added [SecCertificateCopyPreferred()](https://developer.apple.com/documentation/security/1396028-seccertificatecopypreferred)Added [SecCertificateCopySerialNumber()](https://developer.apple.com/documentation/security/1394241-seccertificatecopyserialnumber)Added [SecCertificateCopyShortDescription()](https://developer.apple.com/documentation/security/1396036-seccertificatecopyshortdescripti)Added [SecCertificateCopyValues()](https://developer.apple.com/documentation/security/1396051-seccertificatecopyvalues)Added [SecCertificateSetPreferred()](https://developer.apple.com/documentation/security/1393683-seccertificatesetpreferred)Added kSecCertificateUsageDeriveAndSignAdded kSecCertificateUsageSigningAdded kSecCertificateUsageSigningAndEncryptingAdded [kSecPropertyKeyLabel](https://developer.apple.com/documentation/security/ksecpropertykeylabel)Added [kSecPropertyKeyLocalizedLabel](https://developer.apple.com/documentation/security/ksecpropertykeylocalizedlabel)Added [kSecPropertyKeyType](https://developer.apple.com/documentation/security/ksecpropertykeytype)Added [kSecPropertyKeyValue](https://developer.apple.com/documentation/security/ksecpropertykeyvalue)Added [kSecPropertyTypeData](https://developer.apple.com/documentation/security/ksecpropertytypedata)Added [kSecPropertyTypeDate](https://developer.apple.com/documentation/security/ksecpropertytypedate)Added [kSecPropertyTypeSection](https://developer.apple.com/documentation/security/ksecpropertytypesection)Added [kSecPropertyTypeString](https://developer.apple.com/documentation/security/ksecpropertytypestring)Added [kSecPropertyTypeSuccess](https://developer.apple.com/documentation/security/ksecpropertytypesuccess)Added [kSecPropertyTypeURL](https://developer.apple.com/documentation/security/ksecpropertytypeurl)Added [kSecPropertyTypeWarning](https://developer.apple.com/documentation/security/ksecpropertytypewarning)Modified [SecCertificateGetCLHandle()](https://developer.apple.com/documentation/security/1396053-seccertificategetclhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateGetIssuer()](https://developer.apple.com/documentation/security/1396068-seccertificategetissuer)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateCreateFromData()](https://developer.apple.com/documentation/security/1396025-seccertificatecreatefromdata)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateSetPreference()](https://developer.apple.com/documentation/security/1396063-seccertificatesetpreference)

|  | Declaration |
| --- | --- |
| From | OSStatus SecCertificateSetPreference ( SecCertificateRef certificate, CFStringRef name, CSSM_KEYUSE keyUsage, CFDateRef date); |
| To | OSStatus SecCertificateSetPreference ( SecCertificateRef certificate, CFStringRef name, uint32 keyUsage, CFDateRef date); |

Modified [SecCertificateCopyPreference()](https://developer.apple.com/documentation/security/1396094-seccertificatecopypreference)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | OSStatus SecCertificateCopyPreference ( CFStringRef name, CSSM_KEYUSE keyUsage, SecCertificateRef \*certificate); |
| To | OS X v10.7 | OSStatus SecCertificateCopyPreference ( CFStringRef name, uint32 keyUsage, SecCertificateRef \*certificate); |

Modified [SecCertificateGetData()](https://developer.apple.com/documentation/security/1396100-seccertificategetdata)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateGetType()](https://developer.apple.com/documentation/security/1396092-seccertificategettype)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateGetSubject()](https://developer.apple.com/documentation/security/1396032-seccertificategetsubject)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecCertificateGetAlgorithmID()](https://developer.apple.com/documentation/security/1396071-seccertificategetalgorithmid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecCertificateOIDs.hAdded [kSecOIDADC_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoidadc_cert_policy)Added [kSecOIDAPPLE_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoidapple_cert_policy)Added [kSecOIDAPPLE_EKU_CODE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_code_signing)Added [kSecOIDAPPLE_EKU_CODE_SIGNING_DEV](https://developer.apple.com/documentation/security/ksecoidapple_eku_code_signing_dev)Added [kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION](https://developer.apple.com/documentation/security/ksecoidapple_eku_ichat_encryption)Added [kSecOIDAPPLE_EKU_ICHAT_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_ichat_signing)Added [kSecOIDAPPLE_EKU_RESOURCE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_eku_resource_signing)Added [kSecOIDAPPLE_EKU_SYSTEM_IDENTITY](https://developer.apple.com/documentation/security/ksecoidapple_eku_system_identity)Added [kSecOIDAPPLE_EXTENSION](https://developer.apple.com/documentation/security/ksecoidapple_extension)Added [kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_aai_intermediate)Added [kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_adc_apple_signing)Added [kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_adc_dev_signing)Added [kSecOIDAPPLE_EXTENSION_APPLE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_apple_signing)Added [kSecOIDAPPLE_EXTENSION_CODE_SIGNING](https://developer.apple.com/documentation/security/ksecoidapple_extension_code_signing)Added [kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER](https://developer.apple.com/documentation/security/ksecoidapple_extension_intermediate_marker)Added [kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_itms_intermediate)Added [kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE](https://developer.apple.com/documentation/security/ksecoidapple_extension_wwdr_intermediate)Added [kSecOIDAuthorityInfoAccess](https://developer.apple.com/documentation/security/ksecoidauthorityinfoaccess)Added [kSecOIDAuthorityKeyIdentifier](https://developer.apple.com/documentation/security/ksecoidauthoritykeyidentifier)Added [kSecOIDBasicConstraints](https://developer.apple.com/documentation/security/ksecoidbasicconstraints)Added [kSecOIDBiometricInfo](https://developer.apple.com/documentation/security/ksecoidbiometricinfo)Added [kSecOIDCSSMKeyStruct](https://developer.apple.com/documentation/security/ksecoidcssmkeystruct)Added [kSecOIDCertIssuer](https://developer.apple.com/documentation/security/ksecoidcertissuer)Added [kSecOIDCertificatePolicies](https://developer.apple.com/documentation/security/ksecoidcertificatepolicies)Added [kSecOIDClientAuth](https://developer.apple.com/documentation/security/ksecoidclientauth)Added [kSecOIDCollectiveStateProvinceName](https://developer.apple.com/documentation/security/ksecoidcollectivestateprovincename)Added [kSecOIDCollectiveStreetAddress](https://developer.apple.com/documentation/security/ksecoidcollectivestreetaddress)Added [kSecOIDCommonName](https://developer.apple.com/documentation/security/ksecoidcommonname)Added [kSecOIDCountryName](https://developer.apple.com/documentation/security/ksecoidcountryname)Added [kSecOIDCrlDistributionPoints](https://developer.apple.com/documentation/security/ksecoidcrldistributionpoints)Added [kSecOIDCrlNumber](https://developer.apple.com/documentation/security/ksecoidcrlnumber)Added [kSecOIDCrlReason](https://developer.apple.com/documentation/security/ksecoidcrlreason)Added [kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_email_encrypt)Added [kSecOIDDOTMAC_CERT_EMAIL_SIGN](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_email_sign)Added [kSecOIDDOTMAC_CERT_EXTENSION](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_extension)Added [kSecOIDDOTMAC_CERT_IDENTITY](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_identity)Added [kSecOIDDOTMAC_CERT_POLICY](https://developer.apple.com/documentation/security/ksecoiddotmac_cert_policy)Added [kSecOIDDeltaCrlIndicator](https://developer.apple.com/documentation/security/ksecoiddeltacrlindicator)Added [kSecOIDDescription](https://developer.apple.com/documentation/security/ksecoiddescription)Added [kSecOIDEKU_IPSec](https://developer.apple.com/documentation/security/ksecoideku_ipsec)Added [kSecOIDEmailAddress](https://developer.apple.com/documentation/security/ksecoidemailaddress)Added [kSecOIDEmailProtection](https://developer.apple.com/documentation/security/ksecoidemailprotection)Added [kSecOIDExtendedKeyUsage](https://developer.apple.com/documentation/security/ksecoidextendedkeyusage)Added [kSecOIDExtendedKeyUsageAny](https://developer.apple.com/documentation/security/ksecoidextendedkeyusageany)Added [kSecOIDExtendedUseCodeSigning](https://developer.apple.com/documentation/security/ksecoidextendedusecodesigning)Added [kSecOIDGivenName](https://developer.apple.com/documentation/security/ksecoidgivenname)Added [kSecOIDHoldInstructionCode](https://developer.apple.com/documentation/security/ksecoidholdinstructioncode)Added [kSecOIDInvalidityDate](https://developer.apple.com/documentation/security/ksecoidinvaliditydate)Added [kSecOIDIssuerAltName](https://developer.apple.com/documentation/security/ksecoidissueraltname)Added [kSecOIDIssuingDistributionPoint](https://developer.apple.com/documentation/security/ksecoidissuingdistributionpoint)Added [kSecOIDIssuingDistributionPoints](https://developer.apple.com/documentation/security/ksecoidissuingdistributionpoints)Added [kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH](https://developer.apple.com/documentation/security/ksecoidkerbv5_pkinit_kp_client_auth)Added [kSecOIDKERBv5_PKINIT_KP_KDC](https://developer.apple.com/documentation/security/ksecoidkerbv5_pkinit_kp_kdc)Added [kSecOIDKeyUsage](https://developer.apple.com/documentation/security/ksecoidkeyusage)Added [kSecOIDLocalityName](https://developer.apple.com/documentation/security/ksecoidlocalityname)Added [kSecOIDMS_NTPrincipalName](https://developer.apple.com/documentation/security/ksecoidms_ntprincipalname)Added [kSecOIDMicrosoftSGC](https://developer.apple.com/documentation/security/ksecoidmicrosoftsgc)Added [kSecOIDNameConstraints](https://developer.apple.com/documentation/security/ksecoidnameconstraints)Added [kSecOIDNetscapeCertSequence](https://developer.apple.com/documentation/security/ksecoidnetscapecertsequence)Added [kSecOIDNetscapeCertType](https://developer.apple.com/documentation/security/ksecoidnetscapecerttype)Added [kSecOIDNetscapeSGC](https://developer.apple.com/documentation/security/ksecoidnetscapesgc)Added [kSecOIDOCSPSigning](https://developer.apple.com/documentation/security/ksecoidocspsigning)Added [kSecOIDOrganizationName](https://developer.apple.com/documentation/security/ksecoidorganizationname)Added [kSecOIDOrganizationalUnitName](https://developer.apple.com/documentation/security/ksecoidorganizationalunitname)Added [kSecOIDPolicyConstraints](https://developer.apple.com/documentation/security/ksecoidpolicyconstraints)Added [kSecOIDPolicyMappings](https://developer.apple.com/documentation/security/ksecoidpolicymappings)Added [kSecOIDPrivateKeyUsagePeriod](https://developer.apple.com/documentation/security/ksecoidprivatekeyusageperiod)Added [kSecOIDQC_Statements](https://developer.apple.com/documentation/security/ksecoidqc_statements)Added [kSecOIDSerialNumber](https://developer.apple.com/documentation/security/ksecoidserialnumber)Added [kSecOIDServerAuth](https://developer.apple.com/documentation/security/ksecoidserverauth)Added [kSecOIDStateProvinceName](https://developer.apple.com/documentation/security/ksecoidstateprovincename)Added [kSecOIDStreetAddress](https://developer.apple.com/documentation/security/ksecoidstreetaddress)Added [kSecOIDSubjectAltName](https://developer.apple.com/documentation/security/ksecoidsubjectaltname)Added [kSecOIDSubjectDirectoryAttributes](https://developer.apple.com/documentation/security/ksecoidsubjectdirectoryattributes)Added [kSecOIDSubjectEmailAddress](https://developer.apple.com/documentation/security/ksecoidsubjectemailaddress)Added [kSecOIDSubjectInfoAccess](https://developer.apple.com/documentation/security/ksecoidsubjectinfoaccess)Added [kSecOIDSubjectKeyIdentifier](https://developer.apple.com/documentation/security/ksecoidsubjectkeyidentifier)Added [kSecOIDSubjectPicture](https://developer.apple.com/documentation/security/ksecoidsubjectpicture)Added [kSecOIDSubjectSignatureBitmap](https://developer.apple.com/documentation/security/ksecoidsubjectsignaturebitmap)Added [kSecOIDSurname](https://developer.apple.com/documentation/security/ksecoidsurname)Added [kSecOIDTimeStamping](https://developer.apple.com/documentation/security/ksecoidtimestamping)Added [kSecOIDTitle](https://developer.apple.com/documentation/security/ksecoidtitle)Added [kSecOIDUseExemptions](https://developer.apple.com/documentation/security/ksecoiduseexemptions)Added [kSecOIDX509V1CertificateIssuerUniqueId](https://developer.apple.com/documentation/security/ksecoidx509v1certificateissueruniqueid)Added [kSecOIDX509V1CertificateSubjectUniqueId](https://developer.apple.com/documentation/security/ksecoidx509v1certificatesubjectuniqueid)Added [kSecOIDX509V1IssuerName](https://developer.apple.com/documentation/security/ksecoidx509v1issuername)Added [kSecOIDX509V1IssuerNameCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1issuernamecstruct)Added [kSecOIDX509V1IssuerNameLDAP](https://developer.apple.com/documentation/security/ksecoidx509v1issuernameldap)Added [kSecOIDX509V1IssuerNameStd](https://developer.apple.com/documentation/security/ksecoidx509v1issuernamestd)Added [kSecOIDX509V1SerialNumber](https://developer.apple.com/documentation/security/ksecoidx509v1serialnumber)Added [kSecOIDX509V1Signature](https://developer.apple.com/documentation/security/ksecoidx509v1signature)Added [kSecOIDX509V1SignatureAlgorithm](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithm)Added [kSecOIDX509V1SignatureAlgorithmParameters](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithmparameters)Added [kSecOIDX509V1SignatureAlgorithmTBS](https://developer.apple.com/documentation/security/ksecoidx509v1signaturealgorithmtbs)Added [kSecOIDX509V1SignatureCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1signaturecstruct)Added [kSecOIDX509V1SignatureStruct](https://developer.apple.com/documentation/security/ksecoidx509v1signaturestruct)Added [kSecOIDX509V1SubjectName](https://developer.apple.com/documentation/security/ksecoidx509v1subjectname)Added [kSecOIDX509V1SubjectNameCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnamecstruct)Added [kSecOIDX509V1SubjectNameLDAP](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnameldap)Added [kSecOIDX509V1SubjectNameStd](https://developer.apple.com/documentation/security/ksecoidx509v1subjectnamestd)Added [kSecOIDX509V1SubjectPublicKey](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickey)Added [kSecOIDX509V1SubjectPublicKeyAlgorithm](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeyalgorithm)Added [kSecOIDX509V1SubjectPublicKeyAlgorithmParameters](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeyalgorithmparameters)Added [kSecOIDX509V1SubjectPublicKeyCStruct](https://developer.apple.com/documentation/security/ksecoidx509v1subjectpublickeycstruct)Added [kSecOIDX509V1ValidityNotAfter](https://developer.apple.com/documentation/security/ksecoidx509v1validitynotafter)Added [kSecOIDX509V1ValidityNotBefore](https://developer.apple.com/documentation/security/ksecoidx509v1validitynotbefore)Added [kSecOIDX509V1Version](https://developer.apple.com/documentation/security/ksecoidx509v1version)Added [kSecOIDX509V3Certificate](https://developer.apple.com/documentation/security/ksecoidx509v3certificate)Added [kSecOIDX509V3CertificateCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificatecstruct)Added [kSecOIDX509V3CertificateExtensionCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensioncstruct)Added [kSecOIDX509V3CertificateExtensionCritical](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensioncritical)Added [kSecOIDX509V3CertificateExtensionId](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionid)Added [kSecOIDX509V3CertificateExtensionStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionstruct)Added [kSecOIDX509V3CertificateExtensionType](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensiontype)Added [kSecOIDX509V3CertificateExtensionValue](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionvalue)Added [kSecOIDX509V3CertificateExtensionsCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionscstruct)Added [kSecOIDX509V3CertificateExtensionsStruct](https://developer.apple.com/documentation/security/ksecoidx509v3certificateextensionsstruct)Added [kSecOIDX509V3CertificateNumberOfExtensions](https://developer.apple.com/documentation/security/ksecoidx509v3certificatenumberofextensions)Added [kSecOIDX509V3SignedCertificate](https://developer.apple.com/documentation/security/ksecoidx509v3signedcertificate)Added [kSecOIDX509V3SignedCertificateCStruct](https://developer.apple.com/documentation/security/ksecoidx509v3signedcertificatecstruct)SecCode.hAdded [kSecCodeInfoDigestAlgorithm](https://developer.apple.com/documentation/security/kseccodeinfodigestalgorithm)SecCustomTransform.hAdded [SecTranformCustomGetAttribute()](https://developer.apple.com/documentation/security/1552632-sectranformcustomgetattribute)Added [SecTransformActionBlock](https://developer.apple.com/documentation/security/sectransformactionblock)Added [SecTransformAttributeActionBlock](https://developer.apple.com/documentation/security/sectransformattributeactionblock)Added [SecTransformAttributeRef](https://developer.apple.com/documentation/security/sectransformattributeref)Added [SecTransformCreate()](https://developer.apple.com/documentation/security/1395256-sectransformcreate)Added [SecTransformCreateFP](https://developer.apple.com/documentation/security/sectransformcreatefp)Added [SecTransformCustomSetAttribute()](https://developer.apple.com/documentation/security/1392556-sectransformcustomsetattribute)Added [SecTransformDataBlock](https://developer.apple.com/documentation/security/sectransformdatablock)Added [SecTransformImplementationRef](https://developer.apple.com/documentation/security/sectransformimplementationref)Added [SecTransformInstanceBlock](https://developer.apple.com/documentation/security/sectransforminstanceblock)Added [SecTransformMetaAttributeType](https://developer.apple.com/documentation/security/sectransformmetaattributetype)Added [SecTransformNoData()](https://developer.apple.com/documentation/security/1393788-sectransformnodata)Added [SecTransformPushbackAttribute()](https://developer.apple.com/documentation/security/1400559-sectransformpushbackattribute)Added [SecTransformRegister()](https://developer.apple.com/documentation/security/1393997-sectransformregister)Added [SecTransformSetAttributeAction()](https://developer.apple.com/documentation/security/1396035-sectransformsetattributeaction)Added [SecTransformSetDataAction()](https://developer.apple.com/documentation/security/1399597-sectransformsetdataaction)Added [SecTransformSetTransformAction()](https://developer.apple.com/documentation/security/1402097-sectransformsettransformaction)Added [SecTransformStringOrAttributeRef](https://developer.apple.com/documentation/security/sectransformstringorattributeref)Added [kSecTransformActionAttributeNotification](https://developer.apple.com/documentation/security/ksectransformactionattributenotification)Added [kSecTransformActionAttributeValidation](https://developer.apple.com/documentation/security/ksectransformactionattributevalidation)Added [kSecTransformActionCanExecute](https://developer.apple.com/documentation/security/ksectransformactioncanexecute)Added [kSecTransformActionExternalizeExtraData](https://developer.apple.com/documentation/security/ksectransformactionexternalizeextradata)Added [kSecTransformActionFinalize](https://developer.apple.com/documentation/security/ksectransformactionfinalize)Added [kSecTransformActionInternalizeExtraData](https://developer.apple.com/documentation/security/ksectransformactioninternalizeextradata)Added [kSecTransformActionProcessData](https://developer.apple.com/documentation/security/ksectransformactionprocessdata)Added [kSecTransformActionStartingExecution](https://developer.apple.com/documentation/security/ksectransformactionstartingexecution)Added [kSecTransformMetaAttributeCanCycle](https://developer.apple.com/documentation/security/sectransformmetaattributetype/cancycle)Added [kSecTransformMetaAttributeDeferred](https://developer.apple.com/documentation/security/sectransformmetaattributetype/deferred)Added [kSecTransformMetaAttributeExternalize](https://developer.apple.com/documentation/security/sectransformmetaattributetype/externalize)Added [kSecTransformMetaAttributeHasInboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributehasinboundconnection)Added [kSecTransformMetaAttributeHasOutboundConnections](https://developer.apple.com/documentation/security/sectransformmetaattributetype/hasoutboundconnections)Added [kSecTransformMetaAttributeName](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributename)Added [kSecTransformMetaAttributeRef](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributeref)Added [kSecTransformMetaAttributeRequired](https://developer.apple.com/documentation/security/sectransformmetaattributetype/required)Added [kSecTransformMetaAttributeRequiresOutboundConnection](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributerequiresoutboundconnection)Added [kSecTransformMetaAttributeStream](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributestream)Added [kSecTransformMetaAttributeValue](https://developer.apple.com/documentation/security/sectransformmetaattributetype/ksectransformmetaattributevalue)SecDecodeTransform.hAdded [SecDecodeTransformCreate()](https://developer.apple.com/documentation/security/1395244-secdecodetransformcreate)Added [kSecDecodeTypeAttribute](https://developer.apple.com/documentation/security/ksecdecodetypeattribute)SecDigestTransform.hAdded [SecDigestTransformCreate()](https://developer.apple.com/documentation/security/1394846-secdigesttransformcreate)Added [SecDigestTransformGetTypeID()](https://developer.apple.com/documentation/security/1395722-secdigesttransformgettypeid)Added [kSecDigestHMACKeyAttribute](https://developer.apple.com/documentation/security/ksecdigesthmackeyattribute)Added [kSecDigestHMACMD5](https://developer.apple.com/documentation/security/ksecdigesthmacmd5)Added [kSecDigestHMACSHA1](https://developer.apple.com/documentation/security/ksecdigesthmacsha1)Added [kSecDigestHMACSHA2](https://developer.apple.com/documentation/security/ksecdigesthmacsha2)Added [kSecDigestLengthAttribute](https://developer.apple.com/documentation/security/ksecdigestlengthattribute)Added [kSecDigestMD2](https://developer.apple.com/documentation/security/ksecdigestmd2)Added [kSecDigestMD4](https://developer.apple.com/documentation/security/ksecdigestmd4)Added [kSecDigestMD5](https://developer.apple.com/documentation/security/ksecdigestmd5)Added [kSecDigestSHA1](https://developer.apple.com/documentation/security/ksecdigestsha1)Added [kSecDigestSHA2](https://developer.apple.com/documentation/security/ksecdigestsha2)Added [kSecDigestTypeAttribute](https://developer.apple.com/documentation/security/ksecdigesttypeattribute)SecEncodeTransform.hAdded [SecEncodeTransformCreate()](https://developer.apple.com/documentation/security/1399382-secencodetransformcreate)Added [kSecBase32Encoding](https://developer.apple.com/documentation/security/ksecbase32encoding)Added [kSecBase64Encoding](https://developer.apple.com/documentation/security/ksecbase64encoding)Added [kSecCompressionRatio](https://developer.apple.com/documentation/security/kseccompressionratio)Added [kSecEncodeLineLengthAttribute](https://developer.apple.com/documentation/security/ksecencodelinelengthattribute)Added [kSecEncodeTypeAttribute](https://developer.apple.com/documentation/security/ksecencodetypeattribute)Added [kSecZLibEncoding](https://developer.apple.com/documentation/security/kseczlibencoding)SecEncryptTransform.hAdded [SecDecryptTransformCreate()](https://developer.apple.com/documentation/security/1399526-secdecrypttransformcreate)Added [SecDecryptTransformGetTypeID()](https://developer.apple.com/documentation/security/1393546-secdecrypttransformgettypeid)Added [SecEncryptTransformCreate()](https://developer.apple.com/documentation/security/1399605-secencrypttransformcreate)Added [SecEncryptTransformGetTypeID()](https://developer.apple.com/documentation/security/1397714-secencrypttransformgettypeid)Added [kSecEncryptKey](https://developer.apple.com/documentation/security/ksecencryptkey)Added [kSecEncryptionMode](https://developer.apple.com/documentation/security/ksecencryptionmode)Added [kSecIVKey](https://developer.apple.com/documentation/security/ksecivkey)Added [kSecModeCBCKey](https://developer.apple.com/documentation/security/ksecmodecbckey)Added [kSecModeCFBKey](https://developer.apple.com/documentation/security/ksecmodecfbkey)Added [kSecModeECBKey](https://developer.apple.com/documentation/security/ksecmodeecbkey)Added [kSecModeNoneKey](https://developer.apple.com/documentation/security/ksecmodenonekey)Added [kSecModeOFBKey](https://developer.apple.com/documentation/security/ksecmodeofbkey)Added [kSecPaddingKey](https://developer.apple.com/documentation/security/ksecpaddingkey)Added [kSecPaddingNoneKey](https://developer.apple.com/documentation/security/ksecpaddingnonekey)Added [kSecPaddingPKCS1Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs1key)Added [kSecPaddingPKCS5Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs5key)Added [kSecPaddingPKCS7Key](https://developer.apple.com/documentation/security/ksecpaddingpkcs7key)SecIdentity.hAdded [SecIdentityCopyPreferred()](https://developer.apple.com/documentation/security/1399556-secidentitycopypreferred)Added [SecIdentitySetPreferred()](https://developer.apple.com/documentation/security/1395862-secidentitysetpreferred)Modified [SecIdentityCopyPreference()](https://developer.apple.com/documentation/security/1543662-secidentitycopypreference)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecIdentitySetPreference()](https://developer.apple.com/documentation/security/1543664-secidentitysetpreference)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecIdentitySearch.hModified [SecIdentitySearchCopyNext()](https://developer.apple.com/documentation/security/1396825-secidentitysearchcopynext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecIdentitySearchGetTypeID()](https://developer.apple.com/documentation/security/1396823-secidentitysearchgettypeid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecIdentitySearchCreate()](https://developer.apple.com/documentation/security/1396821-secidentitysearchcreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecImportExport.hAdded [SecItemExport()](https://developer.apple.com/documentation/security/1394828-secitemexport)Added [SecItemImport()](https://developer.apple.com/documentation/security/1395728-secitemimport)Added [SecItemImportExportKeyParameters](https://developer.apple.com/documentation/security/secitemimportexportkeyparameters)Added [kSecImportExportAccess](https://developer.apple.com/documentation/security/ksecimportexportaccess)Added [kSecImportExportKeychain](https://developer.apple.com/documentation/security/ksecimportexportkeychain)Modified [SecKeychainItemExport()](https://developer.apple.com/documentation/security/1412386-seckeychainitemexport)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeychainItemImport()](https://developer.apple.com/documentation/security/1412415-seckeychainitemimport)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecItem.hAdded [kSecAttrAccess](https://developer.apple.com/documentation/security/ksecattraccess)Added [kSecAttrKeyType3DES](https://developer.apple.com/documentation/security/ksecattrkeytype3des)Added [kSecAttrKeyTypeAES](https://developer.apple.com/documentation/security/ksecattrkeytypeaes)Added [kSecAttrKeyTypeCAST](https://developer.apple.com/documentation/security/ksecattrkeytypecast)Added [kSecAttrKeyTypeDES](https://developer.apple.com/documentation/security/ksecattrkeytypedes)Added [kSecAttrKeyTypeDSA](https://developer.apple.com/documentation/security/ksecattrkeytypedsa)Added [kSecAttrKeyTypeECDSA](https://developer.apple.com/documentation/security/ksecattrkeytypeecdsa)Added [kSecAttrKeyTypeRC2](https://developer.apple.com/documentation/security/ksecattrkeytyperc2)Added [kSecAttrKeyTypeRC4](https://developer.apple.com/documentation/security/ksecattrkeytyperc4)Added [kSecAttrPRF](https://developer.apple.com/documentation/security/ksecattrprf)Added [kSecAttrPRFHmacAlgSHA1](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha1)Added [kSecAttrPRFHmacAlgSHA224](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha224)Added [kSecAttrPRFHmacAlgSHA256](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha256)Added [kSecAttrPRFHmacAlgSHA384](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha384)Added [kSecAttrPRFHmacAlgSHA512](https://developer.apple.com/documentation/security/ksecattrprfhmacalgsha512)Added [kSecAttrRounds](https://developer.apple.com/documentation/security/ksecattrrounds)Added [kSecAttrSalt](https://developer.apple.com/documentation/security/ksecattrsalt)Added [kSecClassCertificate](https://developer.apple.com/documentation/security/ksecclasscertificate)Added [kSecClassGenericPassword](https://developer.apple.com/documentation/security/ksecclassgenericpassword)Added [kSecClassIdentity](https://developer.apple.com/documentation/security/ksecclassidentity)Added [kSecClassKey](https://developer.apple.com/documentation/security/ksecclasskey)Added [kSecMatchDiacriticInsensitive](https://developer.apple.com/documentation/security/ksecmatchdiacriticinsensitive)Added [kSecMatchSubjectEndsWith](https://developer.apple.com/documentation/security/ksecmatchsubjectendswith)Added [kSecMatchSubjectStartsWith](https://developer.apple.com/documentation/security/ksecmatchsubjectstartswith)Added [kSecMatchSubjectWholeString](https://developer.apple.com/documentation/security/ksecmatchsubjectwholestring)Added [kSecMatchWidthInsensitive](https://developer.apple.com/documentation/security/ksecmatchwidthinsensitive)Added [kSecUseKeychain](https://developer.apple.com/documentation/security/ksecusekeychain)SecKey.hAdded [SecKeyCreateFromData()](https://developer.apple.com/documentation/security/1393853-seckeycreatefromdata)Added [SecKeyDeriveFromPassword()](https://developer.apple.com/documentation/security/1395028-seckeyderivefrompassword)Added [SecKeyGeneratePair()](https://developer.apple.com/documentation/security/1395339-seckeygeneratepair)Added [SecKeyGeneratePairAsync()](https://developer.apple.com/documentation/security/1394698-seckeygeneratepairasync)Added [SecKeyGeneratePairBlock](https://developer.apple.com/documentation/security/seckeygeneratepairblock)Added [SecKeyGenerateSymmetric()](https://developer.apple.com/documentation/security/1401861-seckeygeneratesymmetric)Added [SecKeySizes](https://developer.apple.com/documentation/security/seckeysizes)Added [SecKeyUnwrapSymmetric()](https://developer.apple.com/documentation/security/1394725-seckeyunwrapsymmetric)Added [SecKeyWrapSymmetric()](https://developer.apple.com/documentation/security/1396734-seckeywrapsymmetric)Added [kSec3DES192](https://developer.apple.com/documentation/security/seckeysizes/sec3des192)Added [kSecAES128](https://developer.apple.com/documentation/security/seckeysizes/secaes128)Added [kSecAES192](https://developer.apple.com/documentation/security/seckeysizes/ksecaes192)Added [kSecAES256](https://developer.apple.com/documentation/security/seckeysizes/secaes256)Added [kSecDefaultKeySize](https://developer.apple.com/documentation/security/seckeysizes/secdefaultkeysize)Added [kSecRSAMax](https://developer.apple.com/documentation/security/seckeysizes/ksecrsamax)Added [kSecRSAMin](https://developer.apple.com/documentation/security/seckeysizes/ksecrsamin)Added [kSecp192r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp192r1)Added [kSecp256r1](https://developer.apple.com/documentation/security/seckeysizes/1398756-secp256r1)Added [kSecp384r1](https://developer.apple.com/documentation/security/seckeysizes/ksecp384r1)Added [kSecp521r1](https://developer.apple.com/documentation/security/seckeysizes/secp521r1)Modified [SecKeyGetCredentials()](https://developer.apple.com/documentation/security/1495756-seckeygetcredentials)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeyGetCSPHandle()](https://developer.apple.com/documentation/security/1495747-seckeygetcsphandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeyCreatePair()](https://developer.apple.com/documentation/security/1495765-seckeycreatepair)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeyGenerate()](https://developer.apple.com/documentation/security/1495754-seckeygenerate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeyGetCSSMKey()](https://developer.apple.com/documentation/security/1495763-seckeygetcssmkey)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecKeychain.hModified [SecKeychainGetDLDBHandle()](https://developer.apple.com/documentation/security/1536077-seckeychaingetdldbhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeychainGetCSPHandle()](https://developer.apple.com/documentation/security/1536084-seckeychaingetcsphandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecKeychainItem.hModified [SecKeychainItemGetUniqueRecordID()](https://developer.apple.com/documentation/security/1415615-seckeychainitemgetuniquerecordid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeychainItemGetDLDBHandle()](https://developer.apple.com/documentation/security/1415616-seckeychainitemgetdldbhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecKeychainSearch.hModified [SecKeychainSearchCreateFromAttributes()](https://developer.apple.com/documentation/security/1515366-seckeychainsearchcreatefromattri)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeychainSearchCopyNext()](https://developer.apple.com/documentation/security/1515362-seckeychainsearchcopynext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecKeychainSearchGetTypeID()](https://developer.apple.com/documentation/security/1515364-seckeychainsearchgettypeid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecPolicy.hAdded [SecPolicyCopyProperties()](https://developer.apple.com/documentation/security/1401915-secpolicycopyproperties)Added [SecPolicyCreateWithOID()](https://developer.apple.com/documentation/security/1563598-secpolicycreatewithoid)Added [SecPolicySetProperties()](https://developer.apple.com/documentation/security/1563596-secpolicysetproperties)Added [kSecPolicyAppleCodeSigning](https://developer.apple.com/documentation/security/ksecpolicyapplecodesigning)Added [kSecPolicyAppleEAP](https://developer.apple.com/documentation/security/ksecpolicyappleeap)Added [kSecPolicyAppleIDValidation](https://developer.apple.com/documentation/security/ksecpolicyappleidvalidation)Added [kSecPolicyAppleIPsec](https://developer.apple.com/documentation/security/ksecpolicyappleipsec)Added [kSecPolicyApplePKINITClient](https://developer.apple.com/documentation/security/ksecpolicyapplepkinitclient)Added [kSecPolicyApplePKINITServer](https://developer.apple.com/documentation/security/ksecpolicyapplepkinitserver)Added [kSecPolicyAppleSMIME](https://developer.apple.com/documentation/security/ksecpolicyapplesmime)Added [kSecPolicyAppleSSL](https://developer.apple.com/documentation/security/ksecpolicyapplessl)Added [kSecPolicyAppleX509Basic](https://developer.apple.com/documentation/security/ksecpolicyapplex509basic)Added [kSecPolicyAppleiChat](https://developer.apple.com/documentation/security/ksecpolicyappleichat)Added [kSecPolicyClient](https://developer.apple.com/documentation/security/ksecpolicyclient)Added [kSecPolicyKU_CRLSign](https://developer.apple.com/documentation/security/ksecpolicyku_crlsign)Added [kSecPolicyKU_DataEncipherment](https://developer.apple.com/documentation/security/ksecpolicyku_dataencipherment)Added [kSecPolicyKU_DecipherOnly](https://developer.apple.com/documentation/security/ksecpolicyku_decipheronly)Added [kSecPolicyKU_DigitalSignature](https://developer.apple.com/documentation/security/ksecpolicyku_digitalsignature)Added [kSecPolicyKU_EncipherOnly](https://developer.apple.com/documentation/security/ksecpolicyku_encipheronly)Added [kSecPolicyKU_KeyAgreement](https://developer.apple.com/documentation/security/ksecpolicyku_keyagreement)Added [kSecPolicyKU_KeyCertSign](https://developer.apple.com/documentation/security/ksecpolicyku_keycertsign)Added [kSecPolicyKU_KeyEncipherment](https://developer.apple.com/documentation/security/ksecpolicyku_keyencipherment)Added [kSecPolicyKU_NonRepudiation](https://developer.apple.com/documentation/security/ksecpolicyku_nonrepudiation)Added [kSecPolicyMacAppStoreReceipt](https://developer.apple.com/documentation/security/ksecpolicymacappstorereceipt)Added [kSecPolicyName](https://developer.apple.com/documentation/security/ksecpolicyname)Added [kSecPolicyOid](https://developer.apple.com/documentation/security/ksecpolicyoid)Modified [SecPolicyGetTPHandle()](https://developer.apple.com/documentation/security/1563593-secpolicygettphandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecPolicyGetValue()](https://developer.apple.com/documentation/security/1563595-secpolicygetvalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecPolicyGetOID()](https://developer.apple.com/documentation/security/1563594-secpolicygetoid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecPolicySetValue()](https://developer.apple.com/documentation/security/1563597-secpolicysetvalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecPolicySearch.hModified [SecPolicySearchCopyNext()](https://developer.apple.com/documentation/security/1562856-secpolicysearchcopynext)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecPolicySearchCreate()](https://developer.apple.com/documentation/security/1562858-secpolicysearchcreate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecPolicySearchGetTypeID()](https://developer.apple.com/documentation/security/1562857-secpolicysearchgettypeid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

SecRandom.hAdded [SecRandomCopyBytes()](https://developer.apple.com/documentation/security/1399291-secrandomcopybytes)Added [SecRandomRef](https://developer.apple.com/documentation/security/secrandomref)Added [kSecRandomDefault](https://developer.apple.com/documentation/security/ksecrandomdefault)SecSignVerifyTransform.hAdded [SecSignTransformCreate()](https://developer.apple.com/documentation/security/1398780-secsigntransformcreate)Added [SecVerifyTransformCreate()](https://developer.apple.com/documentation/security/1393414-secverifytransformcreate)Added [kSecInputIsAttributeName](https://developer.apple.com/documentation/security/ksecinputisattributename)Added [kSecInputIsDigest](https://developer.apple.com/documentation/security/ksecinputisdigest)Added [kSecInputIsPlainText](https://developer.apple.com/documentation/security/ksecinputisplaintext)Added [kSecInputIsRaw](https://developer.apple.com/documentation/security/ksecinputisraw)Added [kSecKeyAttributeName](https://developer.apple.com/documentation/security/kseckeyattributename)Added [kSecSignatureAttributeName](https://developer.apple.com/documentation/security/ksecsignatureattributename)SecStaticCode.hAdded [SecStaticCodeCreateWithPathAndAttributes()](https://developer.apple.com/documentation/security/1394237-secstaticcodecreatewithpathandat)Added [kSecCodeAttributeArchitecture](https://developer.apple.com/documentation/security/kseccodeattributearchitecture)Added [kSecCodeAttributeBundleVersion](https://developer.apple.com/documentation/security/kseccodeattributebundleversion)Added [kSecCodeAttributeSubarchitecture](https://developer.apple.com/documentation/security/kseccodeattributesubarchitecture)SecTask.hAdded [SecTaskCopyValueForEntitlement()](https://developer.apple.com/documentation/security/1393461-sectaskcopyvalueforentitlement)Added [SecTaskCopyValuesForEntitlements()](https://developer.apple.com/documentation/security/1397627-sectaskcopyvaluesforentitlements)Added [SecTaskCreateWithAuditToken()](https://developer.apple.com/documentation/security/1401168-sectaskcreatewithaudittoken)Added [SecTaskGetTypeID()](https://developer.apple.com/documentation/security/1400359-sectaskgettypeid)Added [SecTaskRef](https://developer.apple.com/documentation/security/sectaskref)SecTransform.hAdded [SecGroupTransformGetTypeID()](https://developer.apple.com/documentation/security/1399067-secgrouptransformgettypeid)Added [SecGroupTransformRef](https://developer.apple.com/documentation/security/secgrouptransform)Added [SecMessageBlock](https://developer.apple.com/documentation/security/secmessageblock)Added [SecTransformConnectTransforms()](https://developer.apple.com/documentation/security/1401298-sectransformconnecttransforms)Added [SecTransformCopyExternalRepresentation()](https://developer.apple.com/documentation/security/1397283-sectransformcopyexternalrepresen)Added [SecTransformCreateFromExternalRepresentation()](https://developer.apple.com/documentation/security/1397563-sectransformcreatefromexternalre)Added [SecTransformCreateGroupTransform()](https://developer.apple.com/documentation/security/1400301-sectransformcreategrouptransform)Added [SecTransformExecute()](https://developer.apple.com/documentation/security/1395776-sectransformexecute)Added [SecTransformExecuteAsync()](https://developer.apple.com/documentation/security/1397425-sectransformexecuteasync)Added [SecTransformFindByName()](https://developer.apple.com/documentation/security/1401448-sectransformfindbyname)Added [SecTransformGetAttribute()](https://developer.apple.com/documentation/security/1398748-sectransformgetattribute)Added [SecTransformGetTypeID()](https://developer.apple.com/documentation/security/1397963-sectransformgettypeid)Added [SecTransformRef](https://developer.apple.com/documentation/security/sectransformref)Added [SecTransformSetAttribute()](https://developer.apple.com/documentation/security/1393861-sectransformsetattribute)Added [kSecTransformAbortAttributeName](https://developer.apple.com/documentation/security/ksectransformabortattributename)Added [kSecTransformAbortOriginatorKey](https://developer.apple.com/documentation/security/ksectransformabortoriginatorkey)Added [kSecTransformDebugAttributeName](https://developer.apple.com/documentation/security/ksectransformdebugattributename)Added [kSecTransformErrorAbortInProgress](https://developer.apple.com/documentation/security/ksectransformerrorabortinprogress)Added [kSecTransformErrorAborted](https://developer.apple.com/documentation/security/ksectransformerroraborted)Added [kSecTransformErrorAttributeNotFound](https://developer.apple.com/documentation/security/ksectransformerrorattributenotfound)Added [kSecTransformErrorDomain](https://developer.apple.com/documentation/security/ksectransformerrordomain)Added [kSecTransformErrorInvalidAlgorithm](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidalgorithm)Added [kSecTransformErrorInvalidConnection](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidconnection)Added [kSecTransformErrorInvalidInput](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidinput)Added [kSecTransformErrorInvalidInputDictionary](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidinputdictionary)Added [kSecTransformErrorInvalidLength](https://developer.apple.com/documentation/security/ksectransformerrorinvalidlength)Added [kSecTransformErrorInvalidOperation](https://developer.apple.com/documentation/security/1573760-security_transform_error_codes/ksectransformerrorinvalidoperation)Added [kSecTransformErrorInvalidType](https://developer.apple.com/documentation/security/ksectransformerrorinvalidtype)Added [kSecTransformErrorMissingParameter](https://developer.apple.com/documentation/security/ksectransformerrormissingparameter)Added [kSecTransformErrorMoreThanOneOutput](https://developer.apple.com/documentation/security/ksectransformerrormorethanoneoutput)Added [kSecTransformErrorNameAlreadyRegistered](https://developer.apple.com/documentation/security/ksectransformerrornamealreadyregistered)Added [kSecTransformErrorNotInitializedCorrectly](https://developer.apple.com/documentation/security/ksectransformerrornotinitializedcorrectly)Added [kSecTransformErrorUnsupportedAttribute](https://developer.apple.com/documentation/security/ksectransformerrorunsupportedattribute)Added [kSecTransformInputAttributeName](https://developer.apple.com/documentation/security/ksectransforminputattributename)Added [kSecTransformInvalidArgument](https://developer.apple.com/documentation/security/ksectransforminvalidargument)Added [kSecTransformInvalidOverride](https://developer.apple.com/documentation/security/ksectransforminvalidoverride)Added [kSecTransformOperationNotSupportedOnGroup](https://developer.apple.com/documentation/security/ksectransformoperationnotsupportedongroup)Added [kSecTransformOutputAttributeName](https://developer.apple.com/documentation/security/ksectransformoutputattributename)Added [kSecTransformPreviousErrorKey](https://developer.apple.com/documentation/security/ksectransformpreviouserrorkey)Added [kSecTransformTransformIsExecuting](https://developer.apple.com/documentation/security/ksectransformtransformisexecuting)Added [kSecTransformTransformIsNotRegistered](https://developer.apple.com/documentation/security/ksectransformtransformisnotregistered)Added [kSecTransformTransformName](https://developer.apple.com/documentation/security/ksectransformtransformname)SecTransformReadTransform.hAdded [SecTransformCreateReadTransformWithReadStream()](https://developer.apple.com/documentation/security/1394302-sectransformcreatereadtransformw)SecTrust.hRemoved [SecTrustGetCSSMAnchorCertificates()](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/trust/1805368-sectrustgetcssmanchorcertificate)Removed [SecTrustGetUserTrust()](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/trust/1805379-sectrustgetusertrust)Removed [SecTrustSetUserTrust()](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/trust/1805395-sectrustsetusertrust)Added [SecTrustCallback](https://developer.apple.com/documentation/security/sectrustcallback)Added [SecTrustCopyProperties()](https://developer.apple.com/documentation/security/1401567-sectrustcopyproperties)Added [SecTrustCopyPublicKey()](https://developer.apple.com/documentation/security/1396135-sectrustcopypublickey)Added [SecTrustEvaluateAsync()](https://developer.apple.com/documentation/security/1400632-sectrustevaluateasync)Added [SecTrustGetCertificateAtIndex()](https://developer.apple.com/documentation/security/1395987-sectrustgetcertificateatindex)Added [SecTrustGetCertificateCount()](https://developer.apple.com/documentation/security/1397024-sectrustgetcertificatecount)Added [SecTrustGetTrustResult()](https://developer.apple.com/documentation/security/1396077-sectrustgettrustresult)Added [SecTrustOptionFlags](https://developer.apple.com/documentation/security/sectrustoptionflags)Added [SecTrustSetOptions()](https://developer.apple.com/documentation/security/1392875-sectrustsetoptions)Added [kSecPropertyTypeError](https://developer.apple.com/documentation/security/ksecpropertytypeerror)Added [kSecPropertyTypeTitle](https://developer.apple.com/documentation/security/ksecpropertytypetitle)Added [kSecTrustOptionAllowExpired](https://developer.apple.com/documentation/security/sectrustoptionflags/1396581-allowexpired)Added [kSecTrustOptionAllowExpiredRoot](https://developer.apple.com/documentation/security/sectrustoptionflags/1401432-allowexpiredroot)Added [kSecTrustOptionFetchIssuerFromNet](https://developer.apple.com/documentation/security/sectrustoptionflags/ksectrustoptionfetchissuerfromnet)Added [kSecTrustOptionImplicitAnchors](https://developer.apple.com/documentation/security/sectrustoptionflags/1400933-implicitanchors)Added [kSecTrustOptionLeafIsCA](https://developer.apple.com/documentation/security/sectrustoptionflags/1397419-leafisca)Added [kSecTrustOptionRequireRevPerCert](https://developer.apple.com/documentation/security/sectrustoptionflags/1395313-requirerevpercert)Added [kSecTrustOptionUseTrustSettings](https://developer.apple.com/documentation/security/sectrustoptionflags/ksectrustoptionusetrustsettings)Modified [SecTrustSetParameters()](https://developer.apple.com/documentation/security/1524326-sectrustsetparameters)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecTrustGetTPHandle()](https://developer.apple.com/documentation/security/1524309-sectrustgettphandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecTrustGetCssmResult()](https://developer.apple.com/documentation/security/1524311-sectrustgetcssmresult)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecTrustGetCssmResultCode()](https://developer.apple.com/documentation/security/1524327-sectrustgetcssmresultcode)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [SecTrustGetResult()](https://developer.apple.com/documentation/security/1524331-sectrustgetresult)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

certextensions.hAdded [CE_GeneralSubtree](https://developer.apple.com/documentation/security/ce_generalsubtree)Added [CE_GeneralSubtrees](https://developer.apple.com/documentation/security/ce_generalsubtrees)Added [CE_InhibitAnyPolicy](https://developer.apple.com/documentation/security/ce_inhibitanypolicy)Added [CE_NameConstraints](https://developer.apple.com/documentation/security/ce_nameconstraints)Added [CE_PolicyConstraints](https://developer.apple.com/documentation/security/ce_policyconstraints)Added [CE_PolicyMapping](https://developer.apple.com/documentation/security/ce_policymapping)Added [CE_PolicyMappings](https://developer.apple.com/documentation/security/ce_policymappings)Added [DT_InhibitAnyPolicy](https://developer.apple.com/documentation/security/ce_datatype/dt_inhibitanypolicy)Added [DT_NameConstraints](https://developer.apple.com/documentation/security/dt_nameconstraints)Added [DT_PolicyConstraints](https://developer.apple.com/documentation/security/ce_datatype/dt_policyconstraints)Added [DT_PolicyMappings](https://developer.apple.com/documentation/security/dt_policymappings)Modified [CE_SubjectKeyID](https://developer.apple.com/documentation/security/ce_subjectkeyid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CE_NetscapeCertType](https://developer.apple.com/documentation/security/ce_netscapecerttype)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CE_CrlDistReasonFlags](https://developer.apple.com/documentation/security/ce_crldistreasonflags)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CE_NameRegistrationAuthorities](https://developer.apple.com/documentation/security/ce_nameregistrationauthorities)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CE_CrlReason](https://developer.apple.com/documentation/security/ce_crlreason)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [CE_KeyUsage](https://developer.apple.com/documentation/security/ce_keyusage)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmaci.hModified CSSM_SPI_AC_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmapi.hModified CSSM_VerifyDevice()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ChangeKeyOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlAbortQuery()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DigestDataFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertGroupConstruct()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_Unintroduce()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateKeyP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_CreateRelation()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_FreeContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_TupleGroupToCertGroup()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertVerify()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyMacInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertAbortQuery()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_RetrieveCredResult()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateMacContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptDataFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_FormSubmit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertReclaimKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataInsert()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DbCreate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_GetDbAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_IsCertInCachedCrl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DeleteContextAttributes()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataAbortQuery()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SignDataFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlSign()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptDataFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_Introduce()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetAllFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_FreeUniqueRecord()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_RetrieveCounter()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_FreeFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateKeyPair()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DbDelete()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SignData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DbClose()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_FormRequest()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_ChangeDbAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyMac()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_Login()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlVerify()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DigestDataClone()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataGetFromUniqueRecordId()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertGetAllTemplateFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateDigestContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateKeyPairP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateAsymmetricContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertSign()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetFirstCachedFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_ChangeLoginOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DigestDataUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetFirstFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_QueryKeySizeInBits()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateMac()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetKeyAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CrlSign()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ModuleDetach()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DeleteContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_ApplyCrlToDb()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertGroupPrune()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateAlgorithmParams()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_Logout()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertDescribeFormat()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DbOpen()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_ConfirmCredResult()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_GetDbOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DeriveKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyMacUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataDelete()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ModuleAttach()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateRandom()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateRandomGenContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertSign()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptDataUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetKeyInfo()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_FreeKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DigestDataInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGroupFromVerifiedBundle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_GetLoginAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertRevoke()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertGroupToTupleGroup()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_ChangeDbOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertReclaimAbort()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UnwrapKeyP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_ReceiveConfirmation()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetNextFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlDescribeFormat()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_WrapKeyP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptDataInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptDataP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertCreateTemplate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataModify()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetModuleGUIDFromHandle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_AC_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlSetFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetTimeValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetNextFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_ChangeLoginAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_QuerySize()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SignDataUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptDataInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_Init()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DigestData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_ObtainPrivateKeyFromPublicKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertRemoveFromCrlTemplate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_FreeFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetNextCachedFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateMacInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlCreateTemplate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptDataInitP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_GetDbNames()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetPrivilege()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetFirstCachedFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateDeriveKeyContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SetContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlAbortCache()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SignDataInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertCreateTemplate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlRemoveCert()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetAllTemplateFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_GetOperationalStatistics()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateKeyGenContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetKeyOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyMacFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataGetFirst()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SetPrivilege()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyDataFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptDataUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_WrapKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptDataInitP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetFirstFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CrlVerify()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DestroyRelation()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CrlCreateTemplate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ListAttachedModuleManagers()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateMacFinal()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlVerifyWithKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UpdateContextAttributes()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DataGetNext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetAllCachedRecordFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateSignatureContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_Terminate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ModuleUnload()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DecryptDataP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_GetDbNameFromHandle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyDataUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGroupToSignedBundle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlGetNextCachedFieldValue()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertVerifyWithKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UnwrapKey()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlAddCert()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetSubserviceUIDFromHandle()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreateSymmetricContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ChangeKeyAcl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_AC_AuthCompute()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ModuleLoad()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetAPIMemoryFunctions()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_IsCertInCrl()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CertGroupVerify()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_CreatePassThroughContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_FreeNameList()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_Authenticate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GenerateMacUpdate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_SubmitCredRequest()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GetContextAttribute()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertAbortCache()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_RetrieveUniqueId()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertCache()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CertGetAllFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EncryptData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VerifyDataInit()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_GetLoginOwner()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CL_CrlCache()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmapple.hAdded CSSMERR_APPLETP_MISSING_REQUIRED_EXTENSIONcssmcli.hModified CSSM_SPI_CL_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmcspi.hModified CSSM_SPI_CSP_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmdli.hModified CSSM_SPI_DL_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmkrapi.hModified CSSM_KR_QueryPolicyInfo()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_POLICY_LIST_ITEM_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_RegistrationRequest()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_CreateRecoveryRegistrationContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_RecoveryRequestAbort()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_SetEnterpriseRecoveryPolicy()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_GenerateRecoveryFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_PassThrough()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_RecoveryRequest()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_CreateRecoveryEnablementContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_RegistrationRetrieve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_GetPolicyInfo()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_WRAPPEDPRODUCT_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_POLICY_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_GetRecoveredObject()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_CreateRecoveryRequestContext()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_ProcessRecoveryFields()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_RecoveryRetrieve()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KR_PROFILE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmkrspi.hModified CSSM_SPI_KR_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmspi.hModified CSSM_UPCALLS_CALLOC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SPI_ModuleDetach()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_MODULE_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SPI_ModuleUnload()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UPCALLS_REALLOC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UPCALLS_FREE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified memblock

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UPCALLS_MALLOC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SPI_ModuleAttach()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_UPCALLS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SPI_ModuleLoad()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmtpi.hModified CSSM_SPI_TP_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

cssmtype.hModified CSSM_TP_CERTRECLAIM_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SELECTION_PREDICATE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_BASE_CERTS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTISSUE_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_VERSION_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DB_LIST_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_PKCS5_PBKDF2_PARAMS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_INDEX_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_NAME_LIST_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TUPLEGROUP_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_AUTHORIZATIONGROUP_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_PARSED_CERT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DL_DB_HANDLE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KEY_SIZE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_ENTRY_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_UNIQUE_RECORD_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_PKCS5_PBKDF1_PARAMS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_RECORD_ATTRIBUTE_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_QUERY_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CRLISSUE_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ENCODED_CRL_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_ENTRY_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_VERIFY_CONTEXT_RESULT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TUPLE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CERT_BUNDLE_HEADER_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_GUID_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_VERIFY_CONTEXT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SAMPLEGROUP_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_ATTRIBUTE_DATA_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_RANGE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTISSUE_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_POLICYINFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_RECORD_INDEX_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_SCHEMA_INDEX_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CSP_OPERATIONAL_STATISTICS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KEY_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_LIST_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_PARSING_MODULE_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_FUNC_NAME_ADDR_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SUBSERVICE_UID_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_FIELDGROUP_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_QUERY_SIZE_DATA_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACCESS_CREDENTIALS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTRECLAIM_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CRYPTO_DATA_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_SCHEMA_ATTRIBUTE_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CRL_PAIR_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CERT_BUNDLE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTCHANGE_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DBINFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_FIELD_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_SAMPLE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KEYHEADER_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_RESULT_SET_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_NET_ADDRESS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTNOTARIZE_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_OWNER_PROTOTYPE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_AUTHORITY_ID_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_EDIT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_QUERY_LIMITS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CONFIRM_RESPONSE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTCHANGE_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CERT_PAIR_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_VALIDITY_PERIOD_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_EVIDENCE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CALLERAUTH_CONTEXT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DB_RECORD_ATTRIBUTE_DATA_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_RESOURCE_CONTROL_CONTEXT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTVERIFY_INPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CRLISSUE_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_REQUEST_SET_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_PKCS1_OAEP_PARAMS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DATE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ENCODED_CERT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTNOTARIZE_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_PARSED_CRL_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_DATA_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_TP_CERTVERIFY_OUTPUT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_MEMORY_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_ACL_ENTRY_PROTOTYPE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_CONTEXT_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_KEA_DERIVE_PARAMS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

emmspi.hModified CSSM_MANAGER_REGISTRATION_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_STATE_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified ModuleManagerAuthenticate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

emmtype.hModified CSSM_MANAGER_EVENT_NOTIFICATION_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

mds.hModified MDS_Terminate()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MDS_FUNCS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MDS_Install()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MDS_Initialize()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified MDS_Uninstall()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

oidsalg.hAdded CSSMOID_APPLE_TP_APPLEID_SHARINGAdded CSSMOID_APPLE_TP_MACAPPSTORE_RECEIPTModified CSSMOID_APPLE_TP_SMIME

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbeWithSHAAnd3Key3DESCBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA256

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_LOCAL_CERT_GEN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_STORE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA384WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_ENCRYPT_ALG

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_STATIC_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_SSL

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_ICHAT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_RC5_CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithMD5AndDES

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_MQV2_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_MQV1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_EAP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_MQV1_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA512WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_SW_UPDATE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_FETCH

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSHA224

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithMD5AndRC2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithSHA1AndDES

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_HMAC_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_MQV2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_X509_BASIC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_LIST

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_HYBRID2_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_REVOCATION_CRL

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_FEE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1WithDSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_PUB_NUMBER

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA384

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_RSAWithOAEP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSpecified

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_CODE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_ARCHIVE_REMOVE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_ONE_FLOW

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbeWithSHAAnd2Key3DESCBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_RESOURCE_SIGN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_ASC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DSA_CMS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithMD2AndDES

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD5WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA512

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_HYBRID1_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithMD2AndRC2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_ONE_FLOW_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_USERNAME

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_FEE_MD5

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_PACKAGE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_DES_EDE3_CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD4

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_STATIC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_CSR_GEN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ecPublicKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_PBMAC1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_PBES2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_PKINIT_CLIENT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD5

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSHA384

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_FEE_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1WithDSA_JDK

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_HOSTNAME

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_PASSWORD

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_HYBRID1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OAEP_MGF1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbewithSHAAnd40BitRC2CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_RSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_CODE_SIGN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_IDENTITY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1WithDSA_CMS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSHA256

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_PKINIT_SERVER

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_RC2_CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_SHARED_SERVICES

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_EPHEM_SHA1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_EPHEM

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DSA_JDK

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA1WithRSA_OIW

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbeWithSHAAnd128BitRC2CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_FEED

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OAEP_ID_PSPECIFIED

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_FEEDEXP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_EMAIL_SIGN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_HYBRID_ONEFLOW

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_pbeWithSHA1AndRC2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD2WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbeWithSHAAnd40BitRC4

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DES_CBC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA224WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DH

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_EMAIL_ENCRYPT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_RENEW

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ECDSA_WithSHA512

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_IS_PENDING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_ISIGN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_DIGEST_ALG

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_REVOCATION_OCSP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MD4WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_ECDSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ANSI_DH_HYBRID2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS5_PBKDF2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_TP_IP_SEC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA224

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_pbeWithSHAAnd128BitRC4

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS3

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_REQ_VALUE_ASYNC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SHA256WithRSA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

oidsattr.hModified CSSMOID_ExtendedCertificateAttributes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AD_TIME_STAMPING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_RoleOccupant

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UserPassword

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SerialNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PDA_COUNTRY_RESIDENCE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect283r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_FacsimileTelephoneNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ETSI_QCS_QC_RETENTION

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CommonName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_keyBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveFacsimileTelephoneNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp112r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect233r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_CrlTypes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect113r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_StateProvinceName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectivePostalAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KERBv5_PKINIT_AUTH_DATA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PDA_COUNTRY_CITIZEN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_QT_CPS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OID_QCS_SYNTAX_V1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UniqueMember

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ETSI_QCS_QC_SSCD

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_PubKeyType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_CertTypes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_TelexNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect239k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UnstructuredAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AuthorityRevocationList

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectivePostalCode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AD_CA_REPOSITORY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect233k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_EnhancedSearchGuide

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KERBv5_PKINIT_DH_KEY_DATA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DestinationIndicator

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect131r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_FieldType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_SignedData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CountryName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveStateProvinceName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_X509Crl

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PostalAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PresentationAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect113r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AD_OCSP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Member

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X_121Address

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_GenerationQualifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_TelexTerminalIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectivePostOfficeBox

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UserID

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PDA_GENDER

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_BusinessCategory

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_PrimeCurve

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PDA_PLACE_OF_BIRTH

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_LocalityName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SearchGuide

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveOrganizationName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Name

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp160r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp192r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp128r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_LocalKeyId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_StreetAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AD_CA_ISSUERS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect409k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UserCertificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SeeAlso

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_InternationalISDNNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_SdsiCertificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_C_TwoCurve

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect163r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_X509Certificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_DigestedData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_QT_UNOTICE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_EllCurve

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp224r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OrganizationName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp384r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_GivenName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect193r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp256r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveTelexTerminalIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp112r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS9_FriendlyName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DistinguishedName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CrossCertificatePair

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_RegisteredAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_HouseIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveStreetAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect193r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_EncryptedPrivateKeyInfo

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_shroudedKeyBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_EnvelopedData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveTelephoneNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Description

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DNQualifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_safeContentsBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect131r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect163r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_EmailAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CerticomEllCurve

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Owner

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SigningTime

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect163k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectivePhysicalDeliveryOfficeName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Initials

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_DataWithAttributes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Certicom

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect571k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_EncryptedData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect571r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PostOfficeBox

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_secretBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Title

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MessageDigest

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PDA_DATE_OF_BIRTH

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PostalCode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_Data

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveTelexNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_crlBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect283k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X9_62_SigType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ChallengePassword

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_TelephoneNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SupportedApplicationContext

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OID_QCS_SYNTAX_V2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KnowledgeInformation

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CACertificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp160k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp256k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AliasedEntryName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ContentType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp521r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveOrganizationalUnitName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DomainComponent

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PreferredDeliveryMethod

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ProtocolInformation

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS7_SignedAndEnvelopedData

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ETSI_QCS_QC_LIMIT_VALUE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OrganizationalUnitName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CertificateRevocationList

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PhysicalDeliveryOfficeName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp192k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp224k1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_sect409r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp160r2

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KERBv5_PKINIT_RKEY_DATA

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UniqueIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_Surname

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ETSI_QCS_QC_COMPLIANCE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UnstructuredName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKCS12_certBag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CounterSignature

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ObjectClass

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_secp128r1

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CollectiveInternationalISDNNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

oidsbase.hAdded #def APPLE_CERT_POLICIES_APPLEIDAdded #def APPLE_CERT_POLICIES_APPLEID_LENGTHAdded #def APPLE_CERT_POLICIES_APPLEID_SHARINGAdded #def APPLE_CERT_POLICIES_APPLEID_SHARING_LENGTHAdded #def APPLE_CERT_POLICIES_MACAPPSTOREAdded #def APPLE_CERT_POLICIES_MACAPPSTORE_LENGTHAdded #def APPLE_CERT_POLICIES_MACAPPSTORE_RECEIPTAdded #def APPLE_CERT_POLICIES_MACAPPSTORE_RECEIPT_LENGTHAdded #def APPLE_EXTENSION_AAI_INTERMEDIATEAdded #def APPLE_EXTENSION_AAI_INTERMEDIATE_LENGTHAdded #def APPLE_EXTENSION_APPLEID_SHARINGAdded #def APPLE_EXTENSION_APPLEID_SHARING_LENGTHAdded #def APPLE_EXTENSION_INTERMEDIATE_MARKERAdded #def APPLE_EXTENSION_INTERMEDIATE_MARKER_LENGTHAdded #def APPLE_EXTENSION_ITMS_INTERMEDIATEAdded #def APPLE_EXTENSION_ITMS_INTERMEDIATE_LENGTHAdded #def APPLE_EXTENSION_MACAPPSTORE_RECEIPTAdded #def APPLE_EXTENSION_MACAPPSTORE_RECEIPT_LENGTHAdded #def APPLE_EXTENSION_WWDR_INTERMEDIATEAdded #def APPLE_EXTENSION_WWDR_INTERMEDIATE_LENGTHoidscert.hAdded CSSMOID_APPLEID_CERT_POLICYAdded CSSMOID_APPLEID_SHARING_CERT_POLICYAdded CSSMOID_APPLE_EXTENSION_AAI_INTERMEDIATEAdded CSSMOID_APPLE_EXTENSION_APPLEID_SHARINGAdded CSSMOID_APPLE_EXTENSION_INTERMEDIATE_MARKERAdded CSSMOID_APPLE_EXTENSION_ITMS_INTERMEDIATEAdded CSSMOID_APPLE_EXTENSION_MACAPPSTORE_RECEIPTAdded CSSMOID_APPLE_EXTENSION_WWDR_INTERMEDIATEAdded CSSMOID_InhibitAnyPolicyAdded CSSMOID_MACAPPSTORE_CERT_POLICYAdded CSSMOID_MACAPPSTORE_RECEIPT_CERT_POLICYModified CSSMOID_X509V1SignatureCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KERBv5_PKINIT_KP_CLIENT_AUTH

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1IssuerNameStd

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1IssuerName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_IDENTITY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EXTENSION_ADC_APPLE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_IssuingDistributionPoint

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ExtendedKeyUsage

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectEmailAddress

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectNameCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_IssuerAltName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EXTENSION_ADC_DEV_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectSignatureBitmap

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionsStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ADC_CERT_POLICY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EXTENSION

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SignatureAlgorithm

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DeltaCrlIndicator

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateNumberOfExtensions

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_NameConstraints

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ClientAuth

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_CODE_SIGNING_DEV

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_CODE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectAltName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectPicture

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionsCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SignatureAlgorithmTBS

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1IssuerNameCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_InvalidityDate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CertIssuer

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_MicrosoftSGC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectNameLDAP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_NetscapeCertType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionValue

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SignatureStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ServerAuth

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PrivateKeyUsagePeriod

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_BiometricInfo

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CertificateIssuerUniqueId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_EMAIL_ENCRYPT

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_IssuingDistributionPoints

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CrlDistributionPoints

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_HoldInstructionCode

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_EKU_IPSec

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_EXTENSION

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CertificateSubjectUniqueId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectPublicKeyAlgorithm

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PolicyMappings

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KeyUsage

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_QC_Statements

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AuthorityKeyIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EXTENSION_APPLE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3SignedCertificateCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectPublicKeyAlgorithmParameters

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionCritical

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_POLICY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_RESOURCE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EXTENSION_CODE_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_NetscapeSGC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1ValidityNotAfter

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectPublicKeyCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3SignedCertificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1ValidityNotBefore

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_EmailProtection

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CertificatePolicies

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CrlReason

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CSSMKeyStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectKeyIdentifier

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PolicyConstraints

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3Certificate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectPublicKey

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ExtendedUseCodeSigning

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_KERBv5_PKINIT_KP_KDC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_CrlNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_DOTMAC_CERT_EMAIL_SIGN

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1IssuerNameLDAP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SignatureAlgorithmParameters

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectDirectoryAttributes

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_SubjectInfoAccess

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_ICHAT_ENCRYPTION

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_AuthorityInfoAccess

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectNameStd

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_BasicConstraints

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_OCSPSigning

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SerialNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_SYSTEM_IDENTITY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_ExtendedKeyUsageAny

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_EKU_ICHAT_SIGNING

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_UseExemptions

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V3CertificateExtensionCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_TimeStamping

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1SubjectName

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1Signature

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1Version

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_APPLE_CERT_POLICY

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_NetscapeCertSequence

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

oidscrl.hModified CSSMOID_X509V2CRLRevokedEntryAllExtensionsStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntrySingleExtensionCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_BASIC

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLThisUpdate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLAllExtensionsStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedEntryStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryAllExtensionsCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryExtensionId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLTbsCertListCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_NONCE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_RESPONSE

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryExtensionValue

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryNumberOfExtensions

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryExtensionCritical

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLNextUpdate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_SERVICE_LOCATOR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLExtensionType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLSignedCrlStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_ARCHIVE_CUTOFF

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLNumberOfExtensions

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedCertificatesStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntrySingleExtensionStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLIssuerNameLDAP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_NOCHECK

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLSingleExtensionCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedCertificatesCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLAllExtensionsCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLNumberOfRevokedCertEntries

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedEntryCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLSingleExtensionStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLTbsCertListStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLVersion

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedEntrySerialNumber

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLIssuerStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLRevokedEntryExtensionType

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLSignedCrlCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_PKIX_OCSP_CRL

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLExtensionCritical

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLIssuerNameCStruct

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V1CRLRevokedEntryRevocationDate

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSMOID_X509V2CRLExtensionId

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

x509defs.hModified CSSM_X509_ALGORITHM_IDENTIFIER_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_EXTENSION_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_REVOKED_CERT_LIST_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_TBS_CERTLIST_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_EXTENSIONS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_NAME_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_BASICCONSTRAINTS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_POLICYQUALIFIERS_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_RDN_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_TBS_CERTIFICATE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_PAIR_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_POLICYINFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_TYPE_VALUE_PAIR_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_SIGNED_CRL_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_SIGNATURE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_VALIDITY_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_TAGandVALUE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_TIME_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_SIGNED_CERTIFICATE_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_REVOKED_CERT_ENTRY_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509EXT_POLICYQUALIFIERINFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CSSM_X509_SUBJECT_PUBLIC_KEY_INFO_PTR

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

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
