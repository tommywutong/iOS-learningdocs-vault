---
title: Publishers
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers
source_url: 'https://developer.apple.com/documentation/combine/publishers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers.json'
content_hash: 'sha256:aa6394117590fd59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Publishers

<sub>Enumeration</sub>

A namespace for types that serve as publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Publishers
```

## Overview

The various operators defined as extensions on [Publisher](publisher.md) implement their functionality as classes or structures that extend this enumeration. For example, the `contains(_:)` operator returns a `Publishers.Contains` instance.

## Topics

### Convenience publishers

- [Sequence](publishers/sequence.md) — A publisher that publishes a given sequence of elements.
- [Catch](publishers/catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

### Working with subscribers

- [ReceiveOn](publishers/receiveon.md) — A publisher that delivers elements to its downstream subscriber on a specific scheduler.
- [SubscribeOn](publishers/subscribeon.md) — A publisher that receives elements from an upstream publisher on a specific scheduler.

### Mapping elements

- [Map](publishers/map.md) — A publisher that transforms all elements from the upstream publisher with a provided closure.
- [TryMap](publishers/trymap.md) — A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [MapError](publishers/maperror.md) — A publisher that converts any failure from the upstream publisher into a new error.
- [Scan](publishers/scan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [TryScan](publishers/tryscan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [SetFailureType](publishers/setfailuretype.md) — A publisher that appears to send a specified failure type.

### Filtering elements

- [Filter](publishers/filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](publishers/tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [CompactMap](publishers/compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [TryCompactMap](publishers/trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [RemoveDuplicates](publishers/removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [TryRemoveDuplicates](publishers/tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceEmpty](publishers/replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](publishers/replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.

### Reducing elements

- [Collect](publishers/collect.md) — A publisher that buffers items.
- [CollectByCount](publishers/collectbycount.md) — A publisher that buffers a maximum number of items.
- [CollectByTime](publishers/collectbytime.md) — A publisher that buffers and periodically publishes its items.
- [TimeGroupingStrategy](publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [IgnoreOutput](publishers/ignoreoutput.md) — A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Reduce](publishers/reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [TryReduce](publishers/tryreduce.md) — A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

### Applying mathematical operations on elements

- [Count](publishers/count.md) — A publisher that publishes the number of elements received from the upstream publisher.
- [Comparison](publishers/comparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
- [TryComparison](publishers/trycomparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.

### Applying matching criteria to elements

- [Contains](publishers/contains.md) — A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [ContainsWhere](publishers/containswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [TryContainsWhere](publishers/trycontainswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [AllSatisfy](publishers/allsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [TryAllSatisfy](publishers/tryallsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

### Applying sequence operations to elements

- [DropUntilOutput](publishers/dropuntiloutput.md) — A publisher that ignores elements from the upstream publisher until it receives an element from second publisher.
- [Drop](publishers/drop.md) — A publisher that omits a specified number of elements before republishing later elements.
- [DropWhile](publishers/dropwhile.md) — A publisher that omits elements from an upstream publisher until a given closure returns false.
- [TryDropWhile](publishers/trydropwhile.md) — A publisher that omits elements from an upstream publisher until a given error-throwing closure returns false.
- [Concatenate](publishers/concatenate.md) — A publisher that emits all of one publisher’s elements before those from another publisher.
- [PrefixWhile](publishers/prefixwhile.md) — A publisher that republishes elements while a predicate closure indicates publishing should continue.
- [TryPrefixWhile](publishers/tryprefixwhile.md) — A publisher that republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [PrefixUntilOutput](publishers/prefixuntiloutput.md) — A publisher that republishes elements until another publisher emits an element.

### Selecting specific elements

- [First](publishers/first.md) — A publisher that publishes the first element of a stream, then finishes.
- [FirstWhere](publishers/firstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [TryFirstWhere](publishers/tryfirstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Last](publishers/last.md) — A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [LastWhere](publishers/lastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [TryLastWhere](publishers/trylastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Output](publishers/output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.

### Combining elements from multiple publishers

- [CombineLatest](publishers/combinelatest.md) — A publisher that receives and combines the latest elements from two publishers.
- [CombineLatest3](publishers/combinelatest3.md) — A publisher that receives and combines the latest elements from three publishers.
- [CombineLatest4](publishers/combinelatest4.md) — A publisher that receives and combines the latest elements from four publishers.
- [Merge](publishers/merge.md) — A publisher created by applying the merge function to two upstream publishers.
- [Merge3](publishers/merge3.md) — A publisher created by applying the merge function to three upstream publishers.
- [Merge4](publishers/merge4.md) — A publisher created by applying the merge function to four upstream publishers.
- [Merge5](publishers/merge5.md) — A publisher created by applying the merge function to five upstream publishers.
- [Merge6](publishers/merge6.md) — A publisher created by applying the merge function to six upstream publishers.
- [Merge7](publishers/merge7.md) — A publisher created by applying the merge function to seven upstream publishers.
- [Merge8](publishers/merge8.md) — A publisher created by applying the merge function to eight upstream publishers.
- [MergeMany](publishers/mergemany.md) — A publisher created by applying the merge function to an arbitrary number of upstream publishers.
- [Zip](publishers/zip.md) — A publisher created by applying the zip function to two upstream publishers.
- [Zip3](publishers/zip3.md) — A publisher created by applying the zip function to three upstream publishers.
- [Zip4](publishers/zip4.md) — A publisher created by applying the zip function to four upstream publishers.

### Republishing elements by subscribing to new publishers

- [FlatMap](publishers/flatmap.md) — A publisher that transforms elements from an upstream publisher into a new publisher.
- [SwitchToLatest](publishers/switchtolatest.md) — A publisher that flattens nested publishers.

### Handling errors

- [AssertNoFailure](publishers/assertnofailure.md) — A publisher that raises a fatal error upon receiving any failure, and otherwise republishes all received input.
- [Catch](publishers/catch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.
- [TryCatch](publishers/trycatch.md) — A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher or producing a new error.
- [Retry](publishers/retry.md) — A publisher that attempts to recreate its subscription to a failed upstream publisher.

### Controlling timing

- [MeasureInterval](publishers/measureinterval.md) — A publisher that measures and emits the time interval between events received from an upstream publisher.
- [Debounce](publishers/debounce.md) — A publisher that publishes elements only after a specified time interval elapses between events.
- [Delay](publishers/delay.md) — A publisher that delays delivery of elements and completion to the downstream receiver.
- [Throttle](publishers/throttle.md) — A publisher that publishes either the most-recent or first element published by the upstream publisher in a specified time interval.
- [Timeout](publishers/timeout.md) — A publisher that terminates publishing if the upstream publisher exceeds a specified time interval without producing an element.

### Encoding and decoding

- [Decode](publishers/decode.md) — A publisher that decodes elements received from an upstream publisher, using a given decoder.
- [Encode](publishers/encode.md) — A publisher that encodes elements received from an upstream publisher, using a given encoder.

### Identifying properties with key paths

- [MapKeyPath](publishers/mapkeypath.md) — A publisher that publishes the value of a key path.
- [MapKeyPath2](publishers/mapkeypath2.md) — A publisher that publishes the values of two key paths as a tuple.
- [MapKeyPath3](publishers/mapkeypath3.md) — A publisher that publishes the values of three key paths as a tuple.

### Working with multiple subscribers

- [Multicast](publishers/multicast.md) — A publisher that uses a subject to deliver elements to multiple subscribers.
- [Share](publishers/share.md) — A publisher that shares the output of an upstream publisher with multiple subscribers.

### Buffering elements

- [Buffer](publishers/buffer.md) — A publisher that buffers elements from an upstream publisher.
- [BufferingStrategy](publishers/bufferingstrategy.md) — A strategy that handles exhaustion of a buffer’s capacity.
- [PrefetchStrategy](publishers/prefetchstrategy.md) — A strategy for filling a buffer.

### Using explicit publisher connections

- [Autoconnect](publishers/autoconnect.md) — A publisher that automatically connects to an upstream connectable publisher.
- [MakeConnectable](publishers/makeconnectable.md) — A publisher that provides explicit connectability to another publisher.

### Debugging

- [Breakpoint](publishers/breakpoint.md) — A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [HandleEvents](publishers/handleevents.md) — A publisher that performs the specified closures when publisher events occur.
- [Print](publishers/print.md) — A publisher that prints log messages for all publishing events, optionally prefixed with a given string.

## See Also

### Publishers

- [Publisher](publisher.md) — Declares that a type can transmit a sequence of values over time.
- [AnyPublisher](anypublisher.md) — A publisher that performs type erasure by wrapping another publisher.
- [Published](published.md) — A type that publishes a property marked with an attribute.
- [Cancellable](cancellable.md) — A protocol indicating that an activity or action supports cancellation.
- [AnyCancellable](anycancellable.md) — A type-erasing cancellable object that executes a provided closure when canceled.
