---
title: Publisher
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher
source_url: 'https://developer.apple.com/documentation/combine/publisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher.json'
content_hash: 'sha256:4009552ae7296948'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# Publisher

<sub>Protocol</sub>

Declares that a type can transmit a sequence of values over time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Publisher<Output, Failure>
```

## Overview

A publisher delivers elements to one or more [Subscriber](subscriber.md) instances. The subscriber’s [Input](subscriber/input.md) and [Failure](subscriber/failure.md) associated types must match the [Output](publisher/output.md) and [Failure](publisher/failure.md) types declared by the publisher. The publisher implements the [receive(subscriber:)](<publisher/receive(subscriber_).md>)method to accept a subscriber.

After this, the publisher can call the following methods on the subscriber:

- [receive(subscription:)](<subscriber/receive(subscription_).md>): Acknowledges the subscribe request and returns a [Subscription](subscription.md) instance. The subscriber uses the subscription to demand elements from the publisher and can use it to cancel publishing.
- [receive(_:)](<subscriber/receive(__).md>): Delivers one element from the publisher to the subscriber.
- [receive(completion:)](<subscriber/receive(completion_).md>): Informs the subscriber that publishing has ended, either normally or with an error.

Every `Publisher` must adhere to this contract for downstream subscribers to function correctly.

> [!tip] Tip
> A Combine publisher fills a role similar to, but distinct from, the [AsyncSequence](../swift/asyncsequence.md) in the Swift standard library. A `Publisher` and an `AsyncSequence` both produce elements over time. However, the pull model in Combine uses a [Subscriber](subscriber.md) to request elements from a publisher, while Swift concurrency uses the `for`-`await`-`in` syntax to iterate over elements published by an `AsyncSequence`. Both APIs offer methods to modify the sequence by mapping or filtering elements, while only Combine provides time-based operations like [debounce(for:scheduler:options:)](<publisher/debounce(for_scheduler_options_).md>) and [throttle(for:scheduler:latest:)](<publisher/throttle(for_scheduler_latest_).md>), and combining operations like [merge(with:)](<publisher/merge(with_)-7fk3a.md>) and [combineLatest(_:_:)](<publisher/combinelatest(____)-1n30g.md>). To bridge the two approaches, the property [values](publisher/values-1dm9r.md) exposes a publisher’s elements as an `AsyncSequence`, allowing you to iterate over them with `for`-`await`-`in` rather than attaching a [Subscriber](subscriber.md).

### Using operators

Extensions on `Publisher` define a wide variety of _operators_ that you compose to create sophisticated event-processing chains. Each operator returns a type that implements the [Publisher](publisher.md) protocol Most of these types exist as extensions on the [Publishers](publishers.md) enumeration. For example, the [map(_:)](<publisher/map(__)-99evh.md>) operator returns an instance of [Map](publishers/map.md).

Use operators to assemble a chain of republishers, optionally ending with a subscriber, that processes elements produced by upstream publishers. Each operator creates and configures an instance of a [Publisher](publisher.md) or [Subscriber](subscriber.md), and subscribes it to the publisher that you call the method on.

In the following example, a sequence publisher emits the integers 1, 2, 3, 4, and 5. A [filter(_:)](<publisher/filter(__).md>) operator creates a [Filter](publishers/filter.md) publisher to only republish even values. A second operator creates a [Sink](subscribers/sink.md) subscriber to print out each value received. The sink subscriber automatically subscribes to the filter publisher, at which point the filter publisher subscribes to its upstream publisher, the sequence publisher.

```swift
let cancellable = [1, 2, 3, 4, 5].publisher
    .filter {
        $0 % 2 == 0
    }
    .sink {
        print ("Even number: \($0)")
    }
