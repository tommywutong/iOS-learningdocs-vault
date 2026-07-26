---
title: 'bundleWithPath:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsbundle/bundlewithpath:'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundle/bundlewithpath:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundle/bundlewithpath%3A.json'
content_hash: 'sha256:abee2d82bbd43de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# bundleWithPath:

<sub>Type Method</sub>

Returns an `NSBundle` object that corresponds to the specified directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) bundleWithPath:(NSString *) path;
```

## Parameters

- `path` — The path to a directory. This must be a full pathname for a directory; if it contains any symbolic links, they must be resolvable.

## Return Value

The `NSBundle` object that corresponds to `path`, or `nil` if `path` does not identify an accessible bundle directory.

## Discussion

This method allocates and initializes the returned object if there is no existing `NSBundle` associated with `path`, in which case it returns the existing object.

## See Also

### Related Documentation

- [mainBundle](../bundle/main.md) — Returns the bundle object that contains the current executable.

### Creating and initializing a bundle

- [+ bundleWithURL:](<../bundle/init(url_)-a2t0.md>) — Returns an `NSBundle` object that corresponds to the specified file URL.
- [+ bundleForClass:](<../bundle/init(for_).md>) — Returns the `NSBundle` object with which the specified class is associated.
- [+ bundleWithIdentifier:](<../bundle/init(identifier_).md>) — Returns the `NSBundle` instance that has the specified bundle identifier.
- [- initWithPath:](<../bundle/init(path_).md>) — Returns an `NSBundle` object initialized to correspond to the specified directory.
