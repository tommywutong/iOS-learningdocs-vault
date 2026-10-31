---
title: Security 框架结果代码
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
translated: true
---

> 导航： [Technologies](../technologies.md) · [Security](../security.md)

# Security 框架结果代码

<sub>API 集合</sub>

评估许多 Security 框架函数共有的结果代码。

## 讨论

使用 [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) 函数获取与这些状态代码相对应的人类可读字符串。

除了这里列出的代码之外，某些 Security 框架服务还提供特定于该服务的附加状态代码。具体而言，参见[授权服务结果代码](authorization-services-result-codes.md)、[Sessions API 结果代码](sessions-api-result-codes.md)、[安全传输结果代码](secure-transport-result-codes.md)、[安全下载结果代码](secure-download-result-codes.md)和[代码签名服务结果代码](code-signing-services-result-codes.md)。

## 主题

### 结果字符串

- [SecCopyErrorMessageString](<seccopyerrormessagestring(____).md>) — 返回一个解释安全结果代码含义的字符串。

### 系统结果代码

- [errSecSuccess](errsecsuccess.md) — 无错误。
- [errSecUnimplemented](errsecunimplemented.md) — 某个函数或操作未实现。
- [errSecDskFull](errsecdskfull.md) — 磁盘已满。 _(已废弃)_
- [errSecDiskFull](errsecdiskfull.md) — 磁盘已满。
- [errSecIO](errsecio.md) — I/O 错误。
- [errSecOpWr](errsecopwr.md) — 该文件已以写入权限打开。
- [errSecParam](errsecparam.md) — 传递给函数的一个或多个参数无效。
- [errSecWrPerm](errsecwrperm.md) — 写入权限错误。
- [errSecAllocate](errsecallocate.md) — 分配内存失败。
- [errSecUserCanceled](errsecusercanceled.md) — 用户取消了该操作。
- [errSecBadReq](errsecbadreq.md) — 操作的参数错误或状态无效。

### 内部错误结果代码

- [errSecInternalComponent](errsecinternalcomponent.md) — 某个内部组件发生了错误。
- [errSecCoreFoundationUnknown](errseccorefoundationunknown.md) — 发生了一个未知的 Core Foundation 错误。
- [errSecInternalError](errsecinternalerror.md) — 发生了一个内部错误。

### 钥匙串结果代码

- [errSecNotAvailable](errsecnotavailable.md) — 没有可用的信任结果。
- [errSecReadOnly](errsecreadonly.md) — 只读错误。
- [errSecAuthFailed](errsecauthfailed.md) — 授权和/或认证失败。
- [errSecNoSuchKeychain](errsecnosuchkeychain.md) — 该钥匙串不存在。
- [errSecInvalidKeychain](errsecinvalidkeychain.md) — 该钥匙串无效。
- [errSecDuplicateKeychain](errsecduplicatekeychain.md) — 已存在一个同名的钥匙串。
- [errSecDuplicateCallback](errsecduplicatecallback.md) — 存在多个同名的回调。
- [errSecInvalidCallback](errsecinvalidcallback.md) — 该回调无效。
- [errSecDuplicateItem](errsecduplicateitem.md) — 该条目已存在。
- [errSecItemNotFound](errsecitemnotfound.md) — 找不到该条目。
- [errSecBufferTooSmall](errsecbuffertoosmall.md) — 缓冲区太小。
- [errSecDataTooLarge](errsecdatatoolarge.md) — 对于该特定数据类型而言，数据过大。
- [errSecNoSuchAttr](errsecnosuchattr.md) — 该属性不存在。
- [errSecInvalidItemRef](errsecinvaliditemref.md) — 该条目引用无效。
- [errSecInvalidSearchRef](errsecinvalidsearchref.md) — 该搜索引用无效。
- [errSecNoSuchClass](errsecnosuchclass.md) — 该钥匙串条目类不存在。
- [errSecNoDefaultKeychain](errsecnodefaultkeychain.md) — 不存在默认钥匙串。
- [errSecInteractionNotAllowed](errsecinteractionnotallowed.md) — 不允许与安全服务器（Security Server）交互。
- [errSecReadOnlyAttr](errsecreadonlyattr.md) — 该属性是只读的。
- [errSecWrongSecVersion](errsecwrongsecversion.md) — 版本不正确。
- [errSecKeySizeNotAllowed](errseckeysizenotallowed.md) — 该密钥大小不被允许。
- [errSecNoStorageModule](errsecnostoragemodule.md) — 没有可用的存储模块。
- [errSecNoCertificateModule](errsecnocertificatemodule.md) — 没有可用的证书模块。
- [errSecNoPolicyModule](errsecnopolicymodule.md) — 没有可用的策略模块。
- [errSecInteractionRequired](errsecinteractionrequired.md) — 需要用户交互。
- [errSecDataNotAvailable](errsecdatanotavailable.md) — 该数据不可用。
- [errSecDataNotModifiable](errsecdatanotmodifiable.md) — 该数据不可修改。
- [errSecCreateChainFailed](errseccreatechainfailed.md) — 创建证书链的尝试失败。
- [errSecInvalidPrefsDomain](errsecinvalidprefsdomain.md) — 指定的偏好设置域无效。
- [errSecInDarkWake](errsecindarkwake.md) — 由于系统处于暗唤醒状态，无法显示用户界面。

### 证书结果代码

