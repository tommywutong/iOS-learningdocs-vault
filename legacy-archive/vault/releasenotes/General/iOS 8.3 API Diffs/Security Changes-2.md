---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Security.html
archived_at: '2026-07-18T02:56:27.700706Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Security Changes

## Security

Added kSecPaddingSigRawModified SecKeyDecrypt(SecKey!, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyDecrypt(_ key: SecKey!, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: UInt, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<UInt>) -> OSStatus ``` |
| To | ``` func SecKeyDecrypt(_ key: SecKey!, _ padding: SecPadding, _ cipherText: UnsafePointer<UInt8>, _ cipherTextLen: Int, _ plainText: UnsafeMutablePointer<UInt8>, _ plainTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified SecKeyEncrypt(SecKey!, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyEncrypt(_ key: SecKey!, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: UInt, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<UInt>) -> OSStatus ``` |
| To | ``` func SecKeyEncrypt(_ key: SecKey!, _ padding: SecPadding, _ plainText: UnsafePointer<UInt8>, _ plainTextLen: Int, _ cipherText: UnsafeMutablePointer<UInt8>, _ cipherTextLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified SecKeyGetBlockSize(SecKey!) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> UInt ``` |
| To | ``` func SecKeyGetBlockSize(_ key: SecKey!) -> Int ``` |

Modified SecKeyRawSign(SecKey!, SecPadding, UnsafePointer<UInt8>, Int, UnsafeMutablePointer<UInt8>, UnsafeMutablePointer<Int>) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyRawSign(_ key: SecKey!, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: UInt, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<UInt>) -> OSStatus ``` |
| To | ``` func SecKeyRawSign(_ key: SecKey!, _ padding: SecPadding, _ dataToSign: UnsafePointer<UInt8>, _ dataToSignLen: Int, _ sig: UnsafeMutablePointer<UInt8>, _ sigLen: UnsafeMutablePointer<Int>) -> OSStatus ``` |

Modified SecKeyRawVerify(SecKey!, SecPadding, UnsafePointer<UInt8>, Int, UnsafePointer<UInt8>, Int) -> OSStatus

|  | Declaration |
| --- | --- |
| From | ``` func SecKeyRawVerify(_ key: SecKey!, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: UInt, _ sig: UnsafePointer<UInt8>, _ sigLen: UInt) -> OSStatus ``` |
| To | ``` func SecKeyRawVerify(_ key: SecKey!, _ padding: SecPadding, _ signedData: UnsafePointer<UInt8>, _ signedDataLen: Int, _ sig: UnsafePointer<UInt8>, _ sigLen: Int) -> OSStatus ``` |

Modified SecRandomCopyBytes(SecRandomRef, Int, UnsafeMutablePointer<UInt8>) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func SecRandomCopyBytes(_ rnd: SecRandom!, _ count: UInt, _ bytes: UnsafeMutablePointer<UInt8>) -> Int32 ``` |
| To | ``` func SecRandomCopyBytes(_ rnd: SecRandomRef, _ count: Int, _ bytes: UnsafeMutablePointer<UInt8>) -> Int32 ``` |

Modified SecRandomRef

|  | Declaration |
| --- | --- |
| From | ``` typealias SecRandomRef = SecRandom ``` |
| To | ``` typealias SecRandomRef = COpaquePointer ``` |

Modified kSecRandomDefault

|  | Declaration |
| --- | --- |
| From | ``` let kSecRandomDefault: SecRandom! ``` |
| To | ``` let kSecRandomDefault: SecRandomRef ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
