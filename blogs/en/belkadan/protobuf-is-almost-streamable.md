---
title: Protobuf Is Almost Streamable
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/'
original_language: en
published: 2023-12-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c0627b0f880d148b'
translated: false
---

> 原文：[Protobuf Is Almost Streamable](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Daylight Saving Is Temporal Time Zones](https://belkadan.com/blog/2023/12/Daylight-Saving-Is-Temporal-Time-Zones/)

[CellLVM](https://belkadan.com/blog/2023/12/CellLVM/) »

## [Protobuf Is Almost Streamable](#)

[Protobuf](https://protobuf.dev) is a binary (non-textual) encoding format invented by Google. It has some nice properties and some less nice properties.[1](#fn:recommendation) But one that’s a little frustrating is that it’s _almost_ a streamable format—that is, one where you can process data as it comes in, rather than waiting until you’ve read all of it.more

See, the encoding for protobuf is something like “field number, length of field, bytes of field”, repeated for every field in a message. The [real encoding](https://protobuf.dev/programming-guides/encoding/) packs that in a little tighter for integers, floats, and booleans, but that’s the gist of it. All field types in protobuf v3 (the current version, usually written as “proto3”) have a default value (0, false, empty, or `null` for a nested message), so if you don’t see a field in a stream, you can assume it’s set to its default. Or you can mark the field as `optional` to use `null` as the default for any type, or `repeated` to collect every appearance of a field into a list. All of these modes are a _little_ annoying for streamability, because you don’t have the complete value for a field until you get to the end of the stream, but depending on what’s actually _in_ your top-level record, that might be fine.

And then there’s [this rule](https://protobuf.dev/programming-guides/encoding/#last-one-wins):

> ### Last One Wins
> 
> Normally, an encoded message would never have more than one instance of a non-`repeated` field. However, parsers are expected to handle the case in which they do. For numeric types and strings, if the same field appears multiple times, the parser accepts the _last_ value it sees. For embedded message fields, the parser merges multiple instances of the same field, as if with the `Message::MergeFrom` method – that is, all singular scalar fields in the latter instance replace those in the former, singular embedded messages are merged, and `repeated` fields are concatenated. The effect of these rules is that parsing the concatenation of two encoded messages produces exactly the same result as if you had parsed the two messages separately and merged the resulting objects.
> 
> This property is occasionally useful, as it allows you to merge two messages (by concatenation) even if you do not know their types.

This defeats streaming. If you processed a numeric or string field, you might have to undo it and try again; if you processed a nested message, _you might have done so incorrectly._ And you have to keep the original message around to perform merging anyway, or emulate it very carefully in your processing function.

You could try to promise that _your_ protobufs will never do this, but that means you’re using a restricted subset of the protobuf spec, and suddenly you have to check that all your tools that produce and modify protobufs satisfy it. Which they _probably_ do, but there’s no guarantee. You could also declare all top-level fields `repeated` and then complain if there are ever actually any repeats—something that isn’t the best use of the tools, maybe, but most protos have validity constraints beyond the basic types. But then you _will_ be fighting the tools, and getting to use existing tools is half the point of using protobuf.

I don’t think this “concatenative” property was worth losing streamability. If they had instead said “the first value wins, all others are silently skipped” streaming would have been fine. But alas. Most people who need streaming give up and emit separate protobuf messages with a leading length, and possibly an identifier to say what kind of message it is. Which, you know, sounds like a field…but what do I know?

1. If you are shopping around for a new format, consider one of the newer ones that have come up since; if you are currently using protobuf, it’s probably fine. [↩︎](#fnref:recommendation)

This entry was posted on [December](https://belkadan.com/blog/2023/12) 14, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Encoding](https://belkadan.com/blog/tags/encoding)
