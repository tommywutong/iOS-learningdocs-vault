---
title: NSURL and CFURL Release Notes
apple_id: TP40007753
resource_type: Release Note
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2008-06-05'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/RN-NSURL/index.html
archived_at: '2026-07-18T02:50:22.735546Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# NSURL and CFURL Release Notes for OS X v10.6

#### Contents:

- [Accessing File System Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [File Reference URLs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bookmarks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tonjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Accessing File System Resources

This release of OS X contains new Foundation and Core Foundation APIs for URL-based access to file system resources. These APIs are declared in NSURL.h and CFURLAccess.h. Refer to these framework header files for more detailed documentation.

The following new NSURL methods are functional in this release:

```objc
- (BOOL)getResourceValue:(id *)value forKey:(NSString *)key error:(NSError **)error;
- (NSDictionary *)resourceValuesForKeys:(NSArray *)keys error:(NSError **)error;
```

The following new Core Foundation APIs are functional in this release:

```
Boolean CFURLCopyResourcePropertyForKey(CFURLRef url, CFStringRef key, void *propertyValueTypeRefPtr, CFErrorRef *error);
CFDictionaryRef CFURLCopyResourcePropertiesForKeys(CFURLRef url, CFArrayRef keys, CFErrorRef *error);
void CFURLClearResourcePropertyCacheForKey(CFURLRef url, CFStringRef key);
void CFURLClearResourcePropertyCache(CFURLRef url);
```

The following new NSURL methods are declared but not implemented in this release:

```objc
- (BOOL)setResourceValue:(id)value forKey:(NSString *)key error:(NSError **)error;
- (BOOL)setResourceValues:(NSDictionary *)keyedValues error:(NSError **)error;
- (BOOL)checkResourceIsReachableAndReturnError:(NSError **)error;
```

The following new APIs are declared in CFURLAccess.h, but are not implemented in this release:

```
Boolean CFURLSetResourcePropertyForKey(CFURLRef url, CFStringRef key, CFTypeRef propertValue, CFErrorRef *error);
Boolean CFURLSetResourcePropertiesForKeys(CFURLRef url, CFDictionaryRef keyedPropertyValues, CFErrorRef *error);
void CFURLSetTemporaryResourcePropertyForKey(CFURLRef url, CFStringRef key, CFTypeRef propertyValue);
Boolean CFURLResourceIsReachable(CFURLRef url, CFErrorRef *error);
```

The follow property keys are supported for file URLs. Corresponding CFURL property keys are declared in CFURLAccess.h:

```
NSURLNameKey
NSURLLocalizedNameKey
NSURLIsRegularFileKey
NSURLIsDirectoryKey
NSURLIsSymbolicLinkKey
NSURLIsVolumeKey
NSURLIsPackageKey
NSURLIsSystemImmutableKey
NSURLIsUserImmutableKey
NSURLIsHiddenKey
NSURLHasHiddenExtensionKey
NSURLCreationDateKey
NSURLContentAccessDateKey
NSURLContentModificationDateKey
NSURLAttributeModificationDateKey
NSURLLinkCountKey
NSURLParentDirectoryURLKey
NSURLVolumeURLKey
NSURLTypeIdentifierKey
NSURLLocalizedTypeDescriptionKey
NSURLEffectiveIconKey
NSURLFileSizeKey
NSURLFileAllocatedSizeKey
```

The following property keys (and the parallel Core Foundation property keys) are declared but not supported in this release:

```
NSURLLabelNumberKey
NSURLLabelColorKey
NSURLLocalizedLabelKey
NSURLCustomIconKey
NSURLVolumeLocalizedFormatDescriptionKey
NSURLVolumeTotalCapacityKey
NSURLVolumeAvailableCapacityKey
NSURLVolumeResourceCountKey
NSURLVolumeSupportsPersistentIDsKey
NSURLVolumeSupportsSymbolicLinksKey
NSURLVolumeSupportsHardLinksKey
NSURLVolumeSupportsJournalingKey
NSURLVolumeIsJournalingKey
NSURLVolumeSupportsSparseFilesKey
NSURLVolumeSupportsZeroRunsKey
NSURLVolumeSupportsCaseSensitiveNamesKey
NSURLVolumeSupportsCasePreservedNamesKey
```


### File Reference URLs

OS X v10.6 supports a new form of file URL, called a __file reference URL__. File reference URLs use a URL path syntax that identifies a file (or directory) by its volume ID and file (or directory) ID, much like the Carbon File Manager’s FSRef file identifier. This form of file URL remains valid when the file system path of the URL’s underlying resource changes. New APIs for accessing file system resource properties accept file URLs in either path or reference form.

Existing APIs that generate file URLs continue to return regular path-based file URLs. Applications that need a path-independent file reference URL should request one using the following new APIs:

New NSURL methods (see NSURL.h):

```objc
- (BOOL)isFileReferenceURL;
- (NSURL *)fileReferenceURL;
- (NSURL *)filePathURL;
```

New Core Foundation APIs (see CFURL.h):

```
CFURLRef CFURLCreateFileReferenceURL(CFAllocatorRef allocator, CFURLRef url, CFErrorRef *error);
CFURLRef CFURLCreateFilePathURL(CFAllocatorRef allocator, CFURLRef url, CFErrorRef *error);
```

The syntax of a file reference URL should be considered opaque, and may change from release to release. The following APIs have been enhanced to handle file reference URLs. They automatically return the located resource’s full file system path:

```
-[NSURL path]
CFURLGetFileSystemRepresentation()
CFURLCopyFileSystemPath()
```

A file reference URL remains valid as long as the underlying resource exists and its volume is mounted. When a volume is remounted (including when the system is rebooted), it is assigned a new volume ID. Therefore, file reference URLs referring to the original volume are no longer valid.

### Bookmarks

Bookmarks are a new facility for generating persistent references to resources identified by URLs. A bookmark is a data object generated by the system from a resource URL. The bookmark data encapsulates a durable, opaque reference to the underlying resource as well as value of resource properties captured when the bookmark was created. A bookmark can be stored in memory or on disk and later used to access the resource property values it contains, or resolved to cover the underlying resource’s URL. In the case of file system resources, the bookmark is capable of locating resources that have been moved or renamed since the bookmark was created, similar to Alias Manager aliases. Note that in this release, bookmarks resolve only by path.

The following new NSURL methods are further documented in NSURL.h:

```objc
- (NSData *)bookmarkDataWithOptions:(NSURLBookmarkCreationOptions)options includingResourceValuesForKeys:(NSArray *)keys relativeToURL:( NSURL*)relativeURL error:(NSURL **)error;
- (NSURL*)initByResolvingBookmarkData:(NSData*)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error;
+ (NSURL *)URLByResolvingBookmarkData:(NSData *)bookmarkData options:(NSURLBookmarkResolutionOptions)options relativeToURL:(NSURL *)relativeURL bookmarkDataIsStale:(BOOL *)isStale error:(NSError **)error;
+ (NSDictionary *)resourceValuesForKeys:(NSArray *)keys fromBookmarkData:(NSData *)bookmarkData;
```

The following new CFURL functions are further documented in NSURL.h:

```
CFDataRef CFURLCreateBookmarkData( CFAllocatorRef allocator, CFURLRef url, CFURLBookmarkCreationOptions options, CFArrayRef resourcePropertiesToInclude, CFURLRef relativeToURL, CFErrorRef* error );
CFURLRef CFURLCreateByResolvingBookmarkData( CFAllocatorRef allocator, CFDataRef bookmark, CFURLBookmarkResolutionOptions options, CFURLRef relativeToURL, CFArrayRef resourcePropertiesToInclude, Boolean* isStale, CFErrorRef* error );
CFDictionaryRef CFURLCreateResourcePropertiesForKeysFromBookmarkData( CFAllocatorRef allocator, CFArrayRef resourcePropertiesToReturn, CFDataRef bookmark );
CFTypeRef  CFURLCreateResourcePropertyForKeyFromBookmarkData( CFAllocatorRef allocator, CFStringRef resourcePropertyKey, CFDataRef bookmark );
```
