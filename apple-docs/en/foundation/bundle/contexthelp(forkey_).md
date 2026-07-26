---
title: 'contextHelp(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/bundle/contexthelp(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/contexthelp(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/contexthelp%28forkey%3A%29.json'
content_hash: 'sha256:14a96a2f6534440c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# contextHelp(forKey:)

<sub>Instance Method</sub>

Returns the context-sensitive help for the specified key from the bundle’s help file.

<sub>macOS</sub>

```swift
func contextHelp(forKey key: NSHelpManager.ContextHelpKey) -> NSAttributedString?
```

## Parameters

- `key` — A key in your application’s `Help.plist` file that identifies the context-sensitive help to return.

## Return Value

The help string or `nil` if the application does not have a `Help.plist` file or the file does not contain an entry for the specified `key`.

## Discussion

When you build your application, you can merge multiple RTF-based help files together using the `/usr/bin/compileHelp` tool, which then packages your help file information into a property list named `Help.plist`. After placing this property-list file in your application bundle, you can use this method to extract context help information from it. To look up a particular entry, you specify the name of the original RTF help file in the `key` parameter of this method. For example, if your application project contains a help file named `Copy.rtf`, you would retrieve the text from this file by passing the value `@"Copy.rtf"` to the `key` parameter.

This method is declared in `NSHelpManager.h`.

## See Also

### Related Documentation

- [contextHelp(for:)](<../../appkit/nshelpmanager/contexthelp(for_).md>) — Returns context-sensitive help for an object.
