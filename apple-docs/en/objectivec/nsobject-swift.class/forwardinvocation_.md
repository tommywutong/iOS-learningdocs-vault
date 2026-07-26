---
title: 'forwardInvocation:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/forwardinvocation:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/forwardinvocation:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/forwardinvocation%3A.json'
content_hash: 'sha256:73607d864288930a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# forwardInvocation:

<sub>Instance Method</sub>

Overridden by subclasses to forward messages to other objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) forwardInvocation:(NSInvocation *) anInvocation;
```

## Parameters

- `anInvocation` — The invocation to forward.

## Discussion

When an object is sent a message for which it has no corresponding method, the runtime system gives the receiver an opportunity to delegate the message to another receiver. It delegates the message by creating an `NSInvocation` object representing the message and sending the receiver a [forwardInvocation:](forwardinvocation_.md) message containing this `NSInvocation` object as the argument. The receiver’s [forwardInvocation:](forwardinvocation_.md) method can then choose to forward the message to another object. (If that object can’t respond to the message either, it too will be given a chance to forward it.)

The [forwardInvocation:](forwardinvocation_.md) message thus allows an object to establish relationships with other objects that will, for certain messages, act on its behalf. The forwarding object is, in a sense, able to “inherit” some of the characteristics of the object it forwards the message to.

> [!important] Important
> To respond to methods that your object does not itself recognize, you must override [methodSignatureForSelector:](methodsignatureforselector_.md) in addition to [forwardInvocation:](forwardinvocation_.md). The mechanism for forwarding messages uses information obtained from [methodSignatureForSelector:](methodsignatureforselector_.md) to create the `NSInvocation` object to be forwarded. Your overriding method must provide an appropriate method signature for the given selector, either by pre formulating one or by asking another object for one.

An implementation of the [forwardInvocation:](forwardinvocation_.md) method has two tasks:

- To locate an object that can respond to the message encoded in `anInvocation`. This object need not be the same for all messages.
- To send the message to that object using `anInvocation`. `anInvocation` will hold the result, and the runtime system will extract and deliver this result to the original sender.

In the simple case, in which an object forwards messages to just one destination (such as the hypothetical `friend` instance variable in the example below), a [forwardInvocation:](forwardinvocation_.md) method could be as simple as this:

```objc
- (void)forwardInvocation:(NSInvocation *)invocation
{
    SEL aSelector = [invocation selector];
 
    if ([friend respondsToSelector:aSelector])
        [invocation invokeWithTarget:friend];
    else
        [super forwardInvocation:invocation];
}
```

The message that’s forwarded must have a fixed number of arguments; variable numbers of arguments (in the style of `printf()`) are not supported.

The return value of the forwarded message is returned to the original sender. All types of return values can be delivered to the sender: `id` types, structures, double-precision floating-point numbers.

Implementations of the [forwardInvocation:](forwardinvocation_.md) method can do more than just forward messages. [forwardInvocation:](forwardinvocation_.md) can, for example, be used to consolidate code that responds to a variety of different messages, thus avoiding the necessity of having to write a separate method for each selector. A [forwardInvocation:](forwardinvocation_.md) method might also involve several other objects in the response to a given message, rather than forward it to just one.

`NSObject`‘s implementation of [forwardInvocation:](forwardinvocation_.md) simply invokes the [- doesNotRecognizeSelector:](<doesnotrecognizeselector(__).md>) method; it doesn’t forward any messages. Thus, if you choose not to implement [forwardInvocation:](forwardinvocation_.md), sending unrecognized messages to objects will raise exceptions.

## See Also

### Forwarding Messages

- [- forwardingTargetForSelector:](<forwardingtarget(for_).md>) — Returns the object to which unrecognized messages should first be directed.
