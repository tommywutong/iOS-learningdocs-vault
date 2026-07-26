---
title: Item attribute keys and values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/item-attribute-keys-and-values
source_url: 'https://developer.apple.com/documentation/security/item-attribute-keys-and-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/item-attribute-keys-and-values.json'
content_hash: 'sha256:cd90a73f2cdc8bf8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# Item attribute keys and values

<sub>API Collection</sub>

Specify the attributes of keychain items.

## Overview

In addition to the data that you want to store, keychain items also have attributes that allow you to find them later and that allow you to control how the data is used or shared.

You specify attributes as the keys and values of a dictionary. The available attribute keys are listed below. Typically, the corresponding value is a string, a number, or some other basic type, as given in each key description. In a few cases, the value comes instead from a list of a known constants. These predefined attribute values are also listed below, grouped according to the key that they serve.

> [!note] Note
> Not all attributes apply to every item class. You can find the list of attributes applicable to a given class in the relevant item class value definition, namely in [kSecClassGenericPassword](ksecclassgenericpassword.md), [kSecClassInternetPassword](ksecclassinternetpassword.md), [kSecClassCertificate](ksecclasscertificate.md), [kSecClassIdentity](ksecclassidentity.md), or [kSecClassKey](ksecclasskey.md).

## Topics

### General Item Attribute Keys

- [kSecAttrAccess](ksecattraccess.md) — A key with a value that indicates access control list settings for the item.
- [kSecAttrAccessControl](ksecattraccesscontrol.md) — A key with a value that’s an access control instance indicating access control settings for the item.
- [kSecAttrAccessible](ksecattraccessible.md) — A key with a value that indicates when the keychain item is accessible.
- [kSecAttrAccessGroup](ksecattraccessgroup.md) — A key with a value that’s a string indicating the access group the item is in.
- [kSecAttrSynchronizable](ksecattrsynchronizable.md) — A key with a value that’s a string indicating whether the item synchronizes through iCloud.
- [kSecAttrCreationDate](ksecattrcreationdate.md) — A key with a value that indicates the item’s creation date.
- [kSecAttrModificationDate](ksecattrmodificationdate.md) — A key with a value that indicates the item’s most recent modification date.
- [kSecAttrDescription](ksecattrdescription.md) — A key with a value that’s a string indicating the item’s description.
- [kSecAttrComment](ksecattrcomment.md) — A key with a value that’s a string indicating a comment associated with the item.
- [kSecAttrCreator](ksecattrcreator.md) — A key with a value that indicates the item’s creator.
- [kSecAttrType](ksecattrtype.md) — A key with a value that indicates the item’s type.
- [kSecAttrLabel](ksecattrlabel.md) — A key with a value that’s a string indicating the item’s label.
- [kSecAttrIsInvisible](ksecattrisinvisible.md) — A key with a value that’s a Boolean indicating the item’s visibility.
- [kSecAttrIsNegative](ksecattrisnegative.md) — A key with a value that’s a Boolean indicating whether the item has a valid password.
- [kSecAttrSyncViewHint](ksecattrsyncviewhint.md) — A key with a value that’s a string that provides a sync view hint.
- [kSecAttrPersistantReference](ksecattrpersistantreference.md)
- [kSecAttrPersistentReference](ksecattrpersistentreference.md)
- [kSecUseUserIndependentKeychain](ksecuseuserindependentkeychain.md) — A key with a value that indicates whether to store the data in a keychain available to anyone who uses the device.

### Password Attribute Keys

- [kSecAttrAccount](ksecattraccount.md) — A key whose value is a string indicating the item’s account name.
- [kSecAttrService](ksecattrservice.md) — A key whose value is a string indicating the item’s service.
- [kSecAttrGeneric](ksecattrgeneric.md) — A key whose value indicates the item’s user-defined attributes.
- [kSecAttrSecurityDomain](ksecattrsecuritydomain.md) — A key whose value is a string indicating the item’s security domain.
- [kSecAttrServer](ksecattrserver.md) — A key whose value is a string indicating the item’s server.
- [kSecAttrProtocol](ksecattrprotocol.md) — A key whose value indicates the item’s protocol.
- [kSecAttrAuthenticationType](ksecattrauthenticationtype.md) — A key whose value indicates the item’s authentication scheme.
- [kSecAttrPort](ksecattrport.md) — A key whose value indicates the item’s port.
- [kSecAttrPath](ksecattrpath.md) — A key whose value is a string indicating the item’s path attribute.