- [errSecUnknownCriticalExtensionFlag](errsecunknowncriticalextensionflag.md) — 存在一个未知的关键扩展标志。
- [errSecCertificateCannotOperate](errseccertificatecannotoperate.md) — 该证书无法运作。
- [errSecCertificateExpired](errseccertificateexpired.md) — 检测到一个已过期的证书。
- [errSecCertificateNotValidYet](errseccertificatenotvalidyet.md) — 该证书尚未生效。
- [errSecCertificateRevoked](errseccertificaterevoked.md) — 该证书已被吊销。
- [errSecCertificateSuspended](errseccertificatesuspended.md) — 该证书已被暂停。
- [errSecInvalidCertAuthority](errsecinvalidcertauthority.md) — 该证书颁发机构无效。
- [errSecInvalidCertificateGroup](errsecinvalidcertificategroup.md) — 检测到一个无效的证书组。
- [errSecInvalidCertificateRef](errsecinvalidcertificateref.md) — 检测到一个无效的证书引用。
- [errSecCertificateNameNotAllowed](errseccertificatenamenotallowed.md) — 该证书不允许使用请求的名称。
- [errSecCertificatePolicyNotAllowed](errseccertificatepolicynotallowed.md) — 该证书不允许使用请求的策略。
- [errSecCertificateValidityPeriodTooLong](errseccertificatevalidityperiodtoolong.md) — 证书中的有效期超过了允许的最大期限。

### ACL 结果代码

- [errSecACLAddFailed](errsecacladdfailed.md) — ACL 添加操作失败。
- [errSecACLChangeFailed](errsecaclchangefailed.md) — ACL 更改操作失败。
- [errSecACLDeleteFailed](errsecacldeletefailed.md) — ACL 删除操作失败。
- [errSecACLNotSimple](errsecaclnotsimple.md) — 访问控制列表不是标准的简单形式。
- [errSecACLReplaceFailed](errsecaclreplacefailed.md) — ACL 替换操作失败。
- [errSecAppleAddAppACLSubject](errsecappleaddappaclsubject.md) — 添加应用程序 ACL 主体失败。
- [errSecInvalidBaseACLs](errsecinvalidbaseacls.md) — 基础访问控制列表无效。
- [errSecInvalidACL](errsecinvalidacl.md) — 检测到一个无效的访问控制列表。

### CRL 结果代码

- [errSecCRLExpired](errseccrlexpired.md) — 证书吊销列表已过期。
- [errSecCRLNotValidYet](errseccrlnotvalidyet.md) — 证书吊销列表尚未生效。
- [errSecCRLNotFound](errseccrlnotfound.md) — 未找到证书吊销列表。
- [errSecCRLServerDown](errseccrlserverdown.md) — 证书吊销列表服务器已宕机。
- [errSecCRLBadURI](errseccrlbaduri.md) — 证书吊销列表的统一资源标识符（URI）有误。
- [errSecCRLNotTrusted](errseccrlnottrusted.md) — 证书吊销列表不受信任。
- [errSecUnknownCertExtension](errsecunknowncertextension.md) — 检测到一个未知的证书扩展。
- [errSecUnknownCRLExtension](errsecunknowncrlextension.md) — 检测到一个未知的证书吊销列表扩展。
- [errSecCRLPolicyFailed](errseccrlpolicyfailed.md) — 证书吊销列表策略失败。
- [errSecCRLAlreadySigned](errseccrlalreadysigned.md) — 证书吊销列表已被签名。
- [errSecIDPFailure](errsecidpfailure.md) — 颁发分发点无效。
- [errSecInvalidCRLEncoding](errsecinvalidcrlencoding.md) — 证书吊销列表的编码无效。
- [errSecInvalidCRLType](errsecinvalidcrltype.md) — 证书吊销列表的类型无效。
- [errSecInvalidCRL](errsecinvalidcrl.md) — 证书吊销列表无效。
- [errSecInvalidCRLGroup](errsecinvalidcrlgroup.md) — 检测到一个无效的证书吊销列表组。
- [errSecInvalidCRLIndex](errsecinvalidcrlindex.md) — 证书吊销列表的索引无效。
- [errSecInvaldCRLAuthority](errsecinvaldcrlauthority.md) — 证书吊销列表的颁发机构无效。 _(已废弃)_

### SMIME 结果代码

- [errSecSMIMEEmailAddressesNotFound](errsecsmimeemailaddressesnotfound.md) — 检测到电子邮件地址不匹配。
- [errSecSMIMEBadExtendedKeyUsage](errsecsmimebadextendedkeyusage.md) — 未找到适用于 SMIME 的相应扩展密钥用途。
- [errSecSMIMEBadKeyUsage](errsecsmimebadkeyusage.md) — 密钥用途与 SMIME 不兼容。
- [errSecSMIMEKeyUsageNotCritical](errsecsmimekeyusagenotcritical.md) — 密钥用途扩展未被标记为关键。
- [errSecSMIMENoEmailAddress](errsecsmimenoemailaddress.md) — 在证书中未找到电子邮件地址。
- [errSecSMIMESubjAltNameNotCritical](errsecsmimesubjaltnamenotcritical.md) — 使用者备用名称扩展未被标记为关键。
- [errSecSSLBadExtendedKeyUsage](errsecsslbadextendedkeyusage.md) — 未找到适用于 SSL 的相应扩展密钥用途。

### OCSP 结果代码

