---
title: Atomic
framework: Synchronization
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomic
source_url: 'https://developer.apple.com/documentation/synchronization/atomic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomic.json'
content_hash: 'sha256:2b7fdd6758731ca4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Synchronization](../synchronization.md)

# Atomic

<sub>Structure</sub>

An atomic value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Atomic<Value> where Value : AtomicRepresentable
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<atomic/init(__).md>) — Initializes a value of this atomic with the given initial value.

### Instance Methods

- [add(_:ordering:)](<atomic/add(__ordering_)-1k1sq.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-34u14.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-39vk1.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-4dpjd.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-4ocr0.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-6rhji.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-7ws8q.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-8cc78.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-8xoe3.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-90njk.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-97ilu.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [add(_:ordering:)](<atomic/add(__ordering_)-vm4c.md>) — Perform an atomic add operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-1baj3.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-1gzwl.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-1yz1m.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-3zt46.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-4db7m.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-56lhq.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-5iaoz.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-5m0jk.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-5mhgj.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-6mxdg.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-8ilt7.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseAnd(_:ordering:)](<atomic/bitwiseand(__ordering_)-l1a3.md>) — Perform an atomic bitwise AND operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-206dk.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-39r9q.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-4ozz5.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-4q8ef.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-4y864.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-5574x.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-6fz7a.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-6zz2p.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-72403.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-84e8q.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-9191v.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseOr(_:ordering:)](<atomic/bitwiseor(__ordering_)-aa7f.md>) — Perform an atomic bitwise OR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-271x9.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-2vrf.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-33l7y.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-4umey.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-5df6p.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-5vpxh.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-5zfc.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-8t1qf.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-9l5qb.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-9xi4f.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-m4nt.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [bitwiseXor(_:ordering:)](<atomic/bitwisexor(__ordering_)-sf4i.md>) — Perform an atomic bitwise XOR operation and return the old and new value, applying the specified memory ordering.
- [compareExchange(expected:desired:ordering:)](<atomic/compareexchange(expected_desired_ordering_)-33pf3.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [compareExchange(expected:desired:ordering:)](<atomic/compareexchange(expected_desired_ordering_)-6rsfl.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [compareExchange(expected:desired:ordering:)](<atomic/compareexchange(expected_desired_ordering_)-8uimm.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [compareExchange(expected:desired:ordering:)](<atomic/compareexchange(expected_desired_ordering_)-9bh60.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [compareExchange(expected:desired:ordering:)](<atomic/compareexchange(expected_desired_ordering_)-s52j.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified memory ordering.
- [compareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/compareexchange(expected_desired_successordering_failureordering_)-5obt4.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [compareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/compareexchange(expected_desired_successordering_failureordering_)-7msfy.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [compareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/compareexchange(expected_desired_successordering_failureordering_)-82j0l.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [compareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/compareexchange(expected_desired_successordering_failureordering_)-8d36a.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [compareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/compareexchange(expected_desired_successordering_failureordering_)-cve0.md>) — Perform an atomic compare and exchange operation on the current value, applying the specified success/failure memory orderings.
- [exchange(_:ordering:)](<atomic/exchange(__ordering_)-5n6sy.md>) — Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [exchange(_:ordering:)](<atomic/exchange(__ordering_)-8ip0d.md>) — Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [exchange(_:ordering:)](<atomic/exchange(__ordering_)-9kb4s.md>) — Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [exchange(_:ordering:)](<atomic/exchange(__ordering_)-9y5j8.md>) — Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [exchange(_:ordering:)](<atomic/exchange(__ordering_)-ycta.md>) — Atomically sets the current value to `desired` and returns the original value, applying the specified memory ordering.
- [load(ordering:)](<atomic/load(ordering_)-2u27y.md>) — Atomically loads and returns the current value, applying the specified memory ordering.
- [load(ordering:)](<atomic/load(ordering_)-2v8gp.md>) — Atomically loads and returns the current value, applying the specified memory ordering.
- [load(ordering:)](<atomic/load(ordering_)-3u18o.md>) — Atomically loads and returns the current value, applying the specified memory ordering.
- [load(ordering:)](<atomic/load(ordering_)-4mv5b.md>) — Atomically loads and returns the current value, applying the specified memory ordering.
- [load(ordering:)](<atomic/load(ordering_)-8ufx2.md>) — Atomically loads and returns the current value, applying the specified memory ordering.
- [logicalAnd(_:ordering:)](<atomic/logicaland(__ordering_).md>) — Perform an atomic logical AND operation and return the old and new value, applying the specified memory ordering.
- [logicalOr(_:ordering:)](<atomic/logicalor(__ordering_).md>) — Perform an atomic logical OR operation and return the old and new value, applying the specified memory ordering.
- [logicalXor(_:ordering:)](<atomic/logicalxor(__ordering_).md>) — Perform an atomic logical XOR operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-1l8lv.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-32cin.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-4e4mn.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-4rq6h.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-5qqv7.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-681q1.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-7kusb.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-7qnkd.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-7z7ub.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-81jab.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-957na.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [max(_:ordering:)](<atomic/max(__ordering_)-xy7u.md>) — Perform an atomic maximum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-1uwzs.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-2l64c.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-39r27.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-3tiyt.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-3tk2x.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-4b62m.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-4wv9d.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-6bbf1.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-6ivky.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-73283.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-8k42m.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [min(_:ordering:)](<atomic/min(__ordering_)-yogw.md>) — Perform an atomic minimum operation and return the old and new value, applying the specified memory ordering.
- [store(_:ordering:)](<atomic/store(__ordering_)-195np.md>) — Atomically sets the current value to `desired`, applying the specified memory ordering.
- [store(_:ordering:)](<atomic/store(__ordering_)-22zxw.md>) — Atomically sets the current value to `desired`, applying the specified memory ordering.
- [store(_:ordering:)](<atomic/store(__ordering_)-532ut.md>) — Atomically sets the current value to `desired`, applying the specified memory ordering.
- [store(_:ordering:)](<atomic/store(__ordering_)-5q2fi.md>) — Atomically sets the current value to `desired`, applying the specified memory ordering.
- [store(_:ordering:)](<atomic/store(__ordering_)-97ua7.md>) — Atomically sets the current value to `desired`, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-1atf4.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-1iop7.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-2ddui.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-2ds2s.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-3c2nm.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-47p0x.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-5rq0s.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-65sge.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-6eidf.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-7ebxd.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-9w06o.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [subtract(_:ordering:)](<atomic/subtract(__ordering_)-pqxe.md>) — Perform an atomic subtract operation and return the old and new value, applying the specified memory ordering.
- [weakCompareExchange(expected:desired:ordering:)](<atomic/weakcompareexchange(expected_desired_ordering_)-24bnb.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:ordering:)](<atomic/weakcompareexchange(expected_desired_ordering_)-728eh.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:ordering:)](<atomic/weakcompareexchange(expected_desired_ordering_)-72wpg.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:ordering:)](<atomic/weakcompareexchange(expected_desired_ordering_)-9w8ty.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:ordering:)](<atomic/weakcompareexchange(expected_desired_ordering_)-9xqnl.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the memory ordering. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/weakcompareexchange(expected_desired_successordering_failureordering_)-2ywaz.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/weakcompareexchange(expected_desired_successordering_failureordering_)-3p8t6.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/weakcompareexchange(expected_desired_successordering_failureordering_)-7vtyo.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/weakcompareexchange(expected_desired_successordering_failureordering_)-9kx2t.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [weakCompareExchange(expected:desired:successOrdering:failureOrdering:)](<atomic/weakcompareexchange(expected_desired_successordering_failureordering_)-kfa8.md>) — Perform an atomic weak compare and exchange operation on the current value, applying the specified success/failure memory orderings. This compare-exchange variant is allowed to spuriously fail; it is designed to be called in a loop until it indicates a successful exchange has happened.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-1cynr.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-35sou.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-3ihte.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-3ltc9.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-4da1i.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-7flp6.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-8rrye.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-8wun9.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-9ce27.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-bmso.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-u8d5.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingAdd(_:ordering:)](<atomic/wrappingadd(__ordering_)-ussb.md>) — Perform an atomic wrapping add operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-1bgvk.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-3795w.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-43111.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-6g9gv.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-6xyiw.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-6y8r7.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-7136k.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-7203n.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-7k1nk.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-83zzr.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-8o6j2.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.
- [wrappingSubtract(_:ordering:)](<atomic/wrappingsubtract(__ordering_)-8xrpg.md>) — Perform an atomic wrapping subtract operation and return the old and new value, applying the specified memory ordering.

## See Also

### Atomic Values

- [AtomicLazyReference](atomiclazyreference.md) — A lazily initializable atomic strong reference.
- [WordPair](wordpair.md) — A pair of two word sized `UInt`s.
- [AtomicRepresentable](atomicrepresentable.md) — A type that supports atomic operations through a separate atomic storage representation.
- [AtomicOptionalRepresentable](atomicoptionalrepresentable.md) — An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.
