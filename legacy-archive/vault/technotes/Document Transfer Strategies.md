---
title: Document Transfer Strategies
apple_id: DTS40009179
resource_type: Technical Note
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-07-26'
source_url: https://developer.apple.com/library/archive/technotes/tn2152/_index.html
archived_at: '2026-07-26T19:54:09.692562Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2152

# Document Transfer Strategies

One of the questions most frequently asked by iOS developers is, how can I transfer data between my application running on the user's device and my application running on the user's computer. This technote describes the nature of the problem and outlines the various paths to a solution.

Primarily this technote addresses developers working on iOS. However, many of the techniques described herein apply equally well to Mac OS X, so even developers working exclusively on Mac OS X might find it interesting.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mi)[Networking Problems With Common Solutions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mq)[Reliability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyza)[Bandwidth](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyzq)[Latency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjy2a)[Malicious Attack](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjy2q)[Networking Problems With Architecture-Specific Solutions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4ny)[Service Discovery](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjy3q)[Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjy4a)[On-The-Wire Privacy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjy4q)[On TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mjr)[Networking Designs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mjs)[WWAN Link-Layer Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyyte)[Wi-Fi Link Layer Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyytg)[Bluetooth Link Layer Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyyti)[Solutions For Centralized Server Designs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mjw)[Service Discovery](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyytm)[Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyyto)[On-The-Wire Privacy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyytq)[Renting Infrastructure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyyts)[Solutions For Peer-To-Peer Designs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mrr)[Service Discovery](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyzdc)[Authorization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyzde)[On-The-Wire Privacy](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyzdi)[On GameKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjvkqstivbviskpjyzdk)[Protocol Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mrx)[File Transfer Protocols](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mry)[Syncing Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewugsbrfvjukq2ujfhu4mrz)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsmjxhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Many iOS applications need the ability to transfer data between the user's computer and their iOS device, or between two iOS devices. For example:

- A PDF viewing application needs a way to get PDF files on to the device.
- An iOS to-do list application that has a Mac OS X equivalent needs to sync to-do lists between the application running on the device and the application running on the Mac.
- An iOS application with 'lite' and 'pro' versions needs to transfer data between these versions.
- An iOS note-taking application needs to provide an easy way to backup and restore these notes, independently of the standard iTunes backup mechanism.

Starting with iOS 3.2 on iPad, Apple introduced a file sharing technology (`UIFileSharingEnabled`) that allows an application to expose its Documents directory to the user through iTunes. The user can then move files back and forth between their device and their computer. Moreover, iOS 4 has brought this feature to both iPhone and iPod touch.

