---
title: Identifying the Source of Blocked Connections
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/identifying-the-source-of-blocked-connections
source_url: 'https://developer.apple.com/documentation/security/identifying-the-source-of-blocked-connections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/identifying-the-source-of-blocked-connections.json'
content_hash: 'sha256:ae9cc90306008e96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Preventing Insecure Network Connections](preventing-insecure-network-connections.md)

# Identifying the Source of Blocked Connections

<sub>Article</sub>

Figure out why App Transport Security denies a network connection.

## Overview

If your app experiences connectivity problems that you think might be related to App Transport Security (ATS), be sure that:

- You’re using high-level network frameworks and secure URLs, as described in [Prefer High-Level Frameworks in Your App](preventing-insecure-network-connections.md#Prefer-High-Level-Frameworks-in-Your-App).
- Your server is properly configured. Use the `nscurl` command line tool on your Mac to check how the server’s configuration affects ATS behavior.

### Check Combinations of ATS Exceptions

The `nscurl` command accepts the `--ats-diagnostics` flag that asks it to check how a particular server responds to combinations of ATS exceptions. For example, you can test the canonical example web site:

```sh
$ /usr/bin/nscurl --ats-diagnostics --verbose https://example.com
```

In addition to running with no exceptions at all, the tool tests the global exception keys in [NSAppTransportSecurity](../bundleresources/information-property-list/nsapptransportsecurity.md#Global-Exceptions), as well as a variety of combinations of the exception domain keys [NSExceptionMinimumTLSVersion](../bundleresources/information-property-list/nsexceptionminimumtlsversion.md), [NSExceptionRequiresForwardSecrecy](../bundleresources/information-property-list/nsexceptionrequiresforwardsecrecy.md), [NSExceptionAllowsInsecureHTTPLoads](../bundleresources/information-property-list/nsexceptionallowsinsecurehttploads.md), and [NSExceptionRequiresNIAPTLSPackageVersion](../bundleresources/information-property-list/nsexceptionrequiresniaptlspackageversion.md). `nscurl` outputs the results of all these tests to the terminal:

```console
Starting ATS Diagnostics

Configuring ATS Info.plist keys and displaying the result of HTTPS loads to https://example.com.
A test will "PASS" if URLSession:task:didCompleteWithError: returns a nil error.
================================================================================

Default ATS Secure Connection
---
ATS Default Connection
ATS Dictionary:
{
}
Result : PASS
---

================================================================================

Allowing Arbitrary Loads

---
Allow All Loads
ATS Dictionary:
{
    NSAllowsArbitraryLoads = true;
}
Result : PASS
---

...
```

### Look for Basic Security Failures

If globally allowing arbitrary loads fails, the problem isn’t related to ATS. For example, if the server’s certificate doesn’t match the DNS name of the server, the connection fails default server trust evaluation before ATS has a chance to impose its extended security checks:

```console
...

Allowing Arbitrary Loads

---
Allow All Loads
ATS Dictionary:
{
    NSAllowsArbitraryLoads = true;
}
Result : FAIL
Error : Error Domain=NSURLErrorDomain Code=-1202 "The certificate for this server is invalid...

...
```

When you see this failure, check that your certificate meets the default server trust evaluation requirements described in [Ensure the Network Server Meets Minimum Requirements](preventing-insecure-network-connections.md#Ensure-the-Network-Server-Meets-Minimum-Requirements). For example, make sure the certificate matches the DNS name of the server and that the certificate isn’t expired.

### Consider Specific ATS Exceptions

If the ATS default test fails but the arbitrary loads test passes, you might need to reconfigure your server. Use the remaining tests to help pinpoint the problem. For example, consider the test with the following exceptions dictionary:

```console
{
    NSExceptionDomains =     {
        "example.com" =         {
            NSExceptionRequiresForwardSecrecy = false;
        };
    };
}
```

If simply disabling forward secrecy results in a passing test, you need to reconfigure your server to support perfect forward secrecy (PFS) through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange. If you can’t do that, you might need to add the [NSExceptionRequiresForwardSecrecy](../bundleresources/information-property-list/nsexceptionrequiresforwardsecrecy.md) exception to your app instead, as described in doc:preventing-insecure-network-connections#Configure-Exceptions-Only-When-Needed;-Prefer-Server-Fixes.
