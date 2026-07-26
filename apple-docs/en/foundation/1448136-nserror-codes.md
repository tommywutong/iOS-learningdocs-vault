---
title: NSError Codes
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Errors and Exceptions](errors-and-exceptions.md) · [NSError](nserror.md)

# NSError Codes

<sub>API Collection</sub>

Error codes in the Cocoa error domain.

## Overview

The constants in this enumeration are [NSError](nserror.md) code numbers in the Cocoa error domain ([NSCocoaErrorDomain](nscocoaerrordomain.md)). Other frameworks, most notably the Application Kit, provide their own [NSCocoaErrorDomain](nscocoaerrordomain.md) error codes.

The enumeration constants beginning with `NSFile` indicate file-system errors or errors related to file I/O operations. Use the key [NSFilePathErrorKey](nsfilepatherrorkey.md) or the [NSURLErrorKey](nsurlerrorkey.md) (whichever is appropriate) to access the file-system path or URL in the [userInfo](nserror/userinfo.md) dictionary of the [NSError](nserror.md) object.

## Topics

### Bundle Errors

- [NSBundleErrorMinimum](nsbundleerrorminimum-swift.var.md) — The start of the range of error codes reserved for bundle errors.
- [NSBundleErrorMaximum](nsbundleerrormaximum-swift.var.md) — The end of the range of error codes reserved for bundle errors.
- [NSBundleOnDemandResourceExceededMaximumSizeError](nsbundleondemandresourceexceededmaximumsizeerror-swift.var.md) — The application exceeded the amount of on-demand resources content in use at one time.
- [NSBundleOnDemandResourceInvalidTagError](nsbundleondemandresourceinvalidtagerror-swift.var.md) — The application specified a tag that the system couldn’t find in the application tag manifest.
- [NSBundleOnDemandResourceOutOfSpaceError](nsbundleondemandresourceoutofspaceerror-swift.var.md) — Insufficient space available to download the requested on-demand resources.

### Cancellation

- [NSUserCancelledError](nsusercancellederror-swift.var.md) — The user canceled the operation (for example, by pressing Command-period).

### Cloud-Sharing Errors

- [NSCloudSharingErrorMinimum](nscloudsharingerrorminimum-swift.var.md) — The start of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingErrorMaximum](nscloudsharingerrormaximum-swift.var.md) — The end of the range of error codes reserved for cloud-sharing errors.
- [NSCloudSharingConflictError](nscloudsharingconflicterror-swift.var.md) — A conflict occurred during an attempt to save changes.
- [NSCloudSharingNetworkFailureError](nscloudsharingnetworkfailureerror-swift.var.md) — Sharing failed due to a network failure.
- [NSCloudSharingNoPermissionError](nscloudsharingnopermissionerror-swift.var.md) — The current user doesn’t have permission to perform the requested actions.
- [NSCloudSharingOtherError](nscloudsharingothererror-swift.var.md) — An otherwise unspecified cloud-sharing error occurred.
- [NSCloudSharingQuotaExceededError](nscloudsharingquotaexceedederror-swift.var.md) — The user doesn’t have enough storage space available to share the requested items.
- [NSCloudSharingTooManyParticipantsError](nscloudsharingtoomanyparticipantserror-swift.var.md) — Additional participants couldn’t be added to the share, because the limit was reached.

### Coder Errors

- [NSCoderErrorMinimum](nscodererrorminimum-swift.var.md) — The start of the range of error codes reserved for coder errors.
- [NSCoderErrorMaximum](nscodererrormaximum-swift.var.md) — The end of the range of error codes reserved for coder errors.
- [NSCoderValueNotFoundError](nscodervaluenotfounderror-swift.var.md) — The requested data wasn’t found.
- [NSCoderReadCorruptError](nscoderreadcorrupterror-swift.var.md) — Decoding failed due to corrupt data.

### Executable Errors

