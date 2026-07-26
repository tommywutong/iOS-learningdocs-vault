---
title: SIMDMask
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/simdmask
source_url: 'https://developer.apple.com/documentation/swift/simdmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simdmask.json'
content_hash: 'sha256:f45e73cd2080bc3c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# SIMDMask

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct SIMDMask<Storage> where Storage : SIMD, Storage.Scalar : FixedWidthInteger, Storage.Scalar : SignedInteger
```

## Relationships

- **Conforms To**: [CustomStringConvertible](customstringconvertible.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md), [Hashable](hashable.md), [SIMD](simd.md), [SIMDStorage](simdstorage.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Operators

- [.!(_:)](<simdmask/'.!(__)-1i6z4.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-1taxm.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-1uoo5.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-1wni3.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-21iaq.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-2s4rp.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-2xidg.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-369g7.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-37o53.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-3cez8.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-3v0wb.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-412oe.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-4j1ws.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-4jcjq.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-4x8xz.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-5byae.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-5glpy.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-5qm8v.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-6cygw.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-7iq11.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-7odl6.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-7odqs.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-7oxtu.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-7x8d0.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-864jr.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-88k9y.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-8ewdk.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-8fdgj.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-8ps9r.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-8qmdw.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-8qz21.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-9afyr.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-9j4wf.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-9lm1f.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-9oij3.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!(_:)](<simdmask/'.!(__)-w95r.md>) — A vector mask that is the pointwise logical negation of the input.
- [.!=(_:_:)](<simdmask/'.!=(____)-1bstv.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-1xcmp.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-3aavu.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-3vfg0.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-3ylip.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-423h5.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-4efoo.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-4qjq3.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-4uyji.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-4yah8.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-52wyk.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-57336.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-5b2tn.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-5b65c.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-5c1ea.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-69426.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-6g155.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-6k7jt.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-6xo9v.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-72ix7.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-7c281.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-7eoc8.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-7i3ju.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-9gbp0.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-9pxno.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-9qlrq.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-9tocb.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-9vgs4.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-a5c6.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-dffz.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-eifj.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-g3o1.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-m7n7.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-mac2.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.!=(_:_:)](<simdmask/'.!=(____)-y5ox.md>) — A vector mask with the result of a pointwise inequality comparison.
- [.&(_:_:)](<simdmask/'.&(____)-145py.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-169o8.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-1a23z.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-1pshx.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-1ucx5.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-20xdw.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-2awxi.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-2imak.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-2lwk7.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-2peib.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-3ky5.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-3q922.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-431pz.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-49px.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-4am8f.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-4dlkk.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-4ryow.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-4vik1.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-4x5gc.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-557cy.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-5zen.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-67j.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-67wgv.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-680i1.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-6xa9c.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-6xn07.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-7mo1z.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-892f.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-8pp6f.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-8q5wb.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-9429d.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-97hdm.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-9915i.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-9nff3.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-9qn9n.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-9u9mk.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-fq1q.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&(_:_:)](<simdmask/'.&(____)-zszx.md>) — A vector mask that is the pointwise logical conjunction of the inputs.
- [.&=(_:_:)](<simdmask/'.&=(____)-12gkg.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-1cwox.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-1wpn1.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-1x3hq.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-20boa.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-252cj.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-2na0m.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-34ad1.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-3oxz3.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-4ysik.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-52kbo.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-5en6.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-5jyb3.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-5kwst.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-5lkct.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-5qb7m.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-62ajs.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-63gip.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-6ou9w.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-6p7x3.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-6tmg8.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-6zusl.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-70wd4.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-7oyep.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-7wb1u.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-844uv.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-85bn8.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-86khr.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-8ur23.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-8yjqn.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-95thm.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-962kz.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-9kh2c.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-9wv32.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-icc.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-lg4i.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.&=(_:_:)](<simdmask/'.&=(____)-skpc.md>) — Replaces `a` with the pointwise logical conjunction of `a` and `b`.
- [.==(_:_:)](<simdmask/'.==(____)-11d2d.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-1jvgs.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-1og62.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-1ubfu.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-284j9.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-2brx5.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-2dam3.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-2iimf.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-39nci.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-3gcbu.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-3hdhk.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-3kebh.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-3myzv.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-42ijc.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-45t84.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-4b0ny.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-57ghp.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-587zp.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-5h2mq.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-5uq1i.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-60n7g.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-67dx6.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-6cck1.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-6fplg.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-6vw48.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-71h0j.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-7fdu0.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-7h67k.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-8ergy.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-8vssm.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-91rl9.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-979dh.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-k5h7.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-riwy.md>) — A vector mask with the result of a pointwise equality comparison.
- [.==(_:_:)](<simdmask/'.==(____)-xxgz.md>) — A vector mask with the result of a pointwise equality comparison.
- [.^(_:_:)](<simdmask/'._(____)-11sjt.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1ke9.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1kfk0.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1lqpw.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-1lxbl.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-1lz4p.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1na0j.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1orsn.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-1zt0u.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-2cb7l.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-2fut5.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-2ihng.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-2qbki.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-33q5z.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-374nn.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-3bgdq.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-3n4if.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-3o5p8.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-3qurd.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-3r14q.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-3t3b6.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-3tj8x.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-3uhaz.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-3wd47.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-4akg1.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-4hjau.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-4qn8l.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-521pj.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-52ll8.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-5bq2t.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-5coqj.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-5crsr.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-5ic47.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-5pu7e.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-5to13.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-63r3t.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-6dhf6.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-6g5ou.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-6j7cz.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-6l9ra.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-6pru.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-6v0gb.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-753hw.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-75fbk.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-77675.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-78lxr.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-7feku.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-7qdxf.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-7tall.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-7yq75.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-81c6m.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-856yj.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-865a6.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-86pih.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-87ha8.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-8ovj4.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-8oxhr.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-8pb64.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-8pklp.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-8z99n.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-91mg7.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-93fh3.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-93uww.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-94c8y.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-952oz.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-99sse.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-9h7g4.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-9i0ho.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-9lt9f.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-9picb.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-9s54c.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-9t6d6.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-9wmqe.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-gx5e.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.|(_:_:)](<simdmask/'._(____)-rztm.md>) — A vector mask that is the pointwise logical disjunction of the inputs.
- [.^(_:_:)](<simdmask/'._(____)-vf27.md>) — A vector mask that is the pointwise exclusive or of the inputs.
- [.^=(_:_:)](<simdmask/'._=(____)-10b9k.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-11elm.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-17zji.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-187ym.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-19x8.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-1bqze.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-1kwjk.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-1l06v.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-1skak.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-289ei.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-28avd.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-2fptv.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-32bpi.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-33sbw.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-35gl4.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-36fwo.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-36zd7.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-37pr7.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-3c5yv.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-3cq16.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-3dnxc.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-3dwxc.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-3jpjw.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-3l4kc.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-3lgta.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-3lp52.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-3zval.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-424pq.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-48r5d.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-49ffo.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-4c0l2.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-4hstr.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-4jn7m.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-4m5ba.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-4rjbb.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-4w85p.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-53c71.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-55m63.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-564rm.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-5p4g2.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-5yqz0.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-68krs.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6gi0j.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6jqlh.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6ncn.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-6q6ca.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6rb2k.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6vrul.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-6y37h.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-6yxof.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-75ws5.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-77voy.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-78qic.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-7bu3y.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-7gotm.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-7hjr8.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-7rhqy.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-7vb81.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-8n751.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-8ts0r.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-8wkee.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-8xdh5.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-91v5a.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-9cexc.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-9s8nu.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-9wm9x.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-9ybag.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-bbyz.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-dji1.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.|=(_:_:)](<simdmask/'._=(____)-g3jo.md>) — Replaces `a` with the pointwise logical disjunction of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-gpt7.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-jiue.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-nixb.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.
- [.^=(_:_:)](<simdmask/'._=(____)-wwci.md>) — Replaces `a` with the pointwise exclusive or of `a` and `b`.

### Initializers

- [init()](<simdmask/init().md>) — Creates a vector with zero in all lanes.
- [init(repeating:)](<simdmask/init(repeating_)-1m52n.md>)
- [init(repeating:)](<simdmask/init(repeating_)-202bd.md>)
- [init(repeating:)](<simdmask/init(repeating_)-248q1.md>)
- [init(repeating:)](<simdmask/init(repeating_)-2pmca.md>)
- [init(repeating:)](<simdmask/init(repeating_)-2x534.md>)
- [init(repeating:)](<simdmask/init(repeating_)-2yqe1.md>)
- [init(repeating:)](<simdmask/init(repeating_)-3q2ur.md>)
- [init(repeating:)](<simdmask/init(repeating_)-3w0ux.md>)
- [init(repeating:)](<simdmask/init(repeating_)-3w4ke.md>)
- [init(repeating:)](<simdmask/init(repeating_)-42cre.md>)
- [init(repeating:)](<simdmask/init(repeating_)-42vxu.md>)
- [init(repeating:)](<simdmask/init(repeating_)-4kh6e.md>)
- [init(repeating:)](<simdmask/init(repeating_)-4n5yz.md>)
- [init(repeating:)](<simdmask/init(repeating_)-4p6y0.md>)
- [init(repeating:)](<simdmask/init(repeating_)-59l18.md>)
- [init(repeating:)](<simdmask/init(repeating_)-5cst1.md>)
- [init(repeating:)](<simdmask/init(repeating_)-5gywa.md>)
- [init(repeating:)](<simdmask/init(repeating_)-5zr61.md>)
- [init(repeating:)](<simdmask/init(repeating_)-6cczf.md>)
- [init(repeating:)](<simdmask/init(repeating_)-6lkx7.md>)
- [init(repeating:)](<simdmask/init(repeating_)-6r2mi.md>)
- [init(repeating:)](<simdmask/init(repeating_)-6wd06.md>)
- [init(repeating:)](<simdmask/init(repeating_)-6xdsz.md>)
- [init(repeating:)](<simdmask/init(repeating_)-78cdd.md>)
- [init(repeating:)](<simdmask/init(repeating_)-7xzo4.md>)
- [init(repeating:)](<simdmask/init(repeating_)-80x0s.md>)
- [init(repeating:)](<simdmask/init(repeating_)-87zs0.md>)
- [init(repeating:)](<simdmask/init(repeating_)-89avq.md>)
- [init(repeating:)](<simdmask/init(repeating_)-8omke.md>)
- [init(repeating:)](<simdmask/init(repeating_)-8y7bw.md>)
- [init(repeating:)](<simdmask/init(repeating_)-9fi4f.md>)
- [init(repeating:)](<simdmask/init(repeating_)-9ndns.md>)
- [init(repeating:)](<simdmask/init(repeating_)-9su40.md>)
- [init(repeating:)](<simdmask/init(repeating_)-ufux.md>)
- [init(repeating:)](<simdmask/init(repeating_)-wbsm.md>)

### Instance Properties

- [hashValue](simdmask/hashvalue.md) — The hash value.
- [scalarCount](simdmask/scalarcount.md) — The number of scalars, or elements, in the vector.

### Instance Methods

- [replace(with:where:)](<simdmask/replace(with_where_)-11sio.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-1apjj.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-21nlg.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-24wgu.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-2hsah.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-2l1cw.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-2xv7u.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-3huzu.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-3wsfp.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-4acy9.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-4egrz.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-4zc4a.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-4zrb4.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-58aw.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-5mzr3.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-5wj86.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-6b6u3.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-6unjm.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-6x0g3.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-76v5a.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-7ehzz.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-7hlsy.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-7qg9m.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-7qytv.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-889b7.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-8gg39.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-9nlep.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-9pxoc.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-aosa.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-hn35.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-klo8.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-lhds.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-p18j.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-qerf.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replace(with:where:)](<simdmask/replace(with_where_)-wt51.md>) — Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-1tc07.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-1uajn.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-1vwr2.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-211v4.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-221u7.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-2h7n9.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-2j2hn.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-2jm3v.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-3firb.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-3kfo4.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-3y37w.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-4gvh6.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-4htdo.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-4mmzd.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-4nikh.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-515tf.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-5dsdp.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-5eb2n.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-5n09x.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-60cao.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-6mn7k.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-6vk5h.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7q8n5.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7qxdb.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7uyp7.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7wb0w.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7wxag.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-7yvsx.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-8bs2p.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-8fafz.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-8kc21.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-91l51.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-93wj5.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-9wyi2.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [replacing(with:where:)](<simdmask/replacing(with_where_)-x0wd.md>) — Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.

### Subscripts

- [subscript(_:)](<simdmask/subscript(__).md>) — Accesses the element at the specified index.

### Type Aliases

- [ArrayLiteralElement](simdmask/arrayliteralelement.md) — The type of the elements of an array literal.
- [MaskStorage](simdmask/maskstorage.md) — The mask type resulting from pointwise comparisons of this vector type.
- [Scalar](simdmask/scalar.md)

### Type Methods

- [random()](<simdmask/random().md>) — Returns a vector mask with `true` or `false` randomly assigned in each lane.
- [random(using:)](<simdmask/random(using_).md>) — Returns a vector mask with `true` or `false` randomly assigned in each lane, using the given generator as a source for randomness.

### Default Implementations

- [Equatable Implementations](simdmask/equatable-implementations.md)
- [SIMD Implementations](simdmask/simd-implementations.md)

## See Also

### Supporting Types

- [SIMD](simd.md) — A SIMD vector of a fixed number of elements.
- [SIMDScalar](simdscalar.md) — A type that can be used as an element in a SIMD vector.
- [SIMDStorage](simdstorage.md) — A type that can function as storage for a SIMD vector type.
