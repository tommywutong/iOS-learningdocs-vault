---
title: Type Erasure in Rust
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/'
original_language: en
published: 2023-10-23
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:83793907e8190bff'
translated: false
---

> 原文：[Type Erasure in Rust](https://belkadan.com/blog/2023/10/Type-Erasure-in-Rust/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Soft Orders of Magnitude](https://belkadan.com/blog/2023/10/Soft-Orders-of-Magnitude/)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/) »

« [The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=rust)

## [Type Erasure in Rust](#)

Rust traits have the neat property where you can use them _either_ as generic bounds _or_ as dynamic dispatch, with the `&dyn MyTrait` syntax. The latter is necessary in heterogeneous scenarios, where you want to use multiple concrete types together that all implement a common trait. However, that requires that you have an instance, so that the reference actually “refers” to something. What if you have a trait with “static” requirements, like `const`s or methods without `&self`?

If the implementing types have instances, or are just marker types, you can wrap the base trait in a new trait, like in this stripped-down example from [my work](https://signal.org):

```
trait Parameters {
  const SECRET_KEY_LENGTH: usize;
  fn generate() -> KeyMaterial<Secret>;
}

trait DynParameters {
  fn secret_key_length(&self) -> usize;
  fn generate(&self) -> KeyMaterial<Secret>;
}

impl<T: Parameters> DynParameters for T {
  fn secret_key_length(&self) -> usize {
    Self::SECRET_KEY_LENGTH
  }

  fn generate(&self) -> KeyMaterial<Secret> {
    Self::generate()
  }
}
```

Now `&dyn DynParameters` will work.

However, sometimes the types that conform to the trait don’t have instances to tie a new trait to. If so, take a step back and think about what dynamic dispatch is: a table of trait members that get looked up at run time. You can build a little wrapper type to do this manually:

```
trait Parameters {
  const SECRET_KEY_LENGTH: usize;
  fn generate() -> KeyMaterial<Secret>;
}

struct AnyParameters {
  secret_key_length: usize;
  generate: fn() -> KeyMaterial<Secret>;
}

impl AnyParameters {
  fn new<T: Parameters>() -> Self {
    Self {
      secret_key_length: T::SECRET_KEY_LENGTH,
      generate: T::generate, // we're not calling it, just referring to it
    }
  }
}
```

### Generics

This is all well and good, but what if the type you need to abstract over isn’t a trait at all, but a generic struct? If the generic is just a marker type, we may be able to get away with substituting our own marker type:

```
struct KeyMaterial<T> {
  data: Box<[u8]>,
  kind: PhantomData<T>,
}

impl KeyMaterial<()> {
  fn erasing_kind_of<T>(other: KeyMaterial<T>) -> Self {
    Self {
      data: other.data,
      kind: PhantomData,
    }
  }
}
```

But usually there are some additional operations on the type that we might need. In that case we’ll combine the two techniques: we’ll copy over data from the input struct, and also include a manual dispatch table.

```
struct KeyMaterial<T> {
  data: Box<[u8]>,
  kind: PhantomData<T>,
}

trait KeyKind {
  fn key_length(key_type: KeyType) -> usize;
}

struct AnyKeyMaterial {
  // Data from KeyMaterial<T>
  data: Box<[u8]>,
  // Operations from T: KeyKind
  key_length: fn(KeyType) -> usize;
}

impl AnyKeyMaterial {
  fn erasing_kind_of<T: KeyKind>(other: KeyMaterial<T>) -> Self {
    Self {
      data: other.data,
      key_length: T::key_length,
    }
  }
}
```

And now you have a struct that can be used to represent heterogeneous KeyMaterials. (Never mind that the example no longer makes sense.)

This pattern isn’t very complicated, but I didn’t see it written down in one place for Rust, hence this post. (Swift folks who’ve been around for a few years are pretty familiar with similar patterns, though they’re rarer now that Swift’s `any` types—the equivalent of `dyn`—aren’t as limited as they were in the past.)

This entry was posted on [October](https://belkadan.com/blog/2023/10) 23, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Rust](https://belkadan.com/blog/tags/rust)