- [NSExecutableErrorMinimum](nsexecutableerrorminimum-swift.var.md) — The beginning of the range of error codes reserved for errors related to executable files.
- [NSExecutableErrorMaximum](nsexecutableerrormaximum-swift.var.md) — The end of the range of error codes reserved for errors related to executable files.
- [NSExecutableArchitectureMismatchError](nsexecutablearchitecturemismatcherror-swift.var.md) — The executable doesn’t provide an architecture compatible with the current process.
- [NSExecutableLinkError](nsexecutablelinkerror-swift.var.md) — The executable failed due to linking issues.
- [NSExecutableLoadError](nsexecutableloaderror-swift.var.md) — Executable cannot be loaded for an otherwise-unspecified reason.
- [NSExecutableNotLoadableError](nsexecutablenotloadableerror-swift.var.md) — The executable type isn’t loadable in the current process.
- [NSExecutableRuntimeMismatchError](nsexecutableruntimemismatcherror-swift.var.md) — The executable has Objective-C runtime information that’s incompatible with the current process.

### Formatting Errors

- [NSFormattingErrorMinimum](nsformattingerrorminimum-swift.var.md) — The start of the range of error codes reserved for formatting errors.
- [NSFormattingErrorMaximum](nsformattingerrormaximum-swift.var.md) — The end of the range of error codes reserved for formatting errors.
- [NSFormattingError](nsformattingerror-swift.var.md) — A formatter couldn’t generate a string for an object, or parse a string into an object.

### File Errors

- [NSFileErrorMinimum](nsfileerrorminimum-swift.var.md) — The start of the range of error codes reserved for file errors.
- [NSFileErrorMaximum](nsfileerrormaximum-swift.var.md) — The end of the range of error codes reserved for file errors.
- [NSFileLockingError](nsfilelockingerror-swift.var.md) — The file could not be locked.
- [NSFileManagerUnmountBusyError](nsfilemanagerunmountbusyerror-swift.var.md) — The volume couldn’t be unmounted because it’s in use.
- [NSFileManagerUnmountUnknownError](nsfilemanagerunmountunknownerror-swift.var.md) — The volume couldn’t be unmounted, for unknown reasons.
- [NSFileNoSuchFileError](nsfilenosuchfileerror-swift.var.md) — A filesystem operation was attempted on a non-existent file.

### File Reading Errors

- [NSFileReadCorruptFileError](nsfilereadcorruptfileerror-swift.var.md) — Could not read because of a corrupted file, bad format, or similar reason.
- [NSFileReadInapplicableStringEncodingError](nsfilereadinapplicablestringencodingerror-swift.var.md) — Could not read because the string encoding wasn’t applicable.
- [NSFileReadInvalidFileNameError](nsfilereadinvalidfilenameerror-swift.var.md) — Could not read because of an invalid file name.
- [NSFileReadNoPermissionError](nsfilereadnopermissionerror-swift.var.md) — Could not read because of a permission problem.
- [NSFileReadNoSuchFileError](nsfilereadnosuchfileerror-swift.var.md) — Could not read because no such file was found.
- [NSFileReadTooLargeError](nsfilereadtoolargeerror-swift.var.md) — Could not read because the specified file was too large.
- [NSFileReadUnknownError](nsfilereadunknownerror-swift.var.md) — Could not read, for unknown reasons.
- [NSFileReadUnknownStringEncodingError](nsfilereadunknownstringencodingerror-swift.var.md) — Could not read because the string coding of the file couldn’t be determined.
- [NSFileReadUnsupportedSchemeError](nsfilereadunsupportedschemeerror-swift.var.md) — Could not read because the specified URL scheme is unsupported.

### File Writing Errors

- [NSFileWriteFileExistsError](nsfilewritefileexistserror-swift.var.md) — Could not perform an operation because the destination file already exists.
- [NSFileWriteInapplicableStringEncodingError](nsfilewriteinapplicablestringencodingerror-swift.var.md) — Could not write because the string encoding was not applicable.
- [NSFileWriteInvalidFileNameError](nsfilewriteinvalidfilenameerror-swift.var.md) — Could not write because of an invalid file name.
- [NSFileWriteNoPermissionError](nsfilewritenopermissionerror-swift.var.md) — Could not write because of a permission problem.
- [NSFileWriteOutOfSpaceError](nsfilewriteoutofspaceerror-swift.var.md) — Could not write because of a lack of disk space.
- [NSFileWriteUnknownError](nsfilewriteunknownerror-swift.var.md) — Could not write, for unknown reasons.
- [NSFileWriteUnsupportedSchemeError](nsfilewriteunsupportedschemeerror-swift.var.md) — Could not write because the specified URL scheme is unsupported.
- [NSFileWriteVolumeReadOnlyError](nsfilewritevolumereadonlyerror-swift.var.md) — Could not write because the volume is read-only.