- [errSecOCSPBadResponse](errsecocspbadresponse.md) — 在线证书状态协议（OCSP）响应不正确或无法解析。
- [errSecOCSPBadRequest](errsecocspbadrequest.md) — 在线证书状态协议（OCSP）请求不正确或无法解析。
- [errSecOCSPUnavailable](errsecocspunavailable.md) — 在线证书状态协议（OCSP）服务不可用。
- [errSecOCSPStatusUnrecognized](errsecocspstatusunrecognized.md) — 在线证书状态协议（OCSP）服务器无法识别此证书。
- [errSecEndOfData](errsecendofdata.md) — 检测到数据结束。
- [errSecIncompleteCertRevocationCheck](errsecincompletecertrevocationcheck.md) — 发生了一次不完整的证书吊销检查。
- [errSecNetworkFailure](errsecnetworkfailure.md) — 发生了网络故障。
- [errSecOCSPNotTrustedToAnchor](errsecocspnottrustedtoanchor.md) — 在线证书状态协议（OCSP）响应不受某个根证书或锚点证书的信任。
- [errSecRecordModified](errsecrecordmodified.md) — 该记录已被修改。
- [errSecOCSPSignatureError](errsecocspsignatureerror.md) — 在线证书状态协议（OCSP）响应的签名无效。
- [errSecOCSPNoSigner](errsecocspnosigner.md) — 在线证书状态协议（OCSP）响应没有签名者。
- [errSecOCSPResponderMalformedReq](errsecocsprespondermalformedreq.md) — 在线证书状态协议（OCSP）响应者检测到一个格式错误的请求。
- [errSecOCSPResponderInternalError](errsecocspresponderinternalerror.md) — 在线证书状态协议（OCSP）响应者检测到一个内部错误。
- [errSecOCSPResponderTryLater](errsecocsprespondertrylater.md) — 在线证书状态协议（OCSP）响应者正忙，请稍后重试。
- [errSecOCSPResponderSignatureRequired](errsecocsprespondersignaturerequired.md) — 在线证书状态协议（OCSP）响应者要求签名。
- [errSecOCSPResponderUnauthorized](errsecocspresponderunauthorized.md) — 在线证书状态协议（OCSP）响应者以未授权为由拒绝该请求。
- [errSecOCSPResponseNonceMismatch](errsecocspresponsenoncemismatch.md) — 在线证书状态协议（OCSP）响应的现用数（nonce）与请求不匹配。

### 代码签名结果代码

- [errSecCodeSigningBadCertChainLength](errseccodesigningbadcertchainlength.md) — 代码签名遇到了不正确的证书链长度。
- [errSecCodeSigningNoBasicConstraints](errseccodesigningnobasicconstraints.md) — 代码签名未找到基本约束。
- [errSecCodeSigningBadPathLengthConstraint](errseccodesigningbadpathlengthconstraint.md) — 代码签名遇到了不正确的路径长度约束。
- [errSecCodeSigningNoExtendedKeyUsage](errseccodesigningnoextendedkeyusage.md) — 代码签名未找到扩展密钥用途。
- [errSecCodeSigningDevelopment](errseccodesigningdevelopment.md) — 代码签名表明使用了仅限开发用途的证书。
- [errSecResourceSignBadCertChainLength](errsecresourcesignbadcertchainlength.md) — 资源签名检测到不正确的证书链长度。
- [errSecResourceSignBadExtKeyUsage](errsecresourcesignbadextkeyusage.md) — 资源签名检测到扩展密钥用途中的错误。
- [errSecTrustSettingDeny](errsectrustsettingdeny.md) — 该策略的信任设置被设为“拒绝”。
- [errSecInvalidSubjectName](errsecinvalidsubjectname.md) — 检测到一个无效的证书使用者名称。
- [errSecUnknownQualifiedCertStatement](errsecunknownqualifiedcertstatement.md) — 检测到一个未知的合格证书声明。

### Mobile Me 结果代码

- [errSecMobileMeRequestQueued](errsecmobilemerequestqueued.md) — MobileMe 请求将在下一次连接时发送。
- [errSecMobileMeRequestRedirected](errsecmobilemerequestredirected.md) — MobileMe 请求被重定向。
- [errSecMobileMeServerError](errsecmobilemeservererror.md) — 发生了 MobileMe 服务器错误。
- [errSecMobileMeServerNotAvailable](errsecmobilemeservernotavailable.md) — MobileMe 服务器不可用。
- [errSecMobileMeServerAlreadyExists](errsecmobilemeserveralreadyexists.md) — MobileMe 服务器报告该条目已存在。
- [errSecMobileMeServerServiceErr](errsecmobilemeserverserviceerr.md) — 发生了 MobileMe 服务错误。
- [errSecMobileMeRequestAlreadyPending](errsecmobilemerequestalreadypending.md) — 已有一个 MobileMe 请求正在等待处理。
- [errSecMobileMeNoRequestPending](errsecmobilemenorequestpending.md) — MobileMe 没有正在等待处理的请求。
- [errSecMobileMeCSRVerifyFailure](errsecmobilemecsrverifyfailure.md) — 发生了 MobileMe 证书签名请求验证失败。
- [errSecMobileMeFailedConsistencyCheck](errsecmobilemefailedconsistencycheck.md) — MobileMe 发现一致性检查失败。

### 加密密钥结果代码

