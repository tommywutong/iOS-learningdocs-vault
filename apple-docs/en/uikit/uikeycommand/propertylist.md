---
title: propertyList
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/propertylist
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/propertylist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/propertylist.json'
content_hash: 'sha256:baa09bd1b40745b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# propertyList

<sub>Instance Property</sub>

An object that contains data to associate with the key command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var propertyList: Any? { get }
```

## Discussion

Use [propertyList](propertylist.md) to associate a small amount of data to the command.

**Swift**

In Swift, the property list should contain only standard library types such as [Array](../../swift/array.md), [Dictionary](../../swift/dictionary.md), [String](../../swift/string.md), [Int](../../swift/int.md), and [Double](../../swift/double.md), and Foundation types such as [Date](../../foundation/date.md) and [Data](../../foundation/data.md).

**Objective-C**

In Objective-C, the property list should contain only [NSArray](../../foundation/nsarray.md), [NSDictionary](../../foundation/nsdictionary.md), [NSString](../../foundation/nsstring.md), [NSNumber](../../foundation/nsnumber.md), [NSDate](../../foundation/nsdate.md), and [NSData](../../foundation/nsdata.md) objects.

## See Also

### Associating data

- [UICommandTagShare](../uicommandtagshare.md) — A value that identifies a command as a Share menu.
