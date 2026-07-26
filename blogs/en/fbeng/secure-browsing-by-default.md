---
title: Secure browsing by default
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2013/07/31/android/secure-browsing-by-default/'
original_language: en
published: 2013-07-31
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35ff497fccf30b9a'
translated: false
---

> 原文：[Secure browsing by default](https://engineering.fb.com/2013/07/31/android/secure-browsing-by-default/)　·　Meta Engineering — iOS

We now use https by default for all Facebook users. This feature, which we first introduced as an [option two years ago](https://www.facebook.com/blog/blog.php?post=486790652130), means that your browser is told to communicate with Facebook using a secure connection, as indicated by the “https” rather than “http” in https://www.facebook.com. This uses [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security), formerly known as Secure Sockets Layer (SSL), and makes the communication between your browser and Facebook servers more secure.

More than a third of users had enabled the feature following its introduction, while we worked behind the scenes to make it better. We’ve focused on making it faster throughout the world and improving its compatibility with platform applications.

![](https://engineering.fb.com/wp-content/uploads/2013/07/Fmb_DABkBmcS2qcBAHEM7ExuPQkAAAM.png)

Now that https is on by default, virtually all traffic to www.facebook.com and 80% of traffic to m.facebook.com uses a secure connection. Our native apps for Android and iOS have long used https as well.

## Migrating to https by default

Switching to https is more complicated than it might seem. It’s not simply a matter of redirecting from http://www.facebook.com to https://www.facebook.com. We thought it’d be useful to walk through some changes we’ve already made and some improvements that we’re still working on.

- **The secure attribute for authentication cookies.** By default, web browsers send all cookies, including authentication cookies, on insecure requests. We’ve implemented the secure attribute in the Set-Cookie header, which instructs the browser to only send these cookies on https requests so the cookies won’t be visible on the network if you happen to visit an insecure link to Facebook.
- **An insecure indicator cookie.** Once authentication cookies are sent only on secure requests, insecure requests become ambiguous — it’s not obvious if there’s no authenticated user or if there is a user with a secure session. To address this, we added a new cookie named “csm” that is sent on all requests. This cookie’s value is unimportant. When the server sees a csm cookie but no authentication cookies, it redirects to https so it can see the authentication cookies.
- **Third-party platform applications and https.** Understandably, browsers don’t render insecure content as part of an https page. Because we embed third-party platform applications inside of iframes, we needed to get all platform applications to upgrade their apps to support https. This was treated as a [90-day breaking change for platform applications](https://developers.facebook.com/blog/post/499/), and we actually gave developers 150 days to get a certificate and upgrade their application to https.
- **Controlling referrer headers.** Browsers traditionally omit the referrer when navigating from https to http. When you click on an external link, we’d like the destination site to know you came from Facebook while not learning your user id or other sensitive information. On most browsers, we redirect through an http page to accomplish this, but on Google Chrome we can skip this redirect by using their [meta referrer feature](https://www.facebook.com/note.php?note_id=10151070897728920).
- **Migration and in-flight upgrades.** We tried a couple of different migration strategies before settling on a two-part process. First, update a user’s default setting to https, which will use https for new logins. Second, upgrade their existing sessions to https in-flight while they use Facebook. The former uses https for new logins while the latter ensures that even existing sessions are migrated without needing to sign a user out. On requests where we think this is safe, we redirect your browser to https and update your authentication cookies with a different session secret and the secure attribute set. We only do this on a fraction of qualifying requests, and a request only qualifies if it is a GET request with relatively stale cookies. These constraints help avoid race conditions that might otherwise invalidate your session if there are two requests in-flight at once.

The graph below shows the adoption of https on Facebook since April 2011. Adoption reached about 35% organically before we started actively migrating users to https by default.

![](https://engineering.fb.com/wp-content/uploads/2013/07/Fnf_DAAw317idZ0BAHX7InNuPQkAAAM.png)

- **Ineligible devices and insecure sessions.** Some mobile phones and mobile carrier gateways don’t fully support https. While we’re working with the vendors of these products, we didn’t want to leave https off entirely for affected users. Instead, we only downgrade the session on an ineligible device while continuing to use https on browsers and phones where https is properly supported. This downgrade process leverages the same in-flight migration logic as https upgrades. We’ve seen issues only with some feature phones; desktop browsers and smartphones all seem to work fine.

## Performance

One of the biggest challenges in enabling https by default is performance. In addition to the network round trips necessary for your browser to talk to Facebook servers, https adds additional round trips for the handshake to set up the connection. A full handshake requires two additional round trips, while an abbreviated handshake requires just one additional round trip. An abbreviated handshake can only follow a successful full handshake.

For example, if you’re in Vancouver, where a round trip to Facebook’s Prineville, Oregon, data center takes 20ms, then the full handshake only adds about 40ms, which probably isn’t noticeable. However, if you’re in Jakarta, where a round trip takes 300ms, a full handshake can add 600ms. When combined with an already slow connection, this additional latency on every request could be very noticeable and frustrating. Thankfully, we’ve been able to avoid this extra latency in most cases by upgrading our infrastructure and using abbreviated handshakes.

- **Leveraging an edge network.** Edge networks help reduce latency by modifying our infrastructure to be closer to our users. We have built and deployed custom load balancers around the world that forward requests from users over existing https connections to our data centers and use various techniques to speed up the traffic. We plan on further improving our edge network so we can give our users the fastest experience possible.
- **Reducing full handshakes.** Abbreviated handshakes save a full round trip over the full TLS handshake, so we want to use them whenever possible. We maximize these session resumption rates by using a shared, local cache for traditional TLS sessions,and also by supporting TLS session tickets described in [RFC 5077](http://www.ietf.org/rfc/rfc5077). The latter require no server state.

## Ongoing work

We’re continuing to build on our implementation of https and have a few improvements that we’re planning to launch this fall:

- **2048-bit RSA keys.**Although there’s no generally known case of an actual 1024-bit RSA key being broken, moving to 2048-bit RSA keys further increases the security associated with TLS sessions, and there’s [industry-wide agreement](https://www.cabforum.org/Baseline_Requirements_V1_1_3.pdf) to complete the move by the end of 2013.
- **Elliptic Curve Cryptography.** This is just as secure as traditional forms of asymmetric cryptography but uses smaller keys and is more efficient to calculate. More importantly, it’s now supported by newer versions of modern browsers.
- **Elliptic Curve Ephemeral Diffie-Hellman (ECDHE) key exchange.** Traditional use of RSA in TLS connections encrypts the key material with the server’s long-lived RSA key. If someone were to capture traffic today and then get access to the private RSA key years later, they could decrypt that previously recorded traffic. By contrast, [ECDHE](https://www.imperialviolet.org/2011/11/22/forwardsecret.html) uses keys that are ephemeral to each TLS session. As a result,there is no long-lived key that can be used to later decrypt recorded traffic.This property is known as Perfect Forward Secrecy.
- **Certificate Pinning.** A server’s certificate identifies it to your browser. Browsers trust dozens of different Certification Authorities (CAs) who can issue certificates on behalf of any site. Some of these CAs are well-known while others have suffered security breaches or belong to defunct companies whose security is unknown. Certificate pinning is a mechanism for specifying the CAs a site actually uses and was [originally introduced](https://www.imperialviolet.org/2011/05/04/pinning.html) in Chrome 13. We’re actively testing pinning in Facebook mobile apps and plan to use it in browsers as well.
- **HTTP Strict TransportSecurity (HSTS).** This instructs your browser to interact with a site using only [https connections](http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security). Our use of HSTS today is limited for two reasons. First, we need to support users who have opted out of https. Second, on browsers without a mechanism like meta referrer, we redirect through http to control referrer headers. We plan to use HSTS more widely once we remove the https opt-out.

Turning on https by default is a dream come true, and something Facebook’s Traffic, Network, Security Infrastructure, and Security teams have worked on for years. We’re really happy with how much of Facebook’s traffic is now encrypted and are even more excited about the future changes we’re preparing to launch.

_Scott Renfro is a software engineer who works in Facebook London’s growing Security Infrastructure team, where they write code to make Facebook more secure._