- [errSecKeyUsageIncorrect](errseckeyusageincorrect.md) — 密钥用途不正确。
- [errSecKeyBlobTypeIncorrect](errseckeyblobtypeincorrect.md) — 密钥 blob 类型不正确。
- [errSecKeyHeaderInconsistent](errseckeyheaderinconsistent.md) — 密钥头不一致。
- [errSecKeyIsSensitive](errseckeyissensitive.md) — 该密钥必须经过包装（wrap）才能导出。
- [errSecUnsupportedKeyFormat](errsecunsupportedkeyformat.md) — 不支持该密钥头的格式。
- [errSecUnsupportedKeySize](errsecunsupportedkeysize.md) — 不支持该密钥大小。
- [errSecInvalidKeyUsageMask](errsecinvalidkeyusagemask.md) — 密钥用途掩码无效。
- [errSecUnsupportedKeyUsageMask](errsecunsupportedkeyusagemask.md) — 不支持该密钥用途掩码。
- [errSecInvalidKeyAttributeMask](errsecinvalidkeyattributemask.md) — 密钥属性掩码无效。
- [errSecUnsupportedKeyAttributeMask](errsecunsupportedkeyattributemask.md) — 不支持该密钥属性掩码。
- [errSecInvalidKeyLabel](errsecinvalidkeylabel.md) — 密钥标签无效。
- [errSecUnsupportedKeyLabel](errsecunsupportedkeylabel.md) — 不支持该密钥标签。
- [errSecInvalidKeyFormat](errsecinvalidkeyformat.md) — 密钥格式无效。
- [errSecInvalidKeyBlob](errsecinvalidkeyblob.md) — 指定的数据库包含无效的密钥 blob。
- [errSecInvalidKeyHierarchy](errsecinvalidkeyhierarchy.md) — 检测到一个无效的密钥层级结构。
- [errSecInvalidKeyRef](errsecinvalidkeyref.md) — 遇到了一个无效的密钥。
- [errSecInvalidKeyUsageForPolicy](errsecinvalidkeyusageforpolicy.md) — 对于指定的策略而言，密钥用途无效。

### 无效属性结果代码

- [errSecInvalidAttributeKey](errsecinvalidattributekey.md) — 密钥属性无效。
- [errSecInvalidAttributeInitVector](errsecinvalidattributeinitvector.md) — 初始化向量属性无效。
- [errSecInvalidAttributeSalt](errsecinvalidattributesalt.md) — 盐值属性无效。
- [errSecInvalidAttributePadding](errsecinvalidattributepadding.md) — 填充属性无效。
- [errSecInvalidAttributeRandom](errsecinvalidattributerandom.md) — 随机数属性无效。
- [errSecInvalidAttributeSeed](errsecinvalidattributeseed.md) — 种子属性无效。
- [errSecInvalidAttributePassphrase](errsecinvalidattributepassphrase.md) — 密码短语属性无效。
- [errSecInvalidAttributeKeyLength](errsecinvalidattributekeylength.md) — 密钥长度属性无效。
- [errSecInvalidAttributeBlockSize](errsecinvalidattributeblocksize.md) — 块大小属性无效。
- [errSecInvalidAttributeOutputSize](errsecinvalidattributeoutputsize.md) — 输出大小属性无效。
- [errSecInvalidAttributeRounds](errsecinvalidattributerounds.md) — 轮数属性无效。
- [errSecInvalidAlgorithmParms](errsecinvalidalgorithmparms.md) — 算法参数属性无效。
- [errSecInvalidAttributeLabel](errsecinvalidattributelabel.md) — 标签属性无效。
- [errSecInvalidAttributeKeyType](errsecinvalidattributekeytype.md) — 密钥类型属性无效。
- [errSecInvalidAttributeMode](errsecinvalidattributemode.md) — 模式属性无效。
- [errSecInvalidAttributeEffectiveBits](errsecinvalidattributeeffectivebits.md) — 有效位数属性无效。
- [errSecInvalidAttributeStartDate](errsecinvalidattributestartdate.md) — 起始日期属性无效。
- [errSecInvalidAttributeEndDate](errsecinvalidattributeenddate.md) — 结束日期属性无效。
- [errSecInvalidAttributeVersion](errsecinvalidattributeversion.md) — 版本属性无效。
- [errSecInvalidAttributePrime](errsecinvalidattributeprime.md) — 素数属性无效。
- [errSecInvalidAttributeBase](errsecinvalidattributebase.md) — 基数属性无效。
- [errSecInvalidAttributeSubprime](errsecinvalidattributesubprime.md) — 子素数属性无效。
- [errSecInvalidAttributeIterationCount](errsecinvalidattributeiterationcount.md) — 迭代计数属性无效。
- [errSecInvalidAttributeDLDBHandle](errsecinvalidattributedldbhandle.md) — 数据库句柄属性无效。
- [errSecInvalidAttributeAccessCredentials](errsecinvalidattributeaccesscredentials.md) — 访问凭据属性无效。
- [errSecInvalidAttributePublicKeyFormat](errsecinvalidattributepublickeyformat.md) — 公钥格式属性无效。
- [errSecInvalidAttributePrivateKeyFormat](errsecinvalidattributeprivatekeyformat.md) — 私钥格式属性无效。
- [errSecInvalidAttributeSymmetricKeyFormat](errsecinvalidattributesymmetrickeyformat.md) — 对称密钥格式属性无效。
- [errSecInvalidAttributeWrappedKeyFormat](errsecinvalidattributewrappedkeyformat.md) — 包装密钥格式属性无效。

### 缺失属性结果代码

