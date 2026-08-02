---
title: TLSTool
apple_id: DTS40014927
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2016-05-23'
source_url: https://developer.apple.com/library/archive/samplecode/sc1236/Listings/README_md.html
archived_at: '2026-07-26T19:54:14.677733Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TLSTool](TLSTool.md)


[Next](TLSTool-TLSToolServer.m.md)[Previous](TLSTool-main.m.md)

# README.md

```
# TLSTool

1.2

TLSTool is a sample that shows how to implement Transport Layer Security (TLS), and its predecessor, Secure Sockets Layer (SSL), using the NSStream API.  TLSTool demonstrates TLS in both client and server mode.

TLSTool can also be used to explore TLS interactively, much like OpenSSL’s `s_client` and `s_server` subcommands.  However, because TLSTool uses the OS’s built-in TLS stack, it will behave more like other apps that use that built-in stack (for example, Mail and Safari).

TLSTool can be useful when debugging App Transport Security (ATS) problems. However, you should also be aware of `nscurl`, a tool built-in to OS X 10.11 and later, which includes ATS-specific diagnostics. Run `nsurl -h` for the details.

## Requirements

### Build

Xcode 7.3

The sample was built using Xcode 7.3 on OS X 10.11.4 with the OS X 10.11 SDK.  You should be able to just open the project and choose *Product* > *Build*.

### Runtime

OS X 10.9

Although TLSTool requires OS X 10.9, many of the core TLS techniques it shows are compatible with OS X back to at least OS X 10.4 (and all versions of iOS for that matter).

The main compatibility gotcha with trying to get TLSTool running on older systems are:

* `kCFStreamPropertySSLContext` — TLSTool uses this stream property to achieve a variety of effects, some of which can be implemented via other means but some of which absolutely require that property.

* `CFReadStreamSetDispatchQueue` and `CFWriteStreamSetDispatchQueue` — TLSTool uses a serial dispatch queue for its core synchronisation; supporting older system would require a rewrite to use run loops.

## Packing List

The sample contains the following items:

* README.md — This file.

* TLSTool.xcodeproj — An Xcode project for the program.

* TLSTool — A directory containing:

    - main.m — The command line tool main.

    - TLSToolClient.{h,m} — Core of the client implementation.

    - TLSToolServer.{h,m} — Core of the server implementation.

    - TLSToolCommon.{h,m} — Code shared between the client and server.

    - TLSUtilities.{h,m} — Utilities routines used by various subsystems.

    - QNetworkAdditions.{h,m} — A compatibility shim for certain networking APIs.

    * QHex.{h,m} — Hex dump utilities.

## Using the Sample

### Testing the Client

It’s easy to use TLSTool to run a simple TLS client test.  For example, to fetch the URL `https://apple.com/`:

1. In Terminal, change into the directory containing the tool.

2. Run the tool as shown below:

        $ ./TLSTool s_client -connect apple.com:443
        *  input stream did open
        * output stream did open
        * output stream has space
        * protocol: TLS 1.2
        * cipher: ECDHE_RSA_WITH_3DES_EDE_CBC_SHA
        * trust result: unspecified
        * certificate info:
        *   0 + rsaEncryption 2048 sha256-with-rsa-signature 'apple.com'
        *   1 + rsaEncryption 2048 sha256-with-rsa-signature 'Apple IST CA 2 - G1'
        *   2 + rsaEncryption 2048 sha1-with-rsa-signature 'GeoTrust Global CA'

    **Note** The lines prefixed by `*` represent debugging information from the tool.  The above shows the chain of trust leading from `apple.com` to the trust CA root certificate `Entrust.net Secure Server Certification Authority`.

3. Enter the text below, hitting return after each line and return twice at the end.

        GET / HTTP/1.1
        Host: apple.com
        Connection: close

    The tool will print the server’s response (see below) and then quit once the server closes the connection.

        * output stream has space
        *  input stream has bytes
        HTTP/1.1 301 MOVED PERMANENTLY
        Server:
        Date:
        Referer:
        Location: https://www.apple.com/
        Content-type: text/html
        Connection: close

        *  input stream has bytes
        *  input stream has bytes
        *  input stream end
        * close
        * bytes sent 50, bytes received 144

### Testing the Server

**IMPORTANT** To test the server code you will need a TLS server digital identity in your keychain.  If you don’t have one handy, you can create one using the instructions in Technote 2326 [Creating Certificates for TLS Testing][tn2326].

[tn2326]: <https://developer.apple.com/library/mac/technotes/tn2326/_index.html>

In the following example the TLS server digital identity is called *guy-smiley.local* and it’s issued by the *QSecure CA* certificate authority.

To test the server code:

1. In Terminal, open a client window and a server window and change into the sample code directory in each.

