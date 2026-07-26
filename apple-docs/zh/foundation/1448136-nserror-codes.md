---
title: NSError 代码
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1448136-nserror-codes
source_url: 'https://developer.apple.com/documentation/foundation/1448136-nserror-codes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1448136-nserror-codes.json'
content_hash: 'sha256:b4366f39967aa11a'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Errors and Exceptions](errors-and-exceptions.md) · [NSError](nserror.md)

# NSError 代码

<sub>API 集合</sub>

Cocoa 错误域中的错误代码。

## 概述

该枚举中的常量是 Cocoa 错误域（[NSCocoaErrorDomain](nscocoaerrordomain.md)）中的 [NSError](nserror.md) 代码编号。其他框架，尤其是 Application Kit，也提供了它们各自的 [NSCocoaErrorDomain](nscocoaerrordomain.md) 错误代码。

以 `NSFile` 开头的枚举常量表示文件系统错误，或与文件 I/O 操作相关的错误。请使用键 [NSFilePathErrorKey](nsfilepatherrorkey.md) 或 [NSURLErrorKey](nsurlerrorkey.md)（视具体情况而定），来访问 [NSError](nserror.md) 对象的 [userInfo](nserror/userinfo.md) 字典中的文件系统路径或 URL。

## 主题

### Bundle Errors

- [NSBundleErrorMinimum](nsbundleerrorminimum-swift.var.md) — 为 bundle 错误保留的错误代码范围的起始值。
- [NSBundleErrorMaximum](nsbundleerrormaximum-swift.var.md) — 为 bundle 错误保留的错误代码范围的结束值。
- [NSBundleOnDemandResourceExceededMaximumSizeError](nsbundleondemandresourceexceededmaximumsizeerror-swift.var.md) — App 同时使用的按需资源内容超出了限额。
- [NSBundleOnDemandResourceInvalidTagError](nsbundleondemandresourceinvalidtagerror-swift.var.md) — App 指定了一个系统在 App 标签清单中找不到的标签。
- [NSBundleOnDemandResourceOutOfSpaceError](nsbundleondemandresourceoutofspaceerror-swift.var.md) — 空间不足，无法下载所请求的按需资源。

### Cancellation

- [NSUserCancelledError](nsusercancellederror-swift.var.md) — 用户取消了该操作（例如通过按下 Command-句点）。

### Cloud-Sharing Errors

- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-swift.var.md) — 为云共享错误保留的错误代码范围的起始值。
- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-swift.var.md) — 为云共享错误保留的错误代码范围的结束值。
- [NSCloudSharingConflictError](nscloudsharingconflicterror-swift.var.md) — 在尝试保存更改的过程中发生了冲突。
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-swift.var.md) — 由于网络故障，共享失败。
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-swift.var.md) — 当前用户没有权限执行所请求的操作。
- [NSCloudSharingOtherError](nscloudsharingothererror-swift.var.md) — 发生了一个未另行指明的云共享错误。
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-swift.var.md) — 用户没有足够的可用存储空间来共享所请求的项目。
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-swift.var.md) — 由于已达到人数上限，无法向该共享添加更多参与者。

### Coder Errors

- [NSCoderErrorMinimum](nscodererrorminimum-swift.var.md) — 为编码器错误保留的错误代码范围的起始值。
- [NSCoderErrorMaximum](nscodererrormaximum-swift.var.md) — 为编码器错误保留的错误代码范围的结束值。
- [NSCoderValueNotFoundError](nscodervaluenotfounderror-swift.var.md) — 未找到所请求的数据。
- [NSCoderReadCorruptError](nscoderreadcorrupterror-swift.var.md) — 由于数据损坏，解码失败。

### Executable Errors

- [NSExecutableErrorMinimum](nsexecutableerrorminimum-swift.var.md) — 为与可执行文件相关的错误保留的错误代码范围的起始值。
- [NSExecutableErrorMaximum](nsexecutableerrormaximum-swift.var.md) — 为与可执行文件相关的错误保留的错误代码范围的结束值。
- [NSExecutableArchitectureMismatchError](nsexecutablearchitecturemismatcherror-swift.var.md) — 该可执行文件未提供与当前进程兼容的架构。
- [NSExecutableLinkError](nsexecutablelinkerror-swift.var.md) — 由于链接问题，该可执行文件失败。
- [NSExecutableLoadError](nsexecutableloaderror-swift.var.md) — 由于其他未指明的原因，无法加载该可执行文件。
- [NSExecutableNotLoadableError](nsexecutablenotloadableerror-swift.var.md) — 该可执行文件类型在当前进程中不可加载。
- [NSExecutableRuntimeMismatchError](nsexecutableruntimemismatcherror-swift.var.md) — 该可执行文件包含与当前进程不兼容的 Objective-C 运行时信息。