### Certificate Attribute Keys

- [kSecAttrSubject](ksecattrsubject.md) — A key whose value indicates the item’s subject name.
- [kSecAttrIssuer](ksecattrissuer.md) — A key whose value indicates the item’s issuer.
- [kSecAttrSerialNumber](ksecattrserialnumber.md) — A key whose value indicates the item’s serial number.
- [kSecAttrSubjectKeyID](ksecattrsubjectkeyid.md) — A key whose value indicates the item’s subject key ID.
- [kSecAttrPublicKeyHash](ksecattrpublickeyhash.md) — A key whose value indicates the item’s public key hash.
- [kSecAttrCertificateType](ksecattrcertificatetype.md) — A key whose value indicates the item’s certificate type.
- [kSecAttrCertificateEncoding](ksecattrcertificateencoding.md) — A key whose value indicates the item’s certificate encoding.

### Cryptographic Key Attribute Keys

- [kSecAttrKeyClass](ksecattrkeyclass.md) — A key whose value indicates the item’s cryptographic key class.
- [kSecAttrApplicationLabel](ksecattrapplicationlabel.md) — A key whose value indicates the item’s application label.
- [kSecAttrApplicationTag](ksecattrapplicationtag.md) — A key whose value indicates the item’s private tag.
- [kSecAttrKeyType](ksecattrkeytype.md) — A key whose value indicates the item’s algorithm.
- [kSecAttrPRF](ksecattrprf.md) — A key whose value indicates the item’s pseudorandom function.
- [kSecAttrSalt](ksecattrsalt.md) — A key whose value indicates the salt to use for this item.
- [kSecAttrRounds](ksecattrrounds.md) — A key whose value indicates the number of rounds to run the pseudorandom function.
- [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md) — A key whose value indicates the number of bits in a cryptographic key.
- [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md) — A key whose value indicates the effective number of bits in a cryptographic key.
- [kSecAttrTokenID](ksecattrtokenid.md) — A key whose value indicates that a cryptographic key is in an external store.

### Cryptographic Key Usage Attribute Keys

