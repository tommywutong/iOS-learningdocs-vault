---
title: 'Protobuf Editions explained | Kreya'
source: Kreya Blog
source_key: kreya
source_url: 'https://kreya.app/blog/protobuf-editions-explained/'
original_language: en
published: 2024-05-03
status: active
license: Copyright © riok GmbH（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:377d90ba60c1a736'
translated: false
---

> 原文：[Protobuf Editions explained | Kreya](https://kreya.app/blog/protobuf-editions-explained/)　·　Kreya Blog

[Protobuf Editions](https://protobuf.dev/editions/overview/) bring a major change in the way Protocol Buffer versions are handled. Currently there are two versions, "proto2" and "proto3", and the differences between them aren't always obvious. Migrating from proto2 to proto3 isn't easy either. In this blog post we will explore how Protobuf Editions are going to improve this.

## Current state of Protobuf Buffers versions

The first publicly released version of Protobuf was proto2. Since it had some design flaws (for example the `required` keyword and custom default values for fields), it was decided to create the proto3 version. Proto3 is mainly a simplification of proto2 and fixes most of the design flaws mentioned.

Proto2 and proto3 are **wire-compatible** when using the "same constructs": Messages serialized with proto2 can be read with proto3 and vice versa.

### Proto2

Here is an example of a proto2 message definition:

```protobuf
syntax = "proto2";message Book {  required string name = 1;  optional int32 number_of_pages = 2;}
```

Note the use of `required`: This is discouraged, as a value MUST be set, which impedes subsequent changes of the message definition. As mentioned above, this was one of the main reasons why proto3 was created.

### Proto3

In proto3, all fields have "implicit [field presence](https://protobuf.dev/programming-guides/field_presence/)". This basically means that all fields are optional by default. During deserialization, if no data is provided for a field, the default value for that data type (e.g. `0` for numbers, empty string for `string`) is assigned to the field. This is very good for backwards compatibility, as for example adding a new field just works. However, it does not allow consumers to check whether the default value or "nothing" was sent over the wire. In a later iteration of proto3, the `optional` keyword was added, allowing consumers to check whether a value was set.

The following message is only roughly equivalent to the proto2 definition, since the function of the `required` keyword cannot be replicated with proto3:

```protobuf
syntax = "proto3";message Book {  string name = 1; // Cannot check whether an empty string was set or no value provided  optional int32 number_of_pages = 2; // Can check whether 0 was set or no value provided}
```

Note that all data serialized with the proto2 definition can be read with this proto3 definition. The reverse is not necessarily true, for example if `name` is not set in the proto3 message. Proto2 deserialization would then fail because the `name` is required but not present in the data.

## Need for better Protobuf Versioning

The previous handling of Protobuf versions was quite confusing.

- The official documentation was not very helpful, for example the differences between proto2 and proto3 are still hard to find. Some documentation, e.g. for [Custom Options](https://protobuf.dev/programming-guides/proto3/#customoptions), only exists for proto2, but is still applicable to proto3.
- While proto2 message types can be imported in proto3 (and vice versa), there are some [restrictions](https://protobuf.dev/programming-guides/proto3/#proto2).
- In addition, proto3 has several "implementation versions". For example the `optional` keyword was not originally a part of proto3 and was added later.

Probably for these and other reasons, simply creating a proto4 version for future changes was not an option.

## Protobuf Editions

With Protobuf Editions, instead of "hardcoding" behavior (like `required` in proto2), everything is controlled by [features](https://protobuf.dev/editions/features/). Features are options that can be set on a file, on a message or even on individual fields.

Editions can be thought of as a collection of features with a specific default value. The 2023 edition only specifies only a few features, with most of the defaults matching the proto3 version.

One exception is the `features.field_presence` feature, which is `EXPLICIT` by default in the 2023 edition. It has the following values:

- `LEGACY_REQUIRED`: The field is required for parsing and serialization (legacy value to support the behavior of the proto2 `required` keyword)
- `EXPLICIT`: Explicit tracking whether the field value was sent over the wire, even if it was the default value (matches `optional` from proto2 and proto3)
- `IMPLICIT`: No presence tracking. Default values are not serialized. If a value is missing on deserialization, set the field to the default value (default behavior of proto3)

When a new feature is introduced in future editions, it will be disabled by default, but can be enabled manually by opting into it. Subsequent editions may then enable the feature by default, and users may need to opt out of it.

To ease the transition from one edition to another, the Prototiller tool has been announced.

### Proto2 to edition 2023

Using the Prototiller tool (yet to be released), one can convert proto2 definitions into the new 2023 edition. The nice thing about Prototiller is that it preserves the features of the old version and overrides the defaults of the new version accordingly.

Let's take our proto2 example from above:

```protobuf
syntax = "proto2";message Book {  required string name = 1;  optional int32 number_of_pages = 2;}
```

Converting this to edition 2023 with the Prototiller tool would produce the following result (comment added for clarity):

```text
edition = "2023";message Book {  string name = 1 [features.field_presence = LEGACY_REQUIRED];  int32 number_of_pages = 2; // No annotation needed, optional from proto2 matches the 2023 edition defaults}
```

This definition now has **exactly the same semantics** as the proto2 version. They are essentially identical.

### Proto3 to edition 2023

Now let's take our proto3 example from above:

```protobuf
syntax = "proto3";message Book {  string name = 1;  optional int32 number_of_pages = 2;}
```

Converting this to edition 2023 with the Prototiller tool would give the following result:

```text
edition = "2023";message Book {  string name = 1 [features.field_presence = IMPLICIT];  int32 number_of_pages = 2; // No annotation needed, optional from proto3 matches the 2023 edition defaults}
```

Since the field presence is implicit by default in proto3, but explicit in edition 2023, an annotation must be added to the `name` field to preserve the existing behavior. The converted definitions now make it obvious that the proto2 and proto3 definitions were not identical.

We could also enable the implicit field presence for the whole file while keeping the semantics the same:

```text
edition = "2023";option features.field_presence = IMPLICIT;message Book {  string name = 1;  int32 number_of_pages = 2 [features.field_presence = EXPLICIT];}
```

## Advantages

The first Protobuf Edition (edition 2023) was explicitly designed to combine both proto2 and proto3 features. This plus the design of the Protobuf Editions have several advantages:

- Proto2 and proto3 definitions can finally be converted to a version that preserves the old behavior (instead of differences when converting from proto2 to proto3)
- An edition is more "lighter" than a completely new version à la proto4

    - Updating to a newer version while keeping the semantics identical is possible
    - This makes it easier to release editions more frequently
    - This in turn makes it easier to introduce new features into the language
- Features can be deprecated, giving users time to migrate until the feature is removed in a future edition
- Users can easily change the default behavior of the language (this was not possible with proto2 and proto3 because it was hardcoded)
- Documentation is easier to read and write

    - Each feature can be documented separately (when it was introduced, what the default is for each edition etc.)
    - See for example [https://protobuf.dev/editions/features/#field_presence](https://protobuf.dev/editions/features/#field_presence)

## Closing

Overall, Protobuf Editions will have a positive impact on the Protobuf and gRPC ecosystem. It allows the language to move forward and finally introduces a clear update path for users.

**To allow testing of gRPC APIs that make use of the new Protobuf 2023 edition, Kreya will add support for edition 2023 in the next release.**