- [errSecMissingAttributeKey](errsecmissingattributekey.md) — 缺少密钥属性。
- [errSecMissingAttributeInitVector](errsecmissingattributeinitvector.md) — 缺少初始化向量属性。
- [errSecMissingAttributeSalt](errsecmissingattributesalt.md) — 缺少盐值属性。
- [errSecMissingAttributePadding](errsecmissingattributepadding.md) — 缺少填充属性。
- [errSecMissingAttributeRandom](errsecmissingattributerandom.md) — 缺少随机数属性。
- [errSecMissingAttributeSeed](errsecmissingattributeseed.md) — 缺少种子属性。
- [errSecMissingAttributePassphrase](errsecmissingattributepassphrase.md) — 缺少密码短语属性。
- [errSecMissingAttributeKeyLength](errsecmissingattributekeylength.md) — 缺少密钥长度属性。
- [errSecMissingAttributeBlockSize](errsecmissingattributeblocksize.md) — 缺少块大小属性。
- [errSecMissingAttributeOutputSize](errsecmissingattributeoutputsize.md) — 缺少输出大小属性。
- [errSecMissingAttributeRounds](errsecmissingattributerounds.md) — 缺少轮数属性。
- [errSecMissingAlgorithmParms](errsecmissingalgorithmparms.md) — 缺少算法参数属性。
- [errSecMissingAttributeLabel](errsecmissingattributelabel.md) — 缺少标签属性。
- [errSecMissingAttributeKeyType](errsecmissingattributekeytype.md) — 缺少密钥类型属性。
- [errSecMissingAttributeMode](errsecmissingattributemode.md) — 缺少模式属性。
- [errSecMissingAttributeEffectiveBits](errsecmissingattributeeffectivebits.md) — 缺少有效位数属性。
- [errSecMissingAttributeStartDate](errsecmissingattributestartdate.md) — 缺少起始日期属性。
- [errSecMissingAttributeEndDate](errsecmissingattributeenddate.md) — 缺少结束日期属性。
- [errSecMissingAttributeVersion](errsecmissingattributeversion.md) — 缺少版本属性。
- [errSecMissingAttributePrime](errsecmissingattributeprime.md) — 缺少素数属性。
- [errSecMissingAttributeBase](errsecmissingattributebase.md) — 缺少基数属性。
- [errSecMissingAttributeSubprime](errsecmissingattributesubprime.md) — 缺少子素数属性。
- [errSecMissingAttributeIterationCount](errsecmissingattributeiterationcount.md) — 缺少迭代计数属性。
- [errSecMissingAttributeDLDBHandle](errsecmissingattributedldbhandle.md) — 缺少数据库句柄属性。
- [errSecMissingAttributeAccessCredentials](errsecmissingattributeaccesscredentials.md) — 缺少访问凭据属性。
- [errSecMissingAttributePublicKeyFormat](errsecmissingattributepublickeyformat.md) — 缺少公钥格式属性。
- [errSecMissingAttributePrivateKeyFormat](errsecmissingattributeprivatekeyformat.md) — 缺少私钥格式属性。
- [errSecMissingAttributeSymmetricKeyFormat](errsecmissingattributesymmetrickeyformat.md) — 缺少对称密钥格式属性。
- [errSecMissingAttributeWrappedKeyFormat](errsecmissingattributewrappedkeyformat.md) — 缺少包装密钥格式属性。

### 时间戳结果代码

- [errSecTimestampMissing](errsectimestampmissing.md) — 应有一个时间戳，但未找到。
- [errSecTimestampInvalid](errsectimestampinvalid.md) — 该时间戳无效。
- [errSecTimestampNotTrusted](errsectimestampnottrusted.md) — 该时间戳不受信任。
- [errSecTimestampServiceNotAvailable](errsectimestampservicenotavailable.md)
- [errSecTimestampBadAlg](errsectimestampbadalg.md) — 在时间戳中发现了无法识别或不受支持的算法标识符（AI）。
- [errSecTimestampBadRequest](errsectimestampbadrequest.md) — 该时间戳事务不被允许或不受支持。
- [errSecTimestampBadDataFormat](errsectimestampbaddataformat.md) — 提交的时间戳数据格式错误。
- [errSecTimestampTimeNotAvailable](errsectimestamptimenotavailable.md) — 时间戳颁发机构的时间源不可用。
- [errSecTimestampUnacceptedPolicy](errsectimestampunacceptedpolicy.md) — 时间戳颁发机构不支持请求的策略。
- [errSecTimestampUnacceptedExtension](errsectimestampunacceptedextension.md) — 时间戳颁发机构不支持请求的扩展。
- [errSecTimestampAddInfoNotAvailable](errsectimestampaddinfonotavailable.md) — 请求的附加信息不可用。
- [errSecTimestampSystemFailure](errsectimestampsystemfailure.md) — 由于系统故障，无法处理该时间戳请求。
- [errSecSigningTimeMissing](errsecsigningtimemissing.md) — 缺少签名时间。
- [errSecTimestampRejection](errsectimestamprejection.md) — 该时间戳事务被拒绝。
- [errSecTimestampWaiting](errsectimestampwaiting.md) — 该时间戳事务正在等待。
- [errSecTimestampRevocationWarning](errsectimestamprevocationwarning.md) — 已发出时间戳颁发机构吊销警告。
- [errSecTimestampRevocationNotification](errsectimestamprevocationnotification.md) — 已发出时间戳颁发机构吊销通知。

### 无效参数结果代码

