---
title: Security Framework Result Codes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/security-framework-result-codes
source_url: 'https://developer.apple.com/documentation/security/security-framework-result-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/security-framework-result-codes.json'
content_hash: 'sha256:dcaa1198d27bb135'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# Security Framework Result Codes

<sub>API Collection</sub>

Evaluate result codes common to many Security framework functions.

## Discussion

Use the [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) function to obtain a human readable string corresponding to these status codes.

In addition to the codes listed here, certain Security framework services provide additional status codes that are specific to that service. In particular, see [Authorization Services Result Codes](authorization-services-result-codes.md), [Sessions API Result Codes](sessions-api-result-codes.md), [Secure Transport Result Codes](secure-transport-result-codes.md), [Secure Download Result Codes](secure-download-result-codes.md), and [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Topics

### Result Strings

- [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) — Returns a string explaining the meaning of a security result code.

### System Result Codes

- [errSecSuccess](errsecsuccess.md) — No error.
- [errSecUnimplemented](errsecunimplemented.md) — A function or operation is not implemented.
- [errSecDskFull](errsecdskfull.md) — The disk is full. _(deprecated)_
- [errSecDiskFull](errsecdiskfull.md) — The disk is full.
- [errSecIO](errsecio.md) — I/O error.
- [errSecOpWr](errsecopwr.md) — The file is already open with write permission.
- [errSecParam](errsecparam.md) — One or more parameters passed to the function are not valid.
- [errSecWrPerm](errsecwrperm.md) — Write permissions error.
- [errSecAllocate](errsecallocate.md) — Failed to allocate memory.
- [errSecUserCanceled](errsecusercanceled.md) — User canceled the operation.
- [errSecBadReq](errsecbadreq.md) — Bad parameter or invalid state for operation.

### Internal Error Result Codes

- [errSecInternalComponent](errsecinternalcomponent.md) — An internal component experienced an error.
- [errSecCoreFoundationUnknown](errseccorefoundationunknown.md) — An unknown Core Foundation error occurred.
- [errSecInternalError](errsecinternalerror.md) — An internal error occurred.

### Keychain Result Codes

- [errSecNotAvailable](errsecnotavailable.md) — No trust results are available.
- [errSecReadOnly](errsecreadonly.md) — Read-only error.
- [errSecAuthFailed](errsecauthfailed.md) — Authorization and/or authentication failed.
- [errSecNoSuchKeychain](errsecnosuchkeychain.md) — The keychain does not exist.
- [errSecInvalidKeychain](errsecinvalidkeychain.md) — The keychain is not valid.
- [errSecDuplicateKeychain](errsecduplicatekeychain.md) — A keychain with the same name already exists.
- [errSecDuplicateCallback](errsecduplicatecallback.md) — More than one callback of the same name exists.
- [errSecInvalidCallback](errsecinvalidcallback.md) — The callback is not valid.
- [errSecDuplicateItem](errsecduplicateitem.md) — The item already exists.
- [errSecItemNotFound](errsecitemnotfound.md) — The item cannot be found.
- [errSecBufferTooSmall](errsecbuffertoosmall.md) — The buffer is too small.
- [errSecDataTooLarge](errsecdatatoolarge.md) — The data is too large for the particular data type.
- [errSecNoSuchAttr](errsecnosuchattr.md) — The attribute does not exist.
- [errSecInvalidItemRef](errsecinvaliditemref.md) — The item reference is invalid.
- [errSecInvalidSearchRef](errsecinvalidsearchref.md) — The search reference is invalid.
- [errSecNoSuchClass](errsecnosuchclass.md) — The keychain item class does not exist.
- [errSecNoDefaultKeychain](errsecnodefaultkeychain.md) — A default keychain does not exist.
- [errSecInteractionNotAllowed](errsecinteractionnotallowed.md) — Interaction with the Security Server is not allowed.
- [errSecReadOnlyAttr](errsecreadonlyattr.md) — The attribute is read-only.
- [errSecWrongSecVersion](errsecwrongsecversion.md) — The version is incorrect.
- [errSecKeySizeNotAllowed](errseckeysizenotallowed.md) — The key size is not allowed.
- [errSecNoStorageModule](errsecnostoragemodule.md) — There is no storage module available.
- [errSecNoCertificateModule](errsecnocertificatemodule.md) — There is no certificate module available.
- [errSecNoPolicyModule](errsecnopolicymodule.md) — There is no policy module available.
- [errSecInteractionRequired](errsecinteractionrequired.md) — User interaction is required.
- [errSecDataNotAvailable](errsecdatanotavailable.md) — The data is not available.
- [errSecDataNotModifiable](errsecdatanotmodifiable.md) — The data is not modifiable.
- [errSecCreateChainFailed](errseccreatechainfailed.md) — The attempt to create a certificate chain failed.
- [errSecInvalidPrefsDomain](errsecinvalidprefsdomain.md) — The preference domain specified is invalid.
- [errSecInDarkWake](errsecindarkwake.md) — The user interface cannot be displayed because the system is in a dark wake state.

### Certificate Result Codes

- [errSecUnknownCriticalExtensionFlag](errsecunknowncriticalextensionflag.md) — There is an unknown critical extension flag.
- [errSecCertificateCannotOperate](errseccertificatecannotoperate.md) — The certificate cannot operate.
- [errSecCertificateExpired](errseccertificateexpired.md) — An expired certificate was detected.
- [errSecCertificateNotValidYet](errseccertificatenotvalidyet.md) — The certificate is not yet valid.
- [errSecCertificateRevoked](errseccertificaterevoked.md) — The certificate was revoked.
- [errSecCertificateSuspended](errseccertificatesuspended.md) — The certificate was suspended.
- [errSecInvalidCertAuthority](errsecinvalidcertauthority.md) — The certificate authority is not valid.
- [errSecInvalidCertificateGroup](errsecinvalidcertificategroup.md) — An invalid certificate group was detected.
- [errSecInvalidCertificateRef](errsecinvalidcertificateref.md) — An invalid certificate reference was detected.
- [errSecCertificateNameNotAllowed](errseccertificatenamenotallowed.md) — The requested name isn’t allowed for this certificate.
- [errSecCertificatePolicyNotAllowed](errseccertificatepolicynotallowed.md) — The requested policy isn’t allowed for this certificate.
- [errSecCertificateValidityPeriodTooLong](errseccertificatevalidityperiodtoolong.md) — The validity period in the certificate exceeds the maximum allowed period.

### ACL Result Codes

- [errSecACLAddFailed](errsecacladdfailed.md) — An ACL add operation failed.
- [errSecACLChangeFailed](errsecaclchangefailed.md) — An ACL change operation failed.
- [errSecACLDeleteFailed](errsecacldeletefailed.md) — An ACL delete operation failed.
- [errSecACLNotSimple](errsecaclnotsimple.md) — The access control list is not in standard simple form.
- [errSecACLReplaceFailed](errsecaclreplacefailed.md) — An ACL replace operation failed.
- [errSecAppleAddAppACLSubject](errsecappleaddappaclsubject.md) — Adding an application ACL subject failed.
- [errSecInvalidBaseACLs](errsecinvalidbaseacls.md) — The base access control lists are not valid.
- [errSecInvalidACL](errsecinvalidacl.md) — An invalid access control list was detected.

### CRL Result Codes

- [errSecCRLExpired](errseccrlexpired.md) — The certificate revocation list has expired.
- [errSecCRLNotValidYet](errseccrlnotvalidyet.md) — The certificate revocation list is not yet valid.
- [errSecCRLNotFound](errseccrlnotfound.md) — The certificate revocation list was not found.
- [errSecCRLServerDown](errseccrlserverdown.md) — The certificate revocation list server is down.
- [errSecCRLBadURI](errseccrlbaduri.md) — The certificate revocation list has a bad uniform resource identifier.
- [errSecCRLNotTrusted](errseccrlnottrusted.md) — The certificate revocation list is not trusted.
- [errSecUnknownCertExtension](errsecunknowncertextension.md) — An unknown certificate extension was detected.
- [errSecUnknownCRLExtension](errsecunknowncrlextension.md) — An unknown certificate revocation list extension was detected.
- [errSecCRLPolicyFailed](errseccrlpolicyfailed.md) — The certificate revocation list policy failed.
- [errSecCRLAlreadySigned](errseccrlalreadysigned.md) — The certificate revocation list is already signed.
- [errSecIDPFailure](errsecidpfailure.md) — The issuing distribution point is not valid.
- [errSecInvalidCRLEncoding](errsecinvalidcrlencoding.md) — The certificate revocation list encoding is not valid.
- [errSecInvalidCRLType](errsecinvalidcrltype.md) — The certificate revocation list type is not valid.
- [errSecInvalidCRL](errsecinvalidcrl.md) — The certificate revocation list is not valid.
- [errSecInvalidCRLGroup](errsecinvalidcrlgroup.md) — An invalid certificate revocation list group was detected.
- [errSecInvalidCRLIndex](errsecinvalidcrlindex.md) — The certificate revocation list index is not valid.
- [errSecInvaldCRLAuthority](errsecinvaldcrlauthority.md) — The certificate revocation list authority is not valid. _(deprecated)_

### SMIME Result Codes

- [errSecSMIMEEmailAddressesNotFound](errsecsmimeemailaddressesnotfound.md) — An email address mismatch was detected.
- [errSecSMIMEBadExtendedKeyUsage](errsecsmimebadextendedkeyusage.md) — The appropriate extended key usage for SMIME is not found.
- [errSecSMIMEBadKeyUsage](errsecsmimebadkeyusage.md) — The key usage is not compatible with SMIME.
- [errSecSMIMEKeyUsageNotCritical](errsecsmimekeyusagenotcritical.md) — The key usage extension is not marked as critical.
- [errSecSMIMENoEmailAddress](errsecsmimenoemailaddress.md) — No email address is found in the certificate.
- [errSecSMIMESubjAltNameNotCritical](errsecsmimesubjaltnamenotcritical.md) — The subject alternative name extension is not marked as critical.
- [errSecSSLBadExtendedKeyUsage](errsecsslbadextendedkeyusage.md) — The appropriate extended key usage for SSL is not found.

### OCSP Result Codes

- [errSecOCSPBadResponse](errsecocspbadresponse.md) — The online certificate status protocol (OCSP) response is incorrect or cannot be parsed.
- [errSecOCSPBadRequest](errsecocspbadrequest.md) — The online certificate status protocol (OCSP) request is incorrect or cannot be parsed.
- [errSecOCSPUnavailable](errsecocspunavailable.md) — The online certificate status protocol (OCSP) service is unavailable.
- [errSecOCSPStatusUnrecognized](errsecocspstatusunrecognized.md) — The online certificate status protocol (OCSP) server does not recognize this certificate.
- [errSecEndOfData](errsecendofdata.md) — An end-of-data was detected.
- [errSecIncompleteCertRevocationCheck](errsecincompletecertrevocationcheck.md) — An incomplete certificate revocation check occurred.
- [errSecNetworkFailure](errsecnetworkfailure.md) — A network failure occurred.
- [errSecOCSPNotTrustedToAnchor](errsecocspnottrustedtoanchor.md) — The online certificate status protocol (OCSP) response is not trusted to a root or anchor certificate.
- [errSecRecordModified](errsecrecordmodified.md) — The record is modified.
- [errSecOCSPSignatureError](errsecocspsignatureerror.md) — The online certificate status protocol (OCSP) response has an invalid signature.
- [errSecOCSPNoSigner](errsecocspnosigner.md) — The online certificate status protocol (OCSP) response has no signer.
- [errSecOCSPResponderMalformedReq](errsecocsprespondermalformedreq.md) — The online certificate status protocol (OCSP) responder detected a malformed request.
- [errSecOCSPResponderInternalError](errsecocspresponderinternalerror.md) — The online certificate status protocol (OCSP) responder detected an internal error.
- [errSecOCSPResponderTryLater](errsecocsprespondertrylater.md) — The online certificate status protocol (OCSP) responder is busy, try again later.
- [errSecOCSPResponderSignatureRequired](errsecocsprespondersignaturerequired.md) — The online certificate status protocol (OCSP) responder requires a signature.
- [errSecOCSPResponderUnauthorized](errsecocspresponderunauthorized.md) — The online certificate status protocol (OCSP) responder rejects the request as unauthorized.
- [errSecOCSPResponseNonceMismatch](errsecocspresponsenoncemismatch.md) — The online certificate status protocol (OCSP) response nonce does not match the request.

### Code Signing Result Codes

- [errSecCodeSigningBadCertChainLength](errseccodesigningbadcertchainlength.md) — Code signing encountered an incorrect certificate chain length.
- [errSecCodeSigningNoBasicConstraints](errseccodesigningnobasicconstraints.md) — Code signing found no basic constraints.
- [errSecCodeSigningBadPathLengthConstraint](errseccodesigningbadpathlengthconstraint.md) — Code signing encountered an incorrect path length constraint.
- [errSecCodeSigningNoExtendedKeyUsage](errseccodesigningnoextendedkeyusage.md) — Code signing found no extended key usage.
- [errSecCodeSigningDevelopment](errseccodesigningdevelopment.md) — Code signing indicated use of a development-only certificate.
- [errSecResourceSignBadCertChainLength](errsecresourcesignbadcertchainlength.md) — Resource signing detects an incorrect certificate chain length.
- [errSecResourceSignBadExtKeyUsage](errsecresourcesignbadextkeyusage.md) — Resource signing detects an error in the extended key usage.
- [errSecTrustSettingDeny](errsectrustsettingdeny.md) — The trust setting for this policy is set to Deny.
- [errSecInvalidSubjectName](errsecinvalidsubjectname.md) — An invalid certificate subject name was detected.
- [errSecUnknownQualifiedCertStatement](errsecunknownqualifiedcertstatement.md) — An unknown qualified certificate statement was detected.

### Mobile Me Result Codes

- [errSecMobileMeRequestQueued](errsecmobilemerequestqueued.md) — The MobileMe request will be sent during the next connection.
- [errSecMobileMeRequestRedirected](errsecmobilemerequestredirected.md) — The MobileMe request was redirected.
- [errSecMobileMeServerError](errsecmobilemeservererror.md) — A MobileMe server error occurred.
- [errSecMobileMeServerNotAvailable](errsecmobilemeservernotavailable.md) — The MobileMe server is not available.
- [errSecMobileMeServerAlreadyExists](errsecmobilemeserveralreadyexists.md) — The MobileMe server reported that the item already exists.
- [errSecMobileMeServerServiceErr](errsecmobilemeserverserviceerr.md) — A MobileMe service error occurred.
- [errSecMobileMeRequestAlreadyPending](errsecmobilemerequestalreadypending.md) — A MobileMe request is already pending.
- [errSecMobileMeNoRequestPending](errsecmobilemenorequestpending.md) — MobileMe has no request pending.
- [errSecMobileMeCSRVerifyFailure](errsecmobilemecsrverifyfailure.md) — A MobileMe certificate signing request verification failure occurred.
- [errSecMobileMeFailedConsistencyCheck](errsecmobilemefailedconsistencycheck.md) — MobileMe found a failed consistency check.

### Cryptographic Key Result Codes

- [errSecKeyUsageIncorrect](errseckeyusageincorrect.md) — The key usage is incorrect.
- [errSecKeyBlobTypeIncorrect](errseckeyblobtypeincorrect.md) — The key blob type is incorrect.
- [errSecKeyHeaderInconsistent](errseckeyheaderinconsistent.md) — The key header is inconsistent.
- [errSecKeyIsSensitive](errseckeyissensitive.md) — The key must be wrapped to be exported.
- [errSecUnsupportedKeyFormat](errsecunsupportedkeyformat.md) — The key header format is not supported.
- [errSecUnsupportedKeySize](errsecunsupportedkeysize.md) — The key size is not supported.
- [errSecInvalidKeyUsageMask](errsecinvalidkeyusagemask.md) — The key usage mask is not valid.
- [errSecUnsupportedKeyUsageMask](errsecunsupportedkeyusagemask.md) — The key usage mask is not supported.
- [errSecInvalidKeyAttributeMask](errsecinvalidkeyattributemask.md) — The key attribute mask is not valid.
- [errSecUnsupportedKeyAttributeMask](errsecunsupportedkeyattributemask.md) — The key attribute mask is not supported.
- [errSecInvalidKeyLabel](errsecinvalidkeylabel.md) — The key label is not valid.
- [errSecUnsupportedKeyLabel](errsecunsupportedkeylabel.md) — The key label is not supported.
- [errSecInvalidKeyFormat](errsecinvalidkeyformat.md) — The key format is not valid.
- [errSecInvalidKeyBlob](errsecinvalidkeyblob.md) — The specified database has an invalid key blob.
- [errSecInvalidKeyHierarchy](errsecinvalidkeyhierarchy.md) — An invalid key hierarchy was detected.
- [errSecInvalidKeyRef](errsecinvalidkeyref.md) — An invalid key was encountered.
- [errSecInvalidKeyUsageForPolicy](errsecinvalidkeyusageforpolicy.md) — The key usage is not valid for the specified policy.

### Invalid Attribute Result Codes

- [errSecInvalidAttributeKey](errsecinvalidattributekey.md) — A key attribute is not valid.
- [errSecInvalidAttributeInitVector](errsecinvalidattributeinitvector.md) — An init vector attribute is not valid.
- [errSecInvalidAttributeSalt](errsecinvalidattributesalt.md) — A salt attribute is not valid.
- [errSecInvalidAttributePadding](errsecinvalidattributepadding.md) — A padding attribute is not valid.
- [errSecInvalidAttributeRandom](errsecinvalidattributerandom.md) — A random number attribute is not valid.
- [errSecInvalidAttributeSeed](errsecinvalidattributeseed.md) — A seed attribute is not valid.
- [errSecInvalidAttributePassphrase](errsecinvalidattributepassphrase.md) — A passphrase attribute is not valid.
- [errSecInvalidAttributeKeyLength](errsecinvalidattributekeylength.md) — A key length attribute is not valid.
- [errSecInvalidAttributeBlockSize](errsecinvalidattributeblocksize.md) — A block size attribute is not valid.
- [errSecInvalidAttributeOutputSize](errsecinvalidattributeoutputsize.md) — An output size attribute is not valid.
- [errSecInvalidAttributeRounds](errsecinvalidattributerounds.md) — The number of rounds attribute is not valid.
- [errSecInvalidAlgorithmParms](errsecinvalidalgorithmparms.md) — An algorithm parameters attribute is not valid.
- [errSecInvalidAttributeLabel](errsecinvalidattributelabel.md) — A label attribute is not valid.
- [errSecInvalidAttributeKeyType](errsecinvalidattributekeytype.md) — A key type attribute is not valid.
- [errSecInvalidAttributeMode](errsecinvalidattributemode.md) — A mode attribute is not valid.
- [errSecInvalidAttributeEffectiveBits](errsecinvalidattributeeffectivebits.md) — An effective bits attribute is not valid.
- [errSecInvalidAttributeStartDate](errsecinvalidattributestartdate.md) — A start date attribute is not valid.
- [errSecInvalidAttributeEndDate](errsecinvalidattributeenddate.md) — An end date attribute is not valid.
- [errSecInvalidAttributeVersion](errsecinvalidattributeversion.md) — A version attribute is not valid.
- [errSecInvalidAttributePrime](errsecinvalidattributeprime.md) — A prime attribute is not valid.
- [errSecInvalidAttributeBase](errsecinvalidattributebase.md) — A base attribute is not valid.
- [errSecInvalidAttributeSubprime](errsecinvalidattributesubprime.md) — A subprime attribute is not valid.
- [errSecInvalidAttributeIterationCount](errsecinvalidattributeiterationcount.md) — An iteration count attribute is not valid.
- [errSecInvalidAttributeDLDBHandle](errsecinvalidattributedldbhandle.md) — A database handle attribute is not valid.
- [errSecInvalidAttributeAccessCredentials](errsecinvalidattributeaccesscredentials.md) — An access credentials attribute is not valid.
- [errSecInvalidAttributePublicKeyFormat](errsecinvalidattributepublickeyformat.md) — A public key format attribute is not valid.
- [errSecInvalidAttributePrivateKeyFormat](errsecinvalidattributeprivatekeyformat.md) — A private key format attribute is not valid.
- [errSecInvalidAttributeSymmetricKeyFormat](errsecinvalidattributesymmetrickeyformat.md) — A symmetric key format attribute is not valid.
- [errSecInvalidAttributeWrappedKeyFormat](errsecinvalidattributewrappedkeyformat.md) — A wrapped key format attribute is not valid.

### Missing Attribute Result Codes

- [errSecMissingAttributeKey](errsecmissingattributekey.md) — A key attribute is missing.
- [errSecMissingAttributeInitVector](errsecmissingattributeinitvector.md) — An init vector attribute is missing.
- [errSecMissingAttributeSalt](errsecmissingattributesalt.md) — A salt attribute is missing.
- [errSecMissingAttributePadding](errsecmissingattributepadding.md) — A padding attribute is missing.
- [errSecMissingAttributeRandom](errsecmissingattributerandom.md) — A random number attribute is missing.
- [errSecMissingAttributeSeed](errsecmissingattributeseed.md) — A seed attribute is missing.
- [errSecMissingAttributePassphrase](errsecmissingattributepassphrase.md) — A passphrase attribute is missing.
- [errSecMissingAttributeKeyLength](errsecmissingattributekeylength.md) — A key length attribute is missing.
- [errSecMissingAttributeBlockSize](errsecmissingattributeblocksize.md) — A block size attribute is missing.
- [errSecMissingAttributeOutputSize](errsecmissingattributeoutputsize.md) — An output size attribute is missing.
- [errSecMissingAttributeRounds](errsecmissingattributerounds.md) — The number of rounds attribute is missing.
- [errSecMissingAlgorithmParms](errsecmissingalgorithmparms.md) — An algorithm parameters attribute is missing.
- [errSecMissingAttributeLabel](errsecmissingattributelabel.md) — A label attribute is missing.
- [errSecMissingAttributeKeyType](errsecmissingattributekeytype.md) — A key type attribute is missing.
- [errSecMissingAttributeMode](errsecmissingattributemode.md) — A mode attribute is missing.
- [errSecMissingAttributeEffectiveBits](errsecmissingattributeeffectivebits.md) — An effective bits attribute is missing.
- [errSecMissingAttributeStartDate](errsecmissingattributestartdate.md) — A start date attribute is missing.
- [errSecMissingAttributeEndDate](errsecmissingattributeenddate.md) — An end date attribute is missing.
- [errSecMissingAttributeVersion](errsecmissingattributeversion.md) — A version attribute is missing.
- [errSecMissingAttributePrime](errsecmissingattributeprime.md) — A prime attribute is missing.
- [errSecMissingAttributeBase](errsecmissingattributebase.md) — A base attribute is missing.
- [errSecMissingAttributeSubprime](errsecmissingattributesubprime.md) — A subprime attribute is missing.
- [errSecMissingAttributeIterationCount](errsecmissingattributeiterationcount.md) — An iteration count attribute is missing.
- [errSecMissingAttributeDLDBHandle](errsecmissingattributedldbhandle.md) — A database handle attribute is missing.
- [errSecMissingAttributeAccessCredentials](errsecmissingattributeaccesscredentials.md) — An access credentials attribute is missing.
- [errSecMissingAttributePublicKeyFormat](errsecmissingattributepublickeyformat.md) — A public key format attribute is missing.
- [errSecMissingAttributePrivateKeyFormat](errsecmissingattributeprivatekeyformat.md) — A private key format attribute is missing.
- [errSecMissingAttributeSymmetricKeyFormat](errsecmissingattributesymmetrickeyformat.md) — A symmetric key format attribute is missing.
- [errSecMissingAttributeWrappedKeyFormat](errsecmissingattributewrappedkeyformat.md) — A wrapped key format attribute is missing.

### Timestamp Result Codes

- [errSecTimestampMissing](errsectimestampmissing.md) — A timestamp is expected but is not found.
- [errSecTimestampInvalid](errsectimestampinvalid.md) — The timestamp is not valid.
- [errSecTimestampNotTrusted](errsectimestampnottrusted.md) — The timestamp is not trusted.
- [errSecTimestampServiceNotAvailable](errsectimestampservicenotavailable.md)
- [errSecTimestampBadAlg](errsectimestampbadalg.md) — Found an unrecognized or unsupported algorithm identifier (AI) in timestamp.
- [errSecTimestampBadRequest](errsectimestampbadrequest.md) — The timestamp transaction is not permitted or supported.
- [errSecTimestampBadDataFormat](errsectimestampbaddataformat.md) — The timestamp data submitted has the wrong format.
- [errSecTimestampTimeNotAvailable](errsectimestamptimenotavailable.md) — The time source for the timestamp authority is not available.
- [errSecTimestampUnacceptedPolicy](errsectimestampunacceptedpolicy.md) — The requested policy is not supported by the timestamp authority.
- [errSecTimestampUnacceptedExtension](errsectimestampunacceptedextension.md) — The requested extension is not supported by the timestamp authority.
- [errSecTimestampAddInfoNotAvailable](errsectimestampaddinfonotavailable.md) — The additional information requested is not available.
- [errSecTimestampSystemFailure](errsectimestampsystemfailure.md) — The timestamp request cannot be handled due to a system failure.
- [errSecSigningTimeMissing](errsecsigningtimemissing.md) — A signing time is missing.
- [errSecTimestampRejection](errsectimestamprejection.md) — A timestamp transaction is rejected.
- [errSecTimestampWaiting](errsectimestampwaiting.md) — A timestamp transaction is waiting.
- [errSecTimestampRevocationWarning](errsectimestamprevocationwarning.md) — A timestamp authority revocation warning is issued.
- [errSecTimestampRevocationNotification](errsectimestamprevocationnotification.md) — A timestamp authority revocation notification is issued.

### Invalid parameter result codes

- [errSecInvalidAction](errsecinvalidaction.md) — The action is invalid.
- [errSecInvalidAddinFunctionTable](errsecinvalidaddinfunctiontable.md) — An invalid add-in function table was detected.
- [errSecInvalidAlgorithm](errsecinvalidalgorithm.md) — An invalid algorithm was detected.
- [errSecInvalidAuthority](errsecinvalidauthority.md) — The authority is not valid.
- [errSecInvalidAuthorityKeyID](errsecinvalidauthoritykeyid.md) — The authority key ID is not valid.
- [errSecInvalidBundleInfo](errsecinvalidbundleinfo.md) — The bundle information is not valid.
- [errSecInvalidContext](errsecinvalidcontext.md) — An invalid context was detected.
- [errSecInvalidDBList](errsecinvaliddblist.md) — An invalid DB list was detected.
- [errSecInvalidDBLocation](errsecinvaliddblocation.md) — The database location is not valid.
- [errSecInvalidData](errsecinvaliddata.md) — Invalid data was detected.
- [errSecInvalidDatabaseBlob](errsecinvaliddatabaseblob.md) — The specified database has an invalid blob.
- [errSecInvalidDigestAlgorithm](errsecinvaliddigestalgorithm.md) — An invalid digest algorithm was detected.
- [errSecInvalidEncoding](errsecinvalidencoding.md) — The encoding is not valid.
- [errSecInvalidExtendedKeyUsage](errsecinvalidextendedkeyusage.md) — The extended key usage is not valid.
- [errSecInvalidFormType](errsecinvalidformtype.md) — The form type is not valid.
- [errSecInvalidGUID](errsecinvalidguid.md) — An invalid GUID was detected.
- [errSecInvalidHandle](errsecinvalidhandle.md) — An invalid handle was encountered.
- [errSecInvalidHandleUsage](errsecinvalidhandleusage.md) — The common security services manager handle does not match with the service type.
- [errSecInvalidID](errsecinvalidid.md) — The ID is not valid.
- [errSecInvalidIDLinkage](errsecinvalididlinkage.md) — The ID linkage is not valid.
- [errSecInvalidIdentifier](errsecinvalididentifier.md) — The identifier is not valid.
- [errSecInvalidIndex](errsecinvalidindex.md) — The index is not valid.
- [errSecInvalidIndexInfo](errsecinvalidindexinfo.md) — The index information is not valid.
- [errSecInvalidInputVector](errsecinvalidinputvector.md) — The input vector is not valid.
- [errSecInvalidLoginName](errsecinvalidloginname.md) — An invalid login name was detected.
- [errSecInvalidModifyMode](errsecinvalidmodifymode.md) — The modify mode is not valid.
- [errSecInvalidName](errsecinvalidname.md) — An invalid name was detected.
- [errSecInvalidNetworkAddress](errsecinvalidnetworkaddress.md) — An invalid network address was detected.
- [errSecInvalidNewOwner](errsecinvalidnewowner.md) — The new owner is not valid.
- [errSecInvalidNumberOfFields](errsecinvalidnumberoffields.md) — An invalid number of fields were detected.
- [errSecInvalidOutputVector](errsecinvalidoutputvector.md) — The output vector is not valid.
- [errSecInvalidOwnerEdit](errsecinvalidowneredit.md) — An invalid attempt to change the owner of an item.
- [errSecInvalidPVC](errsecinvalidpvc.md) — An invalid pointer validation checking policy was detected.
- [errSecInvalidParsingModule](errsecinvalidparsingmodule.md) — The parsing module is not valid.
- [errSecInvalidPassthroughID](errsecinvalidpassthroughid.md) — An invalid passthrough ID was detected.
- [errSecInvalidPasswordRef](errsecinvalidpasswordref.md) — The password reference is invalid.
- [errSecInvalidPointer](errsecinvalidpointer.md) — An invalid pointer was detected.
- [errSecInvalidPolicyIdentifiers](errsecinvalidpolicyidentifiers.md) — The policy identifiers are not valid.
- [errSecInvalidQuery](errsecinvalidquery.md) — The specified query is not valid.
- [errSecInvalidReason](errsecinvalidreason.md) — The trust policy reason is not valid.
- [errSecInvalidRecord](errsecinvalidrecord.md) — An invalid record was detected.
- [errSecInvalidRequestInputs](errsecinvalidrequestinputs.md) — The request inputs are not valid.
- [errSecInvalidRequestor](errsecinvalidrequestor.md) — The requestor is not valid.
- [errSecInvalidResponseVector](errsecinvalidresponsevector.md) — The response vector is not valid.
- [errSecInvalidRoot](errsecinvalidroot.md) — The root or anchor certificate is not valid.
- [errSecInvalidSampleValue](errsecinvalidsamplevalue.md) — An invalid sample value was detected.
- [errSecInvalidScope](errsecinvalidscope.md) — An invalid scope was detected.
- [errSecInvalidServiceMask](errsecinvalidservicemask.md) — An invalid service mask was detected.
- [errSecInvalidSignature](errsecinvalidsignature.md) — An invalid signature was detected.
- [errSecInvalidStopOnPolicy](errsecinvalidstoponpolicy.md) — The stop-on policy is not valid.
- [errSecInvalidSubServiceID](errsecinvalidsubserviceid.md) — An invalid sub-service ID was detected.
- [errSecInvalidSubjectKeyID](errsecinvalidsubjectkeyid.md) — The subject key ID is not valid.
- [errSecInvalidTimeString](errsecinvalidtimestring.md) — The time specified is not valid.
- [errSecInvalidTrustSetting](errsecinvalidtrustsetting.md) — The trust setting is invalid.
- [errSecInvalidTrustSettings](errsecinvalidtrustsettings.md) — The trust settings record is corrupted.
- [errSecInvalidTuple](errsecinvalidtuple.md) — The tuple is not valid.
- [errSecInvalidTupleCredendtials](errsecinvalidtuplecredendtials.md) — The tuple credentials are not valid. _(deprecated)_
- [errSecInvalidTupleGroup](errsecinvalidtuplegroup.md) — The tuple group is not valid.
- [errSecInvalidValidityPeriod](errsecinvalidvalidityperiod.md) — The validity period is not valid.
- [errSecInvalidValue](errsecinvalidvalue.md) — An invalid value was detected.

### Unsupported input result codes

- [errSecUnsupportedAddressType](errsecunsupportedaddresstype.md) — The address type is not supported.
- [errSecUnsupportedFieldFormat](errsecunsupportedfieldformat.md) — The field format is not supported.
- [errSecUnsupportedFormat](errsecunsupportedformat.md) — The specified import or export format is not supported.
- [errSecUnsupportedIndexInfo](errsecunsupportedindexinfo.md) — The index information is not supported.
- [errSecUnsupportedLocality](errsecunsupportedlocality.md) — The locality is not supported.
- [errSecUnsupportedNumAttributes](errsecunsupportednumattributes.md) — The number of attributes is not supported.
- [errSecUnsupportedNumIndexes](errsecunsupportednumindexes.md) — The number of indexes is not supported.
- [errSecUnsupportedNumRecordTypes](errsecunsupportednumrecordtypes.md) — The number of record types is not supported.
- [errSecUnsupportedNumSelectionPreds](errsecunsupportednumselectionpreds.md) — The number of selection predicates is not supported.
- [errSecUnsupportedOperator](errsecunsupportedoperator.md) — The operator is not supported.
- [errSecUnsupportedQueryLimits](errsecunsupportedquerylimits.md) — The query limits are not supported.
- [errSecUnsupportedService](errsecunsupportedservice.md) — The service is not supported.
- [errSecUnsupportedVectorOfBuffers](errsecunsupportedvectorofbuffers.md) — The vector of buffers is not supported.

### Apple specific result codes

- [errSecAppleInvalidKeyEndDate](errsecappleinvalidkeyenddate.md) — The specified key has an invalid end date.
- [errSecAppleInvalidKeyStartDate](errsecappleinvalidkeystartdate.md) — The specified key has an invalid start date.
- [errSecApplePublicKeyIncomplete](errsecapplepublickeyincomplete.md) — The public key is incomplete.
- [errSecAppleSSLv2Rollback](errsecapplesslv2rollback.md) — A SSLv2 rollback error has occurred.
- [errSecAppleSignatureMismatch](errsecapplesignaturemismatch.md) — A signature mismatch has occurred.

### Module manager result codes

- [errSecEMMLoadFailed](errsecemmloadfailed.md) — The elective module manager load failed.
- [errSecEMMUnloadFailed](errsecemmunloadfailed.md) — The elective module manager unload has failed.
- [errSecModuleManagerInitializeFailed](errsecmodulemanagerinitializefailed.md) — A module failed to initialize.
- [errSecModuleManagerNotFound](errsecmodulemanagernotfound.md) — A module was not found.
- [errSecModuleManifestVerifyFailed](errsecmodulemanifestverifyfailed.md) — A module manifest verification failure occurred.
- [errSecModuleNotLoaded](errsecmodulenotloaded.md) — A module was not loaded.

### Other Result Codes

- [errSecAddinLoadFailed](errsecaddinloadfailed.md) — The add-in load operation failed.
- [errSecAddinUnloadFailed](errsecaddinunloadfailed.md) — The add-in unload operation failed.
- [errSecAlgorithmMismatch](errsecalgorithmmismatch.md) — An algorithm mismatch occurred.
- [errSecAlreadyLoggedIn](errsecalreadyloggedin.md) — The user is already logged in.
- [errSecAttachHandleBusy](errsecattachhandlebusy.md) — The CSP handle was busy.
- [errSecAttributeNotInContext](errsecattributenotincontext.md) — An attribute was not in the context.
- [errSecBlockSizeMismatch](errsecblocksizemismatch.md) — A block size mismatch occurred.
- [errSecCallbackFailed](errseccallbackfailed.md) — A callback failed.
- [errSecConversionError](errsecconversionerror.md) — A conversion error has occurred.
- [errSecDatabaseLocked](errsecdatabaselocked.md) — The database is locked.
- [errSecDatastoreIsOpen](errsecdatastoreisopen.md) — The data store is open.
- [errSecDecode](errsecdecode.md) — Unable to decode the provided data.
- [errSecDeviceError](errsecdeviceerror.md) — A device error was encountered.
- [errSecDeviceFailed](errsecdevicefailed.md) — A device failure has occurred.
- [errSecDeviceReset](errsecdevicereset.md) — A device reset has occurred.
- [errSecDeviceVerifyFailed](errsecdeviceverifyfailed.md) — A device verification failure has occurred.
- [errSecEventNotificationCallbackNotFound](errseceventnotificationcallbacknotfound.md) — An event notification callback was not found.
- [errSecExtendedKeyUsageNotCritical](errsecextendedkeyusagenotcritical.md) — The extended key usage extension was not marked critical.
- [errSecFieldSpecifiedMultiple](errsecfieldspecifiedmultiple.md) — Too many fields were specified.
- [errSecFileTooBig](errsecfiletoobig.md) — The file is too big.
- [errSecFunctionFailed](errsecfunctionfailed.md) — A function has failed.
- [errSecFunctionIntegrityFail](errsecfunctionintegrityfail.md) — A function address is not within the verified module.
- [errSecHostNameMismatch](errsechostnamemismatch.md) — A host name mismatch has occurred.
- [errSecIncompatibleDatabaseBlob](errsecincompatibledatabaseblob.md) — The specified database has an incompatible blob.
- [errSecIncompatibleFieldFormat](errsecincompatiblefieldformat.md) — The field format is incompatible.
- [errSecIncompatibleKeyBlob](errsecincompatiblekeyblob.md) — The specified database has an incompatible key blob.
- [errSecIncompatibleVersion](errsecincompatibleversion.md) — The version is incompatible.
- [errSecInputLengthError](errsecinputlengtherror.md) — An input length error occurred.
- [errSecInsufficientClientID](errsecinsufficientclientid.md) — The client ID is incorrect.
- [errSecInsufficientCredentials](errsecinsufficientcredentials.md) — Insufficient credentials were detected.
- [errSecInvalidAccessCredentials](errsecinvalidaccesscredentials.md) — Invalid access credentials were detected.
- [errSecInvalidAccessRequest](errsecinvalidaccessrequest.md) — The access request is invalid.
- [errSecLibraryReferenceNotFound](errseclibraryreferencenotfound.md) — A library reference was not found.
- [errSecMDSError](errsecmdserror.md) — A module directory service error occurred.
- [errSecMemoryError](errsecmemoryerror.md) — A memory error occurred.
- [errSecMissingEntitlement](errsecmissingentitlement.md) — A required entitlement is missing.
- [errSecMissingRequiredExtension](errsecmissingrequiredextension.md) — A required certificate extension is missing.
- [errSecMissingValue](errsecmissingvalue.md) — A missing value was detected.
- [errSecMultiplePrivKeys](errsecmultipleprivkeys.md) — An attempt was made to import multiple private keys.
- [errSecMultipleValuesUnsupported](errsecmultiplevaluesunsupported.md) — Multiple values are not supported.
- [errSecNoAccessForItem](errsecnoaccessforitem.md) — The specified item has no access control.
- [errSecNoBasicConstraints](errsecnobasicconstraints.md) — No basic constraints were found.
- [errSecNoBasicConstraintsCA](errsecnobasicconstraintsca.md) — No basic CA constraints were found.
- [errSecNoDefaultAuthority](errsecnodefaultauthority.md) — No default authority was detected.
- [errSecNoFieldValues](errsecnofieldvalues.md) — No field values were detected.
- [errSecNoTrustSettings](errsecnotrustsettings.md) — No trust settings were found.
- [errSecNotInitialized](errsecnotinitialized.md) — A function was called without initializing the common security services manager.
- [errSecNotLoggedIn](errsecnotloggedin.md) — You are not logged in.
- [errSecNotSigner](errsecnotsigner.md) — The certificate is not signed by its proposed parent.
- [errSecNotTrusted](errsecnottrusted.md) — The trust policy is not trusted.
- [errSecOutputLengthError](errsecoutputlengtherror.md) — An output length error was detected.
- [errSecPVCAlreadyConfigured](errsecpvcalreadyconfigured.md) — The PVC is already configured.
- [errSecPVCReferentNotFound](errsecpvcreferentnotfound.md) — A reference to the calling module was not found in the list of authorized callers.
- [errSecPassphraseRequired](errsecpassphraserequired.md) — A password is required for import or export.
- [errSecPathLengthConstraintExceeded](errsecpathlengthconstraintexceeded.md) — The path length constraint was exceeded.
- [errSecPkcs12VerifyFailure](errsecpkcs12verifyfailure.md) — MAC verification failed during PKCS12 Import.
- [errSecPolicyNotFound](errsecpolicynotfound.md) — The specified policy cannot be found.
- [errSecPrivilegeNotGranted](errsecprivilegenotgranted.md) — The privilege is not granted.
- [errSecPrivilegeNotSupported](errsecprivilegenotsupported.md) — The privilege is not supported.
- [errSecPublicKeyInconsistent](errsecpublickeyinconsistent.md) — The public key is inconsistent.
- [errSecQuerySizeUnknown](errsecquerysizeunknown.md) — The query size is unknown.
- [errSecQuotaExceeded](errsecquotaexceeded.md) — The quota was exceeded.
- [errSecRejectedForm](errsecrejectedform.md) — The trust policy has a rejected form.
- [errSecRequestDescriptor](errsecrequestdescriptor.md) — The request descriptor is not valid.
- [errSecRequestLost](errsecrequestlost.md) — The request is lost.
- [errSecRequestRejected](errsecrequestrejected.md) — The request is rejected.
- [errSecSelfCheckFailed](errsecselfcheckfailed.md) — Self-check failed.
- [errSecServiceNotAvailable](errsecservicenotavailable.md) — Self-check failed.
- [errSecStagedOperationInProgress](errsecstagedoperationinprogress.md) — A staged operation is in progress.
- [errSecStagedOperationNotStarted](errsecstagedoperationnotstarted.md) — A staged operation was not started.
- [errSecTagNotFound](errsectagnotfound.md) — The specified tag is not found.
- [errSecTrustNotAvailable](errsectrustnotavailable.md) — No trust results are available.
- [errSecUnknownFormat](errsecunknownformat.md) — The item you are trying to import has an unknown format.
- [errSecUnknownTag](errsecunknowntag.md) — An unknown tag was detected.
- [errSecVerificationFailure](errsecverificationfailure.md) — A verification failure occurred.
- [errSecVerifyActionFailed](errsecverifyactionfailed.md) — A verify action failed.
- [errSecVerifyFailed](errsecverifyfailed.md) — A cryptographic verification failure occurred.

## See Also

### Related Documentation

- [Sessions API Result Codes](sessions-api-result-codes.md) — Recognize result codes specific to the sessions API.
- [Secure Transport Result Codes](secure-transport-result-codes.md) — Recognize result codes specific to the secure transport API.
- [Code Signing Services Result Codes](code-signing-services-result-codes.md) — Recognize result codes specific to the code signing services API.
