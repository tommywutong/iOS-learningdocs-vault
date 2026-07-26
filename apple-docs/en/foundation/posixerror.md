---
title: POSIXError
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/posixerror
source_url: 'https://developer.apple.com/documentation/foundation/posixerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/posixerror.json'
content_hash: 'sha256:038b1c7cefdf2b87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# POSIXError

<sub>Structure</sub>

Describes an error in the POSIX error domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct POSIXError
```

## Relationships

- **Conforms To**: [CustomNSError](customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Aliases

- [Code](posixerror/code.md) — The type of an error code.

### Type Properties

- [E2BIG](posixerror/e2big.md) — Argument list too long.
- [EACCES](posixerror/eacces.md) — Permission denied.
- [EADDRINUSE](posixerror/eaddrinuse.md) — Address already in use.
- [EADDRNOTAVAIL](posixerror/eaddrnotavail.md) — Can’t assign requested address.
- [EAFNOSUPPORT](posixerror/eafnosupport.md) — Address family not supported by protocol family.
- [EAGAIN](posixerror/eagain.md) — non-blocking and interrupt i/o. Resource temporarily unavailable.
- [EALREADY](posixerror/ealready.md) — Operation already in progress.
- [EAUTH](posixerror/eauth.md) — Authentication error.
- [EBADARCH](posixerror/ebadarch.md) — Bad CPU type in executable.
- [EBADEXEC](posixerror/ebadexec.md) — Program loading errors. Bad executable.
- [EBADF](posixerror/ebadf.md) — Bad file descriptor.
- [EBADMACHO](posixerror/ebadmacho.md) — Malformed Macho file.
- [EBADMSG](posixerror/ebadmsg.md) — Bad message.
- [EBADRPC](posixerror/ebadrpc.md) — RPC struct is bad.
- [EBUSY](posixerror/ebusy.md) — Device / Resource busy.
- [ECANCELED](posixerror/ecanceled.md) — Operation canceled.
- [ECHILD](posixerror/echild.md) — No child processes.
- [ECONNABORTED](posixerror/econnaborted.md) — Software caused connection abort.
- [ECONNREFUSED](posixerror/econnrefused.md) — Connection refused.
- [ECONNRESET](posixerror/econnreset.md) — Connection reset by peer.
- [EDEADLK](posixerror/edeadlk.md) — Resource deadlock avoided.
- [EDESTADDRREQ](posixerror/edestaddrreq.md) — Destination address required.
- [EDEVERR](posixerror/edeverr.md) — Device error, for example paper out.
- [EDOM](posixerror/edom.md) — math software. Numerical argument out of domain.
- [EDQUOT](posixerror/edquot.md) — Disc quota exceeded.
- [EEXIST](posixerror/eexist.md) — File exists.
- [EFAULT](posixerror/efault.md) — Bad address.
- [EFBIG](posixerror/efbig.md) — File too large.
- [EFTYPE](posixerror/eftype.md) — Inappropriate file type or format.
- [EHOSTDOWN](posixerror/ehostdown.md) — Host is down.
- [EHOSTUNREACH](posixerror/ehostunreach.md) — No route to host.
- [EIDRM](posixerror/eidrm.md) — Identifier removed.
- [EILSEQ](posixerror/eilseq.md) — Illegal byte sequence.
- [EINPROGRESS](posixerror/einprogress.md) — Operation now in progress.
- [EINTR](posixerror/eintr.md) — Interrupted system call.
- [EINVAL](posixerror/einval.md) — Invalid argument.
- [EIO](posixerror/eio.md) — Input/output error.
- [EISCONN](posixerror/eisconn.md) — Socket is already connected.
- [EISDIR](posixerror/eisdir.md) — Is a directory.
- [ELOOP](posixerror/eloop.md) — Too many levels of symbolic links.
- [EMFILE](posixerror/emfile.md) — Too many open files.
- [EMLINK](posixerror/emlink.md) — Too many links.
- [EMSGSIZE](posixerror/emsgsize.md) — Message too long.
- [EMULTIHOP](posixerror/emultihop.md) — Reserved.
- [ENAMETOOLONG](posixerror/enametoolong.md) — File name too long.
- [ENEEDAUTH](posixerror/eneedauth.md) — Need authenticator.
- [ENETDOWN](posixerror/enetdown.md) — ipc/network software – operational errors Network is down.
- [ENETRESET](posixerror/enetreset.md) — Network dropped connection on reset.
- [ENETUNREACH](posixerror/enetunreach.md) — Network is unreachable.
- [ENFILE](posixerror/enfile.md) — Too many open files in system.
- [ENOATTR](posixerror/enoattr.md) — Attribute not found.
- [ENOBUFS](posixerror/enobufs.md) — No buffer space available.
- [ENODATA](posixerror/enodata.md) — No message available on STREAM.
- [ENODEV](posixerror/enodev.md) — Operation not supported by device.
- [ENOENT](posixerror/enoent.md) — No such file or directory.
- [ENOEXEC](posixerror/enoexec.md) — Exec format error.
- [ENOLCK](posixerror/enolck.md) — No locks available.
- [ENOLINK](posixerror/enolink.md) — Reserved.
- [ENOMEM](posixerror/enomem.md) — Cannot allocate memory.
- [ENOMSG](posixerror/enomsg.md) — No message of desired type.
- [ENOPOLICY](posixerror/enopolicy.md) — No such policy registered.
- [ENOPROTOOPT](posixerror/enoprotoopt.md) — Protocol not available.
- [ENOSPC](posixerror/enospc.md) — No space left on device.
- [ENOSR](posixerror/enosr.md) — No STREAM resources.
- [ENOSTR](posixerror/enostr.md) — Not a STREAM.
- [ENOSYS](posixerror/enosys.md) — Function not implemented.
- [ENOTBLK](posixerror/enotblk.md) — Block device required.
- [ENOTCONN](posixerror/enotconn.md) — Socket is not connected.
- [ENOTDIR](posixerror/enotdir.md) — Not a directory.
- [ENOTEMPTY](posixerror/enotempty.md) — Directory not empty.
- [ENOTRECOVERABLE](posixerror/enotrecoverable.md) — State not recoverable.
- [ENOTSOCK](posixerror/enotsock.md) — ipc/network software – argument errors. Socket operation on non-socket.
- [ENOTSUP](posixerror/enotsup.md) — Operation not supported.
- [ENOTTY](posixerror/enotty.md) — Inappropriate ioctl for device.
- [ENXIO](posixerror/enxio.md) — Device not configured.
- [EOVERFLOW](posixerror/eoverflow.md) — Value too large to be stored in data type.
- [EOWNERDEAD](posixerror/eownerdead.md) — Previous owner died.
- [EPERM](posixerror/eperm.md) — Operation not permitted.
- [EPFNOSUPPORT](posixerror/epfnosupport.md) — Protocol family not supported.
- [EPIPE](posixerror/epipe.md) — Broken pipe.
- [EPROCLIM](posixerror/eproclim.md) — quotas & mush. Too many processes.
- [EPROCUNAVAIL](posixerror/eprocunavail.md) — Bad procedure for program.
- [EPROGMISMATCH](posixerror/eprogmismatch.md) — Program version wrong.
- [EPROGUNAVAIL](posixerror/eprogunavail.md) — RPC prog. not avail.
- [EPROTO](posixerror/eproto.md) — Protocol error.
- [EPROTONOSUPPORT](posixerror/eprotonosupport.md) — Protocol not supported.
- [EPROTOTYPE](posixerror/eprototype.md) — Protocol wrong type for socket.
- [EPWROFF](posixerror/epwroff.md) — Intelligent device errors. Device power is off.
- [EQFULL](posixerror/eqfull.md) — Interface output queue is full.
- [ERANGE](posixerror/erange.md) — Result too large.
- [EREMOTE](posixerror/eremote.md) — Too many levels of remote in path.
- [EROFS](posixerror/erofs.md) — Read-only file system.
- [ERPCMISMATCH](posixerror/erpcmismatch.md) — RPC version wrong.
- [ESHLIBVERS](posixerror/eshlibvers.md) — Shared library version mismatch.
- [ESHUTDOWN](posixerror/eshutdown.md) — Can’t send after socket shutdown.
- [ESOCKTNOSUPPORT](posixerror/esocktnosupport.md) — Socket type not supported.
- [ESPIPE](posixerror/espipe.md) — Illegal seek.
- [ESRCH](posixerror/esrch.md) — No such process.
- [ESTALE](posixerror/estale.md) — Network File System. Stale NFS file handle.
- [ETIME](posixerror/etime.md) — STREAM ioctl timeout.
- [ETIMEDOUT](posixerror/etimedout.md) — Operation timed out.
- [ETOOMANYREFS](posixerror/etoomanyrefs.md) — Too many references: can’t splice.
- [ETXTBSY](posixerror/etxtbsy.md) — Text file busy.
- [EUSERS](posixerror/eusers.md) — Too many users.
- [EWOULDBLOCK](posixerror/ewouldblock.md) — Operation would block.
- [EXDEV](posixerror/exdev.md) — Cross-device link.

## See Also

### Error Codes

- [CocoaError](cocoaerror.md) — Describes errors within the Cocoa error domain.
- [MachError](macherror.md) — Describes an error in the Mach error domain.
- [NSError Codes](1448136-nserror-codes.md) — Error codes in the Cocoa error domain.