// Prints:
// Even number: 2
// Even number: 4
```

## Creating Your Own Publishers

Rather than implementing the `Publisher` protocol yourself, you can create your own publisher by using one of several types provided by the Combine framework:

- Use a concrete subclass of [Subject](subject.md), such as [PassthroughSubject](passthroughsubject.md), to publish values on-demand by calling its [send(_:)](<subject/send(__).md>) method.
- Use a [CurrentValueSubject](currentvaluesubject.md) to publish whenever you update the subject’s underlying value.
- Add the `@Published` annotation to a property of one of your own types. In doing so, the property gains a publisher that emits an event whenever the property’s value changes. See the [Published](published.md) type for an example of this approach.

## Relationships

- **Inherited By**: [ConnectablePublisher](connectablepublisher.md), [Subject](subject.md)

- **Conforming Types**: [AnyPublisher](anypublisher.md), [CurrentValueSubject](currentvaluesubject.md), [Deferred](deferred.md), [Empty](empty.md), [Fail](fail.md), [Future](future.md), [Just](just.md), [ObservableObjectPublisher](observableobjectpublisher.md), [PassthroughSubject](passthroughsubject.md), [Publisher](published/publisher.md), [AllSatisfy](publishers/allsatisfy.md), [AssertNoFailure](publishers/assertnofailure.md), [Autoconnect](publishers/autoconnect.md), [Breakpoint](publishers/breakpoint.md), [Buffer](publishers/buffer.md), [Catch](publishers/catch.md), [Collect](publishers/collect.md), [CollectByCount](publishers/collectbycount.md), [CollectByTime](publishers/collectbytime.md), [CombineLatest](publishers/combinelatest.md), [CombineLatest3](publishers/combinelatest3.md), [CombineLatest4](publishers/combinelatest4.md), [CompactMap](publishers/compactmap.md), [Comparison](publishers/comparison.md), [Concatenate](publishers/concatenate.md), [Contains](publishers/contains.md), [ContainsWhere](publishers/containswhere.md), [Count](publishers/count.md), [Debounce](publishers/debounce.md), [Decode](publishers/decode.md), [Delay](publishers/delay.md), [Drop](publishers/drop.md), [DropUntilOutput](publishers/dropuntiloutput.md), [DropWhile](publishers/dropwhile.md), [Encode](publishers/encode.md), [Filter](publishers/filter.md), [First](publishers/first.md), [FirstWhere](publishers/firstwhere.md), [FlatMap](publishers/flatmap.md), [HandleEvents](publishers/handleevents.md), [IgnoreOutput](publishers/ignoreoutput.md), [Last](publishers/last.md), [LastWhere](publishers/lastwhere.md), [MakeConnectable](publishers/makeconnectable.md), [Map](publishers/map.md), [MapError](publishers/maperror.md), [MapKeyPath](publishers/mapkeypath.md), [MapKeyPath2](publishers/mapkeypath2.md), [MapKeyPath3](publishers/mapkeypath3.md), [MeasureInterval](publishers/measureinterval.md), [Merge](publishers/merge.md), [Merge3](publishers/merge3.md), [Merge4](publishers/merge4.md), [Merge5](publishers/merge5.md), [Merge6](publishers/merge6.md), [Merge7](publishers/merge7.md), [Merge8](publishers/merge8.md), [MergeMany](publishers/mergemany.md), [Multicast](publishers/multicast.md), [Output](publishers/output.md), [PrefixUntilOutput](publishers/prefixuntiloutput.md), [PrefixWhile](publishers/prefixwhile.md), [Print](publishers/print.md), [ReceiveOn](publishers/receiveon.md), [Reduce](publishers/reduce.md), [RemoveDuplicates](publishers/removeduplicates.md), [ReplaceEmpty](publishers/replaceempty.md), [ReplaceError](publishers/replaceerror.md), [Retry](publishers/retry.md), [Scan](publishers/scan.md), [Sequence](publishers/sequence.md), [SetFailureType](publishers/setfailuretype.md), [Share](publishers/share.md), [SubscribeOn](publishers/subscribeon.md), [SwitchToLatest](publishers/switchtolatest.md), [Throttle](publishers/throttle.md), [Timeout](publishers/timeout.md), [TryAllSatisfy](publishers/tryallsatisfy.md), [TryCatch](publishers/trycatch.md), [TryCompactMap](publishers/trycompactmap.md), [TryComparison](publishers/trycomparison.md), [TryContainsWhere](publishers/trycontainswhere.md), [TryDropWhile](publishers/trydropwhile.md), [TryFilter](publishers/tryfilter.md), [TryFirstWhere](publishers/tryfirstwhere.md), [TryLastWhere](publishers/trylastwhere.md), [TryMap](publishers/trymap.md), [TryPrefixWhile](publishers/tryprefixwhile.md), [TryReduce](publishers/tryreduce.md), [TryRemoveDuplicates](publishers/tryremoveduplicates.md), [TryScan](publishers/tryscan.md), [Zip](publishers/zip.md), [Zip3](publishers/zip3.md), [Zip4](publishers/zip4.md), [Record](record.md)

## Topics

### Declaring supporting types

- [Output](publisher/output.md) — The kind of values published by this publisher.
- [Failure](publisher/failure.md) — The kind of errors this publisher might publish.

### Working with subscribers

- [receive(subscriber:)](<publisher/receive(subscriber_).md>) — Attaches the specified subscriber to this publisher.
- [subscribe(_:)](<publisher/subscribe(__)-4u8kn.md>) — Attaches the specified subscriber to this publisher.
- [subscribe(_:)](<publisher/subscribe(__)-3fk20.md>) — Attaches the specified subject to this publisher.

### Mapping elements

- [map(_:)](<publisher/map(__)-99evh.md>) — Transforms all elements from the upstream publisher with a provided closure.
- [tryMap(_:)](<publisher/trymap(__).md>) — Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [mapError(_:)](<publisher/maperror(__).md>) — Converts any failure from the upstream publisher into a new error.
- [replaceNil(with:)](<publisher/replacenil(with_).md>) — Replaces nil elements in the stream with the provided element.
- [scan(_:_:)](<publisher/scan(____).md>) — Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [tryScan(_:_:)](<publisher/tryscan(____).md>) — Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [setFailureType(to:)](<publisher/setfailuretype(to_).md>) — Changes the failure type declared by the upstream publisher.

### Filtering elements

- [filter(_:)](<publisher/filter(__).md>) — Republishes all elements that match a provided closure.
- [tryFilter(_:)](<publisher/tryfilter(__).md>) — Republishes all elements that match a provided error-throwing closure.
- [compactMap(_:)](<publisher/compactmap(__).md>) — Calls a closure with each received element and publishes any returned optional that has a value.
- [tryCompactMap(_:)](<publisher/trycompactmap(__).md>) — Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [removeDuplicates()](<publisher/removeduplicates().md>) — Publishes only elements that don’t match the previous element.
- [removeDuplicates(by:)](<publisher/removeduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [tryRemoveDuplicates(by:)](<publisher/tryremoveduplicates(by_).md>) — Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [replaceEmpty(with:)](<publisher/replaceempty(with_).md>) — Replaces an empty stream with the provided element.
- [replaceError(with:)](<publisher/replaceerror(with_).md>) — Replaces any errors in the stream with the provided element.

### Reducing elements

- [collect()](<publisher/collect().md>) — Collects all received elements, and emits a single array of the collection when the upstream publisher finishes.
- [collect(_:)](<publisher/collect(__).md>) — Collects up to the specified number of elements, and then emits a single array of the collection.
- [collect(_:options:)](<publisher/collect(__options_).md>) — Collects elements by a given time-grouping strategy, and emits a single array of the collection.
- [TimeGroupingStrategy](publishers/timegroupingstrategy.md) — A strategy for collecting received elements.
- [ignoreOutput()](<publisher/ignoreoutput().md>) — Ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [reduce(_:_:)](<publisher/reduce(____).md>) — Applies a closure that collects each element of a stream and publishes a final result upon completion.
- [tryReduce(_:_:)](<publisher/tryreduce(____).md>) — Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.

### Applying mathematical operations on elements

- [count()](<publisher/count().md>) — Publishes the number of elements received from the upstream publisher.
- [max()](<publisher/max().md>) — Publishes the maximum value received from the upstream publisher, after it finishes.
- [max(by:)](<publisher/max(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided ordering closure.
- [tryMax(by:)](<publisher/trymax(by_).md>) — Publishes the maximum value received from the upstream publisher, using the provided error-throwing closure to order the items.
- [min()](<publisher/min().md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [min(by:)](<publisher/min(by_).md>) — Publishes the minimum value received from the upstream publisher, after it finishes.
- [tryMin(by:)](<publisher/trymin(by_).md>) — Publishes the minimum value received from the upstream publisher, using the provided error-throwing closure to order the items.

### Applying matching criteria to elements

- [contains(_:)](<publisher/contains(__).md>) — Publishes a Boolean value upon receiving an element equal to the argument.
- [contains(where:)](<publisher/contains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the predicate closure.
- [tryContains(where:)](<publisher/trycontains(where_).md>) — Publishes a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [allSatisfy(_:)](<publisher/allsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [tryAllSatisfy(_:)](<publisher/tryallsatisfy(__).md>) — Publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

### Applying sequence operations to elements

- [drop(untilOutputFrom:)](<publisher/drop(untiloutputfrom_).md>) — Ignores elements from the upstream publisher until it receives an element from a second publisher.
- [dropFirst(_:)](<publisher/dropfirst(__).md>) — Omits the specified number of elements before republishing subsequent elements.
- [drop(while:)](<publisher/drop(while_).md>) — Omits elements from the upstream publisher until a given closure returns false, before republishing all remaining elements.
- [tryDrop(while:)](<publisher/trydrop(while_).md>) — Omits elements from the upstream publisher until an error-throwing closure returns false, before republishing all remaining elements.
- [append(_:)](<publisher/append(__)-1qb8d.md>) — Appends a publisher’s output with the specified elements.
- [append(_:)](<publisher/append(__)-69sdn.md>) — Appends a publisher’s output with the specified sequence.
- [append(_:)](<publisher/append(__)-5yh02.md>) — Appends the output of this publisher with the elements emitted by the given publisher.
- [prepend(_:)](<publisher/prepend(__)-7wk5l.md>) — Prefixes a publisher’s output with the specified values.
- [prepend(_:)](<publisher/prepend(__)-v9sb.md>) — Prefixes a publisher’s output with the specified sequence.
- [prepend(_:)](<publisher/prepend(__)-5dj9c.md>) — Prefixes the output of this publisher with the elements emitted by the given publisher.
- [prefix(_:)](<publisher/prefix(__).md>) — Republishes elements up to the specified maximum count.
- [prefix(while:)](<publisher/prefix(while_).md>) — Republishes elements while a predicate closure indicates publishing should continue.
- [tryPrefix(while:)](<publisher/tryprefix(while_).md>) — Republishes elements while an error-throwing predicate closure indicates publishing should continue.
- [prefix(untilOutputFrom:)](<publisher/prefix(untiloutputfrom_).md>) — Republishes elements until another publisher emits an element.

### Selecting specific elements

- [first()](<publisher/first().md>) — Publishes the first element of a stream, then finishes.
- [first(where:)](<publisher/first(where_).md>) — Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [tryFirst(where:)](<publisher/tryfirst(where_).md>) — Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [last()](<publisher/last().md>) — Publishes the last element of a stream, after the stream finishes.
- [last(where:)](<publisher/last(where_).md>) — Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [tryLast(where:)](<publisher/trylast(where_).md>) — Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [output(at:)](<publisher/output(at_).md>) — Publishes a specific element, indicated by its index in the sequence of published elements.
- [output(in:)](<publisher/output(in_).md>) — Publishes elements specified by their range in the sequence of published elements.

### Collecting and republishing the latest elements from multiple publishers

- [combineLatest(_:_:)](<publisher/combinelatest(____)-1n30g.md>) — Subscribes to an additional publisher and invokes a closure upon receiving output from either publisher.
- [combineLatest(_:)](<publisher/combinelatest(__).md>) — Subscribes to an additional publisher and publishes a tuple upon receiving output from either publisher.
- [combineLatest(_:_:_:)](<publisher/combinelatest(______)-6ekpz.md>) — Subscribes to two additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:)](<publisher/combinelatest(____)-5crqg.md>) — Subscribes to two additional publishers and publishes a tuple upon receiving output from any of the publishers.
- [combineLatest(_:_:_:_:)](<publisher/combinelatest(________).md>) — Subscribes to three additional publishers and invokes a closure upon receiving output from any of the publishers.
- [combineLatest(_:_:_:)](<publisher/combinelatest(______)-48buc.md>) — Subscribes to three additional publishers and publishes a tuple upon receiving output from any of the publishers.

### Republishing elements from multiple publishers as an interleaved stream

- [merge(with:)](<publisher/merge(with_)-7fk3a.md>) — Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.
- [merge(with:)](<publisher/merge(with_)-7qt71.md>) — Combines elements from this publisher with those from another publisher, delivering an interleaved sequence of elements.
- [merge(with:_:)](<publisher/merge(with___).md>) — Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:)](<publisher/merge(with_____).md>) — Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:)](<publisher/merge(with_______).md>) — Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:)](<publisher/merge(with_________).md>) — Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:)](<publisher/merge(with___________).md>) — Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:_:)](<publisher/merge(with_____________).md>) — Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.

### Collecting and republishing the oldest unconsumed elements from multiple publishers

- [zip(_:)](<publisher/zip(__).md>) — Combines elements from another publisher and deliver pairs of elements as tuples.
- [zip(_:_:)](<publisher/zip(____)-4xn21.md>) — Combines elements from another publisher and delivers a transformed output.
- [zip(_:_:)](<publisher/zip(____)-8d7k7.md>) — Combines elements from two other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:)](<publisher/zip(______)-9yqi1.md>) — Combines elements from two other publishers and delivers a transformed output.
- [zip(_:_:_:)](<publisher/zip(______)-16rcy.md>) — Combines elements from three other publishers and delivers groups of elements as tuples.
- [zip(_:_:_:_:)](<publisher/zip(________).md>) — Combines elements from three other publishers and delivers a transformed output.

### Republishing elements by subscribing to new publishers

- [flatMap(maxPublishers:_:)](<publisher/flatmap(maxpublishers___)-3k7z5.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<publisher/flatmap(maxpublishers___)-qxf.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<publisher/flatmap(maxpublishers___)-hyb0.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<publisher/flatmap(maxpublishers___)-4of8w.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [switchToLatest()](<publisher/switchtolatest()-453ht.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<publisher/switchtolatest()-1c51y.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<publisher/switchtolatest()-20v3t.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<publisher/switchtolatest()-9eb3r.md>) — Republishes elements sent by the most recently received publisher.

### Handling errors

- [assertNoFailure(_:file:line:)](<publisher/assertnofailure(__file_line_).md>) — Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [catch(_:)](<publisher/catch(__).md>) — Handles errors from an upstream publisher by replacing it with another publisher.
- [tryCatch(_:)](<publisher/trycatch(__).md>) — Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.
- [retry(_:)](<publisher/retry(__).md>) — Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.

### Controlling timing

- [measureInterval(using:options:)](<publisher/measureinterval(using_options_).md>) — Measures and emits the time interval between events received from an upstream publisher.
- [debounce(for:scheduler:options:)](<publisher/debounce(for_scheduler_options_).md>) — Publishes elements only after a specified time interval elapses between events.
- [delay(for:tolerance:scheduler:options:)](<publisher/delay(for_tolerance_scheduler_options_).md>) — Delays delivery of all output to the downstream receiver by a specified amount of time on a particular scheduler.
- [throttle(for:scheduler:latest:)](<publisher/throttle(for_scheduler_latest_).md>) — Publishes either the most-recent or first element published by the upstream publisher in the specified time interval.
- [timeout(_:scheduler:options:customError:)](<publisher/timeout(__scheduler_options_customerror_).md>) — Terminates publishing if the upstream publisher exceeds the specified time interval without producing an element.

### Encoding and decoding

- [encode(encoder:)](<publisher/encode(encoder_).md>) — Encodes the output from upstream using a specified encoder.
- [decode(type:decoder:)](<publisher/decode(type_decoder_).md>) — Decodes the output from the upstream using a specified decoder.

### Identifying properties with key paths

- [map(_:)](<publisher/map(__)-6sm0a.md>) — Publishes the value of a key path.
- [map(_:_:)](<publisher/map(____).md>) — Publishes the values of two key paths as a tuple.
- [map(_:_:_:)](<publisher/map(______).md>) — Publishes the values of three key paths as a tuple.

### Working with multiple subscribers

- [multicast(_:)](<publisher/multicast(__).md>) — Applies a closure to create a subject that delivers elements to subscribers.
- [multicast(subject:)](<publisher/multicast(subject_).md>) — Provides a subject to deliver elements to multiple subscribers.
- [share()](<publisher/share().md>) — Shares the output of an upstream publisher with multiple subscribers.

### Buffering elements

- [buffer(size:prefetch:whenFull:)](<publisher/buffer(size_prefetch_whenfull_).md>) — Buffers elements received from an upstream publisher.
- [PrefetchStrategy](publishers/prefetchstrategy.md) — A strategy for filling a buffer.
- [BufferingStrategy](publishers/bufferingstrategy.md) — A strategy that handles exhaustion of a buffer’s capacity.

### Performing type erasure

- [eraseToAnyPublisher()](<publisher/erasetoanypublisher().md>) — Wraps this publisher with a type eraser.

### Specifying schedulers

- [subscribe(on:options:)](<publisher/subscribe(on_options_).md>) — Specifies the scheduler on which to perform subscribe, cancel, and request operations.
- [receive(on:options:)](<publisher/receive(on_options_).md>) — Specifies the scheduler on which to receive elements from the publisher.

### Adding explicit connectability

- [makeConnectable()](<publisher/makeconnectable().md>) — Creates a connectable wrapper around the publisher.

### Connecting simple subscribers

- [assign(to:on:)](<publisher/assign(to_on_).md>) — Assigns each element from a publisher to a property on an object.
- [assign(to:)](<publisher/assign(to_).md>) — Republishes elements received from a publisher, by assigning them to a property marked as a publisher.
- [sink(receiveCompletion:receiveValue:)](<publisher/sink(receivecompletion_receivevalue_).md>) — Attaches a subscriber with closure-based behavior.
- [sink(receiveValue:)](<publisher/sink(receivevalue_).md>) — Attaches a subscriber with closure-based behavior to a publisher that never fails.

### Accessing elements asynchronously

- [values](publisher/values-1dm9r.md) — The elements produced by the publisher, as an asynchronous sequence.
- [values](publisher/values-v7nz.md) — The elements produced by the publisher, as a throwing asynchronous sequence.

### Debugging

- [breakpoint(receiveSubscription:receiveOutput:receiveCompletion:)](<publisher/breakpoint(receivesubscription_receiveoutput_receivecompletion_).md>) — Raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [breakpointOnError()](<publisher/breakpointonerror().md>) — Raises a debugger signal upon receiving a failure.
- [handleEvents(receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<publisher/handleevents(receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) — Performs the specified closures when publisher events occur.
- [print(_:to:)](<publisher/print(__to_).md>) — Prints log messages for all publishing events.

## See Also

### Publishers

- [Publishers](publishers.md) — A namespace for types that serve as publishers.
- [AnyPublisher](anypublisher.md) — A publisher that performs type erasure by wrapping another publisher.
- [Published](published.md) — A type that publishes a property marked with an attribute.
- [Cancellable](cancellable.md) — A protocol indicating that an activity or action supports cancellation.
- [AnyCancellable](anycancellable.md) — A type-erasing cancellable object that executes a provided closure when canceled.
