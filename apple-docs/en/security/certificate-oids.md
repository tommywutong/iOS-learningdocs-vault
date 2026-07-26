---
title: Certificate OIDs
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/certificate-oids
source_url: 'https://developer.apple.com/documentation/security/certificate-oids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/certificate-oids.json'
content_hash: 'sha256:3798213ed73ad895'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# Certificate OIDs

<sub>API Collection</sub>

Use OIDs as keys in the dictionary representing certificate values.

## Overview

These Object Identifiers (OIDs) are the keys that may appear in the dictionary returned by a call to the [SecCertificateCopyValues](<seccertificatecopyvalues(______).md>) function. The values associated with these keys are themselves dictionaries that represent the given property of a certificate, and that may have the keys listed in [Certificate Property Keys](certificate-property-keys.md).

## Topics

### Constants

- [kSecOIDADC_CERT_POLICY](ksecoidadc_cert_policy.md)
- [kSecOIDAPPLE_CERT_POLICY](ksecoidapple_cert_policy.md)
- [kSecOIDAPPLE_EKU_CODE_SIGNING](ksecoidapple_eku_code_signing.md)
- [kSecOIDAPPLE_EKU_CODE_SIGNING_DEV](ksecoidapple_eku_code_signing_dev.md)
- [kSecOIDAPPLE_EKU_ICHAT_ENCRYPTION](ksecoidapple_eku_ichat_encryption.md)
- [kSecOIDAPPLE_EKU_ICHAT_SIGNING](ksecoidapple_eku_ichat_signing.md)
- [kSecOIDAPPLE_EKU_RESOURCE_SIGNING](ksecoidapple_eku_resource_signing.md)
- [kSecOIDAPPLE_EKU_SYSTEM_IDENTITY](ksecoidapple_eku_system_identity.md)
- [kSecOIDAPPLE_EXTENSION](ksecoidapple_extension.md)
- [kSecOIDAPPLE_EXTENSION_AAI_INTERMEDIATE](ksecoidapple_extension_aai_intermediate.md)
- [kSecOIDAPPLE_EXTENSION_ADC_APPLE_SIGNING](ksecoidapple_extension_adc_apple_signing.md)
- [kSecOIDAPPLE_EXTENSION_ADC_DEV_SIGNING](ksecoidapple_extension_adc_dev_signing.md)
- [kSecOIDAPPLE_EXTENSION_APPLEID_INTERMEDIATE](ksecoidapple_extension_appleid_intermediate.md)
- [kSecOIDAPPLE_EXTENSION_APPLE_SIGNING](ksecoidapple_extension_apple_signing.md)
- [kSecOIDAPPLE_EXTENSION_CODE_SIGNING](ksecoidapple_extension_code_signing.md)
- [kSecOIDAPPLE_EXTENSION_INTERMEDIATE_MARKER](ksecoidapple_extension_intermediate_marker.md)
- [kSecOIDAPPLE_EXTENSION_ITMS_INTERMEDIATE](ksecoidapple_extension_itms_intermediate.md)
- [kSecOIDAPPLE_EXTENSION_WWDR_INTERMEDIATE](ksecoidapple_extension_wwdr_intermediate.md)
- [kSecOIDAuthorityInfoAccess](ksecoidauthorityinfoaccess.md)
- [kSecOIDAuthorityKeyIdentifier](ksecoidauthoritykeyidentifier.md)
- [kSecOIDBasicConstraints](ksecoidbasicconstraints.md)
- [kSecOIDBiometricInfo](ksecoidbiometricinfo.md)
- [kSecOIDCSSMKeyStruct](ksecoidcssmkeystruct.md)
- [kSecOIDCertIssuer](ksecoidcertissuer.md)
- [kSecOIDCertificatePolicies](ksecoidcertificatepolicies.md)
- [kSecOIDClientAuth](ksecoidclientauth.md)
- [kSecOIDCollectiveStateProvinceName](ksecoidcollectivestateprovincename.md)
- [kSecOIDCollectiveStreetAddress](ksecoidcollectivestreetaddress.md)
- [kSecOIDCommonName](ksecoidcommonname.md)
- [kSecOIDCountryName](ksecoidcountryname.md)
- [kSecOIDCrlDistributionPoints](ksecoidcrldistributionpoints.md)
- [kSecOIDCrlNumber](ksecoidcrlnumber.md)
- [kSecOIDCrlReason](ksecoidcrlreason.md)
- [kSecOIDDOTMAC_CERT_EMAIL_ENCRYPT](ksecoiddotmac_cert_email_encrypt.md)
- [kSecOIDDOTMAC_CERT_EMAIL_SIGN](ksecoiddotmac_cert_email_sign.md)
- [kSecOIDDOTMAC_CERT_EXTENSION](ksecoiddotmac_cert_extension.md)
- [kSecOIDDOTMAC_CERT_IDENTITY](ksecoiddotmac_cert_identity.md)
- [kSecOIDDOTMAC_CERT_POLICY](ksecoiddotmac_cert_policy.md)
- [kSecOIDDeltaCrlIndicator](ksecoiddeltacrlindicator.md)
- [kSecOIDDescription](ksecoiddescription.md)
- [kSecOIDEKU_IPSec](ksecoideku_ipsec.md)
- [kSecOIDEmailAddress](ksecoidemailaddress.md)
- [kSecOIDEmailProtection](ksecoidemailprotection.md)
- [kSecOIDExtendedKeyUsage](ksecoidextendedkeyusage.md)
- [kSecOIDExtendedKeyUsageAny](ksecoidextendedkeyusageany.md)
- [kSecOIDExtendedUseCodeSigning](ksecoidextendedusecodesigning.md)
- [kSecOIDGivenName](ksecoidgivenname.md)
- [kSecOIDHoldInstructionCode](ksecoidholdinstructioncode.md)
- [kSecOIDInvalidityDate](ksecoidinvaliditydate.md)
- [kSecOIDIssuerAltName](ksecoidissueraltname.md)
- [kSecOIDIssuingDistributionPoint](ksecoidissuingdistributionpoint.md)
- [kSecOIDIssuingDistributionPoints](ksecoidissuingdistributionpoints.md)
- [kSecOIDKERBv5_PKINIT_KP_CLIENT_AUTH](ksecoidkerbv5_pkinit_kp_client_auth.md)
- [kSecOIDKERBv5_PKINIT_KP_KDC](ksecoidkerbv5_pkinit_kp_kdc.md)
- [kSecOIDKeyUsage](ksecoidkeyusage.md)
- [kSecOIDLocalityName](ksecoidlocalityname.md)
- [kSecOIDMS_NTPrincipalName](ksecoidms_ntprincipalname.md)
- [kSecOIDMicrosoftSGC](ksecoidmicrosoftsgc.md)
- [kSecOIDNameConstraints](ksecoidnameconstraints.md)
- [kSecOIDNetscapeCertSequence](ksecoidnetscapecertsequence.md)
- [kSecOIDNetscapeCertType](ksecoidnetscapecerttype.md)
- [kSecOIDNetscapeSGC](ksecoidnetscapesgc.md)
- [kSecOIDOCSPSigning](ksecoidocspsigning.md)
- [kSecOIDOrganizationName](ksecoidorganizationname.md)
- [kSecOIDOrganizationalUnitName](ksecoidorganizationalunitname.md)
- [kSecOIDPolicyConstraints](ksecoidpolicyconstraints.md)
- [kSecOIDPolicyMappings](ksecoidpolicymappings.md)
- [kSecOIDPrivateKeyUsagePeriod](ksecoidprivatekeyusageperiod.md)
- [kSecOIDQC_Statements](ksecoidqc_statements.md)
- [kSecOIDSRVName](ksecoidsrvname.md)
- [kSecOIDSerialNumber](ksecoidserialnumber.md)
- [kSecOIDServerAuth](ksecoidserverauth.md)
- [kSecOIDStateProvinceName](ksecoidstateprovincename.md)
- [kSecOIDStreetAddress](ksecoidstreetaddress.md)
- [kSecOIDSubjectAltName](ksecoidsubjectaltname.md)
- [kSecOIDSubjectDirectoryAttributes](ksecoidsubjectdirectoryattributes.md)
- [kSecOIDSubjectEmailAddress](ksecoidsubjectemailaddress.md)
- [kSecOIDSubjectInfoAccess](ksecoidsubjectinfoaccess.md)
- [kSecOIDSubjectKeyIdentifier](ksecoidsubjectkeyidentifier.md)
- [kSecOIDSubjectPicture](ksecoidsubjectpicture.md)
- [kSecOIDSubjectSignatureBitmap](ksecoidsubjectsignaturebitmap.md)
- [kSecOIDSurname](ksecoidsurname.md)
- [kSecOIDTimeStamping](ksecoidtimestamping.md)
- [kSecOIDTitle](ksecoidtitle.md)
- [kSecOIDUseExemptions](ksecoiduseexemptions.md)
- [kSecOIDX509V1CertificateIssuerUniqueId](ksecoidx509v1certificateissueruniqueid.md)
- [kSecOIDX509V1CertificateSubjectUniqueId](ksecoidx509v1certificatesubjectuniqueid.md)
- [kSecOIDX509V1IssuerName](ksecoidx509v1issuername.md)
- [kSecOIDX509V1IssuerNameCStruct](ksecoidx509v1issuernamecstruct.md)
- [kSecOIDX509V1IssuerNameLDAP](ksecoidx509v1issuernameldap.md)
- [kSecOIDX509V1IssuerNameStd](ksecoidx509v1issuernamestd.md)
- [kSecOIDX509V1SerialNumber](ksecoidx509v1serialnumber.md)
- [kSecOIDX509V1Signature](ksecoidx509v1signature.md)
- [kSecOIDX509V1SignatureAlgorithm](ksecoidx509v1signaturealgorithm.md)
- [kSecOIDX509V1SignatureAlgorithmParameters](ksecoidx509v1signaturealgorithmparameters.md)
- [kSecOIDX509V1SignatureAlgorithmTBS](ksecoidx509v1signaturealgorithmtbs.md)
- [kSecOIDX509V1SignatureCStruct](ksecoidx509v1signaturecstruct.md)
- [kSecOIDX509V1SignatureStruct](ksecoidx509v1signaturestruct.md)
- [kSecOIDX509V1SubjectName](ksecoidx509v1subjectname.md)
- [kSecOIDX509V1SubjectNameCStruct](ksecoidx509v1subjectnamecstruct.md)
- [kSecOIDX509V1SubjectNameLDAP](ksecoidx509v1subjectnameldap.md)
- [kSecOIDX509V1SubjectNameStd](ksecoidx509v1subjectnamestd.md)
- [kSecOIDX509V1SubjectPublicKey](ksecoidx509v1subjectpublickey.md)
- [kSecOIDX509V1SubjectPublicKeyAlgorithm](ksecoidx509v1subjectpublickeyalgorithm.md)
- [kSecOIDX509V1SubjectPublicKeyAlgorithmParameters](ksecoidx509v1subjectpublickeyalgorithmparameters.md)
- [kSecOIDX509V1SubjectPublicKeyCStruct](ksecoidx509v1subjectpublickeycstruct.md)
- [kSecOIDX509V1ValidityNotAfter](ksecoidx509v1validitynotafter.md)
- [kSecOIDX509V1ValidityNotBefore](ksecoidx509v1validitynotbefore.md)
- [kSecOIDX509V1Version](ksecoidx509v1version.md)
- [kSecOIDX509V3Certificate](ksecoidx509v3certificate.md)
- [kSecOIDX509V3CertificateCStruct](ksecoidx509v3certificatecstruct.md)
- [kSecOIDX509V3CertificateExtensionCStruct](ksecoidx509v3certificateextensioncstruct.md)
- [kSecOIDX509V3CertificateExtensionCritical](ksecoidx509v3certificateextensioncritical.md)
- [kSecOIDX509V3CertificateExtensionId](ksecoidx509v3certificateextensionid.md)
- [kSecOIDX509V3CertificateExtensionStruct](ksecoidx509v3certificateextensionstruct.md)
- [kSecOIDX509V3CertificateExtensionType](ksecoidx509v3certificateextensiontype.md)
- [kSecOIDX509V3CertificateExtensionValue](ksecoidx509v3certificateextensionvalue.md)
- [kSecOIDX509V3CertificateExtensionsCStruct](ksecoidx509v3certificateextensionscstruct.md)
- [kSecOIDX509V3CertificateExtensionsStruct](ksecoidx509v3certificateextensionsstruct.md)
- [kSecOIDX509V3CertificateNumberOfExtensions](ksecoidx509v3certificatenumberofextensions.md)
- [kSecOIDX509V3SignedCertificate](ksecoidx509v3signedcertificate.md)
- [kSecOIDX509V3SignedCertificateCStruct](ksecoidx509v3signedcertificatecstruct.md)
