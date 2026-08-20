---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreAudio.html
archived_at: '2026-07-18T02:57:06.820955Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreAudio Changes for Swift

### CoreAudio

Modified [AudioChannelCoordinateIndex [enum]](https://developer.apple.com/documentation/coreaudio/audiochannelcoordinateindex)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [MPEG4ObjectID [enum]](https://developer.apple.com/documentation/coreaudio/mpeg4objectid)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SMPTETimeType [enum]](https://developer.apple.com/documentation/coreaudio/smptetimetype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [UnsafeMutableAudioBufferListPointer [struct]](https://developer.apple.com/documentation/coreaudio/unsafemutableaudiobufferlistpointer)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollectionType, CollectionType, Indexable, SequenceType, MutableIndexable {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> AudioBuffer { get nonmutating set } } ``` | CollectionType, Indexable, MutableCollectionType, MutableIndexable, SequenceType |
| To | ``` struct UnsafeMutableAudioBufferListPointer {     init(_ p: UnsafeMutablePointer<AudioBufferList>)     var count: Int { get nonmutating set }     var unsafePointer: UnsafePointer<AudioBufferList> { get }     var unsafeMutablePointer: UnsafeMutablePointer<AudioBufferList> } extension UnsafeMutableAudioBufferListPointer : MutableCollectionType {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> AudioBuffer { get nonmutating set } } ``` | MutableCollectionType |

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