### iCloud File Errors

- [NSUbiquitousFileErrorMinimum](nsubiquitousfileerrorminimum-swift.var.md) — The minimum error code value that represents an iCloud error.
- [NSUbiquitousFileErrorMaximum](nsubiquitousfileerrormaximum-swift.var.md) — The maximum error code value that represents an iCloud error.
- [NSUbiquitousFileNotUploadedDueToQuotaError](nsubiquitousfilenotuploadedduetoquotaerror-swift.var.md) — The item could not be uploaded to iCloud because it would make the account go over its quota.
- [NSUbiquitousFileUbiquityServerNotAvailable](nsubiquitousfileubiquityservernotavailable-swift.var.md) — A failure to connect to the iCloud servers.
- [NSUbiquitousFileUnavailableError](nsubiquitousfileunavailableerror-swift.var.md) — The item has not been uploaded to iCloud by another device yet.

### Property List Errors

- [NSPropertyListErrorMinimum](nspropertylisterrorminimum-swift.var.md) — The start of the range of error codes reserved for property list errors.
- [NSPropertyListErrorMaximum](nspropertylisterrormaximum-swift.var.md) — The end of the range of error codes reserved for property list errors.
- [NSPropertyListReadCorruptError](nspropertylistreadcorrupterror-swift.var.md) — Parsing of the property list failed.
- [NSPropertyListReadStreamError](nspropertylistreadstreamerror-swift.var.md) — Reading of the property list failed.
- [NSPropertyListReadUnknownVersionError](nspropertylistreadunknownversionerror-swift.var.md) — The version number of the property list cannot be determined.
- [NSPropertyListWriteInvalidError](nspropertylistwriteinvaliderror-swift.var.md) — Writing failed because of an invalid property list object, or an invalid property list type was specified.
- [NSPropertyListWriteStreamError](nspropertylistwritestreamerror-swift.var.md) — Writing to the property list failed.

### User Activity Errors

- [NSUserActivityErrorMinimum](nsuseractivityerrorminimum-swift.var.md) — The start of the range of error codes reserved for user activity errors.
- [NSUserActivityErrorMaximum](nsuseractivityerrormaximum-swift.var.md) — The end of the range of error codes reserved for user activity errors.
- [NSUserActivityConnectionUnavailableError](nsuseractivityconnectionunavailableerror-swift.var.md) — The user activity couldn’t be continued because a required connection wasn’t available.
- [NSUserActivityHandoffFailedError](nsuseractivityhandofffailederror-swift.var.md) — The data for the user activity wasn’t available.
- [NSUserActivityHandoffUserInfoTooLargeError](nsuseractivityhandoffuserinfotoolargeerror-swift.var.md) — The user info dictionary was too large to receive.
- [NSUserActivityRemoteApplicationTimedOutError](nsuseractivityremoteapplicationtimedouterror-swift.var.md) — The remote application failed to send data within the specified time.

### Validation Errors

- [NSValidationErrorMinimum](nsvalidationerrorminimum-swift.var.md) — The start of the range of error codes reserved for validation errors.
- [NSValidationErrorMaximum](nsvalidationerrormaximum-swift.var.md) — The end of the range of error codes reserved for validation errors.

### XPC Errors

- [NSXPCConnectionErrorMinimum](nsxpcconnectionerrorminimum-swift.var.md) — The lower bounds of XPC connection error code values.
- [NSXPCConnectionErrorMaximum](nsxpcconnectionerrormaximum-swift.var.md) — The upper bounds of XPC connection error code values.
- [NSXPCConnectionInterrupted](nsxpcconnectioninterrupted-swift.var.md) — The XPC connection was interrupted.
- [NSXPCConnectionInvalid](nsxpcconnectioninvalid-swift.var.md) — The XPC connection was invalid.
- [NSXPCConnectionReplyInvalid](nsxpcconnectionreplyinvalid-swift.var.md) — The XPC connection reply was invalid.

### URL Errors