- [errSecInvalidAction](errsecinvalidaction.md) — 该操作无效。
- [errSecInvalidAddinFunctionTable](errsecinvalidaddinfunctiontable.md) — 检测到一个无效的外接函数表。
- [errSecInvalidAlgorithm](errsecinvalidalgorithm.md) — 检测到一个无效的算法。
- [errSecInvalidAuthority](errsecinvalidauthority.md) — 该颁发机构无效。
- [errSecInvalidAuthorityKeyID](errsecinvalidauthoritykeyid.md) — 颁发机构密钥 ID 无效。
- [errSecInvalidBundleInfo](errsecinvalidbundleinfo.md) — bundle 信息无效。
- [errSecInvalidContext](errsecinvalidcontext.md) — 检测到一个无效的上下文。
- [errSecInvalidDBList](errsecinvaliddblist.md) — 检测到一个无效的数据库列表。
- [errSecInvalidDBLocation](errsecinvaliddblocation.md) — 数据库位置无效。
- [errSecInvalidData](errsecinvaliddata.md) — 检测到无效数据。
- [errSecInvalidDatabaseBlob](errsecinvaliddatabaseblob.md) — 指定的数据库包含无效的 blob。
- [errSecInvalidDigestAlgorithm](errsecinvaliddigestalgorithm.md) — 检测到一个无效的摘要算法。
- [errSecInvalidEncoding](errsecinvalidencoding.md) — 该编码无效。
- [errSecInvalidExtendedKeyUsage](errsecinvalidextendedkeyusage.md) — 扩展密钥用途无效。
- [errSecInvalidFormType](errsecinvalidformtype.md) — 表单类型无效。
- [errSecInvalidGUID](errsecinvalidguid.md) — 检测到一个无效的 GUID。
- [errSecInvalidHandle](errsecinvalidhandle.md) — 遇到了一个无效的句柄。
- [errSecInvalidHandleUsage](errsecinvalidhandleusage.md) — 通用安全服务管理器句柄与服务类型不匹配。
- [errSecInvalidID](errsecinvalidid.md) — 该 ID 无效。
- [errSecInvalidIDLinkage](errsecinvalididlinkage.md) — 该 ID 关联无效。
- [errSecInvalidIdentifier](errsecinvalididentifier.md) — 该标识符无效。
- [errSecInvalidIndex](errsecinvalidindex.md) — 该索引无效。
- [errSecInvalidIndexInfo](errsecinvalidindexinfo.md) — 索引信息无效。
- [errSecInvalidInputVector](errsecinvalidinputvector.md) — 输入向量无效。
- [errSecInvalidLoginName](errsecinvalidloginname.md) — 检测到一个无效的登录名。
- [errSecInvalidModifyMode](errsecinvalidmodifymode.md) — 修改模式无效。
- [errSecInvalidName](errsecinvalidname.md) — 检测到一个无效的名称。
- [errSecInvalidNetworkAddress](errsecinvalidnetworkaddress.md) — 检测到一个无效的网络地址。
- [errSecInvalidNewOwner](errsecinvalidnewowner.md) — 新所有者无效。
- [errSecInvalidNumberOfFields](errsecinvalidnumberoffields.md) — 检测到无效的字段数量。
- [errSecInvalidOutputVector](errsecinvalidoutputvector.md) — 输出向量无效。
- [errSecInvalidOwnerEdit](errsecinvalidowneredit.md) — 更改条目所有者的尝试无效。
- [errSecInvalidPVC](errsecinvalidpvc.md) — 检测到一个无效的指针验证检查策略。
- [errSecInvalidParsingModule](errsecinvalidparsingmodule.md) — 解析模块无效。
- [errSecInvalidPassthroughID](errsecinvalidpassthroughid.md) — 检测到一个无效的直通 ID。
- [errSecInvalidPasswordRef](errsecinvalidpasswordref.md) — 密码引用无效。
- [errSecInvalidPointer](errsecinvalidpointer.md) — 检测到一个无效的指针。
- [errSecInvalidPolicyIdentifiers](errsecinvalidpolicyidentifiers.md) — 策略标识符无效。
- [errSecInvalidQuery](errsecinvalidquery.md) — 指定的查询无效。
- [errSecInvalidReason](errsecinvalidreason.md) — 信任策略原因无效。
- [errSecInvalidRecord](errsecinvalidrecord.md) — 检测到一个无效的记录。
- [errSecInvalidRequestInputs](errsecinvalidrequestinputs.md) — 请求输入无效。
- [errSecInvalidRequestor](errsecinvalidrequestor.md) — 请求者无效。
- [errSecInvalidResponseVector](errsecinvalidresponsevector.md) — 响应向量无效。
- [errSecInvalidRoot](errsecinvalidroot.md) — 根证书或锚点证书无效。
- [errSecInvalidSampleValue](errsecinvalidsamplevalue.md) — 检测到一个无效的样本值。
- [errSecInvalidScope](errsecinvalidscope.md) — 检测到一个无效的作用域。
- [errSecInvalidServiceMask](errsecinvalidservicemask.md) — 检测到一个无效的服务掩码。
- [errSecInvalidSignature](errsecinvalidsignature.md) — 检测到一个无效的签名。
- [errSecInvalidStopOnPolicy](errsecinvalidstoponpolicy.md) — stop-on 策略无效。
- [errSecInvalidSubServiceID](errsecinvalidsubserviceid.md) — 检测到一个无效的子服务 ID。
- [errSecInvalidSubjectKeyID](errsecinvalidsubjectkeyid.md) — 使用者密钥 ID 无效。
- [errSecInvalidTimeString](errsecinvalidtimestring.md) — 指定的时间无效。
- [errSecInvalidTrustSetting](errsecinvalidtrustsetting.md) — 信任设置无效。
- [errSecInvalidTrustSettings](errsecinvalidtrustsettings.md) — 信任设置记录已损坏。
- [errSecInvalidTuple](errsecinvalidtuple.md) — 该元组无效。
- [errSecInvalidTupleCredendtials](errsecinvalidtuplecredendtials.md) — 元组凭据无效。 _(已废弃)_
- [errSecInvalidTupleGroup](errsecinvalidtuplegroup.md) — 该元组组无效。
- [errSecInvalidValidityPeriod](errsecinvalidvalidityperiod.md) — 有效期无效。
- [errSecInvalidValue](errsecinvalidvalue.md) — 检测到一个无效的值。

### 不支持的输入结果代码

