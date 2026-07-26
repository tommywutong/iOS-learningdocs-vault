---
title: 'removeValue(forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/removevalue(forkey:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/removevalue(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/removevalue%28forkey%3A%29.json'
content_hash: 'sha256:03e532a42f481e3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Dictionary](../dictionary.md)

# removeValue(forKey:)

<sub>Instance Method</sub>

Removes the given key and its associated value from the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeValue(forKey key: Key) -> Value?
```

## Parameters

- `key` — The key to remove along with its associated value.

## Return Value

The value that was removed, or `nil` if the key was not present in the dictionary.

## Discussion

If the key is found in the dictionary, this method returns the key’s associated value. On removal, this method invalidates all indices with respect to the dictionary.

```swift
var hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
if let value = hues.removeValue(forKey: "Coral") {
    print("The value \(value) was removed.")
}
// Prints "The value 16 was removed."
```

If the key isn’t found in the dictionary, `removeValue(forKey:)` returns `nil`.

```swift
if let value = hues.removeValue(forKey: "Cerise") {
    print("The value \(value) was removed.")
} else {
    print("No value found for that key.")
}
// Prints "No value found for that key."
```

> [!abstract] Complexity
> O(_n_), where _n_ is the number of key-value pairs in the dictionary.

## See Also

### Removing Keys and Values

- [filter(_:)](<filter(__).md>) — Returns a new dictionary containing the key-value pairs of the dictionary that satisfy the given predicate.
- [remove(at:)](<remove(at_).md>) — Removes and returns the key-value pair at the specified index.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all key-value pairs from the dictionary.