You can learn more about iTunes file sharing in the [File-Sharing Support](https://developer.apple.com/iphone/library/releasenotes/General/WhatsNewIniPhoneOS/Articles/iPhoneOS3_2.html#//apple_ref/doc/uid/TP40009337-SW11) section of [What's New in iPhone OS](https://developer.apple.com/iphone/library/releasenotes/General/WhatsNewIniPhoneOS/Introduction/Introduction.html).

iTunes file sharing does not, however, solve all document transfer problems. For example:

- It requires iOS 3.2 or later. If you must support older versions of iOS, file sharing is not an option.
- It does not support device-to-device document transfers.
- It is only supported over USB; the user has to plug in their device.

In these circumstances it is necessary to implement your own transfer mechanism based on TCP/IP networking. If you're not familiar with network programming this can be a very daunting task. All network code must deal with certain hard problems, and if you're new to the field you may not even understand the problems, let alone know how to solve them.

The remainder of this document describes the problems you must solve, the two standard designs you can use to address those problems and, within each design, the specific techniques you can use. There's an emphasis on Apple technologies, but you must keep in mind that, if you're targeting general iOS users, your user's computer may be a Windows PC.

__Note:__ Much of the information in this document was presented at WWDC 2010 in the "Network Apps for iPhone OS" talk (part 1 and 2, sessions 207 and 208). If you prefer listening to reading, you should check out the [session videos](https://developer.apple.com/videos/wwdc/2010/).

[Back to Top](#)

## Networking Problems With Common Solutions

Any networking code must deal with a certain set of fundamental problems. Some of these problems have solutions that apply regardless of your overall networking design. The following subsections describe these problems and their solutions.

### Reliability

The network may drop, delay, reorder, or corrupt the packets you send. Moreover, the entire network may come and go. All of these problems are more prevalent on mobile devices than on standard computers. Your application must handle all of these problems gracefully.

The weapon of choice here is TCP. When you open a TCP connection between two networked peers, you are guaranteed one of two results:

- data you send will be transferred intact and in order, or
- the connection will break

TCP takes care of all the fiddly details required to make this work; unless you're a networking expert, you should avoid reinventing this particular wheel and use TCP, or some higher-level protocol layered on top of TCP, for your communications.

### Bandwidth

Every network has a limit to the amount of data that you can move through the network per unit of time. [Wireless wide-area networks](http://en.wikipedia.org/wiki/Wireless_Wide_Area_Network) (WWANs) present a serious bandwidth challenge; that is, the bandwidth of a WWAN is low compared to the typical data size of a modern application. You must keep this limitation in mind when designing your application.

There may also be non-technical aspects of the bandwidth problem. Many iPhone users must pay for their bandwidth, either on a per-megabyte basis, or once they cross some threshold. Your application must respect this reality.

### Latency

Every network takes time to move data between the two communicating peers; that delay is known as the latency. Latency is typically expressed in terms of a round trip time, which is the time it takes for a packet to go from the source to the destination peer, plus the time it takes for a reply packet to make the return trip.

Depending on the network protocol you're using, latency can seriously impact your network performance. For example, let's say you want to move five packets of data from one machine to another. You have two design choices:

1. send #1, wait for ack, send #2, wait for ack, and so on
2. send #1 through #5, wait for all the acks

Someone new to networking might choose option 1 because it's easier to implement; that would be a mistake. Consider what happens if the round trip latency is 200 ms (a typical value in the wider Internet). Option 1 will take at least one second to transfer the five packets, __regardless of the network bandwidth__. The alternative, option 2, will transfer the same data in a little over 200 ms.

Latency is an especially bad problem on WWANs. Current WWAN technology will typically introduce a 200-300 ms latency in the first hop!

### Malicious Attack

Whenever you communicate on the Internet you open yourself up to malicious attack. In the worst-case scenario an attacker can craft a packet that causes your application to execute arbitrary code, at which point the attacker can take over the machine on which you're running and turn it into a [zombie](http://en.wikipedia.org/wiki/Zombie_computer). You must carefully check all data that you receive from the network to prevent this.

iOS is less vulnerable to this sort of problem than Mac OS X because iOS puts strict limits on what memory within your process can be executed as code. Do not use this as an excuse to be complacent about this issue! Malicious attackers are continually finding new ways to exploit bugs like this.

[Back to Top](#)

## Networking Problems With Architecture-Specific Solutions

Any networking code must deal with a certain set of fundamental problems. Some of these problems can only be solved in the context of your overall architecture. The following subsections describe these problems; their solutions are described in the later sections that discuss specific networking designs.

### Service Discovery

Service discovery is the process whereby networking peers learn about the existence and address of other networking peers. Back in the day, service discovery was a challenging problem in some cases. These days there are simple solutions for this problem, although the approach you use depends on your networking architecture.

See Solutions For Centralized Server Designs for information about service discovery in a centralized server architecture, and Solutions For Peer-To-Peer Designs for information about peer-to-peer service discovery.

### Authorization

It's obvious that your application must authorize its communications: your application is the guardian of the user's data—it mustn't hand that data over to just anyone.

What's less obvious is that authorization must be mutual. If you're new to networking you might implement an authorization protocol like:

1. client connects to server
2. client sends the password
3. server checks password and, if it's incorrect, disconnects
4. if the server didn't disconnect, the client sends the data

Protocols like this are susceptible to impersonation. Someone can run a server that pretends to be the real server, and that server, in step 3, always allows the client to connect regardless of the password sent in step 2. Your client will connect to such a server, successfully 'authorize', and then transmit the user's valuable data to the imposter.

Worse yet, the imposter now has a copy of the user's password, which is particularly bad if, like many people, the user uses the same password for a variety of services.

The solution to the overall authorization problem will depend on your networking design, as described in Solutions For Centralized Server Designs and Solutions For Peer-To-Peer Designs.

### On-The-Wire Privacy

You must assume that malicious users are looking at every piece of data you transfer over the network. If you ever transfer any data that might be considered personal in the least way, you must ensure that this data is encrypted on the wire.

In general I recommend that you err on the side of caution and consider all user data to be personal. This is because data that you might not consider especially sensitive might be very sensitive in certain contexts. For example, if you're implementing a remote control application for a home media server, you might not consider the names of the tracks to be sensitive, but it's not hard to imagine at least two scenarios where a user might.

The exact details of your solution to the privacy problem will depend on your overall networking design; see Solutions For Centralized Server Designs and Solutions For Peer-To-Peer Designs for the details.

[Back to Top](#)

## On TLS

Regardless of your overall networking architecture it's likely that TLS (that is, Transport Layer Security or its predecessor, SSL, Secure Sockets Layer) will be part of your solution to the authorization and privacy problems:

- For authorization, it's generally a bad idea to use simple password-based authorization because users are notoriously bad at choosing passwords, making password authorization vulnerable to dictionary attacks. A better solution is to use some sort of pairing scheme, where the password is only used to set up the pairing and subsequent authorization is done by other means (for example, via TLS certificates).
- For privacy, TLS is the only standard encrypted networking API on iOS. To use any other on-the-wire encryption you would have to either implement another protocol yourself or, worse yet, implement some custom on-the-wire encryption. The latter might seem easy, but it has two key disadvantages:

  - On-the-wire encryption is notoriously hard to get right, and such protocols should be designed by security experts.
  - Any custom encryption scheme is going to be harder to explain to the happy folk who manage US export compliance.

If you're not familiar with the capabilities of TLS it would be a good idea to become so. I found the following resources, particularly the last one, to be helpful:

- [Transport Layer Security](http://en.wikipedia.org/wiki/Transport_Layer_Security)
- [X.509](http://en.wikipedia.org/wiki/X.509)
- [PKCS#12](http://en.wikipedia.org/wiki/PKCS12)
- [How Does Secure Socket Layer (SSL or TLS) Work?](http://luxsci.com/blog/how-does-secure-socket-layer-ssl-or-tls-work.html)

The key features of TLS are:

- An X.509 identity consists of an X.509 certificate (which has a public key embedded within it) and a private key (where the private key matches the public key in the certificate).
- A TLS server must apply an identity to its end of the connection. A TLS client may also apply an identity to its end of the connection. After the TLS handshake, the client gets the certificate from the identity of the server and knows that the server holds the private key matching the public key in that certificate. Likewise, if the client applies an identity to its end of the connection, the server can get its associated certificate and know that the client holds the private key matching the public key in that certificate.
- Each peer can then look at the certificate of the remote peer and decide whether to trust that peer. For the client this typically involves checking whether the name in the certificate matches the name of the server it tried to connect to, and then validating the X.509 certificate chain up to a trusted root. However, the actual validation done is a matter of policy on the peer doing the validation. For example, a typical Internet server does no validation of client identities.

The recommended TLS API on both iOS and Mac OS X is CFStream. In addition, you can access HTTPS (that is, HTTP over TLS) via the CFHTTPStream API or the NSURLConnection API. On Mac OS X, you can also use the lower-level [Secure Transport](https://developer.apple.com/mac/library/documentation/Security/Reference/secureTransportRef/Reference/reference.html) API.

__Important:__ CFStream is toll-free bridged to NSStream. So, once you have your streams set up, you can operate on them as if they were NSStreams. For an example of this, see the [Sample Code 'SimpleNetworkStreams'](https://developer.apple.com/samplecode/SimpleNetworkStreams/index.html) sample code.

For more information on these APIs, see the following resources:

- [URL Loading System](https://developer.apple.com/iphone/library/documentation/Cocoa/Conceptual/URLLoadingSystem/URLLoadingSystem.html)
- [Stream Programming Guide for Cocoa](https://developer.apple.com/iphone/library/documentation/Cocoa/Conceptual/Streams/Streams.html)
- [CFNetwork Programming Guide](https://developer.apple.com/iphone/library/documentation/Networking/Conceptual/CFNetwork/Introduction/Introduction.html)
- [Secure Transport Reference](https://developer.apple.com/mac/library/documentation/Security/Reference/secureTransportRef/Reference/reference.html)

[Back to Top](#)

## Networking Designs

There are two fundamentally different designs you can use for your networking code:

- __centralized__ — In this design you have a single server that's on the public Internet, and all clients connect to that server.
- __peer-to-peer__ — In this design your clients talk to each other, without going through a single central server.

Each approach has its pros and cons. The major disadvantage of a centralized server is the server itself; you have to create and run a server on behalf of your users. This can be a daunting task for a small developer (or, indeed, for a large developer with a lot of users; ask the MobileMe team!). Also, it means that you end up storing user data on your server, which has all sorts of wacky legal implications.

Another disadvantage with the centralized approach is latency. For certain latency-sensitive applications, most notably action games, the round trip time to the centralized server will be prohibitively long.

In contrast there are numerous disadvantages with the peer-to-peer approach. The first, and hardest to avoid, is the various link layer issues. iOS devices currently support three link layers for networking (WWAN, Wi-Fi, and Bluetooth), and all of them present challenges for peer-to-peer use. These are discussed in detail in the subsequent sections.

Finally, TLS was really designed with the centralized server model in mind, and using it in a peer-to-peer fashion is tricky. It's not impossible to make it work, but you're definitely swimming against the tide.

### WWAN Link-Layer Issues

It's not possible to do peer-to-peer over the WWAN for a number of reasons:

- If one of the peers is also bound to a Wi-Fi network, iOS will typically shut down the WWAN interface and send all data via the Wi-Fi.
- In general an iPhone will only power up its WWAN interface if it's in use. This makes it impractical to listen for incoming connections on the WWAN interface.
- Devices on different WWAN technologies (for example, EDGE versus 3G) may be on different networks.
- Even if none of the above apply, cellular carriers generally prevent peer-to-peer WWAN communications as a security measure.

### Wi-Fi Link Layer Issues

If two peers are on the same Wi-Fi network, they can generally communicate peer-to-peer. There are, however, issues with this:

- Some Wi-Fi hotspots prevent peer-to-peer communications as a security measure.
- It's not always easy to get the two peers on the same Wi-Fi network. For example, if you're at a hotspot you may have to pay for access, and paying again just so you can sync your iPhone to your Mac is less than ideal.

Another option on the Wi-Fi front is an ad-hoc (IBSS) network. The problems with this include:

- There's no way to create such a network from an iOS device, which makes it impractical for device-to-device communications.
- Most peers can't be on both an infrastructure-based and an ad-hoc network simultaneously, which can make things very inconvenient. To continue the example above, having to take your Mac off the hotspot network just to sync up with your iPhone is less than ideal.

### Bluetooth Link Layer Issues

iOS 3.0 and later support peer-to-peer networking via Bluetooth. While this is a great technology, it still has a number of gotchas:

- It requires iOS 3.0 or later.
- Bluetooth networking is not available on certain hardware (specifically, the first generation iPhone and iPod touch).

An important consequence of the first point is that Bluetooth peer-to-peer networking can only be used to communicate between iOS devices; you can't use it, for example, to communicate between an iOS device and a computer running Mac OS X.

__Important:__ While GameKit is a convenient way to access Bluetooth peer-to-peer networking, you don't have to use GameKit. Applications that browse for services via Bonjour will automatically work over Bluetooth.

[Back to Top](#)

## Solutions For Centralized Server Designs

As mentioned above, by far the hardest part of implementing the centralized server design is running the server itself. The details of this are outside the scope of this document (although see below). Assuming you've got a good handle on that problem, the centralized server design makes it pretty easy to solve your other networking problems, as described in the following subsections.

### Service Discovery

Discovering a centralized server is trivial: just assign your server a fixed DNS name and hard-wire that DNS name into your clients. Problem solved!

### Authorization

As discussed above, there are two aspects to the authorization problem:

- client/server — The client must check that it's talking to the right server.
- server/client — The server must authorize the client.

With a centralized server, the client/server problem has an easy solution: TLS! As part of setting up your server you should create a TLS identity for that server and have its associated certificate signed by one of the certificate authorities trusted by iOS. Then, when the client connects to the server, the TLS mechanism guarantees that it connected to the correct server.

__Note:__ The following AppleCare articles list the trusted root certificates built-in to iOS 2.x and 3.0, respectively:

- [iOS 2.x: List of Available Trusted Root Certificates](http://support.apple.com/kb/HT2185)
- [iOS 3.0: List of Available Trusted Root Certificates](http://support.apple.com/kb/HT3580)

Server/client authorization is trickier, and the solution you use largely depends on the server infrastructure you have available. For example, you might be able to piggyback off the authorization infrastructure supported by your server's host, or you could use TLS client-side identities, or your could use a simple password-based authorization mechanism. There are lots of choices and it's hard to decide on what to use without knowing the specific details of your server.

__Important:__ If you use client-side identities you will not be able to implement your server using CFSocketStream. CFSocketStream does not provide a way for the server to request that the client provide a certificate
(r. [6046415](rdar://problem/6046415))
. This is not a limitation if your server uses some other platform, or some other API (for example, on Mac OS X you can avoid this problem by using Secure Transport or OpenSSL).

### On-The-Wire Privacy

If you use TLS and your centralized server has an identity whose certificate is signed by a trusted root, you get on-the-wire encryption automatically.

### Renting Infrastructure

As mentioned earlier, the hardest part about implementing a centralized server is actually deploying the server. However, you should not let this discourage you. There are a variety of services that can help you with this. For example:

- MobileMe and iDisk — If you just want to upload and download files to some easily-accessible central server, it's very easy to do this using the user's iDisk. Remember that an iDisk is just a WebDAV server, and WebDAV is just HTTP, so uploading or downloading a file is just a simple HTTP transaction.

  One nice feature of this approach is that the user authorizes using their MobileMe credentials, which is very easy to explain.

  The chief disadvantage of this approach is that the user must subscribe to MobileMe.
- Other Services — For something more complex you could use one of many back-end providers to implement your service. Two notable examples are:

  - [Google App Engine](http://code.google.com/appengine/)
  - [Amazon EC2](http://aws.amazon.com/ec2/)

  but there are many, many more.
[Back to Top](#)

## Solutions For Peer-To-Peer Designs

If you've decided to take the peer-to-peer route, you still have to solve the various problems described earlier. The following subsections describe how to do that.

### Service Discovery

In the peer-to-peer case you can implement service discovery using Bonjour. The following resources describe Bonjour in detail:

- [Bonjour Web Site](https://developer.apple.com/networking/bonjour/)
- [Bonjour Overview](https://developer.apple.com/mac/library/documentation/Cocoa/Conceptual/NetServices/Introduction.html)
- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/iphone/library/documentation/Networking/Conceptual/NSNetServiceProgGuide/Introduction.html)
- [Sample Code 'WiTap'](https://developer.apple.com/samplecode/WiTap/index.html)

You can also do service discovery via GameKit, which in turns uses Bonjour.

### Authorization

There's no obvious path to implementing authorization in the peer-to-peer case; the solution space is wide open. A good approach is to design your user interface first and then implement an authorization system based on that. Common user interface designs include:

- authenticate each time — Each time the user connects to the service they must provide their credentials (at least a password, but in many cases a user name as well). You can make this a little more user friendly by storing the password in the keychain on the client.

  The iOS Mail application uses this user interface.

  __Important:__ See the comment above about the security issues associated with passwords.
- authenticate first time — During the first connection the user must enter some credential, and that process generates an authorization token that is used for subsequent connections. This approach is commonly referred to as pairing.

  The iOS Remote application uses this user interface.

  __Important:__ You can use a TLS client-side identity as an authorization token. That is, you can ignore the details of the identity's certificate, and authorize the connection based on a simple certificate comparison. However, be aware of the limitations of CFSocketStream's server support and the difficulties with creating identities from scratch.
- authenticate never — This is an even simpler variant of the above, where the user doesn't even have to authenticate the first time around. Instead the first connection causes the client and server to pair. This allows for a very simple user interface that is fully secure except during the setup phase.

#### Creating Identities

As mentioned earlier, TLS is really designed for use with centralized servers, and is not a good match for peer-to-peer networking. The key problem is that TLS is based on X.509 identities, and these identities are expected to contain the DNS name of the remote peer and to be signed by a trusted root. Neither of these requirements are practical in a peer-to-peer networking design.

It is possible to use TLS in a peer-to-peer network design; you just have to bend the rules a little. The idea is to disable the automatic certificate validation done by TLS and to validate the peer certificate yourself. In this model you don't really need to look inside the certificate; all you need to do is to compare the certificate to a known good certificate that you acquired during pairing.

The main stumbling block is that each peer must have a unique X.509 identity, and creating such an identity is tricky. Currently there are no straightforward APIs for creating an identity on iOS or Mac OS X. However, there are a number of ways to get around this limitation:

- Have some centralized server issue an identity, perhaps using something like [Simple Certificate Enrollment Protocol](http://en.wikipedia.org/wiki/Simple_Certificate_Enrollment_Protocol) (SCEP). These identities may be self-signed or signed by the identity associated with the server.
- Generate a self-signed identity on the peers. While there are no good APIs for doing this, you can create an identity on Mac OS X by sublaunching the `openssl` command line tool.

### On-The-Wire Privacy

Even in a peer-to-peer situation, TLS gives a certain degree of on-the-wire privacy regardless. Specifically, TLS will protect from third party snooping of your traffic. It will not automatically protect you from server spoofing (or, indeed, man-in-the-middle attacks); you would typically gain such protection as the result of your pairing process.

### On GameKit

GameKit addresses some, but not all, of the problems associated with peer-to-peer networking. Most importantly, it provides an easy way to do networking over Bluetooth, which addresses many of the problems associated with peer-to-peer networking over Wi-Fi. It also takes care of service discovery for you. However, it does not address any of the security issues described above and, more to the point, it makes it harder to address these issues because there's no easy way to use TLS to protect your GameKit session.

[Back to Top](#)

## Protocol Issues

Once you've decided on your high-level design, you then have to think about the specific details of the on-the-wire transactions. The first step is to decide on an overall framework for your network transactions. There are two obvious choices:

- HTTP
- a custom TCP-based protocol

Depending on your server architecture this may be a non-issue. For example, if you use the Google App Engine for your server, your transactions must necessarily be framed in HTTP. In the absence of such constraints, you should consider the following points:

- HTTP is probably the most robust way of connecting to a centralized server. There are environments where HTTP will work but a custom TCP connection will not (for example, behind an HTTP proxy).
- HTTP is a natural fit for some transactions but not for others. For example, if you need to do client/server request/response transactions, where the client always sends a request to which the server responds promptly, HTTP is a great fit. On the other hand, if the server needs to be able to inform the client of asynchronous events, HTTP is less than ideal.

  Of course, in that case, you may want to investigate the [push notification](https://developer.apple.com/iphone/library/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html) mechanism introduced with iOS 3.0.
- iOS has many nice HTTP client APIs. Its HTTP server APIs are not as rich; you have to do a lot more work yourself. Thus, for peer-to-peer designs, a custom protocol is more attractive.

[Back to Top](#)

## File Transfer Protocols

A common high-level goal is to transfer files from one machine to another. There are many ways to do this, but two of the most common mechanisms have serious gotchas:

- FTP — Anonymous FTP is an acceptable way to download publicly-visible files. However, you should avoid any other use of FTP like the plague. Specifically, authenticated FTP will send your user's password in plaintext on the wire. This is not acceptable on the modern Internet. Moreover, all forms of FTP send the data in the clear, which is not appropriate for any user data.

  __Note:__ There have been numerous attempts to make a secure 'FTP'.

  These include:

  - [FTPS](http://en.wikipedia.org/wiki/FTPS) — This is FTP over TLS. It is not supported by any built-in APIs on iOS or Mac OS X.
  - [SFTP](http://en.wikipedia.org/wiki/SSH_file_transfer_protocol) — This is a new file transfer protocol based on SSH. There are no SSH APIs built in to either iOS or Mac OS X. On Mac OS X you can access SSH functionality by sublaunching various command line tools. This is not an option on iOS.
- AFP — Given that AFP is the default sharing protocol on Mac OS X, it seems logical to transfer files between a device and a Mac by implementing an AFP client on the device. This is tricky. AFP is quite a complicated protocol, and there's no high-level API for it on iOS. Moreover, AFP is a very Mac-centric protocol, which is a problem if you want to sell your application to users of other platforms.

If you want to support a file sharing protocol the most obvious choices are [WebDAV](http://en.wikipedia.org/wiki/WebDAV) and [SMB](http://en.wikipedia.org/wiki/Server_Message_Block). Still, this is not easy. There are no high-level APIs for these protocols on iOS or Mac OS X, although WebDAV is layered on top of HTTP so the various HTTP APIs make implementing WebDAV easier.

[Back to Top](#)

## Syncing Issues

Another common high-level goal is to sync data structures between two or more machines. Once you've created a reliable and secure network connection between your machines, you can start thinking about what it would take to sync your data between them.

Ultimately your syncing design will be driven by your user experience needs, combined with the amount of programming time you're prepared to invest to achieve that user experience. Some common approaches include:

- manual transfers — A totally manual transfer process does not present a large technical challenge. In fact, this is pretty much equivalent to file transfer.
- full syncing — On the other hand, a fully automatic syncing process, where the application can merge changes made independently on multiple different machines, is quite challenging.
- something in between — For example, if you have a data logging application, syncing is much easier because each datum is read-only and is sourced from one specific machine.

Regardless of your syncing needs, you will have to write all of this code yourself. iOS does not provide any specific high-level support for syncing (for example, there's no equivalent of Sync Services on iOS).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-26 | Updated to reflect the introduction of iTunes file sharing. Some other minor updates. |
| 2010-01-29 | A minor change to clarify the availability of Bluetooth peer-to-peer networking, plus various editorial tweaks. |
| 2009-08-25 | New document that describes various strategies for device-to-device and device-to-computer document transfer. |

