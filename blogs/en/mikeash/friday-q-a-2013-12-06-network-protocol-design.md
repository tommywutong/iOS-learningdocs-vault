---
title: 'Friday Q&A 2013-12-06: Network Protocol Design'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-12-06-network-protocol-design.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:25bd98b91df725c2'
translated: false
---

> 原文：[Friday Q&A 2013-12-06: Network Protocol Design](https://www.mikeash.com/pyblog/friday-qa-2013-12-06-network-protocol-design.html)　·　mikeash.com Friday Q&A

Posted at 2013-12-06 13:29 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-01-10: Let's Break Cocoa](https://www.mikeash.com/pyblog/friday-qa-2014-01-10-lets-break-cocoa.html)  
Previous article: [VoodooPad Acquisition](https://www.mikeash.com/pyblog/voodoopad-acquisition.html)  
Tags: [design](https://www.mikeash.com/pyblog/?tag=design) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [networking](https://www.mikeash.com/pyblog/?tag=networking)

Friday Q&A 2013-12-06: Network Protocol Design

by [Mike Ash](https://www.mikeash.com/)

**TCP and UDP**  
I imagine readers already know about TCP and UDP, but just in case you don't or need a refresher, I want to briefly cover that.

The base level internet protocol is called, imaginatively, Internet Protocol. There are several versions, of which the most common are version 4 and version 6, referred to as IPv4 and IPv6. These protocols handle the very basic routing and addressing tasks of network communication.

Smarter protocols are layered on top of that. There are a lot of protocols out there, but two are by far the most commonly used: TCP and UDP. UDP (User Datagram Protocol) is a simple layer on top of IP which provides the ability to address individual _ports_ on a particular computer and optional checksumming for data integrity. Data is still sent as individual packets which can be lost, duplicated, or received out of order.

TCP (Transmission Control Protocol) is a more complex and capable protocol. It abstracts away the unreliable packet-based nature of the internet and provides the application with a plain stream interface, where bytes are transmitted on one end and received on the other. It automatically retransmits lost data and ensures proper ordering.

Which one to choose depends on your needs. If you want a stream of bytes with reliable delivery then TCP is the obvious choice. However, TCP's insistence on recovering lost data can hurt performance. In cases, such as games, where you'd rather skip over a lost packet rather than wait for it to be retransmitted, TCP's smarts can slow you down. Because of this, UDP is a good choice for realtime games, low-latency audio/video streaming, and other similar tasks.

**Multiple Connections**  
A lot of complex protocols use multiple simultaneous connections. There might be one TCP connection for session initiation and control, another TCP connection for bulk data transmission, a UDP connection for time-sensitive data, etc.

Whatever you do, don't do this. It may seem simpler to keep things separated, but it ends up massively complicating a protocol. It means that each side has to manage multiple sockets instead of just one. It means that the wire protocol must now be aware of the underlying transport protocol, and suddenly a bunch of code that otherwise wouldn't care now has to know the difference between IPv4 and IPv6. It also plays havoc with NAT and firewalls, since you now have to open up several ports instead of just one, and some of those ports might be dynamically chosen and thus difficult to whitelist on a firewall.

Always use a single connection. If you need to support multiple streams, use a base protocol that handles multiplexing multiple streams over a single connection. If some data needs TCP and other data needs UDP, then your best option is to reimplement the necessary TCP features on top of UDP. If you want to stream large amounts of data, then write code to break it up into chunks and send them individually. It's a nice idea in the abstract to just open a separate TCP connection and let the socket library handle it for you, but it's ultimately not worth it.

**Handshake**  
It's often handy to exchange a handshake between the two sides before beginning the transmission of actual data. Starting the transmission with some sort of identifier (e.g. your app's bundle ID) can help make it clear what's generating the traffic and keep accidental connections from other software from proceeding too far.

Version information can be extremely helpful when extending the protocol as your software evolved. I like to transmit a major version number and a minor version number, both of which are plain integers and not intended to synchronize with the software's human-readable version number. Minor version numbers are intended to indicate optional capabilities or known quirks of older versions, but a mismatch should still allow the connection to proceed. A major version number mismatch should be used to indicate that communication is impossible. Transmitting that information allows whichever one has the later version to fall back to the earlier one if you've written it to still support the old version.

**Framing**  
TCP connections generally need some sort of framing to indicate where one chunk of data ends and the next chunk begins. This might be used to separate multiple commands or requests or chunks of data. It's possible to roll your framing into your general data format, but it's a good idea to keep the two separate. By having a framing protocol that simply keeps chunks of arbitrary data separated, you end up with more reusable code. The protocol is also generally easier to understand and debug, since you can consider the framing protocol and the inner data protocol separately.

An easy way to build a framing protocol is with length prefixing. Transmit the length of the frame in bytes, then transmit the frame data, then repeat. The length can either be binary or text depending on your desires. This is easy to read and write, but doesn't work well for large streaming data since you have to know how large the frame will be before you can transmit any of it.

One nice framing protocol is Consistent Overhead Byte Stuffing or COBS. This works by terminating each frame with a zero byte, and then encoding the data within the frame to eliminate all instances of the zero byte. This incurs a small amount of overhead, less than 1% of the length of the data. The encoding is suitable for streaming data and takes little CPU power.

**Text Versus Binary**  
The question of whether a data format should be text or binary is a long-running one with no resolution. Sometimes there are constraints that make it obvious. For example, media data is far more suitably stored in a binary format because of the quantity of data involved. Data that's intended to be human-readable in its raw format should be text, since humans have a hard time reading binary.

In other cases, the question of text versus binary isn't so clear. That question is currently playing out in the world of HTTP, where the largely text-based version 1.1 is currently being replaced by the binary-based version 2.0. Binary is more efficient, but text is often easier to work with.

When in doubt, lean towards a text-based protocol. The ability to telnet into your half-implemented server from the command line and read the wire protocol in a sniffer without extra work can really speed development.

**Text Formats**  
There are a lot of possibilities within the realm of text formats. The traditional formats tend to be line-delimited ad-hoc formats that haven't necessarily grown all that well. For example, HTTP was a decent enough protocol for transmitting hypertext, but it has grown more and more hacks over time to deal with media files, pipelined connections, streams, and resumed downloads, in a way that fits into the original design.

Something like JSON or Apple property lists can be an excellent fit for this. The protocol can be designed at a higher level in terms of dictionaries, maps, strings, etc., and then that can be encoded using a standard, readable format for sending over the wire.

One interesting advantage of property lists is that you can use the XML format when prototyping, then switch over to the binary format once the network code is solid to get better performance. The disadvantage, of course, is that support for property lists on non-Apple platforms is not as good.

Always consider extensibility. For JSON and property lists, that means that the top-level object should _never_ be an array, or anything but a dictionary. This allows adding additional keys at any time, and older versions of the software will simply ignore them.

I've encountered software that provided dictionaries with arbitrary keys and the receiver was intended to iterate over them all. This effectively provided an array of key/value pairs and suffered from the same extensibility problems that an array would. Don't do this.

**Binary Formats**  
Although I prefer text when it's reasonable, sometimes you really just need a binary format, either for performance reasons or just because it's just more suitable for your data.

[Google Protocol Buffers](https://code.google.com/p/protobuf/), or protobufs, can be a great choice here. They're structured enough to give most of the benefits of property lists or JSON, but still provide the performance advantages of a binary format. They work a bit differently from most common serialization libraries, in that you write a format definition which is then compiled into code which you include with the app. The compiled code then knows how to encode and decode protobufs that conform to your format. This makes them a little less natural to use in a project, since that generated code has to be included somehow, but it also means that the resulting code is fast.

If you want to make your own completely custom binary format, then there are a few guidelines which can make your life easier.

Whenever reasonable, make the overall format extensible. Far too many formats are specified as a fixed number of fixed-width fields. When another field is added, chaos ensues as a whole new version of the format has to be used, and any code that wants to work with both needs to start special-casing the new fields. Instead, give each field a name, even something as simple as a four-character code, and write the code to be able to handle fields in any order by looking at the field names. Also specify each field's length in the data itself, so that a reader that doesn't know about a field can still skip over its data and keep reading additional fields that it does know about.

When storing raw integers, you have to make a choice between storing them as big-endian (most significant byte first) or little-endian (least significant byte first). Technically, you can support both by adding a flag to indicate which one a particular field is using, but that's complete madness. Making this choice should be simple: _use big-endian_. It's not a particularly natural choice these days, as we almost always run our code on little-endian computers (x86 is always little-endian, and iOS runs ARM in little-endian mode). However, big-endian is defined as the "network byte order" and is the standard byte order used in protocols like IP and TCP. This is a case where it's best not to rock the boat. Do what everyone else does, and use network byte order (i.e. big-endian) to transmit your binary numbers over the network.

Also consider whether your integer data should have a fixed width at all. It's tempting to just say "this is a 32-bit value" and move on, but this can cause trouble. In the event that you need that value to contain something larger than 232-1, you're screwed. In the more likely event that most of the values stored in that field are small, you waste bytes. A variable-length integer encoding can solve these problems nicely. If you're already transmitting the length of a field in the format, then you can take advantage of that to use only the bytes you actually need to represent the number. If you're transmitting a value less than 256, write out only a single byte. If you're transmitting a value less than 65,536, write out two bytes. For places where this is not suitable (e.g. encoding the length field itself), you can use a variable-length integer encoding.

A common way to encode variable-length integers is to borrow the top bit of each byte to indicate whether or not you've reached the end of the number. A byte with a `1` in the top bit indicates that more bytes follow. A byte with a `0` in the top bit indicates that this is the last byte. Numbers are then encoded seven bits at a time, with the eighth bit set to `0` only in the last byte. The decoder can then read bytes until it sees a top bit of `0`, and construct the number from the other seven bits in each byte. Wikipedia refers to this as a [variable-length quantity](http://en.wikipedia.org/wiki/Variable-length_quantity), and variants are used in a lot of different data formats.

Finally, let's talk about text. A binary format still often needs to store text such as metadata or user input. There are many ways to represent text, but once again the choice is simple: use UTF-8. Don't use any other encoding, don't even _think_ about using any other encoding. Use UTF-8 and be done.

There are several reasons to prefer UTF-8. First, it can represent any text that can be represented in Unicode, which is nearly anything. Second, it's extremely unlikely for text encoded with a different encoding to produce data that decodes as valid (but incorrect) UTF-8, meaning you can have high confidence that your decoded UTF-8 string really was encoded with UTF-8. Third, UTF-8 is identical to ASCII when encoding character in ASCII, which makes UTF-8 strings easy to read by hand and easy to work with. Fourth, UTF-8 is reasonably space-efficient in the best case, and only slightly less efficient than other Unicode encodings in the worst case.

Also make sure that text is stored in a variable-length format, either with a length prefix or by using a terminating zero byte. The same reasons apply here as did for text, but even more so. Text length varies far more than integer length, and fixed-width text fields are a good way to go straight to the crazy house.

**Conclusion**  
Custom network protocols aren't a common need, but they still appear from time to time. First, decide between TCP and UDP based on your needs. Run everything over a single connection, with multiplexing handled internally to the protocol if it's needed. Use a separate framing protocol when running over TCP rather than trying to delimit your data within the format. Prefer text-based formats when possible, and build extensible, sane binary formats when it makes sense to. Use UTF-8 for all text everywhere.

That's it for today. Come back next time for more creamy goodness. Friday Q&A is driven by reader suggestions, so if you have a suggestion for a topic, [please send it in](mailto:mike@mikeash.com).

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.
