---
title: 'SecRandomCopyBytes(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secrandomcopybytes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrandomcopybytes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b55a518c0ce17251'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRandomCopyBytes(_:_:_:)

<sub>Function</sub>

Generates an array of cryptographically secure random bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecRandomCopyBytes(_ rnd: SecRandomRef?, _ count: Int, _ bytes: UnsafeMutableRawPointer) -> Int32
```

## Parameters

- `rnd` — The random number generator object to use. Specify [kSecRandomDefault](ksecrandomdefault.md) to use the default random number generator.

- `count` — The number of random bytes to return in the array pointed to by the `bytes` parameter.

- `bytes` — A pointer to an array that the function fills with cryptographically secure random bytes. Use an array that is large enough to hold at least `count` bytes.

## Return Value

A result code set to [errSecSuccess](errsecsuccess.md) or some other value on failure.

## Discussion

Always test the returned status to make sure that the array has been updated with new, random data before trying to use the values. For example, to create 10 random bytes:

**Swift**

```swift
var bytes = [Int8](repeating: 0, count: 10)
let status = SecRandomCopyBytes(kSecRandomDefault, bytes.count, &bytes)

if status == errSecSuccess { // Always test the status.
    print(bytes)
    // Prints something different every time you run.
}
```

**Objective-C**

```objc
SInt8 bytes[10];
int status = SecRandomCopyBytes(kSecRandomDefault, (sizeof bytes)/(sizeof bytes[0]), &bytes);
    
if (status == errSecSuccess) { // Always test the status.
    for (int i = 0; i < (sizeof bytes)/(sizeof bytes[0]); i++) {
        NSLog(@"%d", bytes[i]);
    }
    // Prints something different every time you run.
}
```
