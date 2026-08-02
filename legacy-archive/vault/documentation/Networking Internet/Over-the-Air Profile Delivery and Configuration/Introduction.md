---
title: Over-the-Air Profile Delivery and Configuration
apple_id: TP40009505
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/iPhoneOTAConfiguration/Introduction/Introduction.html
archived_at: '2026-07-18T01:33:03.667339Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Over-the-Air%20Profile%20Delivery%20Concepts.md)

# Introduction

A configuration profile is an XML file that allows you to distribute configuration information to iOS-based devices. If you need to configure a large number of devices or to provide lots of custom email settings, network settings, or certificates to a large number of devices, configuration profiles are an easy way to do it.

An iOS configuration profile contains a number of settings that you can specify, including:

- Passcode policies
- Restrictions on device features (disabling the camera, for example)
- Wi-Fi settings
- VPN settings
- Email server settings
- Exchange settings
- LDAP directory service settings
- CalDAV calendar service settings
- Web clips
- Credentials and keys
- Advanced cellular network settings

There are four ways to deploy configuration profiles:

- By physically connecting the device
- In an email message
- On a webpage
- Using over-the air configuration as described in this document

iOS supports both encrypted and unencrypted profiles. Encrypted profiles guarantee data integrity and protect sensitive policy information from prying eyes. Encrypted configuration profiles are signed with the public key associated with a device’s identity certificate. This public key can be obtained using over-the-air enrollment.

iOS over-the-air enrollment and configuration provides an automated way to configure devices securely within the enterprise. This process provides IT with assurance that only trusted users are accessing corporate services and that their devices are properly configured to comply with established policies. Because configuration profiles can be both encrypted and locked, the settings cannot be removed, altered, or shared with others.

More importantly, for geographically distributed enterprises, an over-the-air profile service allows you to enroll iOS-based devices without physically to connecting them.

The profile service described in this document creates a configuration on the fly; the device then downloads that configuration. The device remembers the enrollment URL so that it can update its configuration from the server in the future if the configuration expires or a VPN connection failure occurs.

This document describes the over-the-air enrollment process. With this process, administrators can instruct users to begin the process of enrollment by providing a URL via email or SMS notification. When users agree to the profile installation, their devices are automatically enrolled and configured in a single session.

This document takes you through the process of setting up a server to deliver encrypted custom profiles to iOS-based devices over the air.

- [Over-the-Air Profile Delivery Concepts](Over-the-Air%20Profile%20Delivery%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmznknltc) explains the terminology and basic security concepts involved in over-the-air enrollment and profile delivery.
- [Creating a Profile Server for Over-The-Air Enrollment and Configuration](Creating%20a%20Profile%20Server%20for%20Over-The-Air%20Enrollment%20and%20Configuration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqmrnknlte) describes the reference implementation of a profile server, piece by piece, in chronological order of execution, from device authentication and enrollment to profile delivery.
- [Configuration Profile Examples](Configuration%20Profile%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tkmbvfvbuqnbnknltc) provides sample profiles and code to generate profiles.

This document assumes a basic knowledge of Ruby programming, XML, property lists, and OpenSSL.

For more information, see the following pages:

- Cisco: [Digital Certificates PKI for IPSec VPNs](https://cisco.hosted.jivesoftware.com/docs/DOC-3592) (PDF)
- Wikipedia: [Public key infrastructure](http://en.wikipedia.org/wiki/Public_key_infrastructure)
- [IETF SCEP protocol specification](http://tools.ietf.org/internet-drafts/draft-nourse-scep-20.txt)

Additional information and resources for iOS-based devices in the enterprise are available at [http://www.apple.com/iphone/business/](http://www.apple.com/iphone/business/) and in the _[Configuration Profile Reference](https://developer.apple.com/library/archive/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010206)_. This appendix specifies the format of `.mobileconfig` files for developers who want to create their own tools.

[Next](Over-the-Air%20Profile%20Delivery%20Concepts.md)