### Formatting Errors

- [NSFormattingErrorMinimum](nsformattingerrorminimum-swift.var.md) — 为格式化错误保留的错误代码范围的起始值。
- [NSFormattingErrorMaximum](nsformattingerrormaximum-swift.var.md) — 为格式化错误保留的错误代码范围的结束值。
- [NSFormattingError](nsformattingerror-swift.var.md) — 某个格式化器无法为某个对象生成字符串，或者无法将某个字符串解析为对象。

### File Errors

- [NSFileErrorMinimum](nsfileerrorminimum-swift.var.md) — 为文件错误保留的错误代码范围的起始值。
- [NSFileErrorMaximum](nsfileerrormaximum-swift.var.md) — 为文件错误保留的错误代码范围的结束值。
- [NSFileLockingError](nsfilelockingerror-swift.var.md) — 无法锁定该文件。
- [NSFileManagerUnmountBusyError](nsfilemanagerunmountbusyerror-swift.var.md) — 由于该卷正在使用中，无法卸载。
- [NSFileManagerUnmountUnknownError](nsfilemanagerunmountunknownerror-swift.var.md) — 由于未知原因，无法卸载该卷。
- [NSFileNoSuchFileError](nsfilenosuchfileerror-swift.var.md) — 尝试对一个不存在的文件执行文件系统操作。

### File Reading Errors

- [NSFileReadCorruptFileError](nsfilereadcorruptfileerror-swift.var.md) — 由于文件损坏、格式错误或类似原因，无法读取。
- [NSFileReadInapplicableStringEncodingError](nsfilereadinapplicablestringencodingerror-swift.var.md) — 由于字符串编码不适用，无法读取。
- [NSFileReadInvalidFileNameError](nsfilereadinvalidfilenameerror-swift.var.md) — 由于文件名无效，无法读取。
- [NSFileReadNoPermissionError](nsfilereadnopermissionerror-swift.var.md) — 由于权限问题，无法读取。
- [NSFileReadNoSuchFileError](nsfilereadnosuchfileerror-swift.var.md) — 由于找不到该文件，无法读取。
- [NSFileReadTooLargeError](nsfilereadtoolargeerror-swift.var.md) — 由于指定的文件过大，无法读取。
- [NSFileReadUnknownError](nsfilereadunknownerror-swift.var.md) — 由于未知原因，无法读取。
- [NSFileReadUnknownStringEncodingError](nsfilereadunknownstringencodingerror-swift.var.md) — 由于无法确定该文件的字符串编码，无法读取。
- [NSFileReadUnsupportedSchemeError](nsfilereadunsupportedschemeerror-swift.var.md) — 由于指定的 URL scheme 不受支持，无法读取。

### File Writing Errors

- [NSFileWriteFileExistsError](nsfilewritefileexistserror-swift.var.md) — 由于目标文件已存在，无法执行该操作。
- [NSFileWriteInapplicableStringEncodingError](nsfilewriteinapplicablestringencodingerror-swift.var.md) — 由于字符串编码不适用，无法写入。
- [NSFileWriteInvalidFileNameError](nsfilewriteinvalidfilenameerror-swift.var.md) — 由于文件名无效，无法写入。
- [NSFileWriteNoPermissionError](nsfilewritenopermissionerror-swift.var.md) — 由于权限问题，无法写入。
- [NSFileWriteOutOfSpaceError](nsfilewriteoutofspaceerror-swift.var.md) — 由于磁盘空间不足，无法写入。
- [NSFileWriteUnknownError](nsfilewriteunknownerror-swift.var.md) — 由于未知原因，无法写入。
- [NSFileWriteUnsupportedSchemeError](nsfilewriteunsupportedschemeerror-swift.var.md) — 由于指定的 URL scheme 不受支持，无法写入。
- [NSFileWriteVolumeReadOnlyError](nsfilewritevolumereadonlyerror-swift.var.md) — 由于该卷是只读的，无法写入。

