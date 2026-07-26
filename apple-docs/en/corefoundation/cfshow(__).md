---
title: 'CFShow(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfshow(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfshow(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfshow%28_%3A%29.json'
content_hash: 'sha256:ea90a2c2c6e5670f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFShow(_:)

<sub>Function</sub>

Prints a description of a Core Foundation object to stderr.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFShow(_ obj: CFTypeRef!)
```

## Parameters

- `obj` — A Core Foundation object derived from CFType. If `obj` is not a Core Foundation object, an assertion is raised.

## Discussion

The output is printed to the standard I/O standard error (stderr).

This function is useful as a debugging aid for Core Foundation objects. Because these objects are based on opaque types, it is difficult to examine their contents directly. However, the opaque types implement `description` function callbacks that return descriptions of their objects. This function invokes these callbacks.

### Special Considerations

You can use `CFShow` in one of two general ways. If your debugger supports function calls (such as `gdb` does), call `CFShow` in the debugger:

```objc
(gdb) call (void) CFShow(string)
Hello World
```

You can also incorporate calls to `CFShow` in a test version of your code to print out “snapshots” of Core Foundation objects to the console.

## See Also

### Miscellaneous Functions

- [CFCopyDescription](<cfcopydescription(__).md>) — Returns a textual description of a Core Foundation object.
- [CFCopyTypeIDDescription](<cfcopytypeiddescription(__).md>) — Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [CFGetTypeID](<cfgettypeid(__).md>) — Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