- [kSecAttrIsPermanent](ksecattrispermanent.md) — A key whose value indicates the item’s permanence.
- [kSecAttrIsSensitive](ksecattrissensitive.md) — A key whose value indicates the item’s sensitivity.
- [kSecAttrIsExtractable](ksecattrisextractable.md) — A key whose value indicates the item’s extractability.
- [kSecAttrCanEncrypt](ksecattrcanencrypt.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for encryption.
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for decryption.
- [kSecAttrCanDerive](ksecattrcanderive.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for derivation.
- [kSecAttrCanSign](ksecattrcansign.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for digital signing.
- [kSecAttrCanVerify](ksecattrcanverify.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for signature verification.
- [kSecAttrCanWrap](ksecattrcanwrap.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for wrapping.
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md) — A key whose value is a Boolean that indicates whether the cryptographic key can be used for unwrapping.

### Protocol Values

- [kSecAttrProtocolFTP](ksecattrprotocolftp.md) — FTP protocol.
- [kSecAttrProtocolFTPAccount](ksecattrprotocolftpaccount.md) — A client side FTP account.
- [kSecAttrProtocolHTTP](ksecattrprotocolhttp.md) — HTTP protocol.
- [kSecAttrProtocolIRC](ksecattrprotocolirc.md) — IRC protocol.
- [kSecAttrProtocolNNTP](ksecattrprotocolnntp.md) — NNTP protocol.
- [kSecAttrProtocolPOP3](ksecattrprotocolpop3.md) — POP3 protocol.
- [kSecAttrProtocolSMTP](ksecattrprotocolsmtp.md) — SMTP protocol.
- [kSecAttrProtocolSOCKS](ksecattrprotocolsocks.md) — SOCKS  protocol.
- [kSecAttrProtocolIMAP](ksecattrprotocolimap.md) — IMAP  protocol.
- [kSecAttrProtocolLDAP](ksecattrprotocolldap.md) — LDAP protocol.
- [kSecAttrProtocolAppleTalk](ksecattrprotocolappletalk.md) — AFP over AppleTalk.
- [kSecAttrProtocolAFP](ksecattrprotocolafp.md) — AFP over TCP.
- [kSecAttrProtocolTelnet](ksecattrprotocoltelnet.md) — Telnet protocol.
- [kSecAttrProtocolSSH](ksecattrprotocolssh.md) — SSH protocol.
- [kSecAttrProtocolFTPS](ksecattrprotocolftps.md) — FTP over TLS/SSL.
- [kSecAttrProtocolHTTPS](ksecattrprotocolhttps.md) — HTTP over TLS/SSL.
- [kSecAttrProtocolHTTPProxy](ksecattrprotocolhttpproxy.md) — HTTP proxy.
- [kSecAttrProtocolHTTPSProxy](ksecattrprotocolhttpsproxy.md) — HTTPS proxy.
- [kSecAttrProtocolFTPProxy](ksecattrprotocolftpproxy.md) — FTP proxy.
- [kSecAttrProtocolSMB](ksecattrprotocolsmb.md) — SMB protocol.
- [kSecAttrProtocolRTSP](ksecattrprotocolrtsp.md) — RTSP protocol.
- [kSecAttrProtocolRTSPProxy](ksecattrprotocolrtspproxy.md) — RTSP proxy.
- [kSecAttrProtocolDAAP](ksecattrprotocoldaap.md) — DAAP protocol.
- [kSecAttrProtocolEPPC](ksecattrprotocoleppc.md) — Remote Apple Events.
- [kSecAttrProtocolIPP](ksecattrprotocolipp.md) — IPP protocol.
- [kSecAttrProtocolNNTPS](ksecattrprotocolnntps.md) — NNTP over TLS/SSL.
- [kSecAttrProtocolLDAPS](ksecattrprotocolldaps.md) — LDAP over TLS/SSL.
- [kSecAttrProtocolTelnetS](ksecattrprotocoltelnets.md) — Telnet over TLS/SSL.
- [kSecAttrProtocolIMAPS](ksecattrprotocolimaps.md) — IMAP over TLS/SSL.
- [kSecAttrProtocolIRCS](ksecattrprotocolircs.md) — IRC over TLS/SSL.
- [kSecAttrProtocolPOP3S](ksecattrprotocolpop3s.md) — POP3 over TLS/SSL.

### Authentication Type Values

- [kSecAttrAuthenticationTypeNTLM](ksecattrauthenticationtypentlm.md) — Windows NT LAN Manager authentication.
- [kSecAttrAuthenticationTypeMSN](ksecattrauthenticationtypemsn.md) — Microsoft Network default authentication.
- [kSecAttrAuthenticationTypeDPA](ksecattrauthenticationtypedpa.md) — Distributed Password authentication.
- [kSecAttrAuthenticationTypeRPA](ksecattrauthenticationtyperpa.md) — Remote Password authentication.
- [kSecAttrAuthenticationTypeHTTPBasic](ksecattrauthenticationtypehttpbasic.md) — HTTP Basic authentication.
- [kSecAttrAuthenticationTypeHTTPDigest](ksecattrauthenticationtypehttpdigest.md) — HTTP Digest Access authentication.
- [kSecAttrAuthenticationTypeHTMLForm](ksecattrauthenticationtypehtmlform.md) — HTML form based authentication.
- [kSecAttrAuthenticationTypeDefault](ksecattrauthenticationtypedefault.md) — The default authentication type.

### Key Class Values

- [kSecAttrKeyClassPublic](ksecattrkeyclasspublic.md) — A public key of a public-private pair.
- [kSecAttrKeyClassPrivate](ksecattrkeyclassprivate.md) — A private key of a public-private pair.
- [kSecAttrKeyClassSymmetric](ksecattrkeyclasssymmetric.md) — A private key used for symmetric-key encryption and decryption.

### Key Type Values

- [kSecAttrKeyTypeRSA](ksecattrkeytypersa.md) — RSA algorithm.
- [kSecAttrKeyTypeDSA](ksecattrkeytypedsa.md) — DSA algorithm.
- [kSecAttrKeyTypeAES](ksecattrkeytypeaes.md) — AES algorithm.
- [kSecAttrKeyTypeDES](ksecattrkeytypedes.md) — DES algorithm.
- [kSecAttrKeyType3DES](ksecattrkeytype3des.md) — 3DES algorithm.
- [kSecAttrKeyTypeRC4](ksecattrkeytyperc4.md) — RC4 algorithm.
- [kSecAttrKeyTypeRC2](ksecattrkeytyperc2.md) — RC2 algorithm.
- [kSecAttrKeyTypeCAST](ksecattrkeytypecast.md) — CAST algorithm.
- [kSecAttrKeyTypeECDSA](ksecattrkeytypeecdsa.md) — Elliptic curve DSA algorithm. _(deprecated)_
- [kSecAttrKeyTypeEC](ksecattrkeytypeec.md) — Elliptic curve algorithm. _(deprecated)_
- [kSecAttrKeyTypeECSECPrimeRandom](ksecattrkeytypeecsecprimerandom.md) — Elliptic curve algorithm.

### Synchronizability Values

- [kSecAttrSynchronizableAny](ksecattrsynchronizableany.md) — Specifies that both synchronizable and non-synchronizable results should be returned from a query.

### Token ID Values

- [kSecAttrTokenIDSecureEnclave](ksecattrtokenidsecureenclave.md) — Specifies an item should be stored in the device’s Secure Enclave.

### Accessibility Values

- [kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly](ksecattraccessiblewhenpasscodesetthisdeviceonly.md) — The data in the keychain can only be accessed when the device is unlocked. Only available if a passcode is set on the device.
- [kSecAttrAccessibleWhenUnlockedThisDeviceOnly](ksecattraccessiblewhenunlockedthisdeviceonly.md) — The data in the keychain item can be accessed only while the device is unlocked by the user.
- [kSecAttrAccessibleWhenUnlocked](ksecattraccessiblewhenunlocked.md) — The data in the keychain item can be accessed only while the device is unlocked by the user.
- [kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly](ksecattraccessibleafterfirstunlockthisdeviceonly.md) — The data in the keychain item cannot be accessed after a restart until the device has been unlocked once by the user.
- [kSecAttrAccessibleAfterFirstUnlock](ksecattraccessibleafterfirstunlock.md) — The data in the keychain item cannot be accessed after a restart until the device has been unlocked once by the user.
- [kSecAttrAccessibleAlwaysThisDeviceOnly](ksecattraccessiblealwaysthisdeviceonly.md) — The data in the keychain item can always be accessed regardless of whether the device is locked. _(deprecated)_
- [kSecAttrAccessibleAlways](ksecattraccessiblealways.md) — The data in the keychain item can always be accessed regardless of whether the device is locked. _(deprecated)_

### Pseudorandom Function Values

- [kSecAttrPRFHmacAlgSHA1](ksecattrprfhmacalgsha1.md) — Use the SHA1 algorithm.
- [kSecAttrPRFHmacAlgSHA224](ksecattrprfhmacalgsha224.md) — Use the SHA224 algorithm.
- [kSecAttrPRFHmacAlgSHA256](ksecattrprfhmacalgsha256.md) — Use the SHA256 algorithm.
- [kSecAttrPRFHmacAlgSHA384](ksecattrprfhmacalgsha384.md) — Use the SHA384 algorithm.
- [kSecAttrPRFHmacAlgSHA512](ksecattrprfhmacalgsha512.md) — Use the SHA512 algorithm.

### Access Group Values

- [kSecAttrAccessGroupToken](ksecattraccessgrouptoken.md) — The access group containing items provided by external tokens.
