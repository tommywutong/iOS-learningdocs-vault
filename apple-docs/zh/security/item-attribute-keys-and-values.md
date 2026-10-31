---
title: 条目属性键和值
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
translated: true
---

> 导航： [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md) · [Keychain items](keychain-items.md)

# 条目属性键和值

<sub>API 集合</sub>

指定钥匙串条目的属性。

## 概述

除了你要存储的数据之外，钥匙串条目还有一些属性，让你能够在日后查找它们，并控制数据的使用或共享方式。

你以字典的键和值的形式指定属性。可用的属性键列在下方。通常，对应的值是字符串、数字或其他基本类型，具体见每个键的描述。在少数情况下，值来自一个已知常量列表。这些预定义的属性值也列在下方，按它们所服务的键分组。

> [!note] Note
> Not all attributes apply to every item class. You can find the list of attributes applicable to a given class in the relevant item class value definition, namely in [kSecClassGenericPassword](ksecclassgenericpassword.md), [kSecClassInternetPassword](ksecclassinternetpassword.md), [kSecClassCertificate](ksecclasscertificate.md), [kSecClassIdentity](ksecclassidentity.md), or [kSecClassKey](ksecclasskey.md).

## 主题

### 通用条目属性键

- [kSecAttrAccess](ksecattraccess.md) — 一个键，其值指示该条目的访问控制列表设置。
- [kSecAttrAccessControl](ksecattraccesscontrol.md) — 一个键，其值是一个访问控制实例，指示该条目的访问控制设置。
- [kSecAttrAccessible](ksecattraccessible.md) — 一个键，其值指示钥匙串条目何时可访问。
- [kSecAttrAccessGroup](ksecattraccessgroup.md) — 一个键，其值是一个字符串，指示该条目所在的访问组。
- [kSecAttrSynchronizable](ksecattrsynchronizable.md) — 一个键，其值是一个字符串，指示该条目是否通过 iCloud 同步。
- [kSecAttrCreationDate](ksecattrcreationdate.md) — 一个键，其值指示该条目的创建日期。
- [kSecAttrModificationDate](ksecattrmodificationdate.md) — 一个键，其值指示该条目最近一次的修改日期。
- [kSecAttrDescription](ksecattrdescription.md) — 一个键，其值是一个字符串，指示该条目的描述。
- [kSecAttrComment](ksecattrcomment.md) — 一个键，其值是一个字符串，指示与该条目关联的注释。
- [kSecAttrCreator](ksecattrcreator.md) — 一个键，其值指示该条目的创建者。
- [kSecAttrType](ksecattrtype.md) — 一个键，其值指示该条目的类型。
- [kSecAttrLabel](ksecattrlabel.md) — 一个键，其值是一个字符串，指示该条目的标签。
- [kSecAttrIsInvisible](ksecattrisinvisible.md) — 一个键，其值是一个布尔值，指示该条目的可见性。
- [kSecAttrIsNegative](ksecattrisnegative.md) — 一个键，其值是一个布尔值，指示该条目是否具有有效密码。
- [kSecAttrSyncViewHint](ksecattrsyncviewhint.md) — 一个键，其值是一个字符串，提供同步视图提示。
- [kSecAttrPersistantReference](ksecattrpersistantreference.md)
- [kSecAttrPersistentReference](ksecattrpersistentreference.md)
- [kSecUseUserIndependentKeychain](ksecuseuserindependentkeychain.md) — 一个键，其值指示是否把数据存储在设备的任何使用者都可用的钥匙串中。

### 密码属性键

- [kSecAttrAccount](ksecattraccount.md) — 一个键，其值是一个字符串，指示该条目的账户名。
- [kSecAttrService](ksecattrservice.md) — 一个键，其值是一个字符串，指示该条目的服务。
- [kSecAttrGeneric](ksecattrgeneric.md) — 一个键，其值指示该条目的用户定义属性。
- [kSecAttrSecurityDomain](ksecattrsecuritydomain.md) — 一个键，其值是一个字符串，指示该条目的安全域。
- [kSecAttrServer](ksecattrserver.md) — 一个键，其值是一个字符串，指示该条目的服务器。
- [kSecAttrProtocol](ksecattrprotocol.md) — 一个键，其值指示该条目的协议。
- [kSecAttrAuthenticationType](ksecattrauthenticationtype.md) — 一个键，其值指示该条目的认证方案。
- [kSecAttrPort](ksecattrport.md) — 一个键，其值指示该条目的端口。
- [kSecAttrPath](ksecattrpath.md) — 一个键，其值是一个字符串，指示该条目的路径属性。