### iCloud File Errors

- [NSUbiquitousFileErrorMinimum](nsubiquitousfileerrorminimum-swift.var.md) — 表示 iCloud 错误的最小错误代码值。
- [NSUbiquitousFileErrorMaximum](nsubiquitousfileerrormaximum-swift.var.md) — 表示 iCloud 错误的最大错误代码值。
- [NSUbiquitousFileNotUploadedDueToQuotaError](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md) — 由于会导致账户超出配额，该项目无法上传到 iCloud。
- [NSUbiquitousFileUbiquityServerNotAvailable](nsubiquitousfileubiquityservernotavailable-swift.var.md) — 连接 iCloud 服务器失败。
- [NSUbiquitousFileUnavailableError](nsubiquitousfileunavailableerror-swift.var.md) — 该项目尚未被其他设备上传到 iCloud。

### Property List Errors

- [NSPropertyListErrorMinimum](nspropertylisterrorminimum-swift.var.md) — 为属性列表错误保留的错误代码范围的起始值。
- [NSPropertyListErrorMaximum](nspropertylisterrormaximum-swift.var.md) — 为属性列表错误保留的错误代码范围的结束值。
- [NSPropertyListReadCorruptError](nspropertylistreadcorrupterror-swift.var.md) — 解析该属性列表失败。
- [NSPropertyListReadStreamError](nspropertylistreadstreamerror-swift.var.md) — 读取该属性列表失败。
- [NSPropertyListReadUnknownVersionError](nspropertylistreadunknownversionerror-swift.var.md) — 无法确定该属性列表的版本号。
- [NSPropertyListWriteInvalidError](nspropertylistwriteinvaliderror-swift.var.md) — 由于属性列表对象无效，或指定了无效的属性列表类型，写入失败。
- [NSPropertyListWriteStreamError](nspropertylistwritestreamerror-swift.var.md) — 写入该属性列表失败。

### User Activity Errors

- [NSUserActivityErrorMinimum](nsuseractivityerrorminimum-swift.var.md) — 为用户活动错误保留的错误代码范围的起始值。
- [NSUserActivityErrorMaximum](nsuseractivityerrormaximum-swift.var.md) — 为用户活动错误保留的错误代码范围的结束值。
- [NSUserActivityConnectionUnavailableError](nsuseractivityconnectionunavailableerror-swift.var.md) — 由于所需的连接不可用，无法继续该用户活动。
- [NSUserActivityHandoffFailedError](nsuseractivityhandofffailederror-swift.var.md) — 该用户活动的数据不可用。
- [NSUserActivityHandoffUserInfoTooLargeError](nsuseractivityhandoffuserinfotoolargeerror-swift.var.md) — 该用户信息字典过大，无法接收。
- [NSUserActivityRemoteApplicationTimedOutError](nsuseractivityremoteapplicationtimedouterror-swift.var.md) — 远程应用程序未能在指定时间内发送数据。

### Validation Errors

- [NSValidationErrorMinimum](nsvalidationerrorminimum-swift.var.md) — 为验证错误保留的错误代码范围的起始值。
- [NSValidationErrorMaximum](nsvalidationerrormaximum-swift.var.md) — 为验证错误保留的错误代码范围的结束值。

### XPC Errors

- [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-swift.var.md) — XPC 连接错误代码值的下限。
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md) — XPC 连接错误代码值的上限。
- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-swift.var.md) — 该 XPC 连接被中断。
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-swift.var.md) — 该 XPC 连接无效。
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-swift.var.md) — 该 XPC 连接的回复无效。

### URL Errors

