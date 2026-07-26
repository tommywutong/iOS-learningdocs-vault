---
title: The Two Faces of Codable/Serde
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/11/Codable-Serde/'
original_language: en
published: 2022-11-28
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:ee3a08abcb65e861'
translated: false
---

> 原文：[The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Swift was always going to be part of the OS](https://belkadan.com/blog/2022/10/Swift-in-the-OS/)

[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/) »

« [Swift was always going to be part of the OS](https://belkadan.com/blog/2022/10/Swift-in-the-OS/?tag=swift)

[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/?tag=swift) »

« [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=rust)

[Type Erasure in Rust](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/?tag=rust) »

## [The Two Faces of Codable/Serde](#)

Swift has a pair of protocols, [Encodable and Decodable](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types), which represent generic encoding of a tree structure. These protocols are special in that the compiler can provide a default implementation for them under many circumstances. Similarly, Rust has a project called [Serde](https://serde.rs/) which likewise is used for roughly the same purpose; Serde’s traits are even more complicated than Codable’s, but have even more powerful code synthesis via Rust’s proc-macros. Both tools are very useful but occasionally frustrating, and I think some of the frustrating areas come from a tension between two competing use cases.more

_Before we get into this, I want to acknowledge that Codable and Serde will never handle *every* situation, and that’s okay. You can customize their behavior to a certain extent, but at some point it is both easier and *correct* to fall back to handwritten code instead. Codable and Serde *should* follow the 80/20 rule: prioritize the common 80% of use cases and not the “long tail” of complexity in the remaining 20%.[1](#fn:80-20)_

### Pre-existing formats

One of the things that Codable and Serde give you is a _declarative syntax_ for tree-based formats, particularly JSON. We all know how nesting structs works; we all know how JSON objects work.[2](#fn:know) Seems like they should just line up, right? Bam: with Codable/Serde you’re now off and running sending REST requests to someone else’s API, or even your own across language boundaries. You’re able to parse a dataset made freely available somewhere. You can generate something to spec, and that’s really the common element in all of these cases: there _is_ a spec, and you’re just trying to match it. Using normal struct and enum syntax to do that is way easier than writing all the imperative or functional steps out by hand.

There’s an important corollary to this use case, which is that you almost always only care about one format. “Take this JSON and translate it to a binary plist”, said no one ever. Some of the generic nature of Codable and Serde get wasted at this stage; did you know that by default Serde will generate code to deserialize a struct from an _array_ as well as a dictionary?[3](#fn:serde-array) If you’re writing to a spec, this is a waste of time and code size.

It’s not unlikely that the format in the spec is not the most useful format for your program. (At the very least, naming conventions often differ across environments.) Both Codable and Serde have some level of control over this, allowing you to use a more idiomatic description of a field for programmatic use, but adjust that for encoding/decoding. Serde tends to be more feature-complete here than Codable, but writing Codable implementations by hand is simpler than it is for Serde.

#### Defining a format

This looks like a separate use case at first, but in the end it’s really the same: you have some user data in your app, and you want to save it. Maybe it’s the actual contents of a document, maybe it’s preferences that are a little more structured than flags and strings. No need to do custom serialization, just use Codable/Serde.[4](#fn:json-data)

This is totally valid. It also ends up being the same as the “pre-existing format” use case, because as soon as you write the data out, you have a pre-existing format! One that conveniently matches the model you currently have in your program, but if you ever change anything, it’s on you to translate between the old and new formats, and preserve compatibility as best you can, or at least as best you want to.

### Providing a type

The other major use of Codable and Serde is for library authors providing new interchange types. People want to be able to put your type in their data structure and save it; providing Codable/Serde support exposes _some_ serialization that everyone can use, whether they’re going to encode to JSON or binary plists or just a flat buffer. This, really, is why Codable and Serde exist at all, rather than just format-specific APIs: so that the type exposing its structure can do so without knowing or caring what encoder it will eventually be used with.

If these types are always used with self-defined formats, that’s fine. But if you want to use a library type with a pre-existing format, you can quickly run into problems. Think of all the different ways to represent timestamps: [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) strings, seconds since Jan 1 1970, milliseconds since Jan 1 1970, a _decimal_ number of seconds, a struct of seconds and nanoseconds, a struct of date and time (and maybe time zone?)… If you’ve got a standard timestamp type (even if you’ve named it [Date](https://developer.apple.com/documentation/foundation/date)), its default Encodable implementation has to pick _some_ representation. Decodable may accept a few. But if the spec you’re trying to match has a different format, you’re out of luck.

Codable originally tried to handle this by setting “encoding strategies” at the top level, and yeah, that kind of works…if the encoder you use provides the customization you want for the type you want to use. In my opinion, this is a limited approach; the current best strategy for Swift is to use property wrappers that manually implement the Codable protocols to translate from the wire format to the type you want. Unfortunately, property wrappers don’t always compose well, so if you were hoping to use a _different_ property wrapper, or rely on compiler synthesis for a non-Codable protocol, you may be out of luck. Serde’s attribute-and-macro-based approach is less intrusive because it doesn’t affect the stored type for the property, just the code synthesized for the containing type.

### Conclusions?

This isn’t a “Codable and Serde are busted” post. They’re definitely not perfect; there are plenty of criticisms of each that don’t have anything to do with the format-specific/format-agnostic dichotomy I’ve described here.[5](#fn:encoder) But I think the dichotomy does exist, and that does affect the design of Codable and Serde. These serialization mechanisms are trying to serve two separate but related needs, and that means there will sometimes be trade-offs. Recognizing this will hopefully improve the design of Codable and Serde and any supporting libraries in the future.

Thanks to [Gwynne Raskind](https://github.com/gwynne) for beta-reading this post.

1. There are many, many versions of “the 80/20 rule” out there, and I can’t actually find a good citation for this particular one. The original source of the phrase is the [Pareto Principle](https://en.wikipedia.org/wiki/Pareto_principle), but that seems pretty far from how I’m using it. [↩︎](#fnref:80-20)
2. Yes, this is hyperbole. But it’s easy to learn both. [↩︎](#fnref:know)
3. “[The implementation supports two possible ways that a struct may be represented by a data format: as a seq like in Postcard, and as a map like in JSON.](https://serde.rs/deserialize-struct.html)” [↩︎](#fnref:serde-array)
4. But if you have any binary blobs, maybe don’t use JSON as your storage format; since JSON is a “plain text” format typically encoded using UTF-8, it has [significant overhead](https://github.com/qntm/base32768) storing binary blobs. [↩︎](#fnref:json-data)
5. One such criticism is that they’re both very much set up for formats that mirror structs, like JSON and [plists](https://en.wikipedia.org/wiki/Property_list). The further you get from that, the more format-specific customization you end up needing. For XML encoding, for example, you have keyed attributes that can only be strings, and unkeyed children. That doesn’t map nearly as nicely to a struct.

  Writing your own encoder or decoder is also very complicated for both Codable and Serde. For Codable in particular, it also expects out-of-order functionality that results in either ahead-of-time parsing or redundant work, which puts a limit on the throughput and minimum memory usage. [↩︎](#fnref:encoder)

This entry was posted on [November](https://belkadan.com/blog/2022/11) 28, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Rust](https://belkadan.com/blog/tags/rust)