### 证书属性键

- [kSecAttrSubject](ksecattrsubject.md) — 一个键，其值指示该条目的使用者名称。
- [kSecAttrIssuer](ksecattrissuer.md) — 一个键，其值指示该条目的颁发者。
- [kSecAttrSerialNumber](ksecattrserialnumber.md) — 一个键，其值指示该条目的序列号。
- [kSecAttrSubjectKeyID](ksecattrsubjectkeyid.md) — 一个键，其值指示该条目的使用者密钥 ID。
- [kSecAttrPublicKeyHash](ksecattrpublickeyhash.md) — 一个键，其值指示该条目的公钥哈希值。
- [kSecAttrCertificateType](ksecattrcertificatetype.md) — 一个键，其值指示该条目的证书类型。
- [kSecAttrCertificateEncoding](ksecattrcertificateencoding.md) — 一个键，其值指示该条目的证书编码。

### 加密密钥属性键

- [kSecAttrKeyClass](ksecattrkeyclass.md) — 一个键，其值指示该条目的加密密钥类。
- [kSecAttrApplicationLabel](ksecattrapplicationlabel.md) — 一个键，其值指示该条目的应用程序标签。
- [kSecAttrApplicationTag](ksecattrapplicationtag.md) — 一个键，其值指示该条目的私有标签。
- [kSecAttrKeyType](ksecattrkeytype.md) — 一个键，其值指示该条目的算法。
- [kSecAttrPRF](ksecattrprf.md) — 一个键，其值指示该条目的伪随机函数。
- [kSecAttrSalt](ksecattrsalt.md) — 一个键，其值指示此条目要使用的盐值。
- [kSecAttrRounds](ksecattrrounds.md) — 一个键，其值指示运行伪随机函数的轮数。
- [kSecAttrKeySizeInBits](ksecattrkeysizeinbits.md) — 一个键，其值指示加密密钥的位数。
- [kSecAttrEffectiveKeySize](ksecattreffectivekeysize.md) — 一个键，其值指示加密密钥的有效位数。
- [kSecAttrTokenID](ksecattrtokenid.md) — 一个键，其值指示某个加密密钥是否位于外部存储中。

### 加密密钥用途属性键

