---
title: HTTPS Server Trust Evaluation
apple_id: DTS40012884
resource_type: Technical Note
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2014-07-29'
source_url: https://developer.apple.com/library/archive/technotes/tn2232/_index.html
archived_at: '2026-07-26T19:54:10.432721Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2232

# HTTPS Server Trust Evaluation

HTTPS is a cornerstone of Internet security. When making a connection over HTTPS, the client must evaluate whether to trust the server. If this trust evaluation fails, the client refuses to connect. This can happen for a variety of reasons, some benign—the server might be using a self-signed certificate, an intermediate certificate is missing, and so on—and some malicious—the server is an impostor, looking to steal the user's data. This document describes the reasons why server trust evaluation can fail, and how this problem can be resolved while not compromising the user's security.

While the focus of this document is on HTTPS, it also covers TLS, which is the underlying security protocol used by HTTPS, and TLS's older cousin, SSL.

You should read this document if you're creating an iOS or Mac OS X program that uses HTTPS, TLS or SSL to talk to a server securely, and you need to resolve a server trust evaluation failure or enforce a stricter form of server trust evaluation.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2jjzkfet2ekvbviskpjy)[TLS Security Guarantees](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ujrjvgrkdkvjesvczi5kucusbjzkekrkt)[Resolving Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2sivju6tcwjfheo)[Understanding Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2vjzcekustkrau4ra)[Trust Evaluation Fundamentals](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ukjkvgvcfkzauyvkbkreu6tsgkvheiqknivhfiqkmkm)[Common Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dj5gu2t2oizaustcvkjcvg)[Debugging Tools](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2eivbfkr2hjfheovcpj5gfg)[Basic Trust Customization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2cifjusq2ukjkvgvcdkvjvit2njfnecvcjj5ha)[Trust Customization for Specific APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2njfnekqkqjfjq)[WebView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2xivbfmskfk4)[UIWebView](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2vjflukqswjfcvo)[HTTP Live Streaming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ikrkfatcjkzcvgvcsivau2skoi4)[NSURLSession](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2oknkvetctivjvgskpjy)[NSURLConnection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2oknkvetcdj5he4rkdkreu6tq)[CFHTTPStream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvbumscukrifgvcsivau2)[CFSocketStream](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dizju6q2livkfgvcsivau2)[Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tivbvkusfkrjectstkbhveva)[Resolving Specific Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2sivju6tcwjfheorsbjfgfkusfkm)[Server Name Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tivjfmrksjzau2ri)[Missing Intermediate Certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2njfjvgskoi5eu4vcfkjgukrcjifkekuy)[Trusting One Specific Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2nincveva)[Custom Certificate Authority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2nkjhu6va)[Self-Signed Certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tivgemu2ji5hekrcdivjfiuy)[Trust Exceptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ukjkvgvcflbbukucujfhu4uy)[Enforcing Stricter Server Trust Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tkrjesq2uivja)[Hints and Tips](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ijfhfiu2bjzcfiskqkm)[SecTrustEvaluate Can Block](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tivbviusvknkekvsbjrkucvcfinau4qsmj5buw)[Investigating Hard-To-Debug Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2jjzleku2ujfducvcjjzdviusvknkekvsbjrkucvcjj5hemqkjjrkverkt)[Displaying Certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ejfjvatcblfeu4r2divjfiskgjfbucvcfkm)[Displaying Trust Results](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ejfjvatcblfeu4r2ukjkvgvcsivjvktcukm)[Appendix A: Common Server Trust Evaluation Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ukjkvgvcfkjje6ust)[Appendix B: Glossary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Your first encounter with [HTTPS server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) is likely to be an error like the following:

```
Domain=NSURLErrorDomain Code=-1202 "The certificate for this server is invalid. You might be connecting to a server that is pretending to be “example.com” which could put your confidential information at risk." UserInfo=0x14a730 {NSErrorFailingURLStringKey=https://example.com/, NSLocalizedRecoverySuggestion=Would you like to connect to the server anyway?, NSErrorFailingURLKey=https://example.com/, NSLocalizedDescription=The certificate for this server is invalid. You might be connecting to a server that is pretending to be “example.com” which could put your confidential information at risk., NSUnderlyingError=0x14a6c0 "The certificate for this server is invalid. You might be connecting to a server that is pretending to be “example.com” which could put your confidential information at risk.", NSURLErrorFailingURLPeerTrustErrorKey=<SecTrustRef: 0x14ec00>}
```

In this case error -1202 in the `NSURLErrorDomain` domain is `NSURLErrorServerCertificateUntrusted`, which means that [server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) has failed. You might also receive a variety of other errors; [Appendix A: Common Server Trust Evaluation Errors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ukjkvgvcfkjje6ust) lists the most common ones.

If you receive one of these errors and search the 'net for help, you might find advice like this:

```
To get around this problem simply disable the certificate checks.
```

Or, worse yet, like this:

```
To get around this problem disable the certificate checks by calling +[NSURLRequest setAllowsAnyHTTPSCertificate:forHost:].
```

Blindly following this advice is a serious mistake. HTTPS (actually, the underlying TLS protocol) offers two important security guarantees, and if you disable server trust evaluation you totally invalidate one of these guarantees.

__Warning:__ Disabling server trust evaluation puts the user's security at risk. Do not do it in any code you intend to ship to end users. If server trust evaluation is failing, you must understand why it's failing and decide on the best way to resolve that failure.

__Warning:__ `+[NSURLRequest setAllowsAnyHTTPSCertificate:forHost:]` is not a public API and is thus not supported by Apple; moreover, use of non-public APIs is not allowed in App Store apps.

In most cases the best way to resolve a server trust evalution failure is to fix the server. This has two benefits: it offers the best security and it reduces the amount of code you have to write. The remainder of this technote describes how you can diagnose server trust evaluation failures and, if it's not possible to fix the server, how you can customize server trust evaluation to allow your connection to proceed without completely undermining the user's security.

__Important:__ To securely resolve a server trust evaluation failure you will have to understand a lot of security jargon. There is a [glossary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) at the end of this document, and the first time a jargon term is used, it contains a link to its glossary entry.

### TLS Security Guarantees