- [errSecUnsupportedAddressType](errsecunsupportedaddresstype.md) — 不支持该地址类型。
- [errSecUnsupportedFieldFormat](errsecunsupportedfieldformat.md) — 不支持该字段格式。
- [errSecUnsupportedFormat](errsecunsupportedformat.md) — 不支持指定的导入或导出格式。
- [errSecUnsupportedIndexInfo](errsecunsupportedindexinfo.md) — 不支持该索引信息。
- [errSecUnsupportedLocality](errsecunsupportedlocality.md) — 不支持该地区信息。
- [errSecUnsupportedNumAttributes](errsecunsupportednumattributes.md) — 不支持该属性数量。
- [errSecUnsupportedNumIndexes](errsecunsupportednumindexes.md) — 不支持该索引数量。
- [errSecUnsupportedNumRecordTypes](errsecunsupportednumrecordtypes.md) — 不支持该记录类型数量。
- [errSecUnsupportedNumSelectionPreds](errsecunsupportednumselectionpreds.md) — 不支持该选择谓词数量。
- [errSecUnsupportedOperator](errsecunsupportedoperator.md) — 不支持该运算符。
- [errSecUnsupportedQueryLimits](errsecunsupportedquerylimits.md) — 不支持该查询限制。
- [errSecUnsupportedService](errsecunsupportedservice.md) — 不支持该服务。
- [errSecUnsupportedVectorOfBuffers](errsecunsupportedvectorofbuffers.md) — 不支持该缓冲区向量。

### Apple 专属结果代码

- [errSecAppleInvalidKeyEndDate](errsecappleinvalidkeyenddate.md) — 指定的密钥的结束日期无效。
- [errSecAppleInvalidKeyStartDate](errsecappleinvalidkeystartdate.md) — 指定的密钥的起始日期无效。
- [errSecApplePublicKeyIncomplete](errsecapplepublickeyincomplete.md) — 公钥不完整。
- [errSecAppleSSLv2Rollback](errsecapplesslv2rollback.md) — 发生了 SSLv2 回退错误。
- [errSecAppleSignatureMismatch](errsecapplesignaturemismatch.md) — 发生了签名不匹配。

### 模块管理器结果代码

- [errSecEMMLoadFailed](errsecemmloadfailed.md) — 可选模块管理器加载失败。
- [errSecEMMUnloadFailed](errsecemmunloadfailed.md) — 可选模块管理器卸载失败。
- [errSecModuleManagerInitializeFailed](errsecmodulemanagerinitializefailed.md) — 某个模块初始化失败。
- [errSecModuleManagerNotFound](errsecmodulemanagernotfound.md) — 未找到某个模块。
- [errSecModuleManifestVerifyFailed](errsecmodulemanifestverifyfailed.md) — 发生了模块清单验证失败。
- [errSecModuleNotLoaded](errsecmodulenotloaded.md) — 某个模块未被加载。

### 其他结果代码