- [NSURLErrorAppTransportSecurityRequiresSecureConnection](nsurlerrorapptransportsecurityrequiressecureconnection-swift.var.md) — 由于没有安全的网络连接，App Transport Security 禁止了该连接。
- [NSURLErrorBackgroundSessionInUseByAnotherProcess](nsurlerrorbackgroundsessioninusebyanotherprocess-swift.var.md) — 某个 App 或 App 扩展尝试连接到一个已经连接到另一个进程的后台会话。
- [NSURLErrorBackgroundSessionRequiresSharedContainer](nsurlerrorbackgroundsessionrequiressharedcontainer-swift.var.md) — 需要该 URL 会话配置的共享容器标识符，但尚未设置。
- [NSURLErrorBackgroundSessionWasDisconnected](nsurlerrorbackgroundsessionwasdisconnected-swift.var.md) — 在某个后台数据任务处理期间，该 App 被挂起或退出。
- [NSURLErrorBadServerResponse](nsurlerrorbadserverresponse-swift.var.md) — URL Loading System 从服务器收到了错误的数据。
- [NSURLErrorBadURL](nsurlerrorbadurl-swift.var.md) — 格式错误的 URL 导致无法发起某个 URL 请求。
- [NSURLErrorCallIsActive](nsurlerrorcallisactive-swift.var.md) — 在一个不支持同时进行电话和数据通信的网络（例如 EDGE 或 GPRS）上，有电话正在通话时尝试建立连接。
- [NSURLErrorCancelled](nsurlerrorcancelled-swift.var.md) — 某次异步加载已被取消。
- [NSURLErrorCannotCloseFile](nsurlerrorcannotclosefile-swift.var.md) — 某个下载任务无法关闭磁盘上已下载的文件。
- [NSURLErrorCannotConnectToHost](nsurlerrorcannotconnecttohost-swift.var.md) — 尝试连接到某个主机失败。
- [NSURLErrorCannotCreateFile](nsurlerrorcannotcreatefile-swift.var.md) — 由于 I/O 故障，某个下载任务无法在磁盘上创建已下载的文件。
- [NSURLErrorCannotDecodeContentData](nsurlerrorcannotdecodecontentdata-swift.var.md) — 在某次连接请求期间收到的内容数据使用了未知的内容编码。
- [NSURLErrorCannotDecodeRawData](nsurlerrorcannotdecoderawdata-swift.var.md) — 在某次连接请求期间收到的内容数据无法按照某种已知的内容编码进行解码。
- [NSURLErrorCannotFindHost](nsurlerrorcannotfindhost-swift.var.md) — 无法解析某个 URL 的主机名。
- [NSURLErrorCannotLoadFromNetwork](nsurlerrorcannotloadfromnetwork-swift.var.md) — 无法满足某个仅从缓存加载某项内容的特定请求。
- [NSURLErrorCannotMoveFile](nsurlerrorcannotmovefile-swift.var.md) — 无法移动磁盘上某个已下载的文件。
- [NSURLErrorCannotOpenFile](nsurlerrorcannotopenfile-swift.var.md) — 无法打开磁盘上某个已下载的文件。
- [NSURLErrorCannotParseResponse](nsurlerrorcannotparseresponse-swift.var.md) — 无法解析对某次连接请求的响应。
- [NSURLErrorCannotRemoveFile](nsurlerrorcannotremovefile-swift.var.md) — 无法从磁盘中移除某个已下载的文件。
- [NSURLErrorCannotWriteToFile](nsurlerrorcannotwritetofile-swift.var.md) — 某个下载任务无法将该文件写入磁盘。
- [NSURLErrorClientCertificateRejected](nsurlerrorclientcertificaterejected-swift.var.md) — 某个服务器证书被拒绝。
- [NSURLErrorClientCertificateRequired](nsurlerrorclientcertificaterequired-swift.var.md) — 在某次连接请求期间，需要客户端证书才能验证某个 SSL 连接。
- [NSURLErrorDNSLookupFailed](nsurlerrordnslookupfailed-swift.var.md) — 无法通过 DNS 查找找到该主机地址。
- [NSURLErrorDataLengthExceedsMaximum](nsurlerrordatalengthexceedsmaximum-swift.var.md) — 该资源数据的长度超出了允许的最大值。
- [NSURLErrorDataNotAllowed](nsurlerrordatanotallowed-swift.var.md) — 蜂窝网络禁止了某次连接。
- [NSURLErrorDownloadDecodingFailedMidStream](nsurlerrordownloaddecodingfailedmidstream-swift.var.md) — 某个下载任务在下载过程中未能解码某个已编码的文件。
- [NSURLErrorDownloadDecodingFailedToComplete](nsurlerrordownloaddecodingfailedtocomplete-swift.var.md) — 某个下载任务在下载完成后未能解码某个已编码的文件。
- [NSURLErrorFileDoesNotExist](nsurlerrorfiledoesnotexist-swift.var.md) — 指定的文件不存在。
- [NSURLErrorFileIsDirectory](nsurlerrorfileisdirectory-swift.var.md) — 对某个 FTP 文件的请求导致服务器返回该文件不是一个普通文件，而是一个目录。
- [NSURLErrorFileOutsideSafeArea](nsurlerrorfileoutsidesafearea-swift.var.md) — 某个内部文件操作失败。
- [NSURLErrorHTTPTooManyRedirects](nsurlerrorhttptoomanyredirects-swift.var.md) — 检测到重定向循环，或者超出了允许的重定向次数上限（目前为 16 次）。
- [NSURLErrorInternationalRoamingOff](nsurlerrorinternationalroamingoff-swift.var.md) — 尝试建立的连接需要在漫游期间激活数据上下文，但国际漫游已被禁用。
- [NSURLErrorNetworkConnectionLost](nsurlerrornetworkconnectionlost-swift.var.md) — 在某次加载进行过程中，客户端或服务器的连接中断。
- [NSURLErrorNoPermissionsToReadFile](nsurlerrornopermissionstoreadfile-swift.var.md) — 由于权限不足，无法读取某个资源。
- [NSURLErrorNotConnectedToInternet](nsurlerrornotconnectedtointernet-swift.var.md) — 请求了某个网络资源，但尚未建立互联网连接，且无法自动建立连接。
- [NSURLErrorRedirectToNonExistentLocation](nsurlerrorredirecttononexistentlocation-swift.var.md) — 服务器通过响应代码指定了一次重定向，但服务器没有随该代码提供重定向 URL。
- [NSURLErrorRequestBodyStreamExhausted](nsurlerrorrequestbodystreamexhausted-swift.var.md) — 需要一个正文流，但客户端未提供。
- [NSURLErrorResourceUnavailable](nsurlerrorresourceunavailable-swift.var.md) — 无法获取所请求的资源。
- [NSURLErrorSecureConnectionFailed](nsurlerrorsecureconnectionfailed-swift.var.md) — 由于无法更具体说明的原因，尝试建立安全连接失败。
- [NSURLErrorServerCertificateHasBadDate](nsurlerrorservercertificatehasbaddate-swift.var.md) — 某个服务器证书已过期，或尚未生效。
- [NSURLErrorServerCertificateHasUnknownRoot](nsurlerrorservercertificatehasunknownroot-swift.var.md) — 某个服务器证书未经任何根服务器签名。
- [NSURLErrorServerCertificateNotYetValid](nsurlerrorservercertificatenotyetvalid-swift.var.md) — 某个服务器证书尚未生效。
- [NSURLErrorServerCertificateUntrusted](nsurlerrorservercertificateuntrusted-swift.var.md) — 某个服务器证书由一个不受信任的根服务器签名。
- [NSURLErrorTimedOut](nsurlerrortimedout-swift.var.md) — 某次异步操作超时。
- [NSURLErrorUnknown](nsurlerrorunknown-swift.var.md) — URL Loading System 遇到了一个它无法解读的错误。
- [NSURLErrorUnsupportedURL](nsurlerrorunsupportedurl-swift.var.md) — 该框架无法处理某个格式正确的 URL。
- [NSURLErrorUserAuthenticationRequired](nsurlerroruserauthenticationrequired-swift.var.md) — 访问某个资源需要进行身份验证。
- [NSURLErrorUserCancelledAuthentication](nsurlerrorusercancelledauthentication-swift.var.md) — 用户取消了某次异步身份验证请求。
- [NSURLErrorZeroByteResource](nsurlerrorzerobyteresource-swift.var.md) — 服务器报告某个 URL 的内容长度非零，但在未发送任何数据的情况下正常终止了网络连接。

### Miscellaneous Errors

- [NSFeatureUnsupportedError](nsfeatureunsupportederror-swift.var.md) — 由于文件系统缺少该特性，或缺少所需的库，或其他类似原因，该特性不受支持。
- [NSKeyValueValidationError](nskeyvaluevalidationerror-swift.var.md) — 一个键值编码验证错误。

## 另请参阅

### Error Codes

- [CocoaError](cocoaerror.md) — 描述 Cocoa 错误域中的错误。
- [MachError](macherror.md) — 描述 Mach 错误域中的错误。
- [POSIXError](posixerror.md) — 描述 POSIX 错误域中的错误。