- [NSURLErrorAppTransportSecurityRequiresSecureConnection](nsurlerrorapptransportsecurityrequiressecureconnection-swift.var.md) — App Transport Security disallowed a connection because there is no secure network connection.
- [NSURLErrorBackgroundSessionInUseByAnotherProcess](nsurlerrorbackgroundsessioninusebyanotherprocess-swift.var.md) — An app or app extension attempted to connect to a background session that is already connected to a process.
- [NSURLErrorBackgroundSessionRequiresSharedContainer](nsurlerrorbackgroundsessionrequiressharedcontainer-swift.var.md) — The shared container identifier of the URL session configuration is needed but hasn’t been set.
- [NSURLErrorBackgroundSessionWasDisconnected](nsurlerrorbackgroundsessionwasdisconnected-swift.var.md) — The app is suspended or exits while a background data task is processing.
- [NSURLErrorBadServerResponse](nsurlerrorbadserverresponse-swift.var.md) — The URL Loading System received bad data from the server.
- [NSURLErrorBadURL](nsurlerrorbadurl-swift.var.md) — A malformed URL prevented a URL request from being initiated.
- [NSURLErrorCallIsActive](nsurlerrorcallisactive-swift.var.md) — A connection was attempted while a phone call was active on a network that doesn’t support simultaneous phone and data communication, such as EDGE or GPRS.
- [NSURLErrorCancelled](nsurlerrorcancelled-swift.var.md) — An asynchronous load has been canceled.
- [NSURLErrorCannotCloseFile](nsurlerrorcannotclosefile-swift.var.md) — A download task couldn’t close the downloaded file on disk.
- [NSURLErrorCannotConnectToHost](nsurlerrorcannotconnecttohost-swift.var.md) — An attempt to connect to a host failed.
- [NSURLErrorCannotCreateFile](nsurlerrorcannotcreatefile-swift.var.md) — A download task couldn’t create the downloaded file on disk because of an I/O failure.
- [NSURLErrorCannotDecodeContentData](nsurlerrorcannotdecodecontentdata-swift.var.md) — Content data received during a connection request had an unknown content encoding.
- [NSURLErrorCannotDecodeRawData](nsurlerrorcannotdecoderawdata-swift.var.md) — Content data received during a connection request couldn’t be decoded for a known content encoding.
- [NSURLErrorCannotFindHost](nsurlerrorcannotfindhost-swift.var.md) — The host name for a URL couldn’t be resolved.
- [NSURLErrorCannotLoadFromNetwork](nsurlerrorcannotloadfromnetwork-swift.var.md) — A specific request to load an item only from the cache couldn’t be satisfied.
- [NSURLErrorCannotMoveFile](nsurlerrorcannotmovefile-swift.var.md) — A downloaded file on disk couldn’t be moved.
- [NSURLErrorCannotOpenFile](nsurlerrorcannotopenfile-swift.var.md) — A downloaded file on disk couldn’t be opened.
- [NSURLErrorCannotParseResponse](nsurlerrorcannotparseresponse-swift.var.md) — A response to a connection request couldn’t be parsed.
- [NSURLErrorCannotRemoveFile](nsurlerrorcannotremovefile-swift.var.md) — A downloaded file couldn’t be removed from disk.
- [NSURLErrorCannotWriteToFile](nsurlerrorcannotwritetofile-swift.var.md) — A download task couldn’t write the file to disk.
- [NSURLErrorClientCertificateRejected](nsurlerrorclientcertificaterejected-swift.var.md) — A server certificate was rejected.
- [NSURLErrorClientCertificateRequired](nsurlerrorclientcertificaterequired-swift.var.md) — A client certificate was required to authenticate an SSL connection during a connection request.
- [NSURLErrorDNSLookupFailed](nsurlerrordnslookupfailed-swift.var.md) — The host address couldn’t be found via DNS lookup.
- [NSURLErrorDataLengthExceedsMaximum](nsurlerrordatalengthexceedsmaximum-swift.var.md) — The length of the resource data exceeded the maximum allowed.
- [NSURLErrorDataNotAllowed](nsurlerrordatanotallowed-swift.var.md) — The cellular network disallowed a connection.
- [NSURLErrorDownloadDecodingFailedMidStream](nsurlerrordownloaddecodingfailedmidstream-swift.var.md) — A download task failed to decode an encoded file during the download.
- [NSURLErrorDownloadDecodingFailedToComplete](nsurlerrordownloaddecodingfailedtocomplete-swift.var.md) — A download task failed to decode an encoded file after downloading.
- [NSURLErrorFileDoesNotExist](nsurlerrorfiledoesnotexist-swift.var.md) — The specified file doesn’t exist.
- [NSURLErrorFileIsDirectory](nsurlerrorfileisdirectory-swift.var.md) — A request for an FTP file resulted in the server responding that the file is not a plain file, but a directory.
- [NSURLErrorFileOutsideSafeArea](nsurlerrorfileoutsidesafearea-swift.var.md) — An internal file operation failed.
- [NSURLErrorHTTPTooManyRedirects](nsurlerrorhttptoomanyredirects-swift.var.md) — A redirect loop was detected or the threshold for number of allowable redirects was exceeded (currently 16).
- [NSURLErrorInternationalRoamingOff](nsurlerrorinternationalroamingoff-swift.var.md) — The attempted connection required activating a data context while roaming, but international roaming is disabled.
- [NSURLErrorNetworkConnectionLost](nsurlerrornetworkconnectionlost-swift.var.md) — A client or server connection was severed in the middle of an in-progress load.
- [NSURLErrorNoPermissionsToReadFile](nsurlerrornopermissionstoreadfile-swift.var.md) — A resource couldn’t be read because of insufficient permissions.
- [NSURLErrorNotConnectedToInternet](nsurlerrornotconnectedtointernet-swift.var.md) — A network resource was requested, but an internet connection has not been established and can’t be established automatically.
- [NSURLErrorRedirectToNonExistentLocation](nsurlerrorredirecttononexistentlocation-swift.var.md) — A redirect was specified by way of server response code, but the server didn’t accompany this code with a redirect URL.
- [NSURLErrorRequestBodyStreamExhausted](nsurlerrorrequestbodystreamexhausted-swift.var.md) — A body stream was needed but the client did not provide one.
- [NSURLErrorResourceUnavailable](nsurlerrorresourceunavailable-swift.var.md) — A requested resource couldn’t be retrieved.
- [NSURLErrorSecureConnectionFailed](nsurlerrorsecureconnectionfailed-swift.var.md) — An attempt to establish a secure connection failed for reasons that can’t be expressed more specifically.
- [NSURLErrorServerCertificateHasBadDate](nsurlerrorservercertificatehasbaddate-swift.var.md) — A server certificate is expired, or is not yet valid.
- [NSURLErrorServerCertificateHasUnknownRoot](nsurlerrorservercertificatehasunknownroot-swift.var.md) — A server certificate wasn’t signed by any root server.
- [NSURLErrorServerCertificateNotYetValid](nsurlerrorservercertificatenotyetvalid-swift.var.md) — A server certificate isn’t valid yet.
- [NSURLErrorServerCertificateUntrusted](nsurlerrorservercertificateuntrusted-swift.var.md) — A server certificate was signed by a root server that isn’t trusted.
- [NSURLErrorTimedOut](nsurlerrortimedout-swift.var.md) — An asynchronous operation timed out.
- [NSURLErrorUnknown](nsurlerrorunknown-swift.var.md) — The URL Loading System encountered an error that it can’t interpret.
- [NSURLErrorUnsupportedURL](nsurlerrorunsupportedurl-swift.var.md) — A properly formed URL couldn’t be handled by the framework.
- [NSURLErrorUserAuthenticationRequired](nsurlerroruserauthenticationrequired-swift.var.md) — Authentication was required to access a resource.
- [NSURLErrorUserCancelledAuthentication](nsurlerrorusercancelledauthentication-swift.var.md) — An asynchronous request for authentication has been canceled by the user.
- [NSURLErrorZeroByteResource](nsurlerrorzerobyteresource-swift.var.md) — A server reported that a URL has a non-zero content length, but terminated the network connection gracefully without sending any data.

### Miscellaneous Errors

- [NSFeatureUnsupportedError](nsfeatureunsupportederror-swift.var.md) — The feature isn’t supported, because the file system lacks the feature, or required libraries are missing, or other similar reasons.
- [NSKeyValueValidationError](nskeyvaluevalidationerror-swift.var.md) — A key-value coding validation error.

## See Also

### Error Codes

- [CocoaError](cocoaerror.md) — Describes errors within the Cocoa error domain.
- [MachError](macherror.md) — Describes an error in the Mach error domain.
- [POSIXError](posixerror.md) — Describes an error in the POSIX error domain.
