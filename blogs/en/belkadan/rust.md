---
title: Rust
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/rust'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:a1a59c072b79711f'
translated: false
---

> 原文：[Rust](https://belkadan.com/blog/tags/rust)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [Type Erasure in Rust](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/?tag=rust)

23 October 2023

Rust traits have the neat property where you can use them _either_ as generic bounds _or_ as dynamic dispatch, with the `&dyn MyTrait` syntax. The latter is necessary in heterogeneous scenarios, where you want to use multiple concrete types together that all implement a common trait. However, that requires that you have an instance, so that the reference actually “refers” to something. What if you have a trait with “static” requirements, like `const`s or methods without `&self`?

[(Continue reading…)](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/?tag=rust)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Rust](https://belkadan.com/blog/tags/rust)

## [The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=rust)

28 November 2022

Swift has a pair of protocols, [Encodable and Decodable](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types), which represent generic encoding of a tree structure. These protocols are special in that the compiler can provide a default implementation for them under many circumstances. Similarly, Rust has a project called [Serde](https://serde.rs/) which likewise is used for roughly the same purpose; Serde’s traits are even more complicated than Codable’s, but have even more powerful code synthesis via Rust’s proc-macros. Both tools are very useful but occasionally frustrating, and I think some of the frustrating areas come from a tension between two competing use cases.

[(Continue reading…)](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=rust)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Rust](https://belkadan.com/blog/tags/rust)

## [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=rust)

24 April 2022

This post is in response to Aria Beingessner’s “[Defaults Affect Inference in Rust: Expressions Instead Of Types](https://gankra.github.io/blah/defaults-affect-inference/)”, which describes how adding default arguments to Rust could help with some Rust stdlib problems around generics. At the same time, the Rust internals forum has a thread on “[Named Arguments](https://internals.rust-lang.org/t/pre-rfc-named-arguments/16413)” something that’s been discussed for Rust off and on for years (at varying levels of seriousness).

Here I’m going to discuss how those two features interact, and why considering them separately is potentially a bad idea. It’s a lot more braindump-y than my usual style, so be warned. The post is written with a Rust audience in mind, but makes frequent reference to Swift, Python, and C# as examples of real-world languages that have some version of these features. It also overlaps quite a bit with Aria’s post.

[(Continue reading…)](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=rust)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Rust](https://belkadan.com/blog/tags/rust), [Swift](https://belkadan.com/blog/tags/swift), [Programming languages](https://belkadan.com/blog/tags/programming-languages)

## Older Posts

1. 2020-08-26

  Objective-Rust

### Possibly Related Tags

- Objective-C
- Programming languages
- Swift