- [errSecAddinLoadFailed](errsecaddinloadfailed.md) — 外接组件加载操作失败。
- [errSecAddinUnloadFailed](errsecaddinunloadfailed.md) — 外接组件卸载操作失败。
- [errSecAlgorithmMismatch](errsecalgorithmmismatch.md) — 发生了算法不匹配。
- [errSecAlreadyLoggedIn](errsecalreadyloggedin.md) — 用户已经登录。
- [errSecAttachHandleBusy](errsecattachhandlebusy.md) — CSP 句柄正忙。
- [errSecAttributeNotInContext](errsecattributenotincontext.md) — 上下文中没有该属性。
- [errSecBlockSizeMismatch](errsecblocksizemismatch.md) — 发生了块大小不匹配。
- [errSecCallbackFailed](errseccallbackfailed.md) — 某个回调失败。
- [errSecConversionError](errsecconversionerror.md) — 发生了一个转换错误。
- [errSecDatabaseLocked](errsecdatabaselocked.md) — 数据库已锁定。
- [errSecDatastoreIsOpen](errsecdatastoreisopen.md) — 数据存储已打开。
- [errSecDecode](errsecdecode.md) — 无法解码提供的数据。
- [errSecDeviceError](errsecdeviceerror.md) — 遇到了一个设备错误。
- [errSecDeviceFailed](errsecdevicefailed.md) — 发生了设备故障。
- [errSecDeviceReset](errsecdevicereset.md) — 发生了一次设备重置。
- [errSecDeviceVerifyFailed](errsecdeviceverifyfailed.md) — 发生了设备验证失败。
- [errSecEventNotificationCallbackNotFound](errseceventnotificationcallbacknotfound.md) — 未找到事件通知回调。
- [errSecExtendedKeyUsageNotCritical](errsecextendedkeyusagenotcritical.md) — 扩展密钥用途扩展未被标记为关键。
- [errSecFieldSpecifiedMultiple](errsecfieldspecifiedmultiple.md) — 指定的字段过多。
- [errSecFileTooBig](errsecfiletoobig.md) — 文件过大。
- [errSecFunctionFailed](errsecfunctionfailed.md) — 某个函数执行失败。
- [errSecFunctionIntegrityFail](errsecfunctionintegrityfail.md) — 函数地址不在已验证的模块内。
- [errSecHostNameMismatch](errsechostnamemismatch.md) — 发生了主机名不匹配。
- [errSecIncompatibleDatabaseBlob](errsecincompatibledatabaseblob.md) — 指定的数据库包含不兼容的 blob。
- [errSecIncompatibleFieldFormat](errsecincompatiblefieldformat.md) — 字段格式不兼容。
- [errSecIncompatibleKeyBlob](errsecincompatiblekeyblob.md) — 指定的数据库包含不兼容的密钥 blob。
- [errSecIncompatibleVersion](errsecincompatibleversion.md) — 版本不兼容。
- [errSecInputLengthError](errsecinputlengtherror.md) — 发生了输入长度错误。
- [errSecInsufficientClientID](errsecinsufficientclientid.md) — 客户端 ID 不正确。
- [errSecInsufficientCredentials](errsecinsufficientcredentials.md) — 检测到凭据不足。
- [errSecInvalidAccessCredentials](errsecinvalidaccesscredentials.md) — 检测到无效的访问凭据。
- [errSecInvalidAccessRequest](errsecinvalidaccessrequest.md) — 该访问请求无效。
- [errSecLibraryReferenceNotFound](errseclibraryreferencenotfound.md) — 未找到库引用。
- [errSecMDSError](errsecmdserror.md) — 发生了模块目录服务错误。
- [errSecMemoryError](errsecmemoryerror.md) — 发生了内存错误。
- [errSecMissingEntitlement](errsecmissingentitlement.md) — 缺少所需的 entitlement。
- [errSecMissingRequiredExtension](errsecmissingrequiredextension.md) — 缺少所需的证书扩展。
- [errSecMissingValue](errsecmissingvalue.md) — 检测到缺少值。
- [errSecMultiplePrivKeys](errsecmultipleprivkeys.md) — 尝试导入多个私钥。
- [errSecMultipleValuesUnsupported](errsecmultiplevaluesunsupported.md) — 不支持多个值。
- [errSecNoAccessForItem](errsecnoaccessforitem.md) — 指定的条目没有访问控制。
- [errSecNoBasicConstraints](errsecnobasicconstraints.md) — 未找到基本约束。
- [errSecNoBasicConstraintsCA](errsecnobasicconstraintsca.md) — 未找到基本 CA 约束。
- [errSecNoDefaultAuthority](errsecnodefaultauthority.md) — 未检测到默认颁发机构。
- [errSecNoFieldValues](errsecnofieldvalues.md) — 未检测到字段值。
- [errSecNoTrustSettings](errsecnotrustsettings.md) — 未找到信任设置。
- [errSecNotInitialized](errsecnotinitialized.md) — 在未初始化通用安全服务管理器的情况下调用了某个函数。
- [errSecNotLoggedIn](errsecnotloggedin.md) — 你尚未登录。
- [errSecNotSigner](errsecnotsigner.md) — 该证书未由其声称的父证书签名。
- [errSecNotTrusted](errsecnottrusted.md) — 该信任策略不受信任。
- [errSecOutputLengthError](errsecoutputlengtherror.md) — 检测到一个输出长度错误。
- [errSecPVCAlreadyConfigured](errsecpvcalreadyconfigured.md) — PVC 已配置。
- [errSecPVCReferentNotFound](errsecpvcreferentnotfound.md) — 在授权调用者列表中未找到对调用模块的引用。
- [errSecPassphraseRequired](errsecpassphraserequired.md) — 导入或导出需要密码。
- [errSecPathLengthConstraintExceeded](errsecpathlengthconstraintexceeded.md) — 超出了路径长度约束。
- [errSecPkcs12VerifyFailure](errsecpkcs12verifyfailure.md) — PKCS12 导入期间 MAC 验证失败。
- [errSecPolicyNotFound](errsecpolicynotfound.md) — 找不到指定的策略。
- [errSecPrivilegeNotGranted](errsecprivilegenotgranted.md) — 特权未授予。
- [errSecPrivilegeNotSupported](errsecprivilegenotsupported.md) — 不支持该特权。
- [errSecPublicKeyInconsistent](errsecpublickeyinconsistent.md) — 公钥不一致。
- [errSecQuerySizeUnknown](errsecquerysizeunknown.md) — 查询大小未知。
- [errSecQuotaExceeded](errsecquotaexceeded.md) — 超出了配额。
- [errSecRejectedForm](errsecrejectedform.md) — 该信任策略属于被拒绝的形式。
- [errSecRequestDescriptor](errsecrequestdescriptor.md) — 请求描述符无效。
- [errSecRequestLost](errsecrequestlost.md) — 该请求已丢失。
- [errSecRequestRejected](errsecrequestrejected.md) — 该请求被拒绝。
- [errSecSelfCheckFailed](errsecselfcheckfailed.md) — 自检失败。
- [errSecServiceNotAvailable](errsecservicenotavailable.md) — 自检失败。
- [errSecStagedOperationInProgress](errsecstagedoperationinprogress.md) — 某个分阶段操作正在进行中。
- [errSecStagedOperationNotStarted](errsecstagedoperationnotstarted.md) — 某个分阶段操作尚未开始。
- [errSecTagNotFound](errsectagnotfound.md) — 未找到指定的标签。
- [errSecTrustNotAvailable](errsectrustnotavailable.md) — 没有可用的信任结果。
- [errSecUnknownFormat](errsecunknownformat.md) — 你尝试导入的条目格式未知。
- [errSecUnknownTag](errsecunknowntag.md) — 检测到一个未知的标签。
- [errSecVerificationFailure](errsecverificationfailure.md) — 发生了验证失败。
- [errSecVerifyActionFailed](errsecverifyactionfailed.md) — 某个验证操作失败。
- [errSecVerifyFailed](errsecverifyfailed.md) — 发生了加密验证失败。

## 另请参阅

### 相关文档

- [Sessions API Result Codes](sessions-api-result-codes.md) — 识别特定于 sessions API 的结果代码。
- [Secure Transport Result Codes](secure-transport-result-codes.md) — 识别特定于安全传输 API 的结果代码。
- [Code Signing Services Result Codes](code-signing-services-result-codes.md) — 识别特定于代码签名服务 API 的结果代码。