- [kSecAttrIsPermanent](ksecattrispermanent.md) — 一个键，其值指示该条目的持久性。
- [kSecAttrIsSensitive](ksecattrissensitive.md) — 一个键，其值指示该条目的敏感性。
- [kSecAttrIsExtractable](ksecattrisextractable.md) — 一个键，其值指示该条目的可提取性。
- [kSecAttrCanEncrypt](ksecattrcanencrypt.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于加密。
- [kSecAttrCanDecrypt](ksecattrcandecrypt.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于解密。
- [kSecAttrCanDerive](ksecattrcanderive.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于派生。
- [kSecAttrCanSign](ksecattrcansign.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于数字签名。
- [kSecAttrCanVerify](ksecattrcanverify.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于签名验证。
- [kSecAttrCanWrap](ksecattrcanwrap.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于包装。
- [kSecAttrCanUnwrap](ksecattrcanunwrap.md) — 一个键，其值是一个布尔值，指示该加密密钥是否可用于解包。

### 协议值

- [kSecAttrProtocolFTP](ksecattrprotocolftp.md) — FTP 协议。
- [kSecAttrProtocolFTPAccount](ksecattrprotocolftpaccount.md) — 客户端 FTP 账户。
- [kSecAttrProtocolHTTP](ksecattrprotocolhttp.md) — HTTP 协议。
- [kSecAttrProtocolIRC](ksecattrprotocolirc.md) — IRC 协议。
- [kSecAttrProtocolNNTP](ksecattrprotocolnntp.md) — NNTP 协议。
- [kSecAttrProtocolPOP3](ksecattrprotocolpop3.md) — POP3 协议。
- [kSecAttrProtocolSMTP](ksecattrprotocolsmtp.md) — SMTP 协议。
- [kSecAttrProtocolSOCKS](ksecattrprotocolsocks.md) — SOCKS 协议。
- [kSecAttrProtocolIMAP](ksecattrprotocolimap.md) — IMAP 协议。
- [kSecAttrProtocolLDAP](ksecattrprotocolldap.md) — LDAP 协议。
- [kSecAttrProtocolAppleTalk](ksecattrprotocolappletalk.md) — 基于 AppleTalk 的 AFP。
- [kSecAttrProtocolAFP](ksecattrprotocolafp.md) — 基于 TCP 的 AFP。
- [kSecAttrProtocolTelnet](ksecattrprotocoltelnet.md) — Telnet 协议。
- [kSecAttrProtocolSSH](ksecattrprotocolssh.md) — SSH 协议。
- [kSecAttrProtocolFTPS](ksecattrprotocolftps.md) — 基于 TLS/SSL 的 FTP。
- [kSecAttrProtocolHTTPS](ksecattrprotocolhttps.md) — 基于 TLS/SSL 的 HTTP。
- [kSecAttrProtocolHTTPProxy](ksecattrprotocolhttpproxy.md) — HTTP 代理。
- [kSecAttrProtocolHTTPSProxy](ksecattrprotocolhttpsproxy.md) — HTTPS 代理。
- [kSecAttrProtocolFTPProxy](ksecattrprotocolftpproxy.md) — FTP 代理。
- [kSecAttrProtocolSMB](ksecattrprotocolsmb.md) — SMB 协议。
- [kSecAttrProtocolRTSP](ksecattrprotocolrtsp.md) — RTSP 协议。
- [kSecAttrProtocolRTSPProxy](ksecattrprotocolrtspproxy.md) — RTSP 代理。
- [kSecAttrProtocolDAAP](ksecattrprotocoldaap.md) — DAAP 协议。
- [kSecAttrProtocolEPPC](ksecattrprotocoleppc.md) — 远程 Apple 事件。
- [kSecAttrProtocolIPP](ksecattrprotocolipp.md) — IPP 协议。
- [kSecAttrProtocolNNTPS](ksecattrprotocolnntps.md) — 基于 TLS/SSL 的 NNTP。
- [kSecAttrProtocolLDAPS](ksecattrprotocolldaps.md) — 基于 TLS/SSL 的 LDAP。
- [kSecAttrProtocolTelnetS](ksecattrprotocoltelnets.md) — 基于 TLS/SSL 的 Telnet。
- [kSecAttrProtocolIMAPS](ksecattrprotocolimaps.md) — 基于 TLS/SSL 的 IMAP。
- [kSecAttrProtocolIRCS](ksecattrprotocolircs.md) — 基于 TLS/SSL 的 IRC。
- [kSecAttrProtocolPOP3S](ksecattrprotocolpop3s.md) — 基于 TLS/SSL 的 POP3。

### 认证类型值

- [kSecAttrAuthenticationTypeNTLM](ksecattrauthenticationtypentlm.md) — Windows NT 局域网管理器认证。
- [kSecAttrAuthenticationTypeMSN](ksecattrauthenticationtypemsn.md) — Microsoft 网络默认认证。
- [kSecAttrAuthenticationTypeDPA](ksecattrauthenticationtypedpa.md) — 分布式密码认证。
- [kSecAttrAuthenticationTypeRPA](ksecattrauthenticationtyperpa.md) — 远程密码认证。
- [kSecAttrAuthenticationTypeHTTPBasic](ksecattrauthenticationtypehttpbasic.md) — HTTP Basic 认证。
- [kSecAttrAuthenticationTypeHTTPDigest](ksecattrauthenticationtypehttpdigest.md) — HTTP Digest Access 认证。
- [kSecAttrAuthenticationTypeHTMLForm](ksecattrauthenticationtypehtmlform.md) — 基于 HTML 表单的认证。
- [kSecAttrAuthenticationTypeDefault](ksecattrauthenticationtypedefault.md) — 默认认证类型。

### 密钥类值

- [kSecAttrKeyClassPublic](ksecattrkeyclasspublic.md) — 公私钥对中的公钥。
- [kSecAttrKeyClassPrivate](ksecattrkeyclassprivate.md) — 公私钥对中的私钥。
- [kSecAttrKeyClassSymmetric](ksecattrkeyclasssymmetric.md) — 用于对称密钥加密和解密的私钥。

### 密钥类型值

- [kSecAttrKeyTypeRSA](ksecattrkeytypersa.md) — RSA 算法。
- [kSecAttrKeyTypeDSA](ksecattrkeytypedsa.md) — DSA 算法。
- [kSecAttrKeyTypeAES](ksecattrkeytypeaes.md) — AES 算法。
- [kSecAttrKeyTypeDES](ksecattrkeytypedes.md) — DES 算法。
- [kSecAttrKeyType3DES](ksecattrkeytype3des.md) — 3DES 算法。
- [kSecAttrKeyTypeRC4](ksecattrkeytyperc4.md) — RC4 算法。
- [kSecAttrKeyTypeRC2](ksecattrkeytyperc2.md) — RC2 算法。
- [kSecAttrKeyTypeCAST](ksecattrkeytypecast.md) — CAST 算法。
- [kSecAttrKeyTypeECDSA](ksecattrkeytypeecdsa.md) — 椭圆曲线 DSA 算法。 _(已废弃)_
- [kSecAttrKeyTypeEC](ksecattrkeytypeec.md) — 椭圆曲线算法。 _(已废弃)_
- [kSecAttrKeyTypeECSECPrimeRandom](ksecattrkeytypeecsecprimerandom.md) — 椭圆曲线算法。

### 可同步性值

- [kSecAttrSynchronizableAny](ksecattrsynchronizableany.md) — 指定查询应同时返回可同步和不可同步的结果。

### 令牌 ID 值

- [kSecAttrTokenIDSecureEnclave](ksecattrtokenidsecureenclave.md) — 指定某个条目应存储在设备的安全隔区（Secure Enclave）中。

### 可访问性值

- [kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly](ksecattraccessiblewhenpasscodesetthisdeviceonly.md) — 只有在设备解锁时才能访问钥匙串中的数据。仅在设备设置了密码时可用。
- [kSecAttrAccessibleWhenUnlockedThisDeviceOnly](ksecattraccessiblewhenunlockedthisdeviceonly.md) — 只有当用户解锁设备时，才能访问钥匙串条目中的数据。
- [kSecAttrAccessibleWhenUnlocked](ksecattraccessiblewhenunlocked.md) — 只有当用户解锁设备时，才能访问钥匙串条目中的数据。
- [kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly](ksecattraccessibleafterfirstunlockthisdeviceonly.md) — 设备重启后，直到用户解锁一次设备，才能访问钥匙串条目中的数据。
- [kSecAttrAccessibleAfterFirstUnlock](ksecattraccessibleafterfirstunlock.md) — 设备重启后，直到用户解锁一次设备，才能访问钥匙串条目中的数据。
- [kSecAttrAccessibleAlwaysThisDeviceOnly](ksecattraccessiblealwaysthisdeviceonly.md) — 无论设备是否锁定，都可以随时访问钥匙串条目中的数据。 _(已废弃)_
- [kSecAttrAccessibleAlways](ksecattraccessiblealways.md) — 无论设备是否锁定，都可以随时访问钥匙串条目中的数据。 _(已废弃)_

### 伪随机函数值

- [kSecAttrPRFHmacAlgSHA1](ksecattrprfhmacalgsha1.md) — 使用 SHA1 算法。
- [kSecAttrPRFHmacAlgSHA224](ksecattrprfhmacalgsha224.md) — 使用 SHA224 算法。
- [kSecAttrPRFHmacAlgSHA256](ksecattrprfhmacalgsha256.md) — 使用 SHA256 算法。
- [kSecAttrPRFHmacAlgSHA384](ksecattrprfhmacalgsha384.md) — 使用 SHA384 算法。
- [kSecAttrPRFHmacAlgSHA512](ksecattrprfhmacalgsha512.md) — 使用 SHA512 算法。

### 访问组值

- [kSecAttrAccessGroupToken](ksecattraccessgrouptoken.md) — 包含由外部令牌提供的条目的访问组。