[HTTPS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) is defined by [RFC 2818](http://www.ietf.org/rfc/rfc2818.txt) but, for the most part, it consists of a simple composition of two existing protocols:

- [HTTP](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) (as defined by [RFC 2616 Hypertext Transfer Protocol -- HTTP/1.1](http://www.ietf.org/rfc/rfc2616.txt) and others)
- [TLS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) (as defined by [RFC 5246 The Transport Layer Security (TLS) Protocol Version 1.2](http://www.ietf.org/rfc/rfc5246.txt) and others), or the older [SSL](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) protocol

HTTPS inherits its security guarantees from TLS. By default these are:

- on-the-wire privacy — This guarantees that the data is secure from a passive attacker (someone who can see but can't modify the packets exchanged between the client and server).
- client-authenticates-server authentication — This protects the client from an active attacker (someone who can both see and modify the packets exchanged between the client and the server). Most importantly, it protects the client from various forms of man-in-the-middle attack, including impostor servers (servers who pretend to be the real server and thus acquire confidential information from the client).

[TLS server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) is the part of TLS that implements client-authenticates-server authentication. If you disable it, you lose this second, extremely important security guarantee.

__Note:__ [Understanding Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2vjzcekustkrau4ra) explains how TLS protects the client from impostor servers.

__Note:__ TLS also supports server-authenticates-client authentication. This authentication is optional at both ends: the server must specifically request a certificate from the client, the client may choose to apply a client [identity](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) (and thus supply its client certificate to the server, if the server requested it), and the server may choose to allow or deny connections based on whether the client applied a client identity and, if it did, the particulars of the identity's certificate. This is an important technique but it is outside the scope of this document and thus not discussed further here.

### Resolving Server Trust Evaluation Failures

If disabling server trust evaluation completely is a mistake, what should you do? Your first step should be to diagnose the problem. To do this, read [Understanding Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2vjzcekustkrau4ra). Once you understand the problem you'll likely find that the easiest solution is to fix the server. This reduces the amount of code you have to write and guarantees the user's security.

If it's not possible to fix the server, you will need to customize the server trust evaluation to allow the connection to proceed without completely undermining the user's security. [Basic Trust Customization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2cifjusq2ukjkvgvcdkvjvit2njfnecvcjj5ha) explains the general process for customizing server trust evaluation; it's followed by [Trust Customization for Specific APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2njfnekqkqjfjq) which explains the process for various commonly-used APIs. Finally, [Resolving Specific Server Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2sivju6tcwjfheorsbjfgfkusfkm) is a discussion of how to work around specific server trust evaluation problems.

You can also customize server trust evaluation for the opposite reason, that is, to make the connection more secure. See [Enforcing Stricter Server Trust Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tkrjesq2uivja) for a discussion of this.

[Back to Top](#)

## Understanding Server Trust Evaluation Failures

When you connect to a server using TLS, it gives you the certificate of the server and guarantees that the server holds the [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) that matches the [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) embedded in that certificate. This is the first step in establishing a secure connection. The second step, which is just as critical, is for you to examine the certificate you got from the server to decide whether it matches the server you are expecting to talk to. This process is known as [server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq), and this section describes the basic techniques involved.

__Note:__ A full discussion of the [X.509 public key infrastructure](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) is (way) outside of the scope of this document. Instead, this document describes only the basics needed to understand how the system works in practice. If you're looking for more information about [X.509 certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) as they are used on the Internet, see [RFC 5280](http://www.ietf.org/rfc/rfc5280.txt).

### Trust Evaluation Fundamentals

TLS server trust evaluation consists of two basic steps:

1. basic [X.509 certificate trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)
2. TLS-specific additions

To understand the first step, you need to know a little bit about X.509 certificates. An X.509 certificate has five critical attributes:

- information about the [subject](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)
- information about the [issuer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)
- information about the certificate itself (for example, the [valid date range](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq), which is the range of dates for which the certificate is valid)
- a [public key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)
- a [digital signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq)

If the digital signature is valid then the certificate is a guarantee from the issuer that the subject holds the [private key](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) associated with the public key in the certificate. For example, the certificate for DevForums ([https://devforums.apple.com/](https://devforums.apple.com/)) is (at the time of writing) issued by [Entrust](http://www.entrust.net/), and by signing that certificate Entrust is guaranteeing that the maintainers of the DevForums server hold the private key associated with the public key in the certificate.

X.509 certificate trust evaluation is a recursive two-step process:

1. check the validity of the certificate itself — This involves various things, but the two most important are a) verifying the digital signature, and b) checking that the [verify date](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) (typically the current date) is within the certificate's valid date range.
2. check the validity of the issuer — This involves finding the issuer's certificate and (recursively) checking its validity.

Clearly this recursive process must terminate eventually. Trust evaluation can succeed in only one case: if it hits a [trusted anchor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq). A trusted anchor is a certificate that the system trusts implicitly, typically because it's the [root certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) of a well-known [certificate authority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) that has been baked in to the system.

On the other hand, trust evaluation can fail for a variety of reasons:

- if it hits an invalid certificate
- if it can't find the certificate for an issuer
- if it hits a [self-signed certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) that is not a trusted anchor

If X.509 trust evaluation is successful, the system then applies additional TLS-specific checks. In practice this involves checking that the DNS name that you are attempting to connect to matches the DNS name in the certificate. There are, however, a few wrinkles:

- Typically you would expect to find this DNS name in the subject's Common Name field, but it can also be in a Subject Alternative Name extension. If a name is present in the Subject Alternative Name extension, it takes priority over the Common Name.
- The Subject Alternative Name extension may also contain IP addresses, which the client consults if it connected via an IP address rather than a DNS name.
- The DNS name in the certificate might be a wildcard name, for example, "\*.apple.com".
- The Extended Key Usage extension is expected to include the Server Authentication value.

If you're interested in the details of these TLS-specific checks, see [RFC 2818](http://www.ietf.org/rfc/rfcXXX.txt).

### Common Failures

With the above in mind, it's easy to understand the various server trust evaluation failures that you're likely to see. These include:

- missing issuer certificate — For any given certificate (except the trusted anchor), the system must be able to locate the certificate of the issuer.
- date problems — For any given certificate, the verify date must be within the certificate's valid date range.
- self-signed certificate — For any given certificate, if the certificate is self-signed, it will cause evaluation to fail (unless it's a trusted anchor).
- no trusted anchor — The system must be able to follow the path of issuer certificates leading to a trusted anchor.
- DNS name mismatch — The DNS name that you're trying to connect to must match the name in the [server certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq), as described in the previous section.

__Important:__ The first three criteria apply to all certificates in the path of certificates leading from the server certificate to the trusted anchor. For example, if server trust evaluation fails due to a date problem, you must check the valid date range of the server certificate, any [intermediate certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) leading to the trusted anchor, and the trusted anchor itself.

If, after investigating each of the points above, you still can't work out why server trust evaluation is failing, you might want to try the technique described in [Investigating Hard-To-Debug Trust Evaluation Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2jjzleku2ujfducvcjjzdviusvknkekvsbjrkucvcjj5hemqkjjrkverkt).

### Debugging Tools

There are a variety of tools you can use to debug server trust evaluation problems, and this section discusses some of the more common ones.

#### Keychain Access

Keychain Access (in the Utilities folder) has a number of useful certificate debugging features:

- It can import and export certificates and identities in a variety of formats.
- If you double click on a certificate it will display a nice GUI certificate viewer.
- The Certificate Assistant, which you access via Keychain Access, can evaluate trust on a specific certificate.
- The Certificate Assistant can create self-signed certificates.
- The Certificate Assistant can create a certificate authority which you can use to issue leaf and intermediate certificates for testing. You can learn more about this feature of Certificate Assistant below.

When playing around with Keychain Access it's a good idea to create a scratch keychain which you can use for testing credentials. This ensures that your testing credentials don't get mixed up with the important credentials you use day-to-day.

#### Security Tool

The `security` tool on OS X gives you access to a wide range of security functionality, not all of which is exposed via Keychain Access. For example, you can use it to:

- dump the keychain in a text format
- work with trust settings in detail
- add certificates to and remove them from the keychain

For more information about the `security` tool, read its [man page](x-man-page://1/security).

#### Safari on the Mac

If you visit a trusted HTTPS web site with Safari you can click the lock icon in the title bar to view the sequence of certificates leading from the server's certificate to a trusted root.

If you visit an untrusted HTTPS web site with Safari, it will display its "can't verify the identity of the website" sheet. The Show Certificate button will extend the sheet so that you can see the certificates being considered.

Both of these certificate viewers let you drag a certificate out to the desktop (start your drag on the large certificate icon), which is useful if you need to check the certificate with other tools (for example, Certificate Assistant's trust evaluation feature).

#### Interactive Testing

In some cases it's useful to connect to a server and issue it commands for testing purposes. For typical Internet protocols (HTTP, SMTP, NNTP, and so on) you can do this with the [telnet](x-man-page://1/telnet) tool. This does not work, however, if the protocol uses TLS. In that case your best option is the [s_client](x-man-page://1/s_client) subcommand of the [openssl](x-man-page://1/openssl) tool. Listing 1 shows how you can use this tool to manually get the contents of `<https://www.apple.com>` (remember that HTTPS uses port 443).

__Listing 1__  Using openssl s_client

```shell
$ openssl s_client -connect www.apple.com:443
CONNECTED(00000003)
[...]
GET / HTTP/1.1
Host: www.apple.com

HTTP/1.1 200 OK
Server: Apache/2.2.3 (Oracle)
Content-Length: 9464
Content-Type: text/html; charset=UTF-8
ntCoent-Length: 9516
Cache-Control: max-age=47
Expires: Mon, 25 Jun 2012 16:18:24 GMT
Date: Mon, 25 Jun 2012 16:17:37 GMT
Connection: keep-alive

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
[...]
</html>
closed
$
```

The `s_client` subcommand supports a number of useful debugging options. For example:

- You can supply the `-cert` argument to have it respond to client certificate requests.
- You can specify the `-showcerts` option to get the complete list of certificates provided by the server.
- The `-debug` and `-msg` options enable low-level debugging features.

See the [man page](x-man-page://1/s_client) for more information about these options and more.

__Important:__ The [openssl](x-man-page://1/openssl) tool uses the OpenSSL TLS implementation, which is not the standard TLS implementation used by the rest of the system (that is, [Secure Transport](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tivbvkusfkrjectstkbhveva)). This is both an advantage and a disadvantage:

- If you're investigating weird TLS behavior it's sometimes useful to get a 'second opinion' by testing with the OpenSSL TLS stack.
- On the other hand some problems are specific to Secure Transport, so that a successful test with the `s_client` subcommand doesn't guarantee that your app's code will work.

Finally, the `s_client` subcommand with the `-showcerts` option is a good way to get a copy of the server's certificate chain. Listing 2 is an example of this.

__Listing 2__  Getting the full list of certificates

```shell
$ openssl s_client -showcerts -host www.apple.com -port 443
[...]
---
Certificate chain
 0 s:/C=US/L=Cupertino/O=Apple Inc./ST=CALIFORNIA/CN=www.apple.com
   i:/C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
-----BEGIN CERTIFICATE-----
MIIDJzCCApCgAwIBAgIOAQAAAAABNwl6mQWT01EwDQYJKoZIhvcNAQEFBQAwUTEL
MAkGA1UEBhMCVVMxIDAeBgNVBAoTF0FrYW1haSBUZWNobm9sb2dpZXMgSW5jMSAw
HgYDVQQDExdBa2FtYWkgU3Vib3JkaW5hdGUgQ0EgMzAeFw0xMjA1MDExNzUzNDNa
Fw0xMzA1MDExNzUzNDNaMGMxCzAJBgNVBAYTAlVTMRIwEAYDVQQHEwlDdXBlcnRp
bm8xEzARBgNVBAoTCkFwcGxlIEluYy4xEzARBgNVBAgTCkNBTElGT1JOSUExFjAU
BgNVBAMTDXd3dy5hcHBsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK
AoIBAQCdJlExG8umAtxL9Df/10diaYoqFeeVDbU13cH0KNxq2vV0nSb3dROtUAig
/wXj6jFU16fhfFegjcYBkYL9qiUkIiROMNo9r1IzZX4Yv9HT30vBdRMZkuIdy9eP
m9nctNVYyBGRJapem1c+llxAJzToiuQofBY6L6K2dO7nuGm7AZ/PwcbyxZEWoh0E
2SKMbMD9vG0Dph+rZDcPxENFa401j95ZiyyDinHXPliPVGimQmLeaWXMOhJSGXcd
FidodxJCGPUIMuQnxipIH8EAiOg76aKsFvi/7ctoYtRGsXJZqRLnKJ2JVAq+tQxj
6so8vaO5I5wqjyCa+ECJJ0i8Vhp/AgMBAAGjbDBqMDkGA1UdHwQyMDAwLqAsoCqG
KGh0dHA6Ly9jcmwuZ2xvYmFsc2lnbi5uZXQvQWthbWFpU3ViMy5jcmwwHQYDVR0O
BBYEFK5QfqCwo5h4aWa7DmhIJdMZ50FjMA4GA1UdDwEB/wQEAwIFIDANBgkqhkiG
9w0BAQUFAAOBgQCMfDikw5AwrCCCkhcb+ak5oTRmhV88mL5Pk7SzVTbMdCoaktOD
+Bu7iX0OYsISOjYu0x2CzX2VQ5kP5NhA7fqXOiq4iG1G/Ae+xW01lUB1gJ7VUwoX
9LabdT6c812EOMpza4lrnLqnOsiSCDf1SWv0Lo+pMkZ9Ka9EbSd3DqUEHw==
-----END CERTIFICATE-----
 1 s:/C=US/O=Akamai Technologies Inc/CN=Akamai Subordinate CA 3
   i:/C=US/O=GTE Corporation/OU=GTE CyberTrust Solutions, Inc./CN=GTE CyberTrust Global Root
-----BEGIN CERTIFICATE-----
MIIDxzCCAzCgAwIBAgIEBAAEAzANBgkqhkiG9w0BAQUFADB1MQswCQYDVQQGEwJV
[...]
bZ14M6VWhKYouKEZnaAsSCe+XHsF0haUfOnxpj4p7CZj/DnGZVB8Uh92ORa0lyY5
q44d/bV6wDodO38=
-----END CERTIFICATE-----
---
[...]
```

You can examine one of these certificates by:

1. copying the text (the `-----BEGIN CERTIFICATE-----` line through to the `-----END CERTIFICATE-----` line) into a text file with the .pem extension
2. dragging that file into Keychain Access
3. double clicking the newly imported certificate

This will open the standard certificate viewer which you can use to examine the certificate in detail.

#### Dumping ASN.1

Many security technologies, including certificates, use the [ASN.1](http://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One) binary data format. This format is not even remotely human readable, but there are tools that can help. Most notably the [dumpasn1](http://www.cs.auckland.ac.nz/~pgut001/dumpasn1.c) command line tool can convert a file containing ASN.1 binary data to the ASN.1 text format, making it much easier to understand.

[Back to Top](#)

## Basic Trust Customization

iOS and OS X support trust evaluation by way of trust objects (of type `SecTrustRef`). It's possible to create trust objects from scratch but, in the case of TLS server trust evaluation, it's typically the case that the API you're using already does some default server trust evaluation and you want to customize that. Thus the standard approach is:

1. get the trust object
2. evaluate it yourself, just to be sure that it's the cause of the failure
3. if the trust evaluation succeeds, you may choose to enforce stricter trust evaluation rules, as discussed in [Enforcing Stricter Server Trust Evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2tkrjesq2uivja)
4. if the trust evaluation fails, apply your customizations to the trust object
5. evaluate the trust again, and either allow or deny the connection based on this evaluation

The mechanism used to get the trust object is API specific. [Trust Customization for Specific APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2njfnekqkqjfjq) discusses the common cases. However, once you've got the trust object, the process of evaluating and customizing it is the same for all APIs.

Listing 3 shows the basic technique for evaluating a trust object.

__Listing 3__  Evaluating a trust object

```
OSStatus            err;
BOOL                allowConnection;
SecTrustResultType  trustResult;

allowConnection = NO;

err = SecTrustEvaluate(trust, &trustResult);
if (err == noErr) {
    allowConnection = (trustResult == kSecTrustResultProceed) ||
                      (trustResult == kSecTrustResultUnspecified);
}
```

__Important:__ This code allows the connection if the trust result is either `kSecTrustResultProceed` or `kSecTrustResultUnspecified`. In most cases the result is actually the latter, indicating that the user hasn't specified a trust preference, so your app should do the default thing (that is, connect). The distinction between these two values is irrelevant on iOS, but on OS X the user can use Keychain Access to create trust settings, whereupon you might also see a trust result of `kSecTrustResultProceed`.

You can then customize the server trust evaluation as you see fit. For example, if you're talking to a server whose certificate was issued by a certificate authority that's not trusted by the system, you can call `SecTrustSetAnchorCertificates` to set the anchors for the trust object to be that certificate authority's root certificate. Listing 4 shows an example of this.

__Listing 4__  Using a custom anchor

```
OSStatus            err;
BOOL                allowConnection;
SecCertificateRef   customAnchor;
SecTrustResultType  trustResult;

allowConnection = NO;

customAnchor = ... the CA's root certificate ...;

err = SecTrustSetAnchorCertificates(
    trust,
    (__bridge CFArrayRef) [NSArray arrayWithObject:(__bridge id) customAnchor]
);
if (err == noErr) {
    err = SecTrustEvaluate(trust, &trustResult);
}
if (err == noErr) {
    allowConnection = (trustResult == kSecTrustResultProceed) ||
                      (trustResult == kSecTrustResultUnspecified);
}
code
```

__Note:__ This technique is discussed in more detail in [Custom Certificate Authority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2nkjhu6va).

Finally, there may be situations where the required customization cannot be done directly on the trust object. For example, if you want a trust object to consider an additional intermediate certificate, you can't add that certificate directly to the object
(r. [16058372](rdar://problem/16058372))
. You can, however, re-create the trust object with the parameters you want and then evaluate that new trust object. Listing 5 shows an example of this.

__Listing 5__  Re-creating the trust object

```
OSStatus            err;
BOOL                allowConnection;
CFArrayRef          policies;
NSMutableArray *    certificates;
CFIndex             certCount;
CFIndex             certIndex;
SecCertificateRef   extraIntermediate;
SecTrustRef         newTrust;
SecTrustResultType  newTrustResult;

allowConnection = NO;

policies = NULL;
newTrust = NULL;

err = SecTrustCopyPolicies(trust, &policies);
if (err == errSecSuccess) {
    certificates = [NSMutableArray array];

    certCount = SecTrustGetCertificateCount(trust);
    for (certIndex = 0; certIndex < certCount; certIndex++) {
        SecCertificateRef   thisCertificate;

        thisCertificate = SecTrustGetCertificateAtIndex(trust, certIndex);
        [certificates addObject:(__bridge id)thisCertificate];
    }

    extraIntermediate = ... the extra intermediate certificate to use ...;
    [certificates addObject:(__bridge id)extraIntermediate];

    err = SecTrustCreateWithCertificates(
        (__bridge CFArrayRef) certificates,
        policies,
        &newTrust
    );
    if (err == noErr) {
        err = SecTrustEvaluate(newTrust, &newTrustResult);
    }
    if (err == noErr) {
        allowConnection = (newTrustResult == kSecTrustResultProceed) ||
                          (newTrustResult == kSecTrustResultUnspecified);
    }
}

if (newTrust != NULL) {
    CFRelease(newTrust);
}
if (policies != NULL) {
    CFRelease(policies);
}
```

[Back to Top](#)

## Trust Customization for Specific APIs

Once you understand the basics of using a trust object, you have to know how to get such an object from the API you're using. The following sections cover a variety of APIs, from the very high-level (WebView and UIWebView) to the lowest level (Secure Transport).

### WebView

OS X's WebView gives you access to NSURLConnection __authentication challenges__ via its `resourceLoadDelegate` property. You can respond to authentication challenges in the same way that you would with [NSURLConnection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2oknkvetcdj5he4rkdkreu6tq). Alas, it's not possible to access `NSURLAuthenticationMethodServerTrust` authentication challenges via this mechanism
(r. [9475067](rdar://problem/9475067))
. You can work around this limitation using an NSURLProtocol subclass, as illustrated by [Sample Code 'CustomHTTPProtocol'](https://developer.apple.com/samplecode/CustomHTTPProtocol/index.html).

__Note:__ This sample is for iOS but the core core works equally well on OS X.

### UIWebView

UIWebView does not provide any way for an app to customize its HTTPS server trust evaluations
(r. [10131336](rdar://problem/10131336))
. You can work around this limitation using an NSURLProtocol subclass, as illustrated by [Sample Code 'CustomHTTPProtocol'](https://developer.apple.com/samplecode/CustomHTTPProtocol/index.html).

### HTTP Live Streaming

HTTP Live Streaming's support for server trust evaluation depends on the type of resource being fetched, as shown in Table 1.

__Table 1__  Customizing HTTPS Server Trust Evaluation in HTTP Live Streaming

| Resource Type | Extension | Can Customize Server Trust Evaluation? |
| media segment | .ts | no |
| index (playlist) | .m3u8 | yes |
| key | n/a | yes |

For general information about HTTP Live Streaming, see [HTTP Live Streaming Overview](https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Conceptual/StreamingMediaGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008332). For specific information on how to get HTTP Live Streaming to call your code to fetch keys—at which point you can use whatever technique you want to access them, including NSURLSession with a customized HTTPS server trust evaluation—watch WWDC 2011 Session 408 [HTTP Live Streaming Update](https://developer.apple.com/videos/wwdc/2011/).

Also, AV Foundation allows you to implement your own resource loading, at which point you can use any network API to load these resources (and thus customize HTTPS server trust evaluation using that API). Specifically, you can set a resource loader (AVAssetResourceLoader) on an asset (AVAsset) and then use its delegate to override the loading of non-media segment resources (see Table 1). Support for this technique was introduced in iOS 6.0 and OS X 10.9.

### NSURLSession

NSURLSession allows you to customize HTTPS server trust evaluation by implementing the `-URLSession:didReceiveChallenge:completionHandler:` delegate method. To customize HTTPS server trust evaluation, look for a challenge whose __protection space__ has an authentication method of `NSURLAuthenticationMethodServerTrust`. For those challenges, resolve them as described below. For other challenges, the ones that you don't care about, call the completion handler block with the `NSURLSessionAuthChallengePerformDefaultHandling` disposition and a NULL credential.

When dealing with the `NSURLAuthenticationMethodServerTrust` authentication challenge, you can get the trust object from the challenge's protection space by calling the `-serverTrust` method. After using the trust object to do your own custom HTTPS server trust evaluation, you must resolve the challenge in one of two ways:

- If you want to deny the connection, call the completion handler block with the `NSURLSessionAuthChallengeCancelAuthenticationChallenge` disposition and a NULL credential.
- If you want to allow the connection, create a credential from your trust object (using `+[NSURLCredential credentialForTrust:]`) and call the completion handler block with that credential and the `NSURLSessionAuthChallengeUseCredential` disposition.

__Important:__ The system ignores the trust result of the trust object you use to create the credential; any valid trust object will allow the connection to succeed.

### NSURLConnection

NSURLConnection allows you to customize HTTPS server trust evaluation in much the same way as NSURLSession. There are two significant differences:

- You implement a different delegate method (in this case `-connection:willSendRequestForAuthenticationChallenge:`).
- When resolving a challenge, you must get the sender from the challenge (via the `-sender` method) and then call the appropriate method on that sender:

  - for challenges that you don't care about, call `-performDefaultHandlingForAuthenticationChallenge:`
  - if you want to deny a connection, call `-cancelAuthenticationChallenge:`
  - if you want to allow a connection, call `-useCredential:forAuthenticationChallenge:`, passing in a credential created with a trust object as described in [NSURLSession](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2oknkvetctivjvgskpjy)

__Note:__ Support for the `-connection:willSendRequestForAuthenticationChallenge:` delegate method was introduced in OS X 10.7 and iOS 5.0. If you need to support older systems, implement the `-connection:canAuthenticateAgainstProtectionSpace:` and `-connection:didReceiveAuthenticationChallenge:` delegate methods as well.

### CFHTTPStream

You can customize the HTTPS server trust evaluation for a CFHTTPStream in the same way you do for a CFSocketStream (see the [next section](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dizju6q2livkfgvcsivau2)). There is, however, one serious gotcha: by the time you're in a position to get a trust object in order to apply your custom trust evaluation, the CFHTTPStream has already sent your HTTP request to the server. So if the HTTP request is potentially confidential, this technique is not appropriate. In that case you should either move up a layer, and use NSURLSession, or down a layer, and use CFSocketStream directly.

__Note:__ NSURLSession does not suffer from this problem because it delivers the authentication challenge to the delegate before sending the request. It's not possible to do this in CFHTTPStream
(r. [11741769](rdar://problem/11741769))
.

### CFSocketStream

To customize the TLS server trust evaluation for a CFSocketStream, you should do the following:

1. use the `kCFStreamSSLValidatesCertificateChain` entry of the `kCFStreamPropertySSLSettings` property to disable server trust evaluation completely
2. once the stream has connected, but before you send any data or trust any data you receive, get the trust object from the stream via the `kCFStreamPropertySSLPeerTrust` property
3. use that trust object to implement whatever custom server trust evaluation you desire
4. either continue with the connection or close it, depending on your server trust evaluation

The primary gotcha here relates to step 2: when is the stream connected? It turns out that the trust object is not available at the time you get the stream open-completed event. To guarantee that the trust object is available, you must wait for the has-space-available event or the has-bytes-available event. See Table 2 for the details.

__Table 2__  Stream Events and Trust Object Availability

| NSStream Event | CFStream Event | Trust Object? |
| NSStreamEventOpenCompleted | kCFStreamEventOpenCompleted | not available |
| NSStreamEventHasSpaceAvailable | kCFStreamEventCanAcceptBytes | available |
| NSStreamEventHasBytesAvailable | kCFStreamEventHasBytesAvailable | available |

### Secure Transport

Secure Transport is the lowest-level TLS implementation on both OS X and iOS and, as you might expect, it has good support for custom TLS server trust evaluation. The procedure is as follows:

1. before starting the connection, call `SSLSetSessionOption` to set `kSSLSessionOptionBreakOnServerAuth`
2. if necessary, as discussed below, call `SSLSetEnableCertVerify` to disable the default server trust evaluation
3. run the Secure Transport handshake as per usual
4. when `SSLHandshake` returns `errSSLServerAuthCompleted`, call `SSLCopyPeerTrust` to get a trust object for the connection
5. use that trust object to implement whatever custom server trust evaluation you desire
6. either continue the Secure Transport handshake or shut down the connection

__Important:__ It is only necessary to call `SSLSetEnableCertVerify` on the Mac prior to OS X 10.8. On OS X 10.8 and later setting `kSSLSessionOptionBreakOnServerAuth` always disables the built-in trust evaluation. All versions of iOS behave like OS X 10.8 and thus `SSLSetEnableCertVerify` is not available on that platform at all.

[Back to Top](#)

## Resolving Specific Server Trust Evaluation Failures

The previous sections discussed the [type of server trust evaluation failures that might occur](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2vjzcekustkrau4ra), how you use a trust object to [implement your own custom server trust evaluation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2cifjusq2ukjkvgvcdkvjvit2njfnecvcjj5ha), and how you [get a trust object from the most frequently use APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2njfnekqkqjfjq). This section shows how all these pieces fit together: how you can use the techniques described earlier to resolve specific server trust evaluation failures while still maintaining some degree of security.

The bulk of this discussion assumes that you have encountered a server trust evaluation failure with one specific server, or a small, well-characterized group of servers. If you're creating a general-purpose program, one that might connect to a wide range of servers as specified by the user, you should skip forward to [Trust Exceptions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ukjkvgvcflbbukucujfhu4uy).

Before reading the rest of this section, there are two things to keep in mind:

- By far the easiest and most secure way to resolve server trust evaluation failures is to fix the server. You should only consider the techniques described in this section if it's not possible to fix the problem at the source.
- Most users don't have the skills necessary to make educated decisions on security matters. Presenting the user with an alert asking whether to allow a connection is almost always a mistake from a security perspective; it's very likely the user will choose whatever option that works, regardless of how insecure it is.

### Server Name Failures

If server trust evaluation fails because the server's DNS name does not match the DNS name in the certificate, you can work around the failure by overriding the DNS name in the trust object. To do this, call `SecPolicyCreateSSL` to create a new policy object with the correct server name and then call `SecTrustSetPolicies` to apply it to the trust object.

### Missing Intermediate Certificates

There are a number of ways that you can resolve a server trust evaluation failure caused by a missing intermediate certificate:

- The best approach is, as always, to fix the server. TLS requires that the server provide the client all certificates leading from the server certificate to the trusted anchor certificate, including any intermediate certificates (see Section 7.4.2 of RFC 5246). In many cases the absence of an intermediate certificate is just a minor oversight that the server admin can quickly correct.
- On OS X, if your program (or the user) adds the intermediate certificate to any keychain in the keychain search list, the trust object will use it automatically.
- On iOS, if your app adds the intermediate certificate to its keychain, the trust object will use it automatically.
- If all else fails, your program can obtain the intermediate certificate (bundle it with the program or download it from the Internet) and then create a new trust object that includes the union of the certificates from the existing trust object and your extra intermediate certificate. See Listing 5 for an example of this.

__Note:__ Adding arbitrary intermediate certificates to a trust object is always safe because their validity is cryptographically assured.

### Trusting One Specific Certificate

In some cases it's useful to treat a certificate as a simple identity token. For example, in a peer-to-peer program, X.509 trust evaluation is pointless because there is no central authority to issue certificates. However, you can still use TLS to securely communicate within that architecture. The procedure is as follows:

1. get a copy of the remote peer's certificate via a trusted channel of your own devising; you could have the remote user email you their certificate, put it on a USB stick, or whatever
2. get the server certificate from the trust object (pass an index of 0 to `SecTrustGetCertificateAtIndex`)
3. get the data for that server certificate (`SecCertificateCopyData`)
4. compare this to the certificate data you got in step 1; if they match, you're talking to the correct peer

### Custom Certificate Authority

If your server's certificate is issued by a certificate authority that is not trusted by the system by default, you can resolve the resulting server trust evaluation failure by including the certificate authority's root certificate in your program. The procedure is as follows:

1. include a copy of the certificate authority's root certificate in your program
2. once you have the trust object, create a certificate object from the certificate data (`SecCertificateCreateWithData`) and then set that certificate as a trusted anchor for the trust object (`SecTrustSetAnchorCertificates`)
3. `SecTrustSetAnchorCertificates` sets a flag that prevents the trust object from trusting any other anchors; if you also want to trust the default system anchors, call `SecTrustSetAnchorCertificatesOnly` to clear that flag
4. evaluate the trust object as per usual

### Self-Signed Certificates

Dealing with self-signed certificates is problematic because there are a variety of different reasons why people use a self-signed certificate. This section covers the most common cases.

#### Development

During development a self-signed certificate makes it easier to set up an TLS-based server for testing. This is a perfectly reasonable use of self-signed certificates, and a perfectly reasonable excuse for completely disabling TLS server trust evaluation.

__Warning:__ Make sure you re-enable server trust evaluation before shipping your product to users. Failure to do so will expose your users to active attackers. There have been some notable, and embarrassing, examples of developers leaving server trust evaluation disabled in production apps, and you don't want to be tarred with that particular brush.

While a self-signed certificate is a reasonable approach during development, there is a better way: create your own certificate authority (see below) and have it issue a certificate for your test server. You can then either a) hard-wired your certificate authority's root certificate into your app (as explained in [Custom Certificate Authority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2nkjhu6va)), or b) have each of your testers install your certificate authority's root certificate via the standard system user interface (Safari, Mail and configuration profiles on iOS, Keychain Access on OS X). This approach has the advantage that you don't need to disable server trust evaluation during development, which means that you can't forget to re-enable it when you ship a production build.

__Note:__ If you need to create your own certificate authority, there are a couple of ways to go about it:

- Certificate Assistant — This app is built in to OS X and supports a reasonably nice user interface for managing your own certificate authority; [Technical Note TN2326, 'Creating Certificates for TLS Testing'](https://developer.apple.com/technotes/tn2013/tn2326.html) has detailed instructions on how to use it.
- OpenSSL — The OpenSSL command line utility lets you create and manage your own certificate authority. This is rather complex (see the [man page](x-man-doc://ca) for the details) but there are lots of tutorials out there on the Internet.

#### Business Reasons

Some organizations use a self-signed certificate for production infrastructure because of business reasons. Perhaps the organization is unwilling to buy a certificate from a [trusted certificate authority](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2hjrhvgu2bkjmq) (although such certificates are not expensive by any means). Or perhaps the organization can acquire such a certificate, but there is a lot of red tape involved.

The obvious solution here is to resolve the business issue and move on. However, that's not always possible. In that case a self-signed certificate is an option, but it may not be the best option. In most cases it's better to use your own certificate authority, either purely for development purposes (see [Development](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2eivlektcpkbguktsu)) or also in production as well (see the note above). Using your own certificate authority has a number of advantages over a self-signed certificate:

- server changes — If the server changes in such a way that breaks server trust evaluation, your certificate authority can issue a new certificate that describes the new state of the server and clients will automatically trust it. For example, if you have to change the DNS name of the server, the new certificate can contain the new DNS name.
- reissue — If the server's certificate expires, your certificate authority can reissue it.
- revocation — Your certificate authority can support certificate revocation, either via __OCSP__ or a __CRL__.

#### Third Party Server

The previous sections have discussed the reasons why your organization should avoid self-signed certificates. However, what happens if your program communicates with a server out of your control, and it has a self-signed certificate? The best solution here is to work with the server vendor to get them to move to a certificate issued by a trusted certificate authority. If that's not possible, the next best option is to embed the server's certificate in your app and then use the approach described in [Trusting One Specific Certificate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dkvjvit2nincveva) to trust just that certificate.

### Trust Exceptions

The bulk of this technote assumes that you're trying to resolve a server trust evaluation failure with a specific server. But what happens if you're building a general purpose application, one that can connect to a wide variety of servers? The canonical example of this is a web browser, but there many others (email programs, RSS readers, and so on). In that case you can't apply a specific solution; you need a solution that works in general.

The best general-purpose approach is to do nothing. The default server trust evaluation has two critical advantages:

- it's easy to implement
- it's secure

The last point is critical: if there is a server trust evaluation failure and you provide the user with a way to bypass the security, the user will almost always choose whatever option that works, no matter how insecure it is. From a security perspective it's better to just fail, and then have the user pressure the server admin into fixing their server.

If you choose to ignore this advice (and you won't be alone; many popular general-purpose apps present the user with security questions, despite the fact that they don't have the skills to answer meaningfully), you can still take steps to minimize the risk.

The overall strategy here is:

1. try to connect to the server
2. if that fails with a server trust evaluation failure, inform the user about the problem (see [Displaying Certificates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ejfjvatcblfeu4r2divjfiskgjfbucvcfkm) and [Displaying Trust Results](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2ejfjvatcblfeu4r2ukjkvgvcsivjvktcukm) for details)
3. if the user decides to connect anyway, remember that decision and continue with the connection
4. later on, if you encounter the same server trust evaluation failure, ignore the problem and connect anyway

The tricky part is step 4. How can you tell that this is the same failure? If you get this wrong, you risk compromising the user's security above and beyond what they've agreed to. Consider the following sequence:

1. the user connects to a server with an expired certificate
2. your program detects this and asks the user to confirm that they really want to connect
3. the user agrees, so your program remembers that decision and connects to the server
4. later on the user moves to a hostile network, one that includes an active attacker that implements an impostor server; they go to connect to the server again
5. your program connects to the impostor server; it detects the server trust evaluation failure, which is good, but it sees that the user has agreed to connect to the server despite such problems, and connects anyway

The problem here is that your program has now connected to an impostor server, even though the user only agreed to ignore an expired certificate.

You can address this issue using trust exceptions. When the user agrees to connect to a server your program can ask the trust object for a trust exception (`SecTrustCopyExceptions`). This records the information necessary to get around the current trust evaluation failure. In the future, when your program sees a trust evaluation failure for the same server, it can apply the exception to the trust object (`SecTrustSetExceptions`). If that resolves the server trust evaluation failure, it can safely continue with the connection. If not, it must ask the user to agree to an additional trust exception.

__Note:__ On OS X the trust exception API is only available on OS X 10.9 and later. You can do equivalent things on earlier systems (use `SecTrustGetResult` to get detailed trust results and record information about the failures you're seeing), but it's a lot more work.

[Back to Top](#)

## Enforcing Stricter Server Trust Evaluation

Customizing server trust evaluation is not just about working around problems; you can also use it to make security tighter. If you're working on a high-security program, you might want to go beyond the default server trust evaluation and add some more checks of your own.

For example, you might want to not only check that the server's certificate was issued by a trusted certificate authority, but that it was issued by a specific certificate authority (a technique known as __certificate authority pinning__). It's easy to accomplish this using a trust object. The procedure is as follows:

1. include a copy of the certificate authority's root certificate in your program
2. once you have the trust object, create a certificate object from the certificate data (`SecCertificateCreateWithData`) and then set that certificate as the only trusted anchor for the trust object (`SecTrustSetAnchorCertificates`)
3. evaluate the trust object; if the evaluation succeeds, you know that the server's certificate is valid and was issued by the certificate authority that you specified

Certificate authority pinning is just one example of how you can enforce stricter server trust evaluation. There are many other checks that you might consider. For example:

- You can implement __certificate pinning__ by extracting the public key from the server's certificate using `SecTrustCopyPublicKey`.
- You could check for the presence of certain attribute values or extensions in the certificate; on OS X the `SecCertificateCopyValues` routine can be very helpful when implementing such checks.
- `SecTrustCopyResult` lets you determine whether __extended validation__ was done as part of the trust evaluation.
- `SecPolicyCreateRevocation` lets you create a security policy that specifically checks for certificate revocation (for example, via OCSP or a CRL).

[Back to Top](#)

## Hints and Tips

This section describes some general hints and tips when dealing with customizing server trust evaluation.

### SecTrustEvaluate Can Block

There are two situations where `SecTrustEvaluate` may need to access the network in order to complete its job:

- when downloading intermediate certificates
- when determining whether a certificate has been revoked (via a OCSP or CRL)

These network operations have relatively short timeouts, but they still make `SecTrustEvaluate` unsuitable for use on the main thread, especially on iOS. If you need to call `SecTrustEvaluate` from the main thread, you have three options:

- you can use `SecTrustEvaluateAsync` (introduced in OS X 10.7 and iOS 7.0)
- you can use `SecTrustSetNetworkFetchAllowed` to disable network access for your trust object (introduced in OS X 10.9 and iOS 7.0)
- you can use a concurrency primitive (for example, GCD, an NSOperation, or a thread) to run `SecTrustEvaluate` on a secondary thread

### Investigating Hard-To-Debug Trust Evaluation Failures

Sometimes it's hard to work out exactly why trust evaluation is failing. Your first step should always be to work through the points described in [Common Failures](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgayteobygqwugsbrfvjukq2dj5gu2t2oizaustcvkjcvg). If you still can't figure out the problem, there are a few more tricks you can try:

- print the result of `SecTrustCopyResult`
- print the result of `SecTrustCopyProperties`
- examine the trust exception data (as returned by `SecTrustCopyExceptions`)

__Warning:__ The format and contents of the trust exception data is not considered API. This technique is for debugging purposes only.

The first two points need no further explanation. The last point is a bit tricky. If you look inside the data, you'll see that it's actually a binary property list. If you save the data to a file with the `.plist` extension and then open it with Xcode (or your favorite property list editor), you may find useful hints as to why the trust evaluation failed.

### Displaying Certificates

In some circumstances it may be useful to display certificates to a user. For example, an advanced user might want to manually confirm the identity of the server that your app is communicating with. OS X has high-level APIs for this:

- SFCertificateView is an NSView subclass that displays a certificate
- SFCertificatePanel is a panel that displays one or more certificates; it can be used independently or as a sheet

In general you should use these high-level APIs but, if you want to display your own user interface, you can use low-level APIs (specifically, `SecCertificateCopyValues`) to extract details from the certificate and build your own UI from that.

iOS does not have a high-level API for displaying certificates. If you want to do this, you will have to build your own user interface. Doing that is non-trivial because iOS has only limited APIs for getting information from a certificate
(r. [11004183](rdar://problem/11004183))
; in fact, the only thing you can do is get a user-visible name for the certificate by calling `SecCertificateCopySubjectSummary`. Beyond that, you will need your own code to parse the certificate.

### Displaying Trust Results

The advice given throughout this document is that you should not ask users security questions that they are not qualified to answer. If you ignore that advice then you'll probably want a way to display the results of a failed trust evaluation to the user. OS X has a high-level API for this, SFCertificateTrustPanel.

There is no equivalent high-level API on iOS, but both platforms allow you to get detailed information about trust evaluation failures. You can call `SecTrustCopyResult`, which returns information about the overall trust evaluation, and `SecTrustCopyProperties`, which returns information about each certificate in the path leading from the server certificate to the trusted anchor. You can use this information to populate your own trust results UI.

__Note:__ These routines were added in iOS 7.0 and recent versions of OS X (10.9 for `SecTrustCopyResult`, 10.7 for `SecTrustCopyProperties`). On older versions of OS X you can use the older, now-deprecated `SecTrustGetResult` routine and its closely-related companions. Alas, on older versions of iOS there is no good way to get this information.

[Back to Top](#)

## Appendix A: Common Server Trust Evaluation Errors

Table 3 lists some errors you're likely to get back in the face of server trust evaluation failures.

__Table 3__  Common Server Trust Evaluation Errors

| Error Domain | Error Code | Error Code Value |
| NSURLErrorDomain | NSURLErrorSecureConnectionFailed | -1200 |
| NSURLErrorDomain | NSURLErrorServerCertificateHasBadDate | -1201 |
| NSURLErrorDomain | NSURLErrorServerCertificateUntrusted | -1202 |
| NSURLErrorDomain | NSURLErrorServerCertificateHasUnknownRoot | -1203 |
| NSURLErrorDomain | NSURLErrorServerCertificateNotYetValid | -1204 |
| kCFErrorDomainCFNetwork | kCFURLErrorSecureConnectionFailed | -1200 |
| kCFErrorDomainCFNetwork | kCFURLErrorServerCertificateHasBadDate | -1201 |
| kCFErrorDomainCFNetwork | kCFURLErrorServerCertificateUntrusted | -1202 |
| kCFErrorDomainCFNetwork | kCFURLErrorServerCertificateHasUnknownRoot | -1203 |
| kCFErrorDomainCFNetwork | kCFURLErrorServerCertificateNotYetValid | -1204 |
| NSOSStatusErrorDomain | errSSLXCertChainInvalid | -9807 |
| NSOSStatusErrorDomain | errSSLUnknownRootCert | -9812 |
| NSOSStatusErrorDomain | errSSLNoRootCert | -9813 |
| NSOSStatusErrorDomain | errSSLCertExpired | -9814 |
| NSOSStatusErrorDomain | errSSLCertNotYetValid | -9815 |
| NSOSStatusErrorDomain | errSSLHostNameMismatch | -9843 |

[Back to Top](#)

## Appendix B: Glossary

If you're not familiar with TLS, and specifically X.509 public key infrastructure, many of the terms used in this technote may be daunting. This glossary explains these terms and their specific meaning in this context.

- __authentication challenge__ — An HTTP or HTTPS response indicating that the server requires authentication information from the client. Foundation represents this with the `NSURLAuthenticationChallenge` class, and it also uses this infrastructure to support custom HTTPS server trust evaluation. An authentication challenge originates from a protection space.
- __certificate__ — See digital certificate.
- __certificate authority__ — An organization responsible for issuing certificates. Each certificate authority publishes one or more root certificates for the purposes of evaluating trust on certificates issued by that authority. See also trusted certificate authority.
- __certificate authority pinning__ — A stricter form of trust evaluation that requires that the server's certificate be issued by a specific certificate authority (not just any trusted certificate authority).
- __certificate pinning__ — A stricter form of trust evaluation that requires that the server use a specific certificate or a certificate containing a specific public key.
- __certificate revocation list__ (also __CRL__) — A list of certificates that have been revoked, and thus should not be trusted.
- __CRL__ — See certificate revocation list.
- __digital certificate__ (most commonly just __certificate__) — A data structure that uses a digital signature to associate information about an entity with a public key. In TLS, all digital certificates are actually X.509 digital certificates. See also subject, issuer, self-signed certificate, server certificate, intermediate certificate, root certificate and trusted anchor.
- __digital identity__ (also __identity__) — The combination of a certificate and the private key associated with the public key embedded in that certificate.
- __digital signature__ — A data structure that proves the authenticity of some other data. In public key cryptography, you can verify a digital signature with a public key and be guaranteed that it was created with the associated private key.
- __extended validation__ — A strict trust evaluation policy used for [extended validation certificates](http://en.wikipedia.org/wiki/Extended_Validation_Certificate).
- __HTTP__ — See Hypertext Transport Protocol.
- __HTTPS__ — HTTP over TLS. See [RFC 2818](http://www.ietf.org/rfc/rfc2818.txt).
- __HTTPS server trust evaluation__ — HTTPS is HTTP over TLS, so this is equivalent to TLS server trust evaluation.
- __Hypertext Transport Protocol__ (also __HTTP__) — Really? You're looking this up in the glossary!?! Anyway, see [RFC 2616](http://www.ietf.org/rfc/rfc2616.txt).
- __identity__ — See digital identity.
- __intermediate certificate__ — A certificate that exists on the path of issuers between a server certificate and a root certificate.
- __issuer__ — For an X.509 digital certificate, this is the entity that signed the certificate.
- __OCSP__ — See Online Certificate Status Protocol.
- __Online Certificate Status Protocol__ (also __OCSP__) — A protocol to check whether a digital certificate has been revoked. See [RFC 2560](http://www.ietf.org/rfc/rfc2560.txt).
- __private key__ — Within public key cryptography, this is the key used to decrypt data or generate a digital signature.
- __protection space__ (also __realm__) — An HTTP or HTTPS server, or an area on such a server, that requires authentication. Within Foundation this is represented by the `NSURLProtectionSpace` class. See also authentication challenge.
- __public key__ — Within public key cryptography, this is the key used to encrypt data or verify a digital signature.
- __public key cryptography__ — A cryptographic system that uses two separate keys, a public key to encrypt and a private key to decrypt. A private key can also be used to generate a digital signature, which a public key can verify.
- __public key infrastructure__ — A mechanism for managing public and private keys, and specifically the way that a public key is embedded within a certificate. TLS uses the X.509 public key infrastructure.
- __realm__ — See protection space.
- __root certificate__ — A self-signed certificate provided by a certificate authority for the purposes of evaluating trust on certificates issued by that authority.
- __Secure Sockets Layer__ (also __SSL__) — A predecessor to TLS.
- __self-signed certificate__ — An X.509 digital certificate where the subject and the issuer are the same. Root certificates are self-signed, but anyone can create their own self-signed certificate.
- __server certificate__ — The X.509 digital certificate provided by a TLS server. The TLS protocol ensures that the server holds the private key associated with the public key embedded in this certificate. It's this certificate that's the subject of TLS server trust evaluation.
- __server trust evaluation__ — The trust evaluation mechanism used by a client to determine whether it trusts a server. In this context, this is a synonym for TLS server trust evaluation.
- __SSL__ — See Secure Sockets Layer.
- __subject__ — For an X.509 digital certificate, this is the entity that is identified by the certificate. In TLS the subject of a server certificate is typically the server's DNS name.
- __TLS__ — See Transport Layer Security.
- __TLS server trust evaluation__ — Trust evaluation that consists of X.509 certificate trust evaluation followed by additional TLS-specific checks. Operates on the server certificate.
- __Transport Layer Security__ (also __TLS__) — A security protocol in common use on the Internet. The successor to SSL. See [RFC 5246](http://www.ietf.org/rfc/rfc5246.txt).
- __trust evaluation__ — This is the process by which an entity decides whether to trust another entity, based on the other entity's digital certificate. See also TLS server trust evaluation.
- __trusted anchor__ — A certificate that the system trusts implicitly. This is typically a certificate authority's root certificate that has been baked into the system, but in some situations you can programmatically mark any certificate as a trusted anchor.
- __trusted certificate authority__ — A certificate authority whose root certificate is baked into the system as a trusted anchor.
- __valid date range__ — For an X.509 digital certificate, this is the range of dates during which the certificate should be considered valid.
- __verify date__ — In X.509 certificate trust evaluation, this is the date at which the trust evaluation is deemed to have occurred. This is relevant because each certificate includes a valid date range.
- __X.509 certificate__ — See X.509 digital certificate.
- __X.509 certificate trust evaluation__ — Trust evaluation based on X.509 certificates. See also TLS server trust evaluation.
- __X.509 digital certificate__ (also __X.509 certificate__) — A specific type of digital certificate. This is the only type of certificate that's relevant to TLS.
- __X.509 public key infrastructure__ — The public key infrastructure used by TLS. See [RFC 5280](http://www.ietf.org/rfc/rfc5280.txt).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-07-29 | Corrected the guidance in the "HTTP Live Streaming" section (r. 16538960). Fixed the column ordering in the table in Appendix A (r. 16057325). |
| 2014-03-13 | Updated for Security API changes in iOS 7 and OS X 10.9. Added the NSURLSession section. Added three news hints and tips. Updated to reference CustomHTTPProtocol sample code and TN2326. Expanded the "Enforcing Stricter Server Trust Evaluation" section. Other minor editorial changes. |
| 2013-02-07 | Clarified the nature of +setAllowsAnyHTTPSCertificate:forHost:. |
| 2012-10-10 | New document that describes how you can resolve HTTPS server trust evaluation, for example, to work with a server with a missing intermediate certificate. |

