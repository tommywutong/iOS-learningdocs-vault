---
title: Core Foundation Functions
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/core-foundation-functions
source_url: 'https://developer.apple.com/documentation/corefoundation/core-foundation-functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/core-foundation-functions.json'
content_hash: 'sha256:8b02bb55c0565072'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# Core Foundation Functions

<sub>API Collection</sub>

## Topics

### Functions

- [CFAllocatorAllocateBytes](<cfallocatorallocatebytes(______).md>)
- [CFAllocatorAllocateTyped](<cfallocatorallocatetyped(________).md>)
- [CFAllocatorReallocateBytes](<cfallocatorreallocatebytes(________).md>)
- [CFAllocatorReallocateTyped](<cfallocatorreallocatetyped(__________).md>)
- [CFAttributedStringGetBidiLevelsAndResolvedDirections](<cfattributedstringgetbidilevelsandresolveddirections(__________).md>)
- [CFBundleCopyLocalizedStringForLocalizations](<cfbundlecopylocalizedstringforlocalizations(__________).md>) — Returns a localized string from a bundle’s strings file.
- [CFBundleIsArchitectureLoadable](<cfbundleisarchitectureloadable(__).md>)
- [CFBundleIsExecutableLoadable](<cfbundleisexecutableloadable(__).md>)
- [CFBundleIsExecutableLoadableForURL](<cfbundleisexecutableloadableforurl(__).md>)
- [CFCopyHomeDirectoryURL](<cfcopyhomedirectoryurl().md>)
- [CFDateFormatterCreateISO8601Formatter](<cfdateformattercreateiso8601formatter(____).md>)
- [CFFileSecurityClearProperties](<cffilesecurityclearproperties(____).md>) — Clears properties from a `CFFileSecurityRef` object.
- [CFFileSecurityCopyAccessControlList](<cffilesecuritycopyaccesscontrollist(____).md>) — Copies the access control list associated with a `CFFileSecurityRef` object.
- [CFFileSecurityCopyGroupUUID](<cffilesecuritycopygroupuuid(____).md>) — Copies the group UUID associated with a `CFFileSecurityRef` object.
- [CFFileSecurityCopyOwnerUUID](<cffilesecuritycopyowneruuid(____).md>) — Copies the owner UUID associated with a `CFFileSecurityRef` object.
- [CFFileSecurityCreate](<cffilesecuritycreate(__).md>) — Creates a `CFFileSecurityRef` object.
- [CFFileSecurityCreateCopy](<cffilesecuritycreatecopy(____).md>) — Creates a copy of a `CFFileSecurityRef` object.
- [CFFileSecurityGetGroup](<cffilesecuritygetgroup(____).md>) — Gets the group ID associated with a `CFFileSecurityRef` object
- [CFFileSecurityGetMode](<cffilesecuritygetmode(____).md>) — Gets the file mode associated with a `CFFileSecurityRef` object.
- [CFFileSecurityGetOwner](<cffilesecuritygetowner(____).md>) — Gets the owner ID associated with a `CFFileSecurityRef` object.
- [CFFileSecurityGetTypeID](<cffilesecuritygettypeid().md>) — Returns the type identifier for the `CFFileSecurityRef` opaque type.
- [CFFileSecuritySetAccessControlList](<cffilesecuritysetaccesscontrollist(____).md>) — Sets the access control list associated with a `CFFileSecurityRef` object.
- [CFFileSecuritySetGroup](<cffilesecuritysetgroup(____).md>) — Sets the group ID associated with a `CFFileSecurityRef` object.
- [CFFileSecuritySetGroupUUID](<cffilesecuritysetgroupuuid(____).md>) — Sets the group UUID associated with a `CFFileSecurityRef` object.
- [CFFileSecuritySetMode](<cffilesecuritysetmode(____).md>) — Sets the file mode associated with a `CFFileSecurityRef` object.
- [CFFileSecuritySetOwner](<cffilesecuritysetowner(____).md>) — Sets the owner ID associated with a `CFFileSecurityRef` object.
- [CFFileSecuritySetOwnerUUID](<cffilesecuritysetowneruuid(____).md>) — Sets the owner UUID associated with a `CFFileSecurityRef` object.
- [CFReadStreamCopyDispatchQueue](<cfreadstreamcopydispatchqueue(__).md>)
- [CFReadStreamSetDispatchQueue](<cfreadstreamsetdispatchqueue(____).md>)
- [CFRunLoopTimerGetTolerance](<cfrunlooptimergettolerance(__).md>)
- [CFRunLoopTimerSetTolerance](<cfrunlooptimersettolerance(____).md>)
- [CFURLEnumeratorCreateForDirectoryURL](<cfurlenumeratorcreatefordirectoryurl(________).md>) — Creates and returns a directory enumerator with provided enumerator behavior options and properties to be prefetched.
- [CFURLEnumeratorCreateForMountedVolumes](<cfurlenumeratorcreateformountedvolumes(______).md>) — Creates and returns a volume enumerator with provided enumerator behavior options and properties to be prefetched.
- [CFURLEnumeratorGetDescendentLevel](<cfurlenumeratorgetdescendentlevel(__).md>) — Returns the number of levels a recursive directory enumerator has descended.
- [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) — Advances an enumerator to the next URL.
- [CFURLEnumeratorGetSourceDidChange](<cfurlenumeratorgetsourcedidchange(__).md>) — This function is unimplemented, so it performs no operation. _(deprecated)_
- [CFURLEnumeratorGetTypeID](<cfurlenumeratorgettypeid().md>) — Returns the opaque type identifier for the CFURLEnumerator opaque type.
- [CFURLEnumeratorSkipDescendents](<cfurlenumeratorskipdescendents(__).md>) — Tells a recursive enumerator not to descend into the directory at the URL that was returned by the most recent call to the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.
- [CFURLIsFileReferenceURL](<cfurlisfilereferenceurl(__).md>)
- [CFWriteStreamCopyDispatchQueue](<cfwritestreamcopydispatchqueue(__).md>)
- [CFWriteStreamSetDispatchQueue](<cfwritestreamsetdispatchqueue(____).md>)

## See Also

### Reference

- [CFStream](cfstream.md)
- [Core Foundation Structures](core-foundation-structures.md)
- [Core Foundation Enumerations](core-foundation-enumerations.md)
- [Core Foundation Constants](core-foundation-constants.md)
- [Core Foundation Data Types](core-foundation-data-types.md)
- [Core Foundation Macros](corefoundation-macros.md)