2. In the server window, run the tool as shown below:

        server$ ./TLSTool s_server -cert guy-smiley.local
        * server identity: guy-smiley.local
        * server did start

    **Note** If you don’t supply a port number (via the `-accept` command line argument) the server listens on port 4433.

3. In the client window, run the tool as shown below:

        client$ ./TLSTool s_client -noverify
        *  input stream did open
        * output stream did open
        * output stream has space
        * protocol: TLS 1.2
        * cipher: RSA_WITH_AES_256_CBC_SHA256
        * trust result: recoverable trust failure
        * certificate info:
        *   0 + rsaEncryption 2048 sha1-with-rsa-signature 'guy-smiley.local.'
        *   1   rsaEncryption 2048 sha1-with-rsa-signature 'QSecure CA'

    **Note** If you don’t supply a connection address (via the `-connect` command line argument) the client connects to localhost:4433.

    **Note** The `-noverify` option disables TLS server trust evaluation, allowing the connection to succeed even though the server’s certificate is not trusted by the system.  If I configured the system to trust the *QSecure CA* root certificate it would not be necessary.

    In the server window you’ll see:

        *  input stream did open
        * output stream did open
        * output stream has space
        * protocol: TLS 1.2
        * cipher: RSA_WITH_AES_256_CBC_SHA256
        * no trust

4. Once things are connected like this you can type text in the server window and it’ll show up in the client window and vice versa.

5. Enter control-D in either window to close the connection.

### Testing Other Features

The tool has lots of other options.  Run the command below to see the usage:

    $ ./TLSTool -?
    ...

## How it Works

The project contains lots of networking code that’s the same as any other NSStream-based networking app.  You can see the code in TLSToolCommon but you’d probably be better off looking at other, simpler samples, including:

* [SimpleNetworkStreams][SimpleNetworkStreams]

* [WiTap][WiTap]

* [PictureSharing][PictureSharing]

* [RemoteCurrency][RemoteCurrency]

If you’re interested in TLS you should focus on the TLSToolClient and TLSToolServer classes, each of which is quite small.  Specifically:

* `-[TLSToolClient run]` shows how to set up a stream pair for TLS client operation

* `-[TLSToolServer startConnectionWithInputStream:outputStream:responseData:]` shows how to set up a stream pair for TLS server operation

[SimpleNetworkStreams]: <https://developer.apple.com/library/ios/#samplecode/SimpleNetworkStreams/>

[WiTap]: <https://developer.apple.com/library/ios/#samplecode/WiTap/>

[PictureSharing]: <https://developer.apple.com/library/mac/#samplecode/PictureSharing/>

[RemoteCurrency]: <https://developer.apple.com/library/mac/#samplecode/RemoteCurrency/>

## Caveats

The tool’s command line arguments are somewhat compatible with OpenSSL’s `s_client` and `s_server` subcommands.  This compatibility layer is wafer thin; there are lots of options that just aren’t implemented, and some options that don’t work the same way as OpenSSL.  For example, the OpenSSL `s_client` subcommand disables TLS server trust evaluation by default but TLSTool leaves it enabled because disabling it is, in general, a bad idea.

The goal of TLSTool is not to provide 100% compatibility with OpenSSL’s commands, but rather to a) be a reasonable code sample, and b) provide basic compatibility to preserve ‘muscle memory’.  Improving the latter would undermine the former.

## Feedback

If you find any problems with this sample, or you’d like to suggest improvements, please [file a bug][bug] against it.

[bug]: <http://developer.apple.com/bugreporter/>

## Version History

1.0 (Aug 2014) was the first shipping version.

1.2d1 (Jan 2015) was distributed to a small number of developers on a one-to-one basis.  Note the incorrect version number, which should have been 1.1d1.

1.1 (Sep 2015) included a number of enhancements:

* Added support for the server to pass Distinguished Names to the client (via `-cacert`) and for the client to display those names (`-show_DNs`).

* The client now accepts one or more root certificates on the command line (`-cacert`), and will require the server certificate to be issued by one of those roots.

* The program now logs the negotiated TLS version and cypher suite, along with more information about the remote peer’s certificate chain.

* Added support for setting the minimum (`-min`) and maximum (`-max`) allowed TLS version.

* Added the `-autorespond` option to the server, which is helpful when testing HTTPS clients.

* Fixed the `-crlf` option.

* Simplified the server’s client trust evaluation options.

1.2 (Apr 2016) marks the certificates included in the server handshake with a “+”, which makes it easier to debug problems misconfigured servers (ones that don’t supply all the required intermediates).

Share and Enjoy

Apple Developer Technical Support<br>
Core OS/Hardware

14 Apr 2016

Copyright (C) 2014-2016 Apple Inc. All rights reserved.
```

[Next](TLSTool-TLSToolServer.m.md)[Previous](TLSTool-main.m.md)

